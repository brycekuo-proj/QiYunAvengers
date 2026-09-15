# 20｜音效、音樂與語音設計 V1

專案：《氣運復仇者》 / QiYun Avengers

用途：固定整體聲音風格、BGM 方向、Boss 主題音樂、技能音效、UI 音效、關卡環境音、混音規格、素材命名、導入引擎與 MVP 音訊範圍。

> 本文件接續：
>
> - `01_GAME_OVERVIEW.md`
> - `03_ART_DIRECTION.md`
> - `11_CORE_GAMEPLAY_COMBAT_DESIGN.md`
> - `14_BOSS_BATTLE_DESIGN.md`
> - `18_STORY_DIALOGUE_DESIGN.md`
> - `19_ANIMATION_SPRITE_SPEC.md`
>
> 聲音設計核心：**可愛外皮、黑色幽默、怨念復仇、英雄光環被搶走。**

---

## 0. 音訊設計總原則

### 0.1 核心聽感

《氣運復仇者》的聲音不能只有可愛，也不能只有黑暗。

最重要的混合方向是：

```text
可愛 Q 版音色 + 怨念黑紫能量 + 英雄正義旋律被扭曲
```

玩家聽到聲音時，應該能感覺：

- Ghost 很小，但怨念很深。
- 英雄很亮，但亮得有點吵。
- Boss 技能被奪取後，聲音從「正義」變成「黑化」。
- 戰鬥可讀性清楚，不被音效糊住。
- 死亡、道具、UI 有黑色幽默感。

### 0.2 聲音設計三層

| 層級 | 功能 | 聽感 |
|---|---|---|
| Gameplay Readability | 讓玩家知道危險、命中、冷卻、破防 | 清楚、短、方向明確 |
| Character Identity | 讓角色與 Boss 有記憶點 | 每位 Boss 有自己的音色語言 |
| Emotional Flavor | 傳達黑色幽默與反英雄 | 可愛、諷刺、怨念、命運壓迫 |

### 0.3 不做方向

避免：

- 過度寫實恐怖音效。
- 血腥、撕裂、慘叫作為主賣點。
- 太多高頻尖聲造成手機喇叭刺耳。
- BGM 永遠滿編制，蓋過戰鬥提示。
- 使用可辨識既有 IP 旋律、音效、語音口頭禪。
- UI 音效太像一般系統提示，缺少角色感。

---

## 1. 音訊分類

| 類型 | 用途 | 優先級 |
|---|---|---|
| BGM | 關卡、Boss、首頁、結算、Creator | 高 |
| SFX | 普攻、技能、受擊、破防、陷阱 | 最高 |
| UI SFX | 按鈕、卡片、三選一、商店、圖鑑 | 高 |
| Ambience | 地圖環境音、場景氛圍 | 中 |
| Stingers | 勝利、死亡、Boss 登場、技能奪取 | 高 |
| Voice Bark | Boss 短語音、Ghost 小聲反應 | 中，可後製 |
| Adaptive Layers | Phase 變化、氣運壓力、低血量 | 中高 |

MVP 優先順序：

```text
核心戰鬥 SFX → Boss SFX → UI SFX → BGM → Ambience → Voice Bark
```

---

## 2. 整體音樂風格

### 2.1 主風格關鍵字

```text
cute dark-comedy roguelite action, chibi revenge fantasy, playful spooky synth, distorted heroic brass, toy percussion, ghostly choir pads, punchy mobile game combat, mischievous bass, broken luck motif
```

### 2.2 樂器方向

| 聲音來源 | 用途 |
|---|---|
| Pluck synth | 可愛、Q 版、UI、輕快節奏。 |
| Toy piano / music box | 黑色幽默、命運童話感。 |
| Low synth bass | Ghost 怨念底色。 |
| Distorted brass | 英雄正義旋律被扭曲。 |
| Small drums / taiko-lite | 戰鬥推進。 |
| Reverse cymbal | 氣運反撲、Boss Phase。 |
| Ghost choir pad | 怨念集合體、Creator 場景。 |
| Glitch erase noise | Creator / Eraser / 白頁擦除。 |
| Bamboo / wood percussion | 忍者、民俗、修仙系關卡。 |
| Electric guitar-lite | 武道、Boss 狂暴，但不要太寫實金屬。 |

