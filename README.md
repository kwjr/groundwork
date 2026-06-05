# 🪨 Groundwork

> **Project planning, meeting intelligence, and AI-powered insights — all in one offline-capable PWA.**

Groundwork is a single-file progressive web app built for professional services project managers. It replaces scattered notes, spreadsheets, and status email templates with a structured, AI-connected project hub that runs entirely in your browser — no backend, no account, no data leaving your machine unless you ask it to.

---

## ✨ Features at a Glance

| Category | What it does |
|---|---|
| 📋 **Project Charter** | Scope, objectives, assumptions, constraints, success criteria, stakeholders |
| 📝 **Meeting Log** | Structured meeting records with notes, decisions, and action items |
| ✅ **Action Items** | Full action item tracker with priority, status, due dates, and PSA logging |
| ⚖️ **Decisions** | Formal decision register with rationale, status, and PSA logging |
| 📊 **Analysis Archive** | Persistent per-project storage for Risk Analysis, Scope Reviews, and Change Requests |
| ✦ **AI Insights** | 8 AI-powered tools for risk analysis, summaries, agendas, debriefs, and more |
| 🌙 **Dark / Light mode** | Fully themed, preference persisted across sessions |
| 💾 **Offline-capable PWA** | Install to your home screen, works without internet |

---

## 🗂️ Tabs

### 📋 Charter
The foundation of every project. Captures everything you'd put in a project charter:

- **Project metadata** — name, type (Conversion / Implementation / Agile / Consulting), phase, billing model (T&M / Fixed-Fee), PM, sponsor, PSCloud/SharePoint link, start date, target go-live
- **RAG Status** — Red / Amber / Green project health indicator, visible across all tabs
- **Scope & Out of Scope** — side-by-side text areas
- **Objectives, Assumptions, Constraints, Success Criteria, Stakeholders** — editable lists with one-click add, inline editing, and Enter-to-add

---

### 📝 Meetings
A searchable, date-sorted meeting log with full-text search across notes, decisions, and action items.

**Logging a meeting:**
- 6 meeting templates: Status Call, Team Meeting, Sponsor Check-in, Discovery Workshop, Project Kickoff, Go-Live Review
- Fields: date, duration, title, attendees, notes, decisions made, action items
- **Log to Decisions** and **Log to Actions** toggles (off by default) — enable to automatically parse and push entries to the respective tabs on save
- Decisions and actions are parsed from free text (`Owner: Action (Due: date)` format is recognised automatically)

**Meeting Debrief (AI-powered):**
- Click 🗒 **Debrief** on any saved meeting, or use the Meeting Debrief tool in AI Insights
- Paste or upload a transcript (`.txt`, `.md`, `.vtt`)
- AI extracts: meeting date, duration, attendees, summary, decisions, action items, open questions, discussion points
- One click to save — pre-fills the meeting form and simultaneously logs decisions to the Decisions tab and action items to the Actions tab

---

### ✅ Action Items
Full action item tracking per project.

**Fields per item:**
- Auto-generated ID (A001, A002…)
- Description, Owner, Due Date
- Priority: High / Medium / Low
- Status: Open / In Progress / Complete / Cancelled
- Source (auto-linked to originating meeting)
- Notes

**Filters:** Open · In Progress · Overdue · Complete · All

**Log to PSA** — marks the item as complete and stamps a date, indicating it's been recorded in your external RAID tracking tool.

Items are automatically created when:
- Saving a new meeting with the **Log to Actions** toggle enabled
- Clicking **Save Meeting** on a Meeting Debrief result

---

### ⚖️ Decisions
A formal decision register with sequential IDs (D01, D02…).

**Fields:** Date, made by, decision text, rationale, impact/notes, status (Final / Open / Superseded)

**Log to PSA** — stamps the decision as logged to your external RAID tracking tool.

Decisions are automatically created when:
- Saving a new meeting with the **Log to Decisions** toggle enabled
- Clicking **Save Meeting** on a Meeting Debrief result

---

### 📊 Analysis
Persistent per-project archive of AI analysis outputs. Results auto-save here every time you run the relevant AI Insights tools — no extra steps needed.

Three sections:
- **Risk Analysis** — the last risk analysis run for this project
- **Scope Reviews** — all scope review outputs (up to 20, newest first)
- **Change Requests** — all change request briefs (up to 20, newest first)

Each entry shows its run timestamp and a ✕ Remove button. Click **Re-run →** to jump to AI Insights and refresh the analysis.

---

### ✦ AI Insights
Eight AI-powered tools, each tuned to a specific PM task. Results are project-scoped — switching projects clears results and shows only what was generated for the active project.

