# 06 · Flagship (Blocks 5–7) → portfolio repo #2
Goal: a RAG app + agent + MCP server, deployed, with an eval write-up. May move to its own repo later.
Plan: [roadmap/plan.md → Block 5](../roadmap/plan.md#block-5--flagship-v0--first-deploy-7-weeks-holiday-) · [Block 6](../roadmap/plan.md#block-6--agents--mcp-6-weeks) · [Block 7](../roadmap/plan.md#block-7--evals--production-6-weeks-incl--spring-midterms-approx)

Number targets are not gates: **report the number, timebox ≤2 days to improve it, then ship.**

## Block 5 · Flagship v0 + first deploy (7 weeks)
- [ ] 1 · naive RAG over ≥50 docs (vector DB) + 20-question eval set + script → prints a score for all 20
- [ ] 2 · chunking (2 sizes) + recall@5 per config · stretch: hybrid search (BM25 + embeddings)
- [ ] 3 · error analysis (label every failure) + baseline: LLM without retrieval vs RAG · stretch: LLM-as-judge (TPR/TNR), reranker
- [ ] 4 · FastAPI `/ask` + Docker · Langfuse tracing · pytest · GitHub Actions eval gate · p50 latency + cost per question
- [ ] 5 · 🟡 buffer: fix top failure causes, nothing new
- [ ] 6 · deploy v0 on Hugging Face Spaces, README with eval scores + baseline table

**Done:** live link · ≥50 docs · 20-question eval in CI · recall@5 + pass rate next to baselines · p50 latency + cost · Langfuse + pytest + GitHub Actions · 🔒 explain the RAG pipeline in 5 sentences, then write `recall_at_k` in ≤20 lines, no notes.

## Block 6 · Agents + MCP (6 weeks)
- [ ] 1–2 · agent with ≥2 tools (one is the retriever) → right tool on 8/10 test questions, pass rate not lower than v0
- [ ] 3 · MCP server → ≥2 tools called from an MCP client
- [ ] 4 · agent evals + observability: label 20 traces, tool-choice checks in CI
- [ ] 5 · prompt-injection safety: 5 attack questions + a guardrail → ≥4/5 blocked
- [ ] 6 · grow to ≥100 docs, redeploy · 1 OSS PR or 1 public post

**Done:** agent + MCP server here · tool-choice eval in CI · injection test ≥4/5 · 1 OSS PR or post · 🔒 explain the agent loop in 5 sentences, then write a tool-dispatch loop in ≤20 lines, no notes.

## Block 7 · Evals + production (6 weeks)
- [ ] 1 · statistics for evals: bootstrap 95% CI on the pass rate, in this README
- [ ] 2 · eval set → ~50 questions · re-check judge TPR/TNR · open-model switch via config flag
- [ ] 3 · A/B test configs with CIs · full set on `main`, 20-question subset on PRs
- [ ] 4–5 · 🟡 spring midterms: light weeks, notes only
- [ ] 6 · caching + model routing, p50/p95 before/after · redeploy · eval write-up

**Done:** ~50-question eval with bootstrap CI · judge TPR/TNR · CI eval gate green on `main` · eval write-up published · p95 latency/cost before and after · works with API and open model · 🔒 explain the bootstrap CI in 5 sentences, then code it in ≤20 lines, no notes.

## Results
_(fill in: recall@5, pass rate + CI, baselines, p50/p95 latency, cost per question, live link)_
