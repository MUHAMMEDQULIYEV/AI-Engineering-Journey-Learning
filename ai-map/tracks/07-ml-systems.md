# 07 · ML systems: MLOps, serving, quantization, safety basics (5 weeks)

🧪 draft, not walked yet

**Goal:** you can take a model you trained, track it, serve it behind an API in Docker, test it in CI, watch it for drift, make it smaller and faster, and check it for basic safety and fairness problems.
**Done:** one earlier model is packaged (MLflow + FastAPI + Docker + pytest + GitHub Actions + drift check) and a 4-bit vs 16-bit benchmark table is in the README · 🔒 explain the memory math of training vs inference in 5 sentences, then write a `/predict` FastAPI endpoint with a pytest test in ≤20 lines, no notes.

**Prerequisites:** [02 classical ML](02-classical-ml.md) (a model worth serving), [03 deep learning](03-deep-learning.md). Week 4 also uses [04](04-llms.md) core (a small LLM).

Day jobs: [../../roadmap/README.md](../../roadmap/README.md). LEARN = 👀 first, ≤30 min reading, 1 predict question. BUILD = **spike first**, then the docs (see [learning-methods.md](../../roadmap/learning-methods.md)). SHIP = push. REVIEW = AI-off recall + blank-file rebuild.
GPU: weeks 1–3 and 5 run on CPU. Week 4 uses the free Colab T4.
On the LLM path, [plan.md](../../roadmap/plan.md) Blocks 5, 7 and 8 already cover FastAPI + Docker, tracing and vLLM. Do those once and use this track for what's left (tracking, CI, drift, memory math).

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| Pipelines, tracking, deploy, monitoring | [MLOps Zoomcamp (DataTalksClub)](https://github.com/DataTalksClub/mlops-zoomcamp), modules 1–4 core, 5 light | [Made With ML](https://madewithml.com/) (lessons look free; parts are Anyscale marketing) · [Full Stack Deep Learning](https://fullstackdeeplearning.com/course/) (2022) | — |
| Experiment tracking | [MLflow docs](https://mlflow.org/docs/latest/index.html) | Trackio (HF) | the MLflow UI itself |
| Serving + quantization | [vLLM docs](https://docs.vllm.ai/en/latest/) | bitsandbytes · llama.cpp | [Sam Rose: Quantization](https://ngrok.com/blog/quantization) (interactive, float formats from 2-bit to bf16) · [Sam Rose: Prompt caching](https://ngrok.com/blog/prompt-caching) (KV cache) · [Netron](https://netron.app/) |
| Distributed training (concepts only) | [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | [HF Ultra-Scale Playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook) · [HF Smol Training Playbook](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook) (both Spaces were stuck on "Refreshing" when checked) | How to Scale Your Model has the diagrams |
| Safety + fairness basics | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) fairness module · prompt injection: [plan.md](../../roadmap/plan.md) Block 6 | — | — |
| ML system design (optional) | [Stanford CS329S](https://stanford-cs329s.github.io/) (2022) | Chip Huyen, *Designing ML Systems* (paid) | — |

Why MLflow and not Weights & Biases: MLflow is free, open source and runs locally. The W&B docs now redirect to CoreWeave, so its free tier may change.

---

## Block A · From notebook to service (3 weeks)

### Week 1 · Experiment tracking with MLflow

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Zoomcamp module 1 + module 2 intro (≤30 min) · predict: you log 3 runs with different `max_depth`. How many rows in the MLflow UI table? (answer: 3) | notebook + 3 lines of notes |
| ☐ BUILD | Spike first: wrap your [02](02-classical-ml.md) project's training in a `train.py` script with `mlflow.log_param`, `log_metric`, `log_model` · 3 runs | 3 runs in the UI |
| ☐ SHIP | Register the best run's model, load it back by name, predict on 5 rows. Push (not the `mlruns/` folder: add it to `.gitignore`) | commit |
| ☐ REVIEW | AI-off: 🧠 data leakage (from 02) · blank-file "log 1 run" in ≤10 lines | rebuild runs |

### Week 2 · Serving: FastAPI + Docker (Zoomcamp module 4)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Zoomcamp module 4, web service part (≤30 min) · predict: what does `curl -X POST /predict -d '{"age": 40, ...}'` return? Write the JSON before you run it | notes |
| ☐ BUILD | Spike first: FastAPI app, `/predict` with a Pydantic input model, loads the MLflow model once at start · then the docs page for the parts you used | curl works |
| ☐ SHIP | `Dockerfile` (slim Python image, `uv` or pip), `docker build` + `docker run`, same curl works. Push | container runs |
| ☐ REVIEW | AI-off: 🧠 MLflow model registry · blank-file FastAPI `/predict` in ≤15 lines | rebuild runs |

### Week 3 · Tests, CI, monitoring

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Zoomcamp monitoring module intro + the testing lessons of the best-practices module, light (≤30 min; module numbers can change, trust the topic name) · predict: you add 2 standard deviations to one feature. Does a KS test with p < 0.05 flag drift on 500 rows? (answer: yes, clearly) | notes |
| ☐ BUILD | 3 pytest tests: the API returns 200 + the right keys, bad input gives 422, the model beats the baseline on a fixed test set | tests pass |
| ☐ SHIP | GitHub Actions: run the tests on every push (green badge in the README) · `drift.py`: KS test per feature, current vs training data (stats from [01](01-math.md)). Push | green CI |
| ☐ REVIEW | AI-off: 🧠 Dockerfile lines · 🔒 blank-file `/predict` + 1 pytest test | the 🔒 check |

**Done:** MLflow runs + registered model · Docker image serves `/predict` · CI is green · drift check flags a shifted feature · 🔒 explain train/serve skew in 5 sentences, then write `/predict` + 1 test in ≤20 lines, no notes.

---

## Block B · Faster, smaller, safer (2 weeks)

### Week 4 · Inference optimization + quantization (Colab T4)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Sam Rose: Quantization, then Prompt caching (KV cache) · vLLM docs quickstart (≤30 min) · predict: 1B params in fp16 → how much memory for the weights? 4-bit? (answer: 2 GB, 0.5 GB) | notes |
| ☐ BUILD | Spike first: load a ~0.5–1B model in fp16 and in 4-bit (bitsandbytes) on Colab · measure GPU memory, tokens/s, and answers on 5 fixed prompts | 2-row table |
| ☐ SHIP | Same model in vLLM: tokens/s for 1 vs 8 requests at once (batching). Add to the table. Push | 3-row table + commit |
| ☐ REVIEW | AI-off: 🧠 KS drift test · blank-file memory math: params × bytes for fp32 / fp16 / int8 / 4-bit | rebuild done |

### Week 5 · Scaling concepts + safety and fairness basics

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 How to Scale Your Model, intro + the data-parallel part (≤30 min) · predict: data parallel on 4 GPUs, batch 32 on each → global batch? (answer: 128) | notes |
| ☐ BUILD | Without the book: one page of memory math for training a 1B model with Adam in mixed precision (≈ 16 bytes per param → ≈ 16 GB before activations) · 1 line each: data, tensor, pipeline parallel, ZeRO | `notes.md` page |
| ☐ SHIP | Safety: MLCC fairness module, then your [02](02-classical-ml.md) model's recall per group (e.g. by sex) in a table · if you have an LLM app, try 5 prompt-injection attacks on it and log what got through. Project README. Push | **project** ✅ |
| ☐ REVIEW | AI-off: 🧠 4-bit memory · 🔒 memory math in 5 sentences + blank-file `/predict` with a test | the 🔒 check |

**Done:** quantization + vLLM table · memory-math page · fairness table · 🔒 explain why training needs ~4× the memory of inference in 5 sentences, then write the memory calculator (params, dtype, optimizer → GB) in ≤20 lines, no notes.

---

## Build project

**"Ship one model properly."** Take your [02](02-classical-ml.md) or [03](03-deep-learning.md) model: MLflow tracking + registry, FastAPI `/predict` in Docker, pytest + GitHub Actions (green badge), a KS drift check, a per-group fairness table. Add an LLM part: a small model in fp16 vs 4-bit vs vLLM with memory, tokens/s and 5 sample answers. All runs on a laptop + free Colab.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- what MLflow logs: params, metrics, artifacts, model
- FastAPI + Pydantic input: why 422
- what goes in a Dockerfile, and why `.dockerignore`
- CI: what runs on push
- data drift vs concept drift, KS test
- train/serve skew
- bytes per param: fp32 4, fp16 2, int8 1, 4-bit 0.5
- KV cache: what it saves
- batching: why throughput goes up
- data / tensor / pipeline parallel, ZeRO in 1 line each
- fairness: one metric per group
- prompt injection: 2 examples
