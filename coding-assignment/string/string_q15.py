# Python | Maximum frequency character in String
from collections import Counter

def max_frequency_char(s):
    counts = Counter(s)
    return max(counts, key=counts.get)

# Example usage
s = "programming"
print("Maximum frequency character:", max_frequency_char(s))
