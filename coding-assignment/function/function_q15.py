# Function to find the LCM of two numbers
def lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

# Example usage
a, b = 4, 6
print(f"The LCM of {a} and {b} is {lcm(a, b)}.")
