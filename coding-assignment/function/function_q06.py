# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Example usage
s = "madam"
print(f"The string '{s}' is a palindrome: {is_palindrome(s)}.")
