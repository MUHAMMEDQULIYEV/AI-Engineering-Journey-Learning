# Stroke dataset: progress (10.10.2026)

Goal: clean the data myself → split → SMOTE on the training set only → compare ROC-AUC and PR-AUC.

## Done
- Loaded the data (5110 rows, 12 columns). The file is really a CSV, so use `read_csv`.
- `bmi`: 201 NaN (~4%)
- `value_counts()` loop on the object columns found:
  - `gender == "Other"`: 1 row
  - `smoking_status == "Unknown"`: 1544 rows (~30%), mostly young people / children

## Cleaning decisions
1. Drop the 1 `Other` gender row (keep the column) ← **code not written yet**
2. Keep `Unknown` smoking as its own category. Don't fill it with the mode: that would invent 1544 non-smokers.
3. Fill `bmi` NaN with the **median** (outliers pull the mean), computed on the **training set only**, after the split
4. BMI outliers (max 97.6): keep / cap / drop? Depends on how many there are and which model I use.

## When I come back: start here
- Open question: how many rows have `bmi > 60`? My guess first: under 20 or over 100?
- Then write step 1 (drop the `Other` row). Predict the new row count first.

## Rules to remember
- Split first, then median-fill and SMOTE on the **train** set only. The test set stays real and imbalanced.
- With imbalanced data, look at PR-AUC, not only ROC-AUC.
