import os
import time
import pentamath

os.system('clear')

def multipladd(x = 3, y = 5, z = 1000):
    '''Return the sum of all natural numbers below z that are multiples of x or y.
    '''

    x = int(input('Choose the first multiplier: '))
    y = int(input('Choose the second one: '))
    z = int(input('Set the upper limit: '))

    def sum_of_multiples(n, limit):
        '''Calculate the sum of multiples of a number below a limit.

        Uses the formula for the sum of an arithmetic progression.'''

        top = (limit - 1) // n
        return n * (top * (top + 1) // 2)

    start_clock_time = time.time()
    start_cpu_time = time.process_time()

    print('The sum of all the multiples of', x, 'and', y)
    print('below', z, 'is:', sum_of_multiples(x, z) + sum_of_multiples(y, z) - sum_of_multiples(x * y, z))

    end_clock_time = time.time()
    end_cpu_time = time.process_time()

    print('This calculation took {} seconds of clock time and {} seconds of CPU time.'.format(end_clock_time - start_clock_time, end_cpu_time - start_cpu_time))
