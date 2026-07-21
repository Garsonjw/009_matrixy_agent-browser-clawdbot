#!/usr/bin/env bash
# trace-init.sh — 运行时链路追踪入口
# 可从任意目录调用: bash /path/to/trace-init.sh
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR" || exit 0
exec python3 mod_trace/_trigger.py 2>/dev/null
