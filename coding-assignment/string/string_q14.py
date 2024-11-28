# Python – Least Frequent Character in String
from collections import Counter

def least_frequent_char(s):
    counts = Counter(s)
    return min(counts, key=counts.get)

# Example usage
s = "programming"
print("Least frequent character:", least_frequent_char(s))
