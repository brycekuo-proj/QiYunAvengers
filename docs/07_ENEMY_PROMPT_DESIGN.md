# 07｜小怪設計 Prompt V1

專案：《氣運復仇者》

用途：建立小怪的「外觀母 Prompt、Negative Prompt、動作表 Prompt、逐隻小怪生圖 Prompt」，方便後續批量產出角色設定圖、sprite sheet、animation-ready keyframes。

這份文件優先服務手機橫向動作遊戲 / roguelite 關卡小怪，不是單張插畫。小怪要比 Boss 更簡潔，主要負責提供關卡節奏、攻擊模式、阻擋、干擾與狀態異常。

---

## 0. 核心設計原則

- 美術方向：原創 Q 版、手機遊戲、可愛但帶壞心眼、黑色幽默復仇感。
- 小怪定位：每隻小怪都是一個清楚的功能符號，輪廓要比細節更重要。
- 關卡辨識：小怪要能一眼看出屬於哪個 Boss / 地圖陣營。
- 動畫優先：所有外觀都要能做 idle / walk / attack / hit / defeated。
- 量產友善：避免過度精細、避免太多小配件、避免特效遮住身體。
- 原創要求：不要直接生成任何既有 IP、真實人物、商標標誌、可辨識英雄符號或動漫角色造型。
- 手部規格：若小怪有人形手，統一使用圓潤饅頭手 / mitten hands，不使用積木玩具式夾手、卡榫、凸點或可拼接玩具細節。

---

## 1. 小怪共通母 Prompt

