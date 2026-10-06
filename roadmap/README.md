# 🗺️ AI Engineer Roadmap (LLM apps), 2026–2027

A day-by-day roadmap for becoming an **AI engineer who builds apps with LLMs**: RAG, agents, tool calling, MCP, evals and deployment.
I made it for myself and I follow it in public in this repo. You can copy it and use it too.

**Who it's for**
- You know **Python** and some basic ML (regression, a neural network, gradient descent).
- You have about **10–12 hours a week**, for example 4 study days of about 3 hours.
- You have **no GPU**. Google Colab and Kaggle are enough.
- You often don't know what to study next, or you watch courses but don't build.

**What you get at the end:** a mini-GPT you built yourself, several small LLM apps, and one **flagship project** (a RAG app with an agent, deployed, with evals) that you can show to employers.

---

## The 4 phases

| Phase | Months | Focus | Output |
|---|---|---|---|
| **1. Foundations** | 1–2 | Tokenization, BPE, embeddings, attention, a transformer from scratch (PyTorch) | Mini-GPT repo |
| **2. LLM apps** | 3–4 | LLM APIs, prompting, structured output, tool calling, Gradio, Hugging Face, RAG | Small apps + flagship v0 |
| **3. Agents** | 5–6 | Agents, MCP, FastAPI, Docker, deploy | Flagship project with an agent, deployed |
| **4. Quality + job** | 7–9 | Evals, statistics for evals, LoRA basics, portfolio, CV | Job-ready GitHub |

Why this order: most "AI engineer" jobs in 2026 are about the **application layer** (APIs → RAG → agents → evals → deploy), not training models.
Phase 1 is short on purpose. It makes you *understand* what an LLM does, and then you move on to building.

Full plan with every day: **[plan.md](plan.md)** · My real dates as an example: **[my-calendar-2026-27.md](my-calendar-2026-27.md)**

---

## Every study day has a fixed job

Pick 4 days a week that are usually free. Give each day one job:

| Day | Job | Done when |
|---|---|---|
| Day A | **LEARN**: ≤30 min video, then predict questions, then code the idea | the concept runs in a notebook + 3 lines of notes |
| Day B | **BUILD**: write the main thing *without the video* | it runs end to end (ugly is fine) |
| Day C | **SHIP**: fix, test, README, commit + push | a commit on GitHub |
| Day D | **REVIEW**: explain the week from memory, plan next week | next week is written down |

Other days are **optional**. Nothing later depends on them, so zero is fine.

---

## Core rules

1. **Your `NEXT.md` is the truth. Dates are only targets.** If you slip, continue from NEXT and move the dates. Never skip work just to "catch up to the date".
2. **One course + one project open at a time.** Every other resource is *lookup only*: open it for one question, then close it.
3. **70/30:** at least 70% coding, at most 30% watching.
4. **Every session ends with a commit** and a one-line NEXT.
5. **Predict before you run.** Before each cell, write what you think it will print or what shape it will have.
6. **Buffers:** the last SHIP day of every month is a catch-up day. Before a big deadline, keep one empty week.
7. **Exam weeks are light weeks** (≤40 min per day, watch + notes, no new code). They are planned, not failures.
8. **Never miss twice.** Missing one day is normal. Two in a row is the start of quitting.

---

## Files in this folder

| File | What's inside |
|---|---|
| [plan.md](plan.md) | Block-by-block plan, every study day |
| [my-calendar-2026-27.md](my-calendar-2026-27.md) | The same plan with my real dates (Oct 2026 →), as an example |
| [resources.md](resources.md) | Courses (Udemy + free), books, free legal PDFs |
| [ai-tutor.md](ai-tutor.md) | How to use Claude (or any AI assistant) as a tutor, not an answer machine |
| [bad-days.md](bad-days.md) | What to do when you feel tired, bored, lost or unmotivated |
| [templates/](templates/) | `NEXT.md`, session log and weekly check-in templates |

## How to start today
1. Copy `templates/NEXT.md` into your own repo.
2. Pick your 4 study days and write them in your calendar.
3. Open [plan.md](plan.md) → Block 1 · Day 1. Do only that.

Built from my own experience and these public roadmaps: [codebasics 2026](https://codebasics.io/blog/software-engineer-to-ai-engineer-complete-roadmap-for-2026), [Louis Bouchard](https://www.louisbouchard.ai/how-to-learn-ai-engineering-2026/), [mlabonne/llm-course](https://github.com/mlabonne/llm-course) (LLM Engineer track).
Then I checked the plan twice, once for its strengths and once for where it would break, and fixed the weak parts.
