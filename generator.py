my_gen = (num for num in range(2, 1000) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)))
largestprime = -1
for val in my_gen:
    if val > largestprime:
        largestprime = val
    

print(largestprime)