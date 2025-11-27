import time as t

# start = t.time()

# my_gen = (num for num in range(2, 1000000) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
# largestprime = -1
# for val in my_gen:
#     if val > largestprime:
#         largestprime = val
    
# end = t.time()

# elapsed = end - start

# print(largestprime)
# print(elapsed)

primes = []
def prime_checker(n):
    start = t.time()
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    end = t.time()
    elapsed = end - start
    return primes, elapsed

number = int(input("Enter a number: "))
prime_numbers, elapsed = prime_checker(number)
print(elapsed)