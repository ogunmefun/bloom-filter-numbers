import random
from bloom_filter import insert, search

# Generate 1,000 random numbers
random.seed(42)
numbers = [random.randint(2000, 3000) for _ in range(1000)]

# Create a set of unique numbers
unique_numbers = set(numbers)

# Insert all numbers into the Bloom Filter
for number in numbers:
    insert(number)

# Choose one number that exists
present = numbers[0]

# Choose one number that does not exist
missing = sorted(set(range(2000, 3001)) - unique_numbers)
absent = missing[0]

# Display the results
print("Total generated numbers:", len(numbers))
print("Unique numbers:", len(unique_numbers))

print("\nSearch for a present number:", present)
print("Bloom filter:", search(present))

print("\nSearch for an absent number:", absent)
print("Bloom filter:", search(absent))

if search(absent):
    print("False positive detected!")
else:
    print("Number correctly identified as absent.")
