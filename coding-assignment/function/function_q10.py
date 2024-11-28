# Function to check if a number is Armstrong number
def is_armstrong(num):
    n = len(str(num))
    sum_of_digits = sum(int(digit) ** n for digit in str(num))
    return sum_of_digits == num

# Example usage
num = 153
print(f"The number {num} is an Armstrong number: {is_armstrong(num)}.")