**Enemy Common Mother Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, cute but hostile expression, rounded mitten-like hands if hands exist, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, simple readable costume, consistent costume and color palette, animation-ready sprite design, suitable for mobile action RPG battle, readable at small size, full body visible, crisp outline, white background, no scenery, no complex background
```

### 使用方式

每隻小怪 prompt 前面都先加這段，再接「該小怪個別描述」。這段用來鎖定：

- Q 版手機遊戲敵人
- 小尺寸可讀性
- 全身角色
- 白底
- 可動畫化
- 不走寫實恐怖

---

## 2. 小怪共通 Negative Prompt

**Enemy Common Negative Prompt**

```text
low quality, blurry, noisy, messy lineart, cropped body, missing feet, cut off weapon, cut off effect, inconsistent costume, inconsistent color palette, inconsistent face, inconsistent hairstyle, inconsistent body size between poses, extra arms, extra legs, deformed hands, realistic gore, blood splatter, horror corpse detail, photorealistic human, real celebrity likeness, direct copy of existing copyrighted characters, recognizable franchise costume, trademark logo, recognizable superhero emblem, known anime or game character costume, letters or symbols from known IP, toy brick studs, interlocking brick compatibility details, C-shaped gripping hands, visible toy joints, plastic minifigure proportions, overly complex background, scenery background, UI frame, text, watermark, signature, speech bubble, random duplicate enemies, overlapping poses, messy action sheet, unreadable silhouette, too many tiny details
```

### 追加 Negative 條件

若模型開始跑偏，可按狀況追加：

```text
no toy brick, no famous character parody, no logo, no celebrity face, no realistic weapon violence, no horror gore, no background scene, no text labels
```

---

## 3. 小怪動作表共通 Prompt

**Enemy Action Sheet Common Prompt**

```text
Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle, walk, normal attack, skill attack, taking damage, and defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image.
```

### 動作表必含項目

- idle
- walk
- normal attack
- skill attack
- taking damage
- defeated

### 動作建議拆法

| 動作 | 建議 Pose 數 | 重點 |
| --- | ---: | --- |
| idle | 1～3 | 待機、漂浮、呼吸、閃爍、抖動 |
| walk | 2～4 | 左右腳或漂浮位移循環 |
| normal attack | 4 | 起手、揮出、命中、收招 |
| skill attack | 4～6 | 蓄力、釋放、特效、硬直 |
| taking damage | 3 | 受擊、後仰、回穩 |
| defeated | 3 | 暈倒、散煙、碎片、消散，不血腥 |

---

## 4. 輸出規格

每張小怪動作表必須符合：

- white background
- multiple small full-body poses
- clean grid
- consistent costume
- animation-ready keyframes
- idle / walk / normal attack / skill attack / taking damage / defeated

補充要求：

- 全身不可裁切，腳、尾巴、武器、特效都要完整。
- 每個 pose 之間要有足夠空白，方便後續裁切 sprite。
- 同一張 action sheet 中角色比例不可忽大忽小。
- 同一張 action sheet 中服裝、臉、顏色、武器不可變形或換款。
- 特效只能輔助動作，不要蓋住角色輪廓。
- 建議輸出正方形大圖，例如 2048x2048 或 3000x3000，再切圖。
- 若要給動畫師使用，優先保留每個 pose 的腳底位置與角色中心點。

---

## 5. 批量生圖模板

### 5.1 單隻小怪外觀圖模板

```text
[Enemy Common Mother Prompt], [specific enemy design], front three-quarter view, small full-body character, simple readable silhouette, clean character concept art, white background
```

### 5.2 單隻小怪動作表模板

```text
[Enemy Common Mother Prompt], [specific enemy design], [Enemy Action Sheet Common Prompt], idle / walk / normal attack / skill attack / taking damage / defeated, clean grid, multiple small full-body poses, consistent costume, animation-ready keyframes, white background
```

### 5.3 建議工作流

1. 先產出單隻小怪外觀定稿。
2. 從外觀定稿挑一張最穩定的圖當 reference。
3. 再生成 action sheet。
4. 若 action sheet 角色不一致，補上：

```text
same character in every frame, same costume in every frame, same face in every frame, same body size in every frame, same weapon in every frame
```

5. 若 pose 太擠，補上：

```text
large spacing between each pose, separated grid cells, no overlapping poses, each pose isolated
```

---

## 6. 小怪清單總覽

| 編號 | 小怪 | 所屬關卡 / 陣營 | 功能定位 | 視覺關鍵字 |
| ---: | --- | --- | --- | --- |
| 01 | 碎運鬼 | 怨念甦醒地 / Ghost 教學 | 近戰雜兵、教學敵人 | 破碎運勢符、灰紫小鬼、裂紋光 |
| 02 | 黑運糰 | 怨念甦醒地 / 負運群聚 | 滾動干擾、地面障礙 | 黑色糰子、霉運煙、倒楣表情 |
| 03 | 水管工僕 | 紅帽管線城 / M先生 | 近戰工具兵 | 小扳手、水管制服、紅帽陣營 |
| 04 | 噴氣水管兵 | 紅帽管線城 / M先生 | 遠程噴射、擊退 | 背管、蒸氣噴嘴、壓力錶 |
| 05 | 影紙忍 | 影村訓練場 / 滅影忍者 | 快速近戰、閃避 | 紙片身體、忍者剪影、墨影 |
| 06 | 飛鏢影童 | 影村訓練場 / 滅影忍者 | 遠程投射物 | 小忍童、飛鏢、紙影分身 |
| 07 | 藍核守衛球 | 藍核防衛基地 / U-man | 飛行巡邏、能量彈 | 白藍守衛球、藍核心、紅線條 |
| 08 | 小型正義盾 | 藍核防衛基地 / U-man | 格擋、保護其他怪 | 盾牌小兵、白紅藍、防禦姿態 |
| 09 | 螺絲工兵 | 鋼筋戰隊工廠 / 鋼筋戰士 | 修理、防禦建造 | 螺絲帽頭盔、工具包、金屬手套 |
| 10 | 磁鐵鋼怪 | 鋼筋戰隊工廠 / 鋼筋戰士 | 吸引、牽制、拉扯 | U 型磁鐵、鋼片身體、磁力線 |
| 11 | 小葫蘆童 | 七色葫蘆山 / 葫蘆爺 | 彈跳近戰、狀態小怪 | 小葫蘆帽、藤蔓腰帶、彩色葫蘆 |
| 12 | 彩霧葫蘆 | 七色葫蘆山 / 葫蘆爺 | 毒霧、混亂、遮蔽 | 漂浮葫蘆、彩霧、可愛危險感 |
| 13 | 丹火童子 | 異火煉藥宗 / 消炎 | 火焰小怪、灼燒區域 | 丹爐帽、藥火、火苗袖子 |
| 14 | 爆丹怪 | 異火煉藥宗 / 消炎 | 自爆、延遲爆炸 | 圓丹身體、裂光、倒數表情 |

> 目前使用者訊息在「丹」後被截斷，因此這版先補入「丹火童子」與「爆丹怪」作為煉藥宗小怪。若後續有完整清單，可再追加 15 之後。

---

## 7. 小怪個別 Prompt

### 7.1 碎運鬼

**定位**：教學地圖基本近戰敵人，讓玩家第一次學會打小怪與閃避。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, cute but hostile expression, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, simple readable costume, consistent costume and color palette, animation-ready sprite design, suitable for mobile action RPG battle, readable at small size, full body visible, crisp outline, white background, no scenery, no complex background, a tiny broken-luck ghost minion made of gray purple mist, cracked fortune talisman stuck on its forehead, small jagged smile, floating ragged lower body, tiny claw-like mitten hands, faint broken halo fragments around the head, cute unlucky ghost mood
```

