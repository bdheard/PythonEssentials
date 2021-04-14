#
# Demo file for variables
#

# Declare a variable and initialize it
i = 0
print(i)

#inspect data type
print(type(i))

# re-declaring the variable works
x = "abc"
print(x)

# ERROR: variables of different types cannot be combined
#print("this is a string" + 123)

# But this works: variables of different types cannot be combined
print("this is a string" + str(123))

# String literals
print('Ben: "How are you?"')

print("""Ben: "How are you?" Ben's car.""")

print('''Ben: "How are you?" Ben's car.''')

# delete definition of variable previously declared
del i 
print(i)

# data type casting
param1 = "12.10"
param2 = "8.10"

print(float(param1) + float(param2))