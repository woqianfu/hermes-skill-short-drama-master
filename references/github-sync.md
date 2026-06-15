# GitHub Dual-Repo Sync & Git Recovery

## Repositories
- **Primary**: `git@github.com:woqianfu/hermes-skill-short-drama-master.git`
- **Mirror**: `git@github.com:woqianfu/duanju-master.git`

## SSH Sync Script
`~/.hermes/scripts/sync-skill-to-github.sh`:
```bash
#!/bin/bash
cd "$HOME/.hermes/skills/短剧大师" || exit 1
git add SKILL.md README.md 2>/dev/null
git commit -m "auto-sync $(date '+%Y-%m-%d %H:%M')" 2>/dev/null || true
git push origin main 2>&1
git push duanju main 2>&1
```

## Git Recovery from File Truncation
When SKILL.md is truncated by a bad `write_file` (e.g. 2375→112 lines):
```bash
cd ~/.hermes/skills/短剧大师
git log --oneline -3                    # Check commits
git show HEAD:SKILL.md | wc -l          # Verify full version in git
git checkout HEAD -- SKILL.md           # Restore
```
**Rule**: `git add SKILL.md && git commit` after every successful edit round.

## PptxGenJS PPT Creation
Install: `npm install -g pptxgenjs`
Run with: `NODE_PATH=$(npm root -g) node script.js`
Output: `assets/短剧大师v5.9_完整功能介绍.pdf`