**動作表 Prompt**

```text
碎運鬼 action sheet, idle floating with small unlucky smoke, walk as short hover dash, normal attack with tiny claw swipe, skill attack releasing cracked bad-luck talisman shockwave, taking damage with talisman flipping upward, defeated dissolving into gray purple smoke and broken luck fragments, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- idle：身體上下飄，符紙微抖。
- walk：短距離漂浮滑行。
- normal attack：小爪橫揮。
- skill attack：裂運符向前爆出小衝擊波。
- taking damage：符紙翻起、身體壓扁。
- defeated：化成灰紫煙，不血腥。

---

### 7.2 黑運糰

**定位**：低階地面干擾怪，適合成群出現。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, cute but hostile expression, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a round black bad-luck dumpling monster, soft squishy blob body, tiny angry dot eyes, unlucky smoke leaking from its head, small stubby feet, no sharp gore, cute annoying enemy, dark gray and purple palette, simple readable silhouette
```

**動作表 Prompt**

```text
黑運糰 action sheet, idle wobbling like a cursed dumpling, walk rolling and bouncing, normal attack body slam, skill attack leaving a small black unlucky puddle, taking damage squashed flat, defeated popping into harmless dark smoke, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- idle：圓身體左右晃。
- walk：滾動或彈跳。
- normal attack：身體撞擊。
- skill attack：留下小霉運黑泥，短時間減速。
- taking damage：被壓扁。
- defeated：像氣球漏氣消散。

---

### 7.3 水管工僕

**定位**：紅帽管線城近戰小兵，M先生的低階追隨者。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny pipe maintenance servant enemy, red cap without any logo, simple work overalls, round mitten hands, holding a small wrench, short boots, pipe-shaped backpack, smug justice-side worker expression, cute but hostile, original design, no recognizable mascot features
```

**動作表 Prompt**

```text
水管工僕 action sheet, idle tapping wrench on palm, walk short stomping steps, normal attack horizontal wrench swing, skill attack jumping and slamming wrench to make a small pipe shockwave, taking damage losing grip on wrench, defeated sitting dizzy with wrench dropped, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- normal attack：扳手橫揮，讀招清楚。
- skill attack：跳砸地面，產生短小管線震波。
- defeated：坐倒冒星星，不做血腥。

---

### 7.4 噴氣水管兵

**定位**：紅帽管線城遠程兵，提供噴氣擊退與區域壓迫。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny pipe jet soldier enemy, red cap without logo, simple worker suit, large pipe nozzle backpack, pressure gauge, little hose connected to one mitten hand, steam puffs, cute serious face, original mobile game minion design
```

**動作表 Prompt**

```text
噴氣水管兵 action sheet, idle with pressure gauge shaking, walk waddling under heavy pipe tank, normal attack short steam puff from hose, skill attack charged jet blast from pipe nozzle, taking damage spinning from leaking steam, defeated deflating with harmless steam cloud, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- skill attack：背包壓力升高 → 噴射 → 後座力。
- taking damage：管線漏氣、身體轉一圈。

---

### 7.5 影紙忍

**定位**：高速近戰小怪，主打閃現、突刺、紙片感。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny paper shadow ninja enemy, flat paper-like body edges, black and dark indigo outfit, simple mask with cute narrow eyes, folded paper scarf, small paper kunai, ink shadow wisps, original ninja-inspired minion, no known anime costume
```

**動作表 Prompt**

```text
影紙忍 action sheet, idle crouching with paper scarf flutter, walk quick low dash, normal attack paper kunai slash, skill attack leaving a folded paper afterimage then dash slash, taking damage crumpling like paper, defeated folding into a small paper scrap, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- walk：低姿態滑步。
- skill attack：殘影用紙片表現，不做複雜分身。

---

### 7.6 飛鏢影童

**定位**：影村遠程投射兵，配合影紙忍形成前後排壓力。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny shadow dart child enemy, dark paper ninja hood, oversized round head, small mitten hands holding paper shuriken, shy but mischievous eyes, little pouch of folded darts, ink smoke feet, original cute hostile minion design
```

**動作表 Prompt**

