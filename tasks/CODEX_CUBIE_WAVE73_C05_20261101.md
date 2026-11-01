# CODEX TASK — Cubie A7A: Ø73 Waveshare clearance, XLR interference, C0.5, smooth surfaces

Owner-approved execution request dated 2026-10-31. **Implement, verify, and immediately publish the working candidate to GitHub Pages for the owner to inspect. Do NOT wait for approval before publishing a verified working preview; approval is required only before changing the locked baseline.**

## Mandatory immutable baseline

Repository: `taavipihlakas-dev/Cubie`
Sole geometry input: **`main/Kohutavalt kaua ver.1.html`**, exactly 5,527,796 bytes, SHA-256 `661666f196459ec15edce3b1fe39cd552ce4a25dd7212a606bf7cf77d3bdbe91`.

Do not use `Cubie_v48_32_3D.html`, `Cubie_v48_33_3D.html`, older .scad files, or any v01 HTML as a source of geometry. Original HTML embeds a quantized triangle mesh in JS `const geometry=[...]`; reconstructing a different historical CAD model is prohibited. Preserve the exact baseline bytes and all unrelated dimensions/features. Work on this branch. Never overwrite the baseline.

## 1. Waveshare Ø73 mm upper-ring opening from panel FRONT to first ring BOTTOM

Owner's latest explicit dimensions (mm):
- Waveshare: Ø66.
- First ring inner Ø67.
- First ring outer Ø71, radial thickness 2.
- **Required panel-side clearance Ø73**, radius **36.5 mm** — exactly 1 mm radially outside the first ring's outer radius 35.5 mm.
- Remove only material **belonging to the FRONT PANEL** in the upper marked arc/region (not the intact lower half), beginning at the panel's front face and continuing fully to the **bottom plane of the first Waveshare ring**. This is a full-depth clearance through the forward panel material, NOT merely a notch confined to the ring's height.
- Respect the Waveshare ring axis and its existing tilt and precise position as encoded in the immutable baseline. Do NOT infer a depth/angle/position from old .scad files.
- Do NOT reduce or enlarge the ring itself or change its diameters, tilt, placement, cup underneath, or intact lower arc. Do not remove material outside this explicit panel region.
- The owner marked the ring blue, the panel material to remove red, and the interference yellow, in 3 supplied chat screenshots. Since screenshot attachments may not be available in the repo, prioritize the precise written constraints over guesses at the arc limits. If the arc cannot be determined from base geometry alone, report that specifically rather than alter other arcs.

## 2. XLR-vs-Waveshare-cup intersection

Inspect the XLR bore nearest the Waveshare cup over the FULL bore depth for genuine solid-to-solid intersection. If interference exists, remove it with the smallest local correction; the preferred correction is to shift ONLY that XLR bore and its corresponding connector coaxially, preserving diameter, geometry, and their mutual alignment. Do not alter the other XLR or unrelated geometry. Note that an apparently closed XLR hole when the camera is reset is a perspective effect, not a defect: DO NOT attempt to 'fix' the reset view or bore floor solely because of that. If no actual overlap exists, do not move anything; record the evidence.

## 3. All structural edges: C0.5

Create **0.5 mm straight chamfers** (not radius fillets) along all feasible structural edges of the whole manufactured piece: front/back outer perimeters, all holes and recesses on both relevant sides, cup edges including inner edges, lamp roof's two circular bores (top and underside), and other actual sharp structural edges. Retain the existing larger rounded profiles / Fosi reference radii. Preserve bores, part-fitting interfaces, walls, shape, placement, and dimensions outside explicit chamfers. Respect local geometry where a full C0.5 cannot physically fit: record an exact exception, don't silently substitute another radius/chamfer or change wall thickness.

## 4. Inspect and clean the whole manufactured solid for 'mirror smooth' quality

The owner means topologically/geometrically continuous-looking smooth surfaces, **NOT a glossy material**.
- Remove z-fighting from duplicate / coplanar triangles, overlapping surfaces, stray spikes/triangles, visible longitudinal striping/patches on cup walls, faceted-looking cylindrical surfaces, flipped/inconsistent normals, holes, and invalid disconnected artifacts.
- Keep unchanged neutral gray material and lighting, all functional geometry, all fixed external dimensions, and all existing curve radii. Do NOT hide defects simply by changing shaders/colors or turning off transparency.
- Do not assume that applying smooth normals corrects actual geometric overlap. Validate topology as possible, distinguish visual artifacts from CAD defects.

## 5. Preserve viewer functionality from the currently WORKING Pages candidate

Preserve original baseline 3D geometry but maintain existing interactive rotation, pan, zoom, mobile gestures, opacity slider, mm grid, XLR toggles, annotations, and user-specified part visibility UX:
- Initially manufactured panel is visible; all 11 addable parts hidden.
- They can be individually shown and hidden through 'Osad'.
- 'Lähtesta' also returns addable parts to hidden state.
The previous `Cubie_A7A_05mm_faasid_osaline_v01_osad_peidus.html` is allowed only as a **reference for the precise UI logic**. Do not source geometry from it. This administrative UI transplant is a distinct, approved requirement.

## 6. Required checks / evidence

- Verify baseline size and SHA-256 BEFORE and AFTER.
- Verify the changes stay in approved region for the Ø73 cut and XLR clash correction; compare untouched meshes against baseline numerically and/or with deterministic face correspondence, not only a screenshot.
- Check new and prior cylindrical intersections and all chamfer edges; report if some edges cannot be chamfered C0.5 while preserving structure.
- Ensure no new triangle soups, nonmanifold artifacts, or stray bodies.
- Validate embedded JS scripts (at least syntax), geometry decode/triangle counts, browser interactions as available; do not claim actual Samsung Internet/Windows operation without testing it.
- Keep changed-file diff minimal. Do NOT claim 'verified' when checks were skipped.

## 7. Immediate Pages publication of every VERIFIED completed candidate

1. Create a new numbered, standalone HTML candidate; do not alter the locked baseline. Commit on your working branch.
2. Deploy the candidate **immediately** via existing GitHub Pages workflow infrastructure. Pages is already enabled, and current project Pages URL is `https://taavipihlakas-dev.github.io/Cubie/`.
3. Use SHA-256 and real HTTP GET to verify that the published page is EXACTLY the new candidate (not the old cached v01). Record the full direct URL. Preserve rollback to older released candidate. Do NOT gate publishing on owner approval.
4. Report which measures, chamfers and checks were completed, any remaining exceptions, and the live clickable URL.
5. The candidate is NOT the newly approved baseline until owner specifically approves it. If a hard geometry blocker prevents safe completion, do not publish a broken candidate; report blocker clearly.

A prior historical `AGENTS.md` line banning Pages is overridden by the owner's explicit newer instruction to use Pages immediately. You may update AGENTS accordingly on your task branch, without overwriting the locked baseline or merging to main. Current published Pages site must remain accessible while work proceeds.

## Completion criteria
A functionally working updated 3D viewer at a real Pages URL with (a) Ø73 upper-ring cut front-to-ring-bottom, (b) XLR collision solved or explicitly verified absent, (c) C0.5 where geometrically feasible with exact exceptions, (d) geometrically clean smooth surfaces, (e) all original viewer controls and visibility UX, and (f) deterministic comparison to locked baseline.