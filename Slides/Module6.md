---
title: Lesson 6
subtitle: Python Essentials
---

## Overview

1. Classes
1. Inheritance
1. Mixins

## Classes Overview

* Create reusable components
* Group data and operations together
* Classes are nouns
* Properties are adjectives
* Methods are verbs

::: notes

2. Overview of Python
3. Flow Control
4. Sequence Types
5. Sorting and Slicing
6. Functions
7. Dictionaries and Sets
8. Object-oriented Python
9.  Creating and Using Modules
10. Errors and Exception Handling
11. Working with Files
12. Regular Expressions
13. Using the Standard Library

:::

## Creating Classes

```python
class Presenter():
	
    def __init__(self, name):
		# Constructor
		self.name = name
	
    def say_hello(self):
		# method
		print('Hello, ' + self.name)
    
    @property
	def name(self):
		return self.__name
	
    @name.setter
	def name(self, value):
		# cool validation here
		self.__name = value

```

::: notes

:::

## Using Classes

```python
presenter = Presenter('Chris')
presenter.name = 'Christopher'
presenter.say_hello()
print(presenter.name)
```

::: notes

:::

## Accessibility in Python

- **EVERYTHING is public**
- Conventions for suggesting accessibility
- _ means avoid unless you really know what you're doing
- __ (double underscore) means **do not use**


::: notes
:::

## Inheritance

- Creates an "is a" relationship
    - Student is a Person
    - SqlConnection is a DatabaseConnection
    - MySqlConnection is a DatabaseConnection
- Composition (with properties) creates a "has a" relationship
    - Student has a Class
    - DatabaseConnection has a ConnectionString

::: notes
:::

## Python Inheritance

- All methods are "virtual"
    - Can override or redefine their behavior
- Keyword super to access parent class
    - Constructor
    - Properties in methods
- Must always call parent constructor


::: notes
:::

## Inheriting from a class

```python
class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('Hello, ' + self.name)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def sing_school_song(self):
        print('Ode to ' + self.school)
```

::: notes

:::

## Using a derived class

```python
student = Student('John', 'Doe')
student.say_hello()
student.sing_school_song()

print(isinstance(student, Student))
print(isinstance(student, Person))
print(issubclass(Student, Person))
```

::: notes

:::

## Mixins

- Inherit from multiple classes.
- A little controversial.
- Can get messy quickly.
- Many modern languages only support single inheritance.
- Uses:
    - Enable functionality for frameworks such as Django.
    - Streamline repetitious operations.

::: notes
:::

## Using mixins

```python
class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print('Log message from ' + self.title)

class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connecting to database on ' + self.server)

class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'

def framework(item):
	# Perform the connection
    if isinstance(item, Connection):
        item.connect()
	# Log the operation
    if isinstance(item, Loggable):
        item.log()

# Create an instance of our class
sql_connection = SqlDatabase()
# Use our framework
framework(sql_connection) # connects and logs
```


::: notes
- Create:
    - Helper database class
    - Create different types for different databases
- Function: 
    - Connect to a database
    - Log what it's doing
:::