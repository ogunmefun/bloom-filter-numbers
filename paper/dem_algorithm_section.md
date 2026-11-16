Introduction and Bloom filter algorithm
Dem

# Design and Performance Analysis of a Bloom Filter Using Random Integer Data

**COSC 428/528 — Design and Analysis of Algorithms**  
**Bowie State University — Fall 2026**

---

## 1. Introduction

Many computer science applications require finding out if a given value exists in a huge amount of data; hence, efficient searching is an important topic. Linear search and other classical search algorithms look at each element separately until they find a match or the search is over. Although these techniques are user-friendly, their efficacy may diminish as the volume of data increases.

A Bloom filter is a type of probabilistic data structure that is designed to quickly test membership while using very little memory. Burton H. Bloom came up with the structure in 1970. It uses a bit array and several hash functions to check if an element might be part of a set. A Bloom filter, on the other hand, can give false positives, unlike an exact membership structure. But a normal Bloom filter doesn't give false negatives for elements that have been correctly inserted, as long as its bits haven't been changed in the wrong way.

Bloom filters can be used in database systems, caching, network security, and the first screening of known malicious indicators, among other things. The best thing about them is that you can check for membership without having to store each original element directly in the filter.

The project's goal is to create a Bloom filter in Python and study how it works with a set of 1,000 randomly generated numbers between 2,000 and 3,000. The program will put these integers into the Bloom filter and look for both a number that is already there and a number that is missing.

The project will also look at how long it takes to run, how much memory it needs, and how it handles false positives. The aim is to show how Bloom filters work and look at the compromise between quick membership testing and accurate probabilistic testing.

## 2. Algorithm

### 2.1 Overview of the Bloom Filter

A Bloom filter consists of an array containing \(m\) bits, initially set to zero, and \(k\) hash functions. Each hash function maps an input value to a position within the bit array.

When inserting an element, the algorithm calculates its hash positions and sets the corresponding bits to one. When searching for an element, it calculates the same positions and checks whether all corresponding bits are one.

If any required bit is zero, the element is definitely absent from the inserted set. If every required bit is one, the element is possibly present.

This distinction is important because different inserted elements may set overlapping positions, potentially producing false positives.

### 2.2 Generating the Dataset

The Python program generates 1,000 random integers between 2,000 and 3,000 using the `random` module.

```python
random.seed(42)
numbers = [random.randint(2000, 3000)
           for _ in range(1000)]
```

The random seed is fixed at 42 to make the generated dataset reproducible.

The dataset contains 1,000 entries, but some integers appear more than once. In the observed execution, the list contained 637 unique values.

### 2.3 Hash Functions

The implementation uses a bit array with 10,007 positions and three mathematical hash functions.

The functions are defined as follows:

\[
h_1(x)=x\bmod10007
\]

\[
h_2(x)=(31x+7)\bmod10007
\]

\[
h_3(x)=(131x+17)\bmod10007
\]

Here, \(x\) represents the integer being inserted or searched.

Each hash function produces an index between 0 and 10,006. These indices determine which positions are accessed in the Bloom filter.

The selected hash functions are simple and deterministic, making them suitable for demonstrating how the algorithm operates. However, they are not statistically independent, which may affect the observed false-positive probability.

### 2.4 Insertion Procedure

The insertion procedure calculates the three hash positions for an integer and sets each corresponding bit to one.

**Insertion pseudocode:**

```text
INSERT(x)
    FOR each position in HASH_POSITIONS(x)
        BIT_ARRAY[position] ← 1
    END FOR
```

This process is repeated for every integer in the generated list.

### 2.5 Search Procedure

The search procedure calculates the hash positions of the requested integer and examines the corresponding bits.

**Search pseudocode:**

```text
SEARCH(x)
    FOR each position in HASH_POSITIONS(x)
        IF BIT_ARRAY[position] = 0
            RETURN False
        END IF
    END FOR

    RETURN True
```

A return value of `False` means the integer is definitely absent. A return value of `True` means the integer may be present.

For the initial demonstration, the program searches for 2654, which is present in the generated list, and 2004, which is absent.

## 3. Analysis

### 3.1 Time Complexity

The time complexity of a Bloom filter depends primarily on the number of hash functions used.

Let:

- \(n\) represent the number of inserted elements.
- \(m\) represent the size of the bit array.
- \(k\) represent the number of hash functions.

For each insertion, the algorithm calculates \(k\) hash positions and updates the corresponding bits. Therefore, assuming constant-time hash calculations and bit-array accesses, the insertion complexity is:

\[
T_{\text{insert}}=O(k)
\]

Inserting \(n\) elements requires:

