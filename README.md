# Bloom Filter: Searching for Numbers

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

## Equal work split

| Member | Sprint 1: build (~3 hours) | Sprint 2: paper (~2 hours) | Sprint 3: present (~2 hours) |
|---|---|---|---|
| Dem | [#1 Filter and hashes](../../issues/1) | [#4 Introduction and algorithm](../../issues/4) | [#7 Slides 1–3 and code check](../../issues/7) |
| Renee | [#2 Data and demo](../../issues/2) | [#5 Method and paper assembly](../../issues/5) | [#8 Slides 4–6 and demo](../../issues/8) |
| Jacob | [#3 Tests and measurements](../../issues/3) | [#6 Results and analysis](../../issues/6) | [#9 Slides 7–9 and deck assembly](../../issues/9) |

Each person owns 3 issues, about 2 pages of writing, 3 slides, and about 4 minutes of speaking. Estimates are planning targets; redistribute small tasks at check-ins if someone is overloaded. Review cycle: Dem reviews Renee, Renee reviews Jacob, Jacob reviews Dem.

Dem is assigned through the known GitHub account ogunmefun. Renee and Jacob are named in their issue titles/bodies; their GitHub usernames have not been provided.

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

Once implemented, intended run commands are `python demo.py` and `python experiments.py`. These commands are a target interface, not a claim that code already exists.

## Rubric requirements

Based on the supplied COSC 428/528 Fall 2026 project sheet:

- Submit a code listing of the running algorithm.
- Write a paper presenting the algorithm, study, results, and analysis: **no more than 8 single-spaced pages**.
- Present results to the class: **no more than 15 minutes**.
- The algorithm and proposed study require instructor approval; confirm the revised number-search study is approved and the algorithm was not already presented in class.
- All members receive the same grade; classmates score the talk.

Our targets are 6–7 pages total and a 12-minute talk, leaving margin. The rubric does not supply a deadline or citation style; agree on these with the instructor.
