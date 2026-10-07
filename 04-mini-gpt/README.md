# 04 · Mini-GPT from scratch (Block 3) → portfolio repo #1
Goal: build a small GPT in PyTorch and train it on Azerbaijani text.
Plan: [roadmap/plan.md → Block 3](../roadmap/plan.md#block-3--mini-gpt-from-scratch-3-weeks-a-cap--portfolio-repo-1)

3 weeks is the cap, not the target. **Corpus:** Azerbaijani text is the deliverable; tiny Shakespeare is the warm-up and debug set.
Karpathy's video is lookup only: re-watch one part when stuck, then close it.

## Days
Week 1
- [ ] LEARN · load tiny Shakespeare, encode with my Block 1 char tokenizer · train/val split (90/10) + `get_batch` → `xb`, `yb` shapes printed
- [ ] BUILD · `nn.Embedding` bigram model + training loop, generate text
- [ ] SHIP · `estimate_loss()`: mean train + val loss over N batches · push
- [ ] REVIEW · 🧠 tokenization · check-in

Week 2
- [ ] LEARN · single-head self-attention + causal mask, shape tests
- [ ] BUILD · positional embeddings + multi-head attention (reuse my single head)
- [ ] SHIP · feed-forward + residual + LayerNorm = transformer block · push
- [ ] REVIEW · explain attention from memory · check-in

Week 3
- [ ] LEARN · assemble mini-GPT, overfit a small Shakespeare slice on CPU to find bugs
- [ ] BUILD · train on **Azerbaijani text** (Colab / Kaggle GPU), log train + val loss
- [ ] SHIP · samples + loss curve plot + README with results · push
- [ ] REVIEW · LinkedIn post · check-in

## Done when
- [ ] on Azerbaijani text, mini-GPT val loss < bigram val loss
- [ ] loss plot + 3 samples + the numbers in this README
- [ ] 🔒 explain causal self-attention in 5 sentences, then write one attention head with the causal mask in ≤20 lines, no notes

## Results
_(fill in after training: val loss bigram vs mini-GPT, loss plot, 3 samples)_

## Files (I create them)
- notebook(s)
- `notes.md`: in my own words
