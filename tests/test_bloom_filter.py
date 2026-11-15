import contextlib
import importlib
import io
import random
import unittest
import bloom_filter
from bloom_filter import BloomFilter


class BloomFilterTests(unittest.TestCase):
    def test_empty_filter(self):
        bf = BloomFilter()
        self.assertTrue(all(not bf.contains(n) for n in range(2000, 3001)))

    def test_no_false_negatives(self):
        for seed in (42, 43, 44):
            for count in (250, 500, 1000):
                rng = random.Random(seed)
                numbers = [rng.randint(2000, 3000) for _ in range(count)]
                for m in (2000, 8000):
                    with self.subTest(seed=seed, count=count, m=m):
                        bf = BloomFilter(m=m)
                        for n in numbers:
                            bf.add(n)
                        self.assertTrue(all(bf.contains(n) for n in set(numbers)))

    def test_duplicates(self):
        bf = BloomFilter()
        bf.add(2500)
        before = [bf.contains(n) for n in range(2000, 3001)]
        for _ in range(1000):
            bf.add(2500)
        self.assertEqual(before, [bf.contains(n) for n in range(2000, 3001)])

    def test_independent_instances(self):
        a, b = BloomFilter(), BloomFilter()
        a.add(2000)
        self.assertTrue(a.contains(2000))
        self.assertFalse(b.contains(2000))

    def test_repeatable_valid_positions(self):
        for m, k in ((1, 1), (7, 5), (8000, 3)):
            a, b = BloomFilter(m, k), BloomFilter(m, k)
            for n in (-1, 0, 2000, 3000):
                positions = a.hash_positions(n)
                self.assertEqual(positions, b.hash_positions(n))
                self.assertEqual(len(positions), k)
                self.assertTrue(all(0 <= p < m for p in positions))

    def test_false_positive_is_possible(self):
        bf = BloomFilter(m=1, k=3)
        bf.add(2000)
        self.assertTrue(bf.contains(3000))  # Never inserted, but every bit is set.

    def test_invalid_configuration(self):
        for kwargs in ({'m': 0}, {'k': -1}):
            with self.assertRaises(ValueError):
                BloomFilter(**kwargs)
        for kwargs in ({'m': True}, {'k': 1.5}):
            with self.assertRaises(TypeError):
                BloomFilter(**kwargs)

    def test_invalid_numbers(self):
        for value in (True, '2500', 2500.0, None):
            for method in (BloomFilter().add, BloomFilter().contains):
                with self.assertRaises(TypeError):
                    method(value)

    def test_silent_empty_import_and_legacy_api(self):
        output = io.StringIO()
        state = random.getstate()
        with contextlib.redirect_stdout(output):
            importlib.reload(bloom_filter)
        self.assertEqual(output.getvalue(), '')
        self.assertEqual(random.getstate(), state)
        self.assertFalse(bloom_filter.search(2500))
        bloom_filter.insert(2500)
        self.assertTrue(bloom_filter.search(2500))


if __name__ == '__main__':
    unittest.main()

