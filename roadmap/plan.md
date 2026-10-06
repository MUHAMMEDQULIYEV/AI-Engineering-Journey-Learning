# 📋 The plan, block by block

Each block is a set of weeks. Each week has 4 study days: **LEARN · BUILD · SHIP · REVIEW** (see [README](README.md)).
🧠 = cold recall: explain an old topic from memory, with no notes.
Main sources are in [resources.md](resources.md). Light weeks (exams, holidays) are marked 🟡.
Every block ends with a **Done** line. A block is finished when its Done line is true, not when its weeks run out.
Every Done line has one 🔒 **closed-book check**: explain the core idea in 5 sentences, then implement it in ≤20 lines with no notes. A shipped repo is not proof you understand it; this is.

Not sure what to do? Open your `NEXT.md`. If it's empty, take the next unchecked day below.

**Length: 10 months** (Oct 2026 → end of Jul 2027 in [my calendar](my-calendar-2026-27.md)), about 10–12 h/week.

| README phase | Blocks | My dates (approx) |
|---|---|---|
| 1. Foundations | 1–3 | Oct → mid Nov |
| 2. LLM apps | 4–5 | mid Nov → mid Feb |
| 3. Agents | 6 | mid Feb → Mar |
| 4. Quality + job | 7–8 | end of Mar → Jul |

**Portfolio at the end (3 repos):**
1. **Mini-GPT** trained on Azerbaijani text (Block 3)
2. **Flagship**: RAG app + agent + MCP, deployed, with an eval write-up (Blocks 5–7)
3. **Open model vs API on my own task**: a LoRA fine-tune of a small open model, scored on the flagship eval set against the base model and the API model, with cost + latency (Block 8)

---

## Block 1 · Tokenization (1 week)
Goal: know how text becomes numbers, and build your own tokenizer.

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Karpathy *"Let's build the GPT Tokenizer"* 0–40 min. Write 2 predict questions in your notes. Compare `split(" ")` vs a real word tokenizer on your own 2 sentences: count tokens and unique tokens. | notebook + notes |
| ☐ BUILD | Karpathy 40–80 min. Own **character tokenizer**: `encode`, `decode`, test `decode(encode(x)) == x`. | test passes |
| ☐ SHIP | One **BPE merge step**: count pairs, merge the most frequent, repeat ×10. Push. | vocab grows, commit |
| ☐ REVIEW | Your BPE vs `tiktoken` on English + your own language (token counts). 🧠 why BPE? Write 2–3 **candidate** flagship data sources (5 min, no decision yet). | counts table + list |

Optional: stemming, lemmatization, stopwords (classic NLP). Good to know, not required.
**Done:** char tokenizer round-trip test passes · BPE runs 10 merges · token-count table (your BPE vs `tiktoken`, 2 languages) in the repo · 🔒 explain BPE in 5 sentences, then write one merge step (count pairs + merge) in ≤20 lines, no notes.

## Block 2 · Attention, watch only 🟡 (2 weeks, can be an exam period)
≤40 min per day, **no code** (the code-along happens in Block 3). Each video ends with **one predict question** that you write and answer yourself.

| Day | Task |
|---|---|
| ☐ LEARN | 3Blue1Brown, *Transformers* chapter 5 |
| ☐ BUILD | 3Blue1Brown, *Attention* chapter 6 |
| ☐ SHIP | Karpathy *"Let's build GPT"* 0:00–0:40 (data, bigram), watch only |
| ☐ REVIEW | Short weekly check-in |
| ☐ LEARN | Karpathy 0:40–1:20 (self-attention) |
| ☐ BUILD | Karpathy ~1:20 → end (multi-head, feed-forward, residual, LayerNorm, scaling up) |
| ☐ SHIP | One page: "attention in my own words" |
| ☐ REVIEW | Check-in · find and download ~1 MB of **Azerbaijani text** for Block 3 (no code) |

**Done:** 8 predict questions answered in notes · the one-page attention note · Azerbaijani text file saved · 🔒 explain `softmax(QKᵀ/√d)·V` in 5 sentences and write the shapes of Q, K, V and the attention matrix for B=1, T=4, C=8, no notes (no code this block).

