---
title: Module 4
subtitle: Python Essentials
---

## Overview

1. Collections
1. Tuples
1. Calendar
1. Loops

## Lists

* Lists are collections of items.
* Lists can be expanded or contracted as needed.
* Can contain any data type.
* Commonly used to store a single column collection of information, however it is possible to nest lists.

```python
names = ['Christopher', 'Susan']
scores = []
scores.append(98) # Add new item to the end
scores.append(99)

print(names) # ['Christopher', 'Susan']
print(scores) # [98,99]
print(scores[1]) # 99
```

::: notes

:::

## Arrays

* Arrays are collections of items
* Designed to store a uniform basic data type, such as integers or floating point numbers.

```python
from array import array
scores = array('d')
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

```

::: notes

from array library
later module will talk about libraries and modules and packages.
basically we are importing an array

:::

## Lists Vs. Arrays

* Arrays:
  * Simple types such as numbers
  * Must all be the same type
* Lists:
  * Store anything
  * Store any type

::: notes

numpy will give you additional support

:::

## Common

```bash
names = ['Susan', 'Christopher']
print(len(names)) # Get the number of items
names.insert(0, 'Bill') # Insert before index
print(names)
names.sort()
print(names)
```

```
2
['Bill', 'Susan', 'Christopher']
['Bill', 'Christopher', 'Susan']
```

::: notes
sorts side effect is that it will modify the list
:::

## Retrieving Ranges

```bash
names = ['Susan', 'Christopher', 'Bill','Justin']
names
names[3]
names[1:3]
names[:3]
```

```
['Susan', 'Christopher', 'Bill','Justin']
['Justin']
['Christopher', 'Bill']
['Susan', 'Christopher', 'Bill']
```

::: notes
:::

## Dictionaries

- Dictionaries are key/value pairs of a collection of items.
- Dictionaries use keys to identify each item.

```python
person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])
```

```
{'first': 'Christopher', 'last': 'Harrison'}
Christopher
```

::: notes
:::

## Dictionaries Vs Lists 

* Dictionaries:
  * Key/Value pairs
  * Storage order not guaranteed
* Lists:
  * Zero-based index
  * Storage order guaranteed

::: notes

numpy will give you additional support

:::

## Loop through a collection

```python
for name in ['Christopher', 'Susan']:
    print(name)
```

```
Christopher
Susan
```

::: notes
:::

## For loops

- For loops takes each item in an array or collection in order, and assigns it to the variable you define.
- Loop through a collection
    ```python
    for name in ['Christopher', 'Susan']:
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