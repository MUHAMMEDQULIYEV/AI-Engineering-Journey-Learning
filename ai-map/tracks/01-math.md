# 01 · Math for ML (6 weeks)

🧪 draft, not walked yet

**Goal:** you can read `y = Wx + b`, a gradient and a probability in an ML paper or course, and you can code each one in NumPy.
**Done:** the "math from scratch" notebook (PCA + linear regression + a bootstrap CI) runs and matches scikit-learn · 🔒 explain PCA in 5 sentences, then write PCA with `np.linalg.eigh` in ≤20 lines, no notes.

**Prerequisites:** [00 setup](00-setup.md) (NumPy, notebooks). School algebra.

Only the math ML uses: vectors, matrices, eigen/SVD, derivatives + chain rule, probability, basic statistics. Proofs are optional.
Day jobs: [../../roadmap/README.md](../../roadmap/README.md). LEARN = 👀 first, ≤30 min video, 1 predict question. BUILD = without the video. SHIP = push. REVIEW = AI-off recall + blank-file rebuild.

---

## Sources

| Topic | Main | Lookup only | 👀 See it |
|---|---|---|---|
| Linear algebra | [MIT 18.06SC (Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/): only elimination, the 4 spaces, orthogonality, eigen, SVD | [MML book](https://mml-book.github.io/) ch. 2–4 · [Khan linear algebra](https://www.khanacademy.org/math/linear-algebra) | [3Blue1Brown: Essence of LA](https://www.3blue1brown.com/topics/linear-algebra) (watch first, ~3 h total) · [Immersive Linear Algebra](https://immersivemath.com/ila/index.html) · [Setosa: eigenvectors](https://setosa.io/ev/) |
| Calculus, chain rule, gradients | [3Blue1Brown: Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) | [Khan multivariable calculus](https://www.khanacademy.org/math/multivariable-calculus) · MML ch. 5 | [3Blue1Brown calculus](https://www.3blue1brown.com/topics/calculus) · [Desmos](https://www.desmos.com/calculator) / [GeoGebra](https://www.geogebra.org/) to plot f and f′ |
| Probability + statistics | [Seeing Theory](https://seeing-theory.brown.edu/) (interactive, ~8 h) | [StatQuest](https://statquest.org/) · MML ch. 6 · [Harvard Stat 110](https://projects.iq.harvard.edu/stat110) (deeper; link returned 403 when checked, lectures are also on YouTube) | [Seeing Theory](https://seeing-theory.brown.edu/) · [3Blue1Brown probability](https://www.3blue1brown.com/topics/probability) · [Setosa: conditional probability](https://setosa.io/ev/) |

Why Seeing Theory and not Stat 110 as main: Stat 110 is ~30 h and its site could not be checked. Seeing Theory covers what ML needs in ~8 h. If you want the deep version later, add Stat 110 to your ideas list.
MIT 18.06SC is from 2011. The math did not change.

---

## Block A · Linear algebra (3 weeks)

### Week 1 · Vectors, dot product, matrices as functions

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 3Blue1Brown LA ch. 1–4 · predict: `[[2,0],[0,1]] @ [1,1]`? (answer: `[2,1]`, the x-axis is stretched) · code it in NumPy | notebook + 3 lines of notes |
| ☐ BUILD | Without the video: `matvec(A, x)` and `matmul(A, B)` with plain loops, check against `@` on random 3×3 and 2×4 · 4 points of a square → rotate 90° with a matrix → plot before/after | asserts pass + plot |
| ☐ SHIP | Dot product = length × length × cos: check on `[1,0]` and `[1,1]` (answer: 45°). Push | commit |
| ☐ REVIEW | AI-off: 🧠 broadcasting (from 00) · blank-file `matmul` with loops in ≤10 lines | rebuild runs |

### Week 2 · Solving `Ax = b`: elimination, rank, inverse

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Immersive LA, chapter on systems of equations · 18.06SC lecture on elimination (≤30 min) · predict: rank of `[[1,2],[2,4]]`? (answer: 1) | notes |
| ☐ BUILD | Without the video: Gaussian elimination for a 3×3 system, check vs `np.linalg.solve` · `np.linalg.matrix_rank` on 3 matrices, predict each first | asserts pass |
| ☐ SHIP | Determinant as area: `det([[2,0],[0,3]])` = 6, plot the unit square before/after. Push | commit |
| ☐ REVIEW | AI-off: 🧠 what `A @ x` means as a picture · blank-file elimination for 2×2 | rebuild runs |

### Week 3 · Projections, eigenvectors, SVD → PCA

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Setosa eigenvectors + 3Blue1Brown eigen chapter · 18.06SC eigen lecture (≤30 min) · predict: eigenvalues of `[[2,0],[0,3]]`? (answer: 2 and 3) | notes |
| ☐ BUILD | Without the video: power iteration, 20 steps, on a 2×2 symmetric matrix, compare with `np.linalg.eigh` · project `[3,4]` onto `[1,0]` (answer: `[3,0]`) | asserts pass |
| ☐ SHIP | **PCA from scratch** on Iris: center, covariance (4×4), `eigh`, keep 2 components, plot. Compare with `sklearn.decomposition.PCA` (signs may flip). Push | plot + commit |
| ☐ REVIEW | AI-off: 🧠 rank · blank-file PCA in ≤20 lines | the 🔒 check, first try |

**Done:** loops `matmul` = `@` · elimination = `np.linalg.solve` · your PCA = sklearn PCA (up to sign) · 🔒 explain eigenvectors in 5 sentences, then write power iteration in ≤20 lines, no notes.

---

## Block B · Calculus (1 week)

### Week 4 · Derivatives, chain rule, gradient descent

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Desmos: plot `w²` and `2w` · 3Blue1Brown calculus ch. 1–4 (≤30 min) · predict: `f(w) = w²`, w = 3 → slope? (answer: 6) | notes |
| ☐ BUILD | Without the video: numerical gradient `(f(w+h) − f(w−h)) / 2h` vs your hand derivative for 3 functions (`w²`, `sin w`, `(3w+1)²`) · chain rule on the last one: predict the gradient at w = 1 (answer: 24) | asserts pass |
| ☐ SHIP | Gradient descent on `f(w) = (w − 5)²`, lr 0.1, 20 steps, start at 0: predict where w ends (answer: ≈ 4.94) · then linear regression on 50 noisy points with GD **and** the normal equation `(XᵀX)⁻¹Xᵀy`, same weights? Push | 2 weight sets match |
| ☐ REVIEW | AI-off: 🧠 eigenvectors · blank-file GD loop in ≤10 lines | rebuild runs |

**Done:** numerical = analytic gradient on 3 functions · GD weights ≈ normal-equation weights · 🔒 explain the chain rule in 5 sentences, then write GD for linear regression in ≤20 lines, no notes.

---

## Block C · Probability + statistics (2 weeks)

### Week 5 · Probability, Bayes, expectation, variance

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Seeing Theory ch. 1–3 + Setosa conditional probability (≤30 min) · predict: a disease hits 1% of people, the test finds 90% of sick people and says "sick" for 9% of healthy people. P(sick \| positive)? (answer: ≈ 9%) | notes |
| ☐ BUILD | Without the site: simulate the test on 100,000 people, compare with Bayes' formula · mean + variance of a die from 10,000 rolls vs the exact 3.5 and 2.92 | sim ≈ formula |
| ☐ SHIP | Bernoulli, binomial, normal: sample 10,000 of each with NumPy, histogram, write mean + variance next to the formula. Push | 3 plots + commit |
| ☐ REVIEW | AI-off: 🧠 chain rule · blank-file Bayes simulation in ≤15 lines | rebuild runs |

### Week 6 · Sampling, CLT, confidence intervals, MLE

| Day | Task | Output |
|---|---|---|
| ☐ LEARN | 👀 Seeing Theory: probability distributions + frequentist inference (≤30 min) · predict: std of the mean of 25 dice rolls? (answer: 1.71 / 5 ≈ 0.34) | notes |
| ☐ BUILD | Without the site: CLT simulation (mean of n = 1, 5, 25 dice, 10,000 times, 3 histograms) · MLE of a coin: 7 heads in 10 → p̂ = 0.7, check by plotting the likelihood | plots |
| ☐ SHIP | Bootstrap 95% CI for the mean of 50 numbers (1,000 resamples). Finish the project README. Push | CI printed + commit |
| ☐ REVIEW | AI-off: 🧠 Bayes · 🔒 PCA in ≤20 lines from a blank file | the 🔒 check |

**Done:** CLT plots show the bell shape at n = 25 · bootstrap CI printed · 🔒 explain a confidence interval in 5 sentences, then write a bootstrap CI in ≤20 lines, no notes.

---

## Build project

**"Math from scratch in NumPy."** One repo, three parts: PCA (eigendecomposition) on Iris with an explained-variance plot, linear regression with GD and the normal equation (both match `sklearn.linear_model.LinearRegression`), and a bootstrap CI on a real column. CPU only.

## 🧠 Recall list

Gap ladder 1 → 3 → 7 → 21 → 60 days ([learning-methods.md](../../roadmap/learning-methods.md)):
- a matrix as a function (what `A @ x` does to the plane)
- rank and when `Ax = b` has no single answer
- eigenvectors + PCA in 5 sentences
- chain rule: `(3w+1)²` at w = 1
- gradient descent update rule
- Bayes with the 1% / 90% / 9% test
- CLT: why the std of a mean shrinks as 1/√n
- MLE for a coin
