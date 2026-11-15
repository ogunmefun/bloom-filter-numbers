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
    return all(bits[position] == 1
               for position in hash_positions(number))

# Insert all generated numbers
for number in numbers:
    insert(number)

# Choose one present number
present = numbers[0]

# Choose one absent number
missing = sorted(set(range(2000, 3001)) - set(numbers))
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

# Measure average lookup time over repeated searches
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


# Check all absent numbers in the allowed range for false positives
actual_numbers = set(numbers)
absent_numbers = [n for n in range(2000, 3001) if n not in actual_numbers]
false_positives = sum(search(n) for n in absent_numbers)
false_positive_rate = false_positives / len(absent_numbers) if absent_numbers else 0

print("\n--- False Positive Analysis ---")
print("Absent numbers tested:", len(absent_numbers))
print("False positives:", false_positives)
print(f"False positive rate: {false_positive_rate:.2%}")
print("Note: other hash functions can set overlapping bit positions.")