### 2.3 主旋律 Motif

本作可以設計一個「敗者怨念」主題動機：

```text
短短 4～6 音，下行後突然上揚。
感覺像差點倒下，但不甘心又爬起來。
```

使用方式：

- 首頁用慢速、音樂盒版本。
- 普通戰鬥用節奏化版本。
- Boss 破防時用黑紫逆轉版本。
- Creator 戰用被擦除、斷裂、重組版本。

---

## 3. BGM 系統

### 3.1 音樂分層

建議 BGM 做成可分層：

| Layer | 觸發 | 功能 |
|---|---|---|
| Base | 關卡開始 | 場景主氛圍。 |
| Combat | 小怪戰開始 | 增加鼓與低音。 |
| Danger | 低血量 / 氣運壓力高 | 增加高頻脈衝與不安定音。 |
| Boss | Boss 出場 | 切換或疊加 Boss 主題。 |
| Phase | Boss Phase 2 / 3 | 增加速度、鼓、扭曲英雄旋律。 |
| Broken | Boss 被相剋破防 | 短暫抽掉高亮英雄音，換成 Ghost Motif。 |
| Victory | Boss 死亡 / 奪取 | 短 Stinger 接回地圖。 |

### 3.2 Loop 規格

| 用途 | 長度 | 規格 |
|---|---:|---|
| 首頁 | 60～90 秒 | 可自然 loop。 |
| 普通關卡 | 60～120 秒 | 可分 Base / Combat。 |
| Boss | 90～150 秒 | 至少 2 層 Phase 強化。 |
| 商店 | 45～75 秒 | 輕、怪、不要吵。 |
| 事件 | 30～60 秒 | 可用短循環。 |
| Creator | 120～180 秒 | 可做多段變形。 |

### 3.3 音樂強度

| 狀態 | 強度 | 說明 |
|---|---:|---|
| Menu | 20～35% | 背景感，讓 UI 清楚。 |
| Stage Base | 35～50% | 不搶 SFX。 |
| Combat | 50～70% | 有節奏但保留提示空間。 |
| Boss P1 | 65～75% | 明確壓力。 |
| Boss P3 | 75～85% | 高壓但不能糊。 |
| Creator P3 | 80～90% | 終局壓迫。 |

---

## 4. 10 張地圖 BGM 方向

### 4.1 0 怨念甦醒地

定位：Ghost 誕生、失敗者殘響。

音樂方向：

```text
slow music box, ghost pad, soft broken bells, low purple bass, distant reversed whispers, cute but empty
```

關鍵聽感：像可愛玩具壞掉後，自己在深夜播放。

### 4.2 1 紅帽管線城

定位：平台英雄世界、管線、施工、歡呼被扭曲。

音樂方向：

```text
bouncy toy percussion, pipe clanks, muted heroic fanfare fragments, comic walking bass, steam rhythm
```

關鍵聽感：很歡樂，但越聽越像工地在追殺你。

### 4.3 2 影村訓練場

定位：忍者、紙影、分身、月光。

音樂方向：

```text
wood block rhythm, muted shamisen-like plucks, shadow synth, short silence gaps, sneaky percussion
```

關鍵聽感：節奏會突然消失，像真身不見了。

### 4.4 3 藍核防衛基地

定位：特攝光、能源基地、倒數。

音樂方向：

```text
heroic synth brass, pulsing blue core bass, alarm arpeggio, clean electronic drums, distorted justice chord
```

關鍵聽感：正義很亮，也很像警報。

### 4.5 4 鋼筋戰隊工廠

定位：合體、工廠、彩色戰隊。

音樂方向：

```text
factory percussion, metal hits, team chant-like synth stabs, marching rhythm, mechanical bass
```

