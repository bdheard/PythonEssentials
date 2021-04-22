#
# Async
#

# Synchronous logic 

import time

def long_running_function(i):
    print(f"Start function run no. {i}")
    time.sleep(3)
    print(f"End function run no. {i}")

def main():
    for i in range(3):
        long_running_function(i)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"Program executed in {elapsed:0.2f} seconds.")