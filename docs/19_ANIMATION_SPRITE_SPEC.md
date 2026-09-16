# 19｜動畫與 Sprite 規格 V1

專案：《氣運復仇者》 / QiYun Avengers

用途：固定角色、Boss、小怪、VFX、UI Icon、地圖物件與動畫輸出規格，方便後續用 AI 生圖、手修、切圖、導入 Godot / Web / 其他 2D 引擎。

> 本文件接續：
>
> - `03_ART_DIRECTION.md`
> - `06_CHARACTER_PROMPT_DESIGN.md`
> - `07_ENEMY_PROMPT_DESIGN.md`
> - `08_ENEMY_EFFECT_PROMPT_DESIGN.md`
> - `09_UI_PAGE_DESIGN.md`
>
> 美術規格的核心：**可愛、清楚、可切圖、可動畫、不能混入既有 IP 或玩具品牌辨識特徵。**

---

## 0. 整體輸出原則

### 0.1 Sprite 必須符合

- 原創 Q 版比例。
- 饅頭手，不使用 C 形握手或拼裝玩具關節。
- 不使用商標、Logo、可辨識 IP 圖案。
- 白底或透明背景，方便切圖。
- 多姿勢同張圖時要乾淨 grid。
- 角色比例一致。
- 動作方向清楚；角色統一使用 45–60° 半側身（semi-profile / 3/4 side combat view），主移動與攻擊方向維持左右向。
- 多幀角色動作必須是同一動作的時間連續 keyframes，不得只是彼此無關的 pose 集合；前一格要能自然銜接下一格。
- 手機尺寸下仍能讀懂輪廓。

### 0.2 不接受

- 角色切到邊。
- 每格角色大小不一致。
- 動作表背景複雜。
- 角色身上有文字、商標、Logo。
- 手部變成既有玩具式 C 型手。
- 關節像可拆裝玩具。
- 同一動作裡服裝細節大幅變化。
- 特效遮住整個角色，導致看不懂攻擊。

---

## 1. 畫面比例與解析度

### 1.1 Master Art

| 類型 | 建議尺寸 | 用途 |
|---|---:|---|
| 角色 Master | 2000 x 2000 px | 高解析角色設計、宣傳、拆件。 |
| Boss Master | 2400 x 2400 px | Boss 大圖與拆件參考。 |
| 小怪 Master | 1600 x 1600 px | 小怪設計與動作參考。 |
| 道具 Icon Master | 1024 x 1024 px | UI icon 與商店卡。 |
| VFX Master Sheet | 2048 x 2048 px | 特效切圖。 |
| 地圖 Tile / Prop | 1024 x 1024 px | 場景物件。 |

### 1.2 Runtime Sprite

| 類型 | Runtime 尺寸方向 |
|---|---:|
| Ghost | 128～192 px 高 |
| 普通小怪 | 96～160 px 高 |
| 精英小怪 | 160～220 px 高 |
| Boss | 260～420 px 高 |
| Final Boss | 320～520 px 高，依 Phase |
| 投射物 | 32～96 px |
| 道具 Icon | 64～128 px |

---

## 2. Sprite Sheet 格式

### 2.1 基本規格

建議輸出：

```text
PNG
透明背景優先
若 AI 工具不穩，先 white background，再後處理去背
每格留 10% 安全邊距
所有格子等寬等高
角色腳底基準線一致
```

### 2.2 Grid 規格

| 用途 | Grid |
|---|---|
| 小怪動作表 | 4 x 4 或 5 x 4 |
| Ghost 動作表 | 6 x 4 或分動作輸出 |
| Boss 動作表 | 每個動作獨立 sheet，避免太亂 |
| VFX Sheet | 4 x 4 / 6 x 4，特效分離 |
| Icon Sheet | 4 x 4 / 8 x 8 |

### 2.3 命名規則

```text
character_[id]_[action]_[direction].png
boss_[id]_[phase]_[action].png
enemy_[id]_[action].png
vfx_[skill_id]_[type].png
icon_[category]_[id].png
prop_[stage_id]_[prop_id].png
trap_[stage_id]_[trap_id].png
```

範例：

