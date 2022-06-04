'''Project Euler Problem 1: Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

import time
import os

os.system('clear')

print('''
summultiply - selective addition

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. We'll call this "summultiplication."
''')

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
