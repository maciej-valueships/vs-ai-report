---
title: "Context — Demystifying the Value of AI research project"
purpose: "Session transcript reconstruction. Hand-off file for continuing the work in Cursor or any other tool. Captures all decisions, frameworks, data, deliverables, and open questions."
project: "Valueships — Demystifying the Value of AI"
session_dates: "May 12–13, 2026"
author: "Maciej Wilczyński (founder), assisted by Claude research analyst"
last_updated: "2026-05-13"
---

# Context — Demystifying the Value of AI

A self-contained brief for picking up this research project in any tool. If you're loading this into Cursor or another editor: everything you need to keep building is here. Read in order.

---

## 1. The project at a glance

**Title:** *Demystifying the Value of AI — How Much Real Economic Value Is Actually in AI, and Can You Price It?*

**Tagline:** *Gross AI looks like a revolution. Net AI inside unrestructured organisations looks like a productivity tool.*

**Central thesis:** AI today delivers a 20–40 percent productivity multiplier on AI-fit tasks. Not a 10× output revolution. The macroeconomic productivity signal sits at ~0.09 percent per year (Acemoglu, MIT) — roughly 30× below electrification at peak. The CapEx-to-productivity ratio doesn't math out. Pricing AI should follow the measured Value Increase Index, not the maximalist narrative.

**Audience:** Valueships clients, prospects, B2B pricing community, LinkedIn/Substack readers. Founder-style external content.

**Style directives from Maciej (in order of importance):**

1. McKinsey/BCG/Bain Knowledge-Center research-analyst tone. Pyramid Principle. MECE. Crisp lead titles and subtitles. Sources everywhere. *But* don't write meta-language about "this is a desk research meta-analysis" — say what it is, not what kind of document it is.
2. Use the Valueships brand system on every visual. Pink #FF005E dominant, dark blue #0F155B accent at 9:1 ratio, white background, Lato (headers) + Roboto (body). Key visual flowing-line in corners. Spelling is **Valueships** (lowercase s), never *ValueShips*.
3. Only Valueships proprietary frameworks as structuring lenses. External research (NBER, Stanford, McKinsey, BCG, Bain, MIT NANDA, Statista) is data input, not a competing framework. Bain SaaS×AI quadrant and the Verticalist Services quadrant were explicitly removed mid-project.
4. The metric originally drafted as "VII" was renamed to **AVI (AI Value Index)** because VII reads as Roman seven. Brand attribution: **Valueships AI Value Index (AVI)**.
5. The Statista evidence Maciej supplied (13 charts) is canonical. Use the raw chart files he provided.
6. Macro proof (historical ladder, CapEx math, maximalist quotes) belongs in the foreword, not in a separate Part I.
7. The single load-bearing analytic of the dossier is the Value Equation: `Value created by AI = Revenue Increase + Cost Savings`, expressed as the AVI percentage per sector.

---

## 2. The narrative arc (what we built, in order)

### Phase 1 — Initial dossier
- Built `ai-productivity-pricing-evidence-pack.xlsx` with 24 sheets (Cover, TOC, Macro M01–M06, Sector S01–S12, Cases C01–C05, Synthesis Z01–Z04)
- Created companion narrative `real-quantified-value-of-ai-today.pplx.md`
- All sources researched: NBER RCTs, McKinsey, BCG, Bain, MIT NANDA, Stanford HAI

### Phase 2 — Pricing framework expansion
- Added V01–V05 sheets (value created/captured/retained, 10× pricing test, model decision matrix, ROI methodology, real benchmarks)
- Filename promoted from "dossier" to "evidence pack"

### Phase 3 — Statista integration
- Maciej shared Statista Research AI synthesis: 10 chart references
- Added ST01–ST10 sheets, each chart with its Statista URL
- Maciej shared a second batch (industry × function heatmap, TL;DR synthesis) → added ST11, EX01
- Third Statista batch: capital markets 72%, fintech profitability → ST12, ST13

