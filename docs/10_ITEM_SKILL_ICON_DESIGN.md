# 10｜道具、技能與 Icon 設計 V1

專案：《氣運復仇者》 / QiYun Avengers

用途：固定技能 Icon、道具 Icon、遺物 Icon、消耗品 Icon、Buff / Debuff、關卡節點、Boss 徽記、稀有度框與 AI 生圖 Prompt 規格，確保 UI 與戰鬥系統可讀。

> 本文件接續：
>
> - `03_ART_DIRECTION.md`
> - `06_CHARACTER_PROMPT_DESIGN.md`
> - `08_ENEMY_EFFECT_PROMPT_DESIGN.md`
> - `09_UI_PAGE_DESIGN.md`
> - `12_SKILL_BUILD_SYSTEM_DESIGN.md`
> - `13_ITEM_RELIC_EFFECT_DESIGN.md`
> - `19_ANIMATION_SPRITE_SPEC.md`
>
> Icon 核心：**小尺寸也要看得懂功能，大尺寸也要有黑色幽默。**

---

## 0. Icon 設計總原則

### 0.1 目標

Icon 要達成四件事：

1. **一眼辨識功能**：玩家不用讀長文也能猜到用途。
2. **和 Build 標籤一致**：impact / shadow / core / flame 等都有固定視覺語言。
3. **符合本作風格**：可愛、黑紫、裂金、反英雄。
4. **適合手機尺寸**：縮到 64px 仍可讀。

### 0.2 Icon 不做方向

避免：

- 太寫實。
- 背景太複雜。
- 物件太小。
- 放文字、字母、數字。
- 放商標、Logo、既有 IP 符號。
- 用過多細節表達功能。
- 每個 Icon 都是同一團紫光，分不出差異。
- 使用拼裝玩具式手掌、關節、零件比例。

---

## 1. Icon 共通規格

### 1.1 尺寸

| 用途 | Master | Runtime |
|---|---:|---:|
| 技能 Icon | 1024 x 1024 | 96～160 |
| 遺物 Icon | 1024 x 1024 | 64～128 |
| 消耗品 Icon | 512 x 512 | 48～96 |
| Buff / Debuff | 512 x 512 | 32～64 |
| 關卡節點 | 1024 x 1024 | 64～128 |
| Boss 徽記 | 1024 x 1024 | 128～256 |
| UI 小圖示 | 512 x 512 | 24～64 |

### 1.2 構圖

```text
中心主物件 70%
外框 / 光效 20%
安全邊距 10%
```

規則：

- 主物件置中。
- 不靠邊裁切。
- 外框與主物件分層清楚。
- 小尺寸先看輪廓，不看細節。

### 1.3 背景

Icon 背景可以：

- 單色深紫。
- 淡黑紫漸層。
- 稀有度光環。
- 透明背景 + UI 框處理。

不要使用完整場景背景，避免縮小後混亂。

---

## 2. 共通 Icon Prompt

### 2.1 基礎 Prompt

```text
original cute dark-comedy mobile game icon, centered object, clean readable silhouette, thick soft outline, black purple ghost energy, cracked golden hero light accent, simple 2.5D anime game style, high contrast, square composition, game-ready asset, no text, no letters, no numbers, no logo, no trademark, no recognizable IP symbol
```

### 2.2 技能 Icon Prompt

```text
original chibi roguelite action skill icon, centered magical attack symbol, black purple ghost power mixed with cracked golden hero energy, dynamic but readable, thick soft outline, high contrast, square mobile game icon, clear combat function, no text, no logo, no trademark, no recognizable IP symbol
```

### 2.3 遺物 Icon Prompt

```text
original roguelite relic icon, cute dark-comedy fantasy object, centered item, black purple ghost aura, cracked gold rarity glow, simple readable shape, thick soft outline, square mobile game asset, no text, no logo, no trademark, no recognizable IP symbol
```

### 2.4 Negative Prompt

```text
low quality, blurry, messy, unreadable, tiny object, cluttered background, realistic photo, gore, blood, text, letters, numbers, watermark, signature, trademark logo, recognizable IP symbol, copyrighted character, C-shaped toy hands, visible toy joints, construction toy minifigure proportions, complex scenery, low contrast
```

---

## 3. Build 標籤視覺語言

