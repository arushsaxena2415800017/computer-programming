# Python program to print all even numbers in a range
start = 1
end = 20
even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
print("Even numbers in range from", start, "to", end, ":", even_numbers)
