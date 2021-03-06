
#
#  Example file for working with functions
#

x = "abc"

# Global vs. local variables in functions
def someFunction():
    i = 10
    global x 
    x = "xyz"
    print(i)
    print(x)

someFunction()
#print(i) Error!
print(x)

# define a basic function
def func1():
    print("I am a function")

# function with arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function with return value
def cube(arg1):
    return arg1*arg1*arg1

# function with default value for an argument
def power(num, x = 1):
    result = 1
    for num in range(x):
        result = result * num
    return result


#function with variable number of arguments
def multiAdd(*args):
    result = 0
    for x in args:
        result = result + x
    return result 

func1()
print(func1())
print(func1) # print value of the function definition itself. Objects themeselves are objects!

func2(1,2)
print(func2(1,2))
print(func2)

cube(2)
print(cube(2))
print(cube)

print(power(2))
print(power(2,3))
print(power(x = 3, num = 2)) #named parameter can be supplied in any order
print(multiAdd(1,2,3,4,5))

# Lambda functions
x = 10
y = 15

def add(arg1, arg2):
    return arg1 + arg2

print(add(x,y))
print((lambda arg1, arg2: arg1 + arg2)(x, y))