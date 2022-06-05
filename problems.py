"""This module provides functional implementations of a few Project
Euler problems.
"""

import trickymath

# Problem 1: Multiples of 3 or 5
def multipladd(x = 3, y = 5, z = 1000):
    """Return the sum of all natural numbers below z that are multiples
    of x or y.
    """
    return trickymath.sum_of_multiples(x, z) + trickymath.sum_of_multiples(y, z) - trickymath.sum_of_multiples(x * y, z)

# Problem 2: Even Fibonacci numbers
def evenfibs(x = 4000000):
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
