#!/usr/bin/env python3
"""Run quota-efficient generation jobs and materialize canonical ART_QUEUE children."""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone
from PIL import Image
import argparse, json, os, re, subprocess, sys, time

from chatgpt_desktop_images import (
    BACKEND,
    DesktopControlUnavailable,
    DesktopGenerationFailed,
    DesktopImagesError,
    generate_task,
)

ROOT = Path(__file__).resolve().parents[2]
PROD = ROOT / "art/production"
QDIR = PROD / "queue"
BDIR = PROD / "batches"
QUEUE = QDIR / "ART_QUEUE.json"
STATE = QDIR / "queue_state.json"
JOBS = BDIR / "GENERATION_JOBS.json"
JSTATE = BDIR / "generation_job_state.json"
COMPLETE = {"runtime_ready", "complete_reference", "superseded_side_camera"}


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def valid_image(path: Path):
    if not path.exists() or path.stat().st_size < 1000:
        return False
    try:
        with Image.open(path) as im:
            im.verify()
        return True
    except Exception:
        return False


def postprocess_child(task: dict):
    rt = QDIR / "task_runtime" / f"{task['id']}.json"
    save(rt, task)
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools/art/queue_postprocess.py"), str(rt)],
        cwd=ROOT, text=True, capture_output=True, timeout=300,
    )
    if proc.returncode:
        raise RuntimeError((proc.stderr or proc.stdout)[-4000:])


def split_batch(job: dict, task_by_id: dict[str, dict]):
    src = ROOT / job["source_path"]
    with Image.open(src) as im:
        im.load()
        cols, rows = job["grid"]
        w, h = im.size
        for idx, aid in enumerate(job["children"]):
            t = task_by_id[aid]
            col, row = idx % cols, idx // cols
            x0, x1 = round(col*w/cols), round((col+1)*w/cols)
            y0, y1 = round(row*h/rows), round((row+1)*h/rows)
            crop = im.crop((x0, y0, x1, y1)).convert("RGBA")
            dst = ROOT / t["source_path"]
            dst.parent.mkdir(parents=True, exist_ok=True)
            crop.save(dst, "PNG", compress_level=9)
            if not valid_image(dst):
                raise RuntimeError(f"invalid child crop: {aid} -> {dst}")


def synthetic_task(job: dict):
    return {
        "id": job["id"],
        "name": job["id"],
        "category": "batch",
        "tier": "BATCH",
        "status": "queued",
        "retry_count": 0,
        "max_retries": 3,
        "requirements": [],
        "source_path": job["source_path"],
        "reference_paths": job.get("reference_paths", []),
        "target_dimensions": [1536, 1536],
        "frame_count": 1,
        "grid": [1, 1],
        "alpha": "opaque",
        "godot_import_intent": "batch_source_only",
        "pivot": None,
        "padding_fraction": 0.0,
        "master_target": None,
        "exports": [],
        "visual_brief": None,
        "prompt_file": job["prompt_file"],
        "log_file": job["log_file"],
    }


