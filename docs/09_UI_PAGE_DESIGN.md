# 09｜UI 頁面設計 V1

專案：《氣運復仇者》 / QiYun Avengers

用途：固定遊戲整體 UI 風格、主要頁面、HUD、卡片、按鈕、關卡節點、商店、事件、結算與圖鑑頁的設計方向，作為後續 Web / Godot / Mobile 實作依據。

> 本文件接續：
>
> - `01_GAME_OVERVIEW.md`
> - `02_GAMEPLAY.md`
> - `03_ART_DIRECTION.md`
> - `04_BOSS_AND_MINIONS.md`
> - `05_LEVEL_AND_MAP_DESIGN.md`
> - `06_CHARACTER_PROMPT_DESIGN.md`
>
> UI 核心：**讓玩家一眼看懂戰鬥、Build、復仇進度與氣運被搶走的爽感。**

---

## 0. UI 核心風格

### 0.1 風格定位

《氣運復仇者》的 UI 不是嚴肅黑暗，也不是純可愛卡通。

核心方向：

```text
可愛黑色幽默 + 反英雄復仇 + 黑紫怨念 + 被扭曲的金白正義光
```

UI 要看起來像：

- 可愛手機動作遊戲。
- Roguelite 卡片選擇遊戲。
- 黑紫怨念從英雄金光底下滲出。
- 乾淨、可讀、手機友善。
- 不依賴大量文字也能操作。

### 0.2 視覺關鍵字

```text
cute dark-comedy mobile game UI, chibi revenge fantasy, black purple ghost energy, cracked golden hero light, clean rounded panels, thick soft outlines, readable card layout, playful but sinister, high contrast, mobile portrait friendly
```

### 0.3 UI 不做方向

避免：

- 過度寫實恐怖介面。
- 太多骷髏、血、殘酷符號。
- 金色英雄 UI 過度華麗，蓋掉 Ghost 怨念主題。
- 大量小字塞滿手機畫面。
- 背景太花，導致按鈕與卡片看不清楚。
- 使用既有 IP 標誌、符號、辨識性版型。
- 使用拼裝玩具式手部、關節、零件外觀作為 UI 圖示。

---

## 1. 共通 UI Prompt

### 1.1 頁面共通 Prompt

```text
original cute dark-comedy mobile game UI page design for a chibi roguelite action game, black purple ghost revenge theme, cracked golden hero light accents, rounded panels, thick soft outlines, readable mobile portrait layout, playful sinister fantasy, clean hierarchy, high contrast buttons, card-based roguelite interface, no text, no logo, no trademark, no recognizable IP symbols, game-ready UI mockup
```

### 1.2 HUD 共通 Prompt

```text
original mobile action roguelite battle HUD, cute dark fantasy UI, black purple ghost energy HP and skill meters, cracked golden luck pressure accents, clean readable icons, minimal screen obstruction, rounded buttons for touch controls, high contrast cooldown indicators, boss health bar, mobile portrait friendly, no text, no logo, no trademark
```

### 1.3 卡片共通 Prompt

```text
original roguelite skill choice card UI, cute dark-comedy fantasy style, black purple frame with cracked gold highlights, centered icon area, clear rarity frame, readable title area placeholder, description area placeholder, soft thick outline, mobile friendly, no readable text, no logo, no trademark, game-ready asset
```

### 1.4 共通 Negative Prompt

```text
low quality, blurry, messy layout, unreadable tiny UI, too many details, realistic horror, gore, blood, text, letters, numbers, watermark, signature, trademark logo, recognizable IP, copyrighted character symbols, C-shaped toy hands, visible toy joints, construction toy minifigure proportions, cluttered background, low contrast, hard to read buttons
```

---

## 2. 色彩系統

### 2.1 主色

