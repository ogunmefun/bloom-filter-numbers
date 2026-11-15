Introduction and Bloom filter algorithm
Dem

Introduction

Our project studies number membership using a Bloom filter. We generate 1,000 random integers from 2,000 through 3,000, insert them into the filter, and query numbers whose actual membership is known. The range contains 1,001 possible integers, and repeated draws are allowed. Therefore, the number of distinct inserted values can be smaller than the number of draws. We retain the original list to verify answers, while the filter stores a summary of membership.

The purpose is to demonstrate a probabilistic search structure and examine its tradeoff between lookup work, storage, and false positives. Bloom's original paper describes accepting a limited number of membership errors to reduce storage requirements [1]. In our application, a negative answer means definitely absent, while a positive answer means possibly present. The filter cannot return a number's list index or count its occurrences. An exact membership check remains necessary whenever an application must confirm a positive result.

Representation and hashing

Our Python module provides BloomFilter(m=8000, k=3), add(number), and contains(number). The parameter m is the number of logical bit positions, and k is the number of hash calculations per integer. Every new filter starts with zero in every position. Independent instances allow separate experiments without carrying membership information from an earlier run.

For readability, the implementation uses a bytearray with one byte per logical bit. Each entry holds either zero or one. This is not a packed bit array: the default buffer contains 8,000 bytes, rather than the 1,000 bytes needed to pack 8,000 bits. Python object overhead adds further storage. This implementation choice makes the algorithm easy to inspect, but it prevents us from claiming the full memory savings of a packed representation.

For each integer x, the implementation forms the ASCII strings "0:x", "1:x", and "2:x" under the default configuration. It hashes each string with SHA-256, interprets the digest as a nonnegative integer, and takes the remainder modulo m. Python's hashlib module supplies SHA-256 and its digest interface [2]. The different prefixes act as salts that produce repeatable hash mappings. They are not secret passwords or encryption keys. Insertions and queries use exactly the same mapping. Different integers can map to the same position after the modulo operation, even without a collision between their complete SHA-256 digests.

Insertion and membership queries

To insert an integer, add computes its k positions and sets each corresponding entry to one. It never clears an entry. Inserting the same integer again sets the same entries, so duplicate insertion does not change the filter. To query an integer, contains computes its positions and checks their entries. A zero at any required position produces False. If every required entry is one, the method produces True.

Pseudocode

POSITIONS(x):
    For each salt i from 0 to k - 1:
        Compute SHA256 of the ASCII text i + ":" + x
        Interpret the digest as an integer and reduce modulo m
    Return the resulting positions

ADD(x):
    For each position p in POSITIONS(x):
        B[p] = 1

CONTAINS(x):
    For each position p in POSITIONS(x):
        If B[p] is zero, return False
    Return True

Worked example and possible errors

Consider an illustrative filter with ten positions numbered zero through nine. These example positions explain the algorithm; they are not measured SHA-256 outputs. Suppose 2000 maps to positions 1, 4, and 7, while 2500 maps to positions 2, 4, and 8. Inserting both sets positions 1, 2, 4, 7, and 8. Querying 2000 checks three entries that are all one, so the answer is possibly present. If an absent number maps to 0, 4, and 8, the zero at position 0 makes the answer definitely absent. However, another absent number could map to 1, 2, and 8. All three entries are already one, so that query produces a false positive.

A correctly implemented insertion-only filter has no false negatives because insertion sets every position that a later query will check, and subsequent insertions never reset those positions. This guarantee assumes unchanged hashing and configuration and uncorrupted storage. Simply clearing positions to delete a number would break the guarantee because other numbers can share those positions. Our implementation therefore offers no deletion operation.

Complexity and practical limits

For the fixed-size integers in this project, each hash calculation and array access can be treated as constant-cost work. Insertion and lookup take O(k) time. With k fixed at three, each operation is O(1) relative to the number of inserted items. Inserting N draws takes O(Nk), while initializing the array takes O(m), giving O(m + Nk) for initialization plus construction. Our hash_positions method builds a tuple of k positions, using O(k) temporary space and computing every hash before the membership checks begin.

An ideal representation requires m bits. Our bytearray uses O(m) bytes, plus object overhead; this distinction matters when discussing actual memory use. A list membership query can examine O(N) elements, but asymptotic complexity does not establish which implementation is faster for 1,000 numbers. SHA-256 and Python call overhead may outweigh the saved comparisons. Measurements must determine the observed timing. False-positive rate must be calculated using known-absent queries as the denominator. A single correct absent query, or even zero false positives in a finite test, does not establish that false positives are impossible.

References

[1] Burton H. Bloom. 1970. Space/time trade-offs in hash coding with allowable errors. Communications of the ACM 13(7), 422–426. https://doi.org/10.1145/362686.362692

[2] Python Software Foundation. hashlib — Secure hashes and message digests. https://docs.python.org/3/library/hashlib.html
