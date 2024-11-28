# Python | Sum of number digits in List
def sum_of_digits(lst):
    return sum(sum(int(digit) for digit in str(num)) for num in lst)

lst = [123, 456, 789]
print("Sum of digits in the list:", sum_of_digits(lst))