| 色彩 | 用途 | 感覺 |
|---|---|---|
| 黑紫 | Ghost、怨念、主 UI 底色 | 反英雄、深處怨氣。 |
| 深藍紫 | 面板、背景陰影 | 穩定、夜色。 |
| 裂金 | 英雄氣運、稀有獎勵 | 被搶走的主角光環。 |
| 灰白 | 文字區、白頁、Creator | 規則、命運、刪除。 |
| 暗紅 | 詛咒、危險、低血量 | 代價、警告。 |
| 亮藍 | 核心能量、科技、U-man | 光束、核心。 |

### 2.2 陣營色

| 陣營 / 系統 | 色彩方向 |
|---|---|
| Ghost | 黑、紫、幽藍、少量白光。 |
| 英雄氣運 | 金、白、亮黃，但要帶裂紋。 |
| Boss | 依 Boss 主題加入專屬色。 |
| Creator | 白、灰、黑框、橡皮擦痕。 |
| 危險提示 | 橘紅 / 紅紫，外圈清楚。 |
| 可互動物 | 淡金閃光或紫色呼吸。 |

### 2.3 稀有度色彩

| 稀有度 | 色彩方向 | UI 感覺 |
|---|---|---|
| Common | 灰白 / 淡紫 | 穩定、普通。 |
| Rare | 藍紫 | 有功能感。 |
| Epic | 金紫 | Build 成形。 |
| Legendary | 黑金 | 規則改變。 |
| Cursed | 暗紅黑紫 | 強但有代價。 |
| Joke | 粉紫 / 可愛亮色 | 黑色幽默。 |

---

## 3. 字體與排版

### 3.1 字體方向

建議使用：

- 標題：圓潤、厚重、帶一點手寫感。
- 正文：高可讀性無襯線。
- 數字：清楚，不要過度裝飾。
- 英文 Logo：`QIYUN AVENGERS` 可走黑紫裂光 + 金白裂痕。

### 3.2 排版原則

| 元素 | 原則 |
|---|---|
| 標題 | 大、短、清楚，不超過兩行。 |
| 描述 | 行距寬，不要塞滿。 |
| 數值 | 靠近圖示，避免玩家找不到。 |
| 按鈕 | 手機最小觸控區足夠。 |
| 卡片 | Icon > 名稱 > 效果 > 標籤。 |
| HUD | 不遮擋角色與 Boss 攻擊提示。 |

---

## 4. 主要頁面總覽

| 頁面 | MVP | 用途 |
|---|---|---|
| 首頁 / Title Screen | 是 | 進入遊戲與建立第一印象。 |
| 關卡選擇頁 / Stage Select | MVP 簡化 | Roguelite 路線選擇。 |
| 角色構築頁 / Character Build | 可簡化 | 顯示當局技能與遺物。 |
| 戰鬥 HUD | 是 | 操作、血量、技能、Boss 血條。 |
| 升級三選一頁 / Level Up Choice | 是 | Roguelite Build 核心。 |
| 商店 / Shop | 是 | 消耗怨幣換取補給與 Build。 |
| 事件頁 / Event | 是，可簡化 | 風險收益選擇。 |
| 勝利頁 / Victory | 是 | Boss 擊敗與技能奪取。 |
| 失敗頁 / Defeat | 是 | 死亡原因、重開、黑色幽默。 |
| 圖鑑頁 / Archive | 可延後 | 長期收集與世界知識。 |
| 設定頁 / Settings | 是，簡化 | 音量、重新開始、操作。 |

---

## 5. 首頁 / Title Screen

### 5.1 目標

首頁要 3 秒內讓玩家知道：

```text
這是一款可愛但怨念很深的反英雄復仇 Roguelite。
```

### 5.2 畫面構成

| 區域 | 內容 |
|---|---|
| 背景 | 黑紫怨念雲、遠處金白英雄光裂開。 |
| 中央 | Ghost 小小站在光與影交界。 |
| Logo | QIYUN AVENGERS / 氣運復仇者。 |
| 主按鈕 | Start / 開始復仇。 |
| 次按鈕 | Continue、Archive、Settings。 |
| 版本資訊 | 角落小字，低干擾。 |

