# 08｜小怪攻擊與技能特效 Prompt V1

專案：《氣運復仇者》

用途：獨立規劃小怪的普通攻擊、技能攻擊、受擊、陣亡特效 Prompt，方便後續在角色 action sheet 之外，另行生成可疊加的 VFX sprite sheet。

這份文件與 `docs/07_ENEMY_PROMPT_DESIGN.md` 搭配使用：

- `07`：小怪本體、外觀、動作表。
- `08`：小怪攻擊軌跡、投射物、命中特效、技能範圍、受擊與陣亡效果。

---

## 0. 特效核心方向

- 手機遊戲可讀性優先：特效要清楚表達攻擊方向、範圍、危險程度。
- 可愛黑色幽默：可以壞、可以嘲諷，但不要血腥、不要寫實恐怖。
- 小怪特效不可比 Boss 華麗：小怪特效是功能提示，不是視覺主角。
- 每種特效要能拆成 sprite / VFX sheet。
- 特效要能搭配透明背景輸出；若模型不支援透明，先用 white background 方便後續去背。
- 不使用文字、數字、商標、可辨識 IP 符號。

---

## 1. 小怪特效共通母 Prompt

**Enemy VFX Common Mother Prompt**

```text
original chibi mobile game VFX sprite sheet, cute dark-comedy fantasy action effect, clean readable shapes, simple stylized particles, mobile game readability, crisp outline, soft 2.5D anime game style, animation-ready keyframes, clear attack direction, clear impact shape, small-scale enemy effect, not too flashy, suitable for overlay on chibi enemy sprites, white background, no scenery, no UI, no text
```

### 使用說明

所有小怪特效 prompt 前面先加這段，再接不同小怪的特效描述。若要去背工作流，先保留白底；若工具支援透明背景，可把 `white background` 改成：

```text
transparent background, isolated VFX elements, alpha-ready sprite sheet
```

---

## 2. 小怪特效共通 Negative Prompt

**Enemy VFX Common Negative Prompt**

```text
low quality, blurry, noisy, messy particles, overly complex effect, effect covers the whole character, unreadable attack direction, realistic gore, blood splatter, horror corpse detail, photorealistic explosion, real fire photo, real smoke photo, trademark logo, recognizable superhero symbol, known anime or game power effect, text, numbers, letters, watermark, signature, UI frame, background scenery, complex environment, random character body, duplicated enemy, cropped effect, inconsistent style, too many colors, lens flare, cinematic realism
```

---

## 3. 小怪特效動作表共通 Prompt

**Enemy VFX Sheet Common Prompt**

```text
Create a clean VFX sprite sheet on white background. Show multiple small separated effect keyframes arranged in a clean grid with equal spacing. Include anticipation, active attack effect, impact effect, fade-out effect, taking damage effect, and defeated effect. Keep the same visual style and color palette across all frames. The effects must be readable at small mobile game size, animation-ready, easy to cut into sprites, no text labels inside the image.
```

### 建議 VFX 拆法

| 類型 | 建議幀數 | 用途 |
| --- | ---: | --- |
| anticipation | 2 | 起手提示、危險預兆 |
| normal attack trail | 3～4 | 普攻軌跡 |
| skill attack effect | 4～6 | 技能範圍或投射物 |
| impact | 2～3 | 命中特效 |
| taking damage | 2～3 | 小怪受擊反應特效 |
| defeated | 3～5 | 消散、暈眩、爆煙、碎片 |

---

## 4. 輸出規格

每張小怪特效表必須符合：

- white background
- multiple small separated VFX keyframes
- clean grid
- consistent color palette
- animation-ready keyframes
- normal attack / skill attack / impact / taking damage / defeated
- no text labels
- no UI frame
- no scenery background

補充規格：

- 特效不可遮住角色本體輪廓。
- 普攻特效要比技能特效小。
- 技能特效要清楚表達範圍，例如直線、扇形、圓形、地面區域、吸引線。
- 受擊特效要短、乾淨，例如小星星、裂片、煙霧、火星。
- 陣亡特效不使用血，改用煙、碎片、漏氣、暈星、紙片、失效光。
- 顏色要跟小怪陣營一致，避免整張圖彩度過高。

---

## 5. 小怪特效命名規則

建議未來資源命名：

```text
enemy_[enemy_id]_[enemy_name]_normal_vfx.png
enemy_[enemy_id]_[enemy_name]_skill_vfx.png
enemy_[enemy_id]_[enemy_name]_hit_vfx.png
enemy_[enemy_id]_[enemy_name]_defeated_vfx.png
enemy_[enemy_id]_[enemy_name]_vfx_sheet.png
```

範例：

```text
enemy_03_pipe_servant_normal_vfx.png
enemy_03_pipe_servant_skill_vfx.png
enemy_03_pipe_servant_hit_vfx.png
enemy_03_pipe_servant_defeated_vfx.png
enemy_03_pipe_servant_vfx_sheet.png
```