關鍵聽感：團隊精神像輸送帶一樣把你推進機器裡。

### 4.6 5 七色葫蘆山

定位：民俗法寶、山、元素、吸收反吐。

音樂方向：

```text
folk flute-like synth, gourd percussion, bouncing mountain rhythm, elemental accents, playful ritual mood
```

關鍵聽感：可愛民俗感，但葫蘆裡傳來奇怪回音。

### 4.7 6 異火煉藥宗

定位：玄幻煉藥、異火、丹爐。

音樂方向：

```text
low ritual drums, fire crackle rhythm, mystical plucks, unstable flame synth, rising alchemy tension
```

關鍵聽感：每個鼓點都像丹爐快炸。

### 4.8 7 蛛網都市天台

定位：都市英雄、蛛網、高樓夜景。

音樂方向：

```text
urban night beat, plucked web strings, siren-like pads, swing rhythm, rooftop wind ambience
```

關鍵聽感：城市在歡呼英雄，風在提醒你會掉下去。

### 4.9 8 鬥氣武道星

定位：格鬥、爆氣、空中連段。

音樂方向：

```text
fast combat drums, energy bass, short vocal chops, rising power aura, punchy heroic melody twisted darker
```

關鍵聽感：熱血，但熱血到有點不講理。

### 4.10 9 命運劇場

定位：Creator、白頁、劇本、Eraser。

音樂方向：

```text
broken orchestra, glitch erase noise, reversed choir, white-noise sweeps, fragmented hero motifs, final fate tension
```

關鍵聽感：像有人一邊作曲，一邊把你的音軌刪掉。

---

## 5. Boss 主題音樂方向

### 5.1 Boss 音樂共同規格

每位 Boss 的音樂都要有兩個面向：

```text
英雄主題：明亮、自信、正義、被世界偏愛。
Ghost 反轉：黑紫、扭曲、破碎、怨念回收。
```

Boss 被破防時，BGM 可短暫切入 Ghost Motif，表示英雄的劇本被打斷。

### 5.2 M先生

音樂：

```text
bouncy pipe-city boss theme, comic heroic brass, pipe percussion, jump-slam accents, distorted maintenance rhythm
```

重點：每次跳砸前可以有短促上行音，讓玩家聽覺預判。

### 5.3 滅影忍者

音樂：

```text
stealth ninja boss theme, broken wood percussion, sudden silence, shadow plucks, fake rhythm decoys
```

重點：分身出現時可以加入假節拍，真身攻擊前留一個很短的安靜空拍。

### 5.4 U-man

音樂：

```text
bright giant hero theme, pulsing blue core, heroic synth brass, countdown alarm, beam charge riser
```

重點：胸口核心倒數要和 BGM 脈衝同步。

### 5.5 鋼筋戰士

音樂：

```text
team hero factory boss theme, marching drums, metallic claps, colorful synth stabs, combined armor impact
```

重點：合體時加入五段短音，但不能像既有戰隊旋律。

### 5.6 葫蘆爺

音樂：

```text
folk magic boss theme, hollow gourd bass, playful ritual percussion, inhale-exhale rhythm, elemental color changes
```

重點：吸收招式時 BGM 低頻往內收，反吐時突然爆開。

### 5.7 消炎

音樂：

```text
alchemy fire boss theme, unstable flame synth, ritual drums, explosive pills, heroic cultivation melody twisted into resentment
```

重點：火丹倒數用短促顆粒音，不要被火焰環境音蓋掉。

### 5.8 失敗的面

音樂：

```text
urban web hero boss theme, rooftop beat, elastic string plucks, siren pads, quick swing accents, web tension pulls
```

重點：蛛線牽引要有明顯拉伸音，像橡皮筋被拉長。

### 5.9 吾空

音樂：

```text
high-energy martial boss theme, fast drums, aura bass, punch impacts, rising power motif, exaggerated heroic power-up twisted dark
```

重點：爆氣前 BGM 暫時抽空，讓玩家聽見氣聚集。

### 5.10 Creator

