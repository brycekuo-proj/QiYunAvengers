# 07｜小怪設計 Prompt V1

專案：《氣運復仇者》

用途：建立各關卡小怪的基礎外觀 Prompt 與動作表 Prompt，方便後續批量生成角色設定圖、sprite sheet、animation sheet。

---

## 1. 小怪共通母 Prompt

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background
```

### 使用原則

- 所有小怪都要是原創 Q 版手機遊戲敵人。
- 造型要能一眼看出所屬關卡與 Boss 陣營。
- 小怪比 Boss 更簡潔，方便量產、拆圖、做動畫。
- 小怪表情可以可愛、壞、呆、憨，但不要恐怖寫實。
- 不使用既有 IP、真實人物、商標、可辨識超級英雄或動漫造型。
- 手部維持圓潤饅頭手 / mitten hands；避免積木玩具式夾手、卡榫或凸點。

---

## 2. 小怪共通 Negative Prompt

```text
low quality, blurry, noisy, messy lineart, cropped body, missing feet, cut off weapon, inconsistent costume, inconsistent color palette, inconsistent face, inconsistent size between poses, extra limbs, realistic gore, blood splatter, horror corpse detail, photorealistic human, real celebrity likeness, direct copy of existing copyrighted characters, recognizable franchise costume, trademark logo, letters or symbols from known IP, toy brick studs, interlocking brick details, C-shaped gripping hands, visible toy joints, plastic toy minifigure proportions, complex background, scenery, UI, text, watermark, signature, speech bubble, overlapping poses, unreadable silhouette, too many tiny details, random duplicate enemies
```

---

## 3. 小怪動作表共通 Prompt

```text
Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image.
```

### 動作表必含動畫類型

| 動作 | 目的 | 建議拆法 |
| --- | --- | --- |
| idle | 待機辨識、呼吸、漂浮、機械閃爍 | 1～3 個 keyframes |
| walk | 移動循環 | 2～4 個 keyframes |
| normal attack | 普通攻擊 | 4 poses |
| skill attack | 小怪技能 / 特殊行為 | 4～6 poses |
| taking damage | 受擊、擊退、硬直 | 3 poses |
| defeated | 擊倒、消散、暈倒 | 3 poses |

---

## 4. 輸出規格

- white background
- multiple small full-body poses
- clean grid
- consistent costume
- consistent body scale and silhouette
- consistent weapon / prop / elemental effect
- animation-ready keyframes
- idle / walk / normal attack / skill attack / taking damage / defeated
- mobile game character action sheet
- 方便拆 sprite / animation sheet

### 補充規格

- 每張 action sheet 盡量維持同一視角，不要忽然變側面或背面。
- 小怪動作需要比 Boss 更簡潔，避免特效遮住本體。
- white background 是為了後續去背與切 sprite。
- clean grid 是為了讓每個 pose 可以獨立裁切。
- consistent costume 是為了避免同一隻怪在不同幀變成不同角色。
- animation-ready keyframes 是為了能直接進入 Spine / Unity / Godot / Web animation pipeline。

---

## 5. 小怪清單總覽

| 編號 | 小怪 | 所屬關卡 / 陣營 | 功能定位 |
| ---: | --- | --- | --- |
| 1 | 碎運鬼 | 0 怨念甦醒地 / 通用怨念系 | 教學地圖的第一批小怪 |
| 2 | 黑運糰 | 0 怨念甦醒地 / 通用負面氣運系 | 早期地圖的走位教學怪 |
| 3 | 水管工僕 | 1 紅帽管線城 / M先生系 | 第一張 Boss 地圖的標準近戰小怪 |
| 4 | 噴氣水管兵 | 1 紅帽管線城 / M先生系 | 第一關遠程壓力來源 |
| 5 | 影紙忍 | 2 影村訓練場 / 滅影忍者系 | 第二關速度型小兵 |
| 6 | 飛鏢影童 | 2 影村訓練場 / 滅影忍者系 | 第二關遠程干擾兵 |
| 7 | 藍核守衛球 | 3 藍核防衛基地 / U-man系 | 第三關基礎飛行小怪 |
| 8 | 小型正義盾 | 3 藍核防衛基地 / U-man系 | 第三關坦克型小怪 |
| 9 | 螺絲工兵 | 4 鋼筋戰隊工廠 / 鋼筋戰士系 | 第四關功能型小怪 |
| 10 | 磁鐵鋼怪 | 4 鋼筋戰隊工廠 / 鋼筋戰士系 | 第四關重型壓迫小怪 |
| 11 | 小葫蘆童 | 5 七色葫蘆山 / 葫蘆爺系 | 第五關基礎小怪 |
| 12 | 彩霧葫蘆 | 5 七色葫蘆山 / 葫蘆爺系 | 第五關輔助小怪 |
| 13 | 丹火童子 | 6 異火煉藥宗 / 消炎系 | 第六關遠程基礎小怪 |
| 14 | 爆丹怪 | 6 異火煉藥宗 / 消炎系 | 第六關高壓自爆怪 |
| 15 | 蛛絲混混 | 7 蛛網都市天台 / 失敗的面系 | 第七關近戰牽制小怪 |
| 16 | 監控蛛眼 | 7 蛛網都市天台 / 失敗的面系 | 第七關標記型遠程小怪 |
| 17 | 鬥氣猴兵 | 8 鬥氣武道星 / 吾空系 | 第八關高速近戰小怪 |
| 18 | 氣功石頭兵 | 8 鬥氣武道星 / 吾空系 | 第八關坦克與蓄力兵 |
| 19 | 刪除橡皮兵 | 9 命運劇場 / Creator + Eraser 系 | 最終關功能小怪 |
| 20 | 劇本紙偶 | 9 命運劇場 / Creator 系 | 最終關敘事型小怪 |

---

## 6. 小怪 Prompt 詳細設計

### 6.1 碎運鬼

**所屬關卡 / 陣營**：0 怨念甦醒地 / 通用怨念系

**定位**：最基礎的近戰小怪，像被主角怨念吸引而來的碎片鬼魂。用來教玩家普通攻擊、受擊、擊殺節奏。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, tiny cracked-luck ghost minion, pale gray translucent body, broken coin-shaped luck fragments orbiting around it, small angry cyan eyes, ragged smoky tail, cute resentful expression, black-cyan curse spark on forehead, simple floating silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, tiny cracked-luck ghost minion, pale gray translucent body, broken coin-shaped luck fragments orbiting around it, small angry cyan eyes, ragged smoky tail, cute resentful expression, black-cyan curse spark on forehead, simple floating silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 碎運鬼. Required animations: idle pose: floating in place, smoky tail gently curling, broken luck fragments slowly orbiting; walk poses: short hovering drift forward, body bobbing up and down, tiny smoke trail behind; normal attack poses: quick claw swipe with one tiny smoky arm, small cyan slash trail; skill attack poses: spits a small broken luck shard projectile forward with black-cyan sparkle; taking damage poses: body squashes sideways, luck fragments scatter outward, eyes squeezed shut; defeated poses: ghost deflates into smoke and broken coin fragments fade away. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- quick claw swipe with one tiny smoky arm, small cyan slash trail

**技能攻擊**

- spits a small broken luck shard projectile forward with black-cyan sparkle

**受到傷害**

- body squashes sideways, luck fragments scatter outward, eyes squeezed shut

**陣亡**

- ghost deflates into smoke and broken coin fragments fade away

**用途 / 關卡功能**

- 教學地圖的第一批小怪；低血量、低攻擊、數量多，讓玩家理解 Ghost 的復仇打擊感。

---

### 6.2 黑運糰

**所屬關卡 / 陣營**：0 怨念甦醒地 / 通用負面氣運系

**定位**：圓滾滾的黑色霉運怪，行動慢但會干擾玩家。主要負責製造地面障礙與低壓迫感。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, round black unlucky blob minion, soft mochi-like body, tiny purple eyes, stubby mitten hands, small unlucky clover crack mark, black mist puff, cute grumpy face, bouncy compact silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, round black unlucky blob minion, soft mochi-like body, tiny purple eyes, stubby mitten hands, small unlucky clover crack mark, black mist puff, cute grumpy face, bouncy compact silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 黑運糰. Required animations: idle pose: squishy idle bounce, black mist bubbling from top of head; walk poses: slow rolling hop forward, body squashing and stretching like mochi; normal attack poses: short body bump attack, leans forward with tiny impact puff; skill attack poses: drops a small unlucky puddle under itself, purple-black mist circle; taking damage poses: squashed flat for one frame, eyes become spiral marks; defeated poses: pops into three tiny black mist bubbles that dissolve. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- short body bump attack, leans forward with tiny impact puff

**技能攻擊**

- drops a small unlucky puddle under itself, purple-black mist circle

**受到傷害**

- squashed flat for one frame, eyes become spiral marks

**陣亡**

- pops into three tiny black mist bubbles that dissolve

**用途 / 關卡功能**

- 早期地圖的走位教學怪；用低傷害區域效果迫使玩家移動，不需要高操作門檻。

---

### 6.3 水管工僕

**所屬關卡 / 陣營**：1 紅帽管線城 / M先生系

**定位**：M先生手下的維修工小兵，拿扳手近戰，造型像城市管線維修隊的低階成員。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi pipe worker servant minion, small red work cap with blank badge, blue-gray overalls, simple tool belt, tiny wrench, round nose, loyal nervous expression, rounded mitten hands, pipe city maintenance enemy, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi pipe worker servant minion, small red work cap with blank badge, blue-gray overalls, simple tool belt, tiny wrench, round nose, loyal nervous expression, rounded mitten hands, pipe city maintenance enemy. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 水管工僕. Required animations: idle pose: stands with tiny wrench held in both hands, nervous foot tap; walk poses: short marching steps forward, wrench bouncing at side; normal attack poses: basic wrench swing from right to left with small metal spark; skill attack poses: tightens an invisible valve, small steam puff bursts forward as short-range attack; taking damage poses: red cap pops up, body recoils, wrench shakes; defeated poses: falls sitting down, wrench drops, steam puff fades above cap. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- basic wrench swing from right to left with small metal spark

**技能攻擊**

- tightens an invisible valve, small steam puff bursts forward as short-range attack

**受到傷害**

- red cap pops up, body recoils, wrench shakes

**陣亡**

- falls sitting down, wrench drops, steam puff fades above cap

**用途 / 關卡功能**

- 第一張 Boss 地圖的標準近戰小怪；協助建立 M先生管線城的工人軍團氛圍。

---

### 6.4 噴氣水管兵

**所屬關卡 / 陣營**：1 紅帽管線城 / M先生系

**定位**：背著小水管噴射器的遠程兵，會噴水、噴蒸氣，讓管線城不只是近戰。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi steam pipe trooper minion, small worker helmet, blue utility uniform, backpack water tank made of simple pipe shapes, short nozzle hose, round goggles, cute serious face, rounded mitten hands, compact ranged enemy silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi steam pipe trooper minion, small worker helmet, blue utility uniform, backpack water tank made of simple pipe shapes, short nozzle hose, round goggles, cute serious face, rounded mitten hands, compact ranged enemy silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 噴氣水管兵. Required animations: idle pose: holds hose nozzle forward, backpack pipe gently releasing tiny steam; walk poses: careful side-step walk while dragging hose, backpack wobbling; normal attack poses: short water spray burst from hose nozzle; skill attack poses: pressurizes backpack, then releases a stronger steam jet cone; taking damage poses: hose sprays upward accidentally, goggles tilt; defeated poses: backpack leaks water, minion spins once and collapses in a puddle. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- short water spray burst from hose nozzle

**技能攻擊**

- pressurizes backpack, then releases a stronger steam jet cone

**受到傷害**

- hose sprays upward accidentally, goggles tilt

**陣亡**

- backpack leaks water, minion spins once and collapses in a puddle

**用途 / 關卡功能**

- 第一關遠程壓力來源；搭配水管工僕形成近遠混編，逼玩家優先清兵。

---

### 6.5 影紙忍

**所屬關卡 / 陣營**：2 影村訓練場 / 滅影忍者系

**定位**：像紙片剪影的忍者小怪，速度快、血薄，適合做衝刺與假動作。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi paper shadow ninja minion, flat black paper-cut body, folded paper scarf, tiny red eyes, small paper kunai, ink-smoke edge, very thin silhouette but still cute, rounded mitten hands suggested by paper shapes, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi paper shadow ninja minion, flat black paper-cut body, folded paper scarf, tiny red eyes, small paper kunai, ink-smoke edge, very thin silhouette but still cute, rounded mitten hands suggested by paper shapes. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 影紙忍. Required animations: idle pose: paper body flutters subtly, red eyes blinking under folded hood; walk poses: quick zigzag sliding step, leaving two faint paper afterimages; normal attack poses: fast paper kunai stab forward, short black ink slash; skill attack poses: folds into a paper shuriken and dashes in a straight line; taking damage poses: paper body bends and crumples at the corner; defeated poses: unfolds into a flat black paper sheet and blows away. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- fast paper kunai stab forward, short black ink slash

**技能攻擊**

- folds into a paper shuriken and dashes in a straight line

**受到傷害**

- paper body bends and crumples at the corner

**陣亡**

- unfolds into a flat black paper sheet and blows away

**用途 / 關卡功能**

- 第二關速度型小兵；用來訓練玩家判斷衝刺路線與短暫破綻。

---

### 6.6 飛鏢影童

**所屬關卡 / 陣營**：2 影村訓練場 / 滅影忍者系

**定位**：小型影子投擲兵，會丟飛鏢並躲在影子裡。負責讓玩家學會閃避投射物。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi shadow dart child minion, tiny masked ninja kid silhouette, oversized black hood, red scarf knot, pouch full of paper darts, glowing red mischievous eyes, cute sneaky expression, ink shadow puddle under feet, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi shadow dart child minion, tiny masked ninja kid silhouette, oversized black hood, red scarf knot, pouch full of paper darts, glowing red mischievous eyes, cute sneaky expression, ink shadow puddle under feet. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 飛鏢影童. Required animations: idle pose: crouches in a small ink shadow puddle, one dart ready in hand; walk poses: tiny tiptoe run, dart pouch bouncing, shadow puddle following; normal attack poses: throws one black-red paper dart forward; skill attack poses: throws three darts in a fan pattern while sinking halfway into shadow; taking damage poses: hood flips backward, darts spill from pouch; defeated poses: sinks fully into shadow puddle, only scarf knot remains then disappears. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- throws one black-red paper dart forward

**技能攻擊**

- throws three darts in a fan pattern while sinking halfway into shadow

**受到傷害**

- hood flips backward, darts spill from pouch

**陣亡**

- sinks fully into shadow puddle, only scarf knot remains then disappears

**用途 / 關卡功能**

- 第二關遠程干擾兵；與影紙忍搭配形成「衝刺 + 飛鏢」的節奏壓力。

---

### 6.7 藍核守衛球

**所屬關卡 / 陣營**：3 藍核防衛基地 / U-man系

**定位**：浮游防衛球，會巡邏、撞擊、發射藍色能量。是 U-man 基地的基礎機械怪。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi blue-core guard orb minion, floating white metal sphere, bright blue gemstone core eye, red symmetrical stripe markings, tiny side fins, small antenna, cute mechanical angry face, clean sci-fi defense drone silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi blue-core guard orb minion, floating white metal sphere, bright blue gemstone core eye, red symmetrical stripe markings, tiny side fins, small antenna, cute mechanical angry face, clean sci-fi defense drone silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 藍核守衛球. Required animations: idle pose: hovers in place, blue core pulsing gently, side fins twitching; walk poses: smooth floating patrol movement, small blue exhaust dots behind; normal attack poses: quick body ram forward with blue impact ring; skill attack poses: charges blue core then fires a small straight energy bolt; taking damage poses: core flickers, sphere tilts, one fin bends; defeated poses: core dims, orb drops down and opens with tiny blue spark. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- quick body ram forward with blue impact ring

**技能攻擊**

- charges blue core then fires a small straight energy bolt

**受到傷害**

- core flickers, sphere tilts, one fin bends

**陣亡**

- core dims, orb drops down and opens with tiny blue spark

**用途 / 關卡功能**

- 第三關基礎飛行小怪；適合做巡邏線、空中干擾與基地科技感。

---

### 6.8 小型正義盾

**所屬關卡 / 陣營**：3 藍核防衛基地 / U-man系

**定位**：拿盾的小型防衛兵，血量較高，會替後排擋攻擊。負責引入護盾敵人。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi mini justice shield minion, tiny white armored body, oversized oval shield with blue core gem, red stripe accents, blank white oval eyes, stubby legs, rounded mitten hands, cute defensive robot guard, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi mini justice shield minion, tiny white armored body, oversized oval shield with blue core gem, red stripe accents, blank white oval eyes, stubby legs, rounded mitten hands, cute defensive robot guard. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 小型正義盾. Required animations: idle pose: holds shield in front, blue core blinking, tiny feet planted firmly; walk poses: slow guarded march with shield always forward; normal attack poses: shield bash forward with small blue spark; skill attack poses: plants shield and creates a short blue barrier wall in front; taking damage poses: shield cracks slightly, body peeks out with startled eyes; defeated poses: shield falls face-down and tiny guard rolls out dizzy. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- shield bash forward with small blue spark

**技能攻擊**

- plants shield and creates a short blue barrier wall in front

**受到傷害**

- shield cracks slightly, body peeks out with startled eyes

**陣亡**

- shield falls face-down and tiny guard rolls out dizzy

**用途 / 關卡功能**

- 第三關坦克型小怪；讓玩家學習繞背、技能破盾或先打後排。

---

### 6.9 螺絲工兵

**所屬關卡 / 陣營**：4 鋼筋戰隊工廠 / 鋼筋戰士系

**定位**：工廠維修小兵，拿螺絲起子與小盾，會修補同伴或設置障礙。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi screw sapper minion, yellow mini safety helmet, orange vest, gray work gloves as rounded mittens, giant screw backpack, screwdriver spear, small metal plate shield, cute hardworking enemy face, factory floor worker silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi screw sapper minion, yellow mini safety helmet, orange vest, gray work gloves as rounded mittens, giant screw backpack, screwdriver spear, small metal plate shield, cute hardworking enemy face, factory floor worker silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 螺絲工兵. Required animations: idle pose: checks giant screw backpack, screwdriver held like spear; walk poses: busy little run with tool backpack clanking; normal attack poses: jabs forward with screwdriver spear; skill attack poses: plants a large screw into the ground as a small obstacle marker; taking damage poses: helmet spins, screw backpack rattles open; defeated poses: trips over own screw, tools scatter in a neat cartoon pile. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- jabs forward with screwdriver spear

**技能攻擊**

- plants a large screw into the ground as a small obstacle marker

**受到傷害**

- helmet spins, screw backpack rattles open

**陣亡**

- trips over own screw, tools scatter in a neat cartoon pile

**用途 / 關卡功能**

- 第四關功能型小怪；可作為障礙生成兵或修補兵，提升工廠戰場變化。

---

### 6.10 磁鐵鋼怪

**所屬關卡 / 陣營**：4 鋼筋戰隊工廠 / 鋼筋戰士系

**定位**：磁鐵與廢鐵組成的重型怪，會吸引玩家或吸附金屬碎片攻擊。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi magnet steel monster minion, horseshoe magnet horns, chunky scrap metal body, yellow-black caution stripe belly, tiny glowing bolt eyes, stubby heavy legs, rounded magnetic mitten hands, cute industrial brute silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi magnet steel monster minion, horseshoe magnet horns, chunky scrap metal body, yellow-black caution stripe belly, tiny glowing bolt eyes, stubby heavy legs, rounded magnetic mitten hands, cute industrial brute silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 磁鐵鋼怪. Required animations: idle pose: magnet horns hum, small screws orbit around body; walk poses: heavy stomping walk, scrap body wobbling with each step; normal attack poses: swings magnetic fist forward with screw spiral trail; skill attack poses: pulls nearby metal scraps into a small spinning shield then bursts them outward; taking damage poses: scrap plates pop loose, magnet horns flicker; defeated poses: magnet polarity fails, body falls apart into harmless scrap pile. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- swings magnetic fist forward with screw spiral trail

**技能攻擊**

- pulls nearby metal scraps into a small spinning shield then bursts them outward

**受到傷害**

- scrap plates pop loose, magnet horns flicker

**陣亡**

- magnet polarity fails, body falls apart into harmless scrap pile

**用途 / 關卡功能**

- 第四關重型壓迫小怪；可設計成吸附、拉扯或範圍爆散，讓玩家保持距離。

---

### 6.11 小葫蘆童

**所屬關卡 / 陣營**：5 七色葫蘆山 / 葫蘆爺系

**定位**：七色葫蘆山的小童兵，拿小葫蘆與藤蔓，像童話裡的山中守衛。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi little gourd child minion, leaf hat, simple green-brown robe, tiny colorful gourd bottle, vine belt, round innocent face with strict eyebrows, bare little feet, rounded mitten hands, storybook mountain sprite, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi little gourd child minion, leaf hat, simple green-brown robe, tiny colorful gourd bottle, vine belt, round innocent face with strict eyebrows, bare little feet, rounded mitten hands, storybook mountain sprite. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 小葫蘆童. Required animations: idle pose: hugs tiny gourd bottle, leaf hat swaying gently; walk poses: small skipping steps, vine belt bouncing, gourd sloshing; normal attack poses: swings tiny gourd like a club with soft bonk effect; skill attack poses: opens gourd to release a short green vine whip; taking damage poses: leaf hat covers eyes, gourd slips from hands; defeated poses: sits down dizzy while gourd rolls in a tiny circle. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- swings tiny gourd like a club with soft bonk effect

**技能攻擊**

- opens gourd to release a short green vine whip

**受到傷害**

- leaf hat covers eyes, gourd slips from hands

**陣亡**

- sits down dizzy while gourd rolls in a tiny circle

**用途 / 關卡功能**

- 第五關基礎小怪；建立童話山林氛圍，攻擊簡單但數量可以多。

---

### 6.12 彩霧葫蘆

**所屬關卡 / 陣營**：5 七色葫蘆山 / 葫蘆爺系

**定位**：會噴彩色霧氣的葫蘆怪，偏輔助與狀態異常，給葫蘆山增加魔法感。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi colorful mist gourd minion, walking gourd creature with tiny leaf arms, rainbow mist leaking from cork, sleepy cute face carved on gourd surface, green vine feet, soft round silhouette, fantasy support enemy sprite, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi colorful mist gourd minion, walking gourd creature with tiny leaf arms, rainbow mist leaking from cork, sleepy cute face carved on gourd surface, green vine feet, soft round silhouette, fantasy support enemy sprite. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 彩霧葫蘆. Required animations: idle pose: cork wiggles, rainbow mist slowly puffing upward; walk poses: wobbly hopping walk on vine feet, mist trail behind; normal attack poses: bumps forward with gourd body, tiny rainbow puff impact; skill attack poses: uncorks itself and sprays a cone of colorful sleepy mist; taking damage poses: cork pops out, mist shoots upward accidentally; defeated poses: gourd tips over and all mist leaks out into sparkles. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- bumps forward with gourd body, tiny rainbow puff impact

**技能攻擊**

- uncorks itself and sprays a cone of colorful sleepy mist

**受到傷害**

- cork pops out, mist shoots upward accidentally

**陣亡**

- gourd tips over and all mist leaks out into sparkles

**用途 / 關卡功能**

- 第五關輔助小怪；可用於緩速、混亂、遮蔽視線等狀態效果。

---

### 6.13 丹火童子

**所屬關卡 / 陣營**：6 異火煉藥宗 / 消炎系

**定位**：煉藥宗低階童子，手持小丹爐，會丟火苗與補火。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi pill-fire apprentice minion, small alchemist child, dark red training robe, tiny bronze pill furnace in both mitten hands, orange-cyan flame hair tuft, round focused eyes, little sash, xianxia alchemy enemy sprite, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi pill-fire apprentice minion, small alchemist child, dark red training robe, tiny bronze pill furnace in both mitten hands, orange-cyan flame hair tuft, round focused eyes, little sash, xianxia alchemy enemy sprite. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 丹火童子. Required animations: idle pose: carefully holds tiny furnace, small cyan-orange flame flickering above lid; walk poses: short cautious steps while protecting furnace, robe sleeves bouncing; normal attack poses: throws a small flame pellet forward; skill attack poses: opens furnace and releases three tiny fire sparks in a curved burst; taking damage poses: furnace shakes and smoke covers face; defeated poses: furnace lid pops, apprentice sits down covered in harmless soot. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- throws a small flame pellet forward

**技能攻擊**

- opens furnace and releases three tiny fire sparks in a curved burst

**受到傷害**

- furnace shakes and smoke covers face

**陣亡**

- furnace lid pops, apprentice sits down covered in harmless soot

**用途 / 關卡功能**

- 第六關遠程基礎小怪；讓異火煉藥宗有持續彈幕與火焰節奏。

---

### 6.14 爆丹怪

**所屬關卡 / 陣營**：6 異火煉藥宗 / 消炎系

**定位**：失敗丹藥變成的小怪，會膨脹後爆炸。負責做倒數、自爆、範圍警示。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi failed pill bomb monster, round cracked pill body, half orange half dark purple, tiny angry eyes, smoking cracks, short stubby feet, little flame fuse on top, cute unstable alchemy creature silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi failed pill bomb monster, round cracked pill body, half orange half dark purple, tiny angry eyes, smoking cracks, short stubby feet, little flame fuse on top, cute unstable alchemy creature silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 爆丹怪. Required animations: idle pose: body trembles, flame fuse flickering, cracks glowing softly; walk poses: wobbly rolling hop forward, crack glow pulsing faster; normal attack poses: headbutt bump with tiny fire spark; skill attack poses: inflates larger, flashes, then releases a round cartoon smoke explosion effect; taking damage poses: cracks widen, body compresses and sparks fly; defeated poses: pops into harmless smoke ring and tiny pill crumbs. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- headbutt bump with tiny fire spark

**技能攻擊**

- inflates larger, flashes, then releases a round cartoon smoke explosion effect

**受到傷害**

- cracks widen, body compresses and sparks fly

**陣亡**

- pops into harmless smoke ring and tiny pill crumbs

**用途 / 關卡功能**

- 第六關高壓自爆怪；迫使玩家快速處理或引導它炸其他敵人。

---

### 6.15 蛛絲混混

**所屬關卡 / 陣營**：7 蛛網都市天台 / 失敗的面系

**定位**：都市天台小混混，帶蛛絲繩索與破面具塗鴉，負責近戰牽制。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi rooftop web punk minion, oversized hoodie, cracked mask graffiti on chest, red-black cord rope wrapped around wrists, sneakers, mischievous street thug face, rounded mitten hands, urban rooftop enemy sprite, no franchise superhero symbols, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi rooftop web punk minion, oversized hoodie, cracked mask graffiti on chest, red-black cord rope wrapped around wrists, sneakers, mischievous street thug face, rounded mitten hands, urban rooftop enemy sprite, no franchise superhero symbols. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 蛛絲混混. Required animations: idle pose: leans forward with cord rope dangling, hoodie bouncing slightly; walk poses: swaggering quick steps, sneakers exaggerated, cord trailing behind; normal attack poses: short rope punch forward with red-black cord impact; skill attack poses: throws sticky cord loop to briefly bind target direction; taking damage poses: hood flips over eyes, cord tangles around own arm; defeated poses: falls backward tangled in own rope, tiny dizzy stars above hood. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- short rope punch forward with red-black cord impact

**技能攻擊**

- throws sticky cord loop to briefly bind target direction

**受到傷害**

- hood flips over eyes, cord tangles around own arm

**陣亡**

- falls backward tangled in own rope, tiny dizzy stars above hood

**用途 / 關卡功能**

- 第七關近戰牽制小怪；可搭配監控蛛眼形成「綁住 + 射擊」組合。

---

### 6.16 監控蛛眼

**所屬關卡 / 陣營**：7 蛛網都市天台 / 失敗的面系

**定位**：像監視器與蛛眼結合的飛行小怪，會鎖定、標記、射線。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi surveillance spider-eye drone minion, floating black camera eyeball, red lens pupil, four tiny mechanical spider legs folded around body, thin web cables, cracked mask sticker, cute creepy but not horror, compact flying scout silhouette, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi surveillance spider-eye drone minion, floating black camera eyeball, red lens pupil, four tiny mechanical spider legs folded around body, thin web cables, cracked mask sticker, cute creepy but not horror, compact flying scout silhouette. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 監控蛛眼. Required animations: idle pose: hovers while red lens scans left and right, tiny web cable dangling; walk poses: smooth floating drift with small spider legs twitching; normal attack poses: fires a short red scan beam from lens; skill attack poses: projects a red target marker circle then releases a stronger web-laser pulse; taking damage poses: lens cracks with static spark, drone spins slightly; defeated poses: web cable snaps and drone drops, lens light turns off. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- fires a short red scan beam from lens

**技能攻擊**

- projects a red target marker circle then releases a stronger web-laser pulse

**受到傷害**

- lens cracks with static spark, drone spins slightly

**陣亡**

- web cable snaps and drone drops, lens light turns off

**用途 / 關卡功能**

- 第七關標記型遠程小怪；可讓玩家感受到城市監控與天台追殺壓力。

---

### 6.17 鬥氣猴兵

**所屬關卡 / 陣營**：8 鬥氣武道星 / 吾空系

**定位**：猴系武道小兵，拿短棍、跳躍快，是吾空關卡的基礎近戰單位。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi battle-aura monkey soldier minion, small monkey-inspired martial trainee, brown hair tuft, tiny cloud headband, short wooden staff, orange-gold scarf, teal training pants, playful fierce eyes, rounded mitten hands, golden qi aura puff, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi battle-aura monkey soldier minion, small monkey-inspired martial trainee, brown hair tuft, tiny cloud headband, short wooden staff, orange-gold scarf, teal training pants, playful fierce eyes, rounded mitten hands, golden qi aura puff. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 鬥氣猴兵. Required animations: idle pose: bounces on toes while twirling short staff, small golden aura puff; walk poses: quick hopping martial steps, staff tucked under arm; normal attack poses: short staff jab then tiny bonk impact; skill attack poses: leaps on a small cloud puff and slams staff downward; taking damage poses: headband slips, monkey soldier tumbles backward; defeated poses: staff rolls away and soldier collapses on a deflated cloud puff. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- short staff jab then tiny bonk impact

**技能攻擊**

- leaps on a small cloud puff and slams staff downward

**受到傷害**

- headband slips, monkey soldier tumbles backward

**陣亡**

- staff rolls away and soldier collapses on a deflated cloud puff

**用途 / 關卡功能**

- 第八關高速近戰小怪；用跳躍與短突進測試玩家反應。

---

### 6.18 氣功石頭兵

**所屬關卡 / 陣營**：8 鬥氣武道星 / 吾空系

**定位**：練氣失敗變成石頭的武道兵，慢速、高血量，會蓄力氣功波。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi qigong stone soldier minion, small gray stone body with carved martial eyebrows, prayer-bead belt, cracked rock fists as rounded mittens, golden qi glow in cracks, sturdy squat silhouette, cute stubborn expression, martial fantasy enemy sprite, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi qigong stone soldier minion, small gray stone body with carved martial eyebrows, prayer-bead belt, cracked rock fists as rounded mittens, golden qi glow in cracks, sturdy squat silhouette, cute stubborn expression, martial fantasy enemy sprite. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 氣功石頭兵. Required animations: idle pose: holds qigong stance, golden light pulsing through stone cracks; walk poses: slow stomping walk, stone feet thudding, bead belt shaking; normal attack poses: heavy stone palm strike forward with dust puff; skill attack poses: charges golden qi between stone palms and releases a small slow energy ball; taking damage poses: stone chips fly, cracks flash, body rocks backward; defeated poses: stone body cracks into three cute rounded boulders, qi light fades. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- heavy stone palm strike forward with dust puff

**技能攻擊**

- charges golden qi between stone palms and releases a small slow energy ball

**受到傷害**

- stone chips fly, cracks flash, body rocks backward

**陣亡**

- stone body cracks into three cute rounded boulders, qi light fades

**用途 / 關卡功能**

- 第八關坦克與蓄力兵；提供慢速高威脅目標，逼玩家打斷或繞位。

---

### 6.19 刪除橡皮兵

**所屬關卡 / 陣營**：9 命運劇場 / Creator + Eraser 系

**定位**：Creator 的清除小兵，像小型橡皮擦，會擦掉地面效果或玩家召喚物。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi deletion eraser soldier minion, small white eraser body, simple black cursor mark, tiny floating mitten hands, little violet erasing aura, square pixel dust around feet, cute emotionless face, clean final-stage enemy sprite, not a branded product, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi deletion eraser soldier minion, small white eraser body, simple black cursor mark, tiny floating mitten hands, little violet erasing aura, square pixel dust around feet, cute emotionless face, clean final-stage enemy sprite, not a branded product. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 刪除橡皮兵. Required animations: idle pose: hovers silently, cursor mark blinking, pixel dust falling upward; walk poses: slides forward like an eraser across invisible paper, leaving clean white streak; normal attack poses: short eraser swipe attack with white deletion trail; skill attack poses: creates a small rectangular erase zone that dissolves nearby particles; taking damage poses: eraser wobbles, cursor mark flickers, corner bends slightly; defeated poses: breaks into small white cubes that fade into blank space. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- short eraser swipe attack with white deletion trail

**技能攻擊**

- creates a small rectangular erase zone that dissolves nearby particles

**受到傷害**

- eraser wobbles, cursor mark flickers, corner bends slightly

**陣亡**

- breaks into small white cubes that fade into blank space

**用途 / 關卡功能**

- 最終關功能小怪；用於刪除玩家優勢、清場、壓迫走位，呼應 Eraser 大決。

---

### 6.20 劇本紙偶

**所屬關卡 / 陣營**：9 命運劇場 / Creator 系

**定位**：被 Creator 劇本控制的紙偶小兵，像剪紙演員與提線木偶。適合做命運劇場主題。

**Base Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi script paper puppet minion, folded paper actor body, blank comedy-tragedy mask face split in half, thin black puppet strings, tiny quill-shaped dagger, beige parchment texture, red correction marks, cute eerie theater sprite, no horror gore, white background, full body, front three-quarter view, clean enemy concept design sheet, no text, no watermark
```

