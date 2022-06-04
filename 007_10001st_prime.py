'''Project Euler Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

import pentamath

target = 10001
primelist = [2]
i = 2

while len(primelist) <= target - 1:
    i += 1
    if i % 2 > 0:
        if len(pentamath.factors_all(i)) > 1:
            continue
        else:
            primelist.append(i)

print('The {len(primelist)}st prime number is {primelist[len(primelist) - 1]}.')
