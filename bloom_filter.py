"""Insertion-only integer Bloom filter. True means possibly present."""
from hashlib import sha256


class BloomFilter:
    """Use one byte per logical bit for readability, not packed storage."""

    def __init__(self, m=8000, k=3):
        for name, value in (("m", m), ("k", k)):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be positive")
        self._m, self._k = m, k
        self._bits = bytearray(m)

    @property
    def m(self):
        return self._m

    @property
    def k(self):
        return self._k

    def hash_positions(self, number):
        """The same integer and configuration always give the same positions."""
        if type(number) is not int:
            raise TypeError("number must be an integer")
        return tuple(
            int.from_bytes(sha256(f"{salt}:{number}".encode("ascii")).digest(), "big") % self.m
            for salt in range(self.k)
        )

    def add(self, number):
        """Set positions to one; repeated insertion is harmless."""
        for position in self.hash_positions(number):
            self._bits[position] = 1

    def contains(self, number):
        """True: possibly present. False: definitely absent."""
        return all(self._bits[p] for p in self.hash_positions(number))


# Backward compatibility for Renee's existing demo. No data is inserted and
# nothing is printed on import. Use separate instances for experiments.
_default_filter = BloomFilter()


def insert(number):
    _default_filter.add(number)


def search(number):
    return _default_filter.contains(number)


def hash_positions(number):
    return _default_filter.hash_positions(number)