---

## 6. 各小怪攻擊與技能特效 Prompt

### 6.1 碎運鬼｜Broken Luck Ghost VFX

**普通攻擊特效**

```text
original chibi mobile game VFX sprite sheet, cute dark-comedy fantasy action effect, clean readable shapes, simple stylized particles, animation-ready keyframes, white background, a small gray purple claw swipe trail made of unlucky mist and cracked fortune fragments, short horizontal arc, tiny broken halo sparks, readable normal attack effect, not too flashy
```

**技能攻擊特效**

```text
original chibi mobile game VFX sprite sheet, white background, cracked bad-luck talisman shockwave, gray purple circular ripple, small broken luck fragments flying forward, cute cursed smoke, anticipation frame with talisman glow, active frame with short shockwave, impact frame with tiny unlucky stars, fade-out frame, animation-ready keyframes, clean grid
```

**受擊 / 陣亡特效**

```text
small gray purple puff, cracked talisman flip, tiny unlucky stars, defeated dissolve into harmless ghost smoke and broken luck shards, no blood, no gore, clean VFX sprite sheet, white background
```

---

### 6.2 黑運糰｜Bad Luck Blob VFX

**普通攻擊特效**

```text
cute dark-comedy mobile game impact effect, black purple squash-and-stretch body slam impact, small dust ring, unlucky smoke puff, round bounce trail, animation-ready VFX keyframes, white background, clean grid
```

**技能攻擊特效**

```text
small black unlucky puddle VFX, dark purple slime circle on ground, tiny bad-luck bubbles, slow debuff visual, cute cursed smoke rising, anticipation drop, puddle active frame, small ripple impact, fade-out frame, white background, separated VFX keyframes
```

**受擊 / 陣亡特效**

```text
squashed black blob puff, tiny dark bubbles, harmless pop smoke, unlucky mist fading away, no gore, white background, animation-ready keyframes
```

---

### 6.3 水管工僕｜Pipe Servant VFX

**普通攻擊特效**

```text
small wrench swing trail VFX, short silver arc with tiny screw sparks, cute impact star, simple mobile game normal attack effect, clean readable direction, white background, animation-ready keyframes, no logo, no text
```

**技能攻擊特效**

```text
pipe shockwave VFX sprite sheet, small ground slam ring shaped like cartoon pipe pressure ripple, tiny screws and steam puffs, anticipation with wrench raised, active slam arc, impact ground ring, fade-out steam, white background, clean grid, animation-ready keyframes
```

**受擊 / 陣亡特效**

```text
small wrench drop spark, tiny metal stars, steam puff, dizzy cartoon stars, harmless tool clatter effect, white background, clean VFX sheet
```

---

### 6.4 噴氣水管兵｜Jet Pipe Soldier VFX

**普通攻擊特效**

```text
short steam puff projectile VFX, soft white gray steam burst, tiny water droplets, clear forward direction, cute mobile game effect, not realistic smoke, white background, animation-ready keyframes
```

**技能攻擊特效**

```text
charged pipe jet blast VFX sprite sheet, blue white steam cone, pressure ring, small water sparkle particles, anticipation pressure gauge glow, active jet cone, impact push puff, fade-out vapor, white background, clean separated grid, readable at small size
```

**受擊 / 陣亡特效**

```text
leaking steam spiral, pressure valve pop, small harmless vapor cloud, deflating cartoon puff, white background, animation-ready VFX keyframes
```

---

### 6.5 影紙忍｜Paper Shadow Ninja VFX

**普通攻擊特效**

```text
paper kunai slash VFX, dark indigo ink arc, folded paper edge trail, tiny black paper scraps, fast readable melee attack effect, white background, clean grid, animation-ready keyframes
```

**技能攻擊特效**

```text
paper afterimage dash slash VFX sprite sheet, folded paper silhouette smear, black indigo ink slash line, anticipation shadow fold, active dash streak, impact paper cut burst, fade-out paper scraps, white background, no character body, animation-ready keyframes
```

**受擊 / 陣亡特效**

```text
crumpled paper puff, ink splash star, folded paper scraps, defeated fold into small paper pile effect, cute not horror, white background
```

---

### 6.6 飛鏢影童｜Shadow Dart Child VFX

**普通攻擊特效**

```text
single paper shuriken projectile VFX, dark paper star spinning trail, small ink motion line, tiny impact spark shaped like paper fold, white background, animation-ready keyframes, clean grid
```

**技能攻擊特效**

```text
three fan-shaped shadow dart projectiles VFX sheet, paper shuriken spread pattern, dark indigo motion trails, anticipation with three tiny glints, active fan throw, impact paper star bursts, fade-out scraps, white background, clean separated VFX frames
```

