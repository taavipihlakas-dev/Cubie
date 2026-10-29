# Cubie A7A — LOCKED BASELINE / NO GEOMETRY WORK AUTHORIZED

## Status
This is a staging-only task manifest, not permission to edit any CAD geometry.
The user must approve every geometric change before implementation and approve the candidate before any deterministic SCAD/HTML transfer.

## Only user-designated baseline
File name: `Cubie_A7A_05mm_faasid_osaline.html`
SHA-256: `661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91`
Actual baseline location: **NOT YET PRESENT IN THIS BRANCH**.
Do not use or infer a substitute from `Cubie_v48_32_3D.html`, `Cubie_v48_33_3D.html`, repository history, generated STL, or any other file. Those are locked.

## Preparatory assignment for Codex (READ ONLY)
1. Confirm whether `baseline/Cubie_A7A_05mm_faasid_osaline.html` exists on this branch.
2. If it is missing, report exactly: `BLOCKED: user-approved baseline not available in repository` and stop. Do NOT edit other files.
3. If it exists, compute SHA-256, match the exact digest above and provide a brief inspection report only.
4. Do not alter geometry, any viewer source, SCAD, model shape, material, lighting, controls, or component.
5. Do not merge anything, push CAD changes, or create a new baseline without explicit user authorization.

## Later workflow (once baseline has been provided and hash verified)
- The user issues a specific change request to ChatGPT.
- ChatGPT prepares a bounded written task; Codex produces a separate candidate in a work branch.
- ChatGPT independently verifies exact file/geometry diff and renders both computer/mobile viewer.
- User reviews candidate and explicitly approves or rejects.
- Only after approval, generate deterministic matching changes to SCAD and HTML viewer.

## Source controls
- `main` must not be modified from this staging branch.
- The previously created `PR #1` and `PR #2` are test/draft artifacts, NOT model sources.
