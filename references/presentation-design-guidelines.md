# PPT/PDF设计规范 — 短剧大师™ Presentation Guidelines

> 基于 v6.2.4 实战验证。竖版暗色影视风 · 中英双语 · 手机兼容。
>
> ⚠️ **硬性死规则**：纯黑底+纯金字+无边框+无伪元素。任何偏离都会在手机PDF上出问题。

## 尺寸规范

| 参数 | 值 | 说明 |
|------|-----|------|
| 宽度 | 390px | iPhone 14 竖屏宽度 |
| 高度 | 844px | iPhone 14 竖屏高度 |
| @page CSS | `size: 390px 844px; margin: 0` | 嵌入HTML确保Chrome无头渲染精确尺寸 |
| 打印色彩 | `print-color-adjust: exact` | 暗色背景在PDF中保留 |

## 风格规范（最终锁定）

| 要素 | 值 | 说明 |
|------|-----|------|
| 底色 | `#0a0a12`（纯色） | ❌ 禁用渐变——PDF在40%处有色阶横纹 |
| 主金色 | `color: var(--warm-gold)` 或 `#D4A843`（纯色CSS） | ❌ 禁用 `-webkit-background-clip:text`——手机PDF变黑块 |
| 卡片背景 | `#111118` 或 `#1a1a22` | |
| 边框 | **无** `border: none` | ❌ 禁用 `border: 1px solid`——PDF渲染为可见线条 |
| 装饰线 | **无** | ❌ 禁用 `::before` / `::after` 伪元素——产生不可控横线 |
| 字体 | PingFang SC / system-ui | 中文苹方+英文默认系统字体 |
| 每页断页 | `.slide { break-after: page; break-inside: avoid; height:844px!important; overflow:hidden!important; }` | |

## 字体比例铁律

| 元素 | 字号 | 说明 |
|------|------|------|
| 封面标题 | 2.2-2.4rem | 纯金色，无渐变 |
| 页面标题 h2 | 1.35rem | |
| 大师名称 | 0.88rem | 加粗+暖金 |
| 技能描述 | 0.7rem | 正文主色 |
| 统计数字 | 1.3-1.5rem | 卡片内大数字 |
| 表格正文 | 0.64rem | |
| 高亮引用 | 0.78rem | |
| 页脚 | 0.45rem | rgba(255,255,255,0.13) |

## PDF生成流水线

```bash
# Chrome无头渲染
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-sandbox \
  --print-to-pdf="输出路径.pdf" \
  --no-pdf-header-footer \
  "file://HTML文件路径"

# 验证
ls -lh 输出路径.pdf  # 预期 1-2MB
```

## 内容排版规则

| 规则 | 说明 |
|------|------|
| 每页大师数量 | 研究军团1页(1人+6团队) / 创作军团≤5 / 品控军团≤6 / 技术军团≤9（拆页） |
| 封面 | 21大师四军团+进化总督察 + 研究军团+进化KPI标签 |
| 研究军团 | 单独一页：案例大师率6将，标注6平台含红果 |
| 会审 | 二十一位大师会审 |
| 自进化 | 02:30触发 + 03:00进化大师KPI审核 |
| 双排标签 | 封面和数据卡片两排显示，覆盖全部亮点 |
| 数据卡片 | 4-5个深色圆角卡，大数字+小标签 |

## 已验证页面结构（11页）

```
P1  封面 — 短剧大师™ vX.Y.Z + 21大师四军团 + 标签云 + 数据卡
P2  数据总览 — 双排统计
P3  研究军团(案例大师团队7人) — 含6平台扫描(红果)
P4  创作军团 ②-⑥
P5  品控军团 ⑦-⑫
P6  技术军团 ⑬-⑳（灯光→省钱）
P7  技术军团续 + 进化大师 #21
P8  会审系统（二十一位大师）— 竖向流程图
P9  引擎+进化（含KPI仪表盘）
P10 附录
P11 版本历程+结尾
```

## 硬性死规则（实战教训）

| # | 规则 | 后果（真实发生过） |
|:-:|------|-------------------|
| 1 | slide必须 `border:none`，不能有任何边框 | PDF页面边缘留白线 |
| 2 | 必须去掉 `::before` 伪元素金线 | Chrome渲染为黄线→用户反复投诉 |
| 3 | 背景必须纯色 `#0a0a12`，禁用渐变 | PDF在40%处产生色阶横纹 |
| 4 | 金色文字必须 `color: var(--warm-gold)` 纯色CSS | 用`-webkit-background-clip:text`→手机PDF文字变黑块 |
| 5 | 每页 `height:844px; overflow:hidden` | 内容溢出产生空白残页（如"2: Data"残页） |
| 6 | flow必须竖排（`<br>`换行，`↓`箭头），禁用ASCII树 | 横向排版撑出页面 |
| 7 | 每次改完HTML必须跑Chrome headless→PDF | 不改PDF等于白改 |
| 8 | 版本号全域同步（README/SKILL/references/VERSION） | 各说各话→混乱 |
| 9 | card内flex项必须 `flex:1; min-width:0` | 长英文撑出卡片→溢出 |
| 10 | 页脚`position:absolute; bottom:6px`确保到底 | 不设absolute→跟着内容跑 |
| 11 | 封面标题做防溢出测试（手机PDF预览） | 标题被裁=投诉 |
| 12 | 数据卡`gap`必须>8px | 窄间距小屏糊在一起 |

## P1 防溢出策略（按优先级）

1. 删英文行（最有效的压缩）
2. 减 padding（`9px→7px→5px`）
3. 减字号（`0.66rem→0.62rem`）
4. 合并流（两flow合一）
5. 缩间距（`margin 8px→4px→2px`）

**铁律**：先删内容，再调CSS。调padding比调font-size效果好。

## 常见问题速查

| 问题 | 原因 | 修复 |
|------|------|------|
| 空白残页 | 内容溢出844px | 压缩或删英文 |
| 标题上方有横线 | `::before`伪元素或渐变背景 | 删除伪元素 + 纯色背景 |
| 标题变黑块(手机PDF) | `-webkit-background-clip:text` | 用`color: var(--warm-gold)`纯色代替 |
| 多出残页（"2: Data"） | 前一页`</div>`未闭合 | 检查DOM |
| PDF只有1页 | 某页`</div>`未闭合 | 检查HTML完整性 |
| 颜色发白 | `print-color-adjust`未设 | 加`-webkit-print-color-adjust: exact` |
| 标题被裁(手机) | 字号太大或padding太小 | 减到2.2-2.4rem + 紧缩上方间距 |

## 每次推送必须同步

1. HTML展示文件（`assets/短剧大师vX.Y.Z_完整功能介绍.html`）
2. PDF展示文件（Chrome headless渲染）
3. 版本号必须与VERSION/README/SKILL一致
4. 新大师/新平台/新亮点必须体现在展示页中

── 短剧大师™ · 微短剧全流程一体化创作技能 · DCI:RDCS00ANT.202606159652337429 ──