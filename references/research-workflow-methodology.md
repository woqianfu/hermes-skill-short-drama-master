# 研究军团·外部内容提取与吸收工作流

> 方法论文档
> 适用：研究军团（案例大师团队）
> 更新：2026-06-18

---

## 一、工作流概览

```
外部URL/文章 → 提取 → 分析 → 结构化入库 → 大师联动 → 应用
```

## 二、各环节标准操作

### 1. 提取（web_extract / browser）

| 来源类型 | 工具 | 备注 |
|---------|------|------|
| 公众号文章（内容文本可读） | `web_extract(urls=[...])` | 首选，最快 |
| 公众号文章（含图片/付费墙） | `browser_navigate` + `browser_scroll` + `browser_vision` | 截图分析，注意图片加载 |
| 公开网页/文档 | `web_extract` | 直接提取markdown |
| PDF/研究报告 | `web_extract`对PDF链接 | 自动转markdown |

### 2. 分析（提取关键信息）

从文章中提取以下四类信息：

| 类别 | 提取内容 | 入库目标 |
|------|---------|---------|
| **方法论** | 怎么做、为什么这么做 | 对应大师的提示词模板/方案库 |
| **数据/案例** | 播放量、热度、爆款名场面 | case study参考 |
| **趋势判断** | 行业方向、平台政策变化 | 战略决策参考 |
| **技术要点** | 提示词写法、工具用法、参数设置 | 肌肉大师/质检大师等 |

### 3. 结构化入库

每篇文章保存为 `references/<topic>.md`，统一格式：

```markdown
# 标题 — 一句话定位

> 来源：公众号/网站 日期
> 入库时间：
> 关联大师：

---

## 一、核心数据（如有）

| 指标 | 数据 |

## 二、关键方法论

## 三、对短剧大师的启示

## 四、与已有能力的联动

---

*参考来源：*
*入库：*
*短剧大师™ · DCI:...*
```

### 4. 大师联动

入库时必须明确标注**关联大师**，让后续调用直接能找到：

| 文章主题 | 关联大师 |
|---------|---------|
| 微表情控制/眼神/呼吸 | 肌肉大师 |
| 爆款剧分析/名场面拆解 | 剧本大师 |
| 60s节奏/钩子设计 | 节奏大师 |
| 行业报告/平台政策 | 研究军团（案例大师） |
| IP长线运营 | 进化大师 |

### 5. 入库后的引用

在对应大师的方案库中加一行注释指向参考文件：
```
# 参考：references/ai-micro-expression-methodology.md（30+组微表情提示词）
```

---

## 三、付费墙/受限内容处理

1. 优先尝试 `web_extract` → 部分公众号可直接提取
2. 失败后改用 `browser_navigate` + `browser_snapshot` + `browser_scroll`
3. 仍有图片遮挡 → `browser_vision(question="...")` 截图分析
4. 付费内容（知识星球/小报童等）→ 告知用户无法获取，建议关注原作者
5. 找替代资源：用同一关键词 `web_search` 找同主题公开文章

---

## 四、常见陷阱

- ❌ 公众号图片懒加载：需 scroll 到底才能触发加载
- ❌ browser_snapshot 看不到图片文字：改用 browser_vision
- ❌ 同一篇文章多个URL（已读/转载）：检查标题去重
- ✅ 文章中有多张截图时接力分析：vision_analyze 每张图单独问
- ✅ 长文章可分多次 extraction，每次 offset+limit

---

## 五、本技能已入库参考文件清单

| # | 文件 | 主题 | 入库日期 |
|:-:|------|------|---------|
| 1 | references/case-master-team-workflow.md | 研究军团工作流程 | 之前 |
| 2 | references/fa-pei-bian-guan-case-study.md | 发配边关案例（旧版） | 之前 |
| 3 | references/60s-short-episode-structure-template.md | 60秒短集结构模板 | 06-18 |
| 4 | references/fa-pei-bian-guan-explosive-analysis.md | 发配边关22亿爆火复盘 | 06-18 |
| 5 | references/ai-micro-expression-methodology.md | 30+组微表情提示词库 | 06-18 |
| 6 | references/jubao-xianpen-4-analysis.md | 聚宝仙盆4长线IP范式 | 06-18 |
| 7 | references/百度AI漫剧布局与政策研究报告.pdf | 百度AI漫剧行业报告 | 06-18 |
| 8 | references/research-workflow-methodology.md | 本文·研究军团队工作流 | 06-18 |
| 9 | references/evolution-master-kpi.md | 进化大师KPI体系 | 之前 |

---

*短剧大师™ · DCI:RDCS00ANT.202606159652337429*
