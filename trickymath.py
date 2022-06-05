'''
Tricky math functions.
'''

def factors_all(number):
    '''Factor any positive integer.

    Returns a list of all prime factors, including duplicates.'''

    factors = []
    reduced = number

    while True:
        for i in range(2, number):
            if number % i == 0:
                factors.append(i)
                reduced = int(number / i)
                break
        if number == reduced:
            factors.append(number)
            break
        else:
            number = reduced

    return factors

def factors_unique(number):
    '''Factor any positive integer.

    Returns a list of unique prime factors.'''

    factors = []
    reduced = number

    while True:
        for i in range(2, number):
            if number % i == 0:
                if i not in factors:
                    factors.append(i)
                reduced = int(number / i)
                break
        if number == reduced:
            break
        else:
            number = reduced

    if number not in factors:
        factors.append(number)
    return factors

def ispalindrome(input):
    '''Evaluate whether or not an input is palindromic.'''
    if str(input)[:] == str(input)[::-1]:
        return True
    else:
        return False

def isprime(number):
    '''Test a number for primeness.'''

    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False

    return True

def sum_of_multiples(n, limit):
    '''Calculate the sum of multiples of a number below a limit.

    Uses the formula for the sum of an arithmetic progression.'''

    top = (limit - 1) // n
    return n * (top * (top + 1) // 2)

def sum_of_n(n):
    '''Return sum of the first n natural numbers.'''
    return n * (n + 1) // 2

def sum_of_n2(n):
    '''Return sum of the squares of the first n natural numbers.'''
    return n * (n + 1) * ((2 * n) + 1) // 6

def sum_of_n3(n):
    '''Return sum of the cubes of the first n natural numbers.'''
    return (n ** 2) * ((n + 1) ** 2) // 4