def job_done(job, state):
    return all(state["tasks"].get(a, {}).get("status") in COMPLETE for a in job["children"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--retry-delay", type=float, default=1800.0)
    args = ap.parse_args()

    for p in (QUEUE, STATE, JOBS):
        if not p.exists():
            raise SystemExit(f"missing required file: {p.relative_to(ROOT)}")
    queue, state, manifest = load(QUEUE), load(STATE), load(JOBS)
    if len(queue.get("tasks", [])) != 1575:
        raise SystemExit("canonical ART_QUEUE changed; refusing batched production")
    task_by_id = {t["id"]: t for t in queue["tasks"]}
    jstate = load(JSTATE) if JSTATE.exists() else {"schema_version": 1, "jobs": {}}

    pending = [j for j in manifest["jobs"] if not job_done(j, state)]
    if args.limit:
        pending = pending[:args.limit]
    if args.dry_run:
        print(json.dumps({
            "backend": BACKEND,
            "canonical_tasks": len(queue["tasks"]),
            "generation_jobs_total": len(manifest["jobs"]),
            "pending_jobs": len(pending),
            "pending_children": sum(len(j["children"]) for j in pending),
            "first_jobs": [{"id":j["id"],"mode":j["mode"],"children":len(j["children"])} for j in pending[:12]],
        }, ensure_ascii=False, indent=2))
        return 0

    completed_jobs = 0
    for job in pending:
        jid = job["id"]
        js = jstate["jobs"].setdefault(jid, {"status":"queued","updated_at":None,"last_error":None})
        missing_refs = [p for p in job.get("reference_paths", []) if not valid_image(ROOT/p)]
        if missing_refs:
            js.update(status="blocked", last_error="missing reference(s): "+", ".join(missing_refs), updated_at=now())
            save(JSTATE, jstate)
            continue

        try:
            if job["mode"] == "solo":
                aid = job["children"][0]
                t = task_by_id[aid]
                if not valid_image(ROOT / t["source_path"]):
                    ev = generate_task(t, ROOT / t["log_file"])
                    state["tasks"].setdefault(aid, {})["desktop_images_evidence"] = ev.__dict__
                postprocess_child(t)
                state["tasks"].setdefault(aid, {}).update(
                    status="runtime_ready", retry_count=0, last_error=None, backend=BACKEND,
                    generation_job_id=jid, updated_at=now(),
                )
            else:
                bt = synthetic_task(job)
                bsrc = ROOT / job["source_path"]
                evidence = None
                if not valid_image(bsrc):
                    evidence = generate_task(bt, ROOT / job["log_file"])
                split_batch(job, task_by_id)
                for aid in job["children"]:
                    t = task_by_id[aid]
                    postprocess_child(t)
                    rec = state["tasks"].setdefault(aid, {})
                    rec.update(
                        status="runtime_ready", retry_count=0, last_error=None, backend=BACKEND,
                        generation_job_id=jid, batch_source_path=job["source_path"], updated_at=now(),
                    )
                    if evidence is not None:
                        rec["batched_desktop_images_evidence"] = evidence.__dict__

            js.update(status="runtime_ready", last_error=None, updated_at=now())
            completed_jobs += 1
            save(STATE, state); save(JSTATE, jstate)

        except DesktopControlUnavailable as exc:
            js.update(status="blocked_desktop_control", last_error=str(exc), updated_at=now())
            save(JSTATE, jstate); save(STATE, state)
            print(f"BLOCKED_DESKTOP_CONTROL {jid}: {exc}", flush=True)
            return 76
        except (DesktopGenerationFailed, DesktopImagesError) as exc:
            text = str(exc)
            if "ChatGPT Images product limit/unavailable message appeared" in text:
                js.update(status="paused_images_product_limit", last_error=text, updated_at=now())
                save(JSTATE, jstate); save(STATE, state)
                print(f"PAUSED_IMAGES_PRODUCT_LIMIT {jid}: {exc}", flush=True)
                if args.watch:
                    m = re.search(r"(\d+)\s*(?:小时|小時|hours?|hrs?)", text, re.I)
                    hinted = int(m.group(1))*3600 + 90 if m else float(args.retry_delay)
                    delay = max(600.0, hinted, float(args.retry_delay))
                    print(f"WATCH_PRODUCT_LIMIT_RETRY_IN {delay:.0f}s", flush=True)
                    time.sleep(delay)
                    os.execv(sys.executable, [sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]])
                return 75
            js.update(status="queued", last_error=text, updated_at=now())
            save(JSTATE, jstate); save(STATE, state)
            continue
        except Exception as exc:
            js.update(status="failed", last_error=str(exc), updated_at=now())
            for aid in job["children"]:
                rec = state["tasks"].setdefault(aid, {})
                if rec.get("status") not in COMPLETE:
                    rec.update(status="queued", last_error=f"generation job {jid}: {exc}", updated_at=now())
            save(JSTATE, jstate); save(STATE, state)
            continue

    subprocess.run([sys.executable, str(ROOT / "tools/art/build_manifest.py")], cwd=ROOT, text=True, capture_output=True, timeout=120)
    remaining = sum(not job_done(j, state) for j in manifest["jobs"])
    print(json.dumps({
        "backend": BACKEND,
        "completed_jobs_this_run": completed_jobs,
        "remaining_generation_jobs": remaining,
        "finished": remaining == 0,
    }, ensure_ascii=False), flush=True)

    if args.watch and remaining:
        delay = max(10.0, float(args.retry_delay))
        print(f"WATCH_RESCAN_IN {delay:.0f}s remaining_jobs={remaining}", flush=True)
        time.sleep(delay)
        os.execv(sys.executable, [sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
