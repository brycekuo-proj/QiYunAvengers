#!/usr/bin/env python3
"""Build a quota-efficient ChatGPT Desktop generation-job layer over ART_QUEUE.

The canonical 1,575 asset queue is never rewritten.  This builder groups compatible
source-generation tasks into fewer raster calls, while every child asset is still
split back to its original source_path and passed through queue_postprocess.py.
"""
from __future__ import annotations

from collections import defaultdict, Counter
from pathlib import Path
from datetime import datetime, timezone
import json, math, re

from chatgpt_desktop_images import _local_design_context

ROOT = Path(__file__).resolve().parents[2]
QDIR = ROOT / "art/production/queue"
BDIR = ROOT / "art/production/batches"
QUEUE = QDIR / "ART_QUEUE.json"
STATE = QDIR / "queue_state.json"
OUT = BDIR / "GENERATION_JOBS.json"
PROMPTS = BDIR / "prompts"

COMPLETE = {"runtime_ready", "complete_reference", "superseded_side_camera"}
STATIC_CAPS = {"icons": 12, "ui": 6, "traps": 4, "maps": 2}


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def chunk(xs, n):
    return [xs[i:i+n] for i in range(0, len(xs), n)]


def semantic_instruction(task: dict) -> str:
    p = ROOT / task["prompt_file"]
    if not p.exists():
        return task.get("visual_brief") or task["name"]
    text = p.read_text(encoding="utf-8", errors="replace")
    # Preserve the authored task-specific instruction while dropping backend/save boilerplate.
    m = re.search(r"\n(Create .*?)(?=\n\nAfter generation|\Z)", text, flags=re.S)
    if m:
        return " ".join(m.group(1).split())
    return task.get("visual_brief") or task["name"]


def macro_grid(count: int, kind: str) -> list[int]:
    if kind == "icons":
        return [4, 3] if count > 8 else ([4, 2] if count > 4 else [count, 1])
    if kind == "ui":
        return [3, 2] if count > 3 else [count, 1]
    if kind == "traps":
        return [2, 2] if count > 2 else [count, 1]
    if kind == "maps":
        return [2, 1]
    # Short animation actions: stack up to 3 action-panels vertically so each
    # child keeps its own nested grid and temporal ordering.
    return [1, count]


def aspect_hint(cols: int, rows: int) -> str:
    if rows >= cols * 2:
        return "portrait / tall canvas"
    if cols >= rows * 2:
        return "landscape / wide canvas"
    return "square canvas"


def batch_prompt(job: dict, task_by_id: dict[str, dict]) -> str:
    cols, rows = job["grid"]
    lines = [
        "You are generating ONE raster CONTACT SHEET for the game 《氣運復仇者》.",
        "This single image will be deterministically split by the local pipeline into multiple existing asset tasks.",
        "Use the ordinary ChatGPT Desktop Create Image tool in this same conversation. Output image only; no prose in the raster.",
        "",
        "NON-NEGOTIABLE LAYOUT:",
        f"- Overall layout: exactly {cols} columns × {rows} rows of equal OUTER PANELS, filled left-to-right then top-to-bottom.",
        f"- Prefer a {aspect_hint(cols, rows)} so every outer panel has useful resolution.",
        "- Keep a clean pure-white exterior background and generous blank gutters between outer panels.",
        "- Do NOT draw panel borders, labels, numbers, captions, signatures, watermarks or UI text.",
        "- Every requested child must stay completely inside its own outer panel; never overlap panels.",
        "- Preserve each child's exact nested frame grid when it has multiple frames. Those nested frames must remain consecutive time-ordered animation keyframes, not unrelated poses.",
        "- For gameplay characters/enemies/bosses: strict horizontal side-profile facing screen-right, one eye dominant, no front-facing/front-three-quarter stance; preserve all documented identity/costume details and rounded mitten/饅頭 hands.",
        "- Original project style only: no studs, interlocking brick traits, visible toy joints, C-shaped gripping hands, or generic mascot simplification.",
        "",
        "OUTER PANELS IN EXACT ORDER:",
    ]
    for idx, aid in enumerate(job["children"], 1):
        t = task_by_id[aid]
        req = "; ".join(t.get("requirements") or []) or "docs 03–17 + docs/19"
        refs = ", ".join(t.get("reference_paths") or []) or "none"
        lines += [
            f"{idx}. {aid} — {t['name']}",
            f"   category={t['category']}; frames={t['frame_count']}; nested_grid={t.get('grid',[1,1])[0]}x{t.get('grid',[1,1])[1]}; alpha={t.get('alpha','transparent')}",
            f"   authority={req}; identity_reference={refs}",
            f"   instruction={semantic_instruction(t)}",
        ]
    # Carry the same local design authority used by solo generation into the
    # synthetic batch prompt.  Deduplicate repeated doc sections so atlas jobs
    # stay compact enough for Desktop Chat while retaining concrete design data.
    contexts = []
    seen_context = set()
    context_chars = 0
    for aid in job["children"]:
        t = task_by_id[aid]
        key = tuple(t.get("requirements") or [])
        if key in seen_context:
            continue
        seen_context.add(key)
        ctx = _local_design_context(t, max_chars=3500)
        if ctx and context_chars < 12000:
            room = 12000 - context_chars
            contexts.append(ctx[:room])
            context_chars += min(len(ctx), room)
    if contexts:
        lines += ["", "LOCAL DESIGN AUTHORITY (resolved from repository docs; mandatory):", ""]
        for ctx in contexts:
            lines.append(ctx)
            lines.append("")
    lines += [
        "FINAL CHECK: exact outer-panel count/order, no missing child, no extra child, no text, no cropping, correct nested frame count/order, consistent identity, correct side-facing gameplay camera where applicable, clean white gutters/background.",
    ]
    return "\n".join(lines) + "\n"


