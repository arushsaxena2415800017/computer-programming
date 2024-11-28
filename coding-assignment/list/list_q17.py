# Python program to find second largest number in a list
lst = [10, 20, 30, 5, 50]
lst_sorted = sorted(lst, reverse=True)
print("Second largest number in the list:", lst_sorted[1])
