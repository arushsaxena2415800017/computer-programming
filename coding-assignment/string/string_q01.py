# Python program to check whether the string is Symmetrical or Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "madam"
print(f"Is the string '{s}' a palindrome? {is_palindrome(s)}")
