# Juneteenth Build Jam — GDG San Antonio

**Build with AI. Together. In two hours.**

Five civic tracks. Pick one, open the kit, ship a real AI prototype for your community.

---

## Before You Arrive

Install these four things so you're ready to go the moment the jam starts:

| Tool | Where to get it |
|---|---|
| **Antigravity** | [antigravity.google/download](https://antigravity.google/download) |
| **uv** (Python manager) | [astral.sh/uv](https://astral.sh/uv) |
| **Git + GitHub account** | [git-scm.com](https://git-scm.com) |
| **Free Gemini API key** | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) |

---

## Run a Kit in 90 Seconds

```bash
# 1. Clone this repo
git clone https://github.com/GDG-SAN-ANTONIO/juneteenth-build-jam.git

# 2. Go into your chosen track folder
cd juneteenth-build-jam/tracks/01-economic-empowerment

# 3. Add your free Gemini key
cp .env.example .env
# open .env and paste your key next to GEMINI_API_KEY=

# 4. Go
uv run app.py
```

---

## Pick Your Track

| # | Track | What you'll build |
|---|---|---|
| 01 | 🛍️ **Stand Up Shop** | Describe a community business → branded co-op profile, pricing strategy, SEO description, and matched civic grant |
| 02 | 📜 **Griot** | Paste a memory or transcript → historical timeline, map coordinates, narrative summary |
| 03 | 🩺 **PlainCare** | Describe a health or transit gap → plain-language action plan with local resources |
| 04 | 🗣️ **Speak Up** | Paste council meeting notes → key decisions, community impact, how to take action |
| 05 | 🌳 **Block Scan** | Describe a neighborhood hazard → violation classification and formal 311 / EPA petition |

Each track folder contains:
- `SPEC.md` — what to build and why
- `app.py` — starter Python script wired to the Gemini API
- `.env.example` — copy this to `.env` and add your key
- `requirements.txt` — all dependencies

---

## Step-by-Step Codelab

Follow the full guided walkthrough at the event site:
👉 **[gdg-san-antonio.github.io/juneteenth-build-jam/codelab.html](https://gdg-san-antonio.github.io/juneteenth-build-jam/codelab.html)**

It walks you through:
1. Installing Antigravity
2. Installing uv and git
3. Cloning this repo and picking a track
4. Installing workshop AI skills
5. The Spec Talk — aligning the AI on what to build
6. Generating 3 design docs (product, UI, engineering)
7. Implementing and testing with AI
8. Wiring up your Gemini API key
9. Previewing, verifying, and shipping

---

## Event Details

**June 19 · Geekdom, San Antonio**
Hosted by GDG San Antonio

Bring a laptop and an idea. Drop-ins welcome. The free Gemini API tier covers everything you need for the full jam.

---

## License

MIT — build on it, fork it, take it home.