音樂三段：

| Phase | 聲音方向 |
|---|---|
| P1 創辦者 | 極簡節拍、滑鼠點擊、發布會般乾淨音色、冷淡白噪。 |
| P2 完美英雄 | 扭曲全部英雄主題，像最完美但最假。 |
| P3 神話創造者 | 合唱、雷霆、Eraser 刪除噪聲、主旋律被擦掉又重組。 |

Eraser 發動時，音樂可以短暫被低通、靜音、刮擦聲覆蓋，製造「音軌被刪除」的感覺。

---

## 6. Ghost 音效設計

### 6.1 Ghost 聲音語言

Ghost 的聲音不是普通魔法，而是「很多失敗者疊在一起的小聲音」。

關鍵元素：

- Soft ghost puff。
- Black-purple energy fizz。
- Tiny cute cloth movement。
- Low whisper layer，但不要恐怖。
- Reverse sparkle，像氣運被倒著吸回來。

### 6.2 Ghost 基礎 SFX

| 行動 | 音效方向 |
|---|---|
| idle | 很輕的斗篷飄動與怨念氣泡。 |
| move | 軟軟的飄移聲，不要腳步太重。 |
| dash | 短黑影 whoosh + 小殘影 pop。 |
| basic_attack_1 | 小爪擊 swish。 |
| basic_attack_2 | 橫掃 whoop。 |
| basic_attack_3 | 怨念重擊 thump + 低頻小爆。 |
| hit | 可愛短悶聲 + 怨念漏氣。 |
| dead | 黑紫煙散掉 + 小小失敗鈴聲。 |
| victory | 氣運吸收 reverse chime + 怨念和聲。 |

---

## 7. 八個 Boss 奪取技能 SFX

### 7.1 管線衝擊

來源：M先生

Ghost 版本聲音：

```text
pipe metal knock + underground rumble + purple shockwave crack
```

分段：

| 時機 | 聲音 |
|---|---|
| 起手 | 短管線敲擊。 |
| 發動 | 地面低頻震動。 |
| 命中 | 碎裂氣運片 + 小金屬響。 |
| 破隱 | 影子被震出的 pop。 |

### 7.2 影遁衝刺

來源：滅影忍者

```text
soft shadow vanish + paper flutter + quick dark whoosh
```

重點：短、快、乾淨，不拖尾過長。

### 7.3 核心光束

來源：U-man

```text
blue core charge reversed into dark beam, focused synth laser, cracked heroic chime
```

重點：蓄力聲要提示玩家正在站樁。

### 7.4 破甲合擊

來源：鋼筋戰士

```text
multi-hit ghost punches, armor crack, team call chopped into ghost echoes
```

重點：多段要有節奏，不要糊成一聲。

### 7.5 吞運葫蘆

來源：葫蘆爺

```text
hollow gourd inhale, suction swirl, cork pop, reflected energy spit
```

重點：吸收成功要有明顯「裝進去」的聲音。

### 7.6 怨火爆燃

來源：消炎

```text
cute cursed flame ignition, low alchemy pop, purple fire loop, anti-heal sizzling
```

重點：火場 loop 不能太吵，避免長時間疲勞。

### 7.7 蛛線牽引

來源：失敗的面

```text
thin web shot, elastic stretch, sticky snap, rooftop wind pull
```

重點：命中、拉動、斷線要三種不同聲音。

### 7.8 鬥氣爆發

來源：吾空

```text
small ghost roar, aura burst, punchy bass pulse, unstable power-up
```

重點：霸體啟動要有明確防禦感，但不能像無敵星星。

### 7.9 Eraser

來源：Creator

```text
paper scrape, white-noise erase, audio dropout, glitch slice, soft deletion pop
```

重點：Eraser 是「清除」，不是普通爆炸。

---

## 8. Boss SFX 規格

### 8.1 Boss 通用 SFX

