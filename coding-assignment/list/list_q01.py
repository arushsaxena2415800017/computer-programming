# Python program to interchange first and last elements in a list
def interchange_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Example usage
lst = [10, 20, 30, 40, 50]
print("Original List:", lst)
print("List after interchange:", interchange_first_last(lst))
