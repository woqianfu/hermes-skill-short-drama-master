# GitHub Dual-Repo Sync & Git Recovery

## Repositories
- **origin**: `git@github.com:woqianfu/hermes-skill-short-drama-master.git`
- **duanju**: `git@github.com:woqianfu/duanju-master.git`

## Skill Directory
`~/.qclaw-hermes/skills/短剧大师/` — this IS the git repo (not a separate clone). Single source of truth.

## Dual-Push Command
```bash
cd ~/.qclaw-hermes/skills/短剧大师
git push origin main && git push duanju main
```

## Version Bump Checklist (EVERY update must follow)
1. Update version in ALL files (SKILL.md, README.md, references/*.md) — zero tolerance for version mismatch
2. Add entry to `references/changelog.md`
3. Commit message MUST include provenance mark: `DCI:RDCS00ANT.202606159652337429`
4. Dual-push both remotes
5. Historical version references in changelog and file names stay unchanged

## Pitfalls
- **Symlinks vs copies**: Do NOT use symlinks for the skill directory. Copy actual files. Symlinks break skill loading across restarts.
- **Cron workdir**: Must point to `~/.qclaw-hermes/skills/短剧大师/`, NOT `~/.hermes/skills/短剧大师/`
- **git proxy**: Requires `git config --global http.proxy http://127.0.0.1:7897` and `https.proxy` same port
- **git pull divergence**: If local diverges from remote (force push), use `git fetch origin && git reset --hard origin/main`
- **__pycache__ and node_modules**: Must be in `.gitignore` — never commit these
- **Chinese filenames in curl**: Use `--output` with local name instead of relying on URL-encoded paths

## Git Recovery from File Truncation
When SKILL.md is truncated by a bad `write_file`:
```bash
cd ~/.qclaw-hermes/skills/短剧大师
git log --oneline -3
git show HEAD:SKILL.md | wc -l
git checkout HEAD -- SKILL.md
```
**Rule**: `git add SKILL.md && git commit` after every successful edit round.

## PptxGenJS PPT Creation
Install: `cd scripts && npm install pptxgenjs`
Run with: `node scripts/create-presentation.js`
Output: `assets/短剧大师v6.2_完整功能介绍.pdf`

## Midnight Self-Evolution Cron
Job ID: `698a49b1e1a1` · Schedule: `0 0 * * *` · Workdir: `~/.qclaw-hermes/skills/短剧大师/`
If cron needs rebuilding, use `cronjob action=create` with skills=["短剧大师"] and enabled_toolsets=["web","terminal","file","skills"]
