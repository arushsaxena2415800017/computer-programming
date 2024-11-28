# Python program to swap two elements in a list
def swap_elements(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

# Example usage
lst = [10, 20, 30, 40, 50]
print("Original List:", lst)
print("List after swap:", swap_elements(lst, 1, 3))