**Action Sheet Prompt**

```text
original chibi mobile game enemy minion, super deformed proportions, small full-body figure, oversized expressive head, compact readable body, rounded mitten-like hands if hands exist, no visible toy joints, no interlocking toy parts, clean bold silhouette, soft 2.5D anime game art, dark comedy fantasy revenge game mood, cute but hostile, simple readable costume, consistent color palette, animation-ready sprite design, suitable for mobile RPG battle, white background, no scenery, no complex background, original chibi script paper puppet minion, folded paper actor body, blank comedy-tragedy mask face split in half, thin black puppet strings, tiny quill-shaped dagger, beige parchment texture, red correction marks, cute eerie theater sprite, no horror gore. Create a clean mobile game enemy action sheet on white background. Show multiple small full-body poses arranged in a clean grid with equal spacing. Keep the same enemy design, same costume, same face, same weapon, same proportions, and same color palette across every pose. The sheet must be animation-ready keyframes for sprite / animation sheet extraction. Include idle / walk / normal attack / skill attack / taking damage / defeated. Keep every pose full-body and uncropped. Use simple readable motion effects only. No text labels inside the image. Enemy name: 劇本紙偶. Required animations: idle pose: hangs from thin puppet strings, paper body swaying, mask blinking blankly; walk poses: jerky puppet steps forward, strings pulling limbs in stiff rhythm; normal attack poses: slashes with tiny quill dagger, red correction mark trail; skill attack poses: unrolls a short script scroll and summons two red edit marks as projectiles; taking damage poses: paper body folds awkwardly, strings tangle above head; defeated poses: strings snap, paper puppet folds into a crumpled script ball. Output requirements: white background, multiple small full-body poses, clean grid, consistent costume, animation-ready keyframes, idle / walk / normal attack / skill attack / taking damage / defeated.
```