```text
character_ghost_idle_side.png
character_ghost_dash_side.png
boss_m_sir_phase1_jump_slam.png
enemy_shadow_paper_ninja_attack.png
vfx_pipe_impact_ground_wave.png
icon_relic_villain_script_draft.png
trap_pipe_city_steam_burst.png
```

---

## 3. Anchor / Pivot 規格

### 3.1 角色 Pivot

| 類型 | Pivot 位置 |
|---|---|
| Ghost | 腳底中心。 |
| 普通小怪 | 腳底中心。 |
| 飛行小怪 | 身體中心偏下。 |
| Boss | 腳底中心或身體中心，依引擎。 |
| 投射物 | 幾何中心。 |
| 地面陷阱 | 區域中心。 |
| UI Icon | 中心。 |

### 3.2 重要規則

- 同角色所有動作 Pivot 必須一致。
- Dash / 攻擊不能因 Pivot 漂移造成角色瞬移。
- Boss 體型大，但碰撞盒不可完全等於圖片大小。
- 特效 Pivot 應對齊實際命中點。

---

## 4. Ghost 動畫規格

### 4.1 必要動作

| 動作 | 建議幀數 | 說明 |
|---|---:|---|
| idle | 4～6 | 輕微漂浮、斗篷呼吸。 |
| move | 6～8 | 小步飄移或滑行。 |
| dash | 4～6 | 壓縮 → 拉長 → 殘影 → 回復。 |
| basic_attack_1 | 4～6 | 快速爪擊。 |
| basic_attack_2 | 4～6 | 橫掃。 |
| basic_attack_3 | 6～8 | 重擊，稍大後搖。 |
| skill_cast | 6～10 | 通用施法。 |
| hit | 3～4 | 閃白、後仰。 |
| knockback | 4～6 | 被擊退。 |
| dead | 8～12 | 化成黑紫煙。 |
| victory | 8～12 | 吸收氣運，斗篷飄起。 |

### 4.2 Ghost 特效規則

- 眼睛發光可做 2～3 級亮度。
- 怨念煙不應遮住身體輪廓。
- Dash 殘影用黑紫透明影，不要太長。
- 死亡不血腥，改成怨念散掉。

---

## 5. Boss 動畫規格

### 5.1 Boss 共通動作

| 動作 | 建議幀數 | 說明 |
|---|---:|---|
| idle | 6～10 | 每位 Boss 獨特站姿。 |
| intro | 12～24 | 登場動畫，可分鏡。 |
| walk / move | 6～10 | Boss 移動。 |
| light_attack | 6～8 | 快速招。 |
| heavy_attack | 10～16 | 高傷招，有清楚前搖。 |
| signature_attack | 12～24 | 招牌招式。 |
| phase_change | 16～32 | 進入下一 Phase。 |
| broken | 8～12 | 被相剋破防。 |
| hit | 3～5 | 短受擊，不打斷所有招式。 |
| defeated | 16～32 | 氣運被剝離。 |

### 5.2 M先生 動畫需求

| 動作 | 說明 |
|---|---|
| pipe_swing | 水管橫掃。 |
| jump_slam | 起跳、落地、震波。 |
| pipe_dash | 管線突進。 |
| steam_call | 召喚噴管。 |
| broken | 水管彎掉、帽子歪掉。 |
| defeated | 紅帽掉落，氣運被吸走。 |

### 5.3 滅影忍者 動畫需求

| 動作 | 說明 |
|---|---|
| kunai_throw | 苦無投擲。 |
| shadow_step | 瞬身消失與出現。 |
| clone_spawn | 分身生成。 |
| backstab | 背後突刺。 |
| broken | 真身被震出，影子散掉。 |
| defeated | 分身全部碎成紙片。 |

### 5.4 U-man 動畫需求

| 動作 | 說明 |
|---|---|
| core_charge | 胸口藍核蓄力。 |
| core_beam | 直線光束。 |
| shield_up | 正面護盾。 |
| pulse | 核心脈衝。 |
| broken | 胸口核心裂開黑紫光。 |
| defeated | 光消失，身體半跪。 |

### 5.5 Creator 動畫需求

| Phase | 動作 |
|---|---|
| P1 創辦者 | 指令、翻頁、草稿分身、Patch Beam。 |
| P2 完美英雄 | 披風展開、護盾、混合招式、英雄姿勢。 |
| P3 神話創造者 | 巨手、雷霆、Eraser、白頁擦除。 |

