# 📚 Resources

**Rule:** one **main** source per topic. Everything in "lookup only" is for one question at a time: open it, find the answer, close it.

## Courses and videos

| Topic | Main source | Cost | Lookup only |
|---|---|---|---|
| Tokenization, BPE | [Karpathy: Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | free | Krish Naik *Data Science/ML/DL/NLP Bootcamp* (Udemy), NLP preprocessing lectures |
| Attention intuition | [3Blue1Brown: Neural networks, ch.5–6](https://www.3blue1brown.com/topics/neural-networks) | free | *Understanding Deep Learning* ch.12 |
| Mini-GPT | [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (Neural Networks: Zero to Hero) | free | Raschka's book (below) |
| LLM APIs, Gradio, tools, HF, RAG, fine-tuning | **[Ed Donner: AI Engineer Core Track](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/)** (Udemy) | paid / Udemy subscription | [HF LLM Course](https://huggingface.co/learn/llm-course), [OpenAI Cookbook](https://cookbook.openai.com), Anthropic Academy (Claude API) |
| Vector databases | — | — | Chroma / pgvector docs |
| Agents | **[Hugging Face Agents Course](https://huggingface.co/learn/agents-course)** | free + certificate | Ed Donner *AI Engineer Agentic Track* (Udemy) |
| MCP | **[Hugging Face MCP Course](https://huggingface.co/learn/mcp-course)** | free + certificate | Anthropic Academy MCP course |
| Evals | [Hamel Husain: Evals FAQ + free email course](https://ai.hamel.dev/eval-course), DeepLearning.AI *Production-Ready AI Agents* | free | deepeval docs |
| Deploy | FastAPI docs + Docker *Get started* | free | — |
| Big map | [mlabonne/llm-course](https://github.com/mlabonne/llm-course), LLM Engineer track | free | monthly review only |

**Money and hardware:** budget about **$10** for an API key (OpenRouter or OpenAI) when Block 4 starts. Local models with Ollama work only for small (1–3B) models on 8 GB RAM. GPU: Google Colab, with **Kaggle** (about 30 GPU hours/week) as the backup.

**What I don't use:** many overlapping "complete AI bootcamp" courses, paid cohorts, and a new course every month. If you have a Udemy subscription, put only your 1–2 active courses in one list and open Udemy only through that list.

## Books
Read only the chapter for the current block. Borrow at most 2 at a time (1 main + 1 reference).

| Block | Book | Use | Free code |
|---|---|---|---|
| 1–3 ⭐ | Sebastian Raschka, *Build a Large Language Model (From Scratch)*, Manning 2025 | ch.2 tokenization/BPE, ch.3 attention, ch.4 GPT | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) |
| 4–5 ⭐ | Jay Alammar & Maarten Grootendorst, *Hands-On Large Language Models*, O'Reilly 2024 | embeddings, semantic search, RAG, prompting | [HandsOnLLM](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) |
| 4 (ref) | Lewis Tunstall et al., *Natural Language Processing with Transformers*, O'Reilly 2022 | Hugging Face pipelines, tokenizers | [nlp-with-transformers/notebooks](https://github.com/nlp-with-transformers/notebooks) |
| 6 (ref) | Mayo Oshin & Nuno Campos, *Learning LangChain*, O'Reilly 2025 | only if your agent uses LangGraph | — |
| 7–8 | Chip Huyen, *Designing Machine Learning Systems*, O'Reilly 2022 | production, monitoring, evals mindset | — |
| 7–8 | Chip Huyen, *AI Engineering*, O'Reilly 2025 | the whole LLM-app stack | — |
| optional | Martin Kleppmann, *Designing Data-Intensive Applications* | backend depth for interviews | — |

### Free and legal PDFs / online books
- Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft: [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/) (tokenization, embeddings, transformers, RAG)
- Simon Prince, *Understanding Deep Learning*: [udlbook.github.io](https://udlbook.github.io/udlbook/) (ch.12 transformers)
- Zhang et al., *Dive into Deep Learning*: [d2l.ai](https://d2l.ai) (ch.11 attention)
- James et al., *An Introduction to Statistical Learning with Python (ISLP)*: [statlearning.com](https://www.statlearning.com) (statistics refresh, Block 8)
- Deisenroth et al., *Mathematics for Machine Learning*: [mml-book.github.io](https://mml-book.github.io)

For paid books: use your university library plus the free official code repos. No pirated PDFs.

### For INHA University students 🇰🇷
All of these are English editions at 정석학술정보관 (checked in the catalog on 2026-10-06):

| Book | Call number |
|---|---|
| Raschka, *Build a Large Language Model (From Scratch)* | 006.3 R223b |
| Alammar, *Hands-On Large Language Models* | 006.35 A318h |
| Tunstall, *NLP with Transformers* | 006.35 T927n |
| Oshin, *Learning LangChain* | 006.3 O82L |
| Huyen, *Designing Machine Learning Systems* | 006.31 H987d |
| Kleppmann, *Designing Data-Intensive Applications* | 005.3 K64d |
| Stevens, *Deep Learning with PyTorch* | 006.31 S844d |
| Prince, *Understanding Deep Learning* | 006.31 P954u |
| James, *ISL with Applications in Python* | 519.5 I59n |

*AI Engineering* (Huyen) and *LLM Engineer's Handbook* are only in Korean translation there.
