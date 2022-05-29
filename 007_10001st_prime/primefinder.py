'''Project Euler Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

import pentamath

target = int(input('How many primes would you like to find? '))

for i in range(target + 1):
    if unique_factors(i)
