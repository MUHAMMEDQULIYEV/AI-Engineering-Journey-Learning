# 03 · Deep learning (9 weeks)

🟡 partly walked by the author: [01-pytorch-basics](../../01-pytorch-basics/) (week 3: FashionMNIST, 86% test acc) and [CNN/ResNet](../../CNN/ResNet/) (week 8: a ResNet BasicBlock). The other weeks are 🧪 draft.

**Goal:** you know what backprop does with real numbers, you can write a PyTorch training loop from a blank file, and you can make a CNN train well (init, optimizer, regularization).
**Done:** micrograd MLP + a CIFAR-10 CNN with an ablation table, pushed · 🔒 explain backprop in 5 sentences, then write a `Value` class with `+`, `*` and `backward()` in ≤20 lines, no notes.

**Prerequisites:** [01 math](01-math.md) (chain rule, matrices), [02 classical ML](02-classical-ml.md) (splits, overfitting, metrics).

Day jobs: [../../roadmap/README.md](../../roadmap/README.md). LEARN = 👀 first, ≤30 min video, 1 predict question. BUILD = without the video. SHIP = push. REVIEW = AI-off recall + blank-file rebuild.
GPU: weeks 1–7 run on CPU. Week 8 (CIFAR-10) uses Colab or Kaggle.
📄 From this track on, read **1 paper every 2 weeks** on a REVIEW day (see [08 research](08-research.md)). Good ones here: *Adam* (Kingma & Ba, 2014), *Dropout* (Srivastava et al., 2014), *ResNet* (He et al., 2015).

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| Backprop, MLP from scratch | [Karpathy: Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html), videos 1–5 (micrograd, makemore 1–4, ~9.5 h) | [UDL book](https://udlbook.github.io/udlbook/) | [3Blue1Brown: neural networks](https://www.3blue1brown.com/topics/neural-networks) · [TensorFlow Playground](https://playground.tensorflow.org/) · [MLU-Explain NN](https://mlu-explain.github.io/neural-networks/) |
| PyTorch mechanics | [PyTorch: Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | [d2l.ai](https://d2l.ai/) | — |
| Optimizers, regularization | [d2l.ai](https://d2l.ai/) optimization + regularization chapters | [CS231n notes](https://cs231n.github.io/) | [Distill: Why momentum works](https://distill.pub/2017/momentum/) |
| CNNs | [d2l.ai](https://d2l.ai/) CNN + modern CNN chapters | [CS231n notes](https://cs231n.github.io/) | [CNN Explainer](https://poloclub.github.io/cnn-explainer/) · [Setosa: image kernels](https://setosa.io/ev/) · [ConvNetJS](https://cs.stanford.edu/people/karpathy/convnetjs/) (old, still runs) |
| RNN / LSTM | [d2l.ai](https://d2l.ai/) RNN chapters | UDL | [Colah: Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) · [Distill: augmented RNNs](https://distill.pub/2016/augmented-rnns/) |

Notes: d2l.ai is v1.0.3 (2023). Basics don't age, but skip its transformer chapters; [04 LLMs](04-llms.md) covers those. fast.ai (2022) is not used. CS231n: the notes are free; new lecture videos are Stanford-only, older years are on YouTube.

---

## Block A · Backprop by hand (2 weeks)

### Week 1 · micrograd, part 1: a tiny autograd

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 3Blue1Brown NN ch. 1–2 · Karpathy micrograd 0–30 min · predict: `L = a*b + c`, a = 2, b = −3, c = 10 → dL/da? (answer: −3) | notebook + 3 lines of notes |
| ☐ BUILD | Without the video: `Value` with `data`, `grad`, `+`, `*`. Compute the grads of the example by hand on paper first, then in code | grads match paper |
| ☐ SHIP | `backward()` with a topological sort · check against `torch` on the same 3-node graph. Push | grads = torch |
| ☐ REVIEW | AI-off: 🧠 chain rule (from 01) · blank-file `Value` with `+`, `*` | rebuild runs |

### Week 2 · micrograd, part 2: neuron → MLP → training

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 TensorFlow Playground: 1 hidden layer vs 0 on the circle dataset · Karpathy micrograd rest (≤30 min per day) · predict: you forget `zero_grad`. What happens to the grads after 3 steps? (answer: they add up) | notes |
| ☐ BUILD | Without the video: `tanh`, `Neuron`, `Layer`, `MLP(3, [4, 4, 1])`, 4 training examples | loss < 0.01 in ≤100 steps |
| ☐ SHIP | Same MLP in PyTorch, same init → same loss after 1 step. Push | commit |
| ☐ REVIEW | AI-off: 🧠 dL/da example · 🔒 blank-file `Value` + `backward()` in ≤20 lines | the 🔒 check |

**Done:** your MLP trains to loss < 0.01 · your grads = PyTorch grads · 🔒 explain backprop in 5 sentences, then write `Value` with `+`, `*`, `backward()` in ≤20 lines, no notes.

---

## Block B · PyTorch + language-model warm-up (2 weeks)

### Week 3 · PyTorch: tensors, DataLoader, training loop

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | PyTorch *Learn the Basics*: tensors, datasets, autograd (≤30 min) · predict: shape of `nn.Linear(784, 10)(torch.randn(32, 784))`? (answer: `(32, 10)`) | notes |
| ☐ BUILD | Without the tutorial: FashionMNIST, `DataLoader(batch_size=64)`, MLP 784 → 128 → 10, training loop, test accuracy | ≥ 85% test acc |
| ☐ SHIP | Add a val split, plot train + val loss per epoch, save + load the model. Push | plot + commit |
| ☐ REVIEW | AI-off: 🧠 `zero_grad` · blank-file training loop in ≤20 lines | rebuild runs |

### Week 4 · makemore 1–2: bigram → MLP language model

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Karpathy makemore 1 (≤30 min per day) · predict: loss of a uniform guess over 27 characters? (answer: ln 27 ≈ 3.30) | notes |
| ☐ BUILD | Without the video: bigram counts model on `names.txt` (from the video), sample 5 names, negative log-likelihood | loss < 3.30 |
| ☐ SHIP | makemore 2: MLP with a 3-char context + embeddings, train/val split. Push | val loss < bigram |
| ☐ REVIEW | AI-off: 🧠 training loop · blank-file bigram counts + sampling in ≤15 lines | rebuild runs |

**Done:** FashionMNIST ≥ 85% · MLP char model beats the bigram on val loss · 🔒 explain cross-entropy loss in 5 sentences, then write the training loop in ≤20 lines, no notes.

---

## Block C · Training well (2 weeks)

### Week 5 · Init, activations, BatchNorm, optimizers

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Distill momentum · Karpathy makemore 3 (≤30 min per day) · predict: a `tanh` unit with input 5: gradient close to 1 or close to 0? (answer: ≈ 0, it's saturated) | notes |
| ☐ BUILD | Without the video: histograms of activations per layer, default init vs Kaiming · add `BatchNorm1d`, compare | 2 histogram plots |
| ☐ SHIP | Same MLP: SGD vs SGD + momentum vs Adam, same lr search (3 values each), 3 loss curves on one plot. Push | plot + commit |
| ☐ REVIEW | AI-off: 🧠 ln 27 · blank-file Adam update for 1 parameter (m, v, bias correction) | rebuild runs |

### Week 6 · Regularization + manual backprop

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | d2l dropout + weight decay sections (≤30 min) · predict: `Dropout(0.5)` in `model.eval()`: does the output change between 2 runs? (answer: no) | notes |
| ☐ BUILD | Without the book: overfit a 1,000-sample FashionMNIST subset on purpose, then add dropout, then weight decay, then early stopping. Val curves on one plot | 4 curves |
| ☐ SHIP | makemore 4 (manual backprop) light: backprop **one** linear layer + cross-entropy by hand, check vs autograd. Push | grads match |
| ☐ REVIEW | AI-off: 🧠 momentum in 3 sentences · blank-file dropout forward in ≤10 lines | rebuild runs |

**Done:** init/BatchNorm histograms · optimizer plot · regularization plot · 🔒 explain why dropout helps in 5 sentences, then write the Adam update in ≤20 lines, no notes.

---

## Block D · CNNs (2 weeks)

### Week 7 · Convolution, padding, stride, pooling

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 CNN Explainer + Setosa image kernels · d2l convolution chapter (≤30 min) · predict: 32×32 input, 3×3 kernel, padding 1, stride 2 → output size? (answer: 16×16) | notes |
| ☐ BUILD | Without the book: conv2d with 2 loops on a 5×5 image and a 3×3 kernel, check vs `F.conv2d` · LeNet on FashionMNIST | asserts pass |
| ☐ SHIP | LeNet vs your week 3 MLP on FashionMNIST: accuracy + number of params. Push | table + commit |
| ☐ REVIEW | AI-off: 🧠 dropout in eval mode · blank-file conv output-size formula + loop conv in ≤20 lines | rebuild runs |

### Week 8 · Modern CNNs: BatchNorm, ResNet, augmentation (Colab GPU)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | d2l ResNet section (≤30 min) · predict: number of params in `Conv2d(3, 16, 3)`? (answer: 3·16·9 + 16 = 448) | notes |
| ☐ BUILD | Without the book: ResNet `BasicBlock` (skip connection, 2 convs, BatchNorm) → small ResNet, CIFAR-10 on Colab, 10 epochs | test acc printed |
| ☐ SHIP | Ablation, 1 change at a time: no augmentation vs flip + crop · weight decay 0 vs 5e-4 · SGD vs Adam. Table. Push | table + commit |
| ☐ REVIEW | AI-off: 🧠 conv output size · blank-file `BasicBlock` in ≤20 lines | rebuild runs |

**Done:** loop conv = `F.conv2d` · CIFAR-10 ablation table · 🔒 explain the skip connection in 5 sentences, then write `BasicBlock` in ≤20 lines, no notes.

---

## Block E · Sequences (1 week)

### Week 9 · RNN + LSTM, then finish the project

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Colah LSTMs + Distill augmented RNNs · d2l RNN chapter (≤30 min) · predict: `nn.RNN(8, 16, batch_first=True)` on input `(2, 5, 8)` → output shape? (answer: `(2, 5, 16)`) | notes |
| ☐ BUILD | Without the book: char-level RNN on `names.txt`, val loss vs your week 4 MLP | val loss compared |
| ☐ SHIP | Project README: micrograd result, FashionMNIST, CIFAR-10 ablation table, curves. Push | **project** ✅ |
| ☐ REVIEW | AI-off: 🧠 BasicBlock · 🔒 blank-file `Value` + `backward()` | the 🔒 check |

**Done:** RNN vs MLP val loss in the README · 🔒 explain backprop in 5 sentences, then write `Value` with `+`, `*`, `backward()` in ≤20 lines, no notes.

---

## Build project

**"From micrograd to CIFAR-10."** Part 1: your autograd + MLP, grads checked against PyTorch. Part 2: a small ResNet on CIFAR-10 (Colab free GPU, ≤30 min per run) with an ablation table: optimizer, dropout / weight decay, augmentation. Train + val curves for each row. One line per row on why it helped or didn't.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- backprop on `a*b + c` by hand
- why `zero_grad`
- cross-entropy and ln(#classes) as the starting loss
- tanh saturation + good init
- BatchNorm in 3 sentences
- SGD vs momentum vs Adam
- dropout train vs eval
- conv output size: `(n + 2p − k) / s + 1`
- params of a conv layer
- skip connection: why deep nets train with it
- RNN input / output shapes
