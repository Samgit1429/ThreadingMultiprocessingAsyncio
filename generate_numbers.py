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

#Generate a list of 10000 large numbers with a minimum of 10 digits and a maximum of 20 digits
numbers = generate_large_numbers(10000, 10, 20)

#Print each number on separate line
with open("large_numbers.txt", "w") as file:  
    for number in numbers:
        file.write(number + "\n")

print("Numbers saved to large_numbers.txt")