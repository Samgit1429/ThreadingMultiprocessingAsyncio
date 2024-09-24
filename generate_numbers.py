import random

def generate_large_numbers(num_numbers, min_digits, max_digits):
    """
    Generates a list of large numbers.
    
    Args:
        num_numbers: The number of numbers to generate.
        min_digits: The minimum number of digits for each number.
        max_digits: The maximum number of digits for each number.

    Returns:
        A list of large numbers.
    """
    numbers = []
    for _ in range(num_numbers):
        num_digits = random.randint(min_digits, max_digits)
        number = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
        numbers.append(number)
    return numbers

def generate_numbers_file(filename, num_numbers, min_digits, max_digits):
    """
    Generates a list of large numbers and writes them to a file.
    
    Args:
        filename: The name of the file to write to.
        num_numbers: The number of numbers to generate.
        min_digits: The minimum number of digits for each number.
        max_digits: The maximum number of digits for each number.
    """
    numbers = generate_large_numbers(num_numbers, min_digits, max_digits)
    
    # Write each number to the file on a separate line
    with open(filename, "w") as file:
        for number in numbers:
            file.write(number + "\n")
    
    print(f"Numbers saved to {filename}")

# Example usage (optional, for testing the script directly)
if __name__ == "__main__":
    generate_numbers_file("large_numbers.txt", 10000, 10, 20)
