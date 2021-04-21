# Module 7 Quiz

**A Python module is a file with the _____ file extension that contains valid Python code.**

1. [ ] .module
1. [X] .py
1. [ ] .pymodule
1. [ ] .pym

**Explanation:**

Any file containing valid Python code whose file name ends with the .py extension is a Python module.


**To use a module in another module, you must import it using an ________ statement.**

1. [ ] include
1. [X] import
1. [ ] load
1. [ ] namespace

**Explanation:**

When you import one module into another, the contents of the the imported module become available in the other. The module with the import statement is called the calling module.


**Suppose a function called add() is defined in a module called adder.py. Which of the following code snippets correctly show how to import and use the add() function? Select all that apply.**


1. [X]  from adder import add
        result = add(2, 3)
1. [X]  import adder
        result = adder.add(2, 3)
1. [ ]  import add from adder
        result = add(2, 3)
1. [ ]  from adder import add
        result = adder.add(2, 3)

**Explanation:**

The following is not valid because the name adder is not defined:

```python
from adder import add

result = adder.add(2, 3)
```

Only the name add is imported from the adder module.

The following is not valid because the import statement is in the wrong order:

```python
import add from adder

result = add(2, 3)
```
To fix it swap the from and import parts so that the statement reads from adder import add.


**A package is a folder containing one or more Python modules. One of the modules in a package must be called _______.**

1. [ ] init.py
1. [ ] __package__.py
1. [X] __init__.py
1. [ ] __main__.py
1. [ ] main.py

**Explanation:**

A package is a folder that contains one or more Python modules. It must also contain a special module called __init__.py.


**Which of the following is not a valid namespace?**

1. [ ] Global namespace
1. [X] Public namespace
1. [ ] Built-in namespace
1. [ ] Local namespace

**Explanation:** 
During a Python program execution, there are as many as three namespaces – built-in namespace, global namespace and local namespace.

**What is the order of namespaces in which Python looks for an identifier?**

1. [ ] Python first searches the global namespace, then the local namespace and finally the built-in namespace
1. [ ] Python first searches the built-in namespace, then the global namespace and finally the local namespace
1. [X] Python first searches the local namespace, then the global namespace and finally the built-in namespace
1. [ ] Python first searches the built-in namespace, then the local namespace and finally the global namespace

**Explanation:** 
Python first searches for the local, then the global and finally the built-in namespace.