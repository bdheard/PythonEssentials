---
title: Lesson 2
subtitle: Python Essentials
---

## Overview

1. Print
1. Comments
1. Strings
1. Numbers

## Print

```python
print('Hello world')
print()
print("Hello world double quotes")
print('Blank line \nin the middle of string')
```

::: notes

Consistency

:::

## Comments

```python
# This is a comment in my code it does nothing
# print('Hello world')
# print("Hello world")
# No output will be displayed!
```

::: notes

:::

## Data Types

**Text:** str
**Numeric:** int, float, complex
**Sequence:** list, tuple, range
**Mapping:** dict
**Set:** set, frozenset
**Boolean:** bool
**Binary:** bytes, bytearray, memoryview


::: notes
https://www.w3schools.com/python/python_datatypes.asp
:::

## String

```python
first_name = 'Susan'
last_name = 'Ibach'
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)
print('Hello {} {}'.format(first_name, last_name))
print('Hello {0} {1}'.format(first_name, last_name))
print(f'Hello {first_name} {last_name}') # maybe best
```

```python
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))
```

::: notes

:::

## Numbers

```python
first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num ** second_num)

days_in_feb = 28
print(str(days_in_feb) + ' days in February')

first_num = '5'
second_num = '6'
print(first_num + second_num) #Output: 56

first_num = input('Enter first number ')
second_num = input('Enter second number ')
print(int(first_num) + int(second_num)) # Output: 11

```

| Symbol  | Operation      |
|---------|----------------|
| +       | Addition       |
| -       | Substraction   |
| *       | Multiplication |
| /       | Division       |
| **      | Exponent       |

::: notes
When displaying a string that contains numbers you must convert the numbers into strings.

Numbers can be stored as stringsNumbers stored as strings are treated as strings.

The input function always returns strings.
:::