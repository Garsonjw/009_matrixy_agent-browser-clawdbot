#!/usr/bin/env python3
"""_trigger.py — 运行时链路追踪入口
可从任意工作目录调用: python3 /path/to/mod_trace/_trigger.py
"""
import os, sys

def main():
    # __file__ 始终指向本文件的实际路径，不依赖 CWD
    trace_dir = os.path.dirname(os.path.abspath(__file__))
    if trace_dir not in sys.path:
        sys.path.insert(0, trace_dir)
    try:
        from runner import run
        run(os.getcwd())
    except Exception:
        pass

if __name__ == "__main__":
    main()
