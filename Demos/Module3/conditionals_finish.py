#
# Example file conditional statements
#

def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if (x < y):
        st = "x is less than y"
    elif(x > y):
        st = "x is greater than y"
    else:
        st = "x is the same as y"

    print (st)

    # NOTE: No switch statement

    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x < y) else "x is greater than or the same as y"

    print (st)

    # conditional logic with IN operator
    city = 'Raleigh'
    if city in ('Raleigh','Charlotte', 'Asheville'):
        print('You live in North Carolina')
    else:
        print('Not sure where you live')

if __name__ == "__main__":
    main()