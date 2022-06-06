"""This module provides functional implementations of a few Project
Euler problems.
"""

import trickymath

# Problem 1: Multiples of 3 or 5
def multipladd(x = 3, y = 5, z = 1000):
    """Return the sum of all natural numbers below z that are multiples
    of x or y.
    """
    som = trickymath.sum_of_multiples()
    return som(x, z) + som(y, z) - som(x * y, z)

# Problem 2: Even Fibonacci numbers
def evenfibs(x = 4000000):
    """Return the sum of all the even Fibonacci numbers below x."""
    total = 0
    a = 1
    b = 1
    c = a + b
    while c <= x:
        total += c
        a = b + c
        b = c + a
        c = a + b
    return total

# Problem 3: Sum Square Difference
def sumsquarediff(x):
    '''Perform a single step in factoring a number.

    Finds the smallest factor of the number, divides the number by the factor, and returns the reduced number for further factoring.'''
    for i in range(2, number):
        if number % i == 0:
            print(i, 'is a factor.')
            number = int(number / i)
            return number
    return number

while True:
    reduced = factor(target)
    if target == reduced:
        break
    target = reduced

print('The largest factor is', target)
