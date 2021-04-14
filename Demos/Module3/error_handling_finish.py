#
# Error handling
#

 
x = 42
y = 0

# Division

try:
    result = x / y
    print(result)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero")
else:
    print("Something else went wrong")
finally:
    restult = 0
    print("Clean up code")
