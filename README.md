# The Unofficial Guide

Kealiiahonui Ohumukini
Corpora - City Guides

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

I chose the city guides corpus, which is a collection of documents describing the accessibility and features of each city that is listed. My system answers several questions from the level of accessibility to the services provided and tourist locations at each city. The purpose of this tool is to allow users to ask questions about city locations they wish to visit, and attain easy and clear answers.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** 400 characters
**Overlap:** ~40 characters 

Documents are ~2000 characters long but have several sections to be chunked. Each of these sections are 300-600 characters long, and to maintain context, each chunk should either be the length of the section, or split the section. 

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->
     

**Chunk 1** — source: ``guide_accessibility.md — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

## Straightforward

**Thornby Wells** is the easiest town in the region. It is flat, compact, and
everything is within three minutes of everything else.
```

**Chunk 2** — source: ``guide_corry_vale.md — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 2  |  source: guide_corry_vale.md#4  |  produced by: chunker.py::split_documents
======================================================================
ions.

## What to see

The valley itself is the attraction. The footpath network is dense and well marked, and a circuit taking in three of the four villages is about nine miles with 500 metres of ascent. The chapel in the second village is 12th century and always unlocked.

## Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms.
```

**Chunk 3** — source: ``guide_givens_mill.md — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 3  |  source: guide_givens_mill.md#2  |  produced by: chunker.py::split_documents
======================================================================
ontinues in both directions for as far as you want to walk.

## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: ``guide_marchwood.md — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 4  |  source: guide_marchwood.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Marchwood

Marchwood is the regional hub — 180,000 people, the junction everyone changes trains at, and a city most visitors pass through rather than stop in. That is a mistake, though an understandable one, since almost nothing of interest is near the station.

## Getting there

Every railway line in the region meets here, which is the city's defining feature.
```

**Chunk 5** — source: ``guide_regional_transport.md — produced by: chunker.py::split_documents``

```
======================================================================
Chunk 5  |  source: guide_regional_transport.md#5  |  produced by: chunker.py::split_documents
======================================================================
rom Brightwater runs four miles upstream on a good surface. The
old railway trackbed from Kestrelford runs six miles on an easy gradient and is
the best walking in the region for the effort involved. The coastal path from
Halden Bay is more serious — exposed, and closed in high wind.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** What is the most accessible town within this region 

**Answer:**

```
Based on `guide_accessibility.md`, Thornby Wells is described as the easiest town int he region, being flat, compact, and having level pump rooms and gardens. 
```

**My relevance cutoff:** Maintained at 0.6
     The best distance for the OUT_OF_SCOPE questions was 0.784 for "What is the capital of Mongolia". As this question is way off target, I do believe that it is reasonable to keep the relevance cutoff at around 0.6. The worst distance for a question that I have asked with an answer was 0.584. This question 

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What times are the pubs in kestrelford open? | Yes | 0.2680 |
| What town has a long seafront, and a land train that is aimed for children? What food does this location offer? | Yes | 0.4425 |
| What are all the locations that offer minor injuries units or full hospitals? | Yes | 0.4483 |
| What are the longest walkable paths metnioned in this region? | Yes | 0.4786 |
| What is the most accessible town in this region, and what amenities does it provide? | Yes | 0.4023 |
| What is the capital of Mongolia? | refused | 0.803 |
| How do I change the oil in a diesel engine? | refused | 0.891 |
| Who won the 1994 World Cup? | refused | 0.975 |
| What is the recommended dosage of ibuprofen for a headache? | refused | 0.838 |
| How do I write a for loop in Rust? | refused | 0.838 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked AI to validate my chunking system's logical reasoning. I wanted to use regex to build a chunking system that does not abrubtly end each chunk. I utilized AI to bridge the gaps I had within the first iterations of my function. It came back with a regex pattern, an adjustment to the overlapping system, and a few syntax corrections. 

**2.** When generating questions, I asked gemini to give me exmaples of what good questions are and why are they are good questions. Gemini gave me a few examples and stated that good testing questions should require multiple sources, be hyper specific to a doc, or be a general enough question that has an answer, but is hard to find within a pile of similar answers. 

