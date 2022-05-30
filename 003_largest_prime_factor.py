'''
Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

target = int(input('Enter a number for factoring: '))

def factor(number):
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
