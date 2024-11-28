# Python | Program to check if a string contains any special character
import re

def has_special_char(s):
    return bool(re.search(r'[^a-zA-Z0-9]', s))

# Example usage
s = "hello@world"
print("Contains special character:", has_special_char(s))
