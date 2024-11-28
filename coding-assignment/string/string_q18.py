# Python | Frequency of numbers in String
def number_frequency(s):
    return {char: s.count(char) for char in s if char.isdigit()}

# Example usage
s = "abc123123"
print("Frequency of numbers:", number_frequency(s))