\[
T_{\text{build}}=O(nk)
\]

Similarly, a membership search examines at most \(k\) bit positions:

\[
T_{\text{search}}=O(k)
\]

For this project, the number of hash functions is fixed at three. Therefore, each insertion and search requires a constant maximum number of hash-position checks.

The Python implementation may terminate a search early when a zero bit is encountered. Consequently, an absent-number lookup may require fewer checks than a lookup that examines all three positions.

### 3.2 Space Complexity

The theoretical space complexity of a Bloom filter is determined by the size of its bit array:

\[
S(m)=O(m)\text{ bits}
\]

Our implementation uses:

\[
m=10007
\]

Therefore, an ideal packed bit array would require:

\[
\frac{10007}{8}=1250.875\text{ bytes}
\]

This is approximately 1,251 bytes, or 1.22 KiB, after rounding up to whole bytes.

However, the Python implementation uses a list of integer objects rather than a packed bit array. Its actual memory consumption is therefore substantially higher than the theoretical packed-bit requirement.

The generated list of 1,000 integers and the reference set used for testing also require additional memory.

### 3.3 False-Positive Probability

A Bloom filter may produce a false positive when an element that was never inserted happens to map to bit positions that have already been set to one.

Under the standard approximation that hash positions are uniformly distributed and sufficiently independent, the probability of a false positive is:

\[
P_{FP}\approx\left(1-e^{-kn/m}\right)^k
\]

The variables represent:

- \(n\): number of inserted elements
- \(m\): number of bits in the filter
- \(k\): number of hash functions

The approximate optimal number of hash functions is:

\[
k_{\text{optimal}}\approx\frac{m}{n}\ln2
\]

For our experiment, the actual number of distinct inserted integers is 637. Because inserting a duplicate does not introduce any new hash positions, the number of unique values is more relevant than the number of generated entries when estimating occupancy.

Nevertheless, the theoretical false-positive formula is only an approximation. Our implementation uses simple, related hash functions and a restricted integer range, so the independence and uniformity assumptions do not hold exactly.

Therefore, the experimentally measured false-positive rate is more informative for evaluating this particular implementation.

### 3.4 Advantages and Limitations

The Bloom filter provides efficient membership checks and allows the size of the underlying bit array to be configured.

It also has several limitations. A positive result does not guarantee that the searched value was inserted. Additionally, a standard Bloom filter cannot remove individual elements safely without modifications such as counting Bloom filters.

In this experiment, the hash functions are intentionally simple, and the dataset covers a narrow range of integers. These design choices make the algorithm easier to understand but limit how broadly the observed results can be generalized.

## 4. Test

### 4.1 Experimental Setup

The Bloom filter was implemented in Python and executed using Visual Studio Code.

The program generated 1,000 random integers within the inclusive range of 2,000 to 3,000. A fixed random seed of 42 ensured that the same dataset could be reproduced during subsequent executions.

The filter was configured with 10,007 positions and three hash functions.

To evaluate membership checking, the program selected one integer known to be present and one integer known to be absent. It then measured lookup execution time using Python's `time.perf_counter()` function.

Each selected lookup was repeated 100,000 times, and the total elapsed time was divided by the number of repetitions to estimate the average lookup duration.

Finally, the program tested every integer within the allowed range that did not appear in the generated dataset. This provided an observed false-positive count and rate.

### 4.2 Membership Search Results

| Measurement | Result |
|---|---|
| Total generated integers | 1,000 |
| Unique integers | 637 |
| Integer range | 2,000–3,000 |
| Bloom filter size | 10,007 positions |
| Number of hash functions | 3 |
| Present integer | 2654 |
| Present search result | True |
| Absent integer | 2004 |
| Absent search result | False |

The first search returned `True` for 2654, correctly reporting possible membership for a value known to exist in the generated list.

The second search returned `False` for 2004, correctly establishing that this integer was not part of the inserted set.

### 4.3 Execution-Time Results

The observed average lookup times from the latest recorded execution were:

| Search type | Average time |
|---|---:|
| Present number (2654) | 0.563 microseconds |
| Absent number (2004) | 0.782 microseconds |

These measurements indicate that both lookups completed in less than one microsecond on average in the recorded run.

The absent-number lookup was slower in this particular measurement. However, this does not establish that absent searches are generally slower. The results may vary because of Python execution overhead, operating-system scheduling, and the small duration of individual operations.

Additional independent timing trials would be needed to make stronger performance comparisons.

### 4.4 False-Positive Results

The program identified 364 integers between 2,000 and 3,000 that were absent from the generated dataset.

Each of these absent integers was tested against the Bloom filter.

