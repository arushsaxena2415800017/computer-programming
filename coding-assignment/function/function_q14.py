# Function to find the Fibonacci sequence up to nth term
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Example usage
n = 10
print(f"The Fibonacci sequence up to {n}th term is: {fibonacci(n)}.")
