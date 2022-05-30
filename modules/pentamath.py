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
            break
        else:
            number = reduced

    factors.append(number)
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

    factors = []

    for i in range(int(number ** 0.5) + 1):
        if i < 4:
            continue
        if number % i == 0:
            return False

    return True