### 5.3 首頁按鈕

| 按鈕 | 功能 | 文案方向 |
|---|---|---|
| 開始復仇 | 新局 | 主要 CTA。 |
| 繼續怨念 | 讀取 | 有存檔才亮。 |
| 敗者圖鑑 | 圖鑑 | 查看 Boss / 小怪 / 道具。 |
| 音量與設定 | 設定 | 音效、BGM、操作。 |

### 5.4 首頁 Prompt

```text
original title screen UI for a cute dark-comedy chibi roguelite action game, tiny ghost protagonist standing under cracked golden hero light, black purple mist, playful sinister fantasy, large logo area, big rounded start button, clean mobile portrait layout, no readable text, no trademark, no recognizable IP symbols, game-ready mockup
```

---

## 6. 關卡選擇頁 / Stage Select

### 6.1 目標

讓玩家選擇路線時看懂：

- 下一房是戰鬥、事件、商店、精英還是 Boss。
- 哪條路比較安全。
- 哪條路獎勵更高。
- 當前氣運壓力是否危險。

### 6.2 節點類型

| 節點 | Icon | 說明 |
|---|---|---|
| 普通戰鬥 | 小怨爪 | 基礎小怪房。 |
| 精英戰 | 裂冠 | 強敵與高獎勵。 |
| 事件 | 破卷軸 | 風險選擇。 |
| 商店 | 怨幣袋 | 購買補給 / 遺物。 |
| 休息 | 破營火 | 回復或升級。 |
| Boss | 裂開英雄徽記 | Boss 戰。 |
| Creator | 白頁王座 | Final Boss。 |

### 6.3 UI 佈局

```text
上方：當前地圖名、氣運壓力、怨幣
中間：節點路線圖
下方：當前 Build 摘要、返回 / 確認
```

### 6.4 MVP 簡化版

MVP 可以先不用完整 Slay-the-Spire 式地圖，只做 2～3 個選項卡：

```text
安全路：普通戰鬥
風險路：精英 / 事件
商店路：商店 / 補給
```

---

## 7. 角色構築頁 / Character Build

### 7.1 目標

讓玩家看懂本局 Ghost 目前靠什麼活著。

### 7.2 內容

| 區域 | 內容 |
|---|---|
| 左側 / 中央 | Ghost 當前形象。 |
| 技能區 | 普攻、Dash、主動技能、冷卻。 |
| 遺物區 | 已持有遺物 Icon Grid。 |
| 標籤區 | impact / shadow / flame 等 Build 標籤。 |
| 數值區 | HP、怨念、氣運壓力、怨幣。 |

### 7.3 Build 標籤顯示

| 標籤 | 顯示方式 |
|---|---|
| impact | 地裂小圖示。 |
| shadow | 黑影殘影。 |
| core | 藍核裂光。 |
| armor_break | 破盾裂紋。 |
| devour | 葫蘆吸入旋渦。 |
| flame | 紫黑火苗。 |
| web | 蛛線節點。 |
| ki | 霸體氣焰。 |
| curse | 暗紅裂印。 |
| erase | 白色擦除痕。 |

---

## 8. 戰鬥 HUD

### 8.1 HUD 核心原則

戰鬥 HUD 必須：

- 不遮擋角色。
- 不遮擋 Boss 攻擊前搖。
- 技能冷卻清楚。
- HP / 怨念一眼可見。
- 手機按鈕大且不誤觸。

### 8.2 Mobile HUD 佈局

```text
左上：Ghost HP / 怨念
上方中央：Boss 血條
右上：氣運壓力 / 小地圖可延後
左下：虛擬搖桿
右下：普攻、Dash、主動技能
下方中央：當前狀態提示 / 破防提示
```

### 8.3 PC / Web HUD 佈局

```text
左上：HP / 怨念 / Buff
上方中央：Boss 血條
右上：關卡進度 / 怨幣
下方中央：技能列與快捷鍵
```

