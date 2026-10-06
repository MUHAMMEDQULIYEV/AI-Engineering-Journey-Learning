# 📋 The plan, block by block

Each block is a set of weeks. Each week has 4 study days: **LEARN · BUILD · SHIP · REVIEW** (see [README](README.md)).
🧠 = cold recall: explain an old topic from memory, with no notes.
Main sources are in [resources.md](resources.md). Light weeks (exams, holidays) are marked 🟡.

Not sure what to do? Open your `NEXT.md`. If it's empty, take the next unchecked day below.

---

## Block 1 · Tokenization (1 week)
Goal: know how text becomes numbers, and build your own tokenizer.

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Karpathy *"Let's build the GPT Tokenizer"* 0–40 min. Write 2 predict questions in your notes. Compare `split(" ")` vs a real word tokenizer on your own 2 sentences: count tokens and unique tokens. | notebook + notes |
| ☐ BUILD | Karpathy 40–80 min. Own **character tokenizer**: `encode`, `decode`, test `decode(encode(x)) == x`. | test passes |
| ☐ SHIP | One **BPE merge step**: count pairs, merge the most frequent, repeat ×10. Push. | vocab grows, commit |
| ☐ REVIEW | Your BPE vs `tiktoken` on English + your own language (token counts). 🧠 why BPE? **Choose your flagship project + its data source.** | counts table + choice written |
Optional: stemming, lemmatization, stopwords (classic NLP). Good to know, not required.

## Block 2 · Attention, watch only 🟡 (2 weeks, can be an exam period)
≤40 min per day. Each video ends with **one predict question** that you write and answer yourself.

| Day | Task |
|---|---|
| ☐ LEARN | 3Blue1Brown, *Transformers* chapter 5 |
| ☐ BUILD | 3Blue1Brown, *Attention* chapter 6 |
| ☐ SHIP | Karpathy *"Let's build GPT"* 0:00–0:40 (bigram) |
| ☐ REVIEW | Short weekly check-in |
| ☐ LEARN | Karpathy 0:40–1:20 |
| ☐ BUILD | Karpathy to the end of the self-attention part |
| ☐ SHIP | One page: "attention in my own words" |
| ☐ REVIEW | Check-in |

## Block 3 · Mini-GPT from scratch (3 weeks) → portfolio repo #1
| Day | Task | Output |
|---|---|---|
| ☐ LEARN | `nn.Embedding` + bigram language model | shapes printed |
| ☐ BUILD | Train the bigram model, generate text | generated sample |
| ☐ SHIP | **Catch-up day** | everything open is closed |
| ☐ REVIEW | 🧠 tokenization · check-in | — |
| ☐ LEARN | Single-head self-attention + causal mask, shape tests | tests pass |
| ☐ BUILD | Multi-head + feed-forward + residual (`x + f(x)`) + LayerNorm = transformer block | block runs |
| ☐ SHIP | Assemble mini-GPT, train on tiny Shakespeare (Colab / Kaggle GPU) | loss goes down |
| ☐ REVIEW | Explain attention from memory · check-in | — |
| ☐ LEARN | Train on text in **your own language** | — |
| ☐ BUILD | Generation + loss curve plot | plot in repo |
| ☐ SHIP | README with results + a LinkedIn post | **repo #1** ✅ |
| ☐ REVIEW | Check-in | — |

## Block 4 · LLM apps (4 weeks): main course = Ed Donner *AI Engineer Core Track*
Watch at 1.5× speed. **One build per course week:** your own variation of the course project, in your language or for your problem. One course week may take up to 1.5 real weeks, and that's fine.
Pattern for every week: LEARN = watch + predict · BUILD = rebuild the project *without the video* · SHIP = your variation + push · REVIEW = explain + plan.

| Week | Course week | Your build |
|---|---|---|
| ☐ 1 | Week 1: LLM APIs, first app (get an API key, ~$10 budget) | the course app, adapted to your language |
| ☐ 2 | Week 2: Gradio UI, tool calling | an assistant with 1 real tool. Last SHIP = catch-up |
| ☐ 3 | Week 3: Hugging Face pipelines + tokenizers | compare an HF tokenizer with your Block 1 BPE |
| ☐ 4 | **Buffer week**: finish anything open. If you're ahead, start course Week 5 (RAG) | nothing left open |

## Block 5 · Flagship v0 (often a holiday 🔥, 4–5 h/day)
- ☐ Course Week 5 (RAG) → **flagship v0**: RAG over ~20 documents from your data source
- ☐ **10-question eval set from day 1** (question + expected answer); run it after every change
- ☐ Course Week 4 (code generation), low priority
- ☐ Course Weeks 6–8 (fine-tuning): watch, light code
- ☐ Wrap the flagship in **FastAPI** + **Docker**
Write the daily rows for this block at the review before it starts.

## Block 6 · Agents + MCP (2 months)
- ☐ **Hugging Face Agents Course** (free, certificate) → add an agent to the flagship
- ☐ **Hugging Face MCP Course** (free, certificate) → build an MCP server for the flagship
- ☐ Last SHIP day of each month = catch-up

## Block 7 · Evals + deploy (1 month)
- ☐ Hamel Husain's Evals FAQ + free email course
- ☐ DeepLearning.AI *Production-Ready AI Agents* (free)
- ☐ Grow the eval set to ~30 questions, track scores in the README
- ☐ Deploy the flagship (Hugging Face Spaces or a cheap server)

## Block 8 · Job-ready (2–3 months)
- ☐ Statistics for evals: confidence intervals, A/B tests
- ☐ LoRA fine-tuning basics (revisit course Week 7)
- ☐ Polish 3 repos: README, demo GIF, results
- ☐ CV + LinkedIn, apply

---

## Monthly review (last REVIEW day of each month)
- Write the day-by-day rows for next month. Far-future daily plans break, so only plan one month ahead in detail.
- Compare with the [mlabonne LLM Engineer track](https://github.com/mlabonne/llm-course) and 5 real job posts. Is anything important missing?
- Side interests go to an `IDEAS.md` parking list, not into the plan.
