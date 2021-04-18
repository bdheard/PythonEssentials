#
# Fibonnaci sync
#

# Let us try applying asynchronous programming to another problem. 
# # In this example, we will consider the task of calculating different 
# numbers in the Fibonacci sequence. Our starting function will look like:

import time

def seq_fib(n):
    # if n = 0, say 0, if n = 1, say 1
    if n in [0, 1]:
        print(f'{n}: {n}')
        print(f'Took {time.perf_counter() - start:.2f} seconds.')
    
    # sequentially calculating fib(n)
    a, b = 1, 2
    i = 1
    while i < n:
        a, b = b, a + b
        i += 1
    
    # printing the last 20 digits if the result is too large
    print(f'{n}: {a % (10 ** 20)}')
    # printing the time elapsed from the beginning
    print(f'Took {time.perf_counter() - start:.2f} seconds.')

start = time.perf_counter()

seq_fib(1000000)
seq_fib(1000)
seq_fib(20)