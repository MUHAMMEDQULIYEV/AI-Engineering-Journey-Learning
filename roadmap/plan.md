# 📋 The plan, block by block

Each block is a set of weeks. Each week has 4 study days: **LEARN · BUILD · SHIP · REVIEW** (see [README](README.md)).
🧠 = cold recall: explain an old topic from memory, with no notes.
Main sources are in [resources.md](resources.md). Light weeks (exams, holidays) are marked 🟡.
Every block ends with a **Done** line. A block is finished when its Done line is true, not when its weeks run out.

Not sure what to do? Open your `NEXT.md`. If it's empty, take the next unchecked day below.

**Length: 10 months** (Oct 2026 → end of Jul 2027 in [my calendar](my-calendar-2026-27.md)), about 10–12 h/week.

| README phase | Blocks | My dates (approx) |
|---|---|---|
| 1. Foundations | 1–3 | Oct → mid Nov |
| 2. LLM apps | 4–5 | mid Nov → early Feb |
| 3. Agents | 6 | Feb → Mar |
| 4. Quality + job | 7–8 | Apr → Jul |

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
**Done:** char tokenizer round-trip test passes · BPE runs 10 merges · token-count table (your BPE vs `tiktoken`, 2 languages) in the repo.

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

**Done:** 8 predict questions answered in notes · the one-page attention note · you can write the shapes of Q, K, V and the attention matrix for B=1, T=4, C=8 from memory · Azerbaijani text file saved.

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

**Done:** on Azerbaijani text, mini-GPT val loss is lower than the bigram val loss · loss plot + 3 samples + the numbers in the README.

## Block 4 · LLM apps (4 weeks): main course = Ed Donner *AI Engineer Core Track*
Watch at 1.5× speed, **≤30 min of video per day**. A course week has hours of video, so it gets **~1.5 calendar weeks**, and you watch on LEARN days *and* before the build on BUILD days. Skip lectures you don't need for the build; they are lookup only.
Pattern: LEARN = watch + predict · BUILD = rebuild *without the video* · SHIP = your variation + push · REVIEW = 🧠 one older topic + explain + plan.
Course weeks used: 1, 2 here; 3 and 5 are watched in the exam weeks after Block 4; 7 in Block 8. **Weeks 4, 6 and 8 are skipped** (lookup only).

| Week | Focus | Your build | Done when |
|---|---|---|---|
| ☐ 1 | Course Week 1: LLM APIs, first app (get an API key; budget in resources.md) | the course app, adapted to your language. REVIEW: pick a **tentative** flagship idea + data source | app answers in your language, pushed |
| ☐ 2 | Rest of course Week 1 + **prompting + structured output** (system prompt, few-shot, JSON validated by a **Pydantic** model). Last SHIP = catch-up | an extractor: text in → Pydantic object out | 5 test inputs, all parse |
| ☐ 3 | Course Week 2: Gradio UI, tool calling | an assistant with 1 real tool in a Gradio UI | the tool is called on 3 test prompts |
| ☐ 4 | **Embeddings + vector search**, then catch-up. LEARN: cosine similarity on 3 sentences (predict the order first). BUILD: embed ~20 flagship docs (`sentence-transformers`), top-3 search. SHIP: finish anything open (Block 3 overflow first). REVIEW: **confirm or switch the flagship idea** | top-3 search over your docs | the right doc is in the top 3 for 4 of 5 test questions |

If course Week 2 isn't finished, it takes week 4's LEARN/BUILD, and embeddings move to Block 5 week 1 (before any RAG code).
**Done:** 3 small apps pushed (API app, Pydantic extractor, tool assistant) · top-3 search works on your docs · flagship idea confirmed.

## Block 5 · Flagship v0 + first deploy (6 weeks, holiday 🔥)
Holiday weeks may go up to ~15 h/week. Start with **2–3 easy days** after the exam weeks. Every REVIEW day: 🧠 one older topic.
Write the daily rows for this block at the review before it starts. Each week is done when its **Done** column is true.

| Week | Milestone | Done when |
|---|---|---|
| ☐ 1 | Course Week 5 (RAG) build → **flagship v0**: naive RAG over ≥50 docs (vector DB, e.g. Chroma). **Eval set from day 1:** 20 questions (question + expected answer + source doc) and a script that runs it | script prints a score for all 20 |
| ☐ 2 | Retrieval done properly: **chunking** (2 sizes), **hybrid search** (BM25 + embeddings), **recall@5** per config | recall@5 table for ≥3 configs · best ≥ 0.8 |
| ☐ 3 | **Reranker** + **eval basics**: error analysis (read every failure, label its cause), **LLM-as-judge** for answer correctness (check the judge against your own labels). **Baseline:** LLM with no retrieval vs BM25-only vs hybrid + rerank | judge agrees with you on ≥ 16/20 · pass-rate table for the 3 systems |
| ☐ 4 | **FastAPI** (`/ask` endpoint) + **Docker** | `docker run` works locally · p50 latency and cost per question measured |
| ☐ 5 | **Buffer week** 🟡: fix the top failure causes from week 3, nothing new | nothing open · pass rate ≥ week 3 |
| ☐ 6 | **Deploy v0 publicly** (Hugging Face Spaces), README with eval scores + baseline table · **CV + LinkedIn v1**, start applying with the live link | public link works · first 3 applications sent |