```text
飛鏢影童 action sheet, idle juggling one paper shuriken, walk small hopping steps, normal attack throwing one paper dart, skill attack throwing three fan-shaped shadow darts, taking damage dropping all darts, defeated covered by folded paper stars and dizzy, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- normal attack：單枚飛鏢。
- skill attack：扇形三枚飛鏢，方向清楚。

---

### 7.7 藍核守衛球

**定位**：U-man 關卡的飛行巡邏球，提供能量彈與移動威脅。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, compact readable body, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a floating blue-core guard orb enemy, white round armor shell, glowing blue core in center, simple red symmetrical stripes, tiny wing fins, cute strict eye slit, small energy antenna, original justice-base security drone, no superhero logo
```

**動作表 Prompt**

```text
藍核守衛球 action sheet, idle hovering with blue core pulse, walk as smooth patrol hover, normal attack firing one small blue energy pellet, skill attack charging core then releasing a short blue beam, taking damage armor shell cracking with sparks, defeated core flickering and orb falling flat, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- idle：核心呼吸式閃爍。
- skill attack：藍光蓄力，短直線光束。

---

### 7.8 小型正義盾

**定位**：防禦型小怪，用來擋住玩家攻擊或保護後排。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny justice shield minion, short white armored body, blue gem eye, red simple stripes, oversized rounded shield with no logo, stubborn cute face, small boots, original defensive enemy design
```

**動作表 Prompt**

```text
小型正義盾 action sheet, idle hiding behind oversized shield, walk slow shield-forward march, normal attack shield bash, skill attack planting shield to create a small blue guard barrier, taking damage pushed backward with shield dented, defeated shield falling over with dizzy face behind it, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- normal attack：盾牌短撞。
- skill attack：插盾產生小護罩。
- defeated：盾牌倒下，露出暈臉。

---

### 7.9 螺絲工兵

**定位**：工廠關卡輔助兵，可修理、建小障礙或干擾玩家路線。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny screw engineer minion, metal screw-nut helmet, simple gray orange work suit, mitten hands holding tiny screwdriver, tool pouch, square goggles, cute busy expression, small metal boots, original factory enemy
```

**動作表 Prompt**

```text
螺絲工兵 action sheet, idle adjusting screw helmet, walk hurried tiny steps, normal attack poking with screwdriver, skill attack quickly building a small bolt barricade or repairing a metal panel, taking damage tools flying upward, defeated sitting dizzy inside a loose screw nut, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- skill attack：修補防禦物或做小路障。
- 造型要工兵感，但不要寫實重工業。

---

### 7.10 磁鐵鋼怪

**定位**：牽制型小怪，負責吸引玩家、拉扯金屬物、改變走位。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, compact readable body, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a cute hostile magnet steel monster, U-shaped magnet horns, chunky metal plate body, small round eyes, stubby feet, red and blue magnet tips, simple electric magnetic lines, original factory control enemy, readable silhouette
```

**動作表 Prompt**

```text
磁鐵鋼怪 action sheet, idle with magnet tips glowing, walk heavy clanking steps, normal attack headbutt with magnet horns, skill attack creating curved magnetic pull lines toward its body, taking damage polarity sparks exploding outward, defeated magnet horns falling apart and body demagnetized, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- skill attack：磁力線一定要清楚是「拉向自己」。
- defeated：磁鐵失效，鐵片鬆開。

---

### 7.11 小葫蘆童

**定位**：七色葫蘆山基礎近戰 / 彈跳怪。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny calabash child minion, small gourd hat, vine belt, round cheeky face, little leaf cape, colorful small gourd hanging from waist, short bare feet or simple shoes, cute mountain spirit enemy, original design
```

**動作表 Prompt**

```text
小葫蘆童 action sheet, idle swaying like a small gourd, walk bouncing steps, normal attack headbutt with gourd hat, skill attack spinning and releasing small colored seed pellets, taking damage wobbling like a bottle, defeated falling on back with gourd hat rolling away, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- walk：彈跳感。
- skill attack：彩色種子彈，特效小而清楚。

---

### 7.12 彩霧葫蘆

**定位**：狀態異常怪，負責毒霧、混亂、視線遮蔽。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, compact readable body, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a floating colorful mist calabash enemy, round gourd body, tiny sleepy eyes, cork stopper, small leaf wings, rainbow-tinted smoke leaking from mouth, cute but suspicious, original status-effect enemy design, readable at small size
```

**動作表 Prompt**

