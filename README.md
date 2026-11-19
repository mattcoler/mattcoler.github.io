# mattcoler.github.io

Personal academic site built with [Quarto](https://quarto.org) and published on GitHub Pages.

## Put it online

1. Create a repo named `mattcoler.github.io` (your GitHub username) and push these files to `main`.
2. In the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Every push to `main` now rebuilds and publishes the site (`.github/workflows/publish.yml`). No local install needed; you can edit files in GitHub's web editor.
4. Search the files for `USERNAME`, `COURSE-REPO` and `OVERLEAF-LINK` and replace them.

Your class site: any other repo of yours with Pages turned on appears at `mattcoler.github.io/REPO-NAME/`. Link it from `teaching.qmd`.

Custom domain (optional): Settings → Pages → Custom domain. Project sites like the course follow automatically.

## Where things live

| What | File |
|---|---|
| Menu, site title, footer, themes | `_quarto.yml` |
| Home page | `index.qmd` |
| Research / AI Ethics / Teaching / CV | `research.qmd`, `ai-ethics.qmd`, `teaching.qmd`, `cv.qmd` |
| Publications (filterable list) | `publications.yml` (data), `publications.qmd` (page), `_publications.ejs` (layout) |
| News posts | `posts/YYYY-MM-DD-slug/index.qmd` |
| Colours and fonts | `custom.scss` (light), `custom-dark.scss` (dark), `_rules.scss` (shared styling) |

## Add a news post

Make a folder `posts/2026-12-01-my-talk/` with an `index.qmd`:

```
---
title: "Talk title"
description: "One line for the listing."
date: 2026-12-01
categories: [talk, ai-ethics]
image: https://...   # optional thumbnail
---

Text in markdown.
```

It shows up on the News page and the home page automatically.

## Add a publication

Add an entry to `publications.yml`. Categories become filter options; `url` links the title.

## Preview locally (optional)

Install Quarto, then run `quarto preview` in this folder.
