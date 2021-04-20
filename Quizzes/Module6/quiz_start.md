# Module 6 Quiz

A class is ___________ for an object.

1. [ ] a reference
1. [ ] an instance
1. [ ] a blueprint
1. [ ] a pointer

**The correct way to instantiate this class is:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

1. [ ] Person.__init__("James", 30)
1. [ ] Person.create("James", 30)
1. [ ] Person("James", 30)
1. [ ] Person()

**Object and class attributes are accessed using dot notation in Python.**

1. [ ] True
1. [ ] False

**A function within a class definition is called a:**

1. [ ] class function
1. [ ] operation
1. [ ] callable
1. [ ] method

**What’s the output of the following program?**

```python
class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"
class GoldenRetriever(Dog):
    def speak(self):
        return "Arff!"

ace = GoldenRetriever()
ace.walk()
```

1. [] Arff!
1. [] AttributeError: 'GoldenRetriever' object has no attribute 'walk'
1. [ ] *walking*
1. [] Woof!

**What’s the output of the following program?**

```python
class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"
class GoldenRetriever(Dog):
    def speak(self):
        return "Arff!"

ace = GoldenRetriever()
ace.walk()
```

1. [ ] Arff!
1. [ ] AttributeError: 'GoldenRetriever' hides method walk.
1. [ ] *walking*
1. [ ] Woof!

**What’s the output of the following program?**

```python
class Dog:
    def walk(self):
        return "*walking*"
    def speak(self):
        return "Woof!"
class GoldenRetriever(Dog):
    def speak(self):
        return "Arff!"

ace = GoldenRetriever()
ace.walk()
```

1. [ ] Arff!
1. [ ] AttributeError: 'GoldenRetriever' hides method walk.
1. [ ] *walking*
1. [ ] Woof!

**What’s the output of the following program?**

```python
class Dog:
    def walk(self):
        return "*walking*"
    def sprint(self):
        return "*running*"
    def speak(self):
        return "Woof!"
class GoldenRetriever(Dog):
    def speak(self):
        return "Arff!"
    def run(self):
        return super().sprint()

ace = GoldenRetriever()
ace.walk()
```

1. [ ] Arff!
1. [ ] AttributeError: 'GoldenRetriever' hides method sprint.
1. [ ] *running*
1. [ ] Woof!
