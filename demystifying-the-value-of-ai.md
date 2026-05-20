---
title: "What is the real economic value of AI?"
subtitle: "A meta research analysis of productivity reports and pricing implications"
tagline: "Today AI is a useful, highly effective tool, and yet it's far away from the 10x output revolution we were promised"
author: "Maciej Wilczynski, Ph.D. Managing Partner at Valueships"
cover_byline: "by Maciej Wilczynski, Ph.D., Managing Partner"
date: "May 2026"
license: "Valueships proprietary frameworks and methodology"
source_of_truth: "demystifying-the-value-of-ai.md"
build: "python3 build_branded_html.py"
---

# What is the real economic value of AI?

## A meta research analysis of productivity reports and pricing implications

> **Today AI is a useful, highly effective tool, and yet it's far away from the 10x output revolution we were promised**

---

## Foreword: My personal problem with AI value

*To those who are lost in the AI ambiguity,*

A new AI report is published every week. You see another piece of content that says AI creates incredible value. The problem is that every report measures value differently: hours saved, tickets resolved, code shipped, documentation time reduced, revenue generated, errors avoided, or hopefully global GDP lifted.

We were promised a revolution, while I saw a consistent pattern of **20–40%** uplifts in various areas. Considering a staggering **$1 trillion** in capital expenditures from tech giants in 2026, this seemed... low.

None of these sector studies is comparable until you put them on a common economic denominator, so I tried to do that. I was literally lost in the constant stream of numbers and the unclear potential value of AI.

