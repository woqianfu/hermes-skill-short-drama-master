# PPT/PDF 生成指南 — 竖版暗色影视风 / Vertical Dark Cinematic PPT Guide

> 短剧大师™ 的 PPT/PDF 输出规范。所有设计规则来自 v6.1 多轮迭代验证。
> 目标：390×844px（iPhone 14 比例），手机端阅读舒适，不撑出格，不截断。

## 生成命令 / Generation Command

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-sandbox \
  --print-to-pdf="输出路径.pdf" --no-pdf-header-footer \
  "file://HTML路径.html"
```

## @page CSS（必须内嵌） / Required @page CSS

```css
@page { size: 390px 844px; margin: 0; }
@page { bleed: 0; marks: none; }
@media print {
  body { background: #050508 !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .slide { break-after: page; break-inside: avoid; page-break-inside: avoid;
           margin: 0 !important; border-radius: 0 !important;
           width: 390px !important;
           height: 844px !important;
           min-height: 844px !important;
           max-height: 844px !important;
           overflow: hidden !important; }
  .slide:last-child { break-after: auto; }
}
```

## 字体大小规范 / Font Size Specs

| 元素 | 字号 | 说明 |
|------|:--:|------|
| 封面标题 h1 | 2.4rem | 手机一屏可见，不被裁 |
| 章节标题 h2 | 1.4rem | 金色粗体 |
| 副标题 .en-sub | 0.7rem | 灰色英文 |
| 大师卡片名 .name | 0.88rem | 金色粗体 |
| 大师技能 .skill | 0.66rem | 正文白色 |
| 表格 .table | 0.64rem | 四列以内 |
| highlight 框 | 0.78rem | 左侧金色竖线 |
| 统计数字 .num | 1.4rem | 卡片内数字 |
| 页脚 .footer-bar | 0.45rem | 透明度 0.13，不可喧宾夺主 |
| 流程图 .flow | 0.64rem | 暗底卡片 |

## 核心设计规则 / Core Design Rules

### 1. 防溢出三件套 / Overflow Prevention Triad
- 每页 `.slide` 严格 `height: 844px; max-height: 844px; overflow: hidden`
- 内容多的页面（如品控/技术军团6卡页）→ 去掉英文行，只保留中文
- 大师卡片 padding 压缩到 `5px 8px`，margin `1px 0`

### 2. 页脚处理 / Footer Rules
- 页脚用 `position:absolute; bottom:6px`，贴页面最底部
- 字体 `0.45rem`，颜色 `rgba(255,255,255,0.13)` — 可见但不抢眼
- **CSS 规则容易丢失**：每次改动后检查 `.footer-bar` 是否仍存在于 `<style>` 中
- 内容区用 `flex-direction:column; justify-content:center` 居中

### 3. 竖向排版 / Vertical Layout
- 所有流程图（flow block）用竖向 `↓` 箭头式，不用横向 ASCII 树
- 横向文字容易撑出滚动条 → 每项独立一行，加 `<br>` 换行
- 双卡片用 `display:flex; gap:8px` 左右分栏

### 4. 颜色体系 / Color System
- 背景：`#050508` 纯黑 → `#0a0a12` → `#0d0d18`（渐变）
- 金色：`#D4A843`（主）/ `#F0C060`（亮）
- 卡片背景：`#111118`
- 边框：`#1a1a28`（暗）或去掉全部边框（更干净）
- 页面上方不要金色装饰线（`.slide::before` / `::after`）
- 封面亮点用圆角标签（`border-radius:14px`），金/紫/青/绿四色

### 5. 双语规则 / Bilingual Rules
- 每页标题和关键术语中英并列
- 但内容过多时优先保留中文，砍英文
- 英文用 `.en` class，字号比正文小 0.1-0.15rem

### 6. 数据卡片 / Stat Cards
- 数字 `1.4rem`，不超 `1.5rem`（否则溢出）
- padding `14px 6px`，gap `8px`
- 每行 4 个卡片，`min-width:70px`
- 短数字优先（"15%" 而不是 "60→15%"）

## 常见陷阱 / Common Pitfalls

| 陷阱 | 症状 | 修复 |
|------|------|------|
| CSS 规则丢失 | 页脚突然变大、排版错乱 | 全文搜索 `.footer-bar`，补回规则 |
| 内容溢出空白页 | PDF 多出只有页脚的残页 | 检查该页高度，砍英文行/减padding/降字号 |
| 横向滚动条 | flow 块出现左右滑道 | ASCII 树 → 竖向箭头式 |
| 标题被裁 | 手机上看不到完整标题 | h1 降到 2.4rem，加 `margin-top:-10px` |
| 数字撑出卡片 | 4 字以上数字溢出 | 缩短标签，数字不大于 1.5rem |
| Chrome PDF 色差 | 暗色变灰 | `-webkit-print-color-adjust: exact` |

## 迭代流程 / Iteration Workflow

1. 修改 HTML → 
2. Chrome headless 生成 PDF → 
3. `cp` 到桌面 + `assets/` → 
4. `git commit`（中英双语）→ 
5. `git push` 双仓库 →
6. 用户看桌面 PDF，反馈问题 → 回到 1

每次改进后必做：检查之前修好的问题是否被新改动覆盖（尤其是页脚 CSS 和断页规则）。

> v6.1 验证通过 · 10页竖版暗色影视风 · 中英双语