### 8.4 HUD 元件

| 元件 | 規格 |
|---|---|
| HP Bar | 黑紫底，受傷時紅紫閃。 |
| 怨念 Bar | 紫色能量條，滿時微微發光。 |
| Boss HP | 金白外框，受破防時裂開黑紫。 |
| 技能按鈕 | 圓角大按鈕，冷卻用灰紫遮罩。 |
| Dash | 獨立按鈕，可顯示充能點。 |
| 氣運壓力 | 小型裂金儀表，越高裂痕越多。 |

### 8.5 破防提示

當相剋命中：

```text
畫面中央短暫顯示：氣運破裂 / BROKEN LUCK
Boss 血條外框裂開
播放黑紫反吸特效
SFX：golden crack + purple reverse pull
```

提示時間：0.8～1.2 秒，不要太久。

---

## 9. 升級三選一頁 / Level Up Choice

### 9.1 目標

三選一頁是 Roguelite Build 的核心，必須讓玩家快速比較：

- 這個選項強化哪個技能？
- 是傷害、功能、風險還是聯動？
- 稀有度如何？
- 代價是什麼？

### 9.2 版面

```text
上方：標題「選擇一份怨念」
中間：三張大卡
下方：重骰 / 跳過 / 當前 Build 標籤
```

### 9.3 卡片結構

| 區域 | 內容 |
|---|---|
| 稀有度框 | Common / Rare / Epic / Legendary / Cursed。 |
| Icon | 道具或技能圖示。 |
| 名稱 | 短名稱。 |
| 效果 | 1～2 行。 |
| 標籤 | impact / shadow / curse 等。 |
| 代價 | Cursed 或高風險選項才顯示。 |

### 9.4 卡片視覺

| 類型 | 視覺 |
|---|---|
| 技能強化 | 技能 Icon 放大，背景有技能元素。 |
| 遺物 | 物件 Icon，外框看稀有度。 |
| 詛咒 | 暗紅黑紫裂紋，代價區明顯。 |
| 聯動 | 兩個標籤在卡底交叉發光。 |

---

## 10. 商店頁 / Shop

### 10.1 商店定位

商店不是高級精品店，而是「反派在垃圾堆裡買希望」。

聽感與視覺：

- 可愛。
- 有點黑。
- 很會吐槽。
- 價格清楚。

### 10.2 版面

```text
上方：商店名、怨幣數量
中間：商品 5 格
右側 / 下方：商品詳情
底部：離開商店
```

### 10.3 商品格

| 類型 | 顯示 |
|---|---|
| 回血 | 飯糰 / 破碎補給。 |
| 回怨念 | 怨念糖。 |
| 遺物 | Icon + 稀有度框。 |
| 技能升級 | 技能標籤 + 升級符號。 |
| 神秘商品 | 垃圾桶 / 問號 / 詛咒陰影。 |

### 10.4 購買狀態

| 狀態 | UI |
|---|---|
| 可購買 | 正常亮度。 |
| 已購買 | Sold Out 裂印，可用圖示代替文字。 |
| 錢不夠 | 灰紫暗化，怨幣圖示抖一下。 |
| 詛咒商品 | 邊框微微跳動。 |

---

## 11. 事件頁 / Event

### 11.1 事件頁定位

事件頁提供風險選擇，不是純劇情閱讀。

### 11.2 版面

```text
上方：事件插圖 / 小場景
中間：事件描述
下方：2～3 個選項按鈕
角落：當前 HP / 怨幣 / 氣運壓力
```

### 11.3 選項顯示

| 選項類型 | 顯示 |
|---|---|
| 安全低收益 | 灰紫框。 |
| 高收益 | 金紫框。 |
| 詛咒 | 暗紅框。 |
| 花錢 | 怨幣圖示。 |
| 犧牲 HP | HP 心裂圖示。 |
| 降低氣運壓力 | 裂金變淡圖示。 |

### 11.4 範例事件 UI

