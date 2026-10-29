# CUBIE A7A — MANDATORY SOURCE LOCK
This GitHub branch is an isolated transport workspace. Older files from the repository's main branch, previous model versions, screenshots, search results, and history are NOT authorized as input.

**Only approved baseline:** `Cubie_A7A_05mm_faasid_osaline.html` reconstructed byte-for-byte from `locked_source/part_00.txt` through `part_17.txt` by `python3 tools/assemble_locked_baseline.py`.

**Verified SHA-256:** `661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91` (5527796 bytes). If validation fails, STOP. Do not substitute another file.

No CAD/SCAD/HTML geometric edits are authorized at present. Wait for a specific task provided in `tasks/CURRENT_TASK.md`.

For any later task: modify ONLY user-authorized areas, without reshaping/remeshing unrelated surfaces; keep assembled original immutable. Write candidate under `candidates/` and an explicit change report and verification data under `reports/`. Never claim perfect verification without independent comparisons. Never merge to main. Await the user's final approval before propagating changes into viewer or SCAD.

User communicates with ChatGPT as task manager; do not request the user to copy lengthy prompts.