| Measurement | Result |
|---|---:|
| Absent integers tested | 364 |
| False positives | 2 |
| True negatives | 362 |
| Observed false-positive rate | 0.55% |

The observed false-positive rate was calculated as:

\[
\text{False-positive rate}
=\frac{\text{False positives}}{\text{Absent values tested}}\times100
\]

\[
=\frac{2}{364}\times100
\]

\[
\boxed{0.55\%}
\]

This result demonstrates that the Bloom filter can incorrectly identify an absent integer as possibly present.

The program did not identify any false negatives in its present-value demonstration, consistent with the expected behavior of a correctly implemented standard Bloom filter.

### 4.5 Discussion of Results

The experiment successfully demonstrated the fundamental behavior of a Bloom filter.

The program generated the requested dataset, inserted its values into the filter, and performed membership searches for both present and absent integers.

The two false positives illustrate the primary tradeoff of probabilistic membership testing: the filter can use a compact representation of a set, but a positive response may require verification using an exact data structure.

The results also demonstrate the importance of hash-function selection. Although the current implementation uses a 10,007-position array, its simple hash functions do not provide uniformly independent mappings. Consequently, the observed false-positive rate should not be treated as a general performance guarantee for Bloom filters.

Overall, the experiment provides a working demonstration of Bloom filter insertion, searching, execution-time measurement, and false-positive analysis.

## 5. References

[1] B. H. Bloom, “Space/Time Trade-offs in Hash Coding with Allowable Errors,” *Communications of the ACM*, vol. 13, no. 7, pp. 422–426, 1970. DOI: 10.1145/362686.362692.

[2] A. Broder and M. Mitzenmacher, “Network Applications of Bloom Filters: A Survey,” *Internet Mathematics*, vol. 1, no. 4, pp. 485–509, 2004. DOI: 10.1080/15427951.2004.10129096.

[3] Python Software Foundation, “random — Generate pseudo-random numbers,” *Python Documentation*. https://docs.python.org/3/library/random.html

[4] Python Software Foundation, “time — Time access and conversions,” *Python Documentation*. https://docs.python.org/3/library/time.html

## 6. Appendix (Code)

The following Python program implements the Bloom filter and produces the membership, timing, and false-positive results discussed in this paper.

```python
import time
import random

# Generate 1,000 numbers between 2000 and 3000.
random.seed(42)
numbers = [random.randint(2000, 3000) for _ in range(1000)]

# Bloom filter configuration
SIZE = 10007
bits = [0] * SIZE

# Three hash functions
def hash_positions(number):
    return [
        number % SIZE,
        (number * 31 + 7) % SIZE,
        (number * 131 + 17) % SIZE
    ]

# Insert a number into the Bloom filter
def insert(number):
    for position in hash_positions(number):
        bits[position] = 1

# Check whether a number might be present
def search(number):
    return all(
        bits[position] == 1
        for position in hash_positions(number)
    )

# Insert all generated numbers
for number in numbers:
    insert(number)

# Choose one present number
present = numbers[0]

# Choose one absent number
missing = sorted(
    set(range(2000, 3001)) - set(numbers)
)
absent = missing[0]

# Perform the searches
print("Total generated numbers:", len(numbers))
print("Unique numbers:", len(set(numbers)))

print("\nSearch for a present number:", present)
print("Bloom filter:", search(present))

print("\nSearch for an absent number:", absent)
print("Bloom filter:", search(absent))

if search(absent):
    print("False positive detected!")
else:
    print("Number correctly identified as absent.")

# Measure average lookup time
REPEATS = 100000

start = time.perf_counter()

for _ in range(REPEATS):
    search(present)

end = time.perf_counter()
average_present = (end - start) / REPEATS

start = time.perf_counter()

for _ in range(REPEATS):
    search(absent)

end = time.perf_counter()
average_absent = (end - start) / REPEATS

print("\n--- Performance Results ---")
print(f"Present lookup: {average_present:.9f} seconds")
print(f"Absent lookup:  {average_absent:.9f} seconds")

# Test all absent numbers for false positives
actual_numbers = set(numbers)

absent_numbers = [
    n for n in range(2000, 3001)
    if n not in actual_numbers
]

false_positives = sum(
    search(n) for n in absent_numbers
)

false_positive_rate = (
    false_positives / len(absent_numbers)
    if absent_numbers else 0
)

print("\n--- False Positive Analysis ---")
print("Absent numbers tested:", len(absent_numbers))
print("False positives:", false_positives)
print(f"False positive rate: {false_positive_rate:.2%}")
print("Note: other hash functions can set overlapping bit positions.")
```
