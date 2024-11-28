# Python | Multiply all numbers in the list
from functools import reduce

lst = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, lst)
print("Product of all numbers in the list:", result)
