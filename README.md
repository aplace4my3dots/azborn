# AZBORN — E-RUN MAGAZINE
### Futuristic Fashion & Photography · Live Gallery

> **Live Preview:** `https://5173-…e2b.app` (running `npm run dev` on port 5173)  
> **Branch:** `arena/019fd799-azborn` · **32 covers** · **14 Collections** · **Daily Concept Engine**

AZBORN Group's **E-RUN Magazine** engineers haute couture from speculative physics — ferrofluid spikes, acoustic levitation, aerogel silk, cryo ice, holographic chrome & inclusive gothic luxury. Every cover is a production-grade AI prompt + viral Instagram caption kit.

---

## 🚀 Quick Start — Live Gallery

```bash
npm install
npm run dev   # → http://localhost:5173 → preview at https://5173-{sandbox}.e2b.app
npm run build # → dist/ (then: cp -r images dist/images)
```

**Features:**
- Responsive 12-col grid (3/4 aspect) with hover reveal
- Filter by 6 pillars: All / New Concepts / Cyber-Elegance / Bio-Futurism / Neo-Brutalist / Digital Surrealism / Gothic Luxury
- Lightbox with prompt copy, caption copy, download, prev/next, keyboard (← → / Esc), share
- Hero featuring latest `2026-08-06 Ferrofluid Obsidian Velvet`
- Playbooks & Daily Engine sections

---

## 📸 Editorial System (4 Playbooks)

| Playbook | Lines | Purpose |
|----------|-------|---------|
| `E-RUN_MAGAZINE_MASTER_PLAYBOOK.md` | 329 | 14 Collections — every cover → Midjourney v6.1 / Flux prompt + Hook→Story→CTA→Hashtags |
| `NEW_CREATIVE_CONCEPTS_AND_DAILY_AUTOMATION.md` | 89 | 3 new concepts (Mercury / Silkmoth / Lightning) + daily automation guide |
| `AUDIENCE_GROWTH_PLAYBOOK.md` | 131 | 4 visual pillars, prompt framework, 0→100k growth |
| `LAUNCH_CAMPAIGN_GRID_AND_CAPTIONS.md` | 137 | 9-grid launch calendar (9 posts ready) |

All prompts optimized for ` —ar 4:5 —style raw —v 6.1` (3:4 vertical covers).

---

## 🤖 Daily Concept Engine

```bash
python3 scripts/generate_daily_concept.py
# → captions/YYYY-MM-DD.json + .txt (prompt + caption)
# then in Arena: “generate today’s image” → generate_image → images/erun_…
python3 scripts/post_to_instagram.py
# needs: INSTAGRAM_ACCESS_TOKEN + INSTAGRAM_ACCOUNT_ID (Meta Graph API /media + /media_publish)
```

**Matrix (6 rotating themes):** Acoustic Levitation, Silk-Moth Aerogel, Tesla Coils, Ferrofluid Obsidian, Chronolithic Amber…  
**Today (2026-08-06):** `Ferrofluid Magnetic Sculpture & Obsidian Velvet` — [`images/erun_issue_ferrofluid_obsidian_velvet_3x4.jpg`](images/erun_issue_ferrofluid_obsidian_velvet_3x4.jpg) + [`captions/2026-08-06.json`](captions/2026-08-06.json)

**Automation:** `.github/workflows/daily_erun_instagram_bot.yml` runs daily 13:00 UTC (09:00 EST / 17:00 Tehran) → generate → commit → post.  
*Note: GitHub App cannot push `workflows` directly — add the file via GitHub web UI if needed (copy from local `.github/workflows/`).*

---

## 🗂️ Repository Layout

```
.
├── index.html              # Gallery entry
├── style.css               # Editorial dark system (Bebas Neue / Inter / JetBrains Mono)
├── app.js + data.js        # Gallery logic + 32-issue metadata
├── vite.config.js          # host 0.0.0.0 + allowedHosts:true for preview
├── images/                 # 32 covers (3:4)
│   ├── erun_issue_*.jpg    # 14 collections + variants
│   ├── erun_new_concept_*.jpg
│   └── erun_issue_ferrofluid_obsidian_velvet_3x4.jpg  # latest
├── captions/               # YYYY-MM-DD.json/.txt
├── scripts/
│   ├── generate_daily_concept.py
│   └── post_to_instagram.py
└── *.md                    # 4 playbooks
```

---

## 🎨 Pillars & Mastheads

- **Cyber-Elegance** — Neon Cyan #00FFCC, Liquid Chrome
- **Bio-Futurism** — Emerald, Kintsugi Gold, Mycelium
- **Neo-Brutalist** — Carbon Black, Distressed Red Stencil
- **Digital Surrealism** — Iridescent Prism, Lavender Haze
- **Gothic Luxury** — Deep Burgundy #5B061A, Obsidian
- **New Concepts** — Acoustic, Aerogel, Electrostatic

---

## 📈 Next Steps

- Enable daily cron (add `INSTAGRAM_ACCESS_TOKEN` secret)
- Generate next cover: `Chronolithic Amber` (2026-08-07)
- Deploy `dist/` to GitHub Pages / Vercel / Cloudflare Pages

Built in Falkenstein, Saxony · 2026-08-06 · `arena/019fd799-azborn`
