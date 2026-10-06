# Session log

The only log. One row per study session. The **🧠 Recalled → next due** column is the only place where recall dates live: `Start session` picks the **oldest due** topic from the whole log.
Write the result (✅ / partial / ❌) and the next due date from the [gap ladder](../learning-methods.md#the-gap-ladder-spaced-recall): 1 → 3 → 7 → 21 → 60 days. ✅ = one step up, partial = same step, ❌ = back to 1 day. A new topic starts at 1 day.
On REVIEW day, also fill a [weekly check-in](weekly-checkin.md) and put its link in that row.
Minimum days (15 min) don't need a row: NEXT + commit is enough.

| Date | Plan row | Output (link / commit) | Skipped or open | 🧠 Recalled (✅/partial/❌) → next due | NEXT |
|---|---|---|---|---|---|
| 2026-01-01 *(example)* | Block 1 · LEARN | tokenizer notebook, commit `<hash>` | vocab predict | new: BPE → 2026-01-02 | char tokenizer encode() |
| 2026-01-02 *(example)* | Block 1 · BUILD | BPE `merge()` from blank file, commit `<hash>` | — | BPE ✅ → 2026-01-05 | encode() with merges |
