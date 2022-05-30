'''Project Euler Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

import pentamath

largest_palindrome = 0

for x in range(100, 1000):
    for y in range(100, 1000):
        candidate = x * y
        if pentamath.ispalindrome(candidate):
            if candidate > largest_palindrome:
                largest_palindrome = candidate
                spam = x
                eggs = y

print('The largest palindrome made from the product of two 3-digit numbers is:', largest_palindrome)
print('It is the product of', spam, 'and', eggs)
