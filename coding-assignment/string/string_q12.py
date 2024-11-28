# Python program to count number of vowels using sets in given string
def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(1 for c in s if c in vowels)

# Example usage
s = "hello world"
print("Number of vowels:", count_vowels(s))
