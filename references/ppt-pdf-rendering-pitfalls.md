# PDF/PPT 渲染坑点与修复 — Rendering Pitfalls

> 源自手机PDF阅读器兼容性问题排查。记录于v6.2迭代期间。

## 已知坑点

### 1. 渐变文字 → 黑块 ❌
- **症状**：`-webkit-background-clip: text` + `-webkit-text-fill-color: transparent` 
  在手机PDF阅读器上渲染为黑色方块
- **修复**：使用纯色 `color: var(--warm-gold)` 替代渐变文字
- **影响**：所有标题、高亮文字

### 2. 渐变背景 → 横纹 ❌
- **症状**：`background: linear-gradient(180deg, #0a0a12, #0d0d18 40%, #0a0a12)` 
  在PDF中产生可见的水平色阶跳变
- **修复**：使用纯色 `background: #0A0A12`
- **影响**：slide背景

### 3. `::before`/`::after` 伪元素 → 黄线 ❌
- **症状**：`.slide::before` 的金色渐变横线在手机上不美观
- **修复**：移除伪元素，使用纯CSS布局
- **影响**：slide顶部装饰线

### 4. `border: 1px solid var(--border)` → 可见边框 ❌
- **症状**：slide边框在手机上显示为可见线条
- **修复**：使用 `border: none` 或移除border属性
- **影响**：所有slide

## CSS检查清单（生成PDF前）

```css
/* ✅ 安全 */
color: var(--warm-gold);
background: #0A0A12;
border: none;

/* ❌ 不安全 — 会出问题 */
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background: linear-gradient(...);
border: 1px solid ...;
.box-shadow: ...;
```

## 渲染命令

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-sandbox \
  --print-to-pdf="/path/to/output.pdf" --no-pdf-header-footer \
  "file:///path/to/file.html"
```

注意：文件路径包含中文时，使用Python subprocess而非shell直接调用，避免引号嵌套问题。
