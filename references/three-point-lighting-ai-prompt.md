# 三光源布光法（Key/Fill/Backlight）— 灯光大师知识库

> 来源：Stage32/ZipX导演室实战经验（2026）
> 记录时间：2026-06-19

## 核心原理

AI视频生成中，对光照的描述若只有 "cinematic lighting, soft light, high contrast"，模型无法理解光源的精确位置和比例。**三光源布光法**给出了精确参数化提示词公式。

## 三光源公式

| 光源 | 作用 | 参数化提示词 | 色温参考 |
|------|------|-------------|---------|
| **Key Light（主光）** | 决定情绪基调 | `key light: 45-degree side top-down, hard source, 5600K` | 5600K(白)/3200K(暖) |
| **Fill Light（补光）** | 控制阴影对比度 | `fill light: 2:1 ratio, 3200K, bounced off white reflector from camera left` | 比主光暖1档 |
| **Backlight（背光）** | 勾画轮廓/空间感 | `backlight: rim light at 60-degree angle, 1-stop over key, tungsten 4200K` | 钨丝灯4200K |

## 精确 vs 模糊对比

| ❌ 模糊描述 | ✅ 精确参数化 |
|------------|-------------|
| `high-contrast noir` | `key at f/4, fill 2 stops under, no back light` |
| `cinematic lighting` | `key light: 45° top side, hard source; fill: 2:1 ratio bounced` |
| `soft light` | `diffused key light through 6x6 silk, 3/4 frontal` |

## 三光源在短剧大师的映射

| 附录/章节 | 现有内容 | 增强方向 |
|-----------|---------|---------|
| 附录O·13种光源词典 | 1-13种自然/人工光定义 | 新增三光源提示词公式模板 |
| SQ4.5·光影五基调 | 5种情绪基调 | 每基调指定三光源参数 |
| SQ8.3·维1肌肉键盘 | 面部肌肉精控 | 同理可推：光照参数化的「肌肉级精度」思维 |

## 推荐写入prompt的位置

在J.3五段式公式的「场景/光线」段中，替换单句描述为三光源公式：

```
【场景/光线】古井，灰蓝雾，暖金侧光45°
→ 改写为：
【场景/光线】古井，灰蓝雾，key:45°侧顶硬光5600K，fill:2:1暖补，back:60°勾边
```

## 注意事项

- 三光源公式只适用于你已经清晰设想了画面光效的场景
- 仍在探索阶段时，先用通用提示词跑几轮找感觉，再写入三光源公式锁死
- 两阶段工作流最有效：探索→锁死
