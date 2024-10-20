# prime_numbers.py

# Function to check if a number is prime
def is_prime(num):
    # Return False if number is less than or equal to 1
    if num <= 1:
        return False
    # Check divisibility for numbers from 2 up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    # Return True if no divisors are found, meaning the number is prime
    return True

# List to hold prime numbers
prime_numbers = []

# Loop through numbers from 1 to 250
for num in range(1, 251):
    if is_prime(num):
        prime_numbers.append(num)

# Save the prime numbers to a file
with open("results.txt", "w") as file:
    for prime in prime_numbers:
        file.write(f"{prime}\n")

# Notify the user that the results have been saved
print("Prime numbers between 1 and 250 have been saved to results.txt")
