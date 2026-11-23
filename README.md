# Bloom Filter: Searching for Numbers

## Deadline and code freeze

**Team completion deadline: Sunday, November 29, 2026, by 11:59 p.m. Eastern Time.**

**Start with [your next-step checklist](docs/NEXT_STEPS.md).** Dem handles combining/final testing, Renee finishes methods and slides 5–7, and Jacob finishes analysis/charts and slides 8–10. Dem's slides are 1–4. The deck has 10 slides.

The code passed [GitHub Actions on Python 3.12 and 3.13](https://github.com/ogunmefun/bloom-filter-numbers/actions/runs/45093952786) and is now under a [team code freeze](docs/CODE_FREEZE.md). Use the [tested snapshot](https://github.com/ogunmefun/bloom-filter-numbers/tree/code-freeze-2026-11-22). Keep code and canonical results unchanged unless Dem coordinates a confirmed bug fix and revalidation.

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


Group project — Dem, Renee, and Jacob.

## Start here

This repository contains the team's work plan and nine scrum tasks. Code, measured results, the paper, and the PowerPoint are deliverables the team will create by following those tasks.

1. Find your name in the table below and open your Sprint 1 issue.
2. Read its checklist and comment "Started."
3. Complete the work, upload your files or submit a pull request, and request a teammate's review.
4. Close the issue only after its checklist is complete.

## Project goal

Generate a list of 1,000 random integers from 2,000 through 3,000 inclusive. Insert them into a Bloom filter using hash functions. Demonstrate one known-present query and one known-absent query, then measure lookup performance and false positives.

A Bloom filter answers **possibly present** or **definitely absent**. It does not retrieve a number's position in the list. Keep the original list and a set of its distinct numbers to verify answers.

Use Python 3 and standard-library modules to keep setup simple. Default filter: m=8000 positions and k=3 hashes. Duplicates are allowed: 1,000 draws do not mean 1,000 distinct numbers.

Dem's slides 1–4 contain presentation content. Slides 5–10 are designed templates for Renee and Jacob to complete using the instructions in their speaker notes.

## Work split

| Member | Sprint 1: build (~3 hours) | Sprint 2: paper (~2 hours) | Sprint 3: present and finalize |
|---|---|---|---|
| Dem | [#1 Filter and hashes](../../issues/1) | [#4 Introduction and algorithm](../../issues/4) | [#7 Slides 1–4, combining, and final testing](../../issues/7) |
| Renee | [#2 Data and demo](../../issues/2) | [#5 Method](../../issues/5) | [#8 Slides 5–7 and demo](../../issues/8) |
| Jacob | [#3 Tests and measurements](../../issues/3) | [#6 Results and paper formatting](../../issues/6) | [#9 Slides 8–10 and formatting](../../issues/9) |

The presentation now has 10 slides, including a new introduction at the beginning. Dem owns slides 1–4; Renee owns slides 5–7; Jacob owns slides 8–10. Each person still owns 3 issues and about 2 pages of writing. Allow about 4–5 minutes for Dem and adjust the group rehearsal toward 12 minutes total, never more than 15. Dem has chosen to take on the additional combining and final testing. Jacob handles formatting because he owns the final paper section and slides. Time estimates are approximate. Review cycle: Dem reviews Renee, Renee reviews Jacob, Jacob reviews Dem.

GitHub accounts: Dem is @ogunmefun, Renee is @renengobii, and Jacob is @JecoForcer.

## Three simple sprints

Suggested schedule, adjustable to your actual due date:

- **Sprint 1 — Days 1–3:** working code, demonstration, and recorded tests.
- **Sprint 2 — Days 4–5:** combine the paper and check results.
- **Sprint 3 — Days 6–7:** combine PowerPoint slides, rehearse, and check submission files.

Hold a 10-minute check-in at the beginning and end of each sprint. Each member says: "I finished __. Next I will __. I need help with __." Put that update on your current issue. Open issues are To Do; a "Started" comment means In Progress; reviewed and closed issues are Done. A separate project board is optional.

Dependencies: agree on the interfaces in #1 and #2 first. Renee can build data generation while Dem builds the filter; Jacob can prepare the experiment loop. Run integrated tests after both modules work. Write methods early, but use only actual measurements in the results and final slides.

## Guides

- [Paper instructions and outline](docs/PAPER_GUIDE.md)
- [PowerPoint instructions and slide outline](docs/POWERPOINT_GUIDE.md)
- [Final submission checklist](docs/SUBMISSION_CHECKLIST.md)
- [All scrum issues](https://github.com/ogunmefun/bloom-filter-numbers/issues)

## Planned files

- `bloom_filter.py` — Dem's filter.
- `demo.py` — Renee's data generator and two-query demonstration.
- `experiments.py` — Jacob's measurements and correctness checks.
- `results/` — generated numbers, demo output, CSV, and chart.
- `paper/Bloom_Filter_Paper.docx` and PDF — final paper.
- `slides/Bloom_Filter_Presentation.pptx` and PDF — final slides.

Run from the repository directory using Python 3 (no extra packages):

```sh
python -m unittest discover -s tests -v
python demo.py
python experiments.py
```

`bloom_filter.py` provides the shared `BloomFilter(m=8000, k=3)` class with salted SHA-256 hashing. Renee's demo uses this class. Jacob's timing and false-positive checks now live in `experiments.py`, which uses Renee's generator and writes `results/results.csv` for all 18 planned configurations. It checks every distinct inserted number for false negatives and every absent number in the range for false positives.

CSV rates are fractions (multiply by 100 for percentages). Build time includes filter initialization and insertion. Lookup times are seconds per query over 20 batches of the same 1,001 shuffled queries for Bloom and list membership. Printing and file writes are outside timing. An empty absent-query set produces a blank rate. Timings vary by machine; the CSV is one local run, not a universal speed claim.

The November 15 measurements from the separate arithmetic-hash implementation are historical and are superseded by this CSV. Jacob's paper draft is preserved, but its hash description, configuration, and measurements need reconciliation with the restored implementation before submission. The filter uses one byte per logical bit, not packed bits.

## Rubric requirements

Based on the supplied COSC 428/528 Fall 2026 project sheet:

- Submit a code listing of the running algorithm.
- Write a paper presenting the algorithm, study, results, and analysis: **no more than 8 single-spaced pages**.
- Present results to the class: **no more than 15 minutes**.
- The algorithm and proposed study require instructor approval; confirm the revised number-search study is approved and the algorithm was not already presented in class.
- All members receive the same grade; classmates score the talk.

Our targets are 6–7 pages total and a 12-minute talk, leaving margin. The rubric does not supply a deadline or citation style; agree on these with the instructor.

