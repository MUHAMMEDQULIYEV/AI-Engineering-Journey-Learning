# ML Fundamentals: my notes

Written in my own words. Fill each part after I understand it, without copying from the chat.

## 1. Decision thresholds
- What a threshold is:
- Precision (its denominator is ...):
- Recall (its denominator is ...):
- Lower threshold → precision ___, recall ___
- Cancer screening wants ___ because:
- Spam filter wants ___ because:
- One sentence: how do I choose the threshold?

## 2. ROC-AUC vs PR-AUC
- ROC curve axes:
- FPR means:
- What AUC = 0.5 means:
- When PR-AUC is better:

## 3. SMOTE
(later)

## 4. Target encoding leakage
(later)

## My mistakes
- Thought precision at threshold 0.7 was 0.5. It was 1.0, because precision divides by what I **flagged** (only 1), not by the real positives.
- Said cancer screening wants precision. It wants recall: a missed cancer costs far more than a false alarm.
