+# 01 · PyTorch Basics

**Week 1 (Sep 29 – Oct 4, 2026)** · Source: [PyTorch "Learn the Basics"](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)

Goal: learn PyTorch well enough to rewrite my ResNet from TensorFlow.
torchvision:the liblary that used for the computer vision and pretrained model + datasets
fashionmnist:dataset that 28*28 size clothing dataset with labels

> Write every answer in my own words, as if explaining to a friend.

## Tensors
- What is a tensor? How is it different from a NumPy array?

## Autograd
- What does `requires_grad=True` do?
- What happens when I call `.backward()`? How does this connect to the backpropagation I already know?

## nn.Module
- What goes in `__init__` and what goes in `forward`?
- How is this similar to my ResNet class in TensorFlow?

## Loss: Cross-Entropy
```
loss = −log(p_correct)        p_correct = softmax probability of the true class
```
| p_correct | loss |
|---|---|
| 0.9 | 0.11 |
| 0.5 | 0.69 |
| 0.01 | 4.6 |

- `nn.CrossEntropyLoss()` has softmax built in → model outputs raw logits, no `nn.Softmax()` at the end
- pred shape `[batch, 10]`, y shape `[batch]` (class numbers 0–9)

## Optimizer: Adam = Momentum + RMSProp
Sources: [DataMListic — "The Adam Optimizer is Just Momentum + RMSProp"](https://youtu.be/nb09yQZ-iFQ) · [Medium — The Math Behind Adam Optimizer](https://medium.com/data-science/the-math-behind-adam-optimizer-c41407efe59b) · Krish Naik bootcamp

For each weight separately (`g` = current gradient, `t` = step number):
```
1. m  = β1·m + (1 − β1)·g          average of gradients    → direction (momentum)
2. v  = β2·v + (1 − β2)·g²         average of g²           → scale (RMSProp)
3. m̂  = m / (1 − β1ᵗ)              bias correction (m, v start at 0)
4. v̂  = v / (1 − β2ᵗ)
5. w  = w − lr · m̂ / (√v̂ + ε)      update
```
Defaults: `lr = 1e-3`, `β1 = 0.9`, `β2 = 0.999`, `ε = 1e-8`

- β = how much of the OLD value to keep; the new part is `1 − β`
- m expanded: `0.1·g_now + 0.09·g_1ago + 0.081·g_2ago + …` (exponential moving average)
- √v = RMS (Root Mean Square) = typical gradient size of this weight
- m̂/√v̂ ≈ confidence: steady gradients → ≈1 (full step ≈ lr), noisy ±10 → ≈0 (tiny step)
- SGD for comparison: `w = w − lr · g`

Worked example (L = w², g = 2w, w = 5, lr = 0.1) — checked in PyTorch:
| t | g | m | v | w after |
|---|---|---|---|---|
| 1 | 10 | 1.0 | 0.1 | 4.9 |
| 2 | 9.8 | 1.88 | 0.19594 | 4.80 |
| 3 | 9.6 | 2.652 | 0.2879 | 4.70 |

```python
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
```
For transformers / LLMs later: AdamW (Adam + fixed weight decay).

**My explanation (own words):**
- Adam combines momentum + RMSProp. We don't rely on just one gradient: m mixes old and new gradients (newer ones count more), so the direction is smooth, not zig-zag.
- For the step size we use v: square the gradients (removes the − sign), take their average, then √v in the update → typical gradient size of each weight.
- ε is in the update (divide by √v̂ + ε) so we never divide by zero when v ≈ 0 at the start.
- m = direction, v = scale, m/√v = how confident Adam is → step size.
- The DataMListic video showed me momentum and RMSProp separately, then how their formulas combine into Adam.

## Training loop
- The 5 steps: forward → loss → `zero_grad` → `backward` → `step`. Why is each needed?
- `backward()` only **computes** gradients; `optimizer.step()` is what **updates** the weights.

## Evaluation (Sep 29)
- Eval = only **measure**, never change the model → skip `zero_grad`, `backward`, `step`. Keep the forward pass.
- `model.eval()` → switches layers like Dropout/BatchNorm to test mode (none in my model yet, but good habit).
- `torch.no_grad()` → no gradient tracking → faster, less memory.
- Prediction: `logits` `[64, 10]` → `logits.argmax(dim=1)` → `[64]`. `dim` = the dimension that **disappears** (the 10 classes).
- `(pred == labels)` → `[True, False, True]`; `.sum()` counts True as 1; `.item()` turns the tensor into a Python number.
- `total += len(labels)`, not `+= 64` — the last batch is smaller (10000 test images → last batch has 16).
- Accuracy = `correct / total`, counters reset to 0 every epoch.

## Epochs & curves
- Train + test **inside the same epoch loop**: epoch 1 train → test, epoch 2 train → test…
- Appends go **after** the batch loop (once per epoch), not inside it (157 times).
- Call `model.train()` at the start of each epoch (eval() from last epoch stays on otherwise).
- Re-create `model` + `optimizer` + empty lists before a new run; otherwise training continues from old weights.
- Overfitting signal: train loss keeps going down while test accuracy flattens/drops → stop there (early stopping).
- `loss.item()` after the loop = loss of the **last batch only** → noisy curve. Better: average loss over all batches.

My results: 1 epoch → **81.9%**, 5 epochs → **86.3%** test accuracy.

## Save & Load
```python
torch.save(model.state_dict(), "fashion_model.pth")      # save weights only

loaded_model = MyModel()                                  # 1. structure
loaded_model.load_state_dict(torch.load("fashion_model.pth"))  # 2. weights
loaded_model.eval()
```
- `state_dict` = dictionary of layer names → weight tensors. `torch.save` uses pickle inside.
- Don't save the whole model (`torch.save(model)`) — it depends on the class name/location, breaks if I rename/move it.
- Later (Hugging Face): `.safetensors` = same idea, no pickle → safer (pickle can run code) and faster.
- Check: loaded model gave exactly **0.8627** again (same weights, no randomness in eval, test shuffle=False). ~0.10 would mean random weights.

## TensorFlow → PyTorch (for the ResNet rewrite)
| TensorFlow / Keras | PyTorch |
|---|---|
| | |

## Questions I still have

