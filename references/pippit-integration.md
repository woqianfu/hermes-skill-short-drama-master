# pippit-tool-cli 集成手册 — 短剧大师™ 交付引擎

> 交付大师驾驶双引擎：传统小云雀API + pippit-tool-cli。后者为推荐引擎，统一替代4个Python脚本。

## 安装

```bash
npx @pippit-dev/cli@latest install
# CLI 路径: $(npm root -g)/@pippit-dev/cli/
# 命令: pippit-tool-cli
```

## 配置

```bash
export XYQ_ACCESS_KEY="ak-xxx"  # 从 https://xyq.jianying.com/home 创建
```

## 统一封装脚本

`scripts/pippit-engine.sh` 提供8个子命令：

| 子命令 | 功能 | 替代旧脚本 |
|--------|------|-----------|
| `generate` | 单镜头视频生成 | `submit_run.py` + `get_thread.py` + `download_results.py` |
| `upload` | 上传文件 | `upload_file.py` |
| `query` | 查询结果+自动下载 | `get_thread.py` + `download_results.py` |
| `download` | 并行下载（5线程） | `download_results.py` |
| `thread` | 会话详情 | `get_thread.py` |
| `files` | 文件列表 | `get_thread.py` 文件部分 |
| `repost` | 爆款复刻 | 案例大师→交付大师管线 |
| `short-drama` | 短剧工作流 | `submit_run.py` |

## 模型映射

| 短剧大师输出 | pippit 参数 |
|-------------|-------------|
| 五段式prompt | `--prompt` |
| 9:16竖屏 | `--ratio 9:16` |
| 720P/1080P | `--resolution` |
| 镜长X秒 | `--duration` |
| seedance2.0（默认） | `--model seedance2.0_direct` |
| seedance2.0快速 | `--model seedance2.0_fast_direct` |
| 角色参考图 | `--image`（最多9张） |
| BGM/音效 | `--audio`（最多3个） |
| 参考视频（爆款复刻） | `--video`（最多3个） |

VIP用户额外支持：`seedance2.0_vision`（视觉参考模型）

## 爆款复刻管线

```
案例大师找到爆款 → 下载参考视频 → 交付大师repost
```

```bash
bash scripts/pippit-engine.sh repost \
  --video "爆款.mp4" \
  --image "角色图.jpg" \
  --prompt "参考【@视频1】的运镜方式和创作手法，将主体更换为【@图片1】" \
  --ratio 9:16 --duration 5
```

prompt 中用 `@视频1` `@图片1` 引用上传的媒体素材。

## 小云雀Web产品手册吸收要点

来源：字节飞书 wiki（2026.6.4最新修改）

### 短剧Agent 2.0 三大亮点
1. **超强故事理解** — 剧本全自动解析、连贯生成
2. **全局角色/场景管理** — 角色不同时空妆造精准映射
3. **生产自动化** — Agent智能旁白改编、多画风支持、多剧集连发

### 短剧大师覆盖情况
- 21大师四军团 → 远超基础Agent
- 14道SQI关卡 → 原生Agent无质量门
- 875条案例+321剧本库 → 原生Agent无此资产
- BX Protocol降废片 60%→15% → 原生Agent无此机制

### 小云雀独有的补充能力
- 画质提升/字幕擦除（26.5.22上新）
- 故事板音效展示和引用（26.5.22上新）
- 沉浸式短片模式（独立快捷模式）
- 爆款复刻（通过 --video 传参考视频）