## Block 3 · Mini-GPT from scratch (3 weeks, a cap) → portfolio repo #1
3 weeks is the limit, not the target. If it slips, the overflow goes into the Block 4 catch-up days.
**Corpus:** Azerbaijani text is the deliverable. Tiny Shakespeare is the warm-up and debug set (small, known results).
Karpathy's video is lookup only now: re-watch one part when you're stuck, then close it.

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Load tiny Shakespeare, encode with your Block 1 char tokenizer. **Train/val split** (90/10) + `get_batch` | `xb`, `yb` shapes printed |
| ☐ BUILD | `nn.Embedding` bigram model + training loop, generate text | generated sample |
| ☐ SHIP | `estimate_loss()`: mean train + val loss over N batches (`model.eval()`, `torch.no_grad()`). Push | train + val loss printed |
| ☐ REVIEW | 🧠 tokenization · check-in | — |
| ☐ LEARN | Single-head self-attention + causal mask, shape tests | tests pass |
| ☐ BUILD | **Positional embeddings** (token emb + position emb) + multi-head attention (reuse your single head) | shapes match |
| ☐ SHIP | Feed-forward + residual (`x + f(x)`) + LayerNorm = transformer block. Push | block runs |
| ☐ REVIEW | Explain attention from memory · check-in | — |
| ☐ LEARN | **Assemble** mini-GPT (embeddings → N blocks → LayerNorm → linear head). Overfit a small Shakespeare slice on CPU to find bugs | loss goes down |
| ☐ BUILD | Train on **Azerbaijani text** (Colab / Kaggle GPU), log train + val loss | val loss < your bigram's val loss |
| ☐ SHIP | Samples + loss curve plot + README with results. Push | **repo #1** ✅ |
| ☐ REVIEW | LinkedIn post · check-in | — |

**Done:** on Azerbaijani text, mini-GPT val loss is lower than the bigram val loss · loss plot + 3 samples + the numbers in the README · 🔒 explain causal self-attention in 5 sentences, then write one attention head with the causal mask in ≤20 lines, no notes.

## Block 4 · LLM apps (4 weeks): main course = Ed Donner *AI Engineer Core Track*
Watch at 1.5× speed, **≤30 min of video per day**. A course week has hours of video, so it gets **~1.5 calendar weeks**, and you watch on LEARN days *and* before the build on BUILD days. Skip lectures you don't need for the build; they are lookup only.
Pattern: LEARN = watch + predict · BUILD = rebuild *without the video* · SHIP = your variation + push · REVIEW = 🧠 one older topic + explain + plan.
Course weeks used: 1, 2 here; 3 and 5 are watched in the exam weeks after Block 4; 7 in Block 8. **Weeks 4, 6 and 8 are skipped** (lookup only).

| Week | Focus | Your build | Done when |
|---|---|---|---|
| ☐ 1 | Course Week 1: LLM APIs, first app (get an API key; budget in resources.md) | the course app, adapted to your language. REVIEW: pick a **tentative** flagship idea + data source | app answers in your language, pushed |
| ☐ 2 | Rest of course Week 1 + **prompting + structured output** (system prompt, few-shot, JSON validated by a **Pydantic** model). Last SHIP = catch-up | an extractor: text in → Pydantic object out | 5 test inputs, all parse |
| ☐ 3 | Course Week 2: Gradio UI, tool calling | an assistant with 1 real tool in a Gradio UI | the tool is called on 3 test prompts |
| ☐ 4 | **Embeddings + vector search**, then catch-up. LEARN: cosine similarity on 3 sentences (predict the order first). BUILD: embed ~20 flagship docs with a **multilingual** embedder (`sentence-transformers` + bge-m3 or multilingual-e5 (verify); English-only models do badly on Azerbaijani), top-3 search. SHIP: finish anything open (Block 3 overflow first). REVIEW: **confirm or switch the flagship idea** | top-3 search over your docs | the right doc is in the top 3 for 4 of 5 test questions |

If course Week 2 isn't finished, it takes week 4's LEARN/BUILD, and embeddings move to Block 5 week 1 (before any RAG code).
Optional (originality): make the flagship **Azerbaijani-specific** (Azerbaijani docs + questions). Later, publish its eval set as a Hugging Face dataset. Few public Azerbaijani RAG evals exist (verify), so this stands out.

**Applications v0** (late Nov → Dec, on optional days, not study days): CV with repo #1 + the Block 4 apps · a target list of ~30 companies · a tracker (company, role, date, status; keep it private, not in this repo). **First applications go out in Dec.** Don't wait for the flagship.

**Done:** 3 small apps pushed (API app, Pydantic extractor, tool assistant) · top-3 search works on your docs · flagship idea confirmed · CV v0 + target list ready · 🔒 explain the tool-calling loop in 5 sentences, then write cosine top-3 search in ≤20 lines, no notes.

