'''Project Euler Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

import pentamath

target = int(input('\nHow many primes would you like me to find? '))
primelist = []
i = 1

while len(primelist) <= target - 1:
    i += 1
    if len(pentamath.factors_all(i)) > 1:
        continue
    else:
        primelist.append(i)
        print(f'Prime #{len(primelist)}: {primelist[len(primelist) - 1]}')
