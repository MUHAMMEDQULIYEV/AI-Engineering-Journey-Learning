# 📅 My calendar (worked example)

This is [plan.md](plan.md) with my real dates. My study days are **Tue LEARN · Thu BUILD · Sat SHIP · Sun REVIEW**. Other days are optional / rest.
Use it as an example of how to put the plan into your own calendar. Dates are targets, and my `NEXT.md` decides what I actually do.

## Mon Oct 5 – Sun Oct 11 · Block 1 Tokenization
- Mon Oct 5 · (plan starts Tue)
- ☐ Tue Oct 6 · LEARN: vocab fix (guess the unique count first) + commit · Karpathy Tokenizer 0–40 min + 2 predicts
- Wed Oct 7 · optional / rest
- ☐ Thu Oct 8 · BUILD: Karpathy 40–80 · own char tokenizer
- Fri Oct 9 · optional / rest
- ☐ Sat Oct 10 · SHIP: BPE merge step ×10 · push
- ☐ Sun Oct 11 · REVIEW: own BPE vs `tiktoken` (Azerbaijani + English) · 🧠 why BPE? · write 2–3 candidate flagship data sources (5 min, no decision) · check-in

## Mon Oct 12 – Sun Oct 18 · Block 2 Attention 🟡 (exam week, ≤40 min, no code)
- Mon Oct 12 · rest
- ☐ Tue Oct 13 · LEARN: 3B1B ch.5 + 1 predict question
- Wed Oct 14 · rest
- ☐ Thu Oct 15 · BUILD: 3B1B ch.6 + 1 predict question
- Fri Oct 16 · rest
- ☐ Sat Oct 17 · SHIP: Karpathy GPT 0:00–0:40 (bigram), watch only
- ☐ Sun Oct 18 · REVIEW: short check-in

## Mon Oct 19 – Sun Oct 25 · Block 2 Attention 🟡 (exam week, ≤40 min, no code)
- Mon Oct 19 · rest
- ☐ Tue Oct 20 · LEARN: Karpathy 0:40–1:20 (self-attention) + 1 predict
- Wed Oct 21 · rest
- ☐ Thu Oct 22 · BUILD: Karpathy ~1:20 → end (multi-head, FFN, residual, LayerNorm) + 1 predict
- Fri Oct 23 · rest
- ☐ Sat Oct 24 · SHIP: one page "attention in my words"
- ☐ Sun Oct 25 · REVIEW: check-in · download ~1 MB Azerbaijani text for Block 3 (no code)

## Mon Oct 26 – Sun Nov 1 · Block 3 Mini-GPT (week 1)
- Mon Oct 26 · optional / rest
- ☐ Tue Oct 27 · LEARN: tiny Shakespeare (debug set) + char tokenizer · train/val split + `get_batch`, print shapes
- Wed Oct 28 · optional / rest
- ☐ Thu Oct 29 · BUILD: `nn.Embedding` bigram model, train, generate text
- Fri Oct 30 · optional / rest
- ☐ Sat Oct 31 · SHIP: `estimate_loss()` (train + val loss) + push
- ☐ Sun Nov 1 · REVIEW: 🧠 tokenization · check-in

## Mon Nov 2 – Sun Nov 8 · Block 3 Mini-GPT (week 2)
- Mon Nov 2 · optional / rest
- ☐ Tue Nov 3 · LEARN: single-head attention + causal mask, shape tests
- Wed Nov 4 · optional / rest
- ☐ Thu Nov 5 · BUILD: positional embeddings + multi-head attention (reuse your single head)
- Fri Nov 6 · optional / rest
- ☐ Sat Nov 7 · SHIP: feed-forward + residual + LayerNorm = transformer block + push
- ☐ Sun Nov 8 · REVIEW: explain attention from memory · check-in

