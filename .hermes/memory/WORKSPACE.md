# WORKSPACE.md — 短剧大师™ 项目工作区记忆

> Layer ③ 项目隔离记忆（Hermes 三层记忆架构）
> 首次创建: 2026-06-18
> 项目根: ~/.hermes/skills/短剧大师/

## 项目概况
AI 微短剧全流程一体化创作平台（19大师 + 会审 + 自适应进化），
Slogan: "从一句话到 AI 微短剧成片"。

当前版本: v6.2.4
DCI 登记: RDCS00ANT.202606159652337429

## 进度追踪
- **2026-06-17**: 新增造型大师 #22，修复附录H缺失
- **2026-06-17**: 完成发配边关竞品调研 + 角色知识库
- **2026-06-17**: 完成三层记忆架构融合设计

## 技术决策
- 版本号以 Pypi 发布版（~/.hermes/skills/短剧大师/SKILL.md）为准
- 视觉模型优先 Kimi，禁用 Gemini（KIMI_API_KEY 已配，GEMINI 为占位符）
- BX Protocol 调度 + 省 ~75% token + Mini 单秒 ¥0.16

## 已知问题
- SKILL.md 附录格式已统一为 `# 附录 X：标题`
- masters-self-evolution.md 22大师矩阵已补全

## 待办
- 排查 WeChat 心跳 cron（d6f6c7fc1312）报错
- 排查凌晨 gateway 重启 cron（7971424246ea）报错
- 清理 .env 中重复的 KIMI_CN_API_KEY 注释行
