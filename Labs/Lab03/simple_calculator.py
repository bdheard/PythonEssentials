# simple calculator

# This function adds two numbers
def add(x, y):
    return float(x) + float(y)

# This function subtracts two numbers
def subtract(x, y):
    return float(x) - float(y)

# This function multiplies two numbers
def multiply(x, y):
    return float(x) * float(y)

# This function divides two numbers
def divide(x, y):
    try:
        return float(x) / float(y)
    except ValueError:
        return 0
    except ZeroDivisionError:
        return 0
    finally:
        print("There was a problem with the division.")

operation = input("Please enter Operation:")
first_number = input("Please enter first number:")
second_number = input("Please enter second number:")

if operation == 'Add':
    print(first_number, "+", second_number, "=", add(first_number, second_number))
elif operation == 'Sub':
    print(first_number, "-", second_number, "=", subtract(first_number, second_number))
elif operation == 'Mul':
    print(first_number, "*", second_number, "=", multiply(first_number, second_number))
elif operation == 'Div':
    print(first_number, "/", second_number, "=", divide(first_number, second_number))
else:
    print("Unknown operation.")