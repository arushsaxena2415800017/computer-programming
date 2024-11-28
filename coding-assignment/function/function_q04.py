# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Example usage
num = 11
print(f"The number {num} is prime: {is_prime(num)}.")
