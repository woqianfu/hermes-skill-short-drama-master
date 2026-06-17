#!/bin/bash
# pippit-engine.sh — 短剧大师™ × pippit-tool-cli 统一交付引擎
# 统一替代 submit_run.py / get_thread.py / download_results.py / upload_file.py
set -euo pipefail
DEFAULT_MODEL="seedance2.0_mini"
DEFAULT_RATIO="9:16"
DEFAULT_RESOLUTION="720p"
DEFAULT_DURATION=5
DEFAULT_WORKERS=5

if [[ "${1:-help}" != "help" && "${1:-help}" != "--help" && "${1:-help}" != "-h" ]]; then
  if ! command -v pippit-tool-cli &>/dev/null; then
    echo "❌ 安装: npx @pippit-dev/cli@latest install"; exit 1
  fi
  if [[ -z "${XYQ_ACCESS_KEY:-}" ]]; then
    echo "❌ 请设置 XYQ_ACCESS_KEY"; exit 1
  fi
fi

show_help() { cat <<'EOF'
子命令:
  generate    生成单镜头视频（替代 submit_run+query+download）
  upload      上传文件（替代 upload_file.py）
  query       查询结果并下载（替代 get_thread+download_results）
  download    并行下载结果（替代 download_results.py）
  thread      查询会话（替代 get_thread.py）
  files       列出文件（替代 get_thread.py 文件部分）
  repost      爆款复刻（案例大师→交付大师管线）
  short-drama 短剧工作流
EOF
}

cmd_generate() {
  local p="" m="$DEFAULT_MODEL" r="$DEFAULT_RATIO" s="$DEFAULT_RESOLUTION" d="$DEFAULT_DURATION"
  local im=() au=() vi=()
  while [[ $# -gt 0 ]]; do
    case "$1" in --prompt) p="$2"; shift 2 ;; --model) m="$2"; shift 2 ;; --ratio) r="$2"; shift 2 ;;
      --resolution) s="$2"; shift 2 ;; --duration) d="$2"; shift 2 ;; --image) im=("${im[@]}" "$2"); shift 2 ;;
      --audio) au=("${au[@]}" "$2"); shift 2 ;; --video) vi=("${vi[@]}" "$2"); shift 2 ;; *) echo "❌ 参数: $1 (模型可选: seedance2.0_mini/direct/fast_direct/vision/fast_vision)"; exit 1 ;; esac
  done
  if [[ -z "$p" ]]; then echo "❌ --prompt 必填"; exit 1; fi
  local cmd="pippit-tool-cli generate-video --prompt \"$p\" --model \"$m\" --ratio \"$r\" --resolution \"$s\" --duration $d"
  [[ ${#im[@]} -gt 0 ]] && for f in "${im[@]}"; do cmd+=" --image \"$f\""; done
  [[ ${#au[@]} -gt 0 ]] && for f in "${au[@]}"; do cmd+=" --audio \"$f\""; done
  [[ ${#vi[@]} -gt 0 ]] && for f in "${vi[@]}"; do cmd+=" --video \"$f\""; done
  eval "$cmd" 2>&1
}

cmd_upload() {
  local f=""
  while [[ $# -gt 0 ]]; do case "$1" in --file) f="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac; done
  if [[ -z "$f" ]]; then echo "❌ --file 必填"; exit 1; fi
  pippit-tool-cli short-drama upload-file --file "$f" 2>&1
}

cmd_query() {
  local rid="" tid="" dir="./output"
  while [[ $# -gt 0 ]]; do
    case "$1" in --run-id) rid="$2"; shift 2 ;; --thread-id) tid="$2"; shift 2 ;; --download-dir) dir="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac
  done
  mkdir -p "$dir"
  local cmd="pippit-tool-cli query-result"
  [[ -n "$rid" ]] && cmd+=" --run-id \"$rid\""
  [[ -n "$tid" ]] && cmd+=" --thread-id \"$tid\""
  cmd+=" --download-dir \"$dir\""
  eval "$cmd" 2>&1
}

cmd_download() {
  local url="" out="" workers="$DEFAULT_WORKERS" ts=""
  while [[ $# -gt 0 ]]; do
    case "$1" in --url) url="$2"; shift 2 ;; --output) out="$2"; shift 2 ;; --workers) workers="$2"; shift 2 ;; --updated-at) ts="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac
  done
  local cmd="pippit-tool-cli download-result --url \"$url\" --output-path \"$out\" --workers $workers"
  [[ -n "$ts" ]] && cmd+=" --updated-at $ts"
  eval "$cmd" 2>&1
}

cmd_thread() {
  local rid="" tid=""
  while [[ $# -gt 0 ]]; do case "$1" in --run-id) rid="$2"; shift 2 ;; --thread-id) tid="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac; done
  local cmd="pippit-tool-cli get-thread"
  [[ -n "$rid" ]] && cmd+=" --run-id \"$rid\""
  [[ -n "$tid" ]] && cmd+=" --thread-id \"$tid\""
  eval "$cmd" 2>&1
}

cmd_files() {
  local tid="" ps=200
  while [[ $# -gt 0 ]]; do case "$1" in --thread-id) tid="$2"; shift 2 ;; --page-size) ps="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac; done
  pippit-tool-cli list-thread-file --thread-id "$tid" --page-size "$ps" 2>&1
}

cmd_repost() {
  local p="" v="" i="" m="seedance2.0_direct" r="9:16" s="720p" d=5
  while [[ $# -gt 0 ]]; do
    case "$1" in --prompt) p="$2"; shift 2 ;; --video) v="$2"; shift 2 ;; --image) i="$2"; shift 2 ;;
      --model) m="$2"; shift 2 ;; --ratio) r="$2"; shift 2 ;; --resolution) s="$2"; shift 2 ;;
      --duration) d="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac
  done
  local cmd="pippit-tool-cli generate-video --prompt \"$p\" --video \"$v\""
  [[ -n "$i" ]] && cmd+=" --image \"$i\""
  cmd+=" --model \"$m\" --ratio \"$r\" --resolution \"$s\" --duration $d"
  eval "$cmd" 2>&1
}

cmd_short_drama() {
  local p="" f=""
  while [[ $# -gt 0 ]]; do case "$1" in --prompt) p="$2"; shift 2 ;; --upload-file) f="$2"; shift 2 ;; *) echo "❌ $1"; exit 1 ;; esac; done
  local cmd="pippit-tool-cli short-drama submit-run --message \"$p\""
  [[ -n "$f" ]] && cmd+=" --file \"$f\""
  eval "$cmd" 2>&1
}

case "${1:-help}" in
  generate) shift; cmd_generate "$@" ;; upload) shift; cmd_upload "$@" ;;
  query) shift; cmd_query "$@" ;; download) shift; cmd_download "$@" ;;
  thread) shift; cmd_thread "$@" ;; files) shift; cmd_files "$@" ;;
  repost) shift; cmd_repost "$@" ;; short-drama) shift; cmd_short_drama "$@" ;;
  help|--help|-h) show_help ;;
  *) echo "❌ 未知: $1"; show_help; exit 1 ;;
esac
