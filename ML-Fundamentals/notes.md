# ML Fundamentals: my notes

Written in my own words. Fill each part after I understand it, without copying from the chat.

## 1. Decision thresholds
- What a threshold is: a value that separates positive and negative. If the score is higher than the threshold, the model says spam. It can still be wrong, so we have to choose the threshold carefully.
- Precision = TP / flagged (everything the model called positive)
- Recall = TP / all real positives (how many real positives the model caught)
- Lower threshold → precision decreases, recall increases
- Cancer screening wants recall because missing a sick person is the worst mistake. A false alarm is OK, the doctor can check again. → lower threshold
- Spam filter wants precision because a real email in the spam folder is the worst mistake (I never see it). A spam in my inbox is only annoying. → higher threshold, only send to spam when the model is very sure
- How do I choose the threshold: I can't get minimum FPR and maximum recall at the same time, so I ask "which mistake costs more?" and move the threshold that way.

## 2. ROC-AUC vs PR-AUC
- ROC curve axes: x = FPR, y = recall (TPR)
- FPR = FP / (FP + TN) = FP / all real negatives
- AUC = 0.5 means: guessing randomly (the diagonal line)
- When PR-AUC is better: when the data is highly imbalanced (positives are rare)
- Why: FPR divides by all real negatives, which is a huge number. Example 10 spam / 10,000 normal, 100 false alarms: FPR = 100 / 10,000 = 0.01 (looks great). Precision divides by what I flagged: 10 / 110 = 0.09 (looks bad, and that is the truth). So ROC-AUC looks too good and PR-AUC shows the real problem.

## 3. SMOTE
(later)

## 4. Target encoding leakage
(later)

## My mistakes
- Thought precision at threshold 0.7 was 0.5. It was 1.0, because precision divides by what I **flagged** (only 1), not by the real positives.
- Said cancer screening wants precision. It wants recall: a missed cancer costs far more than a false alarm.
