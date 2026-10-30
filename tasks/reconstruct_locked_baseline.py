from pathlib import Path
from hashlib import sha256

root = Path(__file__).resolve().parent.parent
name = "Cubie_A7A_05mm_faasid_osaline.html"
pieces = [root / "baseline_parts" / f"{name}.part{i:02d}" for i in range(1, 8)]
payload = b"".join(piece.read_bytes() for piece in pieces)
expected = "661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91"
assert len(payload) == 5527796
assert sha256(payload).hexdigest() == expected
dest = root / name
assert not dest.exists() or dest.read_bytes() == payload
dest.write_bytes(payload)
assert sha256(dest.read_bytes()).hexdigest() == expected
print(f"VERIFIED {name}: {expected}")