### Phase 4 — Anti-hype layer
- Maciej directed: rebut Altman/Amodei/Huang publicly and quote them ruthlessly
- Added HY01 (maximalist tracker), HY02 (Anthropic Economic Index deep dive)
- Added VI01–VI03 (Value Index decomposition, revenue vs cost framing asymmetry, vendor pricing-page audit)
- Added PR01 (Replaceability × Attribution matrix), PR02 (SaaS vertical decision tree)

### Phase 5 — Capstone: the Value Increase Index (originally VII, now AVI)
- Maciej directed: "I need ONE clear index of value increased where we find this into a common denominator"
- Built IDX01 — live calculator with 17 sector lines, yellow inputs / green formulas
- Formula: `AVI = (Revenue Impact % × Revenue Share) + (Cost Impact % × Cost Share)`
- Built IDX02 — vendor capture worked example (300 FTE × $90K loaded × 20% AVI × 20% capture)
- Result: median AVI ≈ 15%, only 4 sectors clear 25% (the outcome-based pricing threshold)

### Phase 6 — Master of Content + master report
- Built MOC.md (Obsidian-style index)
- Built `demystifying-the-value-of-ai.md` (the master report)
- Added CX01 (CapEx vs productivity), HX01 (Industrial revolutions comparison)

### Phase 7 — Third-party framework cleanup
- Maciej directed: "Don't use other frameworks than the ones I have invented, let's build our own"
- Removed BX01 (Bain SaaS×AI quadrant) and BX02 (Verticalist AI Services quadrant)
- Replaced with VPQ01 — **Valueships AVI Pricing Quadrant** (proprietary 2×2: AVI × Revenue Attribution → Outcome / Effort / Premium / Subscription)

### Phase 8 — Maciej's own frameworks integrated
- Maciej uploaded `value-ships-historical-productivity-ladder` package (chart + CSV + readme)
- This contained his proprietary **Adoption-Adjusted Revolution Test** (5 criteria)
- Added LAD01 (Historical Productivity Ladder) and AAR01 (Adoption-Adjusted Revolution Test) sheets
- VII renamed to AVI in the workbook
- Master report restructured per Maciej's outline: macro folded into foreword, body = Micro → AVI → Pricing

### Phase 9 — Brand discipline pass
- Maciej uploaded vs-visuals zip with full Valueships brand book (SKILL.md, color/typography/logo/key-visual references, Python brand_palette + key_visual modules)
- Global rename ValueShips → Valueships (39 instances across MD files + 8 cells in Excel)
- Built `demystifying-the-value-of-ai.html` — branded publishable HTML
- Built 3× LinkedIn social heroes using the brand Python assets

### Phase 10 — Speed-of-information normalisation
- Maciej directed: "chart that compares revolutions with productivity increase normalized by the speed of information"
- Built `speed-normalized-productivity-chart.png` (dashboard) and `speed-normalized-productivity-linkedin.png` (social)
- Added SPD01 sheet to Excel
- Finding: AI converts 30–70× less productivity per log-decade of information speed than every prior revolution

### Phase 11 — Resources & context (current)
- Built `resources-to-share.md` — a clean, copy-paste source register
- Building `context.md` (this file) and an external-facing shareable HTML artifact

---

## 3. Final file inventory

### Markdown / text
- `demystifying-the-value-of-ai.md` — master report (foreword → micro → AVI → pricing → APA references)
- `MOC - Demystifying the Value of AI.md` — Obsidian map-of-content with wikilinks to everything
- `real-quantified-value-of-ai-today.pplx.md` — companion long-form narrative (early-phase version, still useful)
- `resources-to-share.md` — shareable bibliography organised into 10 tables
- `context.md` — this file
- `value-ships-historical-productivity-ladder-readme.md` — Maciej's chart documentation
- `demystifying-ai-value-master-content-map.md` — Maciej's own MOC variant

