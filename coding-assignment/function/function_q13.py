# Function to check if a number is a perfect number
def is_perfect_number(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Example usage
num = 28
print(f"The number {num} is a perfect number: {is_perfect_number(num)}.")
