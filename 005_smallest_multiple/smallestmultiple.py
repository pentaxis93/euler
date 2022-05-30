'''Project Euler Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import pentimath

top_number = int(input('What\'s your top number? '))

# Build list including all factors of all numbers in series
factors = []
for i in range(2, top_number + 1):
    i_factors = pentimath.factors_all(i)
    for factor in i_factors:
        if factor not in factors:
            factors.append(factor)
        else:
            while i_factors.count(factor) > factors.count(factor):
                factors.append(factor)

# Calculate smallest multiple
smallest_multiple = 1
for factor in factors:
    smallest_multiple *= factor

print('The smallest multiple is:', smallest_multiple)
