---
title: Lesson 10
subtitle: Python Essentials
---

## Overview

1. Working with the OS
1. Reading and writing files

## Working with paths

```python
# Python 3.6 or higher
# Grab the library
from pathlib imporWt Path

# Where am I?
cwd = Path.cwd()
print(cwd)

# Combine parts to create full path and file name
new_file = Path.joinpath(cwd, 'new_file.txt')
print(new_file)
```

```bash
C:\intermediate-python\file_system
C:\intermediate-python\file_system\new_file.txt
False
```

:::notes
:::

## Working with directories

```python
from pathlib import Path
cwd = Path.cwd()

# Get the parent directory
parent = cwd.parent

# Is this a directory?
print(parent.is_dir())

# Is this a file?
print(parent.is_file())

# List child directories
for child in parent.iterdir():
    if child.is_dir():
        print(child)
```

```bash
True
False
C:\essentials-python\.git
C:\essentials-python\.vscode
C:\essentials-python\dir1
C:\essentials-python\dir2
C:\essentials-python\dir3
```

:::notes
:::

## Working with files

```python
from pathlib import Path

cwd = Path.cwd()
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# Get the file name
print(demo_file.name)

# Get the extension
print(demo_file.suffix)

# Get the folder
print(demo_file.parent.name)

# Get the size
print(demo_file.stat().st_size)
```

```bash
demo.txt
.txt
file_system
11
```

:::notes
:::

## Opening a file

```python
stream = open(file_name, mode, buffer_size)
```

**Modes:**
**r:** Read (default)
**w:** Truncate and write
**a:** Append if file exists
**x:** Write, fail if file exists
**+:** Updating (read/write)

**t:** Text (default)
**b:** Binary

:::notes
:::

## Reading from a file

```python
demo_file = open('demo.txt')

print(demo_file.readable()) # Can we read?
print(demo_file.read(1)) # Read the first character
print(demo_file.readline()) # Read a line
demo_file.close() # close the stream
```

```bash
True
L
orem ipsum dolor sit amet, consectetur adipiscing elit.
```

:::notes
:::

## Writing to a file

```python
stream = open('output.txt', 'wt') # write text

stream.write('H') # write a single string
stream.writelines(['ello',' ','world']) # write multiple strings
stream.write('\n') # write a new line
names = ['James','David'] # create a list of strings
stream.writelines(names) # write list of strings 

stream.close() # close the stream (and flush data)
```

```bash
True

# In the file
Hello world
SusanChristopher
```

:::notes
:::

## Working with streaming

```python
stream = open('output.txt', 'wt')
stream.write('demo!')
stream.seek(0) # Put the cursor back at the start
stream.write('cool')
stream.flush() # Write the data to file
stream.close() # Flush and close the stream
```

```bash
# In the file
cool!
```

:::notes
:::

## Error handling

```python
try:
	stream = open('output.txt', 'wt')
	stream.write('Lorem ipsum dolar')
finally:
	stream.close() # THIS IS REALLY IMPORTANT!!
```

or:

```python
with open('output.txt', 'wt') as stream:
    stream.write('Lorem ipsum dolar')
```

:::notes
:::

