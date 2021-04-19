# Module 3 Quiz

**Select one. In a Python program, a control structure:**

1. [ ] Directs the order of execution of the statements in the program
1. [ ] Directs what happens before the program starts and after it terminates
1. [ ] Manages the input and output of control characters
1. [ ] Defines data structures using within the program

**Which one of the following if statements will not execute successfully:**

1. [ ] A
```python
if (1, 2): print('blue')
```

1. [ ] B
```python
if (1, 2):
print('blue')
```

1. [ ] C
```python
if (1, 2):
    print('blue')
```

1. [ ] D
```python
if (1, 2):
                print('blue')
```

1. [ ] E
```python
if (1, 2):

    print('blue')
```

**What signifies the end of a statement block or suite in Python?**

1. [ ] }
1. [ ] A comment
1. [ ] A line that is indented less than the previous line
1. [ ] end

**What is the output of the following code snippet:**

```python
if 'red' in {'blue': 1, 'red': 2, 'green': 3}:
    print(1)
    print(2)
    if 'a' in 'xyz':
        print(3)
print(4)
```

1. [ ] 4
1. [ ]  1
        2
        3
        4
1. [ ]  1
        2
        4

1. [ ] It doesn’t generate any output.

**The following if/elif/else statement will raise a KeyError exception:**

```python
d = {'a': 0, 'b': 1, 'c': 0}

if d['a'] > 0:
    print('ok')
elif d['b'] > 0:
    print('ok')
elif d['c'] > 0:
    print('ok')
elif d['d'] > 0:
    print('ok')
else:
    print('not ok')
```

1. [ ] True
1. [ ] False

**Which of the following are valid if/else statements in Python, assuming x and y are defined appropriately:**

1. [ ] 
```python
if x < y: print('blue')
elif y < x: print('red')
else: print('green')
```

1. [ ] 
```python
if x < y: print('blue'); print('red'); print('green')
```

1. [ ] 
```python
if x < y: print('blue') else: print('red')
```

1. [ ] 
```python
if x < y: if x > 10: print('blue')
```

**What is value of this expression:**

```python
'a' + 'x' if '123'.isdigit() else 'y' + 'b'
```

1. [ ] 'ab'
1. [ ] 'axb'
1. [ ] 'axyb'
1. [ ] 'ax'

**Given two variables x and y defined. Which of these statements would evaluate whether x is less than y, and not do anything, even if the condition is true.**

1. [ ]
```python
if x < y:
    pass
```
1. [ ]
```python
if x < y:
    return
```
1. [ ]
```python
if x < y:
    continue
```
1. [ ]
```python
if x < y:
    break
```

**How are lambda functions useful? Select all that apply:**

1. [ ] Lambda functions always make code easier to read.
1. [ ] They can be useful as quick single line functions.
1. [ ] They allow quick calculations as the input to other functions.
1. [ ] Lambda functions are used for functional programming.

**What is the output of the following code snippet?**

```python
func = lambda x: return x
print(func(2))
```

1. [ ] SyntaxError
1. [ ] 0
1. [ ] x
1. [ ] 2
1. [ ] 2.0

**What are the common functional programming methods that use lambdas? Select all that apply:**

1. [ ] map()
1. [ ] lookup()
1. [ ] filter()
1. [ ] reduce()

**What would be the output of the following code snippet?**

```python
(lambda x: (x + 6) * 10 / 4)(6)
```

1. [ ] 60.0
1. [ ] SyntaxError
1. [ ] 0
1. [ ] 30.0

