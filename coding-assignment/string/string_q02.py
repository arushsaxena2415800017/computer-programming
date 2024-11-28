# Reverse words in a given String in Python
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# Example usage
s = "Python is awesome"
print("Reversed words:", reverse_words(s))
