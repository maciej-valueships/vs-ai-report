# Signs of AI writing — reference guide

Distilled from Wikipedia's "Signs of AI writing" advice page (WikiProject AI Cleanup). This is a catalogue of known patterns that make text read as machine-generated. Use it as a checklist when writing or editing.

---

## 1. Content-level tells

### 1.1 Undue emphasis on significance, legacy, and broader trends

LLMs inflate importance by grafting grand claims onto ordinary subjects.

**Words to avoid:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**What it looks like:** A mundane statistical institute becomes something that "marked a pivotal moment"; a small town "solidifies its role as a regional hub." The subject gets less specific and more exaggerated at the same time.

### 1.2 Undue emphasis on notability, attribution, and media coverage

LLMs try to prove a subject is notable by listing media outlets instead of summarising what those sources actually said.

**Words to avoid:** independent coverage, local/regional/national media outlets, music/business/tech outlets, profiled in, written by a leading expert, active social media presence, featured in, cited in, documented in

**What it looks like:** "She was featured in Vogue, Wired, Toronto Star, and other media" — name-dropping outlets without substance. Or asserting someone "maintains a strong digital presence."

### 1.3 Superficial analyses

LLMs bolt on pseudo-insightful commentary using present-participle ("-ing") phrases, often at the ends of sentences.

**Words to avoid:** highlighting/underscoring/emphasizing ..., ensuring ..., reflecting/symbolizing ..., contributing to ..., cultivating/fostering ... (figurative), encompassing ..., valuable insights, align/resonate with

**What it looks like:** A paragraph about a city's population suddenly claims it is "further enhancing its significance as a dynamic hub of activity and culture."

### 1.4 Promotional and advertisement-like language

LLMs default to brochure-speak even when prompted for neutral prose.

**Words to avoid:** boasts a, vibrant, rich (figurative), profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, featuring, diverse array

**What it looks like:** A Wikipedia article about a town reads like a travel-agency pitch — "Nestled within the breathtaking region ... stands as a vibrant town with a rich cultural heritage."

### 1.5 Vague attributions and overgeneralization of opinions

LLMs attribute claims to unnamed experts or inflate the consensus behind a view.

**Words to avoid:** industry reports, observers have cited, experts argue, some critics argue, several sources/publications (when only a few are cited), such as (before exhaustive word lists), researchers and conservationists, described in scholarship, modern researchers treat

### 1.6 Outline-like conclusions about challenges and future prospects

LLMs end articles with a formulaic "Despite its [positives], [subject] faces challenges..." paragraph, often followed by speculation about "future prospects."

**Words to avoid:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

---

## 2. Language and grammar tells

### 2.1 High density of "AI vocabulary" words

These words appear far more frequently in post-2022 text. One or two are coincidental; a cluster is a strong signal.

**Full list:** Additionally (especially beginning a sentence), align with, boasts (meaning "has"), bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (as a verb), interplay, intricate/intricacies, key (as an adjective), landscape (as an abstract noun), meticulous/meticulously, pivotal, showcase, tapestry (as an abstract noun), testament, underscore (as a verb), valuable, vibrant

**Era breakdown:**
- 2023-mid 2024 (GPT-4 era): Additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, interplay, key, landscape, meticulous, pivotal, underscore, tapestry, testament, valuable, vibrant
- Mid-2024-mid 2025 (GPT-4o): align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant
- Mid-2025 onward (GPT-5): emphasizing, enhance, highlighting, showcasing

### 2.2 Avoidance of basic copulatives ("is"/"are" phrases)

LLMs replace simple "is" or "are" with fancier constructions.

**Words to avoid:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**What it looks like:** Instead of "Gallery 825 is LAAA's exhibition space," the AI writes "Gallery 825 serves as LAAA's exhibition space." Instead of "There are four gallery spaces," it writes "The gallery features four separate spaces."

### 2.3 Negative parallelisms

LLMs overuse contrast structures to seem balanced and thoughtful.

**Patterns to avoid:**
- "Not only ... but also ..."
- "It is not just about ..., it's ..."
- "It's not ..., it's ..." / "No ..., just ..."
- "is not X but Y" / "not a representation of ..., but a mechanism for ..."

### 2.4 Rule of three

LLMs pad out lists to exactly three items to look comprehensive.

**What it looks like:** "global SEO professionals, marketing experts, and growth hackers" — "keynote sessions, panel discussions, and networking opportunities."

### 2.5 Elegant variation

LLMs avoid repeating a word by cycling through synonyms, sometimes awkwardly — e.g. referring to the same concept as "the constraints," "non-conformist artists," "their creativity," "these artists," "their artistic aspirations," "like-minded artists" all within a few sentences.

### 2.6 Overuse of em dashes

LLMs use em dashes (---) more often than human writers, and in places where commas, parentheses, or colons would be more natural. They tend to use them in a formulaic, "punched up" way.

---

## 3. Style tells

### 3.1 Title case in headings

LLMs capitalize every main word in headings (Title Case) rather than using sentence case.

### 3.2 Overuse of boldface

LLMs bold phrases mechanically for emphasis, often in a "key takeaways" style — e.g. every important noun or phrase in a paragraph gets bolded.

### 3.3 Inline-header vertical lists

Numbered or bulleted lists where each item starts with a bolded header followed by a colon, then descriptive text. Often uses non-standard list markers (hyphens, hash symbols, explicit numbers like "1.").

### 3.4 Unnecessary tables

LLMs create small tables for information that would read more naturally as prose.

### 3.5 Skipping heading levels

LLMs tend to jump from H1 straight to H3, skipping H2.

---

## 4. Communication tells (leftover chatbot artifacts)

### 4.1 Collaborative communication phrases

Phrases that belong in a chat response, not in a document.

**Words to avoid:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., is there anything else, let me know, more detailed breakdown, here is a ...

### 4.2 Knowledge-cutoff disclaimers

**Words to avoid:** as of [date], up to my last training update, as of my last knowledge update, while specific details are limited/scarce..., not widely available/documented/disclosed, ...in the provided/available sources/search results..., based on available information...

### 4.3 Phrasal templates and placeholders

Fill-in-the-blank text the user forgot to complete — e.g. "[Entertainer's Name]", "INSERT_SOURCE_URL_30", "PASTE_SPOTIFY_TRACK_URL_HERE."

---

## 5. Structural tells

### 5.1 Section summaries

Older LLMs end sections or articles with "In summary..." or "In conclusion..." paragraphs that restate what was just said.

### 5.2 Didactic disclaimers (2022-2024 era)

Phrases like "it's important to note," "it is crucial to differentiate," "worth noting," "may vary" — the LLM lecturing the reader.

### 5.3 Prompt refusals

Leftover text like "As an AI language model, I cannot offer medical advice, but I can..."

---

## Quick self-check — the clustering principle

No single pattern proves AI authorship. But when several of these patterns cluster in the same piece of text — AI vocabulary words co-occurring with superficial analyses, promotional language, em-dash overuse, and negative parallelisms — the probability rises sharply. When editing your own writing, look for clusters rather than individual words.
