import os
import time
import trickymath

os.system('clear')

def multipladd(x = 3, y = 5, z = 1000):
    '''Return the sum of all natural numbers below z that are multiples of x or y.
    '''

    return sum_of_multiples(x, z) + sum_of_multiples(y, z) - sum_of_multiples(x * y, z)