**普通攻擊**

- slashes with tiny quill dagger, red correction mark trail

**技能攻擊**

- unrolls a short script scroll and summons two red edit marks as projectiles

**受到傷害**

- paper body folds awkwardly, strings tangle above head

**陣亡**

- strings snap, paper puppet folds into a crumpled script ball

**用途 / 關卡功能**

- 最終關敘事型小怪；呈現「命運被劇本操控」的主題，也可做召喚兵或干擾兵。

---

## 7. 批量生成命名建議

| 類型 | 命名範例 |
| --- | --- |
| 小怪設定圖 | `suiyun_ghost_base.png` |
| 小怪完整動作表 | `suiyun_ghost_action_sheet.png` |
| 普通攻擊拆分 | `suiyun_ghost_normal_attack_4poses.png` |
| 技能攻擊拆分 | `suiyun_ghost_skill_attack_6poses.png` |
| 受擊拆分 | `suiyun_ghost_taking_damage_3poses.png` |
| 陣亡拆分 | `suiyun_ghost_defeated_3poses.png` |

---

## 8. 製作優先級建議

### 第一批：可支撐 Demo 的小怪

1. 碎運鬼
2. 黑運糰
3. 水管工僕
4. 噴氣水管兵
5. 影紙忍
6. 飛鏢影童

