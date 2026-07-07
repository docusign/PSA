# Docusign Manage: From Static PDFs to Agentic Workflows

Reference pages for the **Bengaluru Meetup Workshop**.

- **Audience:** Cross-functional business stakeholders (procurement, finance, legal, sales, ops), with a procurement agreement use case as the common thread. Primary hands-on audience: implementation-partner architects & developers.
- **Runtime:** ~65–75 minutes.

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Landing page linking both references |
| `1_Run_of_Show.html` | Presenter agenda, segment timings, persona/audience framing, narrative arc |
| `2_Hands_on_Flow.html` | Step-by-step lab, CLI login & bulk upload → extraction → MCP via Copilot Studio → Agent Studio demo |

Each page uses inline CSS/JS. Official Docusign brand assets are bundled locally under `assets/` (no external CDN calls), so the pages render identically offline or over the web.

## Brand assets (`assets/`)

- `assets/img/`, official Docusign logo SVGs (white for the dark header, black variant, and the "Bringing Agreements to Life" tagline logo).
- `assets/fonts/`, the **DSIndigo** brand typeface (Light / Medium / SemiBold, `woff2` + `woff`), loaded via `@font-face`.
- Brand palette: electric indigo `#4C00FF`, coral `#FF5252`, ink `#130032`.

Keep the `assets/` folder alongside the HTML files when uploading, or the logo and fonts won't resolve.

## Hosting on GitHub Pages

1. Create a new **public** repository and upload all files in this folder, **including the `assets/` directory**.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source = Deploy from a branch**, **Branch = main**, **Folder = / (root)**, then **Save**.
4. After ~1 minute the site is live at `https://<your-username>.github.io/<repo-name>/`, landing on `index.html`.

The `.nojekyll` file is included to skip Jekyll processing and serve the files as-is.

## Note on CLI commands

The Prerequisites and Stage 1 sections of the hands-on flow use the **official Docusign Agreement CLI** (the `ds` command from `@docusign/agreement-cli`), following the IAM Toolkit references: configure agreement types & fields, test customizations, deploy, and bulk-ingest. Stage 2 (extraction in Navigator / Agreement Manager) follows the current product UI, confirm exact screen labels against your account before running the session live.
