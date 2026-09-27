# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer - MISSED

CRITERIA RESULTS: 
STATUS: MISSED
CRITERIA: Unbroken
QUESTION: Broken?
Why: All questions that were missed are ambiguous questions that require a measurable to answer. "What is the most accessible town in this region" is unanswerable if NONE of the documents use "most accessible" to describe a town within the region. 
Adjustment: 

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
Expecting all tests to pass is unrealistic as verbage and context specificity heavily affectcs model accuracy. Hyper specific questions may be ignored due to the lack of clear information or incorrect language.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
Answers provided by the llm must be based on context provided to prevent hallucinations and incorrect answers.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->

---

## 4. At least 9 of 10 chunks sizes reside within the window of 40-120 words (~150-500) characters with a ~10% character overlap between chunks

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->

**Why this target:** The documents provided are small enough that smaller chunks are necessary to parse information correctly. Most chunks should pass this test however, some chunks may end up containing less than 40 characters due to the document length.

---

## 5. For all 5 test questions, the model provides clear and concise answers in under 2 sentences with citations. 
<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->



**Why this target:**
A RAG system needs to base its information on the context provided AND return clear answers that help the user regardless of the question. Longer answers can lead to the inclusion of irrelevant information and inadequate context alongside the answers. 

---

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 2/5 | 2/5 | 2/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |


### What hours are the pubs in Kestrelford open? — run 1

- Best distance: 0.3277 (passed the gate)
- Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md, guide_regional_transport.md

```
According to `guide_kestrelford.md` and `guide_eating.md`, the pubs in Kestrelford serve food between 12 and 2 and again between 6 and 8:30, with nowhere to eat outside of those windows (`guide_kestrelford.md`, `guide_eating.md`).
```
_____________________________________________________________________________________________

### What awn has a long seafront, and a land train that is aimed for children? What food does this location offer? — run 1

- Best distance: 0.4060 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_eating.md, guide_pellew_sands.md

```
Pellew Sands has a two-mile flat seafront and a land train that runs hourly between Easter and September, which is aimed at children but used by everyone (*guide_pellew_sands.md* and *guide_accessibility.md*). The food offered on its seafront consists of chips and ice cream (*guide_pellew_sands.md* and *guide_eating.md*).
```
_______________________________________________________________________________________________

### What locations offer minor injury locations and are often expensive during the summer months july, august, or september? — run 1

- Best distance: 0.5045 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_corry_vale.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md

```
Based on the provided documents, there is no information regarding locations that are expensive during the summer months of July, August, or September (guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_corry_vale.md, guide_brightwater.md). Therefore, I do not have enough information to answer your question.
```
_________________________________________________________________________________________________

### What town in thsi region has the longest walkable path? — run 1

- Best distance: 0.4541 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_halden_bay.md, guide_regional_transport.md, guide_walking.md

```
Based on the provided documents, there is no mention of which town has the longest walkable path, so I do not have enough information to answer your question.
```
_________________________________________________________________________________________________

### What are the least and most accessible towns within this region? — run 1

- Best distance: 0.4032 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_givens_mill.md, guide_walking.md

```
Based on the provided documents, Thornby Wells is described as "the easiest town in the region," making it the most accessible town (*guide_accessibility.md*). However, the documents do not mention which town is the least accessible (*guide_accessibility.md*; *guide_corry_vale.md*; *guide_givens_mill.md*; *guide_walking.md*). Therefore, I do not have enough information to answer that part of the question.
```

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