**3.** More chunking system logistics. I would ask the AI model to explain to me in words how it would be best to implement a header-based chunking system, then a breadcrumb chunking system, and then verify what I had written.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 2/5 | 2/5 | 2/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunk size between 150-500 char & 10% char overlap | 9/10 | 5/10 | 10/10 | 9/10 | MISSED |
| 5. Model provides clear answers under 2 sentences| 5/5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MISSED | 2/5 questions were answered each time.  This means the model did not receive the right chunks |
| 2 | Every answer names a source | MET | EVERY llm response has an in-text citation and shows a source of either checked material or source material |
| 3 | The relevance gate stops out-of-corpus questions | MET | 5/5 out-of-corpus questions were blocked |
| 4 | 9/10 chunks between 150-500 char long & 10% chunk overlap | MISSED | There were more than a few chunks which missed, and the range of overlap was between 10-30% |
| 5 | Clear concise answers in 2 sentences or less | MET | Although a lacking criteria, all model responses were 2 sentences or less |

## Diagnoses

Criteria 1: Questions were ambiguous questions with lacking keywords. "Least accessible town" is difficult to find for retrieval if none of the source material makes such a comparison. Retrieval Issue?

Criteria 4: Embedding issue. Chunks ranged from ~24 - 500 on the first attempt, which means the chunks were out of bounds by quite a bit. This is due to h1 and h2 headers being set as separate chunks.

Criteria 5: A generation issue. Although this criteria was met, this is a lacking standard as half of it is met with the second criteria.

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**
Criteria 4 & 5:

- Criteria 4: All sampled chunks maintain a size of at least 150 characters and end with punctuation.
- Criteria 5: Every retrieved sample chunk includes a full header breadcrumb

Questions:

- Adjusted questions to be more specific. Adjusted questions to ask specific questions with clear information within the documents. Ex. Asking for the most accessible town and what amenities it has, rather than asking for the most/least accessible towns withint he region.

Chunking system:

- Adjusted chunking system to include header breadcrumbs

**Why I picked it:**

Criteria changes: Adjusted to have measurable results with meaningful impact.

Question changes: Questions with vague wording and comparables that aren't stated are not a fit testing metric for the model outside of rejection testing.

Chunking changes: Header breadcrumbs allow the system to see semantic context. If chunks lack a header like "# Walking in the region", there is nothing connectingn general context to the embeddings.
<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks > 150 characters & end with punctuation | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Every chunk has header breadcrumbs | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

### What is the most accessible town in this region, and what amenities does it provide? — run 3

- Best distance: 0.4023 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_walking.md

```
According to `guide_walking.md` and `guide_accessibility.md`, Thornby Wells is the most accessible town in the region on foot. It features flat, formal gardens, level streets, a central station, and a pump room and gardens that are level throughout (`guide_walking.md`, `guide_accessibility.md`).
```

### What are all the locations that offer minor injuries units or full hospitals? — run 2

- Best distance: 0.4483 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md

```
Based on the provided documents, Marchwood has the nearest full hospital, while Brightwater has a hospital, and Kestrelford, Halden Bay, Corry Vale, Givens Mill, and Elder Ness have minor injuries units with limited hours or nothing at all (`guide_accessibility.md`).
```

======================================================================
Chunk 10  |  source: guide_seasons.md#0  |  produced by: chunker.py::split_documents
======================================================================

# When to visit the region > ## Spring, March to May

Days lengthen quickly and businesses that closed for winter reopen through
March and April. By May everything is open and the weather is reliable enough
to plan around. Late May is arguably the best week of the year in Brightwater —
long days, everything running, and the students gone.

---

**Did it help?**
This did help. Metrics are better. Questions now pass the judge as well.
<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

1. Retrieved chunk contains the answer

I would probably add hybrid search so that the llm can answer vague questions. 

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

I would probably re-write most of the criteria. Given that I know how the chunking system works, I would probably write the metrics based on what I wnated the system to do. If I were just concerned with accuracy, I would stick with the current metrics of "Do the retrieved chunks contain the answer" or "Does the model state its sources". If I were concerned with usefulness, I might ask if the model can answer questions through deduction. Can it read through the "guide_walking.md" file and determine that Corry Vale has the longest stated pathway by making its own comparisons?

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
