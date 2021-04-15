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

## Virtual Environments

- By default, packages are installed globally
- Version management becomes a challenge
- Virtual environments can be used to contain and manage package collections
- Really just a folder behind the scenes with all your packages

```python
# Install virtual environment (global)
pip install virtualenv

# Windows systems
python –m venv <folder_name>

# OSX/Linux (bash)
virtualenv <folder_name>

```

::: notes
:::

## Using Virtual Environments

```bash
# Windows systems
# cmd.exe
<folder_name>\Scripts\Activate.bat
# Powershell
<folder_name>\Scripts\Activate.ps1
# bash shell
. ./<folder_name>/Scripts/activate

# OSX/Linux (bash)
<folder_name>/bin/activate

```

::: notes
:::