# Module 2 Quiz

#### What gets printed?

```python
xs = [1,2,3]
xs.append(7)
print(sum(xs))
```

1. [ ] It's impossible to know.
1. [x] 13
1. [ ] Something else.


#### Python Lists and Default Arguments

```python
def take_default_list(xs = []):
    xs.append(7)
    return sum(xs)
```

#### What is the output of ``take_default_list([1,2,3])``?

1. [ ] It's impossible to know.
1. [ ] 13
1. [ ] Something else.

#### In the Python statement x = a + 5 - b:

- a and b are ________
- a + 5 - b is ________

1. [X] operands, an expression
1. [ ] terms, a group
1. [ ] operands, an equation
1. [ ] operators, a statement

#### What is the value of the expression 100 / 25?

1. [ ] 4
1. [X] 4.0

##### Explanation:
If you answered 4, you might have forgotten that the result of standard division is always float. The value of 100 // 25 (integer division) is 4.

#### You should use the == operator to determine whether objects of type float are equal.

1. [ ] True
1. [X] False

##### Explanation:
Internal representation of float objects is not precise, so they can’t be relied on to equal exactly what you think they will:

```python
1.1 + 2.2 == 3.3
```
You should instead compute whether the numbers are close enough to one another to satisfy a specified tolerance.

#### Consider the following code snippet:

```python
x = 10.0
y = (x < 100.0) and isinstance(x, float)
```

After these are executed, what is the value of y?

1. [ ] None
1. [X] True
1. [ ] Correct
1. [ ] 1
1. [ ] 0
1. [ ] False

#### Which of the following are truthy:

1. [X] 0.000001
1. [ ] 0
1. [ ] []
1. [X] True
1. [X] 'None'
1. [ ] False

##### Explanation
The Python object None is falsy, but the non-empty string 'None' is truthy.

0.000001, a non-zero numeric value, is also truthy. But barely.

#### What is the value of the expression a and b?:

```python
a = 100
b = 200
```

1. [ ] 0
1. [X] 200
1. [ ] 100
1. [ ] False
1. [ ] True

##### Explanation
When two non-Boolean values are joined by and or or, the value of the expression is one of the operands, not True or False.

For two non-Boolean values a and b:

If a is	a or b is	a and b is
truthy	a	b
falsy	b	a

#### Will the highlighted line of code raise an exception?

```python
x = -100
from math import sqrt
x > 0 and sqrt(x)
```
1. [ ] Yes
1. [X] No

##### Explanation
In the highlighted line, x > 0 is False. The expression is already known to be falsy at that point. Due to short-circuit evaluation, sqrt(x) (which would raise an exception) is not evaluated.

#### For two objects x and y:

- x is y is True

if and only if

- id(x) == id(y)

1. [X] True
1. [ ] False

#### Which of the following operators has the lowest precedence?

1. [X] and
1. [ ] not
1. [ ] %
1. [ ] +
1. [ ] **

##### Explanation:
and has the lowest precedence of all the operators covered in this tutorial except or.

The question doesn’t state whether the + operator listed is binary addition or unary positive. But it doesn’t matter—it wouldn’t have a lower precedence than and either way.

What is the value of the expression 1 + 2 ** 3 * 4?

1. [X] 33
1. [ ] 36
1. [ ] 108
1. [ ] 4097

##### Explanation:
The ** operator has the highest precedence, followed by *, and + the lowest.

Thus, the calculations are performed as follows:

1 + (2 ** 3) * 4
1 + (8 * 4)
1 + 32
33

To spare the reader from recalling the order of precedence, it wouldn’t be a bad idea to write this as 1 + ((2 ** 3) * 4), even though the parentheses don’t change the way the expression is evaluated.

#### The following statements return the same value:

```python
x = 100

x *= 5
x = x * 5
```

1. [X] True
1. [ ] False

**The Python Enhancement Proposal (PEP) that enumerates stylistic guidelines for Python code is:**

1. [ ] PEP 8000
1. [X] PEP 8
1. [ ] PEP 257
1. [ ] PEP 20

**Explanation:**
The Style Guide for Python Code is outlined in PEP 8. Related information on Docstring Conventions is specified in PEP 257.

For a list of other PEPs, see the Index of PEPs.

**The following code will run successfully without error:**

```python
x, y = 1, 2
    z = 3

print(x, y, z)
```
1. [ ] True
1. [X] False

**Variables must be declared before they are assigned a value.**

1. [ ] True
1. [X] False

**Variables may be assigned a value of one type, and after be assigned a value of a different type.**

1. [X] True
1. [ ] False

**How many objects and how many references are created by this program?**

x = 100
y = x

1. [ ] One object, one reference
1. [ ] Two objects, one reference
1. [ ] Two objects, two references
1. [X] One object, two references

**Which of the following styles does PEP8 recommend for multi-word variable names:**


1. [ ] customerFirstName (Camel Case)
1. [ ] CustomerFirstName (Pascal Case)
1. [X] customer_first_name (Snake Case)
1. [ ] customer-first-name (Kebab Case)