| 行為 | 聲音方向 |
|---|---|
| intro | 短 Stinger，帶 Boss 主題音色。 |
| phase_change | 音樂升層 + 能量轉換。 |
| light_attack | 清楚短音。 |
| heavy_attack | 長前搖 + 低頻命中。 |
| signature_attack | Boss 專屬音色最明顯。 |
| broken | 英雄音色碎裂，Ghost 怨念插入。 |
| defeated | 氣運被抽離，Boss 主題變調下沉。 |

### 8.2 相剋破防聲音

破防聲應該統一有一個核心標記：

```text
golden luck glass crack + purple reverse pull
```

這是玩家聽覺上的「我破解你了」。

不同 Boss 再加專屬層：

| Boss | 追加層 |
|---|---|
| M先生 | 管線彎掉。 |
| 滅影忍者 | 紙分身碎裂。 |
| U-man | 藍核裂開。 |
| 鋼筋戰士 | 裝甲螺絲掉落。 |
| 葫蘆爺 | 葫蘆漏氣。 |
| 消炎 | 火焰被吸熄。 |
| 失敗的面 | 蛛線斷裂。 |
| 吾空 | 爆氣中斷。 |
| Creator | 鍵盤刪除鍵 + 玻璃裂。 |

---

## 9. 小怪 SFX 規格

### 9.1 小怪聲音原則

- 小怪音效要短。
- 不要每隻小怪都有長語音。
- 同類小怪可共用音色變體。
- 攻擊前搖比受擊聲更重要。
- 輔助小怪技能音要清楚，讓玩家知道要優先處理。

### 9.2 小怪類型音色

| 類型 | 音色 |
|---|---|
| 碎運鬼 | 小幽靈 puff、破碎鈴。 |
| 黑運糰 | 軟黏 blob、倒楣泡泡。 |
| 水管工僕 | 小金屬敲擊、水管 swish。 |
| 噴氣水管兵 | 蒸氣噴射、閥門轉動。 |
| 影紙忍 | 紙片、短影步、苦無細聲。 |
| 飛鏢影童 | 輕投擲、紙風聲。 |
| 藍核守衛球 | 小電子 beep、能量 pulse。 |
| 小型正義盾 | 盾牌 clank、護盾 hum。 |
| 螺絲工兵 | 螺絲轉動、機械腳步。 |
| 磁鐵鋼怪 | 磁吸 hum、金屬拉扯。 |
| 小葫蘆童 | 空洞 pop、吸氣小聲。 |

---

## 10. 陷阱與關卡機制 SFX

### 10.1 陷阱生命週期聲音

每個陷阱聲音分三段：

```text
Warning → Active → Recovery
```

| 狀態 | 聲音目的 |
|---|---|
| Warning | 告訴玩家危險快來了。 |
| Active | 表示傷害或控制正在發生。 |
| Recovery | 告訴玩家危險結束，可回去。 |

### 10.2 陷阱音效表

| 陷阱 | Warning | Active | Recovery |
|---|---|---|---|
| 裂運地面 | 裂縫小響 | 黑紫煙爆 | 碎片落地 |
| 地底噴管 | 蒸氣預熱 | 噴管 burst | 閥門關閉 |
| 影紙地雷 | 紙片顫動 | 影刃 burst | 紙灰散開 |
| 藍核雷射 | 充能 beep | 雷射掃過 | 核心冷卻 |
| 火丹地雷 | 丹藥倒數 | 小爆燃 | 火星熄滅 |
| 蛛網陷阱 | 線拉緊 | sticky snap | 線斷掉 |
| 白頁擦除 | 紙面摩擦 | erase sweep | 空白 pop |

---

## 11. UI 音效設計

### 11.1 UI 聽感

UI 音效要可愛、短、帶一點怨念。

關鍵字：

```text
cute dark pop, ghost bubble, broken chime, small paper flip, cursed menu click
```

### 11.2 UI SFX 表