### HTML
- `demystifying-the-value-of-ai.html` — full master report rendered with the Valueships brand system
- `demystifying-ai-shareable.html` — external-facing shareable artifact (being built now)

### Excel
- `ai-productivity-pricing-evidence-pack.xlsx` — 64 chart-ready sheets

### Visuals (PNG)
- `speed-normalized-productivity-chart.png` — dashboard (1920×1200) speed-of-information chart
- `speed-normalized-productivity-linkedin.png` — LinkedIn (1200×1200) speed chart
- `demystifying-ai-linkedin-hero-1.png` — 0.09% vs 2.82% historical ladder pull
- `demystifying-ai-linkedin-hero-2.png` — $725B CapEx vs 0.09% productivity
- `demystifying-ai-linkedin-hero-3.png` — AVI sector heatmap teaser
- `value-ships-historical-productivity-ladder-chart.png` — Maciej's original ladder chart with Adoption-Adjusted Revolution Test sidebar

### Raw data (Statista exports)
- `statistic_id1378626_*.xlsx` — US labour productivity
- `statistic_id1482387_*.xlsx` — Hourly rates outlook
- `statistic_id1610445_*.xlsx` — GenAI value by function
- `statistic_id1610952_*.xlsx` — Cost decrease by AI function
- `statistic_id1619156_*.xlsx` — Task automation
- `statistic_id1620734_*.xlsx` — Pricing model preferences
- `statistic_id1661255_*.xlsx` — Fintech vs traditional profitability
- `statistic_id1661260_*.xlsx` — FinServ workforce impact
- `value-ships-historical-productivity-ladder-data.csv` — Maciej's ladder data
- `value-ships-historical-productivity-ladder-package.zip` — Maciej's full ladder package

### External reference
- `ai_index_report_2026.pdf` — Stanford AI Index 2026 (uploaded by Maciej)

### Cleanup needed (sandbox-blocked deletes)
- `ai-productivity-pricing-evidence-pack (1).xlsx` and `(2).xlsx` — auto-saved duplicates
- `real-quantified-value-of-ai-today.pplx (1).md` and `(2).md` — auto-saved duplicates
- `demystifying-ai-value-master-content-map (1).md` — auto-saved duplicate

---

## 4. The proprietary frameworks (Valueships canon)

### 4.1 Valueships Historical Productivity Ladder
*Sheet `LAD01`; chart `value-ships-historical-productivity-ladder-chart.png`*

Six productivity waves on one comparable scale:

| Wave | Period | Annual % signal | Source |
|---|---|---|---|
| Agrarian | post-1600 | 0.30% | Hoover Institution |
| First industrial | 1780–1860 | 0.78% | Crafts (FRBSF) |
| Electric / 2nd industrial | 1920–1970 | **2.82%** | Gordon |
| ICT baseline | 1970–2015 | 1.38% | Gordon |
| ICT revival | 1994–2004 | 2.26% | Gordon |
| **LLM-era AI** | 2024–2034 | **0.09%** | Acemoglu (NBER w32487) |

AI sits 30× below electrification at peak. 8× below the first industrial revolution.

### 4.2 Valueships Adoption-Adjusted Revolution Test
*Sheet `AAR01`*

Five criteria for whether a technology wave qualifies as a real productivity revolution:

1. **Constraint depth** — Is it removing a deep production bottleneck, or only cognitive friction?
2. **Adoption-speed normalisation** — Has it diffused long enough for multi-decade gains to show?
3. **Shop-floor rebuild** — Have organisations rebuilt their workflows, roles, and accountability around it?
4. **Social displacement capacity** — Are 10× labour claims being absorbed, or publicly reversed?
5. **Complexity tax** — After human review, governance, and integration, what is the NET uplift?

Verdict for LLM-era AI in 2026: **TOOL, NOT YET REVOLUTION** (fails 4 of 5, partial on constraint depth).