**受擊 / 陣亡特效**

```text
dropped paper darts, small ink puff, folded paper stars scattering, dizzy paper swirl, white background, no text
```

---

### 6.7 藍核守衛球｜Blue Core Guard Orb VFX

**普通攻擊特效**

```text
small blue energy pellet projectile VFX, glowing blue orb bullet, tiny white red sparkle, clean sci-fi chibi mobile game effect, clear forward trail, white background, animation-ready keyframes
```

**技能攻擊特效**

```text
short blue core beam VFX sprite sheet, anticipation blue core charge ring, active short beam, impact blue spark burst, fade-out light particles, simple justice-base energy style, white background, clean grid, readable at small size, no superhero symbol
```

**受擊 / 陣亡特效**

```text
blue core flicker sparks, tiny armor chip particles, weak electric pop, light fading out, white background, animation-ready VFX frames
```

---

### 6.8 小型正義盾｜Tiny Justice Shield VFX

**普通攻擊特效**

```text
small shield bash impact VFX, blue white impact star, short red white motion arc, tiny defense spark, clean readable melee effect, white background, animation-ready keyframes, no logo
```

**技能攻擊特效**

```text
small blue guard barrier VFX sprite sheet, rounded shield-shaped energy wall, simple blue transparent aura, anticipation shield glow, active barrier frame, hit shimmer, fade-out fragments, white background, clean separated keyframes, no text
```

**受擊 / 陣亡特效**

```text
shield dent spark, blue crack line, small cartoon stars, barrier breaking into soft light fragments, white background, no gore
```

---

### 6.9 螺絲工兵｜Screw Engineer VFX

**普通攻擊特效**

```text
small screwdriver poke VFX, tiny silver jab line, screw spark, orange metal glint, clean mobile game normal attack effect, white background, animation-ready keyframes
```

**技能攻擊特效**

```text
bolt barricade build VFX sprite sheet, small screws spinning into place, orange gray construction spark, tiny metal panel appearing, anticipation tool glow, active build swirl, impact bolt click, fade-out dust, white background, clean grid, no text
```

**受擊 / 陣亡特效**

```text
loose screws flying, small tool clatter stars, gray dust puff, screw nut wobble effect, white background, animation-ready frames
```

---

### 6.10 磁鐵鋼怪｜Magnet Steel Monster VFX

**普通攻擊特效**

```text
magnet horn headbutt VFX, short metallic impact arc, red blue polarity sparks, tiny steel chips, clean readable normal attack, white background, animation-ready keyframes
```

**技能攻擊特效**

```text
magnetic pull VFX sprite sheet, curved red blue magnetic force lines pulling inward, small floating metal chips moving toward center, anticipation polarity glow, active pull lines, impact clank spark, fade-out demagnetized particles, white background, clean grid, readable at small size
```

**受擊 / 陣亡特效**

```text
polarity spark burst, red blue electric pop, metal plates separating, magnet force lines breaking, white background, no realistic electricity
```

---

### 6.11 小葫蘆童｜Little Calabash Child VFX

**普通攻擊特效**

```text
small gourd headbutt impact VFX, green leaf swoosh, tiny yellow impact star, cute mountain spirit melee effect, white background, clean animation-ready keyframes
```

**技能攻擊特效**

```text
colored seed pellet VFX sprite sheet, small green yellow orange seed projectiles, spinning gourd swirl, anticipation leaf sparkle, active seed spread, impact tiny seed pop, fade-out leaf particles, white background, clean grid, no text
```

**受擊 / 陣亡特效**

```text
gourd wobble stars, tiny leaves flying, soft green puff, small rolling gourd cap effect, white background, no gore
```

---

### 6.12 彩霧葫蘆｜Color Mist Calabash VFX

**普通攻擊特效**

```text
small colorful mist puff VFX, soft pastel cloud, tiny bubble particles, cute suspicious status effect, white background, clean separated keyframes, not realistic smoke
```

**技能攻擊特效**

```text
rainbow confusion cloud VFX sprite sheet, swirling colorful mist ring, pastel purple green yellow smoke, anticipation cork pop, active mist cloud, impact dizzy swirl, fade-out soft bubbles, white background, clean grid, readable at small size, no text symbols
```

**受擊 / 陣亡特效**

```text
cork popping effect, colored mist leak, soft rainbow smoke deflate, tiny harmless bubbles, white background, animation-ready frames
```

---

### 6.13 丹火童子｜Alchemy Fire Child VFX

**普通攻擊特效**

```text
small alchemy fire fan swipe VFX, orange flame spark arc, tiny herb ash particles, cute magical fire effect, not realistic flame, white background, animation-ready keyframes, clean readable attack direction
```

**技能攻擊特效**

