"""This module provides a variety of tricky math functions which may be
useful for exploring Project Euler problems."""

def factor_all(x):
    """Return a list of all the prime factors of x, including
    duplicates.
    """
    factors = []
    reduced = x
    while True:
        for i in range(2, x):
            if x % i == 0:
                factors.append(i)
                reduced = int(x / i)
                break
        if x == reduced:
            factors.append(x)
            break
        else:
            x = reduced
    return factors

def factor_unique(x):
    """Return a list of all the unique prime factors of x."""
    factors = []
    reduced = x
    while True:
        for i in range(2, x):
            if x % i == 0:
                if i not in factors:
                    factors.append(i)
                reduced = int(x / i)
                break
        if x == reduced:
            break
        else:
            x = reduced
    if x not in factors:
        factors.append(x)
    return factors

def smallest_factor(x): """Return the smallest factor of x"""
    for i in range(2, number + 1):
        if number % i == 0:
            return number

def ispalindrome(input):
    """Return True if input is palindromic, and False otherwise."""
    if str(input)[:] == str(input)[::-1]:
        return True
    else:
        return False

def isprime(x):
    """Return True if x is prime, and False otherwise."""
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
    return True

def sum_of_multiples(n, limit):
    """Return the sum of the multiples of x below the limit."""
    top = (limit - 1) // n
    return n * (top * (top + 1) // 2)

def sum_of_n(n):
    """Return the sum of the first n natural numbers."""
    return n * (n + 1) // 2

def sum_of_n2(n):
    """Return the sum of the squares of the first n natural numbers."""
    return n * (n + 1) * ((2 * n) + 1) // 6

def sum_of_n3(n):
    """Return the sum of the cubes of the first n natural numbers."""
    return (n ** 2) * ((n + 1) ** 2) // 4
