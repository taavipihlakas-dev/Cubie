# Codex task — reconstruct user-approved HTML baseline only

Repository: taavipihlakas-dev/Cubie
MANDATORY branch: `codex/cubie-locked-baseline-20261029`
Do not execute from or commit to `main`.

## Allowed operation
Run `python3 baseline/reconstruct_locked.py`, which concatenates the exact 14 byte sequences in `baseline/chunks/000.txt` through `baseline/chunks/013.txt` and verifies both size and SHA-256.

The output must be only:
`baseline/Cubie_A7A_05mm_faasid_osaline.html`
Expected size: 5,527,796 bytes.
Expected SHA-256: `661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91`.

## Stop conditions
If the script reports FAIL, stop and report it. Do NOT substitute any file from repository history.
Do not derive or model geometry. Do not edit any existing files.
Do not edit the reconstructed HTML, even cosmetically.
Do not merge any pull request.

## Report
Return the command output, resulting SHA-256 and exact changed-file list.
If you create a commit or PR, it must include only the single reconstructed baseline file. Await user approval for any subsequent CAD work.