## Block 5 · Flagship v0 + first deploy (7 weeks, holiday 🔥)
Holiday weeks may go up to ~15 h/week. Start with **2–3 easy days** after the exam weeks. Every REVIEW day: 🧠 one older topic.
Write the daily rows for this block at the review before it starts. Each week is done when its **Done** column is true.
**Core** = must ship. **Stretch** = only after core is done; otherwise it moves to the buffer week or Block 7.
Number targets are not gates: **report the number, timebox ≤2 days to improve it, then ship.**
⚠️ 20 questions is a small eval: a pass rate has a 95% CI of about ±0.18, so a 2–3 question difference is noise. Use a bootstrap CI, and pick final configs only at ≥50 questions (Block 7).

| Week | Milestone | Done when |
|---|---|---|
| ☐ 1 | **Core:** course Week 5 (RAG) build → **flagship v0**: naive RAG over ≥50 docs (vector DB, e.g. Chroma). **Eval set from day 1:** 20 questions (question + expected answer + source doc) and a script that runs it | script prints a score for all 20 |
| ☐ 2 | **Core:** **chunking** (2 sizes) + **recall@5** per config. **Stretch:** **hybrid search** (BM25 + embeddings). BM25 on Azerbaijani needs lowercasing + simple suffix handling (strip common endings), or it misses word forms | recall@5 table for ≥2 configs (≥3 with hybrid) · best number reported (aim 0.8, timebox ≤2 days, then ship) |
| ☐ 3 (1.5 wks) | **Core:** **error analysis** (read every failure, label its cause) + **baseline**: LLM with no retrieval vs your RAG. **Stretch:** **LLM-as-judge** for answer correctness, validated against your labels: hand-label ≥10 failing answers + some passing ones, report the judge's **TPR/TNR**; **reranker**; add BM25-only and hybrid + rerank to the baseline table | failure-cause table · pass-rate table for ≥2 systems · (stretch) judge TPR/TNR reported |
| ☐ 4 (1.5 wks) | **Core:** **FastAPI** (`/ask` endpoint) + **Docker** · **Langfuse tracing** (or OpenTelemetry): every `/ask` logs retrieved chunks, prompt, tokens, latency · **pytest** for chunking, retrieval and parsing · **GitHub Actions**: on every PR run pytest + the 20-question eval subset, fail if the pass rate drops > X points (set X above your run-to-run noise, e.g. 10) | `docker run` works locally · one `/ask` trace visible in Langfuse · CI green on a test PR · p50 latency and cost per question measured |
| ☐ 5 | **Buffer week** 🟡: fix the top failure causes from week 3, finish stretch items if there's room, nothing new | nothing open · pass rate ≥ week 3 |
| ☐ 6 | **Deploy v0 publicly** (Hugging Face Spaces), README with eval scores + baseline table · **CV + LinkedIn v1** with the live link, keep applying | public link works · live link in the CV · ≥3 more applications sent |

**Done:** live link · ≥50 docs · 20-question eval set runs in CI · recall@5 + answer pass rate in the README next to the baselines (numbers reported, not gates) · p50 latency + cost per question in the README · Langfuse traces + pytest + GitHub Actions in the repo · 🔒 explain the RAG pipeline in 5 sentences, then write `recall_at_k` in ≤20 lines, no notes.

## Block 6 · Agents + MCP (6 weeks)
Every REVIEW day: 🧠 one older topic. Last SHIP day of each month = catch-up.
The Hugging Face **Agents** and **MCP** courses are **lookup only** (~2 weeks of reading in total, spread over weeks 1–3): read the unit you need for the build, then close it. No certificates; the repo is the proof.

| Weeks | Milestone | Done when |
|---|---|---|
| ☐ 1–2 | Add an **agent** to the flagship (≥2 tools, one is your retriever). HF Agents Course = lookup | the agent picks the right tool on 8 of 10 test questions · pass rate not lower than v0 |
| ☐ 3 | An **MCP server** for the flagship. HF MCP Course = lookup | ≥2 tools called from an MCP client |
| ☐ 4 | **Agent evals + observability:** trace every agent run in Langfuse, read 20 traces, label failure causes (wrong tool, bad args, loops) · add tool-choice checks to the eval set and to CI | failure-cause table from traces · tool-choice eval runs in CI |
| ☐ 5 | **Prompt-injection safety:** 5 attack questions in the eval set + a simple guardrail on the agent's tools | ≥ 4/5 attacks blocked |
| ☐ 6 | Grow the flagship to ≥100 docs, redeploy · **1 open-source PR** (a docs fix or small bug in a library you used) **or 1 public post** (what your traces showed) · catch-up | eval re-run, scores updated in the README · PR or post link |

**Done:** agent + MCP server in the flagship repo · tool-choice eval in CI · injection test ≥ 4/5 · 1 OSS PR or public post · **≥ 4 applications per month** · 🔒 explain the agent loop (model → tool call → result → model) in 5 sentences, then write a tool-dispatch loop in ≤20 lines, no notes.

