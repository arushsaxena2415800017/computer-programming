# Python – Swap elements in String list
def swap_elements(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]
    return lst

# Example usage
lst = ["apple", "banana", "cherry", "date"]
print("Original List:", lst)
print("List after swap:", swap_elements(lst, 0, 2))
