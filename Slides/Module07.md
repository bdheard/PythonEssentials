---
title: Python Essentials
---

# Module 7

## Overview

1. Using modules 
1. Packages
1. Creating modules
1. Python virtual environment

::: notes
:::

## Modules Overview

- A Python file with functions, classes, etc.
- Break code down into reusable structures.
- Referenced by using the import statement.
- To speed up loading modules, Python caches the compiled version of each module in the **__pycache__** directory under the name module.version.pyc

::: notes
:::

## Modules 

- Consider placing all import statements at the start of a module.

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

## Packages Overview

- Modules can be distributed using a Package.
- A Package is a published collection of modules.
- Defines a namespace like PythonEssentials.Calculator
- You can publish to, and install from pypi.org.
- Install package with pip.

::: notes
:::

## Packages Overview

```python
# Install an individual package
pip install colorama

# Install from a list of packages
pip install -r requirements.txt
```

![](../media/pypi.png)

::: notes
https://pypi.org/

if you don't specify version, it will install the latest.

By default, python install all packages globally
:::

## Finding Packages

![](../media/pypi.png)

::: notes

:::

## Creating Packages

- ```__init__.py``` treats directories as packages.
- Can be an empty file or include initialization code.

```
PythonEssentials/
                __init__.py
                calculators/
                            __init__.py
                            simple_calculator.py
                            advanced_calculator.py
                parsers/
                            __init__.py
                            console_input_parser.py
                            console_output_parser.py
                            file_input_parser.py
                            file_output_parser.py
```

::: notes
:::

## Python Virtual Environment

Isolated environment to install your dependencies.

1. Install virtual environment
1. Create virtual environnement.
1. Activate virtual environment in terminal
1. Activate virtual environment in VS Code.
1. Create Requirements file

```bash
pip install virtualenv
python -m venv .venv
.\.venv\Scripts\activate.ps1
pip install colorama
python -m pip freeze > requirements.txt
```
![](../media/ActivatePythonVirtualEnvironment.PNG)

::: notes

- https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
- https://code.visualstudio.com/docs/python/debugging
- https://code.visualstudio.com/docs/python/environments

-m: grab a specific module

:::

