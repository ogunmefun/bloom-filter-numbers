import contextlib
import importlib
import io
import random
import unittest
from unittest.mock import patch

import experiments


class ExperimentTests(unittest.TestCase):
    def test_saturated_filter_counts_only_absent_queries(self):
        row = experiments.run_case(250, 42, m=1, repeats=1)
        self.assertEqual(row['false_negatives'], 0)
        self.assertEqual(row['absent_queries'], 1001 - row['distinct_count'])
        self.assertEqual(row['false_positives'], row['absent_queries'])
        self.assertEqual(row['false_positive_rate'], 1)

    def test_no_absent_queries_has_undefined_rate(self):
        with patch('experiments.generate_numbers', return_value=list(range(2000, 3001))):
            row = experiments.run_case(1001, 42, m=8000, repeats=1)
        self.assertEqual(row['absent_queries'], 0)
        self.assertIsNone(row['false_positive_rate'])

    def test_import_is_silent_and_preserves_rng(self):
        output = io.StringIO()
        before = random.getstate()
        with contextlib.redirect_stdout(output):
            importlib.reload(experiments)
        self.assertEqual(output.getvalue(), '')
        self.assertEqual(random.getstate(), before)