| UI 行為 | 聲音方向 |
|---|---|
| Button hover / focus | 小幽靈 pop。 |
| Button confirm | 乾淨 click + 怨念 chime。 |
| Button cancel | 小漏氣聲。 |
| 卡片翻開 | 紙牌 flip + 黑紫閃。 |
| 三選一出現 | 三段短 chime。 |
| 選中技能 | 技能來源 Boss 音色短版。 |
| 選中遺物 | 稀有度 chime。 |
| 商店購買 | 怨幣叮噹 + 小怪笑聲。 |
| 錢不夠 | 空錢包 puff。 |
| 圖鑑解鎖 | 書頁 + 破碎氣運鈴。 |
| 暫停 | 紙張壓住聲。 |
| 重新開始 | 倒放 chime。 |

### 11.3 稀有度音效

| 稀有度 | 聲音 |
|---|---|
| Common | 短小木鈴。 |
| Rare | 藍紫 chime。 |
| Epic | 金紫和弦。 |
| Legendary | 低頻 + 黑金亮音。 |
| Cursed | 紅黑裂聲 + 心跳感。 |
| Joke | 可愛滑稽 pop。 |

---

## 12. Voice Bark 設計

### 12.1 使用原則

語音不是必需，但可增加角色記憶點。

MVP 可先不做真人語音，用：

- 合成語音。
- 簡短人聲音節。
- 可愛 murmur。
- Boss 文字台詞 + 音效代替語音。

### 12.2 Ghost Voice

Ghost 不適合長篇喊話。

聲音方向：

```text
soft layered whisper, childlike but not childish, many tiny voices, low-volume ghost murmur
```

可用短語：

```text
「收下。」
「輪到我。」
「又是光。」
「不要刪我。」
```

### 12.3 Boss Voice

Boss 可有短 Battle Bark：

| 狀態 | 範例 |
|---|---|
| 開戰 | 「正義登場！」 |
| 大招 | 「看好了！」 |
| 破防 | 「怎麼可能？」 |
| 低血 | 「我不會輸！」 |
| 死亡 | 「劇本不是這樣……」 |

注意：不要使用既有角色口頭禪或可辨識模仿。

---

## 13. 混音規格

### 13.1 音量優先級

由高到低：

1. 玩家受擊 / 致命危險提示。
2. Boss 大招前搖。
3. 玩家技能命中 / 破防。
4. 小怪攻擊前搖。
5. UI 操作。
6. 普通命中聲。
7. Ambience。
8. BGM。

### 13.2 預設音量比例

| 類型 | 音量方向 |
|---|---:|
| Master | 100% |
| BGM | 55～70% |
| SFX | 80～100% |
| UI | 65～85% |
| Voice | 75～95% |
| Ambience | 25～45% |

### 13.3 頻率注意

- 手機喇叭低頻有限，重要低頻要疊中低頻可聽層。
- 避免 2k～5k Hz 長時間刺耳高頻。
- 雷射、警報、倒數音要短，不要持續尖叫。
- 火場、風、機械 ambience 要低音量，避免疲勞。

### 13.4 Ducking

建議：

- Boss 大招 Warning 時，BGM 短暫 duck 10～20%。
- 玩家低血量時，心跳或危險提示優先於 BGM。
- 相剋破防瞬間，其他普通小怪音效降低一點，突出破防爽感。
- Creator Eraser 發動時，BGM 可短暫 glitch duck。

---

## 14. 音訊檔案規格

### 14.1 格式

| 用途 | 格式 | 備註 |
|---|---|---|
| BGM | OGG / AAC | Loop 友善，體積小。 |
| SFX | WAV source，OGG runtime | 原檔保留 WAV，遊戲內可壓縮。 |
| UI | WAV source，OGG runtime | 短音效可壓縮。 |
| Voice | WAV source，OGG runtime | 需保留乾聲版本。 |
| Ambience | OGG loop | 長循環壓縮。 |

### 14.2 取樣率

| 類型 | 建議 |
|---|---:|
| Source | 48 kHz / 24-bit WAV |
| Runtime | 44.1 或 48 kHz OGG |
| Mobile | 44.1 kHz 可接受 |

### 14.3 Loudness