**Done:** live link · ≥50 docs · 20-question eval set · recall@5 ≥ 0.8 · answer pass rate in the README next to the baselines · p50 latency + cost per question in the README.

## Block 6 · Agents + MCP (8 weeks)
Every REVIEW day: 🧠 one older topic. Last SHIP day of each month = catch-up.

| Weeks | Milestone | Done when |
|---|---|---|
| ☐ 1–3 | **Hugging Face Agents Course** (free, certificate) → add an agent to the flagship (≥2 tools, one is your retriever) | the agent picks the right tool on 8 of 10 test questions · pass rate not lower than v0 |
| ☐ 4–6 | **Hugging Face MCP Course** (free, certificate) → an MCP server for the flagship | ≥2 tools called from an MCP client |
| ☐ 7 | **Prompt-injection safety:** 5 attack questions in the eval set + a simple guardrail on the agent's tools | ≥ 4/5 attacks blocked |
| ☐ 8 | Grow the flagship to ≥100 docs, redeploy · catch-up | eval re-run, scores updated in the README |

**Done:** both certificates · agent + MCP server in the flagship repo · injection test ≥ 4/5 · **≥ 4 applications per month**.

## Block 7 · Evals + production (5 weeks, incl. 🟡 spring midterms (approx))
The eval basics are already in place from Block 5. This block goes deeper. Every REVIEW day: 🧠 one older topic.

| Week | Milestone | Done when |
|---|---|---|
| ☐ 1 | **Statistics for evals:** confidence intervals, A/B tests (ISLP refresh) · Hamel Husain's Evals FAQ + email course | 95% CI on your pass rate, in the README |
| ☐ 2 | Grow the eval set to **~50 questions** · A/B test two prompts or two retrieval configs · **open-model switch:** the flagship can run on a small open model from a config flag (needed for Block 8) | A/B result with CI · open model scored on the same eval set |
| ☐ 3–4 | 🟡 **Spring midterms (approx, late Apr)**: light weeks, ≤40 min/day. DeepLearning.AI production AI agents short course (title: verify; watch only) · cold quizzes | notes only |
| ☐ 5 | **Tracing + cost/latency:** log every request, its cost and latency (tracing tool: see resources.md), cache where it helps · redeploy the flagship with the agent · **eval write-up** in the README: failure categories, what fixed what | p50/p95 latency + cost per question in the README · pass rate ≥ 80% on ~50 questions |

**Done:** ~50-question eval with CI · failure analysis + eval write-up published · latency/cost numbers · flagship works with API and open model.

## Block 8 · Job-ready (12 weeks, ends end of Jul)
Applying runs the whole block: **≥ 10 applications per month**. Every REVIEW day: 🧠 one older topic. Keep 1 🟡 light week for spring finals (approx).

| Weeks | Milestone | Done when |
|---|---|---|
| ☐ 1–3 | **Repo #3: one LoRA SFT run** on Colab (course Week 7) on the *same small open model* the flagship can run on (Block 7). Push the adapter to the HF Hub | before/after table on the flagship eval set: base open model vs LoRA vs API model, with cost + latency |
| ☐ 4–5 | **Serving basics:** quantization + vLLM, one small experiment | tokens/s and memory for 2 settings in a table |
| ☐ 6 | 🟡 light week (finals, approx) | — |
| ☐ 7–9 | **Polish 3 repos:** README, demo GIF, results · flagship eval write-up as a blog post | each README has a result table + a run command |
| ☐ 10–12 | **CV + LinkedIn v2** · interview prep: LLM system design (explain your flagship end to end), 1 mock interview per week · buffer | 3 mocks done |

**Done:** 3 polished repos · CV v2 · ≥ 10 applications per month · 3 mock interviews.

---

## Monthly review (last REVIEW day of each month)
- Write the day-by-day rows for next month. Far-future daily plans break, so only plan one month ahead in detail.
- Check the Done targets above. Too easy or too hard? Change the number and write why.
- Compare with the [mlabonne LLM Engineer track](https://github.com/mlabonne/llm-course) and 5 real job posts. Is anything important missing?
- Side interests go to an `IDEAS.md` parking list, not into the plan.
