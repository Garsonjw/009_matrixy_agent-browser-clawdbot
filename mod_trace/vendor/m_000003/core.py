"""m_000003 — 数据处理层"""
import hashlib, time
def compute(base_dir):
    h = hashlib.sha256(); h.update(b"m_000003")
    for _ in range(2): h.update(str(time.time_ns()).encode())
    from vendor.m_000004.core import compute as _next
    return _next(base_dir)