| 標籤 | 主要形狀 | 色彩 | 聽覺 / 感覺 |
|---|---|---|---|
| impact | 地裂、震波、碎石 | 黑紫 + 土黃 | 重、敲擊。 |
| shadow | 殘影、紙影、斜刃 | 深紫 + 黑 | 快、消失。 |
| core | 圓核、光束、裂晶 | 藍 + 金白 | 聚能、穿透。 |
| armor_break | 裂盾、破甲片 | 鋼灰 + 紫裂 | 多段、碎裂。 |
| devour | 葫蘆口、旋渦、吸入 | 深紫 + 亮綠 / 金 | 吸收、反吐。 |
| flame | 紫黑火苗、丹火 | 紫黑 + 橘紅 | 燃燒、持續。 |
| web | 細線、節點、拉扯 | 白線 + 紫節點 | 黏、牽引。 |
| ki | 氣焰、拳風、爆氣 | 紫 + 金 + 暗紅 | 霸體、爆發。 |
| luck | 裂金光環、幸運星碎片 | 金白 + 黑裂 | 氣運、偏心。 |
| curse | 裂印、暗紅契約 | 暗紅 + 黑紫 | 代價、不穩。 |
| economy | 怨幣、袋子、價格牌 | 紫金 | 商店、交換。 |
| survival | 護符、破心、盾 | 紫白 + 淡紅 | 保命、恢復。 |
| erase | 白頁、擦痕、空白框 | 白灰 + 黑邊 | 清除、封鎖。 |

---

## 4. 八個 Boss 奪取技能 Icon

### 4.1 管線衝擊

| 項目 | 規格 |
|---|---|
| 來源 | M先生。 |
| 標籤 | impact / ground / anti_stealth。 |
| 主物件 | 彎曲水管敲向地面，地裂向前擴散。 |
| 色彩 | 黑紫地裂 + 暗金火花 + 金屬灰。 |
| 小尺寸辨識 | 水管 + 地裂。 |

Prompt：

```text
original mobile game skill icon, bent metal pipe striking cracked ground, black purple shockwave, small cracked golden sparks, cute dark-comedy roguelite style, centered object, thick soft outline, high contrast, square icon, no text, no logo, no trademark
```

### 4.2 影遁衝刺

| 項目 | 規格 |
|---|---|
| 來源 | 滅影忍者。 |
| 標籤 | shadow / dash / invincible。 |
| 主物件 | Ghost 殘影穿過黑紫斜線。 |
| 色彩 | 深紫、黑、少量紙白。 |
| 小尺寸辨識 | 斜向殘影 + 消失煙。 |

Prompt：

```text
original mobile game skill icon, dark ghost shadow dash, diagonal purple afterimage, paper-like smoke fragments, cute sinister chibi action style, centered, readable silhouette, thick outline, square icon, no text, no logo, no trademark
```

### 4.3 核心光束

| 項目 | 規格 |
|---|---|
| 來源 | U-man。 |
| 標籤 | core / beam / pierce / shield_break。 |
| 主物件 | 裂開藍核射出黑紫光束。 |
| 色彩 | 藍核 + 黑紫光束 + 裂金邊。 |
| 小尺寸辨識 | 圓核心 + 直線光束。 |

Prompt：

```text
original mobile game skill icon, cracked blue energy core firing dark purple beam, broken golden hero light around the core, clean readable laser shape, cute dark-comedy roguelite style, thick soft outline, square icon, no text, no logo, no trademark
```

### 4.4 破甲合擊

| 項目 | 規格 |
|---|---|
| 來源 | 鋼筋戰士。 |
| 標籤 | armor_break / multi_hit / interrupt。 |
| 主物件 | 多個黑紫拳影打碎盾甲。 |
| 色彩 | 鋼灰、黑紫、裂金。 |
| 小尺寸辨識 | 破盾 + 多拳。 |

Prompt：

```text
original mobile game skill icon, multiple ghostly purple fists smashing a cracked metal shield, armor fragments flying, cute chibi roguelite action style, centered, high contrast, thick outline, square icon, no text, no logo, no trademark
```

### 4.5 吞運葫蘆

| 項目 | 規格 |
|---|---|
| 來源 | 葫蘆爺。 |
| 標籤 | devour / absorb / reflect。 |
| 主物件 | 黑紫葫蘆張口吸入金白氣運。 |
| 色彩 | 深紫葫蘆、金白碎光、旋渦。 |
| 小尺寸辨識 | 葫蘆 + 吸入旋渦。 |

Prompt：

