#
# Formatting
#

x = 12
if x == 24:
    print('Is valid')
else:
    print("Not valid")

def helper(name='sample'):
    pass

def another(name = 'sample'):
    pass

msg = "abc"
msg2 = 'abc'

print(msg)

def print_hello(name: str):
    """
    Greets the user using name
	Parameters:
		name (str): The name of the user
	Returns:
		str: The greeting
	"""
    print('Hello, ' + name)



print_hello('Daniel')