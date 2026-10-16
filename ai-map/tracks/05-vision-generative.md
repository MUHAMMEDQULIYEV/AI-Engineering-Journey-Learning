# 05 · Vision + generative models (6 weeks)

🧪 draft, not walked yet

**Goal:** you can fine-tune a pretrained CNN and a ViT on your own images, run a detector, and explain (and train a tiny) VAE and diffusion model.
**Done:** a ResNet vs ViT table on the same small dataset + a tiny DDPM on MNIST with sample grids, pushed · 🔒 explain the diffusion forward + reverse process in 5 sentences, then write the forward noising `q(x_t | x_0)` and one training step in ≤20 lines, no notes.

**Prerequisites:** [03 deep learning](03-deep-learning.md) (CNNs, ResNet, training well). For the ViT week, [04](04-llms.md) Blocks 2–3 (attention) help a lot; if you skipped 04, watch the 👀 Transformer Explainer first.

Day jobs: [../../roadmap/README.md](../../roadmap/README.md). LEARN = 👀 first, ≤30 min reading, 1 predict question. BUILD = without the tutorial. SHIP = push. REVIEW = AI-off recall + blank-file rebuild.
GPU: weeks 1–3 and 6 use the free Colab / Kaggle GPU. Keep each run ≤30 min (small subsets, few epochs).
📄 Paper every 2 weeks ([08](08-research.md)): *ViT* (Dosovitskiy et al., 2020), *DDPM* (Ho et al., 2020).

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| CNN features + transfer learning | [CS231n notes](https://cs231n.github.io/) (transfer learning part) | [PyTorch transfer learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) (link not checked) · [HF Computer Vision course](https://huggingface.co/learn/computer-vision-course/unit0/welcome/welcome) | [Distill: Feature Visualization](https://distill.pub/2017/feature-visualization/) · [Activation Atlas](https://distill.pub/2019/activation-atlas/) |
| ViT + multimodal | [HF Computer Vision course](https://huggingface.co/learn/computer-vision-course/unit0/welcome/welcome), unit 3 | [UDL book](https://udlbook.github.io/udlbook/) · CS231n notes | [Netron](https://netron.app/) (open the model graph) · [Distill: Grand Tour](https://distill.pub/2020/grand-tour/) |
| Detection + segmentation | HF Computer Vision course, unit 6 | [Ultralytics docs](https://docs.ultralytics.com/) (YOLO) | — |
| VAE + GAN | [UDL book](https://udlbook.github.io/udlbook/), VAE + GAN chapters (check the chapter numbers in the current PDF) | HF Computer Vision course, unit 5 | [GAN Lab](https://poloclub.github.io/ganlab/) |
| Diffusion theory | [Lilian Weng: What are diffusion models?](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) | UDL diffusion chapter | [Diffusion Explainer](https://poloclub.github.io/diffusion-explainer/) · [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) |
| Diffusion practice | [HF Diffusion course](https://huggingface.co/learn/diffusion-course/unit0/1) | [Diffusers docs](https://huggingface.co/docs/diffusers/index) | Diffusion Explainer |

Notes: CS231n's newest lecture videos are Stanford-only; the notes are free and older-year videos are on YouTube. Distill is archived (2016–2021) but the articles still load and still teach.

---

## Block A · Vision (3 weeks)

### Week 1 · Transfer learning with a pretrained CNN

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Distill Feature Visualization (what early vs late layers see) · CS231n transfer learning notes (≤30 min) · predict: ResNet18, backbone frozen, new head 512 → 10. Trainable params? (answer: 5,130) | notebook + 3 lines of notes |
| ☐ BUILD | Without the notes: pretrained ResNet18 on a 5,000-image CIFAR-10 subset (resize to 224 or keep 32 and say why), frozen backbone, 3 epochs on Colab | val acc printed |
| ☐ SHIP | Frozen vs full fine-tune vs from scratch (your [03](03-deep-learning.md) ResNet), same data, one table. Push | table + commit |
| ☐ REVIEW | AI-off: 🧠 skip connection (from 03) · blank-file "load model, freeze, replace head" in ≤10 lines | rebuild runs |

### Week 2 · Vision Transformer (ViT)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Netron: open a small ViT and find the patch embedding · HF CV course unit 3 (≤30 min) · predict: 224×224 image, 16×16 patches → how many tokens with the CLS token? (answer: 196 + 1 = 197) | notes |
| ☐ BUILD | Without the course: patchify a `(1, 3, 224, 224)` tensor with `reshape` / `unfold` → `(1, 196, 768)`, add CLS → `(1, 197, 768)`. Print every shape | shapes match |
| ☐ SHIP | Fine-tune a small pretrained ViT on the same 5,000-image subset. Add a row to week 1's table. Push | table + commit |
| ☐ REVIEW | AI-off: 🧠 frozen vs full fine-tune · blank-file patchify in ≤10 lines | rebuild runs |

### Week 3 · Detection + segmentation

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | HF CV course unit 6 (≤30 min) · predict: IoU of boxes `[0,0,2,2]` and `[1,1,3,3]`? (answer: 1/7 ≈ 0.14) | notes |
| ☐ BUILD | Without the course: `iou(a, b)` and non-max suppression (sort by score, drop IoU > 0.5) from scratch, ≤20 lines, test on 5 boxes | asserts pass |
| ☐ SHIP | Ultralytics YOLO: run a pretrained model on 10 of your own photos, then fine-tune on a small dataset from the docs (few epochs). mAP before/after. Push | images + numbers |
| ☐ REVIEW | AI-off: 🧠 197 tokens · blank-file IoU + NMS | rebuild runs |

**Done:** ResNet (frozen / full / scratch) + ViT in one table · IoU + NMS tests pass · YOLO fine-tune numbers · 🔒 explain transfer learning in 5 sentences, then write IoU + NMS in ≤20 lines, no notes.

---

## Block B · Generative models (3 weeks)

### Week 4 · VAE (and a look at GANs)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 GAN Lab (train one in the browser, watch the generator move) · UDL VAE chapter (≤30 min) · predict: KL term of a latent with μ = 0, σ = 1 vs the prior N(0, 1)? (answer: 0) | notes |
| ☐ BUILD | Without the book: VAE on MNIST, latent dim 2: encoder → μ, log σ² → reparameterize → decoder · loss = reconstruction + KL (CPU is fine) | loss goes down |
| ☐ SHIP | Plot the 2D latent space colored by digit + a 10×10 grid of decoded points. Push | 2 plots + commit |
| ☐ REVIEW | AI-off: 🧠 IoU · blank-file reparameterization trick + KL in ≤10 lines | rebuild runs |

### Week 5 · Diffusion: the forward process and the idea

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Diffusion Explainer + Illustrated Stable Diffusion · Lilian Weng diffusion post, DDPM part (≤30 min) · predict: x₀ = 1, ᾱ_t = 0.25, ε = 0 → x_t? (answer: √0.25 · 1 = 0.5) | notes |
| ☐ BUILD | Without the post: linear β schedule, 1,000 steps, `q_sample(x0, t, eps)` · noise one MNIST image at t = 0, 250, 500, 999 and plot | 4-image plot |
| ☐ SHIP | One training step on paper + in code: pick t, add noise, model predicts ε, MSE. Write the 5-sentence explanation in `notes.md`. Push | commit |
| ☐ REVIEW | AI-off: 🧠 VAE loss · blank-file `q_sample` in ≤10 lines | rebuild runs |

### Week 6 · Tiny DDPM on MNIST (Colab GPU) + project

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | HF Diffusion course unit 1 (≤30 min) · predict: after 1 epoch, will samples look like digits, blobs, or noise? | notes |
| ☐ BUILD | Without the course: `UNet2DModel` from Diffusers + your `q_sample` + the training loop, 28×28 MNIST, ≤30 min on Colab | loss curve |
| ☐ SHIP | Sample grids at 3 checkpoints. Project README: the vision table + VAE plots + DDPM grids. Push | **project** ✅ |
| ☐ REVIEW | AI-off: 🧠 ViT patchify · 🔒 forward noising + one training step from a blank file | the 🔒 check |

**Done:** VAE latent plot · DDPM sample grids at 3 checkpoints · 🔒 explain diffusion in 5 sentences, then write `q_sample` + one training step in ≤20 lines, no notes.

---

## Build project

**"See and generate."** Part 1: ResNet18 (frozen / full) vs a small ViT vs your own CNN on the same 5,000-image subset: accuracy, params, training time on a free T4. Part 2: a 2D-latent VAE and a tiny DDPM on MNIST with sample grids at 3 checkpoints. Optional: YOLO fine-tuned on 50 of your own labeled photos.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- transfer learning: frozen vs full fine-tune, when to use which
- ViT: patches → tokens (197 for 224 / 16)
- IoU + NMS
- VAE: reparameterization trick + the 2 loss terms
- GAN: generator vs discriminator in 3 sentences
- diffusion forward process: `x_t = √ᾱ_t · x₀ + √(1 − ᾱ_t) · ε`
- diffusion training target: predict ε, MSE
- latent diffusion vs pixel diffusion (why Stable Diffusion is fast)
