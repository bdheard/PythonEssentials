# Module 4 Quiz

**What is the slice expression that gives every third character of string s, starting with the last character and proceeding backward to the first?**

1. [ ] s[::-3]
1. [ ] s[-1::-3]
1. [ ] s[:0:-3]
1. [ ] s[-1:0:-3]

**Which of the following statements are true of lists in Python?**

1. [ ] The size of a list has not theoretical limit
1. [ ] These two list are materially the same:
    ['a', 'b', 'c']
    ['c', 'a', 'b']
1. [ ] An object may appear more than once in a list.
1. [ ] All elements in a list must be of the same type
1. [ ] A list cannot contain another list


**Which results are correct given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
print(a[4::-2])
```
1.[ ] ['50', '30']
1.[ ] ['50', '10']
1.[ ] ['50', '30', '10']
1.[ ] ['30', '50', '10']

**Which results are current given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
print(a[-5:-3])
```
1. [ ] ['20', '30']
1. [ ] ['20', '30']
1. [ ] ['20', '30']
1. [ ] ['20', '30']

**Which results are current given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
max(a[2:4] + ['35'])
```
1. [ ] '40'
1. [ ] '40'
1. [ ] '40'
1. [ ] '40'

**Which results are current given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
print(a[-6])
```
1. [ ] '10'
1. [ ] '60'
1. [ ] Index Out of Range Error
1. [ ] '50'

**Given the list ```python a = ['a', 'b', 'c']``` Which of the following statements adds 'd' and 'e' to the end of a, so that it then equals ```python ['a', 'b', 'c', 'd', 'e']```:**

1. [ ] a.append(['d', 'e'])
1. [ ] a += ['d', 'e']
1. [ ] a.extend(['d', 'e'])
1. [ ] a += 'de'
1. [ ] a[-1:] = ['d', 'e']
1. [ ] a[len(a):] = ['d', 'e']

**Given the tuple ```python t = ('a', 'b', 'c')```, which of the following statements replaces the second element ('b') with the string 'x':**

1. [ ] t[1] = 'x'
1. [ ] t(1) = 'x'
1. [ ] t[1:1] = 'x'
1. [ ] The tuple cannot be modified.

**What is the value of b after the following statement is executed:**

```python
a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
```

1. [ ] 6
1. [ ] 5
1. [ ] 4
1. [ ] 2

**Which of the following statements are true regarding dictionaries Python:**

1. [ ] Dictionaries can be nested to any depth.
1. [ ] Dictionaries are mutable.
1. [ ] Dictionaries are accessed by key.
1. [ ] Items are accessed by their position in a dictionary.
1. [ ] A dictionary can contain any object type except another dictionary.
1. [ ] All the keys in a dictionary must be of the same type.

**Given this dictionary ```python d = {'a': 100, 'b': 200, 'c': 300}```, what is the result of this statement:**

```python
d['b':'c']
```

1. [ ] 200 300
1. [ ] It raises an exception
1. [ ] (200, 300)
1. [ ] [200, 300]

**Which of the following statements creates a variable x2 which contains a copy of x1:**

1. [ ] x2 = dict(x1.keys())
1. [ ] x2 = dict(x1)
1. [ ] x2 = x1
1. [ ] x2 = dict(x1.items())
1. [ ] x2 = dict(x1.values())
1. [ ] 
    x2 = {}

    x2.update(x1)

**Which of the following statement are true regarding sets in Python:**

1. [ ] A given element can’t appear in a set more than once
1. [ ] The order of elements in a set is significant.
1. [ ] Sets are mutable.
1. [ ] A set may contain elements that are mutable.

**Which of the following statements define the set {'a', 'b', 'c'}:**

1. [ ] s = set(['a', 'b', 'c'])
1. [ ] s = set('a', 'b', 'c')
1. [ ] s = set('abc')
1. [ ] s = {'a', 'b', 'c'}
1. [ ] s = {('a', 'b', 'c')}