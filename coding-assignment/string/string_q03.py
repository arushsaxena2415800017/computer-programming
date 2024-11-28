# Ways to remove i’th character from string in Python
def remove_ith_char(s, i):
    return s[:i] + s[i+1:]

# Example usage
s = "hello"
i = 1
print("String after removing character:", remove_ith_char(s, i))
