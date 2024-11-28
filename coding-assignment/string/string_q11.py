# Python | Count the Number of matching characters in a pair of string
def matching_characters(str1, str2):
    return sum(1 for a, b in zip(str1, str2) if a == b)

# Example usage
str1 = "hello"
str2 = "hxllo"
print("Number of matching characters:", matching_characters(str1, str2))