def main():
    queue = load(QUEUE)
    state = load(STATE)
    tasks = queue["tasks"]
    if len(tasks) != 1575:
        raise SystemExit(f"refusing: canonical queue count is {len(tasks)}, expected 1575")
    task_by_id = {t["id"]: t for t in tasks}
    remaining = [t for t in tasks if state["tasks"].get(t["id"], {}).get("status", "queued") not in COMPLETE]
    used: set[str] = set()
    jobs: list[dict] = []

    def add_batch(children: list[dict], kind: str):
        if not children:
            return
        n = len(children)
        gid = f"batch_{kind}_{len(jobs)+1:04d}"
        grid = macro_grid(n, kind)
        job = {
            "id": gid,
            "mode": "batch",
            "kind": kind,
            "children": [t["id"] for t in children],
            "grid": grid,
            "source_path": f"art/production/batches/sources/{gid}.png",
            "prompt_file": f"art/production/batches/prompts/{gid}.txt",
            "log_file": f"art/production/batches/logs/{gid}.log",
            "reference_paths": sorted({p for t in children for p in t.get("reference_paths", [])}),
        }
        jobs.append(job)
        for t in children:
            used.add(t["id"])
        p = ROOT / job["prompt_file"]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(batch_prompt(job, task_by_id), encoding="utf-8")

    # 1) High-yield static atlases. These remaining tasks have no identity references.
    for cat, cap in STATIC_CAPS.items():
        arr = [t for t in remaining if t["frame_count"] == 1 and t["category"] == cat]
        for group in chunk(arr, cap):
            add_batch(group, cat)

    # 2) Short animation action sheets. Group only tasks sharing the same category
    # and exact first master reference so identity/costume continuity is protected.
    buckets: dict[tuple, list[dict]] = defaultdict(list)
    for t in remaining:
        if t["id"] in used or not (2 <= int(t["frame_count"]) <= 6):
            continue
        ref = (t.get("reference_paths") or [""])[0]
        small = int(t["frame_count"]) <= 4
        buckets[(t["category"], ref, small)].append(t)
    for (_, _, small), arr in buckets.items():
        cap = 3 if small else 2
        for group in chunk(arr, cap):
            add_batch(group, "short_anim")

    # 3) Everything else remains a protected solo call using its original prompt.
    for t in remaining:
        if t["id"] in used:
            continue
        jobs.append({
            "id": f"solo_{t['id']}",
            "mode": "solo",
            "kind": "solo",
            "children": [t["id"]],
            "grid": [1, 1],
            "source_path": t["source_path"],
            "prompt_file": t["prompt_file"],
            "log_file": t["log_file"],
            "reference_paths": t.get("reference_paths", []),
        })
        used.add(t["id"])

    missing = [t["id"] for t in remaining if t["id"] not in used]
    dupes = [k for k, v in Counter(a for j in jobs for a in j["children"]).items() if v != 1]
    if missing or dupes:
        raise SystemExit(f"coverage failure missing={missing[:5]} duplicate={dupes[:5]}")

    # Preserve the canonical queue's dependency/priority order.  In particular,
    # MASTER sources must be generated before action jobs that reference them.
    queue_index = {t["id"]: i for i, t in enumerate(tasks)}
    jobs.sort(key=lambda j: min(queue_index[a] for a in j["children"]))
    for order, job in enumerate(jobs, 1):
        job["run_order"] = order

    out = {
        "schema_version": 1,
        "created_at": now(),
        "canonical_asset_task_count": len(tasks),
        "already_runtime_ready": len(tasks) - len(remaining),
        "remaining_asset_tasks": len(remaining),
        "generation_job_count": len(jobs),
        "estimated_daily_call_budget": 114,
        "estimated_quota_cycles": round(len(jobs) / 114, 2),
        "policy": {
            "canonical_queue_preserved": True,
            "backend": "ChatGPT Desktop ordinary Chat same-conversation Create Image",
            "no_api": True,
            "no_alternate_backend": True,
            "postprocess_each_child_with_existing_pipeline": True,
            "protected_solo": "character/boss/enemy masters and 8–16-frame/high-detail tasks remain solo",
        },
        "jobs": jobs,
    }
    save(OUT, out)
    print(json.dumps({
        "remaining_asset_tasks": len(remaining),
        "generation_jobs": len(jobs),
        "quota_cycles_at_114": round(len(jobs)/114, 2),
        "batch_jobs": sum(j["mode"] == "batch" for j in jobs),
        "solo_jobs": sum(j["mode"] == "solo" for j in jobs),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
