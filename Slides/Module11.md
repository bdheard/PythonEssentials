---
title: Lesson 11
subtitle: Python Essentials
---

## Overview

1. Regular Expressions
1. Dates
1. Time Zones
1. Calendar

## Regular Expressions (Regex)

- Finding matches based on sophisticated patterns. 
- Use **re** module. 

| Function | Description                                                       |
|----------|-------------------------------------------------------------------|
| findall  | Returns a list containing all matches                             |
| search   | Returns a Match object if there is a match anywhere in the string |
| split    | Returns a list where the string has been split at each match      |
| sub      | Replaces one or many matches with a string                        |

:::notes
https://docs.python.org/2/library/re.html
:::

## Metacharacters

- Characters with a special meaning

| Character |	Description	                                                     | Example        |
|-----------|--------------------------------------------------------------------|----------------|
| []        | A set of characters	                                             | "[a-m]"	      |
| \	        | Signals a special sequence (use also to escape special characters) | "\d"	          |
| .	        | Any character (except newline character)	                         | "he..o"	      |
| ^	        | Starts with	                                                     | "^hello"	      |
| $	        | Ends with	                                                         | "world$"	      |
| *	        | Zero or more occurrences	                                         | "aix*"	      |
| +	        | One or more occurrences	                                         | "aix+"	      |
| {}        | Exactly the specified number of occurrences	                     | "al{2}"	      |
| |	        | Either or	                                                         | "falls|stays"  |	
| ()        | Capture and group	                                                 |                |

:::notes
https://docs.python.org/2/library/re.html
:::

## Special Sequences

- A special sequence is a **\** followed by one of the characters in the list below.
- Have special meaning.

| Element        | Description                                              |
|:--------------:|:--------------------------------------------------------:|
| .              | This element matches any character except \n             |
| \d             | This matches any digit [0-9]                             |
| \D             | This matches non-digit characters [^0-9]                 |
| \s             | This matches whitespace character [ \t\n\r\f\v]          |
| \S             | This matches non-whitespace character [^ \t\n\r\f\v]     |
| \w             | This matches alphanumeric character [a-zA-Z0-9_]         |
| \W             | This matches any non-alphanumeric character [^a-zA-Z0-9] |

:::notes
https://docs.python.org/2/library/re.html
:::

## Dates

* use the datetime library
* timedelta defines a period of time

```python
from datetime import datetime
current_date = datetime.now()
print('Today is: ' + str(current_date))

from datetime import timedelta
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print ('Birthday: ' + str(birthday_date))

```

::: notes
When displaying a string that contains numbers you must convert the numbers into strings.

Numbers can be stored as stringsNumbers stored as strings are treated as strings.

The input function always returns strings.
:::

## Time Zones

- dateutil includes an interface to the IANA time zone database

```python
from dateutil import tz
from datetime import datetime

datetime.now(tz=tz.UTC)
```
::: notes
:::

## Calendar

- Calendar module outputs calendars. 
- Provides useful functions.

```python
import calendar 
    
yy = 2021
mm = 4
    
# display the calendar 
print(calendar.month(yy, mm)) 
```

::: notes
:::