### 4.3 Speed-Normalised Productivity Test
*Sheet `SPD01`; chart `speed-normalized-productivity-chart.png`*

Productivity gain per log-decade of information-speed growth:

| Wave | Productivity %/yr | Info Speed Index (× agrarian) | Conversion efficiency |
|---|---|---|---|
| Agrarian | 0.30% | 1× | 0.300 |
| First industrial | 0.78% | 100× | 0.390 |
| Electric / 2nd industrial | 2.82% | 100,000× | **0.564** |
| ICT baseline | 1.38% | 100,000,000× | 0.172 |
| ICT revival | 2.26% | 1,000,000,000× | 0.251 |
| **LLM-era AI** | 0.09% | 100,000,000,000× | **0.008** |

AI converts 30–70× less productivity per log-decade of info speed than every prior revolution. The bandwidth is unprecedented; the conversion is not.

### 4.4 The Value Equation
*Body of master report, Part II*

> **Value created by AI = Revenue Increase + Cost Savings**

Each component is a percentage of the relevant base (revenue base or labour cost base). Cost Share dominates in 80 to 100% of B2B AI use cases.

### 4.5 AI Value Index (AVI)
*Sheets `IDX01` (live calculator) + `IDX02` (vendor capture worked example)*

> **AVI = (Revenue Impact %  ×  Revenue Share of Value)  +  (Cost Impact %  ×  Cost Share of Value)**
>
> *Revenue Share + Cost Share = 100%.*

17-sector benchmark table (computed live):

| Sector | Rev Imp | Cost Imp | Rev Share | AVI | Value $/FTE/yr | Vendor $/FTE/yr | Pricing band |
|---|---|---|---|---|---|---|---|
| Finance back-office | 3% | 30% | 5% | **28.6%** | $22,920 | $6,876 | OUTCOME |
| Marketing creative | 12% | 30% | 25% | **25.5%** | $22,950 | $4,590 | OUTCOME |
| Manufacturing lighthouses | 15% | 30% | 35% | **24.8%** | $17,325 | $3,465 | OUTCOME |
| Legal doc review | 5% | 28% | 15% | **24.6%** | $49,100 | $12,275 | OUTCOME |
| Software development | 8% | 25% | 20% | 21.6% | $28,080 | $5,616 | EFFORT |
| Consulting | 7% | 25% | 25% | 20.5% | $36,900 | $5,535 | EFFORT |
| TMT IT | 8% | 22% | 30% | 17.8% | $21,360 | $3,845 | EFFORT |
| Sales | 18% | 10% | 70% | 15.6% | $17,160 | $4,290 | OUTCOME (rev-attrib.) |
| FinServ overall | 12% | 18% | 40% | 15.6% | $18,720 | $3,744 | EFFORT |
| Healthcare (scribes) | 5% | 20% | 30% | 15.5% | $38,750 | $5,812 | EFFORT |
| Customer service | 5% | 17% | 30% | 13.4% | $8,040 | $2,814 | PREMIUM (sub: OUTCOME) |
| Consumer & Retail | 14% | 12% | 60% | 13.2% | $9,240 | $1,848 | PREMIUM |
| AEC / Construction | 8% | 15% | 40% | 12.2% | $11,590 | $1,738 | SUBSCRIPTION |
| Manufacturing (avg plant) | 5% | 12% | 30% | 9.9% | $6,930 | $1,040 | SUBSCRIPTION |
| Government | 3% | 10% | 10% | 9.3% | $8,370 | $837 | SUBSCRIPTION |
| Legal senior advisory | 3% | 10% | 20% | 8.6% | $30,100 | $3,010 | PREMIUM |
| Education | 2% | 8% | 10% | 7.4% | $5,180 | $414 | SUBSCRIPTION |

Median AVI ≈ 15%. Only 4 of 17 sectors clear the 25% outcome-based pricing threshold.

### 4.6 AVI Pricing Quadrant™
*Sheet `VPQ01`*