```text
original mobile game skill icon, dark purple magic gourd absorbing cracked golden luck energy, swirling suction vortex, cute dark-comedy fantasy roguelite style, centered object, thick soft outline, high contrast, square icon, no text, no logo, no trademark
```

### 4.6 怨火爆燃

| 項目 | 規格 |
|---|---|
| 來源 | 消炎。 |
| 標籤 | flame / dot / anti_heal / burn_web。 |
| 主物件 | 紫黑火苗包住破裂丹藥。 |
| 色彩 | 紫黑、橘紅、暗金。 |
| 小尺寸辨識 | 火苗 + 丹藥爆裂。 |

Prompt：

```text
original mobile game skill icon, cursed purple black flame bursting from a cracked alchemy pill, orange red outer glow, cute dark fantasy roguelite style, centered, thick soft outline, high contrast, square icon, no text, no logo, no trademark
```

### 4.7 蛛線牽引

| 項目 | 規格 |
|---|---|
| 來源 | 失敗的面。 |
| 標籤 | web / pull / bind / anti_air。 |
| 主物件 | 白紫蛛線鉤住空中黑影。 |
| 色彩 | 白線、紫節點、黑影。 |
| 小尺寸辨識 | 線 + 鉤點 + 拉扯方向。 |

Prompt：

```text
original mobile game skill icon, thin white purple web line pulling a small dark flying shadow downward, elastic tension, cute dark-comedy action style, centered composition, readable silhouette, thick outline, square icon, no text, no logo, no trademark
```

### 4.8 鬥氣爆發

| 項目 | 規格 |
|---|---|
| 來源 | 吾空。 |
| 標籤 | ki / armor / melee_boost / anti_stagger。 |
| 主物件 | 小 Ghost 拳頭周圍爆出黑紫氣焰。 |
| 色彩 | 黑紫、金、暗紅。 |
| 小尺寸辨識 | 拳頭 + 氣焰。 |

Prompt：

```text
original mobile game skill icon, small ghost fist surrounded by dark purple fighting aura, cracked golden energy sparks, cute chibi roguelite action style, centered, powerful readable silhouette, thick outline, square icon, no text, no logo, no trademark
```

### 4.9 Eraser

| 項目 | 規格 |
|---|---|
| 來源 | Creator。 |
| 標籤 | erase / rule / seal。 |
| 主物件 | 白色擦除痕穿過黑紫技能符號。 |
| 色彩 | 白灰、黑框、少量紫裂。 |
| 小尺寸辨識 | 擦痕 + 被刪掉的符號。 |

Prompt：

```text
original final boss skill icon, magical white eraser swipe deleting a dark purple ghost symbol, black frame cracks, paper dust, clean high contrast, cute dark-comedy roguelite style, square icon, no text, no logo, no trademark
```

---

## 5. Ghost 基礎能力 Icon

| Icon | 主物件 | 色彩 | 用途 |
|---|---|---|---|
| 怨念爪擊 | 三道黑紫爪痕 | 紫黑 + 白邊 | 普攻。 |
| 怨念彈 | 小黑紫能量球 | 紫 + 幽藍 | 遠程可選。 |
| Dash | Ghost 殘影小箭頭 | 黑紫 | 閃避。 |
| 受擊無敵 | 破裂小護盾 | 淡白 + 紫 | Buff。 |
| 技能冷卻 | 沙漏 + 紫煙 | 灰紫 | 狀態。 |
| 氣運破裂 | 裂開金星 | 金白 + 紫裂 | 破防提示。 |

---

## 6. 遺物 Icon 設計

### 6.1 Common 遺物

| 名稱 | 主物件 | 辨識重點 |
|---|---|---|
| 怨念小石頭 | 小黑紫石頭 | 石頭中有小眼睛光點。 |
| 破斗篷別針 | 破舊別針 | 斗篷布角。 |
| 壞掉的英雄徽章 | 裂開徽章 | 金白徽章被紫裂侵蝕。 |
| 沒人要的獎盃 | 歪掉獎盃 | 獎盃裡冒黑煙。 |
| 二手訓練沙包 | 小沙包 | 上面有爪痕，不放字。 |
| 黑影鞋墊 | 小鞋墊殘影 | Dash 感。 |
| 低亮度寶石 | 暗淡寶石 | 藍紫小光。 |
| 便宜護甲片 | 裂護甲 | 灰色碎片。 |

### 6.2 Rare 遺物

