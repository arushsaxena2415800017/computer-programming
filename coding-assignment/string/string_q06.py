# Python program to print even length words in a string
def even_length_words(s):
    return [word for word in s.split() if len(word) % 2 == 0]

# Example usage
s = "I love programming in Python"
print("Even length words:", even_length_words(s))
