# Module 1

1. In Python 3, the maximum value for an integer is 263 - 1:

    [X] False
    [] True

1. In Python 3 there is no explicitly defined limit. The only constraint is amount of available address space on machine Python runs on.

1. How would you express the hexadecimal value a5 as a base-16 integer constant in Python?

    [X] 0xa5
    [] a5x0 
    [] 00xa5
    [] 0xaa

Base-16 constant should start with "0x"

1. How would you express the constant floating-point value 3.2 × 10-12 in Python:

[] 3.2 * 10 ** -12
[] 3.2e-12
[] 3.2-12
[] 0.32e-12

We’re looking for a constant value, so an expression like 3.2 * 10 ** -12 would not be a valid answer in this case.

1. Which of the following are valid ways to specify the string literal blue'car in Python:

[X] """blue'car"""
[] 'blue''car'
[X] 'blue\'car'
[X] "blue'car"
[] 'blue'car'

1. Write an expression for a string literal consisting of the following ASCII characters:

Horizontal Tab character
Newline (ASCII Linefeed) character
The character with hexadecimal value 7E

"\t\n\x7E"

'\t' is the escape sequence for the Horizontal Tab character.

'\n' is the escape sequence for the Newline character.

To specify a character by hexadecimal value, use '\xhh', where hh specifies the hexadecimal digits.

Here are a few possible correct answers:

"\t\n\x7E"
'\t\n\x7E'
'''\t\n\x7E'''
"""\t\n\x7E"""

1. Consider this statement:

```python
print(r'blue\\car\nwindow')
```

Which of the following is the correct REPL output?

[] blue\car\nwindow
[] blue\\carwindow
[] blue\car window
[X] blue\\car\nwindow

1. Which of the following is not a Python built-in function:


[] round()
[] repr()
[X] diff()
[] map()
[] isinstance()
