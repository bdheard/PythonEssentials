#
# Reduce
# 

# import reduce
from functools import reduce

# sequence
numbers = [0, 1, 2, 3, 4]

# create function
def addition(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

# invoke reduce
reduce(addition, numbers)