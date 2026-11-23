# PowerPoint guide

## Shared editing workspaces

- [Open the shared paper in Google Docs](https://docs.google.com/document/d/1n6r_RNnZF4_JKkvL_ajq9tNtQcpMoi3ajJ07_u9zYlE/edit)
- [Open the shared presentation in Google Slides](https://docs.google.com/presentation/d/1yE4NqbIkax0z4iZ3ZzpTb0OBpdWHKArRkACLLi1wjIc/edit)

Work in these shared originals so everyone sees the latest version. Linking a file here does not grant Google editing access; the owner manages access through Share.

| Member | Paper sections | Slides |
|---|---|---|
| Dem | Introduction and algorithm | 1–4 |
| Renee | Data and experiment method | 5–7 |
| Jacob | Results, analysis, and conclusion | 8–10 |

Edit your assigned sections/slides. Use comments or suggestions for a teammate's work. Keep the existing issue checklists as the task instructions. Dem combines all code, paper sections, and slides and handles final testing and submission exports. Jacob owns the last paper section and slides, so he formats the completed paper and presentation consistently after Dem combines them. Each author supplies their own content and fixes requested corrections.


The shared deck now has **10 slides**, with an introduction at the beginning. Dem owns 4 slides; Renee and Jacob own 3 each. Target about 12 minutes including the demo; maximum 15 minutes. Allow about 4–5 minutes for Dem and adjust the remaining speaking time during rehearsal.

| Slide | Owner | Put on the slide |
|---|---|---|
| 1 | Dem | Introduction: title, team, number-search goal, experiment overview |
| 2 | Dem | What the filter stores: membership, draws versus distinct values, array and symbols |
| 3 | Dem | Hashing, insertion, search, time complexity and actual storage |
| 4 | Dem | Worked bit-array example, false positives and why false negatives do not occur |
| 5 | Renee | Data and experiment setup: range, duplicates, seed and tested configurations |
| 6 | Renee | Actual known-present query and verified output |
| 7 | Renee | Actual known-absent query and output; explain a false positive if one occurs |
| 8 | Jacob | Measured lookup performance chart with units |
| 9 | Jacob | False-positive results and filter-size comparison |
| 10 | Jacob | Conclusions, limitations and references |

Dem's four slides contain presentation content and plain-English explanations of the mathematics. Renee's and Jacob's slides are **templates only**: each owner must add their own content and measured evidence. Speaker notes contain slide-specific instructions, source files and speaking guidance.

Keep the shared navy, white and teal design. Explain mathematical symbols in English so the audience can follow the slide. Use readable text and concise sentences. Keep detailed guidance in speaker notes and replace template instructions before presenting.

Renee's speaking time includes the live demo; keep saved output or a screenshot ready. Jacob uses the current `results/results.csv` and the restored shared filter, not older arithmetic-hash measurements. Dem combines everyone's work and handles final testing and exports. Jacob formats the completed deck consistently.

Rehearse together and time the entire talk. Everyone should answer: What does a positive mean? Why are false negatives absent in a correct insertion-only filter? How did we confirm a number was absent? What did our timing actually show?

Save slides/Bloom_Filter_Presentation.pptx and a PDF backup. The shared deck is the working copy. Complete the templates and verify all reported values against the final CSV before exporting.
