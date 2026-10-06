# 🧠 Learning methods: which one, when

Watching and rereading *feel* like learning, but most of it is gone a week later. Pulling the idea out of your head is what makes it stay.
This page lists the methods that research supports, and which one to use in which situation.
Sources: Dunlosky et al. (2013), a review of 10 study techniques, and the book *Make It Stick* (Brown, Roediger, McDaniel, 2014).

---

## Situation → method

| Situation | Best method | How (1 line) | Avoid |
|---|---|---|---|
| New math-heavy concept (attention, softmax) | **Dual coding + predict** | Draw the shapes by hand first: `x (B=1,T=4,C=8) → q,k (1,4,8) → q@kᵀ (1,4,4)`, predict each shape, then run it. | Reading the formula 5 times |
| Coding-along video | **Worked example → faded → blank file** | Watch ≤30 min, then redo it with half the lines deleted, then from an empty file the next day (e.g. BPE `merge()`). | Typing along at 2× and calling it done |
| New library or API (FastAPI, LangChain) | **Spike first, then learn** | 30-minute ugly spike: one `/ask` endpoint that returns JSON. *Then* read the docs page for the parts you used. | Watching a full course before writing a line |
| Debugging | **Predict + error log** | Before each fix, write "I think it fails because …"; after, log the bug + the real cause in 1 line in `notes.md`. | Changing random lines until it works |
| Reading a paper | **Docs/source over video + Feynman** | Read abstract, figures and one key equation; then explain it in 5 sentences with the paper closed. | Watching 3 summary videos instead |
| End of a block | **Retrieval + blank-file rebuild** | Closed book: rebuild the core piece timed (e.g. causal self-attention in ≤20 lines), then check against your repo. | Rereading your notebooks |
| Before interviews | **Interleaved recall + Feynman** | Mix old topics in one session: BPE, attention, RAG recall@5, evals. Explain each out loud in 2 minutes. | Cramming one topic the night before |
| Exam / watch-only weeks | **Retrieval after watching** | After each video, close it and write 3 lines from memory in `notes.md`. That's the commit. | Watching with notes copied from the slides |
| Bad day, 15 minutes | **One recall question** | Answer the due question from the session log, or one predict on 1 cell. Commit. | "I'll just watch something" |

---

## The core methods (one line each)

- **Retrieval practice:** answer from memory *before* looking. Getting it wrong and then checking still helps.
- **Spaced repetition:** come back to a topic after growing gaps (the ladder below), not all at once.
- **Predict before run:** write what a cell will print or what shape it will have. Log ✅ hit / ❌ miss.
- **Worked example → fading:** study a full example, then fill in a version with parts removed, then write it from a blank file.
- **Feynman / explain in 5 sentences:** explain it simply with notes closed. The sentence where you get stuck is the gap.
- **Interleaving:** mix old and new topics in one practice session instead of one topic in a long block.
- **Deliberate practice:** rebuild a known piece from a blank file, timed, and aim at the part you get wrong.
- **Error / misconception log:** one line per bug or wrong belief, with the real cause. Reread it before a REVIEW day.
- **Dual coding:** words + a picture. Draw tensor shapes, data flow, the RAG pipeline by hand.
- **Spike first, then learn:** for tools, a small working thing comes first; it gives the docs something to attach to.
- **Docs/source over video:** for libraries, the docs page and the source are faster and more exact than a video.

---

## The gap ladder (spaced recall)

After a topic is learned, recall it on day **1 → 3 → 7 → 21 → 60**.

| Result of the recall | Next gap |
|---|---|
| ✅ correct, without help | move one step up the ladder |
| 🟡 partial (needed a hint, or one part missing) | stay on the same step |
| ❌ miss | **reset to 1 day** |

Example: BPE learned on Oct 7 → recall Oct 8 ✅ → Oct 11 ✅ → Oct 18 🟡 → Oct 25 ❌ → Oct 26.
The session log's 🧠 column holds the next due date. `Start session` picks the **oldest due** topic from the whole log.
After a ✅ at 60 days, the topic is done; it comes back only in interleaved interview recall.

---

## Avoid (and why)

- **Rereading notes:** feels familiar, but familiar is not the same as being able to recall it.
- **Highlighting:** marks text but doesn't make you produce anything.
- **Passive 2× video:** speed hides how little you could rebuild. Watch less, then build.
- **Copying code (yours or the AI's):** if you can't rewrite it from a blank file, you don't own it yet.
- **Massed practice (cramming one topic):** works for tomorrow, fades in a week. Space it.

---

## Which method in which block

| Block | Main methods |
|---|---|
| 1 · Tokenization, BPE | worked example → faded → blank-file `merge()`; predict token counts |
| 2 · Attention | **dual coding** (draw B, T, C shapes) + **predict** every shape |
| 3 · Mini-GPT | fading from Karpathy's video to blank file; error log for training bugs |
| 4 · LLM APIs, tools | spike first, then docs; predict the JSON your schema returns |
| 5 · RAG + deploy | **spike first, then learn** (FastAPI, Chroma); predict recall@5 before each change |
| 6 · Agents, MCP | spike first; error log for tool-calling failures; docs over video |
| 7 · Evals, tracing | Feynman on each metric (TPR/TNR, CI) in 5 sentences; retrieval on stats |
| 8 · LoRA, job-ready | **interleaved recall + Feynman** across Blocks 1–7; timed blank-file rebuilds |

Every REVIEW day, whatever the block: one recall from the gap ladder + one blank-file rebuild.
