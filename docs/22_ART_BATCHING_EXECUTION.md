# 《氣運復仇者》美術生圖 Batching 執行方案 V1

## 目標

在不改變 1,575 個 canonical asset task、不更換生圖後端、不使用 OpenAI API / Codex CLI / 外部生圖服務的前提下，降低 ChatGPT Desktop Images 的實際生成呼叫數，使第一輪素材能在約一週的 Images 額度週期內完成。

## 固定後端

CatDesk → ChatGPT Desktop 一般聊天 → Create Image / Images → 本機保存 → deterministic local split/postprocess → Godot PNG / SpriteFrames / `.tres`。

禁止：OpenAI API、Codex CLI image generation、Draw Things、ComfyUI、Stable Diffusion、任何替代生圖 backend。

## Canonical Queue 不變

- `art/production/queue/ART_QUEUE.json` 仍固定 1,575 項。
- `art/production/queue/queue_state.json` 仍是每個正式 asset 的完成狀態來源。
- batching 只新增「generation-job layer」，不刪除、不合併、不改名原 asset task。
- 一個 batch raster 生成完成後，本機依固定 grid 切回每個 child 的原 `source_path`，再逐項交給既有 `queue_postprocess.py`。

## Batching 規則

### 高收益靜態資產

- icons：最多 12 個 / generation job，4×3 atlas。
- UI：最多 6 個 / generation job，3×2 atlas。
- static traps：最多 4 個 / generation job，2×2 atlas。
- maps / map components：最多 2 個 / generation job，2×1 sheet。

### 短動畫

僅合併 2～6 幀 task，而且必須共用相同 category 與相同第一 identity/master reference。

- 2～4 幀 task：最多 3 個 action / generation job。
- 5～6 幀 task：最多 2 個 action / generation job。
- 每個 action 保留自己的 nested frame grid 與連續時間順序。

### 一律保留 Solo

以下維持 1 task = 1 Images call：

- character / boss / enemy MASTER。
- 8～16 幀高細節動畫與 Boss 大招。
- 其他未達安全 batching 條件的 task。

## 執行工具

- `tools/art/build_generation_jobs.py`
  - 讀 canonical queue/state。
  - 建立 `art/production/batches/GENERATION_JOBS.json`。
  - 產生每個 batch 的本機 prompt。
  - 驗證每個未完成 asset 恰好被一個 generation job 覆蓋。
  - 依 canonical queue 的最早 child index 排序，保證 MASTER 優先於依賴動畫。

- `tools/art/run_generation_jobs.py`
  - 呼叫既有 `chatgpt_desktop_images.generate_task()`。
  - 保存 batch source 到本機。
  - deterministic split 到原 child `source_path`。
  - 每個 child 個別執行既有 `queue_postprocess.py`。
  - 成功後才寫回 `runtime_ready`。
  - 支援 `--dry-run`、`--limit`、`--watch`、`--retry-delay`。
  - 遇 Images product limit 時不消耗 asset retry，等待後續重試。

## 目前 V1 實測規劃值

建立時 canonical queue = 1,575 項；已完成/已 superseded 的 task 會自動排除。

2026-09-17 建立結果：

- remaining canonical asset tasks：1,450
- generation jobs：689
- batch jobs：486
- protected solo jobs：203
- 以約 114 Images calls / quota cycle 估算：約 6.04 個 quota cycles

這代表第一輪在不計 redo、額度政策與實測產能維持相近的前提下，具備在 7 天內完成的容量，並保留約一個額度週期內的部分緩衝。

## 驗證原則

- batch 生成成功不代表 child 完成。
- child 必須成功切圖、來源 PNG 可開啟、`queue_postprocess.py` PASS，才可標記 `runtime_ready`。
- 任何 batch split/postprocess 失敗，child 保留未完成狀態，可恢復重跑。
- 已完成的 canonical child 不重新生成。
- generated binary art 仍只保存在 Mac 本機，不因本方案自動上傳 GitHub。
