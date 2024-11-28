# Function to count occurrences of a character in a string
def count_char(s, char):
    return s.count(char)

# Example usage
s = "hello world"
char = "o"
print(f"The character '{char}' appears {count_char(s, char)} times in '{s}'.")
