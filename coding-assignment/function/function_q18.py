# Function to check if two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
s1 = "listen"
s2 = "silent"
print(f"'{s1}' and '{s2}' are anagrams: {is_anagram(s1, s2)}.")
