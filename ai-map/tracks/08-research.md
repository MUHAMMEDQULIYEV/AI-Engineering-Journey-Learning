# 08 · Research skills (3 weeks + 1 paper every 2 weeks from track 03)

🧪 draft, not walked yet

**Goal:** you can read a paper in 3 passes, reproduce one small result on free Colab, change one thing, and write up what you found, including what didn't work.
**Done:** a 2-page report with a reproduced number, an ablation table (3 seeds) and an honest "deviations + negative results" section, pushed · 🔒 explain the paper's main idea in 5 sentences with the paper closed, then write its core piece in ≤20 lines, no notes.

**Prerequisites:** [03 deep learning](03-deep-learning.md). The dedicated weeks come last, after the tracks your goal needs.

Day jobs: [../../roadmap/README.md](../../roadmap/README.md). LEARN = 👀 first, ≤30 min reading, 1 predict question. BUILD = without the paper open. SHIP = push. REVIEW = AI-off recall + blank-file rebuild.

---

## Part 1 · In parallel, from track 03 on: 1 paper every 2 weeks

On every **second REVIEW day**, after the 🧠 recall: ~45 min with one paper that fits the track you're in.
1. Pass 1 (10 min): title, abstract, figures, conclusion. Write: what problem, what claim, what number.
2. Pass 2 (30 min): the method + one key equation. Skip proofs.
3. Close it. 5 sentences from memory in `papers/notes.md` (Feynman, see [learning-methods.md](../../roadmap/learning-methods.md)). That's the commit.

Suggested papers (find them on [HF Papers](https://huggingface.co/papers) or [alphaXiv](https://www.alphaxiv.org/) by searching the title; use search only, don't scroll the feeds):

| Track | Papers |
|---|---|
| [03](03-deep-learning.md) | *Adam* (Kingma & Ba, 2014) · *Dropout* (Srivastava et al., 2014) · *Batch Normalization* (Ioffe & Szegedy, 2015) · *ResNet* (He et al., 2015) |
| [04](04-llms.md) | *Attention Is All You Need* (Vaswani et al., 2017) · *LoRA* (Hu et al., 2021) |
| [05](05-vision-generative.md) | *ViT* (Dosovitskiy et al., 2020) · *DDPM* (Ho et al., 2020) |
| [06](06-rl.md) | *DQN* (Mnih et al., 2015) · *PPO* (Schulman et al., 2017) · *DPO* (Rafailov et al., 2023) |

Tracks 03–07 are 36 weeks, so that's about 18 papers over the whole map, without extra study days. Pick from this table and add your own.

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| Reading papers | [S. Keshav, *How to Read a Paper*](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) (3-pass method, 2 pages) | [HF Papers](https://huggingface.co/papers) · [alphaXiv](https://www.alphaxiv.org/) (search only) · Andrew Ng's reading-papers lecture (YouTube) | [Connected Papers](https://www.connectedpapers.com/) (citation graph of one paper) |
| Why clear writing matters | [Distill: Research Debt](https://distill.pub/2017/research-debt/) | — | the Distill articles from earlier tracks, as examples |
| Reproducing | a small result you can run on Colab. Default: Shakespeare-char from [nanoGPT](https://github.com/karpathy/nanoGPT) | [nanochat](https://github.com/karpathy/nanochat) (successor, link not checked, made for big GPUs) | — |
| Writing up | [Lilian Weng's blog](https://lilianweng.github.io/) as a style model | — | — |

nanoGPT is deprecated (Nov 2025). That's fine here: a frozen repo with a known number in its README is exactly what you want to reproduce. Any small result works too: a table from one of your Part 1 papers on MNIST / CIFAR-10, or a number from a course notebook.

---

## Block A · Read, reproduce, write (3 weeks)

### Week 1 · Reading well

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Connected Papers on *ResNet* (see what it builds on) · Keshav's 2 pages (≤30 min) · predict: before reading the results section, write the main number you expect (e.g. error on a benchmark) | notes |
| ☐ BUILD | Without help: 3 passes on paper 1 (the one you'll reproduce). Write: claim, setup (data, model size, steps), the exact number to match | 1-page notes |
| ☐ SHIP | 3 passes on paper 2 (a related or a later one). 1 page: what changed between them and why. Read Distill Research Debt. Push | 2 pages + commit |
| ☐ REVIEW | AI-off: 🧠 one paper from Part 1 in 5 sentences · decide the reproduction target + the number + the compute budget (≤2 h of Colab total) | target written down |

### Week 2 · Reproduce one number

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Read the code or the paper's setup section once more (≤30 min) · predict the val loss / accuracy you'll get on your budget, and how far from the paper | prediction in notes |
| ☐ BUILD | Run it on Colab with a fixed seed. Log every setting you changed from the paper (smaller model, fewer steps) | first number |
| ☐ SHIP | 2 more seeds → mean ± std. Compare with the paper's number. Push the config + log | 3-seed table |
| ☐ REVIEW | AI-off: 🧠 3-pass method · list every deviation from the paper and guess its effect | deviation list |

### Week 3 · One ablation + the write-up

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Pick one thing to change (e.g. dropout 0 vs 0.2, context length 64 vs 256, lr ×0.3). Predict: up or down, and by how much? | prediction |
| ☐ BUILD | Run the ablation, 3 seeds each | ablation table |
| ☐ SHIP | 2-page report: question · setup · reproduced number vs paper · ablation table + 1 plot · deviations · negative results (what didn't work) · next step. Push | **report** ✅ |
| ☐ REVIEW | AI-off: 🔒 explain the paper in 5 sentences, then write its core piece in ≤20 lines | the 🔒 check |

**Done:** the report is in the repo with the reproduced number (3 seeds), the ablation and a negative-results section · 🔒 explain the paper in 5 sentences, then write its core piece in ≤20 lines, no notes.

---

## Build project

**"One small reproduction, honestly reported."** A 2-page write-up in Markdown: the claim, your reproduced number (mean ± std over 3 seeds) next to the paper's, one ablation, every deviation, and what didn't work. Small compute (≤2 h free Colab), clear writing. Put the link in your main README; this is the piece that shows you can do research, not only follow courses.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- the 3 passes, and what you write after each
- what makes a reproduction fair (same data, budget, metric, seeds)
- why 3 seeds, and how to report mean ± std
- one ablation = one change
- each paper from Part 1 in 5 sentences (one ladder row per paper)
