# 📚 Resources

**Rule:** one **main** source per topic. Everything in "lookup only" is for one question at a time: open it, find the answer, close it.

## Courses and videos

| Block | Topic | Main source | Cost | Lookup only |
|---|---|---|---|---|
| 1 | Tokenization, BPE | [Karpathy: Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | free | Krish Naik *Data Science/ML/DL/NLP Bootcamp* (Udemy), NLP preprocessing lectures |
| 2 | Attention intuition | [3Blue1Brown: Neural networks, ch.5–6](https://www.3blue1brown.com/topics/neural-networks) | free | *Understanding Deep Learning* ch.12 |
| 3 | Mini-GPT | [Karpathy: Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY) (Neural Networks: Zero to Hero) | free | Raschka's book (below), lookup only |
| 4–5 | LLM APIs, Gradio, tool calling, HF, RAG, fine-tuning | **[Ed Donner: AI Engineer Core Track](https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models/)** (Udemy) | paid / Udemy subscription | [HF LLM Course](https://huggingface.co/learn/llm-course), [OpenAI Cookbook](https://cookbook.openai.com), Anthropic Academy (Claude API + MCP courses) |
| 4–8 | API reference | the docs of the provider you use: [Anthropic API docs](https://docs.claude.com) (verify URL), [OpenAI API docs](https://platform.openai.com/docs) | free | — |
| 4 | Structured output | [Pydantic docs](https://docs.pydantic.dev) (define the schema) | free | your provider's structured-output / tool-use docs |
| 5 | Retrieval, vector databases | *Hands-On LLMs* ch.8 (semantic search + RAG) + [Chroma docs](https://docs.trychroma.com) | library / free | pgvector docs, rank_bm25 |
| 4–5 | Multilingual embeddings (Azerbaijani text) | [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) or [intfloat/multilingual-e5](https://huggingface.co/intfloat/multilingual-e5-base) (verify Azerbaijani quality on 10 of your own queries) | free | [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) |
| 5 | Deploy | FastAPI docs + Docker *Get started* | free | — |
| 6 | Agents | **[Hugging Face Agents Course](https://huggingface.co/learn/agents-course)** | free + certificate | Ed Donner *AI Engineer Agentic Track* (Udemy) |
| 6 | MCP | **[Hugging Face MCP Course](https://huggingface.co/learn/mcp-course)** | free + certificate | [MCP docs](https://modelcontextprotocol.io) |
| 7 | Evals | Hamel Husain: Evals FAQ + free email course ([ai.hamel.dev/eval-course](https://ai.hamel.dev/eval-course), verify URL) | free | DeepLearning.AI short course on production AI agents (title "Production-Ready AI Agents", verify), deepeval docs |
| 7 | Tracing, cost, latency | [Langfuse docs](https://langfuse.com/docs) | free tier | Arize Phoenix docs (verify) |
| 8 | LoRA fine-tuning | [HF PEFT docs](https://huggingface.co/docs/peft) + [TRL `SFTTrainer` docs](https://huggingface.co/docs/trl) on **your own dataset** (see repo #3 below) | free | Ed Donner course Week 7 (LoRA/QLoRA), for the idea only |
| 8 | Quantization + serving | [vLLM docs](https://docs.vllm.ai) | free | HF Transformers quantization docs |
| 8 | Interview prep, LLM system design | *LLM Engineer's Handbook* (book below) + explaining your own flagship's design in 5 minutes | library | Chip Huyen, [ML Interviews Book](https://huyenchip.com/ml-interviews-book/) (free online) |
| from Jan, weekly 45 min | DSA + SQL practice | [LeetCode](https://leetcode.com) (easy/medium arrays, hashing, two pointers) + LeetCode *SQL 50* study plan (verify name) | free tier | [NeetCode](https://neetcode.io) roadmap, [SQLBolt](https://sqlbolt.com) |
| monthly | Big map | [mlabonne/llm-course](https://github.com/mlabonne/llm-course), LLM Engineer track | free | monthly review only |

**Ed Donner course weeks by topic** (the course gets updated, so trust the topic name over the number): Week 1 = LLM APIs, first app · Week 2 = Gradio UI + tool calling · Week 3 = Hugging Face pipelines + tokenizers · Week 5 = RAG · Week 7 = fine-tuning (LoRA/QLoRA).

**If Udemy goes away (free fallback for every Udemy part):**
- Blocks 4–5 (Ed Donner): [HF LLM Course](https://huggingface.co/learn/llm-course) (HF pipelines, tokenizers) + [OpenAI Cookbook](https://cookbook.openai.com) (API calls, tool calling, RAG examples) + [Anthropic courses on GitHub](https://github.com/anthropics/courses) (verify) + [Gradio docs](https://www.gradio.app/docs). The *Hands-On LLMs* book covers RAG.
- Block 6 (Agentic Track): nothing lost, it is lookup only; the HF Agents + MCP courses are free.
- Block 8 (LoRA): HF PEFT + TRL docs and their example notebooks (verify which notebooks are current).
- Block 1 (Krish Naik): lookup only; Karpathy + Raschka's free code cover it.

**Repo #3 (LoRA) uses its own data, not the course's.** Distill a small dataset from an API model: 500–2k examples of one narrow task (e.g. turn a question into your JSON schema), checked by a script, split train/test. Fine-tune a small open model on it and report base vs. LoRA on the test split. This makes the repo yours and it doesn't depend on any course.

**Public demo safety (before the link goes on your CV):**
- a **hard spending cap** on the API key (provider dashboard), separate from your study key
- a **rate limit** per IP (or a simple password) on the endpoint
- a **cache** for repeated questions, so a refresh doesn't cost money

**Money and hardware:** an API key (OpenRouter, OpenAI or Anthropic) from Block 4. My estimate: **about $20–40 over the whole plan** (most of it in Blocks 5–7, when evals run many calls). Set a monthly spending limit on the key. Local models with Ollama work only for small (1–3B) models on 8 GB RAM. GPU: Google Colab, with **Kaggle** (about 30 GPU hours/week) as the backup.

**What I don't use:** many overlapping "complete AI bootcamp" courses, paid cohorts, and a new course every month. If you have a Udemy subscription, put only your 1–2 active courses in one list and open Udemy only through that list.

## Books
Read only the chapter for the current block. Borrow at most 2 at a time (1 main + 1 reference).

| Block | Book | Use | Free code |
|---|---|---|---|
| 1–3 (lookup) | Sebastian Raschka, *Build a Large Language Model (From Scratch)*, Manning 2025 | lookup next to Karpathy: ch.2 tokenization/BPE, ch.3 attention, ch.4 GPT | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) |
| 4–5 ⭐ | Jay Alammar & Maarten Grootendorst, *Hands-On Large Language Models*, O'Reilly 2024 | embeddings, semantic search, RAG, prompting | [HandsOnLLM](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) |
| 4 (ref) | Lewis Tunstall et al., *Natural Language Processing with Transformers*, O'Reilly 2022 | Hugging Face pipelines, tokenizers | [nlp-with-transformers/notebooks](https://github.com/nlp-with-transformers/notebooks) |
| 6 (ref) | Mayo Oshin & Nuno Campos, *Learning LangChain*, O'Reilly 2025 | only if your agent uses LangGraph | — |
| 7–8 ⭐ | Chip Huyen, *AI Engineering*, O'Reilly 2025 | the whole LLM-app stack, evals | — |
| 8 (ref) | Paul Iusztin & Maxime Labonne, *LLM Engineer's Handbook*, Packt 2024 (verify) | end-to-end LLM system design, interview prep | — |
| optional | Chip Huyen, *Designing Machine Learning Systems*, O'Reilly 2022 | classic ML production mindset (older than LLM apps) | — |
| optional | Martin Kleppmann, *Designing Data-Intensive Applications* | backend depth for interviews | — |

### Free and legal PDFs / online books
- Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft: [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/) (tokenization, embeddings, transformers, RAG)
- Simon Prince, *Understanding Deep Learning*: [udlbook.github.io](https://udlbook.github.io/udlbook/) (ch.12 transformers)
- Zhang et al., *Dive into Deep Learning*: [d2l.ai](https://d2l.ai) (ch.11 attention)
- James et al., *An Introduction to Statistical Learning with Python (ISLP)*: [statlearning.com](https://www.statlearning.com) (statistics refresh, Block 7)
- Deisenroth et al., *Mathematics for Machine Learning*: [mml-book.github.io](https://mml-book.github.io)

For paid books: use your university library plus the free official code repos. No pirated PDFs.
Campus library: I checked which of these my library has; the call numbers are in my private notes.
