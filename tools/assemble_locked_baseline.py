#!/usr/bin/env python3
"""Deterministically reconstruct the ONLY authorized baseline from immutable parts."""
from pathlib import Path
from hashlib import sha256
import sys

ROOT = Path(__file__).resolve().parents[1]
PARTS = sorted((ROOT / "locked_source").glob("part_*.txt"))
EXPECTED_SHA256 = "661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91"
EXPECTED_BYTES = 5527796

if len(PARTS) != 18 or [p.name for p in PARTS] != [f"part_{i:02}.txt" for i in range(18)]:
    sys.exit("ERROR: Missing or unexpected parts; no source assembled")
body = b"".join(p.read_bytes() for p in PARTS)
actual = sha256(body).hexdigest()
if len(body) != EXPECTED_BYTES or actual != EXPECTED_SHA256:
    sys.exit(f"ERROR: Baseline integrity check failed, bytes={len(body)} SHA256={actual}")
outdir = ROOT / "baseline"
outdir.mkdir(exist_ok=True)
output = outdir / "Cubie_A7A_05mm_faasid_osaline.html"
if output.exists() and output.read_bytes() != body:
    sys.exit("ERROR: Refusing to overwrite modified baseline")
output.write_bytes(body)
print(f"VERIFIED: {output} ({len(body)} bytes SHA256 {actual})")