Creator 的動畫要像「設計者修改世界」，不是單純魔法師。

---

## 6. 小怪動畫規格

### 6.1 小怪必要動作

| 動作 | 幀數 | 用途 |
|---|---:|---|
| idle | 4～6 | 待機。 |
| walk | 6～8 | 移動。 |
| normal_attack | 4～8 | 普攻。 |
| skill_attack | 6～12 | 技能或特殊機制。 |
| taking_damage | 2～4 | 受擊。 |
| defeated | 6～10 | 陣亡。 |

這與 `07_ENEMY_PROMPT_DESIGN.md` 的小怪 action sheet 對齊。

### 6.2 小怪動作表 Prompt 核心要求

```text
white background, multiple small full-body poses, clean grid, same character, same 45–60 degree semi-profile camera facing screen-right, consistent costume and proportions, continuous chronological animation keyframes with every frame naturally connecting to the next, no unrelated showcase poses, idle / walk / normal attack / skill attack / taking damage / defeated
```

### 6.3 小怪動畫注意事項

- 小怪普攻前搖要能讀出方向。
- 遠程小怪要有抬手 / 聚能 / 投射動作。
- 輔助小怪要有連線、法陣或手勢提示。
- 陣亡用煙霧、暈星、碎片，不使用血。

---

## 7. 技能 VFX 規格

### 7.1 VFX 分層

技能特效建議拆成：

| 層 | 用途 |
|---|---|
| anticipation | 起手提示。 |
| active | 攻擊本體。 |
| impact | 命中特效。 |
| trail | 移動軌跡。 |
| fade | 消散。 |
| debris | 小碎片、煙、粒子。 |

### 7.2 八技能 VFX 規格

| 技能 | VFX 關鍵 |
|---|---|
| 管線衝擊 | 地面黑紫震波、裂縫、碎石、短衝擊線。 |
| 影遁衝刺 | 黑影拉長、殘影、終點小煙。 |
| 核心光束 | 黑紫中心光束，帶少量藍核裂光。 |
| 破甲合擊 | 多個怨靈拳影、破甲碎片。 |
| 吞運葫蘆 | 黑紫葫蘆口、吸入流線、反吐彈。 |
| 怨火爆燃 | 紫黑火場、橘紅外緣、禁療符號不可用文字。 |
| 蛛線牽引 | 細黑紫線、白色節點、拉扯波紋。 |
| 鬥氣爆發 | 黑紫氣焰、短霸體外框、拳風。 |
| Eraser | 白色擦除痕、紙屑、黑框裂縫。 |

### 7.3 VFX 可讀性

- 普攻 VFX 小，技能 VFX 中，Boss 大招 VFX 大。
- VFX 不要用太多顏色。
- 命中點要清楚。
- 危險提示與傷害特效要分開。
- 玩家技能與敵人技能顏色要能區分。

---

## 8. UI Icon 規格

### 8.1 Icon 尺寸

| 用途 | 尺寸 |
|---|---:|
| 技能 Icon | 512 x 512 master，Runtime 96～128。 |
| 遺物 Icon | 512 x 512 master，Runtime 64～96。 |
| Buff / Debuff | 256 x 256 master，Runtime 32～64。 |
| 關卡節點 | 512 x 512 master，Runtime 64～128。 |
| Boss 徽記 | 1024 x 1024 master，Runtime 128～256。 |

### 8.2 Icon 規則

- 中心物件清楚。
- 不放文字。
- 不放商標。
- 不用複雜背景。
- 稀有度靠外框與光效區分。
- 道具功能要一眼可猜。

### 8.3 Icon Prompt

```text
original chibi dark-comedy mobile game icon, centered object, clean readable silhouette, thick soft outline, simple 2.5D anime game style, high contrast, square composition, no text, no letters, no numbers, no logo, no background scenery, game-ready asset
```

---

## 9. 地圖 Tile 與 Prop 規格

### 9.1 Tile 分類

