"""
Project Euler Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# An elegant solution that relies on the fact every third
# Fibonacci number is necessarily even
ceiling = int(input('Enter ceiling for even Fibonacci sum: '))

total = 0
a = 1
b = 1
c = a + b

while c < ceiling:
    total += c
    a = b + c
    b = c + a
    c = a + b

print('The sum of even Fibonacci numbers below', ceiling, 'is:', total)
