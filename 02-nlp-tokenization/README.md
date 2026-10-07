# 02 · Tokenization (Block 1)
Goal: know how text becomes numbers, and build your own tokenizer.
Plan: [roadmap/plan.md → Block 1](../roadmap/plan.md#block-1--tokenization-1-week)

## Days
- [ ] LEARN · Karpathy *"Let's build the GPT Tokenizer"* 0–40 min · 2 predict questions · `split(" ")` vs a real word tokenizer on 2 own sentences (tokens + unique tokens)
- [ ] BUILD · Karpathy 40–80 min · own **character tokenizer**: `encode`, `decode`, test `decode(encode(x)) == x`
- [ ] SHIP · one **BPE merge step**: count pairs, merge the most frequent, repeat ×10 · push
- [ ] REVIEW · my BPE vs `tiktoken` on English + Azerbaijani (token counts) · 🧠 why BPE? · 2–3 candidate flagship data sources

Optional: stemming, lemmatization, stopwords.

## Done when
- [ ] char tokenizer round-trip test passes
- [ ] BPE runs 10 merges
- [ ] token-count table (my BPE vs `tiktoken`, 2 languages) in the repo
- [ ] 🔒 explain BPE in 5 sentences, then write one merge step in ≤20 lines, no notes

## Files
- `tokenization.ipynb`
- `notes.md`: in my own words
