# AI视频灯光+风格控制词典 — 附录O（增强版）

> 核心内容见SKILL.md正文 附录O（13种光源词典+5类电影风格+参数控制）
> 本文件为增强补充：三光源布光法（Three-Point Lighting）

## 三光源布光法（Key/Fill/Backlight）

> 来源：Stage32/ZipX导演室实战经验（2026）

### 三光源公式

| 光源 | 作用 | 参数化提示词 | 色温参考 |
|------|------|-------------|---------|
| **Key Light（主光）** | 决定情绪基调 | `key light: 45-degree side top-down, hard source, 5600K` | 5600K(白)/3200K(暖) |
| **Fill Light（补光）** | 控制阴影对比度 | `fill light: 2:1 ratio, 3200K, bounced off white reflector from camera left` | 比主光暖1档 |
| **Backlight（背光）** | 勾画轮廓/空间感 | `backlight: rim light at 60-degree angle, 1-stop over key, tungsten 4200K` | 钨丝灯4200K |

### 精确 vs 模糊对比

| ❌ 模糊描述 | ✅ 精确参数化 |
|------------|-------------|
| `high-contrast noir` | `key at f/4, fill 2 stops under, no back light` |
| `cinematic lighting` | `key light: 45° top side, hard source; fill: 2:1 ratio bounced` |
| `soft light` | `diffused key light through 6x6 silk, 3/4 frontal` |

### 在J.3五段式公式中的使用

```
【场景/光线】古井，灰蓝雾，暖金侧光45°
→ 改写为：
【场景/光线】古井，灰蓝雾，key:45°侧顶硬光5600K，fill:2:1暖补，back:60°勾边
```

### 注意事项
- 三光源公式只适用于已清晰设想画面光效的场景
- 探索阶段：先用通用提示词跑几轮找感觉 → 再写入三光源公式锁死
- 两阶段工作流：探索→锁死
