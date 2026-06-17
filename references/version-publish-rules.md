# 短剧大师版本发布规则 — 硬性规范

## 每次推送前必须更新的文件

| 文件 | 更新内容 | 必做？ |
|------|----------|--------|
| `VERSION` | 写入最新版本号（如 `v6.2.5`） | ✅ |
| `SKILL.md` | frontmatter `description` 版本号 + 亮点同步 | ✅ |
| `README.md` | 标题版本号 + 所有 badges 同步 | ✅ |
| `assets/短剧大师vX.Y.Z_完整功能介绍.html` | 新建文件，所有页面内容同步 | ✅ |
| `assets/短剧大师vX.Y.Z_完整功能介绍.pdf` | 新建文件，与 HTML 同步生成 | ✅ |

## 步骤

```bash
# 1. 更新 VERSION
echo "v6.2.5" > VERSION

# 2. 更新 SKILL.md frontmatter
#    打开 SKILL.md 第1-3行，改 version + description

# 3. 更新 README.md
#    改标题版本号 + 所有 shields.io badges

# 4. 生成 HTML + PDF
#    cp assets/短剧大师v6.2.4_完整功能介绍.html assets/短剧大师v6.2.5_完整功能介绍.html
#    然后修改内容 + 生成 PDF

# 5. git add -A && git commit -m "v6.2.5: ..."
# 6. git push origin main && git push duanju main
```

## 不更新的后果

- 版本号不一致 → Agent 混淆
- README badges 过时 → 对外展示错误
- 展示文件无新功能 → 用户/客户看不到最新能力
- **不可接受。每次推送都必须执行上述流程。**
