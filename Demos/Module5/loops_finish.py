#
# Example file for loops
#

def main():
    x = 0

    # while loop
    # Executes while condition evaluates to true
    while(x < 5):
        print(x)
        x = x + 1

    # for loop
    # NOTE: no index counter, as opposed to c++
    # in python loops are iterators
    for x in range(5,10):
        print(x)

    # use for loop over a collection
    # operate over sets of things
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # use break and continue statements
    for x in range(5, 10):
        # if (x == 7): break # stop executing this loop
        if (x % 2 == 0): continue # continue to next statement or skip and move on to next value
        print(x)

    # using the enumerate() function to get index
    # returns two values: index and value 
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()