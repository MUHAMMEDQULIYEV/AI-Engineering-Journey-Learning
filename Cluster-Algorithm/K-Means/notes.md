# K-Means Clustering — Notes

## What K-Means does
Groups data into `k` clusters by repeatedly:
1. Assigning each point to its nearest centroid (Euclidean distance)
2. Recomputing each centroid as the **mean** of the points assigned to it
3. Repeating until centroids stop moving (or `max_iter` is hit)

A centroid is nothing more than the column-wise average of its cluster's points —
e.g. for points (2,4), (4,6), (6,8): centroid = (4, 6).

## Stopping condition
- Centroids stop moving (below a tiny threshold), **or**
- No points change cluster assignment between iterations, **or**
- `max_iter` reached (safety net, e.g. `max_iter=300`)

## k
`k` = number of clusters, chosen **before** running the algorithm. K-Means will
force the data into `k` groups even if that's the wrong number — it never tells
you if you picked badly.

## Inertia
Sum of squared distances from every point to its own centroid:

```
inertia = Σ (distance from point to its centroid)²
```

- Lower inertia = tighter clusters
- **Always decreases as k increases** (hits 0 when k = n), so you can't just
  minimize it — use the **elbow method**: plot inertia vs k, look for the bend.

## Silhouette coefficient / score
For one point `i`:
```
s(i) = (b(i) - a(i)) / max(a(i), b(i))
```
- `a(i)` = avg distance to points in its own cluster
- `b(i)` = avg distance to points in the nearest other cluster
- Range: -1 (bad fit) to +1 (great fit), 0 = on the boundary

**Silhouette score** = mean of `s(i)` across all points — one number to compare
different k values (unlike inertia, doesn't automatically favor bigger k).

**Silhouette diagram** = plots each point's `s(i)`, grouped by cluster, sorted —
reveals uneven/weak clusters that the average score alone hides.

## Random initialization problem
Random starting centroid positions can lead K-Means into a bad **local minimum**
(e.g. splitting one true cluster into two). Same data + same k can converge to
different results depending on the random start.

**Fixes (both on by default in sklearn):**
- `n_init` — run K-Means multiple times with different random starts, keep the
  lowest-inertia result
- `init="k-means++"` (sklearn default) — spreads initial centroids out on
  purpose: pick the first centroid randomly, then pick each next one with
  probability proportional to its distance from existing centroids

k-means++ *reduces the chance* of a bad local minimum — it doesn't guarantee
low inertia by itself. Combine with `n_init` for reliability.

## Choosing k automatically
- **KneeLocator** (`pip install kneed`) — finds the elbow point mathematically
  instead of eyeballing the inertia-vs-k plot
  ```python
  from kneed import KneeLocator
  kl = KneeLocator(k_range, inertias, curve="convex", direction="decreasing")
  best_k = kl.elbow
  ```
- **Silhouette scoring as a k-selection method** — compute avg silhouette score
  for several k values, pick the k with the highest score
  ```python
  from sklearn.metrics import silhouette_score
  score = silhouette_score(X_train_scaled, kmeans.labels_)
  ```
  `X_train_scaled` = the (scaled) data points; `kmeans.labels_` = the cluster
  assignment sklearn already computed during `.fit()`. Both must correspond to
  the same fitted model.

Neither method is authoritative alone — cross-check both.

## Accelerated K-Means (`algorithm="elkan"`)
Same result as standard Lloyd's algorithm, just faster: uses the triangle
inequality to skip distance calculations that are provably unnecessary.
Advantage shows up more with larger k and larger, well-separated datasets.

## Mini-Batch K-Means
Updates centroids using small random batches of data per iteration instead of
the full dataset. Trades slightly worse inertia for much better speed/memory
on large datasets — use when data doesn't comfortably fit in memory.

## `make_blobs`
Synthetic data generator from `sklearn.datasets` — creates fake clustered data
with known ground-truth labels, useful for testing/validating clustering code
before using it on real data where the true cluster count is unknown.

Key params: `n_samples`, `centers` (number of clusters), `n_features`
(dimensionality — 2 for plotting directly, more for realistic practice),
`cluster_std` (spread/noise), `random_state`.

Increasing `n_features` doesn't change the number of clusters — it changes the
dimensionality of each point. Distance and centroid formulas just extend to
more terms (more columns to average / more squared differences to sum).
Higher dimensions can make clustering harder ("curse of dimensionality") and
require dimensionality reduction (PCA) to visualize.

## K-Means vs DBSCAN vs anomaly detection
Not a strict hierarchy — different assumptions:
- **K-Means**: fast, scales well, assumes round/blob-shaped, similar-sized
  clusters, you must know `k` in advance
- **DBSCAN**: no need to pick `k`, handles irregular shapes, flags outliers as
  noise automatically — but sensitive to density parameters, struggles with
  clusters of very different densities
- **Anomaly detection** (Isolation Forest, One-Class SVM, etc.): a different
  task entirely — finds rare points that don't belong anywhere, not a
  clustering replacement