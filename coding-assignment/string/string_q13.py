# Python Program to remove all duplicates from a given string
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# Example usage
s = "programming"
print("String without duplicates:", remove_duplicates(s))