## Mon Nov 9 – Sun Nov 15 · Block 3 Mini-GPT (week 3)
- Mon Nov 9 · optional / rest
- ☐ Tue Nov 10 · LEARN: **assemble** mini-GPT · overfit a small Shakespeare slice on CPU (loss goes down)
- Wed Nov 11 · optional / rest
- ☐ Thu Nov 12 · BUILD: train on Azerbaijani text (Colab / Kaggle GPU) · val loss < bigram val loss
- Fri Nov 13 · optional / rest
- ☐ Sat Nov 14 · SHIP: samples + loss curve plot + README with results (**repo #1**)
- ☐ Sun Nov 15 · REVIEW: LinkedIn post · check-in


## Mon Nov 16 – Sun Nov 22 · Block 4 LLM apps · course Week 1 (LLM APIs)
- Mon Nov 16 · optional / rest
- ☐ Tue Nov 17 · LEARN: course Week 1, first ≤30 min at 1.5× + predict · get API key
- Wed Nov 18 · optional / rest
- ☐ Thu Nov 19 · BUILD: next ≤30 min of Week 1 · rebuild the first app without the video
- Fri Nov 20 · optional / rest
- ☐ Sat Nov 21 · SHIP: Azerbaijani variation + push
- ☐ Sun Nov 22 · REVIEW: 🧠 BPE · pick a **tentative** flagship idea + data source · check-in

## Mon Nov 23 – Sun Nov 29 · Block 4 · rest of course Week 1 + structured output
- Mon Nov 23 · optional / rest
- ☐ Tue Nov 24 · LEARN: rest of Week 1 (≤30 min, skip what you don't need) · prompting: system prompt, few-shot
- Wed Nov 25 · optional / rest
- ☐ Thu Nov 26 · BUILD: structured output: LLM → JSON → Pydantic model, 5 test inputs
- Fri Nov 27 · optional / rest
- ☐ Sat Nov 28 · SHIP: **catch-up** (push the extractor, close everything open)
- ☐ Sun Nov 29 · REVIEW: 🧠 attention · explain the week · check-in

## Mon Nov 30 – Sun Dec 6 · Block 4 · course Week 2 (Gradio + tools)
- Mon Nov 30 · optional / rest
- ☐ Tue Dec 1 · LEARN: course Week 2, Gradio part (≤30 min) + predict
- Wed Dec 2 · optional / rest
- ☐ Thu Dec 3 · BUILD: tool-calling part (≤30 min) · Gradio UI for your Week 1 app without the video
- Fri Dec 4 · optional / rest
- ☐ Sat Dec 5 · SHIP: assistant with 1 real tool (called on 3 test prompts) + push
- ☐ Sun Dec 6 · REVIEW: 🧠 causal mask · explain the week · check-in

## Mon Dec 7 – Sun Dec 13 · Block 4 · embeddings + catch-up
- Mon Dec 7 · optional / rest
- ☐ Tue Dec 8 · LEARN: embeddings + cosine similarity on 3 sentences (predict the order first). Course Week 2 not done? Finish it today instead
- Wed Dec 9 · optional / rest
- ☐ Thu Dec 10 · BUILD: embed ~20 flagship docs (`sentence-transformers`), top-3 search on 5 questions
- Fri Dec 11 · optional / rest
- ☐ Sat Dec 12 · SHIP: finish anything open (Block 3 overflow first) + push
- ☐ Sun Dec 13 · REVIEW: 🧠 LLM API call flow · **confirm or switch the flagship idea** · check-in

## Mon Dec 14 – Sun Dec 20 · exam week 🟡 (≤40 min, no code)
- Mon Dec 14 · rest
- ☐ Tue Dec 15 · watch course Week 3 (Hugging Face) + notes
- Wed Dec 16 · rest
- ☐ Thu Dec 17 · 🧠 cold quiz: Blocks 1–2 (tokenization, BPE, attention)
- Fri Dec 18 · rest
- ☐ Sat Dec 19 · collect flagship documents (no code)
- ☐ Sun Dec 20 · short check-in

## Mon Dec 21 – Sun Dec 27 · exam week 🟡 (≤40 min, no code)
- Mon Dec 21 · rest
- ☐ Tue Dec 22 · watch course Week 5 (RAG) + notes
- Wed Dec 23 · rest
- ☐ Thu Dec 24 · 🧠 cold quiz: Blocks 3–4 (mini-GPT, APIs, tools, embeddings)
- Fri Dec 25 · rest
- ☐ Sat Dec 26 · collect + clean flagship documents, aim for ≥50 (no code)
- ☐ Sun Dec 27 · **monthly review**: write daily rows for Block 5 week 1

## Block 5 · Flagship v0 + first deploy (winter break 🔥, start with 2–3 easy days)
Daily rows are written at each review. Weekly milestones (Done criteria are in [plan.md](plan.md)):
- ☐ Dec 28 – Jan 3 · naive RAG over ≥50 docs + 20-question eval set and script
- ☐ Jan 4 – Jan 10 · chunking ×2 + hybrid search + recall@5 table
- ☐ Jan 11 – Jan 17 · reranker + error analysis + LLM-as-judge + baseline table
- ☐ Jan 18 – Jan 24 · FastAPI + Docker · latency + cost measured
- ☐ Jan 25 – Jan 31 · **buffer week** 🟡: fix the top failure causes, nothing new
- ☐ Feb 1 – Feb 7 · **deploy v0** on HF Spaces + CV/LinkedIn v1 → start applying

## Later (rows written at each monthly review)
- ☐ Feb 8 – Apr 4 · Block 6 Agents + MCP (8 weeks)
- ☐ Apr 5 – May 9 · Block 7 Evals + production (5 weeks, incl. 🟡 spring midterms (approx, late Apr))
- ☐ May 10 – Aug 1 · Block 8 Job-ready (12 weeks, incl. 🟡 spring finals (approx)) → end of the 10 months
