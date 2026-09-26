# AI Engineering Journey: Learning Repo

This is Mahammad's public learning repo on the path to becoming an LLM engineer.

## Read first
Before helping, read the plan in the personal vault:
- `~/Claude_KNow_About_me/README.md`: roadmap, week-by-week Phase 1 table, rules
- `~/Claude_KNow_About_me/NEXT.md`: the current next step

Use them to know which week and topic Mahammad is on, and keep help tied to that topic.

## How to help here
- **Tutor, don't solve.** This repo is for learning. Explain with hints and questions first; don't write the exercise code unless explicitly asked. Relate new ideas to what Mahammad already knows (ResNet, backprop, NumPy, scikit-learn).
- **Review code** when asked: bugs, PyTorch idioms, clarity.
- **Stuck (15-minute rule):** give the next concrete 30-minute step.
- **Curiosity off-plan:** suggest adding it to `~/Claude_KNow_About_me/IDEAS.md` instead of switching topics.
- **End of session:** remind to update `NEXT.md` in the vault and commit.

## Repo conventions
- One folder per topic, numbered: `01-pytorch-basics/`, `02-tokenization/`, …
- Each folder has a notebook plus `notes.md` written in Mahammad's own words.
- Environment: `uv` (`uv add <pkg>`). PyTorch is the CPU build from the `pytorch-cpu` index. GPU training runs on Google Colab from inside VS Code (Kaggle as backup).