```text
事件：英雄補給箱
插圖：裂開的金白箱子，Ghost 探頭看
選項 A：打開它，回血但氣運壓力上升
選項 B：砸碎它，獲得怨幣但下房小怪變多
選項 C：假裝沒看到，什麼都不發生
```

---

## 12. 勝利頁 / Victory

### 12.1 小勝利：房間通過

顯示：

- 房間完成。
- 掉落怨幣。
- 補給。
- 是否出現三選一。

### 12.2 Boss 勝利

Boss 勝利是重點演出。

流程：

```text
Boss 倒下
  ↓
金白氣運裂開
  ↓
Ghost 吸收黑紫化
  ↓
技能 Icon 出現
  ↓
顯示技能名稱與一句吐槽
  ↓
進入技能教學或下一關
```

### 12.3 Boss Skill Unlock UI

| 區域 | 內容 |
|---|---|
| 中央 | 新技能 Icon 大圖。 |
| 上方 | Boss 名稱 / 被奪取。 |
| 中段 | 技能名稱。 |
| 下方 | 技能效果短句。 |
| 背景 | Boss 專屬顏色被黑紫侵染。 |

### 12.4 文案方向

```text
你奪走了：管線衝擊
英雄的路，現在會從地底反咬回去。
```

---

## 13. 失敗頁 / Defeat

### 13.1 目標

失敗頁要做到：

- 告訴玩家死因。
- 給一點黑色幽默。
- 讓玩家快速重開。
- 顯示本局學到了什麼。

### 13.2 版面

```text
上方：死亡標題 / Ghost 散掉動畫
中間：死因、擊敗敵人數、打到第幾關
下方：本局 Build 標籤、獲得殘響、重開按鈕
```

### 13.3 死因卡片

| 死因 | UI 提示 |
|---|---|
| 貪刀 | 顯示最後攻擊來源與「攻擊後搖」。 |
| 沒看陷阱 | 顯示陷阱 Icon。 |
| 被分身騙 | 顯示真假影子。 |
| 被 Boss 大招 | 顯示 Boss 招式 Icon。 |
| 被 Eraser | 顯示白頁擦除痕。 |

### 13.4 按鈕

| 按鈕 | 功能 |
|---|---|
| 再復仇一次 | 快速重開。 |
| 回首頁 | 回 Title。 |
| 看死因 | 打開本局摘要。 |
| 圖鑑 | 可延後。 |

---

## 14. 圖鑑頁 / Archive

### 14.1 圖鑑定位

圖鑑是長期知識庫，不是單純收藏頁。

它記錄：

- Boss。
- 小怪。
- 陷阱。
- 遺物。
- 技能。
- 死亡方式。
- Creator 干涉。

### 14.2 圖鑑分類

| 分類 | 顯示 |
|---|---|
| 英雄檔案 | Boss 肖像、招式、已知弱點。 |
| 小怪檔案 | 小怪功能、出現關卡。 |
| 遺物收藏 | 已拿過 / 未拿過。 |
| 技能紀錄 | 已奪取技能。 |
| 死亡紀錄 | 被哪招殺死過。 |
| 劇本碎片 | Creator 相關線索。 |

### 14.3 解鎖狀態

| 狀態 | UI |
|---|---|
| 未遇過 | 黑影剪影。 |
| 遇過 | 顯示名字與剪影。 |
| 被殺過 | 顯示死因提示。 |
| 擊敗過 | 顯示完整資訊。 |
| 完整研究 | 顯示相剋與吐槽。 |

---

## 15. 設定頁 / Settings

### 15.1 MVP 必做

| 設定 | 說明 |
|---|---|
| Master Volume | 總音量。 |
| BGM Volume | 音樂。 |
| SFX Volume | 音效。 |
| UI Volume | UI 音效。 |
| 操作方式 | 觸控 / 鍵盤提示。 |
| 語言 | 初期可固定中文。 |
| 重新開始 | 當局重開。 |

