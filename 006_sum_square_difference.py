'''Project Euler Problem 6: Sum Square Difference

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

import pentamath

n=int(input('I\'ll find the difference between the sum of the squares and the square of the sums for the first ___ natural numbers. How many numbers would you like me to analyze? '))

square_of_sum = pentamath.sum_of_n(n) ** 2
sum_of_squares = pentamath.sum_of_n2(n)

print('The square of the sum is: ', square_of_sum)
print('The sum of the squares is: ', sum_of_squares)
print('The difference is', square_of_sum - sum_of_squares)
