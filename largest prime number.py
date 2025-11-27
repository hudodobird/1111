primes = []
def prime_checker(n):
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes

number = int(input("Enter a number: "))
prime_numbers = prime_checker(number)
print(f"Prime numbers up to {number}: {prime_numbers}")
print(f"Total prime numbers found: {len(prime_numbers)}")
print(f"Largest prime number found: {prime_numbers[-1] if prime_numbers else 'None'}")