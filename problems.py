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
    """Return the difference between sum of squares and square of sum of the
    first n natural numbers.
    """
    square_of_sum = trickymath.sum_of_n(n) ** 2
    sum_of_squares = trickymath.sum_of_n2(n)
    diff = square_of_sum - sum_of_squares
    return diff

# Problem 5: Smallest Multiple
def smallmult(x = 20):
    """Return the smallest positive number that is evenly divisible by all of
    the numbers from 1 to x.
    """
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
    """Return the largest prime factor of x."""
    factors = trickymath.factor_unique(x)
    factors.sort()
    return factors[-1]

# Problem 4: Largest Palindrome Product
def largestpalinprod():
    """Return the largest palindrome made from the product of two
    3-digit numbers."""
    largest_palindrome = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            candidate = x * y
            if trickymath.ispalindrome(candidate):
                if candidate > largest_palindrome:
                    largest_palindrome = candidate
    return largest_palindrome

# Problem 7: 10001st Prime
def nthprime(n = 10001):
    """Return the nth prime number."""
    primelist = [2]
    i = 3
    while len(primelist) < n:
        if i % 2 > 0:
            if trickymath.isprime(i):
                primelist.append(i)
        i += 1
    return primelist[-1]

# Problem 9: Special Pythagorean Triplet
def specpythtrip():
    """Return the product abc for the single Pythagorean triplet for which
    a + b + c = 1000.
    """
    for a in range(1, 999):
        for b in range(1, 1000 - a):
            c = 1000 - a - b
            if (a ** 2) + (b ** 2) == c ** 2:
                return a * b * c

# Problem 8: Largest Product in a Series
def seriesprod(x = 13):
    """Return the value of the product of the x adjacent digits in the given
    1000-digit number that have the greatest product.
    """
    longnum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    greatestprod = 1
    for i in range(1000 - x):
        slice = longnum[i:i + x]
        prod = 1
        for j in range(x):
            prod *= int(slice[j])
        if prod > greatestprod:
            greatestprod = prod
    return greatestprod