As a scientist myself, I ran a meta-analysis of **67 sources** [@1,@2,@12,@19,@29,@37,@71] — macro journals, consulting reports, RCTs, and the publications shaping public opinion (McKinsey, Bain, BCG, Goldman Sachs, MIT, Stanford, Harvard, and others in the reference list). I did not find another synthesis that puts fragmented AI productivity claims on one comparable percentage scale; that gap is what the **AI Value Index (AVI)** is for. Definition, formula, and design history are in Part II (including an expandable **AVI design & methodology** panel); how the desk research was done is in [Methodology: how this report was built](#avi-methodology-appendix).

It's funny, because I have used a lot of AI to deliver this (Claude, Perplexity, Cursor, Statista AI Assistant).

Honestly, I believe we are going in a certain "chimera"-like language and outputs. One can say it creates a certain "monstrosity" language where real AI value meets the AI slop, and where human synthesis capabilities meet human laziness.

My relation with AI was following: I was the craftmaster, an AI was the apprentice. Very fast, capable, but only a practitioner. I believe the overall narrative, methodology is well defined, because it's mine.

Where this report lacks, for sure, is simply because of my AI capabilities — again meeting Liebig's law (see next paragraph) where my knowledge is simply the scarcity.

I normalized those sources into AVI; the pattern is consistent but bounded. I was right: while some headline claims cluster around a **20–40%** uplift on the task being measured, it was just a high anchor for the memory.

**The median realized business impact across sectors is closer to 15 percent.** Meaningful, yet definitely not transformational. AI in current systems is a highly effective tool; however, it is not a 10× output revolution we are promised.

The AI moguls say, "This time is different."

Dario Amodei [@47] says half of entry-level white-collar jobs disappear within five years. Sam Altman says AGI is here, intelligence is too cheap to meter. Jensen Huang [@52] from Nvidia says every job will be affected immediately. The Anthropic Economic Index report [@49] says 49 percent of jobs see AI used for a quarter of their tasks. Each statement is in the public record, sourced and quoted below. What enterprises measure on P&L lines, and what happens when firms try to swap headcount for models at scale, tells a different story.

Marc Benioff from Salesforce recently acknowledged [@37] that cutting thousands of roles to "replace them with AI" had been a mistake. The overall quality fell, and rehiring followed. Well, he stated publicly what the P&L already implied. When Salesforce cut its customer support from 9,000 to 5,000 in 2025, the company spent the next three months walking it back.

Klarna replaced 700 customer service agents with OpenAI and is now rehiring. IBM automated 94 percent of routine HR tasks with AskHR, and the total IBM headcount rose, not decreased. The pattern is repeating elsewhere: efficiency-first layoffs followed by quality regression and partial rehiring.

These cases are public; far from anomalies, they are what happens when headline AI efficiency meets enterprise reality — quality regression, partial rehiring, and P&L lines that tell a quieter story than the press release.

### Valueships - pricing engineers for tech companies

Valueships is a consulting boutique specializing in crafting pricing & commercial solutions for tech companies. We want you to pursue your strategic vision without compromise, and increased EBITDA is a way to achieve it!

Our team is about 30 ex-MBB consultants, scientists with Ph.D.s in pricing and management science, and data engineers who make sure your pricing strategy does not stop in PowerPoint — it goes to market and wins.

We run proprietary models, frameworks, agents, and tools under **ValueOS**, built from 200+ pricing projects.

For this report, the **AI Value Index (AVI)** and **AVI Pricing Quadrant™** are the next step: pricing logic for the AI era.

Use the frameworks to stress-test your strategy and pick an operating model that fits your sector.

Enjoy!

<div class="vs-chapter-cta" role="complementary" aria-label="Contact Valueships about pricing">
  <a class="vs-chapter-cta__btn" href="https://www.valueships.com/contact">Let's talk about your pricing!</a>
</div>

### The binding constraint: human capabilities

<p class="vs-method-note"><strong>Method (Liebig / constraints):</strong> Interpretive framework linking RCT task gains to firm-level bottlenecks. Not a measured coefficient in this report. The interactive bar chart is illustrative; METR (below) is the empirical counterpoint to "generation speed = productivity."</p>

Have you heard of Liebig's law of the minimum (often misattributed, but the name stuck)? Growth is capped by the scarcest input, not by the inputs you have in surplus. It was quite popular in the *Dune* books; here is the agrarian version. In a field short on potassium, you harvest only what the limiting nutrient allows. In a strategy game with wood and stone to spare but no gold, your settlement stops growing for lack of gold, not lack of lumber.

<figure class="vs-figure vs-figure--liebig-interactive">
<iframe src="assets/liebig-barrel-interactive.html" title="Interactive Liebig chart — click bars to add inputs" width="100%" height="560" loading="lazy"></iframe>
<figcaption><strong>Interactive chart:</strong> each bar is a growth factor; the pink line sits at the shortest bar (<strong>yield</strong> in the classic view; <strong>potential increase in value</strong> when you toggle &ldquo;How it works with AI&rdquo;). Click a bar to add more of that input — surplus elsewhere does not raise the line.</figcaption>
</figure>

Applied to AI adoption today, **compute and model capability are not the limiting factor for most firms. Human capability and attention of using AI is.**

Models draft, summarise, code, and route work quickly. Someone still has to verify output, edit tone, reconcile errors, own accountability, and decide what ships. Silicon Valley engineers running agents at scale report the same operational joke: you still cannot walk away from the laptop or close the lid as agents need supervision, code review, and judgment. You are a resource in scarcity. You simple can't click "allow" that many times. That is not a settings problem alone; it is a **throughput limit on review and trust**. AI accelerates the first mile of work. It does not remove the human from the last mile at enterprise reliability standards.

Similar to this is Goldratt's Theory of Constraints and Liebig's minimum ask the same managerial question from different angles: **do you pour more of the scarce resource into the bottleneck, or redesign the system so the bottleneck stops binding?** Bolting agents onto existing workflows increases demand for the same scarce resource, which is a skilled attention, unless you change roles, handoffs, and what "done" means. 

That is why local task gains of 20 to 40 percent so often fail to show up as firm-level productivity. You simply meet the resource in scarcity or face a huge bottleneck that is not easy to overcome. In other words, we operate to fulfil the system capacity to handle.

A useful diagnostic for any AI program: are we training people to fit the tool (prompting, RAG stacks, agent orchestration inside legacy processes), or rebuilding the production system around what the tool actually does well? **The historical evidence below says only the second path produces step-change gains.**

### The historical productivity ladder

Putting AI's measured macro signal on the same scale as every previous productivity revolution forces the order-of-magnitude question:

<p class="vs-ladder__hint">Tap any wave to expand — methodology, period definition, and sources.</p>

<div class="vs-ladder" aria-label="Historical productivity ladder by wave, oldest to newest">

<details class="vs-ladder__item" id="ladder-agrarian">
<summary class="vs-ladder__row">
<span class="vs-ladder__icon" aria-hidden="true">🌾</span>
<div class="vs-ladder__body">
<strong class="vs-ladder__wave">Agrarian revolution</strong>
<span class="vs-ladder__period">post-1600</span>
<span class="vs-ladder__pct">0.30 %/yr</span>
</div>
</summary>
<div class="vs-ladder__expand">
<p><strong>What the number is.</strong> Indicative annual growth in output per agricultural worker for England after enclosure, crop rotation, and selective breeding had diffused — a pre-industrial baseline for how fast the economy could move before factory industry.</p>
<p><strong>How it was derived.</strong> Long-run historical national accounts from parish, probate, and wage series; pre-1600 data are too sparse for a single %/yr line, so the ladder uses a <em>post-1600</em> benchmark. This is not modern multifactor TFP — it mixes land, labour, and technique without separating capital deepening.</p>
<dl>
<dt>Primary sources on this ladder</dt>
<dd>Hoover Institution desk synthesis of English agrarian productivity estimates [@5] — consolidates Maddison / Allen / Clark-style growth-history benchmarks used in comparative GPT work.</dd>
<dt>Read it as</dt>
<dd>Directional floor (0.30 %/yr), not a precision national-accounts statistic. Every row uses the same %/yr display rule so waves are comparable in spirit, not as identical measurement systems.</dd>
</dl>
</div>
</details>

<details class="vs-ladder__item" id="ladder-first-industrial">
<summary class="vs-ladder__row">
<span class="vs-ladder__icon" aria-hidden="true">🏭</span>
<div class="vs-ladder__body">
<strong class="vs-ladder__wave">First industrial revolution</strong>
<span class="vs-ladder__period">1780–1860</span>
<span class="vs-ladder__pct">0.78 %/yr</span>
</div>
</summary>
<div class="vs-ladder__expand">
<p><strong>What the number is.</strong> Average annual British labour productivity growth across the classic Industrial Revolution — steam, mechanised textiles, iron, and factory discipline replacing artisan production.</p>
<p><strong>How it was derived.</strong> Growth accounting on industrialising Britain: output per worker from national-income reconstructions, decomposed into capital deepening, labour quality, and TFP. Crafts reports roughly <strong>0.78 %/yr</strong> for 1780–1860 — slow by electrification standards, but about <strong>2.6×</strong> the agrarian rung.</p>
<dl>
<dt>Primary source</dt>
<dd>Crafts, N. (2002). <em>Productivity growth in the Industrial Revolution: A new growth-accounting perspective.</em> Federal Reserve Bank of San Francisco [@3] — <a href="https://www.frbsf.org/wp-content/uploads/crafts.pdf" target="_blank" rel="noopener">FRBSF (PDF)</a>.</dd>
<dt>Period note</dt>
<dd>1780–1860 is the standard British mechanised take-off window; the US and continental Europe peak on different calendars.</dd>
</dl>
</div>
</details>

<details class="vs-ladder__item" id="ladder-electric">
<summary class="vs-ladder__row">
<span class="vs-ladder__icon" aria-hidden="true">⚡</span>
<div class="vs-ladder__body">
<strong class="vs-ladder__wave">Electric / 2nd industrial</strong>
<span class="vs-ladder__period">1920–1970</span>
<span class="vs-ladder__pct">2.82 %/yr</span>
</div>
</summary>
<div class="vs-ladder__expand">
<p><strong>What the number is.</strong> Peak-era US labour productivity growth when electrification, motor transport, mass production, and managerial hierarchies were fully embedded — the payoff decades after the dynamo (1880s) and assembly line (1910s).</p>
<p><strong>How it was derived.</strong> Gordon's US productivity waves: the <strong>1920–1970</strong> segment captures the electric / second-industrial payoff at <strong>2.82 %/yr</strong> on this ladder [@4]. David [@6] documents a <strong>30–40 year diffusion lag</strong> between invention and measured macro gains.</p>
<dl>
<dt>Primary sources</dt>
<dd>Gordon, R. J. (2016). <em>The rise and fall of American growth</em> [@4] — US labour-productivity sub-periods.</dd>
<dd>David, P. A. (2001). <em>The transition to a new economy after the Second Industrial Revolution</em> (NBER w8676) [@6].</dd>
<dt>Read it as</dt>
<dd>The benchmark revolution pace in this report: LLM-era AI at 0.09 %/yr is roughly <strong>30× below</strong> this rung.</dd>
</dl>
</div>
</details>

<details class="vs-ladder__item" id="ladder-ict-baseline">
<summary class="vs-ladder__row">
<span class="vs-ladder__icon" aria-hidden="true">📊</span>
<div class="vs-ladder__body">
<strong class="vs-ladder__wave">ICT baseline</strong>
<span class="vs-ladder__period">1970–2015</span>
<span class="vs-ladder__pct">1.38 %/yr</span>
</div>
</summary>
<div class="vs-ladder__expand">
<p><strong>What the number is.</strong> The Solow paradox decades: computers and early digital networks were widely adopted, but US labour productivity stayed modest until the late 1990s — the long J-curve shoulder before the ICT revival.</p>
<p><strong>How it was derived.</strong> Gordon [@4] isolates <strong>1970–2015</strong> as the broad ICT-installation era at about <strong>1.38 %/yr</strong>. Brynjolfsson's J-curve [@2] explains the delay: intangible complements (skills, processes, reorganisation) must accumulate before macro statistics move.</p>
<dl>
<dt>Primary sources</dt>
<dd>Gordon [@4] — ICT baseline sub-period.</dd>
<dd>Brynjolfsson, Rock &amp; Syverson [@2] — productivity J-curve for general-purpose technologies.</dd>
<dd>Broader context: Solow (1987) [@53] and the IT productivity paradox literature.</dd>
</dl>
</div>
</details>

<details class="vs-ladder__item" id="ladder-ict-revival">
<summary class="vs-ladder__row">
<span class="vs-ladder__icon" aria-hidden="true">💻</span>
<div class="vs-ladder__body">
<strong class="vs-ladder__wave">ICT revival</strong>
<span class="vs-ladder__period">1994–2004</span>
<span class="vs-ladder__pct">2.26 %/yr</span>
</div>
</summary>
<div class="vs-ladder__expand">
<p><strong>What the number is.</strong> The measured US productivity resurgence when PCs, email, ERP, barcodes, and internet-era workflow redesign reached the national accounts — the closest historical analogue to technology plus organisational rebuild.</p>
<p><strong>How it was derived.</strong> Gordon [@4] isolates <strong>1994–2004</strong> at roughly <strong>2.26 %/yr</strong> — below the electric peak (2.82 %) but far above the ICT baseline shoulder. Firm-level work shows payoffs where management and skills moved with IT [@2].</p>
<dl>
<dt>Primary sources</dt>
<dd>Gordon [@4] — ICT revival sub-period.</dd>
<dd>Brynjolfsson [@2] — complements and firm-level IT returns.</dd>
<dt>Report link</dt>
<dd>Walmart POS / logistics and Excel-as-control-system examples above illustrate <em>process redesign</em>, not gadget insertion.</dd>
</dl>
</div>
</details>

<details class="vs-ladder__item vs-ladder__item--ai" id="ladder-llm-ai">
<summary class="vs-ladder__row">
<span class="vs-ladder__icon" aria-hidden="true">🤖</span>
<div class="vs-ladder__body">
<strong class="vs-ladder__wave">LLM-era AI</strong>
<span class="vs-ladder__period">2024–2034 (10-year view)</span>
<span class="vs-ladder__pct">0.09 %/yr</span>
</div>
</summary>
<div class="vs-ladder__expand">
<p><strong>What the number is.</strong> Acemoglu's task-based upper bound for how much US TFP and labour productivity could rise over ten years if today's generative-AI task exposure diffuses with moderate complement investments — <strong>not</strong> observed 2024–2026 TFP (macro data still show near zero).</p>
<p><strong>How it was derived.</strong> MIT/NBER task model: occupational task exposure → automation vs augmentation → task-level deltas → economy-wide TFP with capital adjustment. Central moderate scenario: well below 1 % TFP over ten years → roughly <strong>0.09 %/yr</strong> on this ladder [@1].</p>
<dl>
<dt>Primary source</dt>
<dd>Acemoglu, D. (2024). <em>The simple macroeconomics of AI</em> (NBER w32487) [@1] — <a href="https://www.nber.org/papers/w32487" target="_blank" rel="noopener">NBER</a>.</dd>
<dt>Read it as</dt>
<dd>Forward-looking model benchmark for early diffusion. vs electric peak: ~<strong>30× lower</strong>; vs first industrial: ~<strong>8× lower</strong>. Plotted on the speed-normalised chart below.</dd>
</dl>
</div>
</details>

</div>

<!-- VS-SOCIAL-CARD:hero1 -->

Of course it is hard to compare the agrarian revolution to AI when the speed of information was completely different — horse-carriage times versus fiber bandwidth. That is why I normalized every productivity gain against information speed.

Electricity looks like a certain sweet spot: the technology lifted productivity **and** accelerated information speed itself (radio, telephony, broadcast). A snowball effect.

On that lens, AI embedded in today's systems is potentially not groundbreaking — yet. It may change when we build **new** systems around it: agentic platforms that communicate on their own and route work without sitting behind the human review bottleneck.

<div class="vs-chart-mount vs-speed-chart-mount">
<canvas id="vs-productivity-speed-chart" aria-label="Scatter chart: annual productivity gain vs information speed by era; LLM-era AI sits far below the historical trend line"></canvas>
<p class="vs-chart-hint">Hover points for era labels · dashed line = expected trend excluding LLM-era AI · Sources: Crafts [@3], Gordon [@4], Acemoglu [@1].</p>
</div>

Acemoglu's MIT benchmark for LLM-era AI [@1] is **30× below the electrification peak**, **25× below the ICT revival**, and **8× below the first industrial revolution**.

Every prior general-purpose technology had a diffusion lag:

- **Electricity:** ~**30–40 years** from the dynamo (1880s) to the productivity surge (1920s).
- **IT:** ~**20 years** before the paradox broke. In 1987 Robert Solow [@53] wrote in the *New York Times Book Review* that *"you can see the computer age everywhere except in the productivity statistics"* — true until the late-1990s lift.

**LLM-era AI in 2026 is in early diffusion, not at a productivity peak.**

**Information velocity compresses the calendar, not the economics.** Eighteenth-century news moved at horse speed; today it moves at feed speed. Two years of generative AI have generated more headlines than decades of industrial diffusion — yet measured productivity per calendar year is, if anything, **weaker than prior waves relative to capital already committed**. Speed of awareness is not speed of restructuring.

<blockquote class="vs-quote vs-quote--pull">
<p><em>Who wanted to win built a new system around the technology. Who bolted technology onto the old system stayed in the low-teens percent band.</em></p>
</blockquote>

**System redesign, not gadget insertion, separated step-change from incremental gain in every prior wave:**

- **First industrial:** New factories around machines — not steam engines wedged into old workshops.
- **Electrification:** Ford's River Rouge (through 1928) — greenfield for power and moving assembly, not bulbs in a barn.
- **ICT:** Mainframes in the 1970s changed little until PC, email, networked processes, and decentralized management rewired work.
- **Spreadsheets (1980s):** **Excel did not speed old control systems — it enabled new ones** ("power CFOs", consolidated reporting, valuation workflows).
- **Retail ops:** Walmart's early POS, barcodes, and logistics — value followed **process redesign around the tool**, not drop-in automation.
- **Firms (1990s):** Brynjolfsson [@2] — IT payoffs where skills, management, and workflows moved together. His **productivity J-curve** [@2]: complements delay macro gains for years even when micro experiments look strong.

> *"The first rule of any technology used in a business is that automation applied to an efficient operation will magnify the efficiency. The second is that automation applied to an inefficient operation will magnify the inefficiency."* — Bill Gates

LLM-era AI applied locally to today's processes — without role redesign, without new accountability for machine output, without factory-floor logic — lands in the **low-teens percent** band the AVI measures. That is consistent with history. It is uncomfortable relative to **$725 billion** of hyperscaler CapEx projected for 2026 alone [@71].

**Right now we have what I would call "bounded value":** as long as we keep bolting AI onto old systems, we will not unlock what the technology can do. The ceiling is organisational, not algorithmic.

**Want to change the world? Reinvent the shop floor.**

---

## Macro estimates — what the serious models actually say

<p class="vs-method-note"><strong>Method (macro):</strong> Independent macro and meso estimates only (NBER, OECD, IMF, census surveys, peer-reviewed micro-to-macro bridges). No vendor-only ROI decks. Figures match the published sources; the cards state scope where horizons differ (10 yr vs 2040). Key citations: [@1,@8,@11,@12,@14]. Full list in <a href="#avi-references">References (APA)</a>.</p>

Vendor decks rarely agree on one number. Independent macro work does agree on something narrower: **modest near-term TFP and GDP gains**, with upside tied to adoption depth and complement investment — not to today's pilot evidence alone.

<div class="vs-macro-grid" role="figure" aria-label="Macro estimates from independent research on AI productivity and GDP">

<section class="vs-macro-card">
<p class="vs-macro-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 24 L10 18 L16 20 L22 10 L28 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 26 H28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></p>
<p class="vs-macro-card__source"><a href="https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent" target="_blank" rel="noopener">Goldman Sachs Research</a></p>
<p class="vs-macro-card__scope">US GDP to ~2034</p>
<p class="vs-macro-card__signal">~0.4 pp cumulative GDP · up to ~1.5 pp/yr productivity in broad-adoption scenario</p>
<p class="vs-macro-card__implication">Bullish long run, delayed ignition — little measurable GDP impact before ~2027</p>
</section>

<section class="vs-macro-card">
<p class="vs-macro-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6 12 L16 6 L26 12 V22 L16 28 L6 22 Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M12 16 L16 13 L20 16 V20 L16 23 L12 20 Z" stroke="currentColor" stroke-width="1.5"/></svg></p>
<p class="vs-macro-card__source"><a href="https://www.nber.org/papers/w32487" target="_blank" rel="noopener">Acemoglu (MIT, NBER w32487)</a></p>
<p class="vs-macro-card__scope">10 years, task-based</p>
<p class="vs-macro-card__signal">&lt;0.55% TFP · GDP effects &lt;0.9% in moderate exposure</p>
<p class="vs-macro-card__implication">Hard to defend large macro gains from current task exposure alone</p>
</section>

<section class="vs-macro-card">
<p class="vs-macro-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="10" stroke="currentColor" stroke-width="2"/><path d="M4 16 H28 M16 6 C11 11 11 21 16 26 M16 6 C21 11 21 21 16 26" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></p>
<p class="vs-macro-card__source"><a href="https://www.oecd.org/en/publications/miracle-or-myth-assessing-the-macroeconomic-productivity-gains-from-artificial-intelligence_530716f5-en.html" target="_blank" rel="noopener">OECD, <em>Miracle or Myth?</em> (2024)</a></p>
<p class="vs-macro-card__scope">10 years</p>
<p class="vs-macro-card__signal">0.25–0.6 pp/yr TFP · 0.4–0.9 pp/yr labour productivity</p>
<p class="vs-macro-card__implication">Middle of the range — meaningful, not miraculous</p>
</section>

<section class="vs-macro-card">
<p class="vs-macro-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="6" y="18" width="6" height="8" rx="1" stroke="currentColor" stroke-width="2"/><rect x="13" y="12" width="6" height="14" rx="1" stroke="currentColor" stroke-width="2"/><rect x="20" y="6" width="6" height="20" rx="1" stroke="currentColor" stroke-width="2"/></svg></p>
<p class="vs-macro-card__source"><a href="https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier" target="_blank" rel="noopener">McKinsey Global Institute (2023)</a></p>
<p class="vs-macro-card__scope">To 2040</p>
<p class="vs-macro-card__signal">$2.6–4.4T/yr value pool · genAI labour productivity 0.1–0.6%/yr</p>
<p class="vs-macro-card__implication">Large addressable value, thin annual productivity flow</p>
</section>

<section class="vs-macro-card vs-macro-card--wide">
<p class="vs-macro-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="11" r="4" stroke="currentColor" stroke-width="2"/><path d="M8 26 C8 20 11 17 16 17 C21 17 24 20 24 26" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M22 12 L26 8 M26 12 L22 8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></p>
<p class="vs-macro-card__source"><a href="https://www.nber.org/papers/w31161" target="_blank" rel="noopener">Brynjolfsson, Li &amp; Raymond (NBER / <em>QJE</em>)</a></p>
<p class="vs-macro-card__scope">Micro, customer support</p>
<p class="vs-macro-card__signal">14–15% uplift · concentrated in lower-skilled workers</p>
<p class="vs-macro-card__implication">Strong task evidence, slow organisational payback (J-curve)</p>
</section>

</div>

None of these bodies are trying to minimise AI. They are measuring **realized economic throughput** after exposure, adoption, and complementarity — the same object the AVI approximates at sector level. The CapEx line and the productivity line are on different slopes today.

### The CapEx vs productivity math

<p class="vs-method-note"><strong>Method (CapEx chart):</strong> Hyperscaler CapEx ($B/yr) from Statista / Goldman synthesis (2022–2027E). LLM-era productivity (%/yr) from Acemoglu NBER w32487. Different units on dual axes, shown together for contrast, not as a fitted regression. Bain $2T revenue gap and Covello/Hatzius quotes are cited in the text.</p>

Big Tech hyperscaler annual CapEx has gone vertical while measured LLM-era productivity remains stuck near the **0.09 %/yr** Acemoglu benchmark [@1] — two different slopes on the same timeline.

<div class="vs-chart-mount vs-capex-chart-mount">
<canvas id="vs-capex-chart" aria-label="Line chart: hyperscaler CapEx in billions vs LLM-era productivity percent per year, 2022–2027"></canvas>
<p class="vs-chart-hint">Hover for values · toggle series in the legend · CapEx: Statista [@71]; productivity: Acemoglu [@1].</p>
</div>

Bain's 2025 Technology Report [@35] calculates that the sector needs **$2 trillion of new annual revenue by 2030** to fund the announced compute buildout. Combined AI application revenue today is under $50 billion. That is a **40× revenue gap** that has to close through some combination of buyer adoption, pricing expansion, or financial reset.

Goldman Sachs' James Covello — author of *Gen AI: Too Much Spend, Too Little Benefit?* [@9] (June 2024) — said in 2026 that he had been wrong about details but "more convinced" on the central question: AI augments at the margins; the spending is not producing commensurate returns. Hatzius, Goldman's chief economist, has stated publicly that AI's contribution to US GDP in 2025 is "basically zero." Goldman's own data has the ratio that does not math. See <a href="https://www.goldmansachs.com/images/migrated/insights/pages/gs-research/gen-ai--too-much-spend,-too-little-benefit-/TOM_AI%202.0_ForRedaction.pdf" target="_blank" rel="noopener">Goldman Sachs, <em>Gen AI: Too Much Spend, Too Little Benefit?</em> (2024)</a>; <a href="https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out" target="_blank" rel="noopener">Tracking trillions</a> (2026).

### Don't ask the barber if you need a haircut — some quotes from AI moguls

<p class="vs-method-note"><strong>Method (CEO quotes):</strong> Verbatim public claims from hyperscaler and frontier-lab leaders (2024–2026), chosen to show the maximalist narrative. Enterprise cases and macro estimates counter them later. Not a representative sample of CEO speech.</p>

Overselling is part of every CEO's job, and many are very good at it. That is not a moral failure; it is what markets reward. But when a handful of leaders run companies that together make up a large share of the S&P 500, their narratives shape global trade, capital allocation, and even geopolitical risk. We should read those narratives carefully. That is one reason reports like this exist: to stack public claims against measured evidence.

---

## Sector perspective: digging into fragmented evidence

<p class="vs-method-note"><strong>Method (micro → sector):</strong> Task-level evidence (RCTs and field experiments first, surveys second) mapped to **17 sector synthesis lines**. Each AVI row combines **Revenue Impact %**, **Cost Impact %**, and **Revenue/Cost Share of value** (judgment where studies use different units). Formula and calibration: Part II and <a href="#avi-methodology">AVI design &amp; methodology</a>.</p>

The micro evidence is everywhere, and every study measures something different — obviously vertical-oriented metrics. Every consulting firm, think tank, or academic paper has a different number. The fragmentation is simply too high to form a reliable view. That's why I created the AI Value Index (AVI), described in a later part of this report.

Reports remember the **high bound** (20 to 40 percent on a named process). Boards rarely see the **firm-level realized impact** after review, rework, governance, and uneven rollout. That gap is not measurement error alone; it is Liebig's minimum operating in the wild: the scarcest step is no longer "produce the draft" but "stand behind the output."

### What the best articles in the field tell us about AI value

<p class="vs-method-note"><strong>Method (RCT band):</strong> Peer-reviewed or NBER/HBS field experiments with controlled designs. They set the <strong>14–40 % task-level band</strong> used as an input floor for AVI, not firm-level P&L. Citations: [@19,@20,@23,@26,@27,@29] in <a href="#avi-references">References (APA)</a>.</p>

The most rigorous workplace AI studies are randomised controlled trials. They produce a tight range, but it's nowhere close to the overpromised 10× increase. It's a lot, yet it's definitely not that high.

- **Noy & Zhang, 2023 (*Science*)** [@29]: 453 professionals on writing tasks. **37 % time saved, 18 % quality improvement.** Lower-skilled workers gained most.
- **Brynjolfsson, Li & Raymond, 2023 / 2025 (*QJE*)** [@19,@20]: 5,179 customer-support agents at a Fortune 500. **14–15 % average productivity uplift.** 34 % for novices; near-zero for top quintile.
- **Dell'Acqua et al., 2023 (HBS-BCG)** [@23]: 758 BCG consultants. **25 % faster, 12 % more tasks, 40 % higher quality** inside AI's capabilities. **19 percentage points worse** outside them.
- **GitHub Copilot RCT, 2023** [@26]: 95 developers, controlled task. **55 % faster** on a green-field HTTP-server task.
- **METR, 2025** [@27]: 16 experienced open-source developers, 246 real-world tickets. **19 % slower** with AI than without — despite developers reporting they felt 20 % faster.
- **Choi & Schwarcz, 2024** [@22]: Law students, GPT-4. Large speed gain, uneven quality lift.
- **JAMA Open / TPMG, 2024–2025:** AI medical scribes [@39,@45]. **16 minutes saved per 8-hour shift; physician burnout down 13 percentage points in 30 days.**

The convergent band is 14 to 40 percent task-level uplift on AI-fit work, with negative effects when AI is applied to mis-fit tasks. This is the empirical floor of any defensible AI productivity claim.

**METR is the cautionary Liebig case:** experienced developers were **19 percent slower** with AI on real tickets while **believing** they were 20 percent faster. Perceived speed on generation; measured speed after review, debugging, and trust. Any ROI model that counts only the first mile systematically overstates value.

### Sector by sector: 12 industries, mapped

Task-level studies vary by industry, and we can't easily tell what the real value is. Whether it's revenue increase or cost decrease, the signal is highly dispersed. My take was to create the **AI Value Index (AVI)** — which I describe in Part II of this report — as **one clear economic metric** you can use to compare overall value added across sectors. The chart below shows where that lands:

<div class="vs-chart-mount vs-avi-sector-chart-mount">
<canvas id="vs-avi-sector-chart" aria-label="Horizontal bar chart: AVI percent by sector, top industries"></canvas>
<p class="vs-chart-hint">Hover bars for AVI %. Median across 17 sector lines: ~15 %. Only four sectors clear 25 % — the threshold that typically defends outcome-based pricing.</p>
</div>

### An exemplary study: MIT NANDA: 95 percent of pilots produce no P&L

MIT's NANDA initiative published *State of AI in Business 2025* [@37] in August 2025 (150 leader interviews, 350 employee surveys, 300 public deployments):

- **95 %** of enterprise GenAI pilots show **no measurable P&L impact**, on **$30–40B** of enterprise GenAI spend.
- **5 %** of pilots show rapid revenue acceleration.
- RAND (2024) [@38]: **>80 %** pilot failure — about **2×** non-AI IT projects.

McKinsey *State of AI 2025* [@13]:

- Only **39 %** attribute *any* EBIT impact to AI; most of those say **<5 %** of EBIT.
- Function-level wins are real (**10–20 %** cost savings in software, manufacturing, IT).
- Enterprise roll-up still loses to integration, governance, security, and aggregation friction.

### The case studies: the layoff-then-reverse pattern

<p class="vs-method-note"><strong>Method (enterprise cases):</strong> Public filings, earnings calls, and CEO statements (2023–2025). Not independent ROI audits. Selected for layoff → quality regression → partial rehire. Paired with MIT NANDA [@37] and McKinsey [@13] above. See also [@38].</p>

Four enterprise cases now form the public record on AI-driven headcount strategies:

- **Salesforce:** customer support headcount cut from **9,000 to 5,000** in 2025; CEO publicly said "I need less heads"; AI handled 50 % of conversations; support cost down 17 %. By December 2025, the company was publicly walking it back — institutional knowledge loss, complex-case quality regression, rehiring.
- **Klarna:** **700 customer service agents replaced** with OpenAI (2022–2024); claimed 75 % of chat volume automated. By 2025: CSAT dropped, complaints rose. CEO Siemiatkowski: "we focused too much on efficiency." Rehiring underway.
- **IBM:** Krishna's AskHR agent automated **94 percent of routine HR tasks**, displacing ~200 HR roles. **Total IBM headcount went up**, not down — redeployed into engineering, sales, "critical thinking." Public framing evolved from "30 percent replaceable" (2023) to "redeployment, not reduction" (2025).
- **Duolingo:** April 2025 "AI-first" memo triggered immediate backlash — 1,000+ LinkedIn comments, 600 reposts. Within four months, von Ahn clarified that no full-time employees would be laid off. Soft-version Salesforce.

I observe the following pattern. There are some cost-savings gains, yet they are far smaller than promised, and they are usually eaten up by lower quality and increased bottlenecks in the organization. The key reason? They are operating in the old system.

---

## The Value Equation and creation of AI Value Index - one metric to rule them all

<p class="vs-method-note"><strong>Method (frameworks):</strong> Value Equation and AVI follow standard B2B value decomposition (Anderson, Narus & Van Rossum [@54]; Hinterhuber [@56]). Valueships work: calibrating inputs from this meta-analysis, sector normalisation, pricing-band thresholds, and vendor-capture bands. Formula lineage and open vs proprietary detail: <a href="#avi-methodology">AVI design &amp; methodology</a>.</p>

### The Value Equation - pricing science applied in practice

I believe in transparency and in building in public. This report is about **increased value** — and we chose to develop the frameworks **with** AI, not only about it. My working relationship with the models was closer to **professor and student** than to autopilot: I set the brief, the tools produced drafts and iterations, and the reviewing, rejection, and final direction stayed with the author. I think that is a good and ethical way to use AI for research synthesis: accelerate the loop, keep accountability human. For the full iteration log — kernel, asymmetric VII draft, symmetric AVI, and what is open vs Valueships-specific — see [**AVI design & methodology**](#avi-methodology).

Across every sector, every AI use case, every productivity claim, value reduces to two components:

> **Value created by AI  =  Revenue Increase  +  Cost Savings**

<details class="vs-expand" id="avi-value-equation-detail">
<summary class="vs-expand__bar">
<span class="vs-expand__title">Value Equation — definitions &amp; P&amp;L skew</span>
<span class="vs-expand__subtitle">Academic lineage, revenue vs cost, why we normalise</span>
</summary>
<div class="vs-expand__panel">

<p>Same structure as <strong>economic value added</strong> (NOPAT minus a capital charge) and classic B2B value work (Anderson, Narus &amp; Van Rossum [@54]; Hinterhuber [@56]): revenue or margin uplift plus cost reduction, in money terms. AVI applies that split to <strong>AI productivity claims</strong> so sectors compare on one scale.</p>

<ul>
<li><strong>Revenue increase</strong> — % uplift in revenue from AI in the workflow (output, conversion, speed-to-market, targeting).</li>
<li><strong>Cost savings</strong> — % reduction in fully loaded labour or COGS (hours × loaded rate, fewer errors, same-cost throughput).</li>
</ul>

<p>In most B2B cases here, <strong>cost share of value is ~60–80 %</strong> (higher in back-office automation): realised value is still mostly labour and COGS displacement, not net-new revenue. Boards still fund revenue stories more easily than cost avoidance — even when the spreadsheet favours cost. Sales is the main exception where revenue attribution can dominate.</p>

<p><strong>Follow the money, then normalise.</strong> Sector reports celebrate local wins (queues, no-shows, coding speed, fraud) in incompatible units. AVI turns that into <strong>one % per sector</strong> for pricing and investment cases.</p>

</div>
</details>

### The AI Value Index (AVI)

**In one sentence:** AVI is the standard B2B value decomposition (Anderson, Narus & Van Rossum [@54]; Hinterhuber [@56]) applied to AI productivity evidence, with revenue and cost each weighted by its share of realised value — two auditable inputs, one percentage output. What is Valueships-specific is the **calibration for AI** (Revenue/Cost shares from this meta-analysis), the **pricing bands** tied to AVI, and the **vendor capture** sub-index below.

<details class="vs-expand" id="avi-formula-inputs">
<summary class="vs-expand__bar">
<span class="vs-expand__title">Formula &amp; inputs</span>
<span class="vs-expand__subtitle">Weighted average, input table, attribution vs AVI</span>
</summary>
<div class="vs-expand__panel">

<h4 class="vs-minor">The formula</h4>

<blockquote class="vs-quote vs-quote--compact"><p><strong>AVI  =  (Revenue Impact %  ×  Revenue Share of Value)  +  (Cost Impact %  ×  Cost Share of Value)</strong><br><em>Revenue Share + Cost Share = 100 %.</em></p></blockquote>

<p>Each input is a percentage; the output is a percentage on the same scale. The construction is a <strong>symmetric weighted average</strong>: both sides are scaled by their share of total value, so you do not double-count when revenue and cost effects are both large. (An earlier asymmetric draft — revenue at full weight plus cost × share only — was dropped for that reason; expand <strong>AVI design &amp; methodology</strong> below for the iteration log.)</p>

<h4 class="vs-minor">How to read the inputs</h4>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Input</th><th>Meaning</th><th>Typical source in this report</th></tr></thead>
<tbody>
<tr><td><strong>Revenue Impact %</strong></td><td>Uplift in revenue or gross margin attributable to AI in the workflow</td><td>Sector studies, Statista revenue-impact charts, sales/conversion evidence</td></tr>
<tr><td><strong>Cost Impact %</strong></td><td>Reduction in fully loaded labour or COGS attributable to AI</td><td>RCT hours saved, automation rates, McKinsey/Statista cost-decrease bands</td></tr>
<tr><td><strong>Revenue Share of value</strong></td><td>What fraction of <em>total</em> AI value in that sector sits on the revenue side (remainder is cost)</td><td>Synthesised from sector evidence; often 10–40 % in B2B today</td></tr>
<tr><td><strong>Cost Share of value</strong></td><td>Complement of Revenue Share (must sum to 100 %)</td><td>Dominates in most back-office and automation-heavy sectors</td></tr>
</tbody>
</table></div>

<p><strong>Attribution</strong> (used later in the Pricing Quadrant) is separate: it scores how cleanly procurement can tie one outcome unit to your product (0–100 judgment), not whether value exists.</p>

<p><strong>Open vs proprietary (short):</strong> the weighted-average algebra and two-component value split are standard (Anderson, Narus & Van Rossum [@54]; Hinterhuber [@56]; EVA [@75]). Valueships-specific work is <strong>normalising AI evidence</strong> into one AVI %, calibrating Revenue/Cost shares from this source base, linking AVI to pricing bands, and the vendor-capture sub-index.</p>

</div>
</details>

<details class="vs-expand" id="avi-methodology">
<summary class="vs-expand__bar">
<span class="vs-expand__title">AVI design &amp; methodology</span>
<span class="vs-expand__subtitle">Lineage, formula iterations, what we own, limitations</span>
</summary>
<div class="vs-expand__panel">

<p class="vs-expand__lead">The AVI formula is <strong>not a novel invention in abstract value theory</strong>. What this report ships is how it is applied to AI productivity evidence and how inputs are calibrated from 67 sources.</p>

<h4 class="vs-minor">1. Key thesis we started from</h4>

<blockquote class="vs-quote vs-quote--compact"><p><em>Total economic value decomposes into revenue increase and cost savings — the same two-component structure used in B2B value quantification and in economic value added (EVA) thinking, here expressed as auditable percentages.</em></p></blockquote>

<p>Everything else expresses that identity as <strong>percentages on one comparable scale</strong> across sectors.</p>

<h4 class="vs-minor">2. Early asymmetric draft (Statista Research AI)</h4>

<p>An early synthesis proposed a <strong>Value Increase Index (VII)</strong>:</p>

<p><strong>VII = (Revenue Increase %) + (Cost Reduction % × Cost Share of Value)</strong></p>

<p>That weights cost by share but leaves revenue at full weight, which can <strong>overstate</strong> total value when both effects are large. The same pass noted: revenue often ~20–40 % of value, cost reduction ~60–80 % — a pattern this report's sector weights reflect.</p>

<h4 class="vs-minor">3. Symmetric weighted average (AVI, final)</h4>

<p><strong>AVI = (Revenue Impact % × Revenue Share) + (Cost Impact % × Cost Share)</strong>, with Revenue Share + Cost Share = 100 %.</p>

<p>Standard weighted-average decomposition (contribution-margin logic). Renamed <strong>AVI</strong> because "VII" reads as Roman numeral seven in client materials.</p>

<h4 class="vs-minor">4. Academic and finance ancestry (open, citable)</h4>

<p>Each row maps to a live source in <a href="#avi-references">References (APA)</a> — click the superscripts.</p>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Lineage</th><th>Contribution to AVI</th></tr></thead>
<tbody>
<tr><td><strong>Anderson, Narus &amp; Van Rossum (HBR 2006)</strong> [@54]</td><td>B2B value as quantified monetary benefits: revenue/margin, cost, risk, capital. AVI uses the first two; risk/capital inform Revenue Share judgment.</td></tr>
<tr><td><strong>Hinterhuber (2004)</strong> [@56]</td><td>Value-based pricing: sum of quantified customer benefits. AVI is the two-component MVP for AI.</td></tr>
<tr><td><strong>Economic Value Added (Stern Stewart)</strong> [@75]</td><td>Precedent for a single net value metric (NOPAT minus capital charge) — the finance-side analogue of compressing uplift into one number.</td></tr>
<tr><td><strong>Contribution / weighted-average finance</strong> [@54], [@56], [@57]</td><td>Impact × share — standard algebra (contribution-margin logic); not claimed as new math. Hinterhuber (2022) [@57] extends quantified benefits into pricing execution.</td></tr>
</tbody>
</table></div>

<h4 class="vs-minor">5. What Valueships owns in this report</h4>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Element</th><th>Status</th></tr></thead>
<tbody>
<tr><td>Formula shape (symmetric weighted average)</td><td><strong>Open</strong> — reproducible</td></tr>
<tr><td>Normalising fragmented AI metrics into one AVI %</td><td><strong>Valueships</strong> — this meta-analysis</td></tr>
<tr><td>Revenue / Cost Share calibration for AI</td><td><strong>Valueships</strong> — empirical synthesis</td></tr>
<tr><td>AVI → pricing band thresholds (~15 % median, ~25 % outcome)</td><td><strong>Valueships</strong> — operational calibration</td></tr>
<tr><td>Vendor capture (AVI × capture rate; 5–50 % by model)</td><td><strong>Valueships</strong> — value → defensible revenue</td></tr>
</tbody>
</table></div>

<h4 class="vs-minor">6. Formula iteration log</h4>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Version</th><th>Formula</th><th>Problem</th><th>Resolution</th></tr></thead>
<tbody>
<tr><td><strong>v0</strong></td><td>Value = Revenue + Cost</td><td>Correct identity, wrong units for compare</td><td>Express each side as %</td></tr>
<tr><td><strong>v1</strong></td><td>VII = Revenue % + (Cost % × Cost Share)</td><td>Asymmetric</td><td>Weight both sides</td></tr>
<tr><td><strong>v2 (AVI)</strong></td><td>(Rev % × Rev Share) + (Cost % × Cost Share)</td><td>Symmetric weighted average</td><td>Published index</td></tr>
</tbody>
</table></div>

<h4 class="vs-minor">7. Why only two components</h4>

<p>Hinterhuber lists four to six benefit types. For most AI deployments in this evidence set, revenue and cost dominate measurable P&L impact. Regulated workflows are handled via <strong>Premium / outcome zones</strong> in the pricing-by-sector section rather than a six-input master formula. Two inputs fit on a slide and let a CFO challenge each assumption.</p>

<h4 class="vs-minor">8. What AVI does not capture (when to extend)</h4>

<ul class="vs-list">
<li><strong>Risk reduction</strong> — fraud, compliance (material in financial services and legal).</li>
<li><strong>Capital expense savings</strong> — infra or vendor spend retired by AI.</li>
<li><strong>Strategic / option value</strong> — capability monetised later.</li>
<li><strong>Network effects</strong> — compounding ROI over time.</li>
<li><strong>Externalities</strong> — trust, brand, workforce wellbeing.</li>
</ul>

<p>Extend explicitly in engagement work for regulated or capital-heavy cases; do not force into the headline AVI %.</p>

<p class="vs-expand__defense"><strong>One-sentence defense:</strong> <em>The AVI is the standard B2B value decomposition (Anderson, Narus & Van Rossum [@54]; Hinterhuber [@56]) applied to AI productivity claims, with revenue and cost weighted by their share of realised value; the proprietary contribution is AI-specific calibration, cross-sector normalisation, pricing-band thresholds, and vendor capture — not the weighted-average algebra itself.</em></p>

<p class="vs-expand__more">Full research stack (sources, tools, reproducibility): <a href="#avi-methodology-appendix">Full methodology brief: how this report was built</a>.</p>

</div>
</details>

### Sector benchmarks — from AVI % to dollars per employee

AVI gives you a **percentage** you can compare across sectors. Buyers and boards still ask: *what does that mean in money?* This table answers that by translating each sector's AVI into **annual dollars per full-time equivalent (FTE)** — one knowledge worker (or equivalent role) in that industry, on sector-typical loaded labour economics.

**How to read the columns**

| Column | What it means |
| --- | --- |
| **Rev Impact / Cost Impact** | The raw productivity evidence inputs (before weighting) — uplift on revenue and savings on labour or COGS. |
| **Rev Share** | How much of total AI value in that sector sits on the revenue side vs cost (must sum with cost share to 100 %). |
| **AVI** | The blended index: both sides weighted by share — the number you use to compare sectors and set pricing ambition. |
| **Value $/FTE/yr** | **Economic value created** if AVI were fully realised on one FTE: AVI × sector-typical loaded cost per employee per year. Example: 28.6 % AVI on ~$80K loaded back-office labour ≈ **$23K of value per seat per year** — not necessarily cash in year one, but the size of the prize if adoption and restructuring catch up. |
| **Vendor $/FTE/yr** | **Illustrative vendor revenue** at the capture rate typical for that row's pricing band (see Vendor capture below). High-AVI, high-attribution sectors support outcome pricing (~30–50 % capture); subscription bands sit nearer 5–10 %. |
| **Pricing band** | Which pricing model the AVI + attribution profile supports (the section below maps these to the AVI Pricing Quadrant™). |

Rows are **synthesis lines**, not a single company's pilot. Use them to benchmark a sector narrative, stress-test a business case, or see why finance back-office and legal doc review look like outcome zones while education and government look like subscription plays.

<p class="vs-method-note"><strong>Method (benchmark table):</strong> <strong>Value $/FTE/yr</strong> = AVI × sector-typical fully loaded labour cost (higher in legal doc review than education, for example). <strong>Vendor $/FTE/yr</strong> = illustrative capture at the zone's typical rate, not a market price survey. Inputs: sector studies, Statista [@59,@64,@65], RCTs [@19,@29]. Rev/Cost shares use judgment where evidence conflicts.</p>

**Median AVI across 17 sector lines: ~15 percent.** Only four sector lines clear 25 percent (the threshold that defends outcome-based pricing).

<details class="vs-expand" id="avi-sector-benchmark">
<summary class="vs-expand__bar">
<span class="vs-expand__title">Full 17-sector AVI benchmark table</span>
<span class="vs-expand__subtitle">Rev/cost inputs, value per FTE, pricing band</span>
</summary>
<div class="vs-expand__panel">

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Sector</th><th>Rev Impact</th><th>Cost Impact</th><th>Rev Share</th><th><strong>AVI</strong></th><th>Value $/FTE/yr</th><th>Vendor $/FTE/yr</th><th>Pricing band</th></tr></thead>
<tbody>
<tr><td>Finance — back office / ops</td><td>3 %</td><td>30 %</td><td>5 %</td><td><strong>28.6 %</strong></td><td>$22,920</td><td>$6,876</td><td>OUTCOME</td></tr>
<tr><td>Writing / Marketing creative</td><td>12 %</td><td>30 %</td><td>25 %</td><td><strong>25.5 %</strong></td><td>$22,950</td><td>$4,590</td><td>OUTCOME</td></tr>
<tr><td>Manufacturing (lighthouses)</td><td>15 %</td><td>30 %</td><td>35 %</td><td><strong>24.8 %</strong></td><td>$17,325</td><td>$3,465</td><td>OUTCOME</td></tr>
<tr><td>Legal — document review</td><td>5 %</td><td>28 %</td><td>15 %</td><td><strong>24.6 %</strong></td><td>$49,100</td><td>$12,275</td><td>OUTCOME</td></tr>
<tr><td>Software development</td><td>8 %</td><td>25 %</td><td>20 %</td><td><strong>21.6 %</strong></td><td>$28,080</td><td>$5,616</td><td>EFFORT</td></tr>
<tr><td>Consulting / Professional svs</td><td>7 %</td><td>25 %</td><td>25 %</td><td><strong>20.5 %</strong></td><td>$36,900</td><td>$5,535</td><td>EFFORT</td></tr>
<tr><td>TMT — IT functions</td><td>8 %</td><td>22 %</td><td>30 %</td><td><strong>17.8 %</strong></td><td>$21,360</td><td>$3,845</td><td>EFFORT</td></tr>
<tr><td>Sales</td><td>18 %</td><td>10 %</td><td>70 %</td><td><strong>15.6 %</strong></td><td>$17,160</td><td>$4,290</td><td>OUTCOME (rev-attrib.)</td></tr>
<tr><td>Financial services (overall)</td><td>12 %</td><td>18 %</td><td>40 %</td><td><strong>15.6 %</strong></td><td>$18,720</td><td>$3,744</td><td>EFFORT</td></tr>
<tr><td>Healthcare — clinical (scribes)</td><td>5 %</td><td>20 %</td><td>30 %</td><td><strong>15.5 %</strong></td><td>$38,750</td><td>$5,812</td><td>EFFORT</td></tr>
<tr><td>Customer service / support</td><td>5 %</td><td>17 %</td><td>30 %</td><td><strong>13.4 %</strong></td><td>$8,040</td><td>$2,814</td><td>PREMIUM (sub-segment OUTCOME)</td></tr>
<tr><td>Consumer &amp; Retail — sales/ops</td><td>14 %</td><td>12 %</td><td>60 %</td><td><strong>13.2 %</strong></td><td>$9,240</td><td>$1,848</td><td>PREMIUM</td></tr>
<tr><td>AEC / Construction</td><td>8 %</td><td>15 %</td><td>40 %</td><td><strong>12.2 %</strong></td><td>$11,590</td><td>$1,738</td><td>SUBSCRIPTION</td></tr>
<tr><td>Manufacturing (avg plant)</td><td>5 %</td><td>12 %</td><td>30 %</td><td><strong>9.9 %</strong></td><td>$6,930</td><td>$1,040</td><td>SUBSCRIPTION</td></tr>
<tr><td>Government / Public sector</td><td>3 %</td><td>10 %</td><td>10 %</td><td><strong>9.3 %</strong></td><td>$8,370</td><td>$837</td><td>SUBSCRIPTION</td></tr>
<tr><td>Legal — advisory (senior)</td><td>3 %</td><td>10 %</td><td>20 %</td><td><strong>8.6 %</strong></td><td>$30,100</td><td>$3,010</td><td>PREMIUM</td></tr>
<tr><td>Education</td><td>2 %</td><td>8 %</td><td>10 %</td><td><strong>7.4 %</strong></td><td>$5,180</td><td>$414</td><td>SUBSCRIPTION</td></tr>
</tbody>
</table></div>

</div>
</details>

### Vendor capture — what you can charge vs what the customer keeps

<p class="vs-method-note"><strong>Method (capture):</strong> Capture rates (2–50 % of value pool) from Statista [@65,@55] and public list prices (Copilot, Intercom Fin, etc.). Illustrative bands, not a transaction database. Worked example: 300 FTE × $90K loaded.</p>

The sector table's **Value $/FTE/yr** is what AI *creates* for the customer. **Vendor $/FTE/yr** is what you can realistically *charge* — and the two are not the same. Buyers will not hand over 100 % of measured productivity gain; procurement, competition, and attribution risk cap what sticks as vendor revenue.

**Vendor capture** is the share of customer value that becomes your price. In practice most AI vendors today capture only **2–8 % of the customer's underlying labour cost** — even when AVI looks generous. That is why a $30/seat/month Copilot line can still imply a **40×+ ROI** for the buyer: the value pool is large; the vendor's take is small.

<details class="vs-expand" id="avi-vendor-capture">
<summary class="vs-expand__bar">
<span class="vs-expand__title">Capture rates, formula &amp; worked example</span>
<span class="vs-expand__subtitle">Per-seat vs outcome pricing on 300 FTE</span>
</summary>
<div class="vs-expand__panel">

<p><strong>Core formula:</strong></p>

<blockquote class="vs-quote vs-quote--compact"><p><strong>Vendor revenue ≈ AVI × loaded labour cost × capture rate</strong><br><em>(per FTE per year, or roll up by headcount)</em></p></blockquote>

<p><strong>Capture rate</strong> = what fraction of the <em>value pool</em> (AVI × labour cost) you convert into price. It rises when pricing is tied to a clean outcome unit (resolved ticket, closed deal, completed review) and falls when you sell a generic seat or token bundle.</p>

<p><strong>Typical capture rates by pricing model</strong></p>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Pricing model</th><th>Capture rate (of value pool)</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Per-seat / subscription</td><td>5–10 %</td><td>Floor — easy to buy, hard to prove ROI per seat (e.g. Copilot at ~$30/seat/mo)</td></tr>
<tr><td>Usage / token / credit</td><td>10–25 %</td><td>Metered — Cursor, Replit, API-style products</td></tr>
<tr><td>Effort / complexity tiers</td><td>20–35 %</td><td>Work units priced (Devin ACUs, Lovable tiers)</td></tr>
<tr><td><strong>Outcome-based</strong></td><td><strong>30–50 %</strong></td><td>Ceiling when attribution is clean (e.g. Intercom Fin per resolution)</td></tr>
<tr><td>Gainsharing</td><td>20–40 %</td><td>High upside, high dispute risk on what was "caused" by AI</td></tr>
</tbody>
</table></div>

<p><strong>Worked example — same customer, three pricing postures</strong></p>

<p>Assume <strong>300 knowledge workers</strong>, <strong>$90K fully loaded cost</strong> each → <strong>$27M</strong> annual labour base. At <strong>20 % AVI</strong>, AI creates about <strong>$5.4M/year</strong> of economic value (<em>if</em> realised). How much of that becomes vendor revenue?</p>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Pricing posture</th><th>Capture rate</th><th>Vendor revenue / yr</th><th>Vendor take as % of labour cost</th><th>Buyer ROI multiple</th></tr></thead>
<tbody>
<tr><td>Per-seat at $30/seat/mo (~$360/yr × 300)</td><td>~2 % of value pool</td><td>~$108K</td><td><strong>~2 %</strong></td><td><strong>~49×</strong> — buyer keeps almost all value</td></tr>
<tr><td>Hybrid base + usage (20 % capture)</td><td>20 %</td><td>~$1.08M</td><td><strong>~4 %</strong></td><td><strong>~4×</strong> — still strong buyer economics</td></tr>
<tr><td>Outcome-based, Intercom-style (40 % capture)</td><td>40 %</td><td>~$2.16M</td><td><strong>~8 %</strong></td><td><strong>~3×</strong> — vendor earns more; buyer still wins</td></tr>
</tbody>
</table></div>

<p><strong>How to read the last two columns:</strong> <em>Vendor take as % of labour cost</em> is your price divided by the customer's payroll — the number boards recognise. <em>Buyer ROI multiple</em> is value created ÷ vendor revenue — values above 3× usually pass procurement; values above 10× explain why cheap per-seat AI can still look like a bargain even when AVI is "only" 15–20 %.</p>

<p>Statista's AI pricing synthesis puts realised vendor capture in the <strong>2–6 % of labour cost</strong> band for most deployments today. This calculator is calibrated to that range — not to the headline AVI % alone.</p>

</div>
</details>

### Why the value-equation answer matters for pricing

<details class="vs-expand" id="avi-reframe-playbook">
<summary class="vs-expand__bar">
<span class="vs-expand__title">Revenue-side reframe playbook</span>
<span class="vs-expand__subtitle">Cost → revenue language before the pricing page</span>
</summary>
<div class="vs-expand__panel">

<p>Roughly 80 percent of measured AI value in the underlying synthesis is on the cost side. Pricing science (Anderson, Narus &amp; Van Rossum [@54]; Hinterhuber [@56]) is unambiguous that B2B buyers respond to revenue-impact framings more strongly than cost-saving framings. Cost-saving language is perceived as commodity; revenue language passes through procurement because it ties to the buyer's own performance metrics. The reframe playbook turns cost-side findings into revenue-capacity arguments before they reach the pricing page:</p>

<div class="vs-table-wrap"><table class="vs-table">
<thead><tr><th>Cost-side raw</th><th>Revenue-side reframe</th></tr></thead>
<tbody>
<tr><td>"Saves the team 14 hours per week"</td><td>"Lets you serve 8 % more customers without hiring"</td></tr>
<tr><td>"Faster doc review"</td><td>"Higher deal velocity, more deals closed per quarter"</td></tr>
<tr><td>"Less physician burnout"</td><td>"One additional patient every two weeks per clinician (~$6,500/yr/MD)"</td></tr>
<tr><td>"Fewer manufacturing defects"</td><td>"More yield to sell at the same fixed cost"</td></tr>
</tbody>
</table></div>

<p>This is the structural commercial weakness of most current AI pricing narratives — and the single highest-leverage edit on any AI pricing page today.</p>

</div>
</details>

---

## Pricing implications by sector

<p class="vs-method-note"><strong>Method (pricing):</strong> Pricing zones combine AVI (Part II) with an <strong>attribution score (0–100)</strong>: expert judgment on whether procurement can audit one outcome unit per sector. Not a statistical estimate. Outcome ★ thresholds: AVI ≥ ~15 % and attribution ≥ ~70 (see axis table). Buyer preference: Statista 2025 [@66].</p>

### The AVI Pricing Quadrant™

Part II answered *how much* value AI creates by sector (AVI % and dollars per FTE). This section answers the next question: **which pricing model can you defend?** Not "add 20 % because it is AI," but outcome, effort/credits, premium seat-plus-bonus, or subscription.

The **AVI Pricing Quadrant™** plots each sector on two scores:

1. **AVI (horizontal):** size of the economic prize if value is realised. Below ~15 %, AI still reads as a productivity tool in the benchmark; at 15 %+, the value pool supports bolder packaging.
2. **Revenue attribution (vertical):** whether procurement accepts a *single attributable unit* tied to your product (resolved ticket, closed deal, reviewed document, fraud case avoided). High AVI with low attribution is common: large value, weak proof.

Chart position maps to **one of four pricing zones**, each with a typical **capture band** (share of value that becomes vendor revenue; see Vendor capture above). The chart below shows **17 sectors as bubbles**: position = AVI × attribution; **bubble size = value $/FTE/yr** from the sector table.

**Headline results**

- **Outcome ★ (high AVI, high attribution):** **five** sector lines: finance back-office, marketing creative, manufacturing lighthouses, legal document review, and sales *when* conversion ties to a clean unit. Rare cases where **outcome or gainsharing at 30–50 % capture** holds up economically.
- **Effort (high AVI, low attribution):** **five** sectors: software development, consulting, TMT IT, financial services overall, healthcare clinical (scribes). Large value pools (healthcare **~$39K value/FTE/yr**), but no single auditable outcome, so vendors use **credits, consumption, or complexity tiers** (10–25 % capture).
- **Premium (moderate AVI, cleaner attribution):** **three** sectors: customer service, consumer & retail, legal senior advisory. Seat-plus-bonus or hybrid (10–20 % capture): attribution is good enough for a bonus tier; AVI stays below the outcome band.
- **Subscription (lower AVI, weak attribution):** **four** sectors: AEC/construction, average manufacturing plant, government, education. Per-seat with usage caps (5–10 % capture). Measured AVI and provable attribution in the public evidence both stay modest.

**Median AVI ≈ 15 %:** horizontal split between subscription/premium and effort/outcome. **Only four sectors clear 25 % AVI**; outcome pricing still needs attribution (legal advisory: decent AVI, attribution too fuzzy for pure outcome).

| Axis | Low | High |
| --- | --- | --- |
| **AVI** (horizontal) | &lt;15 %: productivity tool band | ≥15 %: material value band |
| **Revenue attribution** (vertical) | Hard to tie one outcome unit to the product | Clean trace from product → revenue or cost line |

<div id="vs-vpq-chart" class="vs-vpq-chart-mount"></div>

<div class="vs-vpq-zones">
<div class="vs-vpq-zone-card vs-vpq-zone-card--outcome"><strong>Outcome ★</strong><span>High AVI · High attribution</span><em>Outcome / gainsharing · 30–50 %</em></div>
<div class="vs-vpq-zone-card vs-vpq-zone-card--effort"><strong>Effort</strong><span>High AVI · Low attribution</span><em>Credits / consumption · 10–25 %</em></div>
<div class="vs-vpq-zone-card vs-vpq-zone-card--premium"><strong>Premium</strong><span>Low AVI · High attribution</span><em>Per-seat + bonus · 10–20 %</em></div>
<div class="vs-vpq-zone-card vs-vpq-zone-card--subscription"><strong>Subscription</strong><span>Low AVI · Low attribution</span><em>Per-seat + cap · 5–10 %</em></div>
</div>

#### Sector placement

| Sector | AVI | Attribution | Zone | Pricing model | Capture band |
| --- | ---: | ---: | --- | --- | --- |
| Finance back-office | 28.6 % | 88 | Outcome ★ | Outcome / gainsharing | 30–50 % |
| Marketing creative | 25.5 % | 76 | Outcome ★ | Outcome / gainsharing | 30–50 % |
| Manufacturing lighthouses | 24.8 % | 82 | Outcome ★ | Outcome / gainsharing | 30–50 % |
| Legal document review | 24.6 % | 74 | Outcome ★ | Outcome / gainsharing | 30–50 % |
| Software development | 21.6 % | 38 | Effort | Credits / consumption | 10–25 % |
| Consulting | 20.5 % | 42 | Effort | Credits / consumption | 10–25 % |
| TMT IT | 17.8 % | 40 | Effort | Credits / consumption | 10–25 % |
| Sales (clean conversion attrib.) | 15.6 % | 92 | Outcome ★ | Outcome / gainsharing | 30–50 % |
| FinServ overall | 15.6 % | 44 | Effort | Credits / consumption | 10–25 % |
| Healthcare (clinical / scribes) | 15.5 % | 36 | Effort | Credits / consumption | 10–25 % |
| Customer service (overall) | 13.4 % | 68 | Premium | Per-seat + outcome bonus | 10–20 % |
| Consumer & retail | 13.2 % | 72 | Premium | Per-seat + outcome bonus | 10–20 % |
| AEC / construction | 12.2 % | 32 | Subscription | Per-seat + usage cap | 5–10 % |
| Manufacturing (average plant) | 9.9 % | 28 | Subscription | Per-seat + usage cap | 5–10 % |
| Government | 9.3 % | 18 | Subscription | Per-seat + usage cap | 5–10 % |
| Legal senior advisory | 8.6 % | 58 | Premium | Per-seat + outcome bonus | 10–20 % |
| Education | 7.4 % | 22 | Subscription | Per-seat + usage cap | 5–10 % |

#### Reading the placement: what the 17 rows imply

**Five sectors in Outcome ★**, **five in Effort**, **three in Premium**, **four in Subscription**. The central story: **outcome pricing is the exception**, even in AI-hyped categories.

**Outcome cluster** — AVI ≥ ~15 %, attribution ≥ ~70. Outcome or gainsharing works when procurement can audit *one unit* tied to your product. Proof beats headline AVI.

- **Finance back-office** — 28.6 % AVI · attribution 88 · exceptions cleared, reconciliations automated.
- **Legal document review** — 24.6 % · 74 · documents reviewed, hours per matter.
- **Manufacturing lighthouses** — 24.8 % · high attribution · throughput and defect metrics on redesigned lines.
- **Marketing creative** — 24 %+ AVI · measurable campaign / asset output.
- **Sales** (edge case) — 15.6 % AVI · attribution 92 · only when **conversion** is the contracted unit.

**Only four sectors clear 25 % AVI** (finance, marketing, mfg lighthouses, legal doc review). That is the band where outcome pricing stops sounding aspirational.

**Effort cluster** — high AVI, low attribution. Large value pools, no single auditable outcome → credits, consumption, complexity tiers (typical capture 10–25 %).

- **Software development** — 21.6 % AVI · attribution 38 · heterogeneous work product → Cursor-style metering.
- **Consulting** — 20.5 % · 42 · real RCT uplift, hard to contract on one deliverable.
- **Financial services (overall)** — 15.6 % · 44 · front office may be provable; the sector aggregate is not.
- **Healthcare clinical (scribes)** — 15.5 % · 36 · ~$39K value/FTE in the table, but liability and mixed workflows block clean outcome contracts.
- **TMT / IT** — same pattern (see table).

**Premium cluster** — moderate AVI, cleaner attribution. Seat-plus-bonus or hybrid (10–20 % capture), not full gainsharing.

- **Customer service** — 13.4 % AVI · attribution 68 · bonus on deflected contacts or handle time, not whole P&amp;L.
- **Consumer &amp; retail** — 13.2 % · 72 · similar hybrid logic.
- **Legal senior advisory** — 8.6 % · 58 · attribution does not rescue low AVI; premium seat, not outcome.

**Subscription cluster** — lower AVI, weak attribution. Per-seat + usage caps (5–10 % capture); vendor $/FTE often under **$1K/yr** at typical rates.

- **Government** — 9.3 % AVI · attribution 18.
- **Education** — 7.4 % · 22.
- **Manufacturing (average plant)** — 9.9 % · diffuse value, procurement rigidity.
- **AEC / construction** — same band (see table).

**Manufacturing twice on purpose**

- **Lighthouses** — 24.8 % AVI · Outcome ★ · process rebuilt for AI.
- **Average plant** — 9.9 % · Subscription · tool bolted onto legacy workflow.

Same lesson as Part I: value sits where the production system was redesigned, not where the model was dropped in.

Use the table above for exact numbers on a pricing page, RFP, or sector pitch. The chart is the same data in two dimensions.

### Buyer-side pricing preference

<p class="vs-method-note"><strong>Method (buyer survey):</strong> Statista (2025) [@66]: share of enterprises that <em>prefer</em> each pricing model for agentic AI tools. Multi-select allowed; percentages are not mutually exclusive. Stated preference, not contract terms. Compared to the Quadrant's sector-by-sector model choice.</p>

The quadrant picks the *economically defensible* model. Buyer preference picks what *closes*. Statista's 2025 survey [@66] on preferred pricing models for agentic AI shows a systematic gap between vendor narrative and procurement reality:

<div class="vs-buyer-bars" role="figure" aria-label="Enterprise preference for agentic AI pricing models, Statista 2025">
<div class="vs-buyer-bars__row vs-buyer-bars__row--lead"><span class="vs-buyer-bars__label">Consumption-based</span><span class="vs-buyer-bars__track"><span class="vs-buyer-bars__fill" style="width:55%"></span></span><span class="vs-buyer-bars__pct">55 %</span></div>
<div class="vs-buyer-bars__row"><span class="vs-buyer-bars__label">Platform-based</span><span class="vs-buyer-bars__track"><span class="vs-buyer-bars__fill" style="width:43%"></span></span><span class="vs-buyer-bars__pct">43 %</span></div>
<div class="vs-buyer-bars__row"><span class="vs-buyer-bars__label">License-based</span><span class="vs-buyer-bars__track"><span class="vs-buyer-bars__fill" style="width:37%"></span></span><span class="vs-buyer-bars__pct">37 %</span></div>
<div class="vs-buyer-bars__row"><span class="vs-buyer-bars__label">Tier-based</span><span class="vs-buyer-bars__track"><span class="vs-buyer-bars__fill" style="width:33%"></span></span><span class="vs-buyer-bars__pct">33 %</span></div>
<div class="vs-buyer-bars__row vs-buyer-bars__row--outcome"><span class="vs-buyer-bars__label">Outcome-based</span><span class="vs-buyer-bars__track"><span class="vs-buyer-bars__fill vs-buyer-bars__fill--muted" style="width:17%"></span></span><span class="vs-buyer-bars__pct">17 %</span></div>
<p class="vs-buyer-bars__source">Source: <a href="https://www.statista.com/statistics/1620734/adoption-of-pricing-models-for-agentic-ai-tools/" target="_blank" rel="noopener">Statista (2025)</a> [@66]. Enterprises preferring each model for agentic AI tools.</p>
</div>

<div class="vs-pricing-gap" role="figure" aria-label="Gap between buyer pricing preference and vendor outcome narrative">
<p class="vs-pricing-gap__title">The 3× mismatch: buyer preference vs vendor pitch</p>

<div class="vs-pricing-gap__stats">
<div class="vs-pricing-gap__stat vs-pricing-gap__stat--buyer">
<p class="vs-pricing-gap__stat-label">Enterprises preferring consumption / usage</p>
<p class="vs-pricing-gap__stat-num">55%</p>
<p class="vs-pricing-gap__stat-sub">#1 buyer choice (Statista 2025)</p>
</div>
<div class="vs-pricing-gap__ratio" aria-hidden="true">
<span class="vs-pricing-gap__ratio-num">3.2×</span>
<span class="vs-pricing-gap__ratio-label">Consumption lead over outcome</span>
</div>
<div class="vs-pricing-gap__stat vs-pricing-gap__stat--outcome">
<p class="vs-pricing-gap__stat-label">Enterprises preferring outcome-based</p>
<p class="vs-pricing-gap__stat-num">17%</p>
<p class="vs-pricing-gap__stat-sub">Buyers want predictability; attribution is hard</p>
</div>
</div>

<p class="vs-pricing-gap__bars-title">Same scale: preferred pricing models (% of enterprises)</p>
<div class="vs-pricing-gap__bar-row">
<span class="vs-pricing-gap__bar-label">Consumption</span>
<span class="vs-pricing-gap__bar-track"><span class="vs-pricing-gap__bar-fill vs-pricing-gap__bar-fill--consumption" style="width:55%"></span></span>
<span class="vs-pricing-gap__bar-pct">55%</span>
</div>
<div class="vs-pricing-gap__bar-row">
<span class="vs-pricing-gap__bar-label">Outcome</span>
<span class="vs-pricing-gap__bar-track"><span class="vs-pricing-gap__bar-fill vs-pricing-gap__bar-fill--outcome" style="width:17%"></span></span>
<span class="vs-pricing-gap__bar-pct">17%</span>
</div>

<div class="vs-pricing-gap__align">
<p class="vs-pricing-gap__align-card vs-pricing-gap__align-card--quad"><strong>5 of 17</strong> sectors in Outcome ★ on the AVI quadrant: outcome / gainsharing fits the economics (~29 % of benchmark rows)</p>
<p class="vs-pricing-gap__align-card vs-pricing-gap__align-card--buyer"><strong>17%</strong> of buyers prefer outcome pricing. Vendor decks often lead with the opposite story.</p>
</div>

<p class="vs-pricing-gap__rule"><strong>Pricing-page rule:</strong> Lead with consumption or hybrid (what most buyers want). Reserve outcome / gainsharing for Outcome ★ sectors and attribution-mature accounts, not as the default headline.</p>
</div>

### The 10× pricing test

A vendor can defensibly charge 10× their non-AI predecessor only if one of five conditions holds:

1. **Scarce specialist labour replacement** — senior radiologist, M&A partner, ML scientist — when AI quality reaches that level on the specific task.
2. **Revenue-generating outcome with clean attribution** — conversion lift, fraud recovery — where procurement accepts the attribution.
3. **Bottleneck / capacity unlock** — drug discovery cycle, M&A diligence — where time-to-market value dwarfs the price.
4. **Regulated workflow with liability** — AML/KYC, SOX, medical documentation — insurer-style premium where AI assumes risk.
5. **Mission-critical reliability with HITL** — narrow domains where the alternative is unacceptable.

Outside these five conditions, the 14–40 percent RCT evidence does not support 10× pricing. For the 95 percent of knowledge work that sits outside them, defensible pricing follows the AVI band.

### Labour productivity implications

This report's macro evidence supports a specific labour story:

- **Aggregate labour displacement is much smaller than maximalist claims**, and reversing in public where it happened (Salesforce, Klarna).
- **Skill compression is real:** the most rigorous RCTs (Brynjolfsson, Noy/Zhang, Dell'Acqua) all find AI lifts low-skill workers most and provides little or negative uplift to high-skill workers. The wage implication: AI is a wage-compressor in the short run.
- **Total headcount tends to stay flat or rise** when AI is applied to back-office routine (IBM AskHR is the cleanest case). The Salesforce strategy of cutting headcount in proportion to AI deployment is empirically failing.
- **Hourly billing models compress slowly:** Statista [@63] shows only 44 percent of respondents expect hourly billing to shrink in the next five years. AI changes pricing model mix gradually, not abruptly.

The right narrative for the labour question: **AI moves productive workers faster on the AI-fit slice of their work; it does not yet replace the workforce at scale; and the firms that bet on full replacement are publicly walking it back.**

### Why scale may still fail: political and social friction

<p class="vs-method-note"><strong>Method (political friction):</strong> Historical comparison plus Duolingo, Salesforce, and Klarna cases. Interpretive thesis on adoption ceilings; not modelled in AVI or the Quadrant.</p>

Technology curves and AVI math are not enough for civilisation-scale adoption. **Displacement has a balance sheet outside the firm.**

| Era | What happened |
| --- | --- |
| **19th century** | Clearing workshops: low political cost, thin social insurance. |
| **21st century** | Hyperscaler / SaaS at scale: halving headcount on an AI story triggers brand risk, regulators, unions, customers, and fiscal cost of displaced taxpayers. |

**Public cases:**

- **Duolingo (2025):** "AI-first" memo → backlash → clarification that no full-time roles would go (soft version).
- **Salesforce, Klarna:** Cuts → service quality hit → rehiring (hard version).

That friction does not mean AI fails. It means the feasible path is **augmentation, redeployment, and system redesign** — not headline layoffs as the main value-capture move. GTM that sells "replace your team" fights the constraint; GTM that sells "more capacity per FTE" aligns with it.

This report stops at the economic and commercial boundary. Labour institutions, tax, and democratic response need a separate note. Forward thesis: **even if models improve, realized value can stay capped until political and social systems absorb displacement as cheaply as nineteenth-century factories did — and they do not today.**

---

## Conclusion

### What the evidence actually says

After normalising **67 sources** [@1,@12,@19,@37,@66] onto one scale, one picture holds — and it is uncomfortable for the maximalist story.

<div class="vs-evidence-grid" role="list" aria-label="Summary of what the evidence says">

<article class="vs-evidence-card" role="listitem">
<p class="vs-evidence-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="11" stroke="currentColor" stroke-width="2"/><path d="M8 20 L16 10 L24 18" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 24 H22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></p>
<p class="vs-evidence-card__label">Macro</p>
<p class="vs-evidence-card__body">LLM-era AI sits near <strong>0.09 %/yr</strong> productivity in credible models [@1], against <strong>$725 billion+</strong> of hyperscaler CapEx [@71] in 2026. Prior GPT waves looked weak early too — none had this much capital committed this soon relative to measured throughput.</p>
</article>

<article class="vs-evidence-card" role="listitem">
<p class="vs-evidence-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="7" y="8" width="18" height="16" rx="2" stroke="currentColor" stroke-width="2"/><path d="M11 14 h10 M11 18 h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M16 6 v3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></p>
<p class="vs-evidence-card__label">Task level</p>
<p class="vs-evidence-card__body">Rigorous RCTs cluster around <strong>14–40 %</strong> uplift [@19,@29,@23] on AI-fit work — real, repeatable, worth buying at the task boundary.</p>
</article>

<article class="vs-evidence-card" role="listitem">
<p class="vs-evidence-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="6" y="14" width="8" height="12" rx="1" stroke="currentColor" stroke-width="2"/><rect x="13" y="10" width="8" height="16" rx="1" stroke="currentColor" stroke-width="2"/><rect x="20" y="6" width="6" height="20" rx="1" stroke="currentColor" stroke-width="2"/></svg></p>
<p class="vs-evidence-card__label">Firm &amp; sector</p>
<p class="vs-evidence-card__body">Median <strong>AVI ~15 %</strong> [@73] — meaningful, not revolutionary. Only <strong>four of seventeen</strong> sectors clear <strong>25 % AVI</strong>. MIT NANDA [@37], McKinsey [@13], and layoff-then-reverse cases (Salesforce, Klarna, IBM): pilots rarely reach P&amp;L when review and bottlenecks bind.</p>
</article>

<article class="vs-evidence-card" role="listitem">
<p class="vs-evidence-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 12 h16 v12 H8 z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M12 12 V9 a4 4 0 0 1 8 0 v3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="16" cy="18" r="2" fill="currentColor"/></svg></p>
<p class="vs-evidence-card__label">Pricing</p>
<p class="vs-evidence-card__body">Value created ≠ value captured. Vendors often realise <strong>2–8 % of customer labour cost</strong> [@65,@55] as revenue. Buyers prefer <strong>consumption / hybrid (55 %)</strong> over <strong>outcome (17 %)</strong> [@66] by ~<strong>3×</strong> — while decks still sell outcome. Quadrant [@74]: only <strong>five sectors</strong> in Outcome ★.</p>
</article>

<article class="vs-evidence-card vs-evidence-card--punchline" role="listitem">
<p class="vs-evidence-card__icon" aria-hidden="true"><svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16 4 L19 12 L28 13 L21 19 L23 28 L16 23 L9 28 L11 19 L4 13 L13 12 Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg></p>
<p class="vs-evidence-card__label">Bottom line</p>
<p class="vs-evidence-card__body">The point is not &ldquo;AI fails.&rdquo; <strong>Gross AI can look like a revolution; net AI inside unrestructured organisations behaves like a strong productivity tool</strong> — bounded by human attention, proof of attribution, and the political cost of displacement.</p>
</article>

</div>

### What to do with it

**If you sell AI or AI-augmented services**

1. **Price the sector's AVI band, not the keynote.** Anchor every business case in revenue + cost decomposition (Value Equation → AVI), not in "10×" language the macro math and public case studies do not support.
2. **Choose the model from the Quadrant, not from LinkedIn.** AVI × attribution → Outcome, Effort, Premium, or Subscription. One decision, defensible in procurement.
3. **Lead the pricing page with what buyers want.** Consumption or hybrid first; outcome / gainsharing as a tier for attribution-mature accounts in Outcome ★ sectors, not as the default headline.
4. **Reframe cost-side wins as revenue capacity** before procurement sees them. Eighty percent of measured value is cost-side; buyers still fund revenue stories more easily.
5. **Design for the Liebig minimum.** Until workflows are rebuilt, not just tool-inserted, expect **low-teens percent** firm-level gains, not civilisation-scale jumps. Price and promise accordingly.

**If you buy or govern AI spend**

1. **Demand one comparable metric** (AVI or equivalent) across vendors and pilots. Hours saved alone is not a strategy metric.
2. **Separate pilot uplift from P&L impact** before you scale seat count or cut roles; the case studies in this report are the control group.
3. **Treat CEO maximalism as positioning**, not as your workforce plan, until independent measurement and restructuring catch up.
4. **Negotiate predictability.** The market prefers meters and caps; outcome contracts only where attribution is auditable.

**The 10× test still applies**, but narrowly: scarce expert labour replacement, clean revenue attribution, bottleneck unlock, regulated liability, or mission-critical HITL domains. Outside those five conditions, defensible pricing follows the AVI band and the capture math in this report, not the hype cycle.

### Why I have created this report? tl;dr for myself

Vendors need a pricing story that survives the next board cycle. Buyers need a filter for claims that all use different numerators. Both need the same vocabulary: **value created (AVI), value captured (pricing model × capture rate), and proof (attribution).**

This synthesis is tied to evidence, normalised by sector, and built to survive the next press release. When the numbers move (and they will, as adoption and restructuring deepen), update the AVI inputs; the framework should not need to be reinvented.

**A practitioner's check.** Valueships has spent on the order of one million PLN on AI tooling, automation, and workflow experiments to date. Uplift is real in specific workflows (research synthesis, draft generation, pricing analytics) and invisible in others once integration, review time, and uneven adoption are netted out. That uneven distribution is itself evidence of Liebig's minimum: the constraint is not whether the model can draft; it is whether the organisation can absorb, verify, and commercialise output at scale.

> **Inside unrestructured organisations, AI remains a productivity tool, capped today by human attention, organisational design, and the social cost of displacement. Price it that way and you will still win. Price it as magic and the next earnings call will correct you.**

---

## Full methodology brief: how this report was built

**Research question:** What economic value does AI deliver in production today, on a common denominator, and what does that imply for B2B pricing?

**Approach:** Desk meta-analysis of **67 primary and secondary sources** (May 2026): RCTs and field experiments, macro and sector studies, consulting surveys, Statista charts, enterprise case evidence, and documented maximalist public claims, normalised into **AVI** and the **AVI Pricing Quadrant™**. External research is the data; Valueships frameworks structure the narrative.

Method notes and superscript citations appear in each chapter. This appendix holds the map, glossary, limits, and the numbered <a href="#avi-references">reference list</a>.

### Where methodology lives in this report

| Topic | What we did | Where in the report |
| --- | --- | --- |
| Source corpus | 74 numbered sources; live URL check at publication | Foreword; <a href="#avi-references">References (APA)</a> |
| Historical ladder | Directional %/yr synthesis across eras | Historical productivity ladder |
| Macro estimates | Independent models only; scope per card | Macro estimates |
| Task-level band | RCT / field experiment priority | Sector perspective → RCT section |
| Sector AVI | Rev/Cost inputs + weighted AVI formula | Part II; sector benchmark table |
| Attribution & zones | Expert scores 0–100; zone thresholds | Pricing implications → Quadrant |
| Buyer preference | Statista 2025 (stated preference) | Buyer-side pricing preference |
| CEO maximalism | Selected public quotes vs measured evidence | Barber / moguls section |
| CapEx vs productivity | Dual-axis synthesis (CapEx $ vs %/yr TFP) | CapEx vs productivity math |
| Liebig / bottlenecks | Interpretive + METR counterpoint | Binding constraint; RCT section |
| Enterprise cases | Public disclosures; pattern sample | Case studies (layoff-then-reverse) |
| Vendor capture | Statista + list-price bands | Vendor capture expander |
| Political friction | Interpretive adoption ceiling | Why scale may still fail |
| Formula defence | Lineage, iterations, open vs proprietary | Part II → [AVI design & methodology](#avi-methodology) |

### Glossary

| Term | Meaning |
| --- | --- |
| **Value Equation** | Value from AI = revenue increase + cost savings (before normalisation). |
| **AVI (AI Value Index)** | One percentage per sector: (Revenue impact % × Revenue share) + (Cost impact % × Cost share). Median in this synthesis ≈ **15 %**. |
| **Attribution** | How cleanly procurement can tie one outcome unit to your product (separate from whether value exists). |
| **AVI Pricing Quadrant™** | Plot AVI vs attribution → one of four pricing models (Outcome, Effort, Premium, Subscription). |

### Sources and verification

Peer-reviewed papers and NBER working papers; OECD, IMF, and central-bank research; consulting macro studies (used critically); **13 Statista charts** integrated where noted; enterprise case studies (Salesforce, Klarna, IBM, Duolingo); and Valueships proprietary framework documentation. Every URL in the reference list was checked live at time of publication.

### Human judgment (explicit)

- **Revenue / Cost Share of value** per sector when studies use incompatible units or mix revenue with cost savings.
- **Attribution scores (0–100)** for the Pricing Quadrant: procurement-auditability judgment, not regression output.
- **Selection of CEO quotes** to test maximalist claims against case and macro evidence.
- **Liebig minimum** and **political-friction** sections: interpretive thesis linking evidence streams, not measured coefficients.

### Limits

- **Desk research only.** No proprietary client field data; no new RCTs commissioned.
- **Synthesis rows** are sector benchmarks, not guarantees for any single deployment.
- **AVI medians and zone counts** will move as the source register is updated.

*May 2026 — Maciej Wilczyński, Valueships.*

---

## References (APA)

All references below were verified live at time of writing. Superscript numbers in the report (e.g. [@1]) map to this list.

### Macro productivity, AI economics

Acemoglu, D. (2024). *The simple macroeconomics of AI* (NBER Working Paper No. 32487). National Bureau of Economic Research. https://www.nber.org/papers/w32487

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). *The productivity J-curve: How intangibles complement general purpose technologies.* AEJ: Macroeconomics. https://www.aeaweb.org/articles?id=10.1257/mac.20180386

Crafts, N. (2002). *Productivity growth in the Industrial Revolution: A new growth accounting perspective.* Federal Reserve Bank of San Francisco. https://www.frbsf.org/wp-content/uploads/crafts.pdf

Gordon, R. J. (2016). *The rise and fall of American growth: The U.S. standard of living since the Civil War.* Princeton University Press. (US labour productivity — electric era and ICT baseline/revival; synthesis in FRBSF / NBER reviews.)

Hoover Institution. (n.d.). *Summary of English agrarian productivity estimates (post-1600 benchmark).* Desk synthesis for the historical productivity ladder (Part I).

David, P. A. (2001). *The transition to a new economy after the Second Industrial Revolution* (NBER Working Paper No. 8676). https://www.nber.org/papers/w8676

Federal Reserve Bank of St. Louis. (2025). *Generative AI and the future of work productivity.* https://www.stlouisfed.org/

Goldman Sachs. (2023). *Generative AI could raise global GDP by 7 %.* https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent

Goldman Sachs. (2024). *Gen AI: Too much spend, too little benefit?* https://www.goldmansachs.com/images/migrated/insights/pages/gs-research/gen-ai--too-much-spend,-too-little-benefit-/TOM_AI%202.0_ForRedaction.pdf

Goldman Sachs. (2026). *Tracking trillions: The assumptions shaping the scale of the AI build-out.* https://www.goldmansachs.com/insights/articles/tracking-trillions-the-assumptions-shaping-scale-of-the-ai-build-out

International Monetary Fund. (2024). *AI will transform the global economy. Let's make sure it benefits humanity.* https://www.imf.org/

McKinsey & Company. (2023). *The economic potential of generative AI: The next productivity frontier.* https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier

McKinsey & Company. (2025, November). *The state of AI 2025: Agents, innovation, and transformation.* https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

OECD. (2024). *Miracle or myth? Assessing the macroeconomic productivity gains from artificial intelligence.* https://www.oecd.org/

Stanford HAI. (2025). *Artificial Intelligence Index Report 2025.* https://hai.stanford.edu/ai-index/2025-ai-index-report

Stanford HAI. (2026). *Artificial Intelligence Index Report 2026.* https://hai.stanford.edu/ai-index/2026-ai-index-report

US Census Bureau. (2024). *Tracking firm use of AI in real time: A snapshot from the Business Trends and Outlook Survey* (CES-WP-24-16). https://www.census.gov/library/working-papers/2024/adrm/CES-WP-24-16.html

### Workplace productivity — RCTs and field experiments

Bick, A., Blandin, A., & Deming, D. J. (2024). *The rapid adoption of generative AI* (NBER Working Paper). National Bureau of Economic Research.

Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). *Generative AI at work* (NBER Working Paper No. 31161). National Bureau of Economic Research. https://www.nber.org/papers/w31161

Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942. https://academic.oup.com/qje/article/140/2/889/7990658

Choi, J. H., & Schwarcz, D. (2023). *AI assistance in legal analysis: An empirical study* (SSRN 4539836). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4539836

Choi, J. H., Monahan, A., & Schwarcz, D. (2024). *Lawyering in the age of artificial intelligence* (SSRN 4626276). https://ssrn.com/abstract=4626276

Dell'Acqua, F., McFowland, E. III, Mollick, E. R., Lifshitz-Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2023). *Navigating the jagged technological frontier* (HBS Working Paper 24-013). https://www.hbs.edu/ris/Publication%20Files/24-013_d9b45b68-9e74-42d6-a1c6-c72fb70c7282.pdf

Dillon, E., et al. (2025). *Microsoft 365 Copilot field experiment* (Harvard Business School).

Donati, D., et al. (2025). *AI and online retail productivity / sales uplift evidence* (arXiv preprint).

GitHub / Microsoft Research. (2023). *The impact of AI on developer productivity: Evidence from GitHub Copilot* (arXiv:2302.06590). https://arxiv.org/abs/2302.06590

METR. (2025, July). *Measuring the impact of early-2025 AI on experienced open-source developer productivity.* https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

MIT Generative AI Lab. (2025). *Copilot field experiment with Microsoft and Accenture.*

Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science, 381*(6654), 187–192. https://www.science.org/doi/10.1126/science.adh2586

UK Government. (2025). *Microsoft 365 Copilot experiment: Cross-government findings report.* https://www.gov.uk/

### AI in the workplace — surveys

BCG. (2025, June). *AI at work 2025: Momentum builds, but gaps remain.* Boston Consulting Group. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain

Microsoft. (2024, May). *Work Trend Index 2024: AI at work is here. Now comes the hard part.* https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part

Microsoft. (2025). *Breaking down the infinite workday.* https://www.microsoft.com/en-us/worklab/work-trend-index/breaking-down-infinite-workday

PwC. (2025). *The fearless future: 2025 Global AI Jobs Barometer.* https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html

### Enterprise AI failure and ROI

Bain & Company. (2025). *Technology Report 2025: AI leaders are extending their edge.* https://s3.amazonaws.com/media.mediapost.com/uploads/BAIN_report_technology_report_2025.pdf

Bain & Company. (2025, September 23). *$2 trillion in new revenue needed to fund AI's scaling trend* [Press release]. https://www.bain.com/about/media-center/press-releases/20252/$2-trillion-in-new-revenue-needed-to-fund-ais-scaling-trend---bain--companys-6th-annual-global-technology-report/

MIT NANDA Initiative. (2025, August). *The GenAI Divide: State of AI in business 2025.* https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf

RAND Corporation. (2024). *The root causes of failure for artificial intelligence projects and how they can succeed.* https://www.rand.org/pubs/research_reports/RRA2680-1.html

### Sector-specific evidence

American Medical Association. (2025). *AI scribes save 15,000 hours and restore the human side of medicine.* https://www.ama-assn.org/practice-management/digital-health/ai-scribes-save-15000-hours-and-restore-human-side-medicine

Mass General Brigham. (2026). *AI scribes linked to modest reductions in electronic health record use and clinical documentation time.*

McKinsey & Company. (2024). *Generative AI fuels creative physical product design but is no magic wand.*

McKinsey & Company. (2025). *Generative AI in healthcare.* https://www.mckinsey.com/industries/healthcare/our-insights/generative-ai-in-healthcare-current-trends-and-future-outlook

McKinsey & Company. (2025). *Manufacturing lighthouses — Capturing the full value of AI.* https://www.mckinsey.com/capabilities/operations/our-insights/how-manufacturings-lighthouses-are-capturing-the-full-value-of-ai

Thomson Reuters. (2024). *AI set to save professionals 12 hours per week by 2029.*

UCLA Health. (2025). *UCLA study finds AI scribes may reduce documentation time and improve physician well-being.* https://www.uclahealth.org/news/release/ucla-study-finds-ai-scribes-may-reduce-documentation-time

### AI maximalist claims

Amodei, D. (2024, October). *Machines of loving grace.* https://www.darioamodei.com/essay/machines-of-loving-grace

Amodei, D. (2025, May 28). Interview in Axios. *AI jobs danger: Sleepwalking into a white-collar bloodbath.* https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic

Anthropic. (2026, January). *Anthropic Economic Index report: Economic primitives.* https://www.anthropic.com/research/anthropic-economic-index-january-2026-report

Anthropic. (2026, March). *Anthropic Economic Index report: Learning curves.* https://www.anthropic.com/research/economic-index-march-2026-report

Anthropic. (2026). *Labor market impacts of AI: A new measure and early evidence.* https://www.anthropic.com/research/labor-market-impacts

Huang, J. (2024, March 19). Comments at GTC Conference. *AGI and hallucinations.* TechCrunch. https://techcrunch.com/2024/03/19/agi-and-hallucinations/

Huang, J. (2025, May 28). Comments at Milken Institute Global Conference. CNBC. https://www.cnbc.com/2025/05/28/nvidia-ceo-jensen-huang-youll-lose-your-job-to-somebody-who-uses-ai.html

Solow, R. M. (1987, July 12). *We'd better watch out.* New York Times Book Review.

### Pricing science

Anderson, J. C., Narus, J. A., & Van Rossum, W. (2006). Customer value propositions in business markets. *Harvard Business Review, 84*(3), 91–99. https://hbr.org/2006/03/customer-value-propositions-in-business-markets

Bessemer Venture Partners. (2025). *The AI pricing and monetization playbook.* https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook

Hinterhuber, A. (2004). Towards value-based pricing — An integrative framework for decision making. *Industrial Marketing Management, 33*(8), 765–778. https://users.metu.edu.tr/mugan/Hinterhuber%202004%20value%20based%20pricing.pdf

Hinterhuber, A., & Snelgrove, T. C. (2022). *Value first, then price: Building value-based pricing strategies* (2nd ed.). Routledge.

Stobierski, T. (2022). *A beginner's guide to value-based strategy.* Harvard Business School Online. https://online.hbs.edu/blog/post/what-is-value-based-strategy

### Statista evidence (13 charts integrated)

Statista. (2024). *Revenue impact of AI in financial services* (Chart 1254724). https://www.statista.com/statistics/1254724/revenue-impact-of-ai-financial-services/

Statista. (2024). *Working hours impacted by generative AI in finance, by sector — Accenture data* (Chart 1558899). https://www.statista.com/statistics/1558899/working-hours-impacted-generative-ai-finance/

Statista. (2024). *AI fintech impact on profitability* (Chart 1617474). https://www.statista.com/statistics/1617474/ai-fintech-impact-on-profitability/

Statista. (2025). *Growth of labor productivity — AI adoption* (Chart 1378626). https://www.statista.com/statistics/1378626/growth-of-labor-productivity-ai-adoption-2023/

Statista. (2025). *AI impact on hourly rates-based pricing global* (Chart 1482387). https://www.statista.com/statistics/1482387/ai-impact-on-hourly-rates-based-pricing-global/

Statista. (2025). *Functional impact of generative AI worldwide* (Chart 1610445). https://www.statista.com/statistics/1610445/functional-impact-of-generative-ai-worldwide/

Statista. (2025). *Cost decrease by AI function* (Chart 1610952). https://www.statista.com/statistics/1610952/cost-decrease-by-ai-analytics-enterprise/

Statista. (2025). *Adoption of pricing models for agentic AI tools* (Chart 1620734). https://www.statista.com/statistics/1620734/adoption-of-pricing-models-for-agentic-ai-tools/

Statista. (2025). *AI task automation trends among employees globally — Capgemini, June 2025* (Chart 1619156). https://www.statista.com/statistics/1619156/ai-task-automation-trends-among-employees-global/

Statista. (2026). *AI impact on profitability in finance worldwide* (Chart 1661254). https://www.statista.com/statistics/1661254/ai-impact-on-profitability-in-finance-worldwide/

Statista. (2026). *AI impact on profitability in financial services by characteristics* (Chart 1661255). https://www.statista.com/statistics/1661255/ai-impact-on-profitability-in-finance-worldwide-by-characteristics/

Statista. (2026). *AI impact on workforce in last 3 years — finance worldwide* (Chart 1661260). https://www.statista.com/statistics/1661260/ai-impact-on-workforce-in-last-three-years-finance-worldwide/

Statista. (2026). *Big Tech AI spending to reach $725 billion in 2026* (Chart 35046). https://www.statista.com/chart/35046/capital-expenditure-of-meta-alphabet-amazon-and-microsoft/

### Valueships proprietary frameworks (citable as such)

Wilczyński, M. (2026, May). *The Valueships Historical Productivity Ladder.* Valueships proprietary framework.

Wilczyński, M. (2026, May). *The Valueships Value Equation and the AI Value Index (AVI).* Valueships proprietary framework.

Wilczyński, M. (2026, May). *The AVI Pricing Quadrant™.* Valueships proprietary framework.

### Finance lineage (AVI)

Stern, J. M., Stewart, G. B., & Chew, D. H. (1995). The EVA financial management system. *Journal of Applied Corporate Finance, 8*(2), 32–46. https://doi.org/10.1111/j.1745-6622.1995.tb00295.x