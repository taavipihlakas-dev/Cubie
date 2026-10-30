#!/usr/bin/env python3
"""Reconstruct an unchanged user-approved source file. No geometric processing."""
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[1]
parts_dir = root / "baseline" / "chunks"
target = root / "baseline" / "Cubie_A7A_05mm_faasid_osaline.html"
expected_sha = "661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91"
expected_size = 5527796
expected_files = [f"{i:03d}.txt" for i in range(14)]
actual_files = sorted(p.name for p in parts_dir.iterdir() if p.is_file())
if actual_files != expected_files:
    sys.exit(f"FAIL: expected 14 ordered chunks, got: {actual_files}")
data = b"".join((parts_dir / name).read_bytes() for name in expected_files)
actual_sha = hashlib.sha256(data).hexdigest()
print(f"Combined size: {len(data)} bytes")
print(f"SHA-256: {actual_sha}")
if len(data) != expected_size or actual_sha != expected_sha:
    sys.exit("FAIL: source mismatch; file NOT written")
if target.exists():
    if target.read_bytes() != data:
        sys.exit("FAIL: existing baseline differs; no overwriting allowed")
    print("PASS: locked baseline already exists and is identical")
else:
    target.write_bytes(data)
    print("PASS: exact locked baseline restored (no transformations)")