```text
short orange alchemy flame cone VFX sprite sheet, anticipation pill fire glow, active cone of stylized orange flame, impact small scorch puff, fade-out ember particles, cute fantasy alchemy style, white background, clean grid, not too flashy
```

**受擊 / 陣亡特效**

```text
flame shrinking puff, cauldron smoke, tiny failed pill pop, orange ember stars, harmless smoke fade-out, white background, no gore
```

---

### 6.14 爆丹怪｜Exploding Pill Monster VFX

**普通攻擊特效**

```text
small bump tackle VFX, red orange pill impact star, tiny medicinal powder puff, cute unstable energy crack spark, white background, clean animation-ready keyframes
```

**技能攻擊特效**

```text
stylized alchemy burst VFX sprite sheet, red orange glowing crack anticipation, swelling pill energy ring, cute cartoon pop explosion, medicinal smoke cloud, small pill fragments, fade-out ember dust, white background, clean separated frames, no realistic explosion, no gore, no text numbers
```

**受擊 / 陣亡特效**

```text
bright crack flash, tiny pill fragments, orange powder puff, harmless smoke pop, failed alchemy burst fade-out, white background, animation-ready VFX frames
```

---

## 7. 各陣營色彩與特效語彙

| 陣營 / 地圖 | 小怪 | 主要色彩 | 特效語彙 |
| --- | --- | --- | --- |
| 怨念甦醒地 | 碎運鬼、黑運糰 | 灰、紫、黑 | 霉運煙、裂符、倒楣星、黑泥 |
| 紅帽管線城 | 水管工僕、噴氣水管兵 | 紅、藍、白、灰 | 扳手弧線、蒸氣、水滴、壓力波 |
| 影村訓練場 | 影紙忍、飛鏢影童 | 黑、靛、紙白 | 紙片、墨影、飛鏢、摺紙殘影 |
| 藍核防衛基地 | 藍核守衛球、小型正義盾 | 白、藍、紅 | 藍核心、能量彈、短光束、護罩 |
| 鋼筋戰隊工廠 | 螺絲工兵、磁鐵鋼怪 | 灰、橘、紅藍 | 螺絲、火星、磁力線、鐵片 |
| 七色葫蘆山 | 小葫蘆童、彩霧葫蘆 | 綠、黃、彩霧 | 藤葉、種子、葫蘆霧、泡泡 |
| 異火煉藥宗 | 丹火童子、爆丹怪 | 橘、紅、金 | 丹火、藥煙、爆丹、火星 |

---

## 8. VFX 與角色本體合成注意事項

- 普攻軌跡建議放在角色手部 / 武器前方，不要跨過臉部。
- 遠程投射物需要獨立輸出，方便調整速度與碰撞框。
- 地面型技能要保留底部接地位置，方便在遊戲中對齊地面。
- 吸引型技能要讓線條方向明確指向施法者。
- 受擊特效可以共用一部分素材，但顏色要配合陣營。
- 陣亡特效可獨立播放，不一定要和角色本體合併在同張圖。
- 若後續進 Godot / Unity / Web Canvas，建議每個 VFX 都拆成獨立 png sequence 或 spritesheet。

---

## 9. 常見修正 Prompt

### 9.1 特效太像 Boss 大招

```text
make it smaller, simpler, less flashy, enemy minion scale, normal attack readable, fewer particles, lower intensity
```

### 9.2 特效遮住角色

```text
effect does not cover the character body, keep center character silhouette clear, place effect in front of weapon only, transparent readable attack trail
```

### 9.3 方向不清楚

```text
clear left-to-right attack direction, obvious projectile path, readable motion trail, simple arrow-like energy flow without text or symbols
```

### 9.4 不是 sprite sheet

```text
multiple separated VFX keyframes, clean grid, equal spacing, animation-ready sprite sheet, each effect isolated, no overlapping frames
```

### 9.5 太寫實

```text
stylized chibi mobile game effect, cute cartoon particles, soft 2.5D anime style, no photorealistic fire, no realistic smoke, no cinematic explosion
```

---

## 10. 優先製作順序

### 第一優先：玩法辨識最重要

1. 水管工僕普通攻擊：扳手揮擊。
2. 噴氣水管兵技能：噴氣擊退。
3. 影紙忍技能：紙影突刺。
4. 飛鏢影童技能：扇形飛鏢。
5. 小型正義盾技能：小護罩。
6. 磁鐵鋼怪技能：磁力吸引。
7. 彩霧葫蘆技能：混亂彩霧。
8. 爆丹怪技能：延遲爆丹。

### 第二優先：共用素材

1. 小型命中特效：impact star。
2. 小型受擊煙：hit puff。
3. 小型暈眩星：dizzy stars。
4. 小型碎片：generic fragments。
5. 小型消散煙：defeated smoke。

共用素材可以節省美術與動畫成本，但每個陣營要換色與替換少量粒子形狀，避免看起來全部一樣。
