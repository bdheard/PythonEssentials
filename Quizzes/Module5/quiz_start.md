# Module 5 Quiz

**A while loop in Python is used for what type of iteration?**

1. [ ] indeterminate
1. [ ] indefinite
1. [ ] discriminant
1. [ ] definite

**What is the output of the following code snippet:**

```python
a = {'x': 1, 'y': 2, 'z': 3}
while a:
    print(a.popitem())
print('Done.')
```

1. [ ] Done.
1. [ ] No output is generated.
1. [ ] ('z', 3)
       ('y', 2)
       ('x', 1)
       Done.
1. [ ]  x
        y
        z

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
1. [ ]  e
        d
        c
        Done.
1. [ ] The snippet doesn’t generate any output.

**What is the output of the following code snippet:**

```python
a = ['a', 'b', 'c', 'd', 'e']
while a:
    if len(a) < 3:
        continue
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
1. [ ]  e
        d
        c
        Done.
1. [ ] The snippet doesn’t generate any output.
1. [ ] The loop never terminates

**True or False. The print() statement will be executed in the following program:**

```python
a = ['a', 'b', 'c', 'd', 'e']
while a:
    print(a.pop())
else:
    print('Done.')
```
1. [ ]  True
1. [ ]  False