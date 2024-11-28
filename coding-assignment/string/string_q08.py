# Python program to capitalize the first and last character of each word in a string
def capitalize_first_last(s):
    words = s.split()
    return ' '.join([word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper() for word in words])

# Example usage
s = "hello python world"
print("Capitalized first and last characters:", capitalize_first_last(s))
