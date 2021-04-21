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

def union(list_one: set, list_two: set):
    list_one = set(list_one.split(","))
    list_two = set(list_two.split(","))
    return list_one.union(list_two)

def difference(list_one, list_two):
    list_one = set(list_one.split(","))
    list_two = set(list_two.split(","))
    return list_one.difference(list_two)

def intersection(list_one, list_two):
    list_one = set(list_one.split(","))
    list_two = set(list_two.split(","))
    return list_one.intersection(list_two)

def calculate_stats(list_one, list_two):
    list_one = list_one.split(",")
    list_two = list_two.split(",")
    print(f"List 1 Min: {min(list_one)}")
    print(f"List 1 Max: {max(list_one)}")
    print(f"List 1 Length: {len(list_one)}")
    print(f"List 2 Min: {min(list_two)}")
    print(f"List 2 Max: {max(list_two)}")
    print(f"List 2 Length: {len(list_two)}")
    
def sort_lists(list_one, list_two):
    list_one = list_one.split(",")
    list_two = list_two.split(",")
    combined_list = list_one + list_two
    combined_list.sort()
    return combined_list

operation = input("Please enter Operation:")
first_param = input("Please enter first parameter:")
second_param = input("Please enter second parameter:")

if operation == 'Add':
    print(first_param, "+", second_param, "=", add(first_param, second_param))
elif operation == 'Sub':
    print(first_param, "-", second_param, "=", subtract(first_param, second_param))
elif operation == 'Mul':
    print(first_param, "*", second_param, "=", multiply(first_param, second_param))
elif operation == 'Div':
    print(first_param, "/", second_param, "=", divide(first_param, second_param))
elif operation.upper() == 'UNION':
    print(f"Union: {union(first_param, second_param)}")
elif operation.upper() == 'INTERSECTION':
    print(f"Intersection: {intersection(first_param, second_param)}")
elif operation.upper() == 'DIFFERENCE':
    print(f"Difference: {difference(first_param, second_param)}")
elif operation.upper() == 'SORT':
    print(sort_lists(first_param, second_param))
elif operation.upper() == 'STATS':
    print(calculate_stats(first_param, second_param))
else:
    print("Unknown operation.")