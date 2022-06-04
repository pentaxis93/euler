'''Project Euler Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

import pentamath

target = 10001
primelist = [2]
i = 3

while len(primelist) < target:
    if i % 2 > 0:
        if pentamath.isprime(i):
            primelist.append(i)
    i += 1

print('The {}st prime number is {}.'.format(len(primelist), primelist[len(primelist) - 1]))
