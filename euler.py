import time
import problems

# Problem 1
start_clock_time = time.time()
start_cpu_time = time.process_time()
p1 = problems.multipladd()
end_clock_time = time.time()
end_cpu_time = time.process_time()
clock_time = end_clock_time - start_clock_time
cpu_time = end_cpu_time - start_cpu_time
print('The solution to Problem 1 is {}.'.format(format(p1, ',')))
print('''This calculation required {} seconds of clock time
but only {} seconds of cpu time.'''.format(clock_time, cpu_time))
