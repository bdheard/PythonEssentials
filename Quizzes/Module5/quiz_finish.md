# Module 5 Quiz

**A while loop in Python is used for what type of iteration?**

1. [ ] indeterminate
1. [X] indefinite
1. [ ] discriminant
1. [ ] definite

**Explanation:**

A while loop implements indefinite iteration, where the number of times the loop will be executed is not specified explicitly in advance.


**What is the output of the following code snippet:**

```python
a = {'x': 1, 'y': 2, 'z': 3}
while a:
    print(a.popitem())
print('Done.')
```

1. [ ] Done.
1. [ ] No output is generated.
1. [X] ('z', 3)
       ('y', 2)
       ('x', 1)
       Done.
1. [ ]  x
        y
        z

**Explanation:**

The .popitem() method removes one key-value pair from d and returns it as a tuple. So the body of this while loop displays the contents of d as tuples.

Once the last key-value pair has been removed, d is empty and is falsy in Boolean context. The while loop then terminates and displays the line following the loop body.

**What is the output of the following code snippet:**

```python
a = ['a', 'b', 'c', 'd', 'e']
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')
```

1. [ ]  e
        d
        c
1. [ ]  e
        d
        c
        b
        a
        Done.
1. [X]  e
        d
        c
        Done.
1. [ ] The snippet doesn’t generate any output.

**Explanation:**
When no arguments are specified, a.pop() removes and returns the last item in a. So each time through the loop, the last item is displayed.

But when the loop contains fewer than three items, the break statement on line 4 is reached, and the loop is terminated. Execution then proceeds to the print() statement following the loop, on line 6.

**What is the output of the following code snippet:**

```python
a = ['a', 'b', 'c', 'd', 'e']
while a:
    if len(a) < 3:
        continue
    print(a.pop())
print('Done.')
```

1. [X]  e
        d
        c
1. [ ]  e
        d
        c
        b
        a
        Done.
1. [ ]  e
        d
        c
        Done.
1. [ ] The snippet doesn’t generate any output.
1. [X] The loop never terminates

**Explanation:**

In this case, though, when the list shrinks to fewer than three items, a continue statement is executed instead of a break statement. Instead of terminating the loop completely, execution jumps to the top of the loop and the while loop expression is re-evaluated. a is truthy because it is not empty, so the loop executes again.

All list elements are printed in the same order as before, but there is no "Done." text printed at the end.

**True or False. The print() statement will be executed in the following program:**

```python
a = ['a', 'b', 'c', 'd', 'e']
while a:
    print(a.pop())
else:
    print('Done.')
```
1. [X]  True
1. [ ]  False

**Explanation:**

The else clause will be executed only if the loop terminates “by exhaustion”—that is, if the loop iterates until the controlling condition becomes false. If the loop is exited by a break statement, the else clause won’t be executed.