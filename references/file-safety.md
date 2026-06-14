# 大型技能文件安全操作规范

> 本文件记录在维护短剧大师技能（2800+行）过程中发现的文件操作陷阱和恢复方法。
> 每日 cron 自愈任务在操作 SKILL.md 时必须遵守这些规范。

## 陷阱 1：read_file 默认截断导致写回损坏

**症状**：`read_file` 默认 `limit=500`。如果用 `read_file` 读取全文 → 得到 500 行截断 → `write_file` 或 `patch` 写回 → 文件从 2800 行变为 500 行。

**正确做法**：
- 大文件（>500行）必须用 `offset` + `limit` 分页读取，或用 `terminal: wc -l` 先确定总行数
- 编辑大文件用 `patch` 工具（工具内自己处理完整文件），不用 `write_file`
- `write_file` 永远是覆盖写入，不是追加。大文件用 `write_file` 极其危险

## 陷阱 2：terminal heredoc 追加静默失败

**症状**：`cat >> file << 'EOF' ... EOF` 在某些环境下静默失败，输出不附加到文件。

**正确做法**：用 `patch` 匹配文件中最后一行做追加，不要用 shell heredoc。

## 恢复方法：Git 恢复

```bash
cd ~/.hermes/skills/短剧大师
git checkout HEAD -- SKILL.md        # 恢复到最近提交
git show HEAD:SKILL.md | wc -l        # 验证行数
```

## 恢复方法：备份恢复

```bash
cp SKILL.md.original SKILL.md         # 从备份恢复（如果有）
```

## Git credential 提取（macOS）

```bash
# 从系统 credential helper 提取 token
TOKEN=*** 'url=https://github.com' | git credential fill 2>/dev/null | grep '^password=' | cut -d= -f2)
```

不要在 shell 单行中用 `$(...)` 嵌套这个命令——会有语法冲突。分两步：先写到临时文件，再 source。

## 记忆管理

- 记忆容量限制 2,200 字符
- 替换旧入条用 `memory action=replace old_text="匹配子串"`
- old_text 只需要匹配旧入条的足够唯一片段，不需要完全一致
- 旧入条删除后空间释放，新入条可以立即写入
