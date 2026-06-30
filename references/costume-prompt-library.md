# AI 漫剧服装提示词库 — 造型大师参数增强

> **来源**: 哈哈编程《AI漫剧服装类提示词大全·古风仙侠类》(2026)
> **吸收日期**: 2026-06-30
> **关联**: 造型大师 6维参数 → ③ 服饰结构 ④ 配色方案 ⑤ 材质渲染
> **灯光大师联动**: 服装材质→决定主辅轮选型(见各款式「灯光建议」)
> **用途**: AI 短剧角色服装 prompt 词精准选配，按题材/身份/气质三维索引
> **配套**: `references/character-hairstyle-encyclopedia.md`（108种发型）

---

## 使用方式

```
「造型大师，为[角色名]设计[题材]·[身份]服装 → 输出款式编号+关键词+灯光联动建议」
```

---

## 一、古风仙侠类（8种核心款式）

### 1.1 仙侠长袍战斗服
| 维度 | 内容 |
|------|------|
| **风格** | 玄色银纹·铠甲护肩·战斗飘逸 |
| **身份** | 出战修士 / 战斗型弟子 |
| **关键词** | `玄色、银纹、铠甲护肩、飘带飞扬、御剑凌空` |
| **英文Prompt** | `dark mystical robe, silver patterns, armored shoulder guards, flowing ribbons, flying sword immortal, dynamic battle pose, layered dark blue and black fabric` |
| **配色** | #1a1a2e 玄黑 / #c0c0c0 银纹 / #0d0d1a 内衬 |
| **材质** | 金属肩甲 + 丝绸主体 + 纱质飘带 |
| **灯光建议** | 主光侧逆(kicker)凸显银纹反光 + 轮廓光打亮飘带体积 → 「逆光剪影」或「赛博冷光」 |

### 1.2 宗门弟子服
| 维度 | 内容 |
|------|------|
| **风格** | 青蓝宽袖·云纹刺绣·清雅素净 |
| **身份** | 普通/内门弟子 |
| **关键词** | `青蓝、宽袖、云纹刺绣、束腰带、清雅素净` |
| **英文Prompt** | `cyan-blue sect disciple robe, wide sleeves, cloud pattern embroidery, cinched waist belt, elegant and pure, layered scholar robes, traditional Chinese academy style` |
| **配色** | #4a7c8e 青蓝 / #f0ece4 内领白 / #d4af37 云纹金线 |
| **材质** | 棉麻主体 + 刺绣纹理 + 丝质束带 |
| **灯光建议** | 柔光漫射(soft diffused)凸显布料质感 + 避免强侧光防纹理过曝 → 「柔光窗光」 |

### 1.3 白衣剑仙飘逸袍
| 维度 | 内容 |
|------|------|
| **风格** | 纯白层叠·流云刺绣·轻纱飘逸 |
| **身份** | 剑仙 / 上仙 / 主角高光 |
| **关键词** | `白衣、宽袖、流云刺绣、轻纱层叠、御剑气质` |
| **英文Prompt** | `white sword immortal robe, flowing wide sleeves, cloud embroidery, layered translucent gauze, ethereal elegance, wind-blown fabric, immortal presence, pure white with silver accents` |
| **配色** | #ffffff 纯白 / #e8e8e8 层纱 / #c0c0c0 银线绣 |
| **材质** | 多层轻纱 + 绸缎主身 + 透明外罩 |
| **灯光建议** | 背光逆射(backlight)穿透轻纱造光晕 + 正面补柔和面光 → 「圣光穿透」或「柔光背光」 |

### 1.4 魔道黑金战袍
| 维度 | 内容 |
|------|------|
| **风格** | 黑金暗纹·锋利肩甲·邪魅冷峻 |
| **身份** | 魔尊 / 反派主角 |
| **关键词** | `黑金、暗纹、锋利肩甲、暗红内衬、邪魅冷峻` |
| **英文Prompt** | `black-gold demon lord battle robe, dark hidden patterns, spiked sharp shoulder armor, dark red inner lining, sinister cold aura, dark energy wisps, menacing presence` |
| **配色** | #0a0a0a 墨黑 / #d4af37 金纹 / #8b0000 暗红内衬 |
| **材质** | 硬甲片 + 金属饰件 + 厚重锦缎 |
| **灯光建议** | 底光(underlight)从下往上打 + 轮廓光勾金纹边缘 → 「底光恶魔」或「阴森侧光」 |