| Tool | Model | What it produces |
|---|---|---|
| 🔍 **Risk Analysis** | Sonnet | Colour-coded risk cards (High/Medium/Low) with details and mitigations |
| 📊 **Project Summary** | Sonnet | Structured RAG status report — Project, Schedule, Financial, Scope + Last/Next 30 Days |
| 🗺️ **Scope Review** | Sonnet | Scope creep risks, gaps, ambiguities, and clarification recommendations |
| 🔀 **Change Request** | Sonnet | Formal change request brief with full impact analysis |
| 📅 **Generate Agenda** | Haiku | Time-boxed agenda for your next meeting, tied to open items |
| 📋 **Extract Action Items** | Haiku | Paste raw notes → structured action items with owners and due dates |
| 📣 **Sponsor Update** | Haiku | Internal status email draft for your executive sponsor |
| 🗒️ **Meeting Debrief** | Haiku | Structured debrief from a transcript — summary, decisions, actions, open questions |

**All tools include:**
- ◼ **Stop** button — cancel any in-flight request instantly
- **⎘ Copy** — copies clean plain-text output for pasting into emails, docs, or your RAID log
- **Ask Groundwork** — free-form question box for anything not covered by the 8 tools

---

## 🏗️ Multi-Project Support

Groundwork manages as many projects as you need. The **project selector bar** sits below the tabs on every screen.

- Click the project name to open the dropdown — switch, rename (✏), duplicate (⧉), or delete (🗑) any project
- Projects are sorted alphabetically
- **Duplicate** clones the full charter without copying meetings, decisions, or action items — useful for similar engagements
- Each project has its own charter, meeting log, action items, decisions, and AI analysis archive
- AI Insights results are scoped per project — switching projects shows only that project's results

---

## ⚙️ Settings

Access via the ⚙ icon in the top-right corner.

### API Key
Paste your Anthropic API key to enable AI Insights when running outside claude.ai. Stored in browser `localStorage` only — never transmitted anywhere except directly to the Anthropic API.

### Appearance
Light / dark mode toggle. Preference persists across sessions.

### Backup & Restore
- **Save backup** — downloads a timestamped `.json` file of all project data
- **Restore from backup** — load a previously saved file (replaces all current data)
- **Saved snapshots** — up to 5 in-browser snapshots, each showing project count and timestamp. Restore or delete individually.

---

## 🚀 Deployment

Groundwork ships as a zip containing 8 files:

```
index.html                 ← the entire app
groundwork-sw.js           ← service worker (offline support)
groundwork-manifest.json   ← PWA manifest
groundwork-icon-512.png    ← home screen icon
groundwork-icon-192.png    ← home screen icon (Android)
groundwork-icon-32.png     ← favicon
.nojekyll                  ← GitHub Pages config
generate_groundwork_icons.py  ← icon source (Python/PIL)
```

**To deploy on GitHub Pages:**

1. Create a new repository (or use an existing one with a `gh-pages` branch)
2. Upload all 8 files to the root of the branch
3. In repository Settings → Pages, set source to the branch root
4. Your app will be live at `https://yourusername.github.io/your-repo/`

**To install as a PWA:**
- On desktop Chrome/Edge: click the install icon in the address bar
- On iOS Safari: Share → Add to Home Screen
- On Android Chrome: the browser will prompt automatically

---

## 💾 Data & Privacy

All project data is stored in your browser's `localStorage` under the key `groundwork_v2`. Nothing is sent to any server except:
- AI Insights calls → Anthropic API (using your API key)
- Google Fonts → fonts.googleapis.com (for DM Sans)

**No account. No telemetry. No cloud sync.**

To move your data between browsers or devices, use **Settings → Save backup** and **Restore from backup**.

---

## 🧠 AI Model Configuration

| Tools | Model | Rationale |
|---|---|---|
| Risk Analysis, Project Summary, Scope Review, Change Request | **claude-sonnet** | Judgment-heavy — requires reasoning about implications, not just pattern matching |
| Agenda, Extract Actions, Sponsor Update, Meeting Debrief, Ask | **claude-haiku** | Structured extraction and drafting — fast, cheap, reliable |

Estimated cost at full usage (15 projects × all 8 tools × once per week): **~$5–6/month**.

---

## 🎨 Design

Groundwork is part of **The Works** — a suite of standalone PWA tools for professional services PMs, all sharing the same visual language:

- **Font:** DM Sans
- **Palette:** Dark navy (`#0c1526`) with emerald green (`#34d399`) accent
- **Light mode:** Clean off-white with adjusted accent tones
- **Icons:** Custom isometric cornerstone mark (PIL-generated, 4× supersampled)

---

## 📄 License

Personal use. Not affiliated with Hyland Software.