這 6 隻可以先覆蓋教學地圖、紅帽管線城、影村訓練場，足夠測試近戰、遠程、衝刺、投射物、地面效果。

### 第二批：中期關卡機制怪

1. 藍核守衛球
2. 小型正義盾
3. 螺絲工兵
4. 磁鐵鋼怪
5. 小葫蘆童
6. 彩霧葫蘆
7. 丹火童子
8. 爆丹怪

這批負責補足盾牌、飛行、防衛球、障礙、自爆、狀態異常等玩法。

### 第三批：後期主題怪

1. 蛛絲混混
2. 監控蛛眼
3. 鬥氣猴兵
4. 氣功石頭兵
5. 刪除橡皮兵
6. 劇本紙偶

這批用來強化後期關卡主題：監控、牽制、跳躍武道、蓄力、刪除、劇本操控。

---

## 9. 實作注意事項

- 小怪不要比 Boss 複雜；小怪是「功能符號」，Boss 才是「視覺主角」。
- 每關至少需要一隻近戰、一隻遠程或機制怪，避免關卡只是在換皮。
- 小怪動作要能從輪廓看出攻擊方向，例如扳手橫揮、飛鏢扇形、橡皮擦橫掃。
- 受擊與陣亡不做血腥，改用暈眩、散煙、碎片、漏水、漏氣、掉工具等 Q 版效果。
- 若生圖模型把角色做太精細，要追加：`simple mobile sprite, readable at small size, fewer details, clean silhouette`。
- 若 action sheet 角色不一致，要使用 Base Prompt 的最佳圖作 reference image，再追加：`same character in every frame, same costume in every frame, same size in every frame`。
- 若 pose 互相重疊，要追加：`large spacing between each pose, no overlapping poses, clean separated grid cells`。