| 類型 | 說明 |
|---|---|
| ground | 可行走地面。 |
| wall | 邊界 / 不可通過。 |
| hazard | 危險地面。 |
| platform | 平台或高低差。 |
| decoration | 裝飾，不影響碰撞。 |
| interactable | 可破壞或可互動。 |

### 9.2 Prop 規格

- 每個 Prop 要有正常、受擊、破壞後三種狀態，重要物件再加啟動狀態。
- 破壞物件要能掉落道具或觸發陷阱。
- 背景 Prop 不要和可互動 Prop 長太像。

### 9.3 地圖物件例子

| 地圖 | Prop |
|---|---|
| 紅帽管線城 | 管線、閥門、井蓋、警示牌。 |
| 影村訓練場 | 木樁、紙符、燈籠、暗幕。 |
| 藍核基地 | 能源柱、雷射器、護盾門。 |
| 鋼筋工廠 | 輸送帶、磁鐵塔、裝甲門。 |
| 命運劇場 | 白頁、草稿框、修正游標、Eraser 痕。 |

---

## 10. 方向與視角

### 10.1 方向需求

MVP 統一使用 45–60° 半側身（semi-profile / 3/4 side combat view），避免正面展示，也避免完全平坦的 90° 純側面。身體與移動方向必須明確左右向，臉與胸口只微微朝鏡頭。

| 角色 | 必要方向 |
|---|---|
| Ghost | 45–60° semi-profile 半側身，MASTER 統一面向畫面右側；臉與胸口只微微朝鏡頭，向左由 Godot 水平鏡像。 |
| 小怪 | 45–60° semi-profile 半側身，MASTER 統一面向畫面右側；主動作保持左右向，向左由 Godot 水平鏡像。 |
| Boss | 45–60° semi-profile 半側身，MASTER 統一面向畫面右側；Boss 面向玩家方向由 Godot 水平鏡像。 |
| VFX | 水平左右為主，可旋轉。 |

### 10.2 翻轉規則

- 普通小怪可水平翻轉。
- Boss 若有不對稱設計，翻轉前要確認不影響辨識。
- 文字與 Logo 禁用，因此翻轉不會造成字反轉問題。
- 光束、管線、蛛線等 VFX 可程式旋轉，不必每方向都畫。

---

## 11. 動畫 Timing

### 11.1 FPS

| 類型 | FPS |
|---|---:|
| 角色 idle / move | 8～12 FPS |
| 普攻 | 12～18 FPS |
| Boss heavy attack | 10～16 FPS |
| VFX | 12～24 FPS |
| UI 動畫 | 12～24 FPS |

### 11.2 Hit Frame

每個攻擊動畫必須先確保幀序是時間連續的：anticipation / startup → launch → active / impact → follow-through → recovery。若幀數較少，可合併階段，但不可用互不相關的姿勢填格。

每個攻擊動畫必須標記：

```text
startup frames
active hit frames
recovery frames
```

範例：

```json
{
  "animation": "ghost_basic_attack_1",
  "fps": 16,
  "frames": 6,
  "startup": [0, 1],
  "active": [2, 3],
  "recovery": [4, 5]
}
```

---

## 12. Collision / Hurtbox 規格

### 12.1 Box 分類

| Box | 說明 |
|---|---|
| hurtbox | 被打判定。 |
| hitbox | 攻擊判定。 |
| collision | 牆壁 / 地形碰撞。 |
| pickup | 道具拾取範圍。 |
| trigger | 陷阱或事件觸發。 |

### 12.2 規則

- Hurtbox 比圖像略小，避免看起來沒碰到卻受傷。
- Boss 的 hurtbox 可分身體與弱點核心。
- Hitbox 要跟 VFX 方向一致。
- 地面陷阱用簡單幾何形，避免複雜輪廓。
- 飛行敵人 hurtbox 不要過小。

---

## 13. AI 生圖工作流規格

### 13.1 角色動作表 Prompt 結構

```text
[共通風格]
[角色外觀]
[動作需求]
[輸出格式]
[限制]
```

範例：

```text
original stylized block-figure dark-comedy 2D mobile game character sprite sheet, Ghost character, black purple cloak, glowing dot eyes, rounded mitten hands, cute but eerie, 45–60 degree semi-profile side-scroller combat view facing screen-right, body and movement read horizontally, face and torso only slightly toward viewer, multiple full-body consecutive animation keyframes forming continuous chronological actions, every frame naturally connects to the next, same camera angle and scale, idle, move, dash, attack, hit, defeated, clean grid, white background, consistent costume, animation-ready, no unrelated showcase poses, no text, no logo, no toy joints
```