### 15.2 可延後

- 無障礙完整設定。
- 自訂按鍵。
- 畫質選項。
- 難度細項。
- 色盲模式。

---

## 16. UI 元件設計

## 16.1 按鈕

### 16.1.1 按鈕類型

| 類型 | 用途 | 視覺 |
|---|---|---|
| Primary | 開始、確認、選擇 | 黑紫底 + 裂金邊。 |
| Secondary | 返回、略過 | 深灰紫底。 |
| Danger | 放棄、詛咒選項 | 暗紅裂紋。 |
| Disabled | 不可用 | 灰紫半透明。 |
| Icon Button | 戰鬥操作 | 圓形大按鈕。 |

### 16.1.2 按鈕狀態

| 狀態 | 視覺 |
|---|---|
| Normal | 穩定發光。 |
| Hover / Focus | 邊框變亮。 |
| Pressed | 按鈕下沉，怨念小爆。 |
| Disabled | 灰暗，無發光。 |
| Warning | 暗紅脈衝。 |

---

## 16.2 血條 / 能量條

### 16.2.1 Ghost HP

視覺：黑紫容器 + 紅紫受傷閃光。

受傷時：

- HP 條先快速掉一段。
- 延遲殘影條慢慢追上。
- Ghost 頭像抖一下。

### 16.2.2 怨念值

視覺：紫色流動液體。

滿值時：

- 技能按鈕微微發光。
- 怨念條出現小鬼臉氣泡。

### 16.2.3 Boss 血條

視覺：金白英雄框 + 黑紫裂痕。

破防時：

- 金框碎裂。
- 血條下方顯示破防狀態。
- 音效與畫面同步。

---

## 16.3 技能卡 / 道具卡

### 16.3.1 卡片尺寸

手機直式建議：

| 卡片類型 | 尺寸方向 |
|---|---|
| 三選一卡 | 螢幕寬度 28～32%，高度 45～55%。 |
| 商店商品卡 | 螢幕寬度 40～45%，高度 20～25%。 |
| 道具詳情卡 | 螢幕寬度 80～90%。 |
| 圖鑑卡 | Grid，小卡 + 詳情頁。 |

### 16.3.2 卡片資訊層級

```text
Icon 最大
名稱第二
效果第三
標籤第四
Flavor text 可藏在詳情頁
```

---

## 16.4 稀有度框

| 稀有度 | 外框規格 |
|---|---|
| Common | 單層淡紫框。 |
| Rare | 藍紫雙層框。 |
| Epic | 金紫裂光框。 |
| Legendary | 黑金厚框，有低頻脈衝。 |
| Cursed | 暗紅裂紋框，邊緣像被咬掉。 |
| Joke | 圓潤粉紫框，帶滑稽小裂痕。 |

---

## 16.5 Boss 血條

### 16.5.1 結構

```text
Boss 名稱
Phase 小刻度
主血條
破防 / 狂暴 / 氣運反撲狀態
```

### 16.5.2 Phase 表示

- 65% 與 30% 位置可有小裂痕刻度。
- 進 Phase 時血條外框短暫亮金。
- 被相剋破防時亮金被黑紫吞掉。

---

## 16.6 關卡節點

| 節點 | 形狀 |
|---|---|
| 普通戰鬥 | 小圓節點。 |
| 精英 | 裂冠節點。 |
| 商店 | 怨幣袋節點。 |
| 事件 | 破卷軸節點。 |
| 休息 | 小營火節點。 |
| Boss | 大裂徽節點。 |
| Creator | 白頁王座節點。 |

---

## 17. 手機 UI 安全區

### 17.1 直式畫面

優先支援手機直式。

建議：

- 左下搖桿不超過螢幕高 25%。
- 右下技能按鈕保留拇指區。
- Boss 血條固定上方，避免遮角色。
- 三選一卡片可上下滑看詳情，但選擇按鈕固定。

### 17.2 橫式畫面

可延後，但如果支援：