## Block 7 · Evals + production (6 weeks, incl. 🟡 spring midterms (approx))
The eval basics, tracing and CI are already in place from Block 5. This block goes deeper. Every REVIEW day: 🧠 one older topic.

| Week | Milestone | Done when |
|---|---|---|
| ☐ 1 | **Statistics for evals:** confidence intervals, **bootstrap**, A/B tests (ISLP refresh) · Hamel Husain's Evals FAQ + email course | bootstrap 95% CI on your pass rate, in the README |
| ☐ 2 | Grow the eval set to **~50 questions** · re-check the judge on the new set (TPR/TNR on ≥10 labeled failures) · **open-model switch:** the flagship can run on a small open model from a config flag (needed for Block 8) | judge TPR/TNR reported · open model scored on the same eval set |
| ☐ 3 | **Pick configs with evidence:** A/B test chunking / hybrid / reranker / prompt on ~50 questions with CIs · CI runs the full set on `main`, the 20-question subset on PRs | A/B results with CIs · chosen config + why, in the README |
| ☐ 4–5 | 🟡 **Spring midterms (approx, late Apr)**: light weeks, ≤40 min/day. DeepLearning.AI production AI agents short course (title: verify; watch only) · cold quizzes | notes only |
| ☐ 6 | **Cost + latency work:** caching, model routing (cheap model first, big model only when needed), measure **p95** from your Langfuse traces · redeploy the flagship with the agent · **eval write-up** in the README: failure categories, what fixed what | p50/p95 latency + cost per question, before/after · pass rate on ~50 questions reported (aim ≥ 80%, timebox, then ship) |

**Done:** ~50-question eval with bootstrap CI · judge TPR/TNR · pytest + GitHub Actions eval gate green on `main` · failure analysis + eval write-up published · p95 latency/cost before and after caching/routing · flagship works with API and open model · 🔒 explain the bootstrap CI in 5 sentences, then code it in ≤20 lines, no notes.

## Block 8 · Job-ready (12 weeks, ends end of Jul)
Applying runs the whole block: **≥ 10 applications per month**. Every REVIEW day: 🧠 one older topic. Keep 1 🟡 light week for spring finals (approx).

| Weeks | Milestone | Done when |
|---|---|---|
| ☐ 1–3 | **Repo #3: one LoRA SFT run** on Colab with PEFT + TRL on your own dataset (500–2k examples distilled from the API model; see resources.md) on the *same small open model* the flagship can run on (Block 7). Push the adapter to the HF Hub | before/after table on the flagship eval set: base open model vs LoRA vs API model, with cost + latency |
| ☐ 4–5 | **Serving basics:** quantization + vLLM, one small experiment | tokens/s and memory for 2 settings in a table |
| ☐ 6 | 🟡 light week (finals, approx) | — |
| ☐ 7–9 | **Polish 3 repos:** README, demo GIF, results · flagship eval write-up as a blog post | each README has a result table + a run command |
| ☐ 10–12 | **CV + LinkedIn v2** · interview prep: LLM system design (explain your flagship end to end), 1 mock interview per week (the first mocks were in Mar–Apr, see the weekly slot below) · buffer | 3 mocks done |

**Done:** 3 polished repos · CV v2 · ≥ 10 applications per month · 3 mock interviews in this block · 🔒 explain LoRA in 5 sentences, then write a LoRA linear layer (`W x + B A x`) in ≤20 lines, no notes.

---

## Weekly interview + retention slot (from Jan 2027)
45 min, once a week, on a non-study day (my calendar: the optional Wed). Skip it in 🟡 weeks. Alternate:
- **Odd weeks · DSA/SQL:** 2 LeetCode easy/medium + 1 SQL problem, timed.
- **Even weeks · blank-file rebuild:** pick an old topic (BPE merge, attention head, recall@k, …), explain it in 5 sentences, rebuild it from a blank file, then diff against your repo.
- **Mar–Apr:** once a month the slot is a **mock interview** (a friend or a peer-mock site): 1 coding problem + walk through the flagship.

Why this works (spaced, closed-book practice): see [learning-methods.md](learning-methods.md).

## Monthly review (last REVIEW day of each month)
- Write the day-by-day rows for next month. Far-future daily plans break, so only plan one month ahead in detail.
- Check the Done targets above. Too easy or too hard? Change the number and write why.
- Compare with the [mlabonne LLM Engineer track](https://github.com/mlabonne/llm-course) and 5 real job posts. Is anything important missing?
- Side interests go to an `IDEAS.md` parking list, not into the plan.
