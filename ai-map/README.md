# 🧭 AI map: from Python to AI engineer or researcher

A full "learn AI" roadmap in 9 tracks, from setup and math to LLMs, vision, RL, ML systems and research.
Every track has weekly plans with 4 study days, one main source per topic, a 👀 visual site to open first, a portfolio project and a 🔒 closed-book check.

The LLM part is my own roadmap in [../roadmap/](../roadmap/README.md), which I'm walking now. The other tracks are 🧪 drafts: planned and source-checked (Oct 2026), but not walked yet. I'll mark each one as I go.

**Who it's for**
- You know **Python** (functions, loops, lists, dicts) but **no ML** yet.
- You have about **11 hours a week**: 4 study days of ~2.5–3 h.
- You have **no GPU**. Free Google Colab and Kaggle are enough for every project here.
- You want to *build* things, not collect certificates.

---

## How to use it

1. Read the rules once: [../roadmap/README.md](../roadmap/README.md). The day jobs (LEARN · BUILD · SHIP · REVIEW), `NEXT.md` as the truth, 70/30 coding, buffers and "never miss twice" apply to every track.
2. Pick your goal in the [goal → path table](#goal--path) below. Do only the tracks on your path.
3. Open the first track, Week 1, ☐ LEARN. Do only that. Tick the box when its Output exists.
4. Keep one `NEXT.md` and one session log: copy them from [../roadmap/templates/](../roadmap/templates/).

| Need help with… | File |
|---|---|
| which study method fits (predict, recall, blank-file rebuild) + the gap ladder 1 → 3 → 7 → 21 → 60 days | [learning-methods.md](../roadmap/learning-methods.md) |
| using Claude or another AI as a tutor, not an answer machine | [ai-tutor.md](../roadmap/ai-tutor.md) |
| tired, bored, lost | [bad-days.md](../roadmap/bad-days.md) |
| learning from a YouTube video | [videos/RULES.md](../videos/RULES.md) |
| which websites are main / lookup / 👀 visual / skip | [websites/README.md](../websites/README.md) |
| the fixed shape of every track file | [_track-template.md](_track-template.md) |

**Every week, in every track:**

| Day | Job |
|---|---|
| ☐ LEARN | open the 👀 visual first (5 min) → ≤30 min video or reading → write + answer 1 predict question → code the idea |
| ☐ BUILD | write the main thing **without the video** |
| ☐ SHIP | fix, test, README, commit + push |
| ☐ REVIEW | **AI-off**: 🧠 recall from the gap ladder + a blank-file rebuild. The AI checks only afterwards |

A block is finished when its **Done** line is true, not when its weeks run out.

---

## The tracks

| # | Track | Weeks | Prereqs | Output project | Status |
|---|---|---|---|---|---|
| 00 | [Setup: git, uv, notebooks, NumPy, pandas, SQL, data cleaning](tracks/00-setup.md) | 2 | Python | one messy table, cleaned (SQL = pandas answers) | 🧪 draft |
| 01 | [Math: linear algebra, calculus, probability + stats](tracks/01-math.md) | 6 | 00 | PCA + linear regression + bootstrap CI from scratch in NumPy | 🧪 draft |
| 02 | [Classical ML: scikit-learn, CV, trees, boosting, pipelines](tracks/02-classical-ml.md) | 8 | 00, 01 (weeks 1–4) | Kaggle tabular: baseline vs gradient boosting + error analysis | 🧪 draft (example work linked) |
| 03 | [Deep learning: backprop, PyTorch, training well, CNNs, RNNs](tracks/03-deep-learning.md) | 9 | 01, 02 | micrograd → CIFAR-10 ResNet with an ablation table | 🟡 partly walked |
| 04 | [LLMs → bridge to roadmap/](tracks/04-llms.md) | 10 core (41 full) | 03 | mini-GPT + LLM apps (full: deployed RAG + agent flagship) | ✅ being walked |
| 05 | [Vision + generative: transfer learning, ViT, YOLO, VAE, diffusion](tracks/05-vision-generative.md) | 6 | 03 (04 Blocks 2–3 for ViT) | ResNet vs ViT table + tiny DDPM on MNIST | 🧪 draft |
| 06 | [RL → RLHF / DPO](tracks/06-rl.md) | 6 | 03; 04 for weeks 5–6 | own DQN on CartPole + DPO on a 0.5B model | 🧪 draft |
| 07 | [ML systems: MLOps, serving, quantization, safety basics](tracks/07-ml-systems.md) | 5 | 02, 03 (04 for week 4) | one model shipped: MLflow + Docker + CI + drift + 4-bit benchmark | 🧪 draft |
| 08 | [Research skills: read, reproduce, write](tracks/08-research.md) | 3 (+ 1 paper / 2 weeks from 03 on) | 03 | 2-page reproduction report with an ablation | 🧪 draft |

**Total: 2 + 6 + 8 + 9 + 10 + 6 + 6 + 5 + 3 = 55 weeks ≈ 600 hours** at 11 h/week, about **13 months** of calendar time with the monthly catch-up days.
With the full LLM track (all 8 blocks of [plan.md](../roadmap/plan.md), 41 weeks instead of 10) it's 86 weeks. Nobody needs all of it: pick a path below.

---

## How the tracks depend on each other

```
00 setup ─► 01 math ─► 02 classical ML ─► 03 deep learning ─┬─► 04 LLMs ─────────► 06 RL → RLHF/DPO
                                                             │      │ (attention)
                                                             ├──────┴─► 05 vision + generative
                                                             └─► 07 ML systems (needs a model from 02/03)

08 research: 1 paper / 2 weeks on REVIEW days from 03 on ─► 3 dedicated weeks at the end
```

- 01 is "just enough" math. If you're keen to start ML, begin 02 after 01 week 4 and do 01 weeks 5–6 next to 02.
- 06 comes after 04 because its last 2 weeks (RLHF, DPO) fine-tune an LLM. Weeks 1–4 (classic RL) only need 03.

---

## Goal → path

| Goal | Path | Weeks |
|---|---|---|
| **LLM / AI engineer** (apps: RAG, agents, evals, deploy) | 00 → 01 weeks 1–4 → 02 weeks 1–5 → 03 weeks 1–6 + 9 → **04 full** ([roadmap/](../roadmap/README.md)) · optional: 06 weeks 5–6 (DPO) | 2 + 4 + 5 + 7 + 41 = **59** |
| **ML engineer** (train + ship models) | 00 → 01 → 02 → 03 → 04 core → **07** · optional: 05 | 2 + 6 + 8 + 9 + 10 + 5 = **40** |
| **CV engineer** | 00 → 01 → 02 weeks 1–5 → 03 → 04 Blocks 2–3 (attention, mini-GPT) → **05** → 07 | 2 + 6 + 5 + 9 + 5 + 6 + 5 = **38** |
| **Researcher** (read + reproduce papers, grad school) | 00 → 01 → 02 → 03 → 04 core → 05 → 06 → **08** (+ papers from 03 on) · 07 later | 2 + 6 + 8 + 9 + 10 + 6 + 6 + 3 = **50** |
| **Everything** | all 9 tracks, 04 core | **55** |

Already know some of it? Do the track's 🔒 closed-book checks cold. If you pass all of a block's checks, skip the block.
Already know Python + basic ML and only want LLM apps? Go straight to [../roadmap/](../roadmap/README.md) (41 weeks).

---

## How this compares to other roadmaps

> I read the big public roadmaps before writing this (Oct 2026). They agree on the order (Python + math → classical ML → neural nets → transformers / LLMs → deployment), and this map follows it too. What's different here:
> - **Pacing:** every week has 4 concrete study days for ~11 h/week. Most roadmaps are topic lists with no time attached.
> - **Building:** every week ends in code you pushed, and every track ends in a portfolio project. Not a link list.
> - **Spaced recall:** every track has a 🧠 recall list for the 1 → 3 → 7 → 21 → 60 day ladder. None of the roadmaps I checked had this.
> - **Closed-book checks:** a 🔒 check per block (explain in 5 sentences + ≤20 lines from a blank file). A shipped repo isn't proof you understand it.
> - **No GPU needed**, **one main source per topic** (free first), and **research skills** as their own track.
> - **Honest status:** tracks I haven't walked are marked 🧪 draft.
>
> Good alternatives, if you want a different shape:
> - [mlabonne/llm-course](https://github.com/mlabonne/llm-course): the best map for LLMs (LLM Scientist + LLM Engineer parts). No pacing.
> - [roadmap.sh: ML Engineer](https://roadmap.sh/machine-learning) and [roadmap.sh: AI Engineer](https://roadmap.sh/ai-engineer): clean topic trees.
> - [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch): very wide (19+ phases, ~300 h), good if you want breadth.

Not covered here (on purpose, to keep it finishable): speech / audio, recommender systems, time series. Add them to your ideas list and pick one after your path is done.

License: [MIT](../LICENSE), like the rest of the repo.
