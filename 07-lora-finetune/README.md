# 07 · Open model vs API: LoRA fine-tune (Block 8, weeks 1–3) → portfolio repo #3
Goal: one LoRA SFT run on my own task, scored on the flagship eval set against the base open model and the API model.
Plan: [roadmap/plan.md → Block 8](../roadmap/plan.md#block-8--job-ready-12-weeks-ends-end-of-jul)

## Steps
- [ ] dataset: 500–2k examples distilled from the API model (see [resources.md](../roadmap/resources.md))
- [ ] LoRA SFT on Colab with PEFT + TRL, on the *same small open model* the flagship can run on (Block 7)
- [ ] push the adapter to the Hugging Face Hub
- [ ] before/after table on the flagship eval set: base open model vs LoRA vs API model, with cost + latency

## Done when
- [ ] the before/after table is in this README
- [ ] 🔒 explain LoRA in 5 sentences, then write a LoRA linear layer (`W x + B A x`) in ≤20 lines, no notes

## Results
| Model | Pass rate | Cost / question | Latency |
|---|---|---|---|
| base open model | | | |
| + LoRA | | | |
| API model | | | |

## Files (I create them)
- notebook(s)
- `notes.md`: in my own words