- HUD 更靠邊。
- 技能列可橫排。
- Boss 血條可放上方中央。

---

## 18. UI 動效

### 18.1 共通動效

| 動作 | 動效 |
|---|---|
| 按鈕點擊 | 下沉 + 小怨念 pop。 |
| 卡片出現 | 從黑紫煙中翻開。 |
| 選中卡片 | 外框裂金亮起，再被黑紫吸收。 |
| Boss 破防 | UI 金框碎裂。 |
| 技能冷卻完成 | Icon 呼吸亮一下。 |
| 死亡 | UI 變暗，文字像被怨念包住。 |
| Eraser | UI 部分短暫白頁擦過，但不可影響操作。 |

### 18.2 動效時間

| 動效 | 時間 |
|---|---:|
| 按鈕回饋 | 0.08～0.15 秒 |
| 卡片翻開 | 0.25～0.45 秒 |
| 三選一進場 | 0.4～0.8 秒 |
| Boss 破防提示 | 0.8～1.2 秒 |
| 技能解鎖 | 1.5～3.0 秒 |
| 死亡轉場 | 1.0～2.0 秒 |

---

## 19. MVP UI 範圍

### 19.1 必做

| UI | 內容 |
|---|---|
| 首頁 | 開始、設定。 |
| Battle HUD | HP、怨念、Boss 血條、普攻、Dash、技能。 |
| 技能解鎖頁 | 管線衝擊、影遁衝刺。 |
| 三選一頁 | 3 張卡、選擇、跳過可選。 |
| 商店 | 5 商品格、怨幣、購買。 |
| 事件頁 | 插圖、描述、2～3 選項。 |
| 死亡頁 | 死因、進度、重開。 |
| 勝利頁 | Boss 擊敗、下一關。 |
| 設定頁 | 音量與返回。 |

### 19.2 可延後

- 完整圖鑑。
- 完整角色構築頁。
- 外觀收藏。
- 高難模式 UI。
- 成就頁。
- 多語言切換。

---

## 20. UI 資料結構草案

### 20.1 Card UI

```json
{
  "id": "relic_resentment_stone",
  "type": "relic",
  "rarity": "common",
  "icon": "icon_relic_resentment_stone",
  "nameKey": "relic.resentment_stone.name",
  "descKey": "relic.resentment_stone.desc",
  "tags": ["survival", "resentment"],
  "cost": null
}
```

### 20.2 HUD Skill Button

```json
{
  "slot": "active_1",
  "skillId": "pipe_impact",
  "icon": "icon_skill_pipe_impact",
  "cooldown": 6,
  "costType": "resentment",
  "cost": 20,
  "input": "R2"
}
```

### 20.3 Stage Node

```json
{
  "id": "node_stage_01_elite_01",
  "type": "elite",
  "icon": "icon_node_elite",
  "risk": "high",
  "rewardHint": "rare_relic",
  "next": ["node_shop_01", "node_boss_01"]
}
```

---

## 21. UI 驗收清單

每個 UI 頁面完成後檢查：

- 手機上是否看得清楚？
- 主要按鈕是否一眼可見？
- 玩家是否知道下一步要按哪裡？
- 戰鬥 HUD 是否不遮擋角色與危險提示？
- 三選一卡片是否能快速比較？
- 稀有度是否不用讀文字也能分辨？
- 商店價格是否清楚？
- 死亡頁是否告訴玩家死因？
- 勝利頁是否有搶能力爽感？
- 是否符合黑紫怨念 + 裂金正義主題？
- 是否沒有商標、Logo、既有 IP 符號？
- 是否能直接拆成 UI asset？

---

## 22. 最終 UI 規格句

```text
《氣運復仇者》的 UI 必須讓玩家感覺：我不是在管理一堆數值，而是在把英雄身上的氣運一片一片撬下來。
```

如果 UI 漂亮但沒有傳達「復仇、奪取、相剋、黑色幽默」，就需要重做。