| 名稱 | 主物件 | 辨識重點 |
|---|---|---|
| 背後的黑手 | 小黑手影 | 背刺、偷襲。 |
| 震盪怨骨 | 骨頭震波 | impact 聯動。 |
| 反英雄聚焦鏡 | 裂鏡片 | core / luck。 |
| 分身驗屍單 | 紙影碎片 | shadow 反制。 |
| 燒焦的蛛網 | 燒斷網線 | flame + web。 |
| 空葫蘆保固書 | 葫蘆小牌 | devour。 |
| 武道會敗者名單 | 捲軸 + 拳印 | ki。 |
| 補給員的悔意 | 小飯盒 | survival。 |

### 6.3 Epic 遺物

| 名稱 | 主物件 | 辨識重點 |
|---|---|---|
| 遲到的主角光環 | 歪掉光環 | 金光裂開。 |
| 合體失敗證明書 | 破碎合體徽 | armor_break。 |
| 被吞掉的奇蹟 | 葫蘆裡的星 | devour + luck。 |
| 禁藥目錄 | 丹藥書頁 | flame / curse。 |
| 都市屋簷契約 | 屋簷 + 蛛線 | web。 |
| 裝甲稅單 | 破甲片 + 錢幣 | economy / armor。 |
| 世界不公證明 | 裂天平 | luck / curse。 |
| 第五個隊友 | 空椅子 + 黑影 | team parody, 不用既有標誌。 |

### 6.4 Legendary 遺物

| 名稱 | 主物件 | 辨識重點 |
|---|---|---|
| 反派劇本原稿 | 黑紫劇本頁 | 規則被改寫。 |
| 黑洞葫蘆 | 葫蘆內黑洞 | 強吸收。 |
| 第零根蛛線 | 一條發光線 | web 核心。 |
| 借來的正義光 | 被偷來的金光 | luck。 |
| 越輸越強證明 | 裂冠 + 怨念 | 失敗者成長。 |
| 無名敗者王冠 | 歪王冠 | Ghost 王冠。 |
| 小型世界漏洞 | 空白破洞 | Creator 伏筆。 |
| 怨念總帳 | 厚帳本 | 經濟 + 怨念。 |

### 6.5 Cursed 遺物

| 名稱 | 主物件 | 辨識重點 |
|---|---|---|
| 借命復仇 | 裂心 + 紫火 | HP 代價。 |
| 爛尾主角光環 | 斷掉光環 | 強但不穩。 |
| 被刪掉的護身符 | 白頁擦過護符 | erase。 |
| 反派稅務局 | 怨幣被咬 | economy curse。 |
| 不穩定氣運瓶 | 裂瓶金光 | luck risk。 |
| 失敗者契約 | 黑紅契約 | curse。 |
| 英雄仇恨名單 | 怨念名冊 | aggro。 |
| 假結局邀請函 | 白門票 | Creator 伏筆。 |

---

## 7. 消耗品 Icon

| 名稱 | 主物件 | 用途 |
|---|---|---|
| 小怨念糖 | 紫色糖果 | 回怨念。 |
| 破碎飯糰 | 裂飯糰 | 回 HP。 |
| 臨時護符 | 小護符 | 短護盾。 |
| 倒楣煙霧彈 | 小煙球 | 脫身。 |
| 過期仙豆 | 皺豆子 | 回血但可能副作用。 |
| 反派便當 | 黑紫便當 | 回復 + 吐槽。 |
| 一次性怨雷 | 小雷瓶 | 一次攻擊。 |
| 小型 Eraser 碎屑 | 白色橡皮碎 | 清除小陷阱。 |
| 假主角光環 | 塑膠裂光環 | 一次保命。 |
| 緊急退場符 | 燒焦符紙 | 逃離事件。 |

---

## 8. Buff / Debuff Icon

| 狀態 | Icon | 色彩 |
|---|---|---|
| 霸體 | 小紫盾 + 拳頭 | 紫金。 |
| 禁療 | 裂心被火包住 | 紫紅。 |
| 緩速 | 腳下黏液 / 網 | 白紫。 |
| 燃燒 | 小紫火 | 橘紫。 |
| 束縛 | 蛛線纏身 | 白紫。 |
| 破甲 | 裂盾 | 鋼灰紫。 |
| 破隱 | 眼睛 + 影子 | 黑紫金。 |
| 氣運破裂 | 裂金星 | 金紫。 |
| Erased | 白頁擦痕 | 白灰。 |
| 詛咒 | 暗紅裂印 | 紅黑。 |