| 類型 | 方向 |
|---|---|
| BGM | 不要過度壓縮，保留動態。 |
| SFX | 峰值清楚，不爆音。 |
| UI | 音量一致，不忽大忽小。 |
| Voice | 清楚可聽，但不壓過危險提示。 |

---

## 15. 命名規則

### 15.1 資料夾

```text
assets/audio/
  bgm/
    menu/
    stage/
    boss/
    creator/
  sfx/
    ghost/
    boss/
    enemy/
    skill/
    trap/
    ui/
    item/
  ambience/
    stage/
  voice/
    ghost/
    boss/
  stinger/
    victory/
    death/
    unlock/
```

### 15.2 檔名規則

```text
bgm_[context]_[id]_[loop/intro/phase].ogg
sfx_[category]_[id]_[action]_[variant].wav
ui_[screen]_[action]_[variant].wav
amb_[stage_id]_[layer].ogg
vox_[character_id]_[state]_[variant].wav
stinger_[event]_[id].wav
```

範例：

```text
bgm_stage_01_pipe_city_loop.ogg
bgm_boss_m_sir_phase2.ogg
sfx_skill_pipe_impact_cast_01.wav
sfx_skill_pipe_impact_hit_01.wav
sfx_boss_shadow_ninja_clone_spawn_01.wav
sfx_trap_pipe_steam_warning_01.wav
ui_card_select_rare_01.wav
vox_ghost_skill_steal_01.wav
stinger_boss_defeated_m_sir.wav
```

---

## 16. 音訊事件命名

程式事件建議使用固定 key。

### 16.1 Gameplay Events

```text
audio.play("ghost.attack.1")
audio.play("ghost.dash")
audio.play("skill.pipe_impact.cast")
audio.play("skill.pipe_impact.hit")
audio.play("boss.m_sir.jump_slam.warning")
audio.play("boss.m_sir.jump_slam.impact")
audio.play("boss.shadow_ninja.clone.spawn")
audio.play("combat.luck_break")
audio.play("combat.player_hit")
audio.play("combat.death")
```

### 16.2 Music Events

```text
audio.music.setStage("stage_01_pipe_city")
audio.music.enterCombat()
audio.music.exitCombat()
audio.music.enterBoss("m_sir")
audio.music.setBossPhase(2)
audio.music.triggerBrokenLuck()
audio.music.triggerVictory()
audio.music.enterCreatorPhase(3)
```

---

## 17. Adaptive Audio 設計

### 17.1 氣運壓力

氣運壓力升高時，聲音變化：

| 壓力 | 聲音變化 |
|---|---|
| 低 | 正常 BGM。 |
| 中 | 加入微弱金白高頻 shimmer。 |
| 高 | 加入英雄旋律碎片與警報脈衝。 |
| 爆表 | 短暫壓過 Ghost motif，Boss 主題變強。 |

### 17.2 低血量

低血量不需要很吵。

建議：

- 心跳低頻。
- BGM 稍微 low-pass。
- UI 邊框音與畫面同步。
- 不要一直播放尖銳警告聲。

### 17.3 Boss 破防

破防時：

```text
Boss Theme duck → golden crack + purple reverse pull → Ghost motif 1～2 秒 → 回到 Boss Phase 音樂
```

這個流程會把相剋爽感做成聽覺記憶。

---

## 18. 音效生成 Prompt 方向

若使用 AI 音效工具，可用以下文字方向。

### 18.1 Ghost Dash

```text
short cute ghost dash sound effect, dark purple shadow whoosh, soft cloth flutter, tiny magical pop, mobile game action SFX, clean and readable, not scary, no voice
```

### 18.2 管線衝擊

```text
stylized mobile game ground shockwave sound, small metal pipe hit, underground rumble, purple magic crack, punchy but cute, short combat SFX, no realistic explosion
```

### 18.3 影遁衝刺

```text
fast ninja shadow vanish sound, paper flutter, soft dark whoosh, tiny smoke pop, clean mobile game SFX, short and readable
```

### 18.4 核心光束

