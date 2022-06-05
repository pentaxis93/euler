import os
import time
import trickymath

os.system('clear')

# Problem 1: Sum of Multiples
def multipladd(x = 3, y = 5, z = 1000):
    '''Return the sum of all natural numbers below z that are multiples of x or y.
    '''

    return trickymath.sum_of_multiples(x, z) + trickymath.sum_of_multiples(y, z) - trickymath.sum_of_multiples(x * y, z)

    end_clock_time = time.time()
    end_cpu_time = time.process_time()

    print('This calculation took {} seconds of clock time and {} seconds of CPU time.'.format(end_clock_time - start_clock_time, end_cpu_time - start_cpu_time))
