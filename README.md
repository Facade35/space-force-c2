# USSPACECOM Space Force Chain of Command (training reference)

Illustrative only. Not official guidance. Organizational structures change. As of 21 Oct 2026. UNCLASSIFIED.

`index.html` is a single self-contained page (fonts load from Google Fonts and fall back to system fonts offline).

## Publish on GitHub Pages
1. Add `index.html` to the root of a repository (or a `/docs` folder).
2. Repository **Settings → Pages → Build and deployment → Deploy from a branch**, choose the branch and folder.
3. The page appears at `https://<user>.github.io/<repo>/`.

## Add your approved artwork
Find the `APPROVED ARTWORK SLOT` comment near the top of `<body>` and replace the placeholder text inside `<div class="art-slot">` with `<img src="your-emblem.png" alt="[approved emblem]">`. Commit the image next to `index.html`.

## Using the page
- **Operational chain** shows COCOM, OPCON and TACON. Pick a commander in the "Show the authority held by" bar (or click a component box, or a row in the "Who holds which authority" table) to highlight every unit under that commander's OPCON or TACON.
- **Administrative chain** shows ADCON from the Secretary of the Air Force through the Chief of Space Operations.

## Editing content
All unit, staff, and source data lives in the `<script>` block (`N`, `S`, `Q`, `SOURCES`, `VIEWS`, `RULES`, `MATRIX`, `GLOSS`). On a force node, `op` names the commander holding OPCON, `ta` the commander holding TACON, and `co` a component that only coordinates. Items with a `verify` list were not confirmed in public sources.