### 1.5 女主汉服轻纱飘带
| 维度 | 内容 |
|------|------|
| **风格** | 粉紫轻纱·飘带翻跃·柔美灵动 |
| **身份** | 女主角 / 仙子 / 大家闺秀 |
| **关键词** | `粉紫、轻纱、飘带翻跃、花纹刺绣、柔美灵动` |
| **英文Prompt** | `pink-purple hanfu, light gauze, dancing flying ribbons, floral embroidery, soft and lively, flowing fabric, feminine grace, traditional Chinese dress with waterfall sleeves` |
| **配色** | #d8b4d0 粉紫 / #f5e6f0 浅纱 / #c9a0b0 花绣 |
| **材质** | 轻纱外层 + 丝绸内衬 + 刺绣花边 |
| **灯光建议** | 正面柔光渲染肤色 + 侧逆光透纱显飘带层次 → 「柔光窗光」+ 背光补层次 |

### 1.6 宫廷贵族华服
| 维度 | 内容 |
|------|------|
| **风格** | 金色刺绣·珠玉流苏·雍容华贵 |
| **身份** | 王后 / 公主 / 贵妃 |
| **关键词** | `金色、刺绣、珠玉流苏、层叠裙摆、雍容华贵` |
| **英文Prompt** | `golden imperial court dress, intricate embroidery, pearl and jade tassels, layered skirt hem, luxurious and noble, phoenix motifs, elaborate hair ornaments, regal bearing` |
| **配色** | #d4af37 帝金 / #8b0000 朱红边 / #ffffff 珍珠白 |
| **材质** | 织锦缎 + 珍珠串饰 + 金属发冠 |
| **灯光建议** | 多点布光：顶光打下突出金冠 + 正面柔光照珠宝反光 + 侧光显刺绣层次 → 「三点布光」 |

### 1.7 江湖侠客布衣
| 维度 | 内容 |
|------|------|
| **风格** | 棕灰麻布·斗笠披风·洒脱不羁 |
| **身份** | 游侠 / 流浪剑客 |
| **关键词** | `棕灰、麻布、束带、披风斗笠、洒脱不羁` |
| **英文Prompt** | `brown-gray hemp cloth ranger, conical bamboo hat, draped cloak, tied leather belt, free and unrestrained, rugged wandering swordsman, earthy tones, weathered traveler` |
| **配色** | #6b5b4e 棕灰 / #8b7355 麻本色 / #3d2b1f 革带 |
| **材质** | 粗麻 + 皮革 + 竹编斗笠 |
| **灯光建议** | 硬光侧照(hard side light)强化粗粝质感 + 斗笠在面部投射半阴影 → 「阴森侧光」或「硬朗侧光」 |

### 1.8 仙门长老道袍
| 维度 | 内容 |
|------|------|
| **风格** | 淡紫道袍·祥云纹路·仙风道骨 |
| **身份** | 掌门 / 长老 / 师尊 |
| **关键词** | `淡紫、道袍、祥云纹路、玉佩配饰、仙风道骨` |
| **英文Prompt** | `light purple Taoist elder robe, auspicious cloud patterns, jade pendant accessories, immortal demeanor, wooden staff, flowing white beard, wise spiritual master, celestial authority` |
| **配色** | #9b8ea8 淡紫 / #f5f0e8 内衬白 / #6b8e6b 玉佩绿 |
| **材质** | 厚缎 + 佩玉 + 木杖 |
| **灯光建议** | 顶侧光(top-side light)突出皱纹/胡须立体感 + 柔和轮廓光显仙气 → 「古典顶光」或「柔光窗光」 |

---

