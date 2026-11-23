"""Jacob's timing and false-positive checks, using the shared filter API.

Run: python experiments.py
Times are seconds; lookup times are per query over 20 repeated batches.
"""
import csv
from pathlib import Path
import random
from time import perf_counter

from bloom_filter import BloomFilter
from demo import generate_numbers


def measure_lookup(lookup, queries, repeats):
    start = perf_counter()
    for _ in range(repeats):
        for number in queries:
            lookup(number)
    return (perf_counter() - start) / (repeats * len(queries))


def run_case(count, seed, m, k=3, repeats=20):
    if repeats <= 0:
        raise ValueError("repeats must be positive")
    numbers = generate_numbers(count, seed)
    actual = set(numbers)
    start = perf_counter()
    bf = BloomFilter(m=m, k=k)
    for number in numbers:
        bf.add(number)
    build_time = perf_counter() - start
    absent = sorted(set(range(2000, 3001)) - actual)
    false_negatives = sum(not bf.contains(n) for n in actual)
    false_positives = sum(bf.contains(n) for n in absent)
    if false_negatives:
        raise AssertionError("An inserted number was reported absent")
    queries = list(range(2000, 3001))
    random.Random(seed).shuffle(queries)
    return {
        "seed": seed, "draws": count, "distinct_count": len(actual),
        "m": m, "k": k, "absent_queries": len(absent),
        "false_positives": false_positives,
        "false_positive_rate": false_positives / len(absent) if absent else None,
        "false_negatives": false_negatives,
        "build_seconds": build_time, "batch_repetitions": repeats,
        "queries_per_batch": len(queries),
        "bloom_seconds_per_query": measure_lookup(bf.contains, queries, repeats),
        "list_seconds_per_query": measure_lookup(numbers.__contains__, queries, repeats),
    }


def main():
    rows = [run_case(count, seed, m)
            for count in (250, 500, 1000)
            for seed in (42, 43, 44)
            for m in (2000, 8000)]
    destination = Path(__file__).resolve().parent / "results" / "results.csv"
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for row in rows:
        print(f"draws={row['draws']} seed={row['seed']} m={row['m']}: "
              f"{row['false_positives']}/{row['absent_queries']} false positives "
              f"({row['false_positive_rate']:.2%}), "
              f"false negatives={row['false_negatives']}")
    print(f"Saved {len(rows)} configurations to {destination}")
    print("Lookup times: seconds per query, 20 batches of 1001 shuffled queries.")
    print("Timings vary by machine; zero observed false positives is not a guarantee.")


if __name__ == "__main__":
    main()
