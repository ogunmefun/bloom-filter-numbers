# Code freeze

Frozen on November 22, 2026 after GitHub-hosted verification passed.

- Tested commit: [`dbe1355e3eff34a988f2909612107c122864a1d2`](https://github.com/ogunmefun/bloom-filter-numbers/commit/dbe1355e3eff34a988f2909612107c122864a1d2)
- Snapshot branch: [code-freeze-2026-11-22](https://github.com/ogunmefun/bloom-filter-numbers/tree/code-freeze-2026-11-22)
- [Passing GitHub Actions run](https://github.com/ogunmefun/bloom-filter-numbers/actions/runs/45093952786)
- Team deadline: **Sunday, November 29, 2026, 11:59 p.m. Eastern Time**.

## Freeze rules

Keep `bloom_filter.py`, `demo.py` and `experiments.py` unchanged while finishing the paper and slides. Keep the shared result files consistent with this version. Do not rewrite the algorithm, change hashes/configurations or replace results with a different implementation.

This is a documented team freeze with a saved snapshot, not a GitHub permissions lock. The exact commit above remains the reference even if someone moves a branch.

If a confirmed bug appears, report it in a GitHub issue with reproduction steps. Dem reviews the fix before integration. Rerun GitHub verification, record the new tested commit, and update affected measurements, paper text and slides together. Documentation, paper, slide, chart and formatting work can continue.

## Verification completed

GitHub-hosted Ubuntu jobs passed on Python 3.12 and 3.13:
- 16 tests, including invalid inputs, independent filters, duplicate insertions, silent imports and repeatable generation.
- The demo produces 1,000 draws, 637 distinct numbers, and correct present/absent examples.
- All 18 planned configurations run with zero false negatives.
- Every configuration's distinct count, absent count, false-positive count and rate agree with the committed CSV.
- Tests execute both command-line programs from another working directory and validate their saved outputs.
- The run uploaded separate result artifacts and Python/platform information for each Python version.

## Refinements made before freezing

The generator rejects negative or non-integer counts. Experiment repetitions must be positive integers. Both commands support `--output-dir`, and their default output directory is the repository's `results/` folder. These changes do not alter the hashes, generated default data or deterministic error counts.

## One source of results

Use the committed `results/results.csv` and `results/demo.txt` for the paper and slides. The CSV's original local timings are retained to prevent conflicting charts. GitHub artifacts are separate validation runs, not replacement presentation timings. Wall-clock times vary by machine and must not be compared for exact equality.

To verify without overwriting the shared results:

```sh
python -m unittest discover -s tests -v
python demo.py --output-dir verification-output
python experiments.py --output-dir verification-output
```

Do not commit `verification-output/`. The Actions workflow runs on code/result changes and pull requests, and can also be started manually. Its artifacts expire after 30 days; the committed canonical CSV remains available.

[Everyone's next-step checklist](NEXT_STEPS.md)
