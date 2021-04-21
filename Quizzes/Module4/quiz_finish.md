# Module 4 Quiz

**What is the slice expression that gives every third character of string s, starting with the last character and proceeding backward to the first?**

1. [ ] s[::-3]
1. [ ] s[-1::-3]
1. [ ] s[:0:-3]
1. [X] s[-1:0:-3]

**Explanation:**
The third index in the slice expression is -3, which indicates every third character stepping backward.

The first and second indices should be -1 (the last character) and 0 (the first character). Either of these can be allowed to default.


**Which of the following statements are true of lists in Python?**

1. [X] The size of a list has not theoretical limit
1. [ ] These two list are materially the same:
    ['a', 'b', 'c']
    ['c', 'a', 'b']
1. [X] An object may appear more than once in a list.
1. [ ] All elements in a list must be of the same type
1. [ ] A list cannot contain another list

**Explanation:**
A list is an ordered collection of objects. The order of the elements is an innate characteristic of the list.

A list may contain any number of elements (constrained by the computer’s memory, of course), of any type. The same object may occur any number of times.


**Which results are correct given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
print(a[4::-2])
```
1.[ ] ['50', '30']
1.[ ] ['50', '10']
1.[X] ['50', '30', '10']
1.[ ] ['30', '50', '10']

**Explanation:**
Slice syntax [4::-2] begins with the element at index 4 ('50') and proceeds to the start of the list, skipping every other item. That yields the elements at indices 4, 2, and 0.

**Which results are current given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
print(a[-5:-3])
```
1. [X] ['20', '30']
1. [ ] ['20', '30']
1. [ ] ['20', '30']
1. [ ] ['20', '30']

**Explanation:**

[-5:-3] starts at index -5 and goes up to but not including index -3

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
1. [X] '40'

**Explanation:**
The + operator concatenates, so the argument to max() is ['30', '40', '35']. The maximum value (for strings, the latest in alphabetical order) is '40'.

**Which results are current given the list below:**

```python
a = ['10', '20', '30', '40', '50', '60']
```
```python
print(a[-6])
```
1. [ ] '10'
1. [X] '60'
1. [ ] Index Out of Range Error
1. [ ] '50'

**Explanation:**
Negative indices begin with -1, so -6 actually is a valid index, corresponding to the first item in the list ('10'). This statement would not actually generate an error. Positive indices start with 0, so 6 would not be a valid index for this list.

**Given the list ```python a = ['a', 'b', 'c']``` Which of the following statements adds 'd' and 'e' to the end of a, so that it then equals ```python ['a', 'b', 'c', 'd', 'e']```:**

1. [ ] a.append(['d', 'e'])
1. [X] a += ['d', 'e']
1. [X] a.extend(['d', 'e'])
1. [X] a += 'de'
1. [ ] a[-1:] = ['d', 'e']
1. [X] a[len(a):] = ['d', 'e']

**Explanation:**

Correct answers:

Each of the following statements appends 'd' and 'e' to a:

a += ['d', 'e']

The += augmented assignment operator expects an iterable as the second operand. It iterates over the second operand and adds the resulting items to the end of the target operand.

a += 'de'

Remember that when Python iterates over a string, the result is a list of the component characters. Thus, this statement also appends the list ['d', 'e'].

a.extend(['d', 'e'])

The .extend() method also expects an iterable as an argument, and adds the designated items to the target list.

a[len(a):] = ['d', 'e']

Designates an empty slice at the end of a. This assignment replaces that slice with ['d', 'e'].

Incorrect Answers:

These statements do not append 'd' and 'e' to a:

a.append(['d', 'e'])

Output ['a', 'b', 'c', ['d', 'e']]

The .append() method takes a single object as its argument, and adds that object intact to the end of the target list. So this statement actually adds the list ['d', 'e'] to the end of a.

a[-1:] = ['d', 'e']

Output: ['a', 'b', 'd', 'e']

a[-1:] designates the slice of a consisting of only the element 'c', so this statement replaces that slice with ['d', 'e']:


**Given the tuple ```python t = ('a', 'b', 'c')```, which of the following statements replaces the second element ('b') with the string 'x':**

1. [ ] t[1] = 'x'
1. [ ] t(1) = 'x'
1. [ ] t[1:1] = 'x'
1. [X] The tuple cannot be modified.

