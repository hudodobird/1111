primes = [num for num in range(2, 101) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]
print(f"Prime numbers up to 100: {primes}")
print(f"Total prime numbers found: {len(primes)}")
print(f"Largest prime number found: {primes[-1] if primes else 'None'}")