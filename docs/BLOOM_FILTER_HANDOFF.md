# Bloom filter handoff and Sprint 1 validation

For Renee and Jacob: import `BloomFilter` from `bloom_filter`. Use a fresh instance for every dataset/configuration.

```python
from bloom_filter import BloomFilter
bf = BloomFilter(m=8000, k=3)
bf.add(2500)
print(bf.contains(2500))  # True means possibly present
print(bf.hash_positions(2500))  # Repeatable indices in [0, m)
```

The existing module-level insert/search functions remain available for Renee's demo. Their shared default filter starts empty. Importing the module no longer generates numbers, changes random state, inserts data, or prints output.

Hashes use SHA-256 on the ASCII string "salt:number", salts 0..k-1, digest converted to an integer modulo m. add sets entries to 1; contains checks all entries. Duplicates are harmless. The bytearray uses one byte per logical bit, not packed storage. Parameters and input must be integers (booleans excluded); m and k must be positive.

## Validation on November 15, 2026

Run from the repository root with Python 3:

```
python -m unittest discover -s tests -v
python demo.py
```

All 9 tests passed. Covered empty filter, repeated insertion, independent instances, repeatable/in-range positions, invalid inputs, silent import and legacy compatibility, and a deliberately saturated m=1 filter showing a false positive. No false negatives occurred across the 18 combinations of seeds 42/43/44, counts 250/500/1000, and sizes 2000/8000.

Renee's unchanged demo ran successfully with 1000 draws, 637 distinct values, present query 2654 returning True, and absent query 2004 returning False. This is a correctness smoke test, not the full performance experiment or a measured false-positive-rate study.

## Integration review for Renee

The current demo correctly uses inclusive randint bounds, seed 42, and an exact set difference to choose an absent value. It remains compatible with this module. To finish issue #2, it still needs generate_numbers(count=1000, seed=42), saved numbers/output files, and human-readable "possibly present"/"definitely absent" labels with exact membership. Keep a main guard so importing the future generator does not execute the demo. No changes to Renee's demo have been made here.

The shared paper was blank when opened for Sprint 2, so Renee's written method section was not available for review. Review it after she adds it. Jacob's independent peer review and an actual group walkthrough remain human follow-up items; this document provides the interface and explanation for that handoff.
