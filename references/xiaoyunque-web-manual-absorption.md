# 小云雀Web产品手册吸収报告 — 短剧大师™ 对接参考

> 来源: 字节跳动飞书文档 https://bytedance.larkoffice.com/wiki/PxZgwJwxti0dutk6WIdcwRA6nTd
> 版本: 2026.6.4 最新修改

## 一、小云雀Web端定位

| 维度 | 说明 |
|------|------|
| 定位 | 专业内容生产力平台（vs App端随手创作） |
| 三大优势 | 大屏操控、多任务并行、批量规模化出片 |
| 目标用户 | 持续产出内容的团队和创作者 |

## 二、短剧&漫剧Agent（核心）

搭载 **Seedance 2.0** 的行业首个短剧&漫剧Agent。

### 三大核心亮点

| # | 能力 | 短剧大师覆盖情况 |
|:--:|------|:----------------:|
| 1️⃣ | **超强故事理解** — 剧本全自动解析、连贯生成，只需输入剧本即可输出完整剧集 | ✅ 剧本大师+暗线大师+节奏大师远超此能力 |
| 2️⃣ | **全局角色/场景管理** — 全剧集角色场景一键直出，角色不同时空妆造精准映射 | ✅ 肌肉大师(六维精控)+构图大师覆盖，但平台级「一键直出」是补充能力 |
| 3️⃣ | **生产自动化** — Agent智能旁白改编、多画风支持、多剧集连发 | ✅ 交付大师+省钱大师覆盖 |

### 能力差距分析

短剧大师™ 在以下方面**远超**小云雀原生Agent：
- 21大师四军团 vs 基础Agent → 精度深度完全不是一个量级
- 14道SQI关卡 vs 无质量门 → 短剧大师确保输出质量
- 875条蒸馏案例+321剧本库 → 原生Agent无此资产
- BX Protocol降废片60%→15% → 原生Agent无此机制

**小云雀平台独有的补充能力**（值得吸收）：
- **Seedance 2.0 模型** — 视频生成引擎（`seedance2.0_direct`, `seedance2.0_fast_direct`, `seedance2.0_vision`, `seedance2.0_fast_vision`）
- **画质提升/字幕擦除** — 综合Agent和沉浸式短片支持（26.5.22上新）
- **故事版音效展示和引用** — Agent模式故事板编辑面板（26.5.22上新）
- **沉浸式短片** — 输入指令一键直出（独立于短剧Agent的快捷模式）
- **爆款复刻** — 复刻已有爆款视频

## 三、对接优化方案

交付大师的 pippit 对接应使用以下模型映射：

| 短剧大师输出 | pippit-tool-cli 参数 |
|-------------|---------------------|
| 五段式prompt | `--prompt` |
| 9:16竖屏 | `--ratio 9:16` |
| 720P/1080P | `--resolution` |
| 镜长秒数 | `--duration` |
| seedance2.0 Mini（默认） | `--model seedance2.0_mini` |
| seedance2.0 标准 | `--model seedance2.0_direct` |
| seedance2.0 快速 | `--model seedance2.0_fast_direct` |
| seedance2.0视觉参考 | `--model seedance2.0_vision` |
| 角色参考图 | `--image` |
| BGM/音效 | `--audio` |
| 视频参考 | `--video` |

> ✅ 已验证：普通用户也可使用 `seedance2.0_mini`（性价比最高，单秒¥0.16）
> VIP用户还可使用 `seedance2.0_vision` 和 `seedance2.0_fast_vision`（视觉参考模型）
