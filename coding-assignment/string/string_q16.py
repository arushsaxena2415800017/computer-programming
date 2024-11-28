# Python – Odd Frequency Characters
from collections import Counter

def odd_frequency_chars(s):
    counts = Counter(s)
    return [char for char, count in counts.items() if count % 2 != 0]

# Example usage
s = "programming"
print("Odd frequency characters:", odd_frequency_chars(s))
