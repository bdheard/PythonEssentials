# Module 3 Quiz

**In a Python program, a control structure:**

1. [X] Directs the order of execution of the statements in the program
1. [ ] Directs what happens before the program starts and after it terminates
1. [ ] Manages the input and output of control characters
1. [ ] Defines data structures using within the program

**Which one of the following if statements will not execute successfully:**

1. [ ] A
```python
if (1, 2): print('blue')
```

1. [X] B
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
1. [X] A line that is indented less than the previous line
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
1. [X]  1
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

1. [X] True
1. [ ] False

**Explanation:**
d['d'] does refer to an invalid key. But the expression in that elif clause is never evaluated. Once the elif d['b'] > 0 clause on line 5 is found to be True, the remaining elif clauses are skipped because of short-circuit evaluation.

**Which of the following are valid if/else statements in Python, assuming x and y are defined appropriately:**

1. [X] 
```python
if x < y: print('blue')
elif y < x: print('red')
else: print('green')
```

1. [X] 
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

**Explanation**

It is syntactically correct to specify multiple semicolon-separated statements for a single if, although it is discouraged by PEP 8 except for very simple cases. The semicolons bind most tightly, so if the expression is true, all the statements are executed (as in this case), and if it is false, none of them are.

You can specify the statement(s) on the same line as if, elif or else, immediately following the colon. However, this is not considered desirable style either.

**What is value of this expression:**

```python
'a' + 'x' if '123'.isdigit() else 'y' + 'b'
```

1. [ ] 'ab'
1. [ ] 'axb'
1. [ ] 'axyb'
1. [X] 'ax'

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
1. [X]
```python
if x < y:
    break
```

**Explanation:**

Because code blocks are defined by indentation in Python, there must be something to indent. A block can not be empty.

The pass statement serves as a do-nothing statement that can be used to define a code stubs.

**How are lambda functions useful? Select all that apply:**


1. [ ] Lambda functions always make code easier to read.
1. [X] They can be useful as quick single line functions.
1. [X] They allow quick calculations as the input to other functions.
1. [X] Lambda functions are used for functional programming.

**Explanation:**
You should consider that lambdas can be hard for another developer to read/debug. 

**What is the output of the following code snippet**

```python
func = lambda x: return x
print(func(2))
```

1. [X] SyntaxError
1. [ ] 0
1. [ ] x
1. [ ] 2
1. [ ] 2.0

**Explanation:**
In a lambda function, statements like return, pass, assert, or raise will raise a SyntaxError exception.

What are the common functional programming methods that use lambdas? Select all that apply:


1. [X] map()
1. [ ] lookup()
1. [X] filter()
1. [X] reduce()

