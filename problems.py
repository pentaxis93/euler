"""This module provides functional implementations of a few Project
Euler problems.

The problems are listed in order of difficulty, not by problem number.
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

# Problem 6: Sum Square Difference
def sumsquarediff(n = 100):
    square_of_sum = trickymath.sum_of_n(n) ** 2
    sum_of_squares = trickymath.sum_of_n2(n)
    diff = square_of_sum - sum_of_squares
    return diff

# Problem 5: Smallest Multiple
def smallmult(x = 20):
    factors = []
    for i in range(2, x + 1):
        i_factors = trickymath.factor_all(i)
        for factor in i_factors:
            if factor not in factors:
                factors.append(factor)
            else:
                while i_factors.count(factor) > factors.count(factor):
                    factors.append(factor)
    smallest_multiple = 1
    for factor in factors:
        smallest_multiple *= factor
    return smallest_multiple

# Problem 3: Largest Prime Factor
def largestpfactor(x = 600851475143):
    factors = trickymath.factor_unique(x)
    factors.sort()
    return factors[-1]
