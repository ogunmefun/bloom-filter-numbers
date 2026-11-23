"""End-to-end checks for the published demo and experiment commands."""
import csv
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest

from demo import generate_numbers
from experiments import run_case

ROOT = Path(__file__).resolve().parents[1]


class IntegrationTests(unittest.TestCase):
    def test_generator_is_repeatable_and_preserves_global_rng(self):
        state = random.getstate()
        values = generate_numbers()
        self.assertEqual(len(values), 1000)
        self.assertEqual(len(set(values)), 637)
        self.assertTrue(all(2000 <= n <= 3000 for n in values))
        self.assertEqual(values, generate_numbers())
        self.assertEqual(random.getstate(), state)
        self.assertEqual(generate_numbers(0), [])

    def test_generator_rejects_invalid_counts(self):
        for count in (True, 1.5, "10"):
            with self.subTest(count=count), self.assertRaises(TypeError):
                generate_numbers(count)
        with self.assertRaises(ValueError):
            generate_numbers(-1)

    def test_experiments_reject_invalid_repetitions(self):
        for repeats in (True, 1.5, "20"):
            with self.subTest(repeats=repeats), self.assertRaises(TypeError):
                run_case(250, 42, 8000, repeats=repeats)
        with self.assertRaises(ValueError):
            run_case(250, 42, 8000, repeats=0)

    def test_cli_output_and_all_experiments_match_saved_counts(self):
        # Run from a different working directory with an explicit output folder.
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "run results"
            demo = subprocess.run(
                [sys.executable, str(ROOT / "demo.py"), "--output-dir", str(output)],
                cwd=directory, capture_output=True, text=True, check=True)
            self.assertEqual((output / "demo.txt").read_text().strip(), demo.stdout.strip())
            numbers = [int(n) for n in (output / "numbers.txt").read_text().splitlines()]
            self.assertEqual(numbers, generate_numbers())
            self.assertIn("2654", demo.stdout)
            self.assertIn("2004", demo.stdout)
            self.assertIn("True (possibly present)", demo.stdout)
            self.assertIn("False (definitely absent)", demo.stdout)
            subprocess.run(
                [sys.executable, str(ROOT / "experiments.py"), "--output-dir", str(output)],
                cwd=directory, capture_output=True, text=True, check=True)
            with (output / "results.csv").open(newline="") as stream:
                rows = list(csv.DictReader(stream))
            with (ROOT / "results/results.csv").open(newline="") as stream:
                baseline = list(csv.DictReader(stream))
            key = lambda row: tuple(int(row[n]) for n in ("draws", "seed", "m"))
            expected = {(n, seed, m) for n in (250, 500, 1000)
                        for seed in (42, 43, 44) for m in (2000, 8000)}
            self.assertEqual(len(rows), 18)
            self.assertEqual({key(row) for row in rows}, expected)
            saved = {key(row): row for row in baseline}
            self.assertEqual(set(saved), expected)
            for row in rows:
                with self.subTest(configuration=key(row)):
                    self.assertEqual(int(row["false_negatives"]), 0)
                    self.assertEqual(int(row["k"]), 3)
                    self.assertEqual(int(row["queries_per_batch"]), 1001)
                    self.assertEqual(int(row["batch_repetitions"]), 20)
                    absent = int(row["absent_queries"])
                    self.assertEqual(absent + int(row["distinct_count"]), 1001)
                    self.assertAlmostEqual(float(row["false_positive_rate"]),
                                           int(row["false_positives"]) / absent)
                    for column in ("distinct_count", "absent_queries", "false_positives",
                                   "false_negatives", "false_positive_rate"):
                        self.assertEqual(row[column], saved[key(row)][column])
                    # Wall-clock timings vary and must not be compared for equality.
                    for column in ("build_seconds", "bloom_seconds_per_query",
                                   "list_seconds_per_query"):
                        value = float(row[column])
                        self.assertTrue(math.isfinite(value) and value >= 0)
