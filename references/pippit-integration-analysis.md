# pippit-tool-cli × 短剧大师™ 对接分析 (v6.2.4)

> 2026-06-17 分析。pippit-tool-cli 是小云雀的 Go CLI 封装，安装方式：`npx @pippit-dev/cli@latest install`

## CLI 命令总览

| 命令 | 功能 | 短剧大师对接优先级 |
|------|------|:---:|
| `generate-video` | 文生视频（--prompt/--model/--ratio/--resolution/--duration/--image/--audio） | **P0** |
| `short-drama submit-run` | 短剧工作流提交（基础版，不如短剧大师完整） | 不接 |
| `short-drama upload-file` | 上传参考文件 | **P2** |
| `query-result` | 查询生成结果并下载 | **P1** |
| `download-result` | 多线程并行下载 | **P1** |
| `get-thread` | 查询会话详情 | **P3** |
| `list-thread-file` | 列出会话文件清单 | **P3** |

## P0: 交付大师改用 `generate-video`

最直接的对接点。交付大师当前的提交流程改为调用 CLI：

```bash
pippit-tool-cli generate-video \
  --prompt "$五段式prompt" \
  --model seedance2.0_direct \
  --ratio 9:16 \
  --resolution 720p \
  --duration "$镜长秒数" \
  --image "$角色图路径" \
  --audio "$BGM路径"
```

短剧大师输出 → CLI 参数对照：
- 五段式公式 → `--prompt`
- 竖屏7:16 → `--ratio 9:16`
- 720P量/1080P质 → `--resolution 720p`
- 镜长（2-5s/镜） → `--duration`
- BX Protocol 降废片后 → 直接提交，不再手动调API
- 角色参考图（肌肉大师输出） → `--image`（最多9张）
- BGM参考（配乐大师输出） → `--audio`（最多3个）

## P1: 下载管道

```bash
# 轮询结果
pippit-tool-cli query-result --run-id "$run_id" --thread-id "$thread_id" --download-dir "./output/"

# 或直接下载已知URL
pippit-tool-cli download-result --url "$url" --output-path "./output/E01_scene1.mp4" --workers 5
```

## 已有的捆绑技能（不接）

pippit 自带 `xyq-short-drama-skill` 和 `xyq-nest-skill`，都是基础版小云雀 skill。
短剧大师™ 的21大师体系 + 14道SQI + 875条案例库是完全超集，不需要降级使用。

## CLI 路径

```bash
# 安装后全局路径
$(npm root -g)/@pippit-dev/cli/

# 捆绑技能路径
$(npm root -g)/@pippit-dev/cli/skills/short-drama/SKILL.md
$(npm root -g)/@pippit-dev/cli/skills/xyq-nest-skill/SKILL.md
```
