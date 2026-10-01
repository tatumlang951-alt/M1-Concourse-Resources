# Tatum Langston — Motorsports Resources

A complete static website for GitHub Pages. No paid service, framework, database, or build service is required. All photos are local files. The same repository should be updated for future changes; do not regenerate an unrelated website.

## Publish on GitHub Pages

1. Create a public repository, such as `motorsports-resources`.
2. Add this folder's **contents** to the repository root (so `index.html` is at the root).
3. Open repository **Settings → Pages**.
4. Choose **Deploy from a branch**, branch **main**, folder **/ (root)**, then save.
5. Wait for GitHub's Pages deployment to succeed. The Pages settings page supplies the actual public URL.

The empty `.nojekyll` file tells GitHub to serve these static files without Jekyll. Ordinary pushes to the publishing branch update the same website. No custom domain or paid plan is necessary for a public repository.

Official instructions: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Edit without losing the design

- `styles.css`: shared colors, typography, spacing, and responsive layout.
- `tools/build.py`: page templates and most content.
- `tools/dynamics.py`: vehicle-dynamics entries and definitions.
- `tools/books.json`: the 27 book entries in the required order.
- `assets/`: photographs, screenshots, and logos.
- `site.js`: optional local image preview and active navigation scrolling.

After changing content, run:

```sh
python tools/build.py
python tools/check.py
```

Commit both source and generated HTML. You can also edit the HTML directly for a quick change, but update the corresponding generator before the next rebuild so that change is preserved.

## Preview locally

Open `index.html` in a browser, or run:

```sh
python -m http.server 8000
```

Then open http://localhost:8000 . Test at phone and desktop widths before publishing substantial layout changes.

## Images

Seventeen images are included and displayed, including the high-school EV Grand Prix photo, NAIR logo, and collegiate iRacing image. To replace an image, update its file in `assets/` or its path in `tools/build.py`, regenerate, and commit.

Do not replace existing images with generated people, cars, or logos. Keep the college EV kart photo separate from the high-school program. Organization imagery and logos belong to their respective owners; no endorsement is implied.

## Validation performed

`tools/check.py` checks all local navigation links, internal anchors, image paths, the nine pages, all 27 books, the four recommended outlines, and selected required content. JavaScript syntax was checked with Node. A browser screenshot check was not completed in the authoring environment because a browser runtime was unavailable; responsive CSS was implemented but should still be visually reviewed.

## Editorial decisions

See `CONTENT_NOTES.md` for editorial decisions and source references. No analytics, tracking, external fonts, authentication, or third-party JavaScript is included.
