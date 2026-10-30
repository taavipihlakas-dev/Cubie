# Codex Cloud — read-only locked baseline verification (2026-10-30)

Purpose: verify the user-designated exact baseline without any CAD or repository edits.

Repository: `taavipihlakas-dev/Cubie`.
Required working branch or PR head: `codex/read-only-baseline-check-20261030`.
Expected locked file: `baseline/Cubie_A7A_05mm_faasid_osaline.html`.
Expected byte length: `5527796`.
Expected SHA-256: `661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91`.

Do these read-only steps:

1. Report the checked-out Git ref and `git rev-parse HEAD`.
2. Ensure `baseline/Cubie_A7A_05mm_faasid_osaline.html` exists on this checkout.
3. Compute its exact length and SHA-256 from disk. Compare against both values above.
4. Report `VERIFIED baseline/Cubie_A7A_05mm_faasid_osaline.html 661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91` **only if both checks pass**. Otherwise state `BLOCKED` and the precise observed failure.
5. Report the result of `git status --porcelain`; do not make changes.

Absolutely no edits, commits, PR updates, merges, geometry modeling, HTML modifications, new versions, or substitutions. Previous `Cubie_v48_32_3D.html` and `Cubie_v48_33_3D.html` are not substitute baselines.
