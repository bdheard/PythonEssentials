---
title: Python Essentials
---


# Module 8

## Overview

1. Clean code
1. Linting

::: notes
:::

## This is valid, but is it clean?

```python
x = 12
if x== 24:
 print('Is valid')
else:
    print("Not valid")

def helper(name='sample'):
 pass

def convertTouc( name = 'sample' ):
         return name.upper()
```

::: notes
touc: to upper case
:::

## Why clean code?

- Makes code readable
- Easier to debug
- Easier to maintain by you and others

::: notes

:::

## Spacing

- Spaces, not tabs
- VSCode automatically converts tabs to spaces
- Avoid extraneous whitespace

```python
{'good': 200}
{ 'bad' : 100}
```

::: notes

:::

## Naming

- **Bad:**
    - d
    - DaysSinceCreation
    - daysSinceCreation
    - c = dta_rcrd_102()
- **Good:**
    - days_since_creation
    - customer_address = Address()


::: notes
Notes:
https://www.python.org/dev/peps/pep-0008/
:::

## Functions

- Think small
- Should do one thing
    - They should do it well.
    - They should do it only.
- Descriptive names. Don't fear long names
- Reduce number of arguments.
    - wrap arguments inside meaningful objects

```python
makeCircle(double x, double y, double radius)

makeCircle(Point center, double radius)
```

::: notes
Notes:

Reduce number of arguments
0: ideal
1: ok
2: ok
3: justify
4 or more: avoid
:::

## Comments

- “Don’t comment bad code—rewrite it.” —Brian W. Kernighan and P. J. Plaugher
- Can be helpful or damaging
- Inaccurate comments are worse than no comments at all
- Used to compensate failure expressing with code
- They can lie
- Must have them, but minimize them
- Express yourself in code

::: notes
:::

## Comments Example

**Bad:**
```python
# Check to see if the employee is eligible for full benefits
if ((employee.flags & HOURLY_FLAG) && (employee.age > 65))
```

**Good:**
```python
if (employee.isEligibleForFullBenefits())
```

::: notes
:::

## Documentation

- String literal at start of module, function, class, or method.
- Used for documentation.

```python
def print_hello(user_name: str) -> str:
    """
    Generates a greeting to the user by name

	Parameters:
		user_name (str): The name of the user
	Returns:
		str: The greeting
	"""
	return 'Hello, ' + name
```

::: notes
Use 3 quotes to create a docstring when it is placed at the top of the function, class, or module.
:::

## Classes

- Should be small
- Single responsibility principle
- Automatically run by Visual Studio Code

![image](../media/single_responsibility_principle.png)

::: notes
:::

## Linting

- Identify formatting issues
- Pylint for Python
- Windows:

    ```bash
    pip install pylint
    ```
- macOS or Linux:

    ```bash
    pip3 install pylint
    ```

::: notes
:::

## Type hints

- Tell the editor and linter what data types to expect
- DOES NOT cause "compiler" errors

```python
def get_user_greeting(user_name):
    return 'Hello, ' + user_name

greeting = get_user_greeting(42)

print(greeting)
```
**Error!**
```python
TypeError: must be str, not int 
```

```python
def get_user_greeting(user_name: str) -> str:
    return 'Hello, ' + user_name

greeting = get_user_greeting(42)

print(greeting)
```
:::notes

Notes:
- parameter type
- return type

:::

