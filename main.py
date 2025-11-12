n = int(input("Enter the number of terms in the Fibonacci sequence: "))
def fibonacci_sequence(n):
    sequence = []
    a, b = int(input("Enter the first term: ")), int(input("Enter the second term: "))
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci_sequence(n))