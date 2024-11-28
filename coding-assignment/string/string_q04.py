# Find length of a string in python (4 ways)
s = "Hello, world!"

# Method 1: Using len()
print("Length using len():", len(s))

# Method 2: Using a for loop
count = 0
for _ in s:
    count += 1
print("Length using for loop:", count)

# Method 3: Using list comprehension
print("Length using list comprehension:", sum(1 for _ in s))

# Method 4: Using reduce
from functools import reduce
print("Length using reduce:", reduce(lambda count, _: count + 1, s, 0))
