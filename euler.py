import time
import problems

# Problem 1
start_clock_time = time.time()
start_cpu_time = time.process_time()
solution = problems.multipladd()
end_clock_time = time.time()
end_cpu_time = time.process_time()
clock_time = end_clock_time - start_clock_time
cpu_time = end_cpu_time - start_cpu_time
print('The solution to Problem 1 is {}.'.format(format(solution, ',')))
print('''This calculation required {} seconds of clock time
and {} seconds of cpu time.
'''.format(clock_time, cpu_time))

# Problem 2
start_clock_time = time.time()
start_cpu_time = time.process_time()
solution = problems.evenfibs()
end_clock_time = time.time()
end_cpu_time = time.process_time()
clock_time = end_clock_time - start_clock_time
cpu_time = end_cpu_time - start_cpu_time
print('The solution to Problem 2 is {}.'.format(format(solution, ',')))
print('''This calculation required {} seconds of clock time
and {} seconds of cpu time.
'''.format(clock_time, cpu_time))

# Problem 6
start_clock_time = time.time()
start_cpu_time = time.process_time()
solution = problems.sumsquarediff()
end_clock_time = time.time()
end_cpu_time = time.process_time()
clock_time = end_clock_time - start_clock_time
cpu_time = end_cpu_time - start_cpu_time
print('The solution to Problem 6 is {}.'.format(format(solution, ',')))
print('''This calculation required {} seconds of clock time
and {} seconds of cpu time.
'''.format(clock_time, cpu_time))

# Problem 3
start_clock_time = time.time()
start_cpu_time = time.process_time()
solution = problems.largestpfactor()
end_clock_time = time.time()
end_cpu_time = time.process_time()
clock_time = end_clock_time - start_clock_time
cpu_time = end_cpu_time - start_cpu_time
print('The solution to Problem 3 is {}.'.format(format(solution, ',')))
print('''This calculation required {} seconds of clock time
and {} seconds of cpu time.
'''.format(clock_time, cpu_time))
