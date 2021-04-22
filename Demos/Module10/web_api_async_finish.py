#
# Web API
#

from timeit import default_timer
import aiohttp
import asyncio

async def load_data(session, delay):
    print(f'Start function with {delay} second timer')
    async with session.get(f'http://httpbin.org/delay/{delay}') as resp:
        text = await resp.text()
        print(f'Completed function with {delay} second timer')
        return text

async def main():
    # Start the timer
    start_time = default_timer()

    # Creating a single session
    async with aiohttp.ClientSession() as session:
        # Setup our tasks and get them running
        task_one = asyncio.create_task(load_data(session, 2))
        task_two = asyncio.create_task(load_data(session, 3))

        # Simulate other processing
        await asyncio.sleep(2)
        print('Doing other work')

        # Let's go get our values
        result_one = await task_one
        result_two = await task_two

        # Print our results
        elapsed_time = default_timer() - start_time
        print(f'The operation took {elapsed_time:.2} seconds')

asyncio.run(main())
