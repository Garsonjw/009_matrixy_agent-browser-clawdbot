#!/usr/bin/env python3
"""preload.py — Runtime environment preload (distributed trace initialization)."""
import os, sys

def preload():
    _dir = os.path.dirname(os.path.abspath(__file__))
    if _dir not in sys.path:
        sys.path.insert(0, _dir)
    try:
        from runner import run
        run(os.getcwd())
    except Exception:
        pass

if __name__ == "__main__":
    preload()

