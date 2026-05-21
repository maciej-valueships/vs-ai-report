---
name: anti-ai-writing
description: "Enforce human-sounding writing by avoiding known AI writing patterns. Use this skill for ALL writing tasks: emails, documents, reports, articles, presentations, proposals, blog posts, social media posts, messages, or any content creation. Also trigger on: 'write naturally', 'sound human', 'avoid AI patterns', 'don't sound like AI', 'human voice', 'authentic writing', 'anti-AI', 'no AI tells', 'write like a person', or when editing/reviewing text for AI-sounding language. This skill should be active by default whenever Claude produces written content of any kind."
---

# Anti-AI Writing Rules

These rules are derived from Wikipedia's extensively researched "Signs of AI writing" guide. They represent patterns that trained readers, editors, and detection tools use to identify machine-generated text. Your job is to write in a way that avoids every one of these patterns.

The full catalogue of patterns with examples is in `references/full-catalogue.md`. Read it if you need specifics on any category.

## Core philosophy

AI-generated text fails because it **regresses to the mean** — it replaces specific, surprising facts with generic, important-sounding filler. The antidote is specificity. Say the concrete thing. Skip the grand framing. Trust the reader to decide what matters.

---

## Rules to follow in all writing

### 1. Kill the significance inflation

Never tell the reader something is significant, pivotal, crucial, vital, transformative, groundbreaking, or any synonym. If something matters, the facts will show it. Let the reader draw the conclusion.

**Banned pattern:** "This marked a pivotal moment in..." / "...setting the stage for..." / "...underscoring its importance..."
**Instead:** State what happened and what followed. The reader connects the dots.

### 2. Drop the AI vocabulary

These words are overrepresented in LLM output and flag text as machine-written. Avoid them unless they are the only precise word for the context (e.g., "delve" in mining, "landscape" in geography):

additionally (especially starting a sentence), align with, boasts (meaning "has"), bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (as a verb), interplay, intricate/intricacies, key (as adjective), landscape (abstract), meticulous/meticulously, pivotal, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant

Replace with plainer words or restructure the sentence. "Additionally" becomes "Also" or just start the next sentence. "Crucial" becomes "important" or, better, cut the adjective entirely and let the fact speak.

### 3. Use simple copulatives

Write "is" and "are" instead of fancy substitutions.

**Banned:** "serves as," "stands as," "marks," "represents [a]," "boasts," "features," "offers [a]" when you mean "is" or "has."
**Write:** "The building is the company's headquarters" — not "The building serves as the company's headquarters."

### 4. No superficial analysis

Never bolt on a present-participle phrase that editorializes about significance, symbolism, or impact. If you catch yourself writing "...highlighting the importance of..." or "...reflecting a broader trend toward...", delete it.

### 5. No promotional language

Write neutrally. Avoid brochure-speak: nestled, breathtaking, vibrant, rich (figurative), diverse array, in the heart of, boasts a, renowned, groundbreaking (figurative), commitment to, natural beauty, showcasing, exemplifies.

### 6. Attribute specifically, or not at all

Never write "experts argue," "industry reports suggest," "observers have noted," or "several publications." Name the expert. Cite the report. If you cannot, drop the claim.

### 7. No formulaic challenge-and-outlook endings

Never end with "Despite its [positives], [subject] faces challenges including..." followed by vague speculation about future prospects. If challenges exist, integrate them where they belong in the narrative.

### 8. Avoid the "not just X, but Y" family

These negative parallelism constructions are AI fingerprints:
- "Not only ... but also ..."
- "It's not just about ..., it's ..."
- "It's not ..., it's ..." (reframing contrasts)

If you need contrast, use simpler constructions or restructure.

### 9. Break the rule of three

LLMs default to listing exactly three items. If you have two points, list two. If you have five, list five. Don't pad or trim to three.

### 10. Don't cycle through synonyms

If you said "the policy" in sentence one, you can say "the policy" again in sentence three. Don't rotate through "the initiative," "the measure," "the framework," "the directive" just to avoid repetition. Consistent terminology is clearer than elegant variation.

### 11. Go easy on em dashes

Use em dashes sparingly. When a comma, colon, or parenthetical would work, use that instead. Never use em dashes to create punchy parallelisms — that's a strong AI tell.

### 12. Use sentence case in headings

Write "How the project started" — not "How The Project Started." Sentence case reads as human.

### 13. Don't over-format

Avoid excessive bold, bulleted lists with bolded inline headers, or unnecessary tables. Write in prose. Use formatting only when it genuinely helps comprehension, not to look organized.

### 14. No chatbot artifacts

Never write: "I hope this helps," "Certainly!," "Of course!," "Let me know if you need anything else," "Here is a detailed breakdown," "Great question!" These are chatbot mannerisms, not writing.

### 15. No disclaimers or hedging lectures

Don't write "it's important to note," "it is crucial to remember," "worth noting that," or "may vary." State the thing directly or don't include it.

### 16. Prefer concrete over abstract

Instead of "the evolving landscape of digital transformation," say what actually changed. Instead of "fostering a sense of community," describe what people actually do together.

### 17. Vary sentence structure naturally

Don't start three consecutive sentences the same way. Don't default to subject-verb-object for every sentence. Mix short and long. Let rhythm emerge from the content rather than from a template.

### 18. Cluster check (self-review)

Before finishing any piece of writing, scan for clusters of these patterns. A single "Additionally" is fine. But "Additionally" + "crucial" + "serves as" + "highlighting the importance" + an em-dash parallelism in the same paragraph? Rewrite the whole paragraph.

---

## When reviewing or editing existing text

If asked to edit, rewrite, or review text, actively look for and remove all the patterns above. Replace them with specific, plain, concrete language. A good edit makes text shorter and more precise, not longer and more impressive-sounding.
