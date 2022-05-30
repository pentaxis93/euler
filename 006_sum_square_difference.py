'''Project Euler Problem 6: Sum Square Difference

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

how_many=int(input('I\'ll find the difference between the sum of the squares and the square of the sums for the first ___ natural numbers. How many numbers would you like me to analyze? '))

sum_of_squares = 0
sum = 0
square_of_sum = 0

for i in range(1, how_many + 1):
    sum_of_squares += i ** 2
    sum += i

square_of_sum = sum ** 2

print('The square of the sum is', square_of_sum, '.')
print('The sum of the squares is', sum_of_squares, '.')
print('The difference is', square_of_sum - sum_of_squares, '.')