### 13.2 Negative Prompt 必加

```text
low quality, blurry, messy, inconsistent costume, different character, cropped body, realistic human, gore, blood, text, letters, numbers, watermark, signature, trademark logo, recognizable IP character, C-shaped toy hands, visible toy joints, stud-compatible parts, LEGO-like minifigure proportions, complex background
```

### 13.3 生成後處理

流程：

```text
AI 生成 → 挑選最穩版本 → 去背 → 切格 → 對齊 Pivot → 調整大小 → 匯出 PNG → 導入引擎 → 測試動畫
```

---

## 14. 檔案資料夾建議

```text
assets/
  characters/
    ghost/
      master/
      sprites/
      vfx/
  bosses/
    m_sir/
    shadow_ninja/
    u_man/
    creator/
  enemies/
    pipe_city/
    shadow_village/
  vfx/
    skills/
    enemy/
    traps/
  ui/
    icons/
    cards/
    hud/
  stages/
    00_resentment_birthplace/
    01_pipe_city/
    02_shadow_village/
```

---

## 15. 匯入引擎注意事項

### 15.1 Godot

若使用 Godot：

- Sprite2D / AnimatedSprite2D 做角色動畫。
- AnimationPlayer 控制 hitbox 啟用時機。
- Area2D 做技能命中。
- CollisionShape2D 使用簡單形狀。
- Texture import 關閉不必要壓縮，避免像素邊緣髒。
- 手機版本注意 draw call 與透明特效數量。

### 15.2 Web / Phaser

若使用 Phaser：

- Texture Atlas 優先於大量單張 PNG。
- 用 animation key 控制狀態。
- VFX 可用 sprite animation + particles。
- 注意手機瀏覽器記憶體。

### 15.3 Unity

若使用 Unity：

- Sprite Atlas 打包。
- Animator 或自訂狀態機。
- 2D Physics hitbox 需和動畫事件同步。
- Mobile build 注意透明 Overdraw。

---

## 16. MVP 美術與動畫範圍

第一版只需要：

| 類型 | 數量 |
|---|---:|
| Ghost 動作 | idle / move / dash / attack / hit / dead |
| M先生 動作 | idle / move / pipe_swing / jump_slam / broken / defeated |
| 滅影忍者 動作 | idle / move / kunai / shadow_step / clone / broken / defeated |
| 小怪 | 6 種，每種 6 動作 |
| 技能 VFX | 管線衝擊、影遁衝刺 |
| 陷阱 VFX | 裂運地面、地底噴管、影紙地雷 |
| UI Icon | 技能 2、遺物 15、消耗品 3、節點 6 |

不要第一版就追求所有 Boss 完整動畫。

---

## 17. 品質驗收清單

### 17.1 單張角色驗收

- 是否原創？
- 是否符合 Q 版比例？
- 是否沒有商標 / 文字 / 既有 IP 特徵？
- 是否沒有 C 形玩具手或拼裝玩具關節？
- 手機尺寸下輪廓是否清楚？
- 顏色是否符合角色陣營？

### 17.2 動作表驗收

- 每格角色大小是否一致？
- 腳底基準線是否一致？
- 服裝是否一致？
- 動作是否真的能串成動畫？
- 攻擊方向是否清楚？
- 是否有足夠安全邊距？

### 17.3 VFX 驗收

- 能否看出危險方向？
- 是否遮住角色？
- 是否與敵我顏色區分？
- 命中點是否清楚？
- 是否方便切圖？

### 17.4 Runtime 驗收

- 動畫是否抖動？
- Pivot 是否漂移？
- Hitbox 是否和特效一致？
- 手機上是否太小？
- 同時播放多個 VFX 是否掉幀？

---

## 18. 最終規格句

所有美術資產都應服務這句話：

```text
玩家一眼看懂誰在打、攻擊從哪來、哪裡危險、哪一招是剛從英雄身上搶來的。
```

看不懂，就算畫得漂亮也不合格。
