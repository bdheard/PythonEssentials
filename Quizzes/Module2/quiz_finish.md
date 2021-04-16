### A. Python Lists

```python
xs = [1,2,3]
xs.append(7)
print(sum(xs))
```

What gets printed?

1. [ ] It's impossible to know.
1. [x] 13
1. [ ] Something else.


### B. Python Lists and Default Arguments

```python
def take_default_list(xs = []):
    xs.append(7)
    return sum(xs)
```

What is the output of ``take_default_list([1,2,3])``?

1. [ ] It's impossible to know.
1. [ ] 13
1. [ ] Something else.