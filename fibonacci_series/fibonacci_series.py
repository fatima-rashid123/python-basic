# Fibonacci sequence program

# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Ask user how many terms they want
num = int(input("Enter the number of terms: "))

# Display the sequence
print("Fibonacci sequence:")
print(fibonacci(num))
