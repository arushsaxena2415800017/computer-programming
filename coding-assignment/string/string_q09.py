# Python program to check if a string has at least one letter and one number
def has_letter_and_number(s):
    return any(c.isalpha() for c in s) and any(c.isdigit() for c in s)

# Example usage
s = "abc123"
print("String has at least one letter and one number:", has_letter_and_number(s))
