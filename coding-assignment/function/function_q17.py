# Function to generate multiplication table
def multiplication_table(num):
    return [num * i for i in range(1, 11)]

# Example usage
num = 7
print(f"Multiplication table for {num} is: {multiplication_table(num)}.")