Two axes: **AVI** (low <15% vs high ≥15%) and **Revenue Attribution** (low vs high judgment call).

| Quadrant | AVI | Attribution | Pricing model | Capture rate |
|---|---|---|---|---|
| **OUTCOME ZONE ★** | HIGH | HIGH | Outcome-based / gainsharing | 30–50% |
| **EFFORT ZONE** | HIGH | LOW | Credit / effort / consumption | 10–25% |
| **PREMIUM ZONE** | LOW | HIGH | Premium per-seat + revenue-share bonus | 10–20% |
| **SUBSCRIPTION ZONE** | LOW | LOW | Per-seat with usage cap | 5–10% |

### 4.7 Replaceability × Attribution Matrix
*Sheet `PR01`*

Finer 5×3 lens for sub-segment decisions. Replaceability tiers: HIGH / MED-HIGH / MED / LOW-MED / LOW. Attribution: HIGH / MED / LOW.

### 4.8 SaaS Vertical Decision Tree
*Sheet `PR02`*

13 SaaS verticals mapped to recommended pricing model via 5-step decision tree (replaceability check → attribution check → buyer maturity check → risk check → revenue-frame check).

---

## 5. Hyperlinks ready to share

The full source register lives in `resources-to-share.md`. The single most-important sources to know:

- **Acemoglu (NBER w32487)** — https://www.nber.org/papers/w32487 — the 0.09% LLM-era AI annual productivity benchmark
- **Brynjolfsson, Li & Raymond (NBER w31161)** — https://www.nber.org/papers/w31161 — the 14% customer-support RCT
- **Dell'Acqua et al. (HBS 24-013)** — https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf — the BCG consultant 25% / 40% study
- **METR (Jul 2025)** — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — the −19% experienced-dev RCT
- **MIT NANDA (Aug 2025)** — https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf — the 95% pilot failure stat
- **Bain Technology Report 2025** — https://www.bain.com/about/media-center/press-releases/20252/$2-trillion-in-new-revenue-needed-to-fund-ais-scaling-trend---bain--companys-6th-annual-global-technology-report/ — the $2T revenue gap
- **Goldman Sachs CapEx tracking** — https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out — the $7.6T cumulative AI CapEx
- **Statista chart 35046** — https://www.statista.com/chart/35046/capital-expenditure-of-meta-alphabet-amazon-and-microsoft/ — Big Tech 2026 CapEx at $725B

For the maximalist quotes (rebuttal section):
- **Amodei "white-collar bloodbath"** — https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic
- **Altman "Reflections"** — https://blog.samaltman.com/reflections
- **Huang "every job affected"** — https://www.cnbc.com/2025/05/28/nvidia-ceo-jensen-huang-youll-lose-your-job-to-somebody-who-uses-ai.html
- **Anthropic Economic Index Mar 2026** — https://www.anthropic.com/research/economic-index-march-2026-report

For the public-case-study layer:
- **Salesforce reversal** — https://fortune.com/2025/09/02/salesforce-ceo-billionaire-marc-benioff-ai-agents-jobs-layoffs-customer-service-sales/
- **Klarna rehiring** — https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- **IBM redeployment** — https://www.entrepreneur.com/business-news/ibm-ceo-ai-replaced-hundreds-of-human-resources-staff/491341

---

## 6. The brand system (mandatory for any new visual)

From `vs-visuals-2` skill package:

- **Pink #FF005E** dominant (~90% of color use). Hero numbers, headlines, accents, dividers, arrows, logo icon, CTAs.
- **Dark blue #0F155B** restrained accent. 9:1 ratio to pink. Single accent moments, never dominant.
- **Black #080808** body text.
- **White background**.
- **Lato** for headers and hero callouts. H1 = Lato Medium 60pt. Hero numbers = Lato Black 70–90pt.
- **Roboto** for body and captions. 16pt 140% line height.
- **Key visual**: flowing-line concentric pattern, thin pink stroke, cropped/trimmed, anchored in corners. Never centered.
- **Logo**: pink arrow + "Valueships" wordmark. Protective field = 0.5× logo height minimum.
- **Reusable Python assets** in `vs-visuals-2/assets/`: `brand_palette.py` (the VS namespace), `key_visual.py` (the `draw_key_visual_corner` function).
- **CSS variables** for web work: `--vs-pink: #FF005E; --vs-blue: #0F155B; --vs-font-display: 'Lato'; --vs-font-body: 'Roboto';`

