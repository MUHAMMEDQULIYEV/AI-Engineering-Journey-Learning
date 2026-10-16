# 02 · Classical ML (8 weeks)

🧪 draft, not walked yet · example work by the author: [ML-Fundamentals](../../ML-Fundamentals/) (imbalanced data, SMOTE) and [Cluster-Algorithm](../../Cluster-Algorithm/) (K-Means, DBSCAN)

**Goal:** you can take a table, split it honestly, train a baseline and a strong model with scikit-learn, and explain why one is better.
**Done:** a Kaggle tabular project with a `Pipeline`, cross-validation, a baseline vs gradient-boosting table and an error analysis, pushed · 🔒 explain the bias-variance trade-off in 5 sentences, then write k-fold cross-validation by hand (index splits) in ≤20 lines, no notes.

**Prerequisites:** [00 setup](00-setup.md), [01 math](01-math.md) (at least weeks 1–4: matrices, gradients).

Day jobs: [../../roadmap/README.md](../../roadmap/README.md). LEARN = 👀 first, ≤30 min reading, 1 predict question. BUILD = without the book. SHIP = push. REVIEW = AI-off recall + blank-file rebuild.

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| On-ramp (weeks 1–2) | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) | ISLP ch. 3–4 | [MLU-Explain](https://mlu-explain.github.io/): linear + logistic regression, ROC/AUC, precision/recall |
| Whole track (weeks 3–7) | [ISLP, *An Introduction to Statistical Learning with Python*](https://www.statlearning.com/) (2023, free PDF + Python labs). Ch. 2, 4, 5, 6, 8, 9, 12; skip survival + multiple testing | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) · [StatQuest](https://statquest.org/) | [MLU-Explain](https://mlu-explain.github.io/): bias-variance, CV, trees, random forest, double descent · [bias-variance demo](https://web-apps.thecoatlessprofessor.com/data/bias-variance-tradeoff-demo-app/bias-variance-tradeoff-demo.html) |
| PCA + clustering | ISLP ch. 12 | scikit-learn user guide | [Setosa PCA](https://setosa.io/ev/principal-component-analysis/) · [Distill: t-SNE](https://distill.pub/2016/misread-tsne/) |
| Evaluation + features | scikit-learn user guide, "Model selection and evaluation" | [Kaggle Learn](https://www.kaggle.com/learn) | [Setosa OLS](https://setosa.io/ev/ordinary-least-squares-regression/) |

Not used: Andrew Ng's ML Specialization (free audit unclear), Géron's book (paid). R2D3's decision-tree story (http://www.r2d3.us/visual-intro-to-machine-learning-part-1/) is great but was down (HTTP 522) when checked; try it, skip it if it doesn't load.

---

## Block A · On-ramp (2 weeks)

### Week 1 · Linear regression, loss, train / val / test

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 MLU-Explain linear regression · MLCC linear regression + loss (≤30 min) · predict: MSE of predictions `[2, 4]` vs truth `[3, 3]`? (answer: 1) | notebook + 3 lines of notes |
| ☐ BUILD | Without the course: `fetch_california_housing`, split 60/20/20 with a fixed seed, `LinearRegression`, MSE on train / val / test. Predict which is lowest first | 3 numbers |
| ☐ SHIP | Your GD linear regression from [01](01-math.md) week 4 on the same data (scale features first): same MSE as sklearn ± 1%? Push | commit |
| ☐ REVIEW | AI-off: 🧠 normal equation · blank-file split + fit + MSE in ≤10 lines | rebuild runs |

### Week 2 · Logistic regression, classification metrics

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 MLU-Explain logistic regression + precision/recall + ROC/AUC · MLCC classification (≤30 min) · predict: 100 samples, 90 negative, the model says "negative" for all: accuracy and recall? (answer: 90%, 0) | notes |
| ☐ BUILD | Without the course: `load_breast_cancer`, `LogisticRegression`, confusion matrix **by hand** from `y_pred` (4 counts), then precision, recall, F1; check vs `classification_report` | numbers match |
| ☐ SHIP | ROC curve by hand: 20 thresholds → TPR, FPR → plot; compare with `roc_auc_score`. Push | plot + commit |
| ☐ REVIEW | AI-off: 🧠 MSE vs log loss: which for which task? · blank-file confusion matrix in ≤10 lines | rebuild runs |

**Done:** train/val/test MSE table · hand confusion matrix = sklearn · 🔒 explain precision vs recall in 5 sentences, then write both from `y_true`, `y_pred` in ≤20 lines, no notes.

---

## Block B · Core ideas from ISLP (3 weeks)

### Week 3 · Bias-variance, cross-validation (ISLP ch. 2, 5)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 bias-variance demo + MLU-Explain CV · ISLP ch. 2.2 (≤30 min) · predict: polynomial degree 1 vs 15 on 20 points: which has lower train error, which lower test error? | notes |
| ☐ BUILD | Without the book: 20 noisy points from `sin(x)`, fit degree 1, 3, 15, plot train + val error vs degree · 5-fold CV by hand (shuffle indices, 5 slices) vs `cross_val_score` | U-shaped val curve |
| ☐ SHIP | Pick the degree with CV, report test error once. Push | commit |
| ☐ REVIEW | AI-off: 🧠 precision vs recall · blank-file k-fold in ≤20 lines | the 🔒 check, first try |

### Week 4 · Regularization + kNN (ISLP ch. 6, 4)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | ISLP ch. 6.2 ridge + lasso (≤30 min) · predict: lasso with a very large alpha on 10 features: how many coefficients are 0? (answer: all 10) | notes |
| ☐ BUILD | Without the book: ridge and lasso on `load_diabetes` (10 features), 20 alphas, plot the coefficient paths · scale first, and say why in 1 line | 2 plots |
| ☐ SHIP | kNN classifier from scratch (distances + majority vote) in ≤20 lines, k = 1, 5, 15 on Iris vs `KNeighborsClassifier`. Push | same accuracy |
| ☐ REVIEW | AI-off: 🧠 bias-variance · blank-file kNN | rebuild runs |

### Week 5 · Trees, random forests, gradient boosting (ISLP ch. 8)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 MLU-Explain decision trees + random forest · ISLP ch. 8.1 (≤30 min) · predict: Gini of a node with 5 yes / 5 no? (answer: 0.5) and 10 yes / 0 no? (answer: 0) | notes |
| ☐ BUILD | Without the book: Gini + best split for **one** numeric feature from scratch (try every threshold) · check against a depth-1 `DecisionTreeClassifier` | same threshold |
| ☐ SHIP | Same dataset: tree vs `RandomForestClassifier` vs `HistGradientBoostingClassifier`, 5-fold CV, one table. Push | table + commit |
| ☐ REVIEW | AI-off: 🧠 ridge vs lasso · blank-file Gini split in ≤20 lines | rebuild runs |

**Done:** U-shaped val curve plot · coefficient paths plot · model comparison table · 🔒 explain why a random forest beats one tree in 5 sentences, then write the Gini best split in ≤20 lines, no notes.

---

## Block C · Unsupervised + real pipelines (2 weeks)

### Week 6 · SVM (light), PCA, k-means (ISLP ch. 9, 12)

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Setosa PCA + Distill t-SNE · ISLP ch. 12.4 clustering (≤30 min) · predict: 3 well-separated blobs, k-means with k = 1 vs k = 3: does the inertia go down a little or a lot? | notes |
| ☐ BUILD | Without the book: k-means from scratch (assign → update, 10 iterations) on `make_blobs`, compare with `KMeans` · elbow plot k = 1…8 | 2 plots |
| ☐ SHIP | Your PCA from [01](01-math.md) → 2D → k-means on digits; color by the true label. One SVM (`SVC`, linear vs RBF) on the same 2D data, 1 line on which won. Push | commit |
| ☐ REVIEW | AI-off: 🧠 Gini · blank-file k-means in ≤20 lines | rebuild runs |

### Week 7 · Features, Pipeline, leakage, imbalance

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | scikit-learn guide: "Model selection and evaluation" + `Pipeline` / `ColumnTransformer` pages (≤30 min) · predict: you scale **before** the train/test split. Is the test score too high, too low, or fine? (answer: a bit too high, that's leakage) | notes |
| ☐ BUILD | Without the guide: `Pipeline(imputer → OneHotEncoder + StandardScaler → model)` on your cleaned Titanic from [00](00-setup.md) · `GridSearchCV` over 6 combos | best params printed |
| ☐ SHIP | Imbalance: class weights vs SMOTE vs nothing on one imbalanced set, PR-AUC for each (see the author's [ML-Fundamentals](../../ML-Fundamentals/)). Push | table + commit |
| ☐ REVIEW | AI-off: 🧠 k-means · blank-file Pipeline in ≤15 lines | rebuild runs |

**Done:** k-means = sklearn on blobs · Pipeline + GridSearchCV runs · imbalance table · 🔒 explain data leakage in 5 sentences, then write a leak-free Pipeline + CV in ≤20 lines, no notes.

---

## Block D · Project (1 week)

### Week 8 · Kaggle tabular project

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | Pick one: Titanic, House Prices, or a stroke dataset. EDA: 5 plots max · predict the baseline (majority class or the mean) score before you compute it | EDA notebook |
| ☐ BUILD | Without help: Pipeline + 5-fold CV · baseline vs logistic / ridge vs `HistGradientBoosting` | 3-row table |
| ☐ SHIP | `permutation_importance` top 5 features · look at the 10 worst errors and write 3 lines on why they fail · README with the table + plot. Push | **project** ✅ |
| ☐ REVIEW | AI-off: 🧠 leakage · 🔒 k-fold by hand in ≤20 lines | the 🔒 check |

**Done:** the project README has the baseline row, the best row, the top features and the error notes · 🔒 explain bias-variance in 5 sentences, then write k-fold by hand in ≤20 lines, no notes.

---

## Build project

**"Honest tabular model."** One Kaggle tabular dataset, a scikit-learn `Pipeline`, 5-fold CV, baseline vs gradient boosting, permutation importance and an honest error analysis (where does it fail, and why?). CPU only. Submit to Kaggle once if it's a competition, and put the score in the README.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- train / val / test: what each one is for
- precision, recall, F1, ROC-AUC
- bias-variance and the U-shaped val curve
- k-fold CV by hand
- ridge vs lasso (which one makes zeros?)
- Gini + how a tree picks a split
- bagging (random forest) vs boosting
- k-means steps
- data leakage: 2 examples
- class imbalance: 3 fixes
