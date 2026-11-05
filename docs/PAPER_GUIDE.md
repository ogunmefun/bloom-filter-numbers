# Paper guide

## Shared editing workspaces

- [Open the shared paper in Google Docs](https://docs.google.com/document/d/1n6r_RNnZF4_JKkvL_ajq9tNtQcpMoi3ajJ07_u9zYlE/edit)
- [Open the shared presentation in Google Slides](https://docs.google.com/presentation/d/1yE4NqbIkax0z4iZ3ZzpTb0OBpdWHKArRkACLLi1wjIc/edit)

Work in these shared originals so everyone sees the latest version. Linking a file here does not grant Google editing access; the owner manages access through Share.

| Member | Paper sections | Slides |
|---|---|---|
| Dem | Introduction and algorithm | 1–3 |
| Renee | Data and experiment method | 4–6 |
| Jacob | Results, analysis, and conclusion | 7–9 |

Edit your assigned sections/slides. Use comments or suggestions for a teammate's work. Keep the existing issue checklists as the task instructions. Renee handles final paper formatting; Jacob handles final slide formatting. Export final DOCX/PDF and PPTX/PDF copies to the repository for submission.


Target 6–7 single-spaced pages total; maximum 8. Use a short title block instead of a separate cover page. Include all three names. Keep figures and references inside the limit.

| Author | Sections | Target |
|---|---|---|
| Dem | Introduction; how the algorithm works; pseudocode and complexity | About 2 pages |
| Renee | Data generation; study design; demo and test procedure | About 2 pages |
| Jacob | Measured results; analysis; limitations; conclusion | About 2 pages |
| Everyone | References for their own sources; final review | Remaining space |

## Questions to answer

**Dem:** What problem are we solving? What are m and k? How are numbers hashed into positions? Why can different numbers share positions? Why does a zero bit rule out membership, while all-one positions cannot prove membership? Explain O(k) per operation under fixed-size integer/hash assumptions, O(Nk) construction, and theoretical m-bit storage. A Python list or bytearray can use more memory than m packed bits; do not claim measured memory savings without measuring.

**Renee:** How were the 1,000 random draws generated? What seeds make the study repeatable? How many distinct values occurred? How did we verify a query was present or absent? Explain the 18 configurations: 3 input counts × 3 seeds × 2 filter sizes, with k=3. Record environment, batch repetitions, time units, and exact query set.

**Jacob:** What happened? Include a table and one chart from real measurements. Compare lookup time, construction cost, and false-positive rate. Discuss the effect of filter size and distinct insertions. Do not assume faster results or invent a false positive. Explain limitations and summarize what the experiment supports.

## Results table template

| Draws | Distinct values | Seed | m | k | Absent queries | False positives | FP rate | Build time | Bloom lookup | List lookup |
|---|---|---|---|---|---|---|---|---|---|---|

Fill with actual output; include units in time headers. False-positive rate = false positives / known-absent queries. Check every distinct inserted value: there should be zero false negatives.

Optional extension only: compare observed rate with the approximation (1 - exp(-k*n/m))^k, where n is the distinct inserted count, assuming approximately independent uniform hashes. This is not required for the simple project.

## Assembly

Each author sends their section and citations to Renee. Renee combines and formats; authors fix their own content after review. Save the final DOCX and PDF in paper/. Check page count in the exported PDF. Use one consistent citation style and cite factual sources, reused illustrations, and any borrowed code. Keep raw results in results/ so claims can be checked.