---

## 9. 關卡節點 Icon

| 節點 | 主物件 | 色彩 |
|---|---|---|
| 普通戰鬥 | 小怨爪 | 紫黑。 |
| 精英戰 | 裂冠 | 金紫。 |
| 事件 | 破卷軸 | 灰紫。 |
| 商店 | 怨幣袋 | 紫金。 |
| 休息 | 破營火 | 橘紫。 |
| Boss | 裂英雄徽記 | 金白裂紫。 |
| Creator | 白頁王座 | 白灰黑框。 |
| 寶箱 | 裂寶箱 | 金紫。 |
| 詛咒房 | 暗紅門 | 紅黑紫。 |

---

## 10. Boss 徽記 Icon

Boss 徽記不要使用既有作品標誌，要用原創抽象符號。

| Boss | 徽記方向 |
|---|---|
| M先生 | 彎水管 + 裂地。 |
| 滅影忍者 | 紙影月牙 + 分身裂片。 |
| U-man | 藍核心 + 放射光裂。 |
| 鋼筋戰士 | 五片無標誌裝甲合成裂盾。 |
| 葫蘆爺 | 葫蘆口 + 七色小點，不做既有造型。 |
| 消炎 | 丹火 + 裂藥爐。 |
| 失敗的面 | 城市屋簷 + 斷蛛線。 |
| 吾空 | 小拳頭 + 爆氣環。 |
| Creator | 白頁王座 + 擦除痕。 |

---

## 11. 稀有度框設計

### 11.1 框體規則

稀有度框與 Icon 分離，方便同一 Icon 套不同稀有度或升級版本。

| 稀有度 | Frame |
|---|---|
| Common | 單層圓角淡紫框。 |
| Rare | 雙層藍紫框，有小亮點。 |
| Epic | 金紫裂光框，角落有怨念煙。 |
| Legendary | 黑金厚框，外圈像王冠裂片。 |
| Cursed | 暗紅黑框，不規則裂邊。 |
| Joke | 粉紫圓胖框，帶滑稽裂痕。 |

### 11.2 Frame Prompt

```text
original mobile game item rarity frame, cute dark-comedy roguelite style, rounded square border, black purple ghost energy, cracked gold accents, transparent center, clean readable frame, no text, no logo, no trademark
```

---

## 12. Icon 變體規格

### 12.1 升級變體

技能升級可用 3 種方式表現：

| 方式 | 說明 |
|---|---|
| 外框變化 | 不改 Icon，本體套升級框。 |
| 小角標 | 加小裂星、火苗、蛛線等角標。 |
| 色彩強化 | 黑紫能量更亮，金裂更多。 |

### 12.2 不建議

- 每一級都重畫完全不同 Icon。
- 小角標放文字數字。
- 升級後失去原本技能輪廓。

---

## 13. Icon 命名規則

### 13.1 檔名

```text
icon_skill_[skill_id].png
icon_relic_[relic_id].png
icon_item_[item_id].png
icon_buff_[buff_id].png
icon_node_[node_type].png
icon_boss_[boss_id].png
frame_rarity_[rarity].png
```

### 13.2 範例

```text
icon_skill_pipe_impact.png
icon_skill_shadow_dash.png
icon_relic_villain_script_draft.png
icon_relic_borrowed_life_revenge.png
icon_item_broken_riceball.png
icon_buff_broken_luck.png
icon_node_elite.png
icon_boss_m_sir.png
frame_rarity_legendary.png
frame_rarity_cursed.png
```

---

## 14. 資料夾規劃

```text
assets/ui/icons/
  skills/
  relics/
  items/
  buffs/
  nodes/
  bosses/
  frames/
  raw/
  export/
```

建議：

- `raw/` 放 AI 原圖與手修檔。
- `export/` 放遊戲實際使用檔。
- 透明 PNG 優先。
- 保留 1024 master，另輸出 512、256、128、64。

---

## 15. AI 生圖工作流

### 15.1 流程

```text
列出功能 → 決定主物件 → 決定標籤視覺 → 生成 4～8 張 → 選輪廓最好的一張 → 去背 → 套稀有度框 → 縮小測試 → 導入 UI
```

### 15.2 縮小測試

每張 Icon 必須測：

