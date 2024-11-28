# Python | Program to accept the strings which contains all vowels
def contains_all_vowels(s):
    vowels = set("aeiou")
    return vowels.issubset(s.lower())

# Example usage
s = "education"
print("Contains all vowels:", contains_all_vowels(s))
