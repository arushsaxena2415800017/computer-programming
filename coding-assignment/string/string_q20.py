# Generating random strings until a given string is generated
import random
import string

def generate_random_string(target):
    while True:
        random_str = ''.join(random.choices(string.ascii_lowercase, k=len(target)))
        print("Generated string:", random_str)
        if random_str == target:
            return random_str

# Example usage
target = "hello"
generated = generate_random_string(target)
print(f"Target string '{target}' generated!")