- 1024px：細節是否好看。
- 256px：UI 卡片是否清楚。
- 128px：戰鬥 HUD 是否清楚。
- 64px：Buff / 小格是否清楚。
- 32px：如果不清楚，不要用於小狀態列。

### 15.3 選圖標準

優先選：

- 主輪廓最清楚。
- 物件最置中。
- 顏色最不髒。
- 沒有文字或奇怪符號。
- 小尺寸仍能辨識。

不要只選大圖最漂亮的一張。

---

## 16. Icon 與 UI 對應

| UI 場景 | Icon 使用方式 |
|---|---|
| 戰鬥 HUD | 技能 Icon + 冷卻遮罩。 |
| 三選一 | Icon + 稀有度框 + 標籤。 |
| 商店 | 商品 Icon + 價格。 |
| 事件 | 選項代價 Icon。 |
| 圖鑑 | 已解鎖 Icon 亮，未解鎖剪影。 |
| 結算 | 本局 Build 標籤 Icon。 |
| Boss 血條 | Boss 徽記 + Phase。 |

---

## 17. MVP Icon 範圍

第一版只做必要 Icon。

### 17.1 必做技能 Icon

- 怨念爪擊。
- Dash。
- 管線衝擊。
- 影遁衝刺。
- 氣運破裂。

### 17.2 必做道具 / 遺物 Icon

- 怨念小石頭。
- 破斗篷別針。
- 黑影鞋墊。
- 二手訓練沙包。
- 低亮度寶石。
- 背後的黑手。
- 震盪怨骨。
- 分身驗屍單。
- 遲到的主角光環。
- 反派劇本原稿。
- 借命復仇。
- 施工不同意。
- 影縫短刃。
- 神秘垃圾桶。
- 假主角光環。

### 17.3 必做消耗品 Icon

- 破碎飯糰。
- 小怨念糖。
- 臨時護符。

### 17.4 必做節點 Icon

- 普通戰鬥。
- 精英戰。
- 商店。
- 事件。
- Boss。
- 休息。

### 17.5 必做 Boss 徽記

- M先生。
- 滅影忍者。
- Creator 可先做灰階伏筆版。

---

## 18. 風格一致性檢查

### 18.1 同一批 Icon 必須一致

檢查：

- 外框厚度一致。
- 光影方向一致。
- 主物件大小一致。
- 稀有度色彩一致。
- 背景深度一致。
- 黑紫怨念特效一致。

### 18.2 不同類型要可分辨

| 類型 | 差異 |
|---|---|
| 技能 | 動態、斜線、能量感強。 |
| 遺物 | 物件感，較穩定。 |
| 消耗品 | 可愛、小、直覺。 |
| Buff | 簡化符號，不塞細節。 |
| Boss 徽記 | 更像章紋，但不能變商標。 |

---

## 19. Icon Data 草案

```json
{
  "id": "icon_skill_pipe_impact",
  "type": "skill",
  "sourceId": "pipe_impact",
  "tags": ["impact", "ground", "anti_stealth"],
  "rarityFrame": null,
  "asset": "assets/ui/icons/skills/icon_skill_pipe_impact.png",
  "smallReadable": true,
  "notes": "水管 + 地裂必須清楚。"
}
```

```json
{
  "id": "icon_relic_delayed_hero_aura",
  "type": "relic",
  "sourceId": "delayed_hero_aura",
  "tags": ["luck", "survival"],
  "rarityFrame": "epic",
  "asset": "assets/ui/icons/relics/icon_relic_delayed_hero_aura.png",
  "smallReadable": true,
  "notes": "歪掉的金色光環，帶黑紫裂紋。"
}
```

---

## 20. 驗收清單

每個 Icon 完成後檢查：

- 64px 是否看得懂？
- 主物件是否置中？
- 是否沒有文字、數字、Logo？
- 是否沒有既有 IP 符號？
- 是否符合黑紫怨念 + 裂金氣運風格？
- 是否能看出功能？
- 是否和標籤視覺語言一致？
- 稀有度框是否清楚？
- 放在三選一卡片上是否好讀？
- 放在戰鬥 HUD 上是否不混亂？
- 是否可切透明 PNG？
- 是否不依賴細節才能辨識？

---

## 21. 最終 Icon 規格句

```text
《氣運復仇者》的 Icon 必須像一張很小的復仇證據：玩家看到它，就知道這個能力從哪裡搶來、能打誰、代價是什麼。
```

如果 Icon 只能看出「很炫」，卻看不出功能，就不是合格 Icon。
