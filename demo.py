from pathlib import Path
import random

from bloom_filter import BloomFilter


def generate_numbers(count=1000, seed=42):
    """Generate random integers from 2000 through 3000, allowing duplicates."""
    rng = random.Random(seed)
    return [rng.randint(2000, 3000) for _ in range(count)]


def main():
    # Generate the numbers and keep the original list, including duplicates.
    numbers = generate_numbers()
    unique_numbers = set(numbers)

    # Create a fresh Bloom Filter and insert every generated number.
    bf = BloomFilter()
    for number in numbers:
        bf.add(number)

    # Choose one number known to be present.
    present = numbers[0]

    # Choose one number in the allowed range that was not generated.
    missing = sorted(set(range(2000, 3001)) - unique_numbers)
    if not missing:
        raise ValueError("No absent number is available in the range 2000–3000.")
    absent = missing[0]

    # Check exact membership and the Bloom Filter answer for both queries.
    present_exact = present in unique_numbers
    present_bloom = bf.contains(present)
    absent_exact = absent in unique_numbers
    absent_bloom = bf.contains(absent)

    def bloom_description(answer):
        if answer:
            return "possibly present"
        return "definitely absent"

    # Build the output once so it can be printed and saved to a file.
    output = [
        f"Total generated numbers: {len(numbers)}",
        f"Unique numbers: {len(unique_numbers)}",
        "",
        f"Search for a present number: {present}",
        f"Exact membership: {present_exact}",
        f"Bloom filter: {present_bloom} ({bloom_description(present_bloom)})",
        "",
        f"Search for an absent number: {absent}",
        f"Exact membership: {absent_exact}",
        f"Bloom filter: {absent_bloom} ({bloom_description(absent_bloom)})",
    ]

    if absent_bloom and not absent_exact:
        output.append("False positive detected!")
    else:
        output.append("No false positive for this absent-number query.")

    output_text = "\n".join(output)
    print(output_text)

    # Create the results folder if it does not already exist.
    results_folder = Path("results")
    results_folder.mkdir(parents=True, exist_ok=True)

    # Save all generated numbers, preserving duplicates and their order.
    numbers_file = results_folder / "numbers.txt"
    numbers_file.write_text(
        "\n".join(str(number) for number in numbers) + "\n",
        encoding="utf-8",
    )

    # Save the same demonstration output that was printed above.
    demo_file = results_folder / "demo.txt"
    demo_file.write_text(output_text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
