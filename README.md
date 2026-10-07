# AI Engineering Journey 🚀

My public learning log on the way to becoming an **AI engineer who builds apps with LLMs** (RAG, agents, MCP, evals).
I'm an IT student at INHA University, graduating in 2027. Every study session here ends with a commit.

## 🗺️ The roadmap (free to use)
**→ [roadmap/](roadmap/README.md)**: a day-by-day plan from tokenization to a deployed RAG + agent project, for people with Python + basic ML, ~11 h/week and no GPU.

| | |
|---|---|
| [Plan, block by block](roadmap/plan.md) | every study day: LEARN · BUILD · SHIP · REVIEW |
| [Resources](roadmap/resources.md) | courses (Udemy + free), books, free legal PDFs |
| [Using an AI tutor](roadmap/ai-tutor.md) | how to use Claude without letting it do your thinking |
| [Bad days](roadmap/bad-days.md) | what to do when you feel tired or unmotivated |
| [Templates](roadmap/templates/) | NEXT line, session log, weekly check-in |

## 📈 My progress

| Block | Topic | Folder | Status |
|---|---|---|---|
| 0 | PyTorch basics: tensors, DataLoader, training loop (FashionMNIST, 86% test acc) | [01-pytorch-basics](01-pytorch-basics/) | ✅ |
| 0 | CNN: ResNet BasicBlock in PyTorch | [CNN/ResNet](CNN/ResNet/) | ✅ block only |
| 1 | Tokenization: NLTK tokenizers, stemming, lemmatization → own BPE | [02-nlp-tokenization](02-nlp-tokenization/) | 🔄 |
| 2 | Attention (watch + notes) | [03-attention](03-attention/) | ⏳ |
| 3 | Mini-GPT from scratch | [04-mini-gpt](04-mini-gpt/) | ⏳ |
| 4 | LLM apps: APIs, structured output, tool calling, embeddings | [05-llm-apps](05-llm-apps/) | ⏳ |
| 5–7 | Flagship: RAG v0 → agent + MCP → evals + production | [06-flagship](06-flagship/) | ⏳ |
| 8 | Open model vs API: LoRA fine-tune | [07-lora-finetune](07-lora-finetune/) | ⏳ |
| 8 | Serving basics: quantization + vLLM | [08-serving-basics](08-serving-basics/) | ⏳ |

Earlier ML work: [Cluster-Algorithm](Cluster-Algorithm/) (K-Means, DBSCAN) · [Projects](Projects/) · [CIFAR10-Implementation](https://github.com/MUHAMMEDQULIYEV/CIFAR10-Implementation) (separate repo)

## Setup
```bash
uv sync                     # Python env (PyTorch CPU build)
uv run jupyter lab          # or open notebooks in VS Code
```
GPU training runs on Google Colab or Kaggle.

License: [MIT](LICENSE). Use the roadmap however you like. A ⭐ or a link back is appreciated.
