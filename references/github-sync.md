# 短剧大师 GitHub 发布与同步机制

## 仓库信息
- **URL**: https://github.com/woqianfu/hermes-skill-short-drama-master
- **本地路径**: ~/.hermes/skills/短剧大师/
- **同步脚本**: ~/.hermes/scripts/sync-skill-to-github.sh

## 同步脚本内容
```bash
#!/bin/bash
SKILL_DIR="$HOME/.hermes/skills/短剧大师"
cd "$SKILL_DIR" || exit 1

# Init git if needed
[ ! -d .git ] && git init && git add SKILL.md && git commit -m "init"

# Get token from credential helper
TOKEN=*** 'url=https://github.com' | git credential fill 2>/dev/null | grep '^password=' | cut -d= -f2)
[ -z "$TOKEN" ] && exit 1

# Push
git remote remove origin 2>/dev/null
git remote add origin "https://woqianfu:${TOKEN}@github.com/woqianfu/hermes-skill-short-drama-master.git"
git add SKILL.md
git commit -m "auto-sync $(date '+%Y-%m-%d %H:%M')" || true
git push -u origin main 2>&1
```

## 恢复机制
如果文件被意外截断/损坏：
```bash
cd ~/.hermes/skills/短剧大师
git checkout HEAD -- SKILL.md  # 恢复到最后一次提交的版本
```
前提：.git 目录存在且有过成功 commit。

## Cron 任务
job_id=5e499f7b6ce1，每天 0:00 执行：
1. 全网搜索最新 AI 视频技巧
2. 逻辑自洽检查（8 类交叉引用）
3. 发现新内容→最小化 patch
4. 有修改→自动执行 sync-skill-to-github.sh 推送

## 注意事项
- git credential helper 需要有有效的 GitHub token
- 网络不通时 git push 会超时，不影响本地 commit
- SKILL.md 是大文件（~155KB），read_file 默认只读 500 行——操作前必须检查行数避免截断