**Explanation:**

The main difference between tuples and list is: tuples are immutable.


**What is the value of b after the following statement is executed:**

```python
a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
```

1. [ ] 6
1. [X] 5
1. [ ] 4
1. [ ] 2

The slice expression on the right side of the assignment produces the tuple (2, 5, 8):

The assignment is thus equivalent to this compound tuple packing/unpacking assignment:

a, b, c = (2, 5, 8)

**Which of the following statements are true regarding dictionaries Python:**

1. [ ] Dictionaries can be nested to any depth.
1. [ ] Dictionaries are mutable.
1. [X] Dictionaries are accessed by key.
1. [ ] Items are accessed by their position in a dictionary.
1. [ ] A dictionary can contain any object type except another dictionary.
1. [ ] All the keys in a dictionary must be of the same type.

**Explanation:**

Python dictionaries are similar to lists in that they are mutable and can be nested to any arbitrary depth (constrained only by available memory).

A dictionary can contain any type of Python object, including another dictionary. The keys in a given dictionary do not need to be the same type as one another, nor do the values.

Dictionary elements are accessed by key. Unlike with list indexing, the order of the items in a dictionary plays no role in how the items are accessed.

Even though dictionary access does not rely on item order, as of version 3.7 the Python language specification does guarantee that the order of items in a dictionary is maintained once the dictionary is created.


**Given this dictionary ```python d = {'a': 100, 'b': 200, 'c': 300}```, what is the result of this statement:**

```python
d['b':'c']
```

1. [ ] 200 300
1. [X] It raises an exception
1. [ ] (200, 300)
1. [ ] [200, 300]

**Explanation:**
Dictionaries are accessed by key, not by the position of the items. It would trow the following error message:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'slice'


**Which of the following statements creates a variable x2 which contains a copy of x1:**

1. [ ] x2 = dict(x1.keys())
1. [X] x2 = dict(x1)
1. [ ] x2 = x1
1. [X] x2 = dict(x1.items())
1. [ ] x2 = dict(x1.values())
1. [X] 
    x2 = {}

    x2.update(x1)

**Explanation:**

Correct Answers:

x2 = dict(x1)

x1 can be passed directly as an argument to dict() to create a new dictionary. The REPL output shows that the resulting x2 is a copy—it has the same value as x1, but is not the same object.

x2 = dict(x1.items())

x1.items() returns a list of tuples containing the key-value pairs in x1. That is also a valid argument to pass to dict() to create a copy of x1.

x2 = {}
x2.update(x1)

The first statement creates an empty dictionary in x2. Then x2.update(x1) merges entries from x1 into x2, which creates a copy of x1.

Incorrect Answers:

These statements do not create a copy of x1:

x2 = x1

This does make x2 point to an object equal to x1, but the same object, not a copy. 

x2 = dict(x1.keys())

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: dictionary update sequence element #0 has length 1; 2 is required

x1.keys() generates a list of the keys in x1. By itself, that is not valid input to the dict() function, and will not create another dictionary.

x2 = dict(x1.values())

Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: cannot convert dictionary update sequence element #0 to a sequence

x1.values() generates a list of the values in x1. Passing that to the dict() function will not create the dictionary.

**Which of the following statement are true regarding sets in Python:**

1. [X] A given element can’t appear in a set more than once
1. [ ] The order of elements in a set is significant.
1. [X] Sets are mutable.
1. [ ] A set may contain elements that are mutable.

**Explanation:**
- A set is a collection of distinct objects, called elements or members.
- Sets are unordered. 
- Set elements are unique. if you try to add an element to a set a second time, it has no effect.
- A set itself may be modified, but the elements contained in a set must be immutable.

**Which of the following statements define the set {'a', 'b', 'c'}:**

1. [X] s = set(['a', 'b', 'c'])
1. [ ] s = set('a', 'b', 'c')
1. [X] s = set('abc')
1. [X] s = {'a', 'b', 'c'}
1. [ ] s = {('a', 'b', 'c')}

**Explanation:**

- The simplest way to define a set is to specify the set elements in curly brackets.
- You can also define a set with the built-in set() function. The argument should be an iterable that yields the elements of the set.
- Sets are unordered. The fact that s displays as {'a', 'c', 'b'} instead of the order specified in the definition has no meaningful significance. 