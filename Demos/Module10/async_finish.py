#
# Async
#

# Synchronous logic 

import time
import asyncio

async def long_running_function(i):
    print(f"Start function run no. {i}")
    await asyncio.sleep(1)
    print(f"End function run no. {i}")

async def main():
    await asyncio.gather(long_running_function(1), long_running_function(2), long_running_function(3))

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"Program executed in {elapsed:0.2f} seconds.")