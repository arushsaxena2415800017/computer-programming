# Python – Uppercase Half String
def uppercase_half(s):
    mid = len(s) // 2
    return s[:mid].lower() + s[mid:].upper()

# Example usage
s = "hello world"
print("Uppercase half string:", uppercase_half(s))
