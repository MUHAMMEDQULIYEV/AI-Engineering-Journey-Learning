# 04 · LLMs (10 weeks core · 41 weeks full)

✅ being walked by the author, see [roadmap/](../../roadmap/README.md)

This track is not written here twice. It **is** the LLM-engineer roadmap in [../../roadmap/](../../roadmap/README.md), with every study day in [plan.md](../../roadmap/plan.md).
This page only says where to enter it from the ai-map, and which part you need for your goal.

**Prerequisites:** [03 deep learning](03-deep-learning.md) (at least weeks 1–6: backprop, PyTorch loop, makemore). That is more than the "Python + basic ML" the roadmap asks for, so you can start at Block 1 · Day 1.

---

## Which part do you need?

| Part | plan.md blocks | Weeks | What you build | Who needs it |
|---|---|---|---|---|
| **Core** (counted in the ai-map total) | 1 Tokenization · 2 Attention · 3 Mini-GPT · 4 LLM apps | 1 + 2 + 3 + 4 = **10** | own BPE, NumPy attention, a mini-GPT, small LLM apps (APIs, structured output, tool calling, embeddings) | everyone who goes on to 05, 06 or 08 |
| **Full** (the LLM-engineer path) | + 5 Flagship v0 · 6 Agents + MCP · 7 Evals + production · 8 Job-ready | + 7 + 6 + 6 + 12 = **41 in total** | a deployed RAG + agent flagship with evals, a LoRA fine-tune vs API comparison, serving basics | LLM / AI engineers |

The Done lines and 🔒 closed-book checks are in [plan.md](../../roadmap/plan.md) at the end of each block. Use them as they are.
Block 2 is a light 🟡 block (≤1 h per study day) on purpose; it fits an exam period.

---

## 👀 See it (open before the matching block)

| Block | Site | What it shows |
|---|---|---|
| 1 Tokenization | [Tiktokenizer](https://tiktokenizer.vercel.app/) | type text, see the tokens and their ids live |
| 2 Attention | [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) | a live GPT-2 in the browser: attention patterns, shapes |
| 2 Attention | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/) | Q / K / V pictures |
| 3 Mini-GPT | [bbycroft LLM visualization](https://bbycroft.net/llm) | 3D walk through one small GPT, every shape |
| 4 Embeddings | [Embedding Projector](https://projector.tensorflow.org/) · [WizMap](https://poloclub.github.io/wizmap/) | embeddings in 2D / 3D (PCA, t-SNE, UMAP) |
| 4–8 | [Sam Rose: Prompt caching](https://ngrok.com/blog/prompt-caching) | interactive essay: tokens → embeddings → attention → KV cache |

Sources for every block are in [../../roadmap/resources.md](../../roadmap/resources.md) and [../../websites/README.md](../../websites/README.md).

---

## Notes for ai-map learners

- **You already did makemore** in [03](03-deep-learning.md) week 4. Block 3's "Let's build GPT" will feel familiar; that's the point.
- **nanoGPT is deprecated** (Nov 2025); Karpathy's newer repo is [nanochat](https://github.com/karpathy/nanochat) (link not checked live). For Block 3 you write your own mini-GPT anyway, so nothing changes. nanochat's full run is made for a rented multi-GPU machine; read its code, don't try to train it on free Colab.
- **Overlap with other tracks:** Block 7 (evals) uses the statistics from [01](01-math.md) weeks 5–6. Block 8 (LoRA, quantization, vLLM) overlaps [07 ML systems](07-ml-systems.md) week 4; do it once. DPO in [06](06-rl.md) week 6 builds on Block 8's LoRA setup.
- **Alternative map for this track:** [mlabonne/llm-course](https://github.com/mlabonne/llm-course). Its "LLM Scientist" part goes deeper into pretraining and post-training; its "LLM Engineer" part matches Blocks 4–8. Use it for the monthly big-picture look, not as a second course.

## 🧠 Recall list

The roadmap's session log holds these (see [learning-methods.md](../../roadmap/learning-methods.md)): BPE merge step · `softmax(QKᵀ/√d)·V` with shapes · causal mask · mini-GPT block (attention + MLP + residual + LayerNorm) · structured output with Pydantic · tool calling loop · cosine similarity + top-k search · RAG recall@5 · eval metrics · LoRA in 5 sentences.
