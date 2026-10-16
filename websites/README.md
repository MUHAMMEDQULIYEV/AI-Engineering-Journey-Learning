# 🌐 Websites

Websites for learning AI on the LLM-engineer path. Checked live on 2026-10-16 (2 research agents + 1 head reviewer).
Same rule as [`../roadmap/resources.md`](../roadmap/resources.md): **one main source per topic.** "Lookup only" = open it for one question, find the answer, close it.

## ✅ Main sources

| Site | Topic | Why |
|---|---|---|
| [PyTorch Tutorials](https://docs.pytorch.org/tutorials/) | PyTorch basics | Official and current |
| [Karpathy: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Tokenizer + mini-GPT | Tokenizer video and "Let's build GPT" |
| [HF Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) | Agents | Free, kept up to date |
| [HF MCP Course](https://huggingface.co/learn/mcp-course/unit0/introduction) | MCP | Free, MCP from the basics to a deployed use case |
| [HF PEFT docs](https://huggingface.co/docs/peft/index) | LoRA | The LoRA reference, use together with the TRL docs |

## 🔎 Lookup only

| Site | Topic | Use it for |
|---|---|---|
| [Understanding Deep Learning (free book)](https://udlbook.github.io/udlbook/) | Attention | Ch. 12: written check of `softmax(QKᵀ/√d)·V` |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Attention | Q/K/V pictures |
| [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) | Attention | Live GPT-2 in the browser: attention patterns, shapes |
| [bbycroft LLM Visualization](https://bbycroft.net/llm) | Attention / mini-GPT | 3D walk through one layer's shapes |
| [Sebastian Raschka: Ahead of AI](https://magazine.sebastianraschka.com) | Mini-GPT | From-scratch LLM write-ups |
| [Lilian Weng: Lil'Log](https://lilianweng.github.io) | Attention → LoRA | Deep surveys, one post for one concept |
| [HF LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | LLM apps | Free backup to the Udemy course |
| [Anthropic Academy](https://academy.claude.com/) | LLM apps | Claude API + MCP courses |
| [Simon Willison](https://simonwillison.net) | LLM apps | Tools + MCP, search it, don't read the daily feed |
| [Eugene Yan](https://eugeneyan.com/writing/) | Flagship | Evals + RAG patterns |
| [Chip Huyen](https://huyenchip.com/blog/) | Flagship | AI engineering (old but solid posts) |
| [Arena](https://arena.ai) (formerly LMArena) | Flagship | Choosing which model to use |
| [DeepLearning.AI short courses](https://www.deeplearning.ai/short-courses/) | Serving | At most one 1–2 h course (e.g. vLLM) |
| [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) | Serving | Quantization / serving answers, search only, never scroll |

## 👀 Visual / interactive

Sites that **show** an idea: drag, click, watch it move. Open the matching one for 5 minutes *before* the LEARN video. Checked live on 2026-10-17.
Grouped by the tracks of the full [AI map](../ai-map/README.md). Distill.pub is archived (no new posts since 2021) but its old interactive articles still load, so they are listed here even though Distill is in the Skip list for the LLM path.

| Track | Site | What it shows |
|---|---|---|
| 01 math | [3Blue1Brown: linear algebra](https://www.3blue1brown.com/topics/linear-algebra) · [calculus](https://www.3blue1brown.com/topics/calculus) · [probability](https://www.3blue1brown.com/topics/probability) | Animations: matrices as transformations, derivatives, probability |
| 01 math | [Immersive Linear Algebra](https://immersivemath.com/ila/index.html) | Interactive textbook with 3D figures |
| 01 math | [Seeing Theory](https://seeing-theory.brown.edu/) | Interactive probability + statistics (archived, still works) |
| 01 math | [Setosa: Explained Visually](https://setosa.io/ev/) | Eigenvectors, Markov chains, conditional probability, image kernels |
| 01 math | [Desmos](https://www.desmos.com/calculator) · [GeoGebra](https://www.geogebra.org/) | Plot a function and its derivative |
| 02 classical ML | [MLU-Explain](https://mlu-explain.github.io/) | Linear / logistic regression, trees, random forest, bias-variance, CV, ROC/AUC, precision/recall, double descent |
| 02 classical ML | [Setosa: PCA](https://setosa.io/ev/principal-component-analysis/) · [OLS](https://setosa.io/ev/ordinary-least-squares-regression/) | Drag the points, watch PCA / regression change |
| 02 classical ML | [Bias-variance demo](https://web-apps.thecoatlessprofessor.com/data/bias-variance-tradeoff-demo-app/bias-variance-tradeoff-demo.html) | Polynomial degree vs train / test error |
| 02 classical ML | [Distill: How to use t-SNE effectively](https://distill.pub/2016/misread-tsne/) | t-SNE perplexity, live |
| 02 classical ML | [R2D3: visual intro to ML](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) | Decision trees as a scrolling story · ⚠️ flaky (HTTP 522 when checked) |
| 03 deep learning | [TensorFlow Playground](https://playground.tensorflow.org/) | Tweak a small MLP, watch the decision boundary |
| 03 deep learning | [3Blue1Brown: neural networks](https://www.3blue1brown.com/topics/neural-networks) · [MLU-Explain: neural networks](https://mlu-explain.github.io/neural-networks/) | Backprop animations, a visual intro to NNs |
| 03 deep learning | [Distill: Why momentum works](https://distill.pub/2017/momentum/) | Optimizer dynamics |
| 03 deep learning | [CNN Explainer](https://poloclub.github.io/cnn-explainer/) · [ConvNetJS](https://cs.stanford.edu/people/karpathy/convnetjs/) | Conv / ReLU / pool step by step · train on MNIST in the browser (old) |
| 03 deep learning | [Colah: Understanding LSTMs](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) · [Distill: augmented RNNs](https://distill.pub/2016/augmented-rnns/) | RNN / LSTM diagrams |
| 04 LLMs | [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) · [bbycroft LLM viz](https://bbycroft.net/llm) | Live GPT-2 · 3D walk through a small GPT |
| 04 LLMs | [Tiktokenizer](https://tiktokenizer.vercel.app/) | Live tokenization |
| 04 LLMs | [Embedding Projector](https://projector.tensorflow.org/) · [WizMap](https://poloclub.github.io/wizmap/) | Embeddings in 2D / 3D |
| 04 LLMs | [Sam Rose: Prompt caching](https://ngrok.com/blog/prompt-caching) | Interactive essay: tokens → attention → KV cache |
| 05 vision + generative | [GAN Lab](https://poloclub.github.io/ganlab/) · [Diffusion Explainer](https://poloclub.github.io/diffusion-explainer/) | Train a GAN in the browser · Stable Diffusion step by step |
| 05 vision + generative | [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/) | Latent diffusion pipeline (static) |
| 05 vision + generative | [Distill: Feature Visualization](https://distill.pub/2017/feature-visualization/) · [Activation Atlas](https://distill.pub/2019/activation-atlas/) · [Grand Tour](https://distill.pub/2020/grand-tour/) | What CNN neurons respond to |
| 05 / 07 | [Netron](https://netron.app/) | Open a model file, see its graph |
| 06 RL | [REINFORCEjs](https://cs.stanford.edu/people/karpathy/reinforcejs/) | Gridworld DP, TD / Q-learning, DQN in the browser |
| 06 RL | [MLU-Explain: RL](https://mlu-explain.github.io/reinforcement-learning/) · [Gymnasium CartPole](https://gymnasium.farama.org/environments/classic_control/cart_pole/) | RL basics · the env with a GIF |
| 06 RL | [UNIPO](https://poloclub.github.io/unipo/) | RL fine-tuning of an LLM token by token (PPO, GRPO) · ⚠️ not confirmed live |
| 07 ML systems | [Sam Rose: Quantization](https://ngrok.com/blog/quantization) | Float formats from 2-bit to bf16, interactive |
| 07 ML systems | [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | Parallelism, sharding, rooflines |
| 08 research | [Connected Papers](https://www.connectedpapers.com/) · [Distill: Research Debt](https://distill.pub/2017/research-debt/) | Citation graph of one paper · why clear explanations matter |

Left out: alphaXiv RL Playground (404, dead) · Learn ML Visualized gridworld (HTTP 503) · HF Ultra-Scale and Smol Training Playbooks (Spaces stuck on "Refreshing"; listed as lookup in [track 07](../ai-map/tracks/07-ml-systems.md)).

## ❌ Skip (and why)

| Site | Why skip |
|---|---|
| [Stanford CS224N](https://web.stanford.edu/class/cs224n/), [d2l.ai](https://d2l.ai/) | Overlap 3Blue1Brown + Karpathy + UDL; d2l stale since 2023 |
| [Stanford CS336](https://cs336.stanford.edu/) | Excellent but a full semester, revisit after the serving block |
| [HF Daily Papers](https://huggingface.co/papers), [alphaXiv](https://www.alphaxiv.org), [Language Models & Co.](https://newsletter.languagemodels.co) | Feeds that pull you into reading instead of building |
| [Kaggle Learn](https://www.kaggle.com/learn), [Kaggle Competitions](https://www.kaggle.com/competitions) | Overlap HF courses / off the path (Kaggle GPU notebooks stay as GPU backup) |
| [fast.ai](https://course.fast.ai/), [Full Stack LLM Bootcamp](https://fullstackdeeplearning.com/llm-bootcamp/) | Stale (2022–23), no current LLM content |
| llmbootcamp.com, [Distill.pub](https://distill.pub) | Dead (domain for sale) / on hiatus since 2021 |
