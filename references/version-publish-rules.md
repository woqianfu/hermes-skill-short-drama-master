# 短剧大师版本发布规则 — 硬性规范

> ⚠️ 用户明确要求写死此规则。每次推送前必须执行，少一步视为违规。
> ⚠️ **关键：只在用户说「双仓更新」时才能push。** 其他任何时候（包括本AI主动）不得推送到任何远程仓库。
> ⚠️ 双仓更新前必须做脱敏检查：`.gitignore` 已覆盖 `.env`/`__pycache__`/`*.log`/`session-*` 等。推送前先 `git status` 确认无敏感文件。
> 此规则由用户多次纠正后固化：**任何时候更新并向 GitHub 推送前必须执行本流程。**

## 版本号规则

格式 `vX.Y.Z`（如 `v6.2.4`）：

| 位置 | 说明 | 示例 |
|------|------|------|
| X | 大版本号（架构级变更时+1） | 6 |
| Y | 功能版本号（新增大师/军团时+1） | 2 |
| Z | 小版本号（每次提交+1） | 4 |

版本号记录在根目录 `VERSION` 文件（纯文本，仅版本号）。

## 推送前必更新清单

| # | 文件 | 更新内容 | 必做？ |
|:-:|------|----------|:-----:|
| 1 | `VERSION` | 写入最新版本号（如 `v6.2.5`） | ✅ |
| 2 | `SKILL.md` frontmatter | `description` 版本号 + 亮点同步 | ✅ |
| 3 | `README.md` | 标题版本号 + 所有 shields.io badges | ✅ |
| 4 | `assets/短剧大师vX.Y.Z_完整功能介绍.html` | 新建，内容同步最新功能 | ✅ |
| 5 | `assets/短剧大师vX.Y.Z_完整功能介绍.pdf` | 新建，与HTML同步生成 | ✅ |
| 6 | GitHub About 描述 | 双仓库（origin + duanju）同步更新 | ✅ |

## 双仓库同步规则

两处必须同步，不能只推一个：

```bash
git push origin main    # 主仓库：hermes-skill-short-drama-master
git push duanju main    # 镜像仓库：duanju-master
```

GitHub About 描述（仓库首页右侧简介）也必须同步更新两个仓库。
当前 token 无 repo 写入权限，需手动去 `github.com/woqianfu/<repo>` → 右侧 ✏️ 编辑。

## 脱敏规则

推送前检查以下内容已在 `.gitignore` 中排除或确认不包含私密数据：

- `.env` / `.env.local` — API Key 文件
- `*.log` — 日志文件
- `session-*` — 会话文件
- `personal-*` / `私人-*` / `我的-*` — 个人工作文件
- `__pycache__/` / `*.pyc` — 缓存文件
- `.DS_Store` — 系统文件
- `assets/short-writing/` — 如需脱敏，在 .gitignore 中取消注释

所有 API key 必须通过环境变量传递，不得在代码中硬编码。

## 推送触发规则

**本地只做 `git commit`，不主动 push。** 只有用户说「双仓更新」时才执行推送：

```bash
git add -A && git commit -m "vX.Y.Z: 中文描述 / English description"
git push origin main && git push duanju main
```

无用户指令不上传。commit message 格式：`vX.Y.Z: 中文要点 / English summary`

## 操作步骤

```bash
# 1. 更新 VERSION
echo "v6.2.5" > VERSION

# 2. 更新 SKILL.md frontmatter（版本号 + description 亮点）
# 3. 更新 README.md（标题版本号 + 所有 badges）
# 4. 复制 HTML + 更新内容
cp assets/短剧大师v6.2.4_完整功能介绍.html assets/短剧大师v6.2.5_完整功能介绍.html
# 修改 HTML 内容同步最新功能
# 5. 生成 PDF（Chrome 无头渲染）
# 6. 检查 .gitignore 脱敏

# 7. 本地提交
git add -A && git commit -m "v6.2.5: 功能描述 / English"

# 8. 等用户说「双仓更新」→ 推送
git push origin main && git push duanju main
# 9. 手动更新 GitHub About（两个仓库）
```

## 不执行的后果

- 版本号不一致 → Agent 混淆
- README badges 过时 → 对外展示错误
- 展示文件无新功能 → 客户/用户看不到最新能力
- **用户明确要求写死此规则。不可接受。**
