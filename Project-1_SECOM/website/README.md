# SECOM project website

This folder contains a dependency-free, static project page designed for GitHub Pages.

## Preview locally

From `Project-1_SECOM`, start a static server:

```powershell
..\.venv\Scripts\python.exe -m http.server 8000 --directory website
```

Then open `http://localhost:8000`.

## GitHub Pages deployment

The repository contains multiple projects, so the cleanest option is to publish this folder to a dedicated `gh-pages` branch. Commit the website files first, then run this command from the repository root:

```powershell
git subtree push --prefix Project-1_SECOM/website origin gh-pages
```

In the GitHub repository, open **Settings → Pages**, choose **Deploy from a branch**, and select the `gh-pages` branch and `/ (root)` folder.

The expected project-page address is:

`https://drpproton.github.io/semiconductor-projects-tda/`

## Contents

- `index.html`: editorial case-study page
- `styles.css`: responsive layout, typography, print styles, and motion
- `script.js`: reading progress and scroll reveals
- `assets/`: self-contained figures and favicon

All links to the analysis point directly to the `Project-1_SECOM` folder on GitHub.
