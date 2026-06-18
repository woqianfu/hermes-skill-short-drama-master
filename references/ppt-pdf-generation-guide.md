# 短剧大师™ PPT/PDF 生成规范 v1.0

> 基于 v6.2.4 实战验证的完整工作流。从 HTML 设计到 PDF 输出，避开所有已知坑。

## 一、HTML 基础结构

### 尺寸
- 竖屏 390×844px（iPhone 14 比例）
- 每页一个 `.slide` div，`break-after: page`

### 背景
- **必须用纯色** `#0a0a12`，禁止渐变——PDF 渲染会在 40% 处产生横纹
- **禁止** `::before` / `::after` 伪元素——会在 PDF 中产生不可控的横线
- **禁止** `border` 在 `.slide` 上——PDF 渲染为可见线条

### 字体/文本渲染
- **禁止 `-webkit-background-clip:text`** — 手机 PDF 阅读器不兼容，文字变黑块。用 `color: var(--warm-gold)` 纯色代替
- **禁止 `-webkit-text-fill-color: transparent`** — 同上，导致文字透明→黑块
- 标题用纯金 `#D4A843` 或 `color: var(--warm-gold)`，不要用渐变
```css
.footer-bar {
  position: absolute; bottom: 6px; left: 50%;
  transform: translateX(-50%);
  font-size: 0.45rem;
  color: rgba(255,255,255,0.13);
  letter-spacing: 1px; white-space: nowrap;
}
```
- 字体不宜过小（< 0.3rem 手机上看不见），不宜过大（喧宾夺主）
- 透明度 0.10-0.15 区间，融入背景但不消失

## 二、PDF 生成命令

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-sandbox \
  --print-to-pdf="输出路径.pdf" \
  --no-pdf-header-footer \
  "file://绝对路径.html"
```

### @page 必须嵌入
```css
@page { size: 390px 844px; margin: 0; }
```

### 防溢出三件套
```css
@media print {
  .slide {
    break-after: page;
    break-inside: avoid;
    height: 844px !important;
    max-height: 844px !important;
    overflow: hidden !important;
  }
  .slide:last-child { break-after: auto; }
}
```

## 三、防溢出策略（按优先级）

1. **删英文行** — P4/P5 这类密集大师卡片页，英文 skill-en 行是最大溢出源，直接删掉
2. **减 padding** — `.master-detail` padding 从 9px→7px→5px 逐级压缩
3. **减字号** — skill 从 0.66rem→0.62rem 缩 5%
4. **合并流** — 两个 `.flow` 合并为一个，去 `↓` 箭头冗余
5. **缩间距** — margin 从 8px→4px→2px

**铁律**：先删内容，再调 CSS。调 padding 比调 font-size 效果好。

## 四、常见问题速查

| 问题 | 原因 | 修复 |
|------|------|------|
| 空白残页（只有页脚） | 内容溢出 844px | 压缩内容或删英文行 |
| 标题上方有横线 | `::before` 伪元素或渐变背景 | 删除伪元素 + 纯色背景 |
| 标题文字出现黑块（手机PDF） | `-webkit-background-clip:text` / `-webkit-text-fill-color:transparent` | 用 `color: var(--warm-gold)` 纯色代替渐变裁切 |
| 多出一页显示残码（如"2: Data"） | 前一页 `</div>` 未闭合或悬浮在页面之间 | 检查 DOM 结构，确保每页 slide 内的 div 成对闭合 |
| PDF 颜色发白 | `print-color-adjust` 未设 | 加 `-webkit-print-color-adjust: exact` |
| 内容横向撑出 | `flow` 中 ASCII 树横排 | 改为竖排 `↓` 箭头式 |
| 标签文字撑出卡片 | `min-width` 不够 | 缩短文字或加大 `min-width` |
| PDF 只有 1 页 | 某页 `</div>` 未闭合 | 检查 HTML 结构完整性 |

## 五、设计原则

- **竖向优于横向**：流程图用 `↓` 箭头竖排，不用 `├─` ASCII 树
- **简洁优于花哨**：一个 `.flow` 框 + 一个 `.highlight` 框 > 四个 step-card
- **融合优于凸显**：页脚、分隔线融入背景，不抢主内容
- **纯色优于渐变**：PDF 不支持 CSS 渐变抗锯齿
- **内容充满页面**：上下分布均匀，不留大片空白

## 六、版权信息原则

- DCI 编号只在页脚和 README badge 栏出现
- 不设独立版权页
- 不写「侵权警告」类措辞
- 暗纹追踪保留但对外不张扬
