# Function to find the factorial of a number using iteration
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 5
print(f"The factorial of {num} is {factorial_iterative(num)}.")
