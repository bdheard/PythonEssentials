#
# Fibonnaci async
#

# We see that our responsiveness problem has been addressed: 
# after running the program, the more lightweight tasks were 
# executed first, and the longest-running task returned last.

import asyncio
import time

async def async_fib(n):
    # if n = 0, say 0, if n = 1, say 1
    if n in [0, 1]:
        print(f'{n}: {n}')
        print(f'Took {time.perf_counter() - start:.2f} seconds.')
    
    # sequentially calculating fib(n)
    a, b = 1, 2
    i = 1
    while i < n:
        a, b = b, a + b
        
        if i % 50000 == 0:
            await asyncio.sleep(0) # switches task every 50,000 iterations
        
        i += 1
    
    # print the last 20 digits if the result is too large
    print(f'{n}: {a % (10 ** 20)}')
    # print the time elapsed from the beginning
    print(f'Took {time.perf_counter() - start:.2f} seconds.')

loop = asyncio.get_event_loop() # creating the event loop
# adding tasks to the task queue
tasks = [
    loop.create_task(async_fib(1000000)),
    loop.create_task(async_fib(1000)),
    loop.create_task(async_fib(20))
]

start = time.perf_counter()
# run the event loop until all tasks are complete
loop.run_until_complete(asyncio.wait(tasks))

print('Done.')