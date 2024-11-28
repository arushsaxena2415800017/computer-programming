# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
a, b = 60, 48
print(f"The GCD of {a} and {b} is {gcd(a, b)}.")