```text
stylized dark hero laser beam sound, short energy charge, focused beam release, cracked blue core chime, mobile game boss skill SFX, not sci-fi realistic, not too harsh
```

### 18.5 Eraser

```text
magical eraser deletion sound effect, paper scrape, white noise swipe, brief audio dropout, soft glitch pop, final boss ability SFX, clean mobile game style
```

### 18.6 稀有遺物獲得

```text
cute cursed treasure obtain sound, dark chime, small ghost pop, magical sparkle, roguelite item pickup, short UI SFX, satisfying but not loud
```

---

## 19. MVP 音訊範圍

第一版不要做完整 10 關音樂。

### 19.1 MVP 必做

| 類型 | 數量 | 內容 |
|---|---:|---|
| BGM | 4 | 首頁、教學地圖、M先生 Boss、滅影忍者 Boss。 |
| Ghost SFX | 10～15 | 移動、Dash、普攻三段、受擊、死亡、勝利。 |
| 技能 SFX | 8～12 | 管線衝擊、影遁衝刺，每招 cast / hit / special。 |
| Boss SFX | 20～30 | M先生、滅影忍者核心招式。 |
| 小怪 SFX | 15～25 | 前兩關小怪共用變體。 |
| UI SFX | 15～20 | 按鈕、卡片、三選一、商店、圖鑑。 |
| Stinger | 8～12 | Boss 登場、擊敗、技能奪取、死亡、勝利。 |
| Ambience | 3 | 怨念甦醒地、管線城、影村。 |

### 19.2 MVP 可延後

- 全 Boss 專屬 BGM。
- 完整語音。
- 多語音版本。
- 複雜 adaptive audio middleware。
- 每個小怪完全獨立音色。
- 完整 10 張地圖 ambience。

---

## 20. Godot / 引擎導入建議

### 20.1 Godot

若使用 Godot：

- `AudioStreamPlayer`：UI / 全域短音。
- `AudioStreamPlayer2D`：場上角色、陷阱、技能，可有距離感。
- BGM 使用獨立 Music Manager。
- UI 音效不要使用 2D 距離衰減。
- Boss 大招 Warning 用高優先級 Bus。
- 設定 Music / SFX / UI / Voice / Ambience 五個 Bus。

### 20.2 Bus 建議

```text
Master
  Music
  SFX
    Player
    Enemy
    Boss
    Trap
  UI
  Voice
  Ambience
```

### 20.3 Mobile 注意

- 同時音效數量限制，避免小怪太多時爆音。
- 同類小怪音效加 pitch variation，避免機械重複。
- 長 ambience 使用低音量 loop。
- 避免過多未壓縮 WAV 進 APK。

---

## 21. 音訊品質驗收清單

### 21.1 SFX 驗收

- 是否能聽出攻擊方向或危險類型？
- Boss 大招前搖是否夠明顯？
- 玩家受擊音是否不刺耳？
- 相剋破防是否有爽感？
- 技能 cast / hit / special 是否分得清？
- 同時多個小怪音效是否不混亂？
- 手機喇叭是否仍可聽清？

### 21.2 BGM 驗收

- 是否符合可愛黑色幽默？
- 是否不直接像任何既有 IP 旋律？
- 是否不蓋過戰鬥提示？
- Boss Phase 是否有升級感？
- 破防時是否有音樂反轉？
- Loop 是否自然？
- 長時間聽是否不疲勞？

### 21.3 UI 驗收

- 點擊是否乾淨？
- 稀有度是否聽得出差異？
- 三選一是否有抽卡感但不廉價？
- 商店音效是否可愛又有點壞？
- 圖鑑解鎖是否有成就感？

---

## 22. 音訊實作驗收句

所有音訊都要服務這句話：

```text
玩家不看畫面，也要能大概聽出：誰要攻擊、哪招命中、Boss 是否破防、Ghost 是否正在把英雄的氣運搶走。
```

如果聲音只是熱鬧，但不能幫助玩家判斷戰鬥，就不是合格音效。
