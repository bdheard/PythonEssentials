---
title: Lesson 7
subtitle: Python Essentials
---

## Overview

1. Using modules 
1. Pakcages
1. Creating modules
1. Python virtual environment

## Modules Overview

- A Python file with functions, classes and other components
- Break code down into reusable structures
- They're referenced by using the import statement.


```python
# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')
```

::: notes
:::

## Packages

- Modules can be distributed using a Package.
- Pakcages are published collection of modules.
- You can publish to, and install from pypi.org.
- Install package with pip.


```python
# Install an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt

# requirements.txt
colorama
```

![](../media/pypi.png)

::: notes
:::

## Python Virtual Environment

- Isolated environement where to install your dependencies.
- Create virtual environement.

    ```bash
    python -m venv .venv
    ```

- Activate virtual environement in VS Code.

    ![image](../media/ActivatePythonVirtualEnvironment.PNG)

- Activate virtual environement in command line
    ```bash
    .\.venv\Scripts\activate
    ```

- Create Requirements file
    ```bash
    python -m pip freeze > requirements.txt
    ```

::: notes

- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
- https://code.visualstudio.com/docs/python/debugging
- https://code.visualstudio.com/docs/python/environments

:::

