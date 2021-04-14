---
title: Module 5
subtitle: Python Essentials
---

## Overview

1. Loops
1. Map
1. filter
1. Reduce
1. List comprehensions

## For loops

- For loops takes each item in an array or collection in order, and assigns it to the variable you define.
- Loop through a collection
    ```python
    for name in ['David', 'James']:
        print(name)
    ```
- Loop a number of times
    ```python
    for index in range(0, 2):
        print(index)
    ```

::: notes
:::

## While loop

- While loops perform an operation as long as a condition is true.

```python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
	print(names[index])
	# Change the condition!!
	index = index + 1

```

::: notes
:::

## Using map()

- Alternative approach that’s based in functional programming.
- You pass in a function and an iterable, and map() will create an object. 
- This object contains the output you would get from running each iterable element through the supplied function.

```python
fruits = ["apple", "banana", "cherry"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x.upper())

print(newlist)
```

```python
fruits = ["apple", "banana", "cherry"]
newlist = []

def copy_list(fruits):
  return fruits.upper()

newlist = map(copy_list, fruits)

print(newlist)
```

```bash
['APPLE', 'BANANA', 'MANGO']
```

::: notes
:::

## Lambda Functions

- Alternative approach that’s based in functional programming.
- You pass in a function and an iterable, and map() will create an object. 
- This object contains the output you would get from running each iterable element through the supplied function.

```python
fruits = ["apple", "banana", "cherry"]
newlist = []

def copy_list(fruits):
  return fruits.upper()

newlist = map(copy_list, fruits)

print(newlist)
```

```python
fruits = ["apple", "banana", "cherry"]
newlist = []

def copy_list(fruits):
  return fruits.upper()

newlist = map(lamda fruits: , fruits)

print(newlist)
```

```bash
['APPLE', 'BANANA', 'MANGO']
```

::: notes
:::

## List Comprehensions

- Shorter syntax when you want to create a new list based on the values of an existing list.
- new_list = [expression for member in iterable]

```python
fruits = ["apple", "banana", "cherry"]
newlist = []

def copy_list(fruits):
  return fruits.upper()

newlist = map(copy_list, fruits)

print(newlist)
```

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
```

```bash
['apple', 'banana', 'mango']
```

::: notes

Considered more Pythonic:
1. Can be used for mapping and filtering. You don’t have to use a different approach for each scenario.
  This is the main reason why list comprehensions are considered Pythonic, as Python embraces simple, powerful tools that you can use in a wide variety of situations. 
1. You don't need to remember the proper order of arguments like you would when you call map().
1. List comprehensions are also more declarative than loops, which means they’re easier to read and understand. 
  Loops require you to focus on how the list is created.

**Warning!**
List comprehensions might make your code run more slowly or use more memory. If your code is less performant or harder to understand, then it’s probably better to choose an alternative.

List comprehension in Python includes three elements:

1. expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression i * i is the square of the member value.
1. member is the object or value in the list or iterable. In the example above, the member value is i.
1. iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(10).

https://realpython.com/list-comprehension-python/
:::