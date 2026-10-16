# 00 · Setup: tools + data basics (2 weeks)

🧪 draft, not walked yet

**Goal:** you can make a project folder with git + `uv`, work in a notebook, and clean a messy table with NumPy, pandas and a little SQL.
**Done:** a public repo with a cleaned dataset notebook and a README that says how to run it · 🔒 explain broadcasting in 5 sentences, then write a `clean(df)` function (missing values, one categorical column, a check for no NaN) in ≤20 lines, no notes.

**Prerequisites:** Python (functions, lists, dicts, loops). No ML.

Day jobs: [../../roadmap/README.md](../../roadmap/README.md) (LEARN · BUILD · SHIP · REVIEW). LEARN = ≤30 min reading + 1 predict question + code the idea. BUILD = without the tutorial. SHIP = push. REVIEW = AI-off recall + blank-file rebuild.

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| git + GitHub | git's own `--help` pages + this repo's [README](../../README.md) setup block (no link checked for a git course) | — | — |
| `uv`, notebooks | `uv init`, `uv add`, `uv run jupyter lab` (the uv docs on astral.sh, no link checked) | VS Code notebooks | — |
| NumPy | the NumPy "absolute beginners" guide on numpy.org (no link checked) | [Kaggle Learn](https://www.kaggle.com/learn) | — |
| pandas + data cleaning | [Kaggle Learn](https://www.kaggle.com/learn): *Pandas*, then *Data Cleaning* | pandas docs | — |
| SQL | [SQLBolt](https://sqlbolt.com) lessons 1–6 | [Kaggle Learn](https://www.kaggle.com/learn): *Intro to SQL* | — |

No visual sites for this track. Your own `print(x.shape)` is the visual.

---

## Block A · Tools + data (2 weeks)

### Week 1 · git, uv, notebooks, NumPy

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | `uv init ml-setup`, `uv add numpy pandas jupyter`, open a notebook. Read the NumPy guide (≤30 min). Predict: shape of `np.arange(12).reshape(3, 4).sum(axis=0)`? (answer: `(4,)`) | notebook + 3 lines of notes |
| ☐ BUILD | Without the guide: 8 small NumPy cells. `(3,1) + (1,4)` → predict the shape first · boolean mask: values > 5 in `arange(10)` · mean of each column of a 5×3 array · `x @ y` vs a loop for 3×3, check they are equal | all asserts pass |
| ☐ SHIP | `git init`, `.gitignore` (`.venv/`, `.ipynb_checkpoints/`), 3 small commits, push to GitHub. README: 3 lines + `uv sync` | repo on GitHub |
| ☐ REVIEW | AI-off: 🧠 the broadcasting rule (when do 2 shapes fit?) · blank folder → env + one NumPy cell in ≤10 min | rebuild works |

### Week 2 · pandas, data cleaning, SQL

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Kaggle Learn *Pandas* lessons 1–3 (≤30 min). Load the Titanic CSV. Predict: how many rows does `df.groupby("Sex")["Age"].mean()` return? (answer: 2) | notebook + notes |
| ☐ BUILD | Without the lessons: count missing values per column · fill `Age` with the median · drop `Cabin` · one-hot `Embarked` · `assert df.isna().sum().sum() == 0` | clean table |
| ☐ SHIP | SQLBolt lessons 1–6. Load the clean table into `sqlite3` from Python. Answer 3 questions in SQL **and** pandas (e.g. survival rate by `Pclass`), check both give the same numbers. Push | 3 matching answers, commit |
| ☐ REVIEW | AI-off: 🧠 git add / commit / push from memory · blank-file `clean(df)` in ≤20 lines | the 🔒 check |

**Done:** the repo has the NumPy notebook, the cleaning notebook and the 3 SQL = pandas answers · 🔒 explain broadcasting in 5 sentences, then write `clean(df)` in ≤20 lines, no notes.

---

## Build project

**"One messy table, cleaned."** Titanic (or any public CSV you like): missing-value report before/after, 3 SQL questions with the same answers in pandas, and a README that someone else can run with `uv sync`. Small on purpose: the real goal is a working setup you will reuse in every later track.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- broadcasting: when do two shapes fit?
- `axis=0` vs `axis=1`
- git: add → commit → push, and what `.gitignore` is for
- 3 ways to handle missing values, and when each is wrong
- `GROUP BY` in SQL = `groupby` in pandas
