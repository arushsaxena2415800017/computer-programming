# Function to find the sum of squares of a list of numbers
def sum_of_squares(lst):
    return sum(x ** 2 for x in lst)

# Example usage
lst = [1, 2, 3, 4]
print(f"The sum of squares is: {sum_of_squares(lst)}.")