```text
彩霧葫蘆 action sheet, idle floating with gentle colored mist, walk drifting sideways, normal attack spitting a tiny mist puff, skill attack releasing a larger swirling rainbow confusion cloud, taking damage cork popping loose, defeated deflating into harmless colored smoke, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- 特效要可愛，不要做成毒氣恐怖感。
- skill attack：彩霧範圍清楚，但不可遮住本體。

---

### 7.13 丹火童子

**定位**：異火煉藥宗基礎火焰兵，提供灼燒地面與短距火苗。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a tiny alchemy fire child minion, small bronze cauldron hat, warm orange fire sleeves, simple robe with pill furnace pattern but no text, round mischievous face, tiny flame tail, holding a small herb fan, cute dangerous alchemy sect enemy, original design
```

**動作表 Prompt**

```text
丹火童子 action sheet, idle warming hands with small pill fire, walk hopping with little flame trail, normal attack swiping with herb fan and fire spark, skill attack blowing a short orange alchemy flame cone, taking damage flame shrinking and cauldron hat tilting, defeated turning into smoke with a tiny failed pill, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- normal attack：草藥扇揮出火星。
- skill attack：短火焰錐，控制在角色前方。
- defeated：變成失敗丹藥與煙，不血腥。

---

### 7.14 爆丹怪

**定位**：延遲自爆小怪，提供倒數壓迫與走位風險。

**外觀 Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, compact readable body, clean bold silhouette, soft 2.5D anime game art, playful dark-comedy fantasy revenge game mood, animation-ready sprite design, white background, no scenery, a round unstable pill bomb monster, red orange medicinal pill body, glowing crack lines, tiny anxious eyes, little fuse-like herb stem on top, small feet, cute panic expression, alchemy failure enemy, original design, no gore
```

**動作表 Prompt**

```text
爆丹怪 action sheet, idle trembling with glowing cracks, walk bouncing nervously, normal attack small bump tackle, skill attack countdown swelling then harmless stylized alchemy burst, taking damage cracks flashing brighter, defeated popping into smoke and pill fragments, white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes
```

**動作備註**

- skill attack：倒數感要明顯，可用膨脹、發光、抖動表現，不要放文字數字。
- defeated：若被提前擊倒，爆成小煙花式丹煙。

---

## 8. 第一批實作建議

### 第一批：教學與前三關

1. 碎運鬼
2. 黑運糰
3. 水管工僕
4. 噴氣水管兵
5. 影紙忍
6. 飛鏢影童

這 6 隻足夠測試：

- 基礎近戰
- 滾動地面干擾
- 工具揮擊
- 噴氣遠程
- 快速突刺
- 扇形投射物

### 第二批：中期機制怪

1. 藍核守衛球
2. 小型正義盾
3. 螺絲工兵
4. 磁鐵鋼怪
5. 小葫蘆童
6. 彩霧葫蘆
7. 丹火童子
8. 爆丹怪

這 8 隻負責：

- 飛行巡邏
- 盾牌防禦
- 建造 / 修理
- 吸引牽制
- 彈跳近戰
- 狀態霧氣
- 灼燒區域
- 延遲自爆

---

## 9. 品質檢查清單

生成後逐張檢查：

- 是否白底？
- 是否全身沒有裁切？
- 是否每格角色比例一致？
- 是否沒有文字、水印、Logo？
- 是否沒有可辨識既有 IP 特徵？
- 是否沒有積木玩具式手、卡榫、凸點？
- 是否能一眼看出攻擊方向？
- 是否能在手機小尺寸下辨識？
- 是否技能特效沒有遮住本體？
- 是否 idle / walk / normal attack / skill attack / taking damage / defeated 都有？

---

## 10. 常見問題修正 Prompt

### 10.1 小怪太像 Boss

```text
make the enemy simpler, weaker, smaller, less detailed than a boss, clear minion silhouette, fewer accessories, mobile sprite readability
```

### 10.2 動作表角色不一致

```text
same character in every pose, same costume, same face, same body size, same weapon, same color palette, consistent model sheet
```

### 10.3 特效太亂

```text
simple readable motion effects, effects must not cover the character body, clean attack trail, clear silhouette, fewer particles
```

### 10.4 圖太像玩具積木

```text
organic chibi cartoon body, rounded mitten hands, no toy brick studs, no interlocking brick parts, no plastic minifigure joints, no C-shaped gripping hands
```

### 10.5 動作太少，不像 animation sheet

```text
more animation keyframes, multiple small full-body poses, clean separated grid, idle walk normal attack skill attack taking damage defeated, sprite animation planning
```