If a new visual breaks the 9:1 pink-to-blue ratio, it is off-brand. Use the checklist in `vs-visuals-2/references/checklist.md`.

---

## 7. Outstanding decisions and open questions

These were flagged in-session and never finalised:

1. **AVI naming** — Maciej said "VII sounds like seven, potentially might change it." Default chosen: **AVI (AI Value Index)**. Alternative: **VVI (Valueships Value Index)** for brand-first naming. One word from Maciej and rename is a 30-second global search-and-replace.
2. **PDF version of the master report** — the HTML can be print-converted, but a dedicated PDF wasn't built. Browser-print of `demystifying-the-value-of-ai.html` is the working interim.
3. **Polish-language version** — Maciej writes the Amalgamaty newsletter in Polish; a PL translation/adaptation of key sections may be needed but wasn't started.
4. **Folder cleanup** — five `(1)` and `(2)` duplicate files need manual deletion (sandbox blocks me).
5. **Stanford AI Index 2026 PDF** — uploaded but not yet parsed; useful for additional 2026 macro data points if needed.

---

## 8. How to continue this work in Cursor (or any tool)

**To extend the report:**
- The single source of truth is `demystifying-the-value-of-ai.md`. Edit it, then regenerate the HTML.
- The HTML generator script is in `outputs/build_branded_html.py` — re-run after edits.

**To add a new chart:**
- Use `vs-visuals-2/assets/brand_palette.py` and `key_visual.py`. Pattern proven in `outputs/build_linkedin_hero.py` and `build_speed_normalized_chart.py`.
- The mandatory brand checklist: pink dominant, key visual in corner, Lato + Roboto only, no other colors, logo present.

**To add a new sheet to the evidence pack:**
- Pattern proven across 64 sheets. Use the openpyxl approach in `outputs/add_spd_sheet.py` as the template.
- Reorder via `wb._sheets = [wb[s] for s in ordered_list]`.
- Run `recalc.py` after if formulas added.

**To swap AVI naming:**
- Global search-and-replace: `AVI` → `[new]` and `AI Value Index` → `[new full name]` across `.md` files, the HTML, the Excel pack (in cell values), and the LinkedIn social PNG `linkedin_example.py` if regenerating.

**To translate to Polish:**
- The wilczynski-voice skill handles Maciej's Polish writing style. Load it for any PL translation/adaptation pass.

**To publish externally:**
- The `demystifying-ai-shareable.html` (built alongside this context.md) is the external landing artifact.
- The full report HTML is for deep readers.
- The three LinkedIn social PNGs are the social-promotion set.

---

## 9. One-line summary for anyone joining the project

> Valueships built a proprietary research dossier arguing that AI today is a 20–40 percent productivity multiplier (not a 10× revolution), formalised via the Valueships AI Value Index (AVI), the AVI Pricing Quadrant, the Historical Productivity Ladder, and the Adoption-Adjusted Revolution Test. The macro math doesn't add up (Big Tech spending $725B/yr against a 0.09% productivity signal). Pricing should follow the AVI band, not the maximalist narrative. Salesforce, Klarna, and IBM cases prove the operational point. Companion artifacts: 64-sheet evidence pack, branded HTML report, three LinkedIn social PNGs, two charts, a shareable resources register, and this context file.

---

*End of context. Hand off to Cursor (or any other tool) with this file plus the markdown report and the brand system pack. Every decision, every framework, every URL, every chart number is here.*