## 二、通用关键词池（跨款式组合）

### 材质层叠
| 中文 | 英文 Prompt | 配什么款式 |
|:----|:------------|:----------|
| 飘逸 | `flowing, ethereal, wind-blown` | 1.1/1.3/1.5 |
| 层叠 | `layered, multi-layered, overlapping fabric` | 1.2/1.3/1.6 |
| 轻纱 | `gauze, translucent silk, sheer fabric` | 1.3/1.5 |
| 宽袖 | `wide sleeves, waterfall sleeves, flowing sleeves` | 1.2/1.3 |
| 纹理刺绣 | `textured embroidery, intricate patterns, brocade` | 1.2/1.6/1.8 |

### 配饰点缀
| 中文 | 英文 Prompt | 款式 |
|:----|:------------|:----|
| 飘带 | `ribbon, sash, flowing ribbon` | 1.1/1.5 |
| 玉佩 | `jade pendant, ornamental jade` | 1.8 |
| 流苏 | `tassel, beaded tassel, dangling ornament` | 1.6 |
| 斗笠 | `bamboo hat, conical hat, traveler hat` | 1.7 |
| 护甲 | `armored shoulder, metal pauldron, battle gear` | 1.1/1.4 |

### 气质关键词
| 风格方向 | 关键词 |
|:---------|:-------|
| 战斗系 | `dynamic, battle-ready, powerful stance, wind-blown` |
| 仙气系 | `ethereal, celestial, otherworldly, graceful` |
| 邪魅系 | `sinister, menacing, dark aura, cold gaze` |
| 江湖系 | `rugged, weathered, free-spirited, untamed` |
| 华贵系 | `regal, luxurious, noble bearing, opulent` |

---

## 三、灯光大师联动矩阵

> 造型大师选定服装后 → 灯光大师根据材质/配色自动匹配灯光方案

| 材质类型 | 服装举例 | 灯光方案 | 原因 |
|:---------|:---------|:---------|:-----|
| 金属/甲片 | 1.1/1.4 | **侧逆光(kicker)** + 轮廓光 | 金属需要定向光产生反光，柔光会让甲片变灰 |
| 轻纱/透明 | 1.3/1.5 | **逆光(backlight)** + 正面补光 | 逆光穿透纱质显通透感，正面补光保肤色 |
| 粗麻/棉布 | 1.7 | **硬侧光(hard side)** | 硬光强化粗粝质感，柔光会让粗麻变"塑料" |
| 刺绣/锦缎 | 1.2/1.6/1.8 | **三点布光** + 柔光 | 刺绣需要均匀光线让纹理可见，硬光会造成局部过曝 |
| 深色/黑色 | 1.1/1.4 | **强轮廓光** + 底光 | 深色吸光，必须靠轮廓光分离主体与背景 |

---

## 四、扩展题材索引（后续扩充占位）

```
AI漫剧服装类提示词大全·其他题材（待吸收）
━━━━━━━━━━━━━━━━━━━━━━
■ 二、玄幻奇幻类（魔法袍/兽皮/异域风情） 
■ 三、武侠江湖类（劲装／夜行衣／掌门服）
■ 四、宫廷权谋类（朝服／官服／后宫装）
■ 五、民国风情类（旗袍／中山装／军装）
■ 六、现代都市类（职场／休闲／夜店装）
■ 七、科幻赛博类（机械铠／光甲／霓虹衣）
```

---

## 五、与造型大师6维参数对应关系

```
造型大师6维参数 → 服装库映射
━━━━━━━━━━━━━━━━━━━━━
③ 服饰结构   → 选择款式编号（1.1-1.8）+ 配套配饰
④ 配色方案   → 款式内配色 + 通用池气质色调整
⑤ 材质渲染   → 款式内材质 + 灯光联动矩阵（直接指导灯光大师）
⑥ 气质人设   → 通用池气质关键词 + 款式身份标签
```

> **完整调用链**：造型大师选款 → 6维参数化 → 服装库输出提示词 → 灯光大师联动矩阵自动匹配灯光方案
