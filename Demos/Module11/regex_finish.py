#
# Regex
#

import re

text_to_search = '''
Begining of a sentence.. the Begining

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789

ha haHa

an example word:cat!!cat

MetaCharacters we need to escape
[ ] \ . ^ $ * + { } | ( )

johndoe@microsoft.com
john.doe@duke.edu
johndoe@my-life.net

212--123-4561
212-123-4561
217-888-9123
212.123.4561
217.888.9123

Mr. Doe
Mr Doe
Mr D
Mr. D
Ms Doe
Mrs. Doe
Mrs. D

some things eventually end
'''

# Search for patterns
pattern = re.compile(r'cat')
pattern = re.compile(r'.')
pattern = re.compile(r'\.')
pattern = re.compile(r'\D')
pattern = re.compile(r'\w')
pattern = re.compile(r'\W')
pattern = re.compile(r'\s')
pattern = re.compile(r'\S')
pattern = re.compile(r'^Begining')
pattern = re.compile(r'end$')
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') # [] or just one character
pattern = re.compile(r'\d\d[27][-.]\d\d\d[-.]\d\d\d\d') # [] or just one character
pattern = re.compile(r'\d\d[27][-.]\d\d\d[-.]\d\d\d\d') # [] or just one character
pattern = re.compile(r'[a-z]')
pattern = re.compile(r'[a-zA-Z]')
pattern = re.compile(r'[^a-zA-Z]') # ^ not
pattern = re.compile(r'Mr[a-zA-Z]')
pattern = re.compile(r'Mr[^s]') # match any single characcter that it isn't a s
pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}') # quantifier
pattern = re.compile(r'Mr\.?\s[A-Z]\w*') # match prefix and entire name
pattern = re.compile(r'M(r|s|rs)?\.?\s[A-Z]\w*') # group
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') # emails
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)') # emails handle dots and edu
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') # handlde - and net



matches = pattern.finditer(text_to_search)
print(matches)
for match in matches:
    print(match)

#matches_all = pattern.findall(test_to_search)
#print(matches_all)



'''
| .             | matches any character except n                     |
| d             | matches any digit [0-9]                             |
| D             | matches non-digit characters [^0-9]                 |
| s             | matches whitespace character (space, tab, new line)          |
| S             | matches non-whitespace character (space, tab, new line)     |
| w             | matches alphanumeric character [a-zA-Z0-9_]         |
| W             | matches any non-alphanumeric character [^a-zA-Z0-9] |

Word Anchors

| Character |	Description	                | Example      |
|-----------|-------------------------------|--------------|
| \b        | Word boundary	                | "\babc"	   |
| \B        | Not a word boundary	        | "\Babc"	   |
| []        | A set of characters	        | "[a-m]"	   |
| \	        | escape special characters     | "\d"	       |
| .	        | Any character (except newline)| "he..o"	   |

Anchors:

| Character |	Description	                | Example      |
|-----------|-------------------------------|--------------|
| ^	        | Starts with	                | "^hello"	   |
| $	        | Ends with	                    | "world$"	   |

Quantifiers:

| Character |	Description	                | Example      |
|-----------|-------------------------------|--------------|
| *	        | Zero or more	                | "aix*"	   |
| +	        | One or more 	                | "aix+"	   |
| ?	        | Zero or One 	                | "aix+"	   |
| {}        | Exact number of occurrences	| "al{2}"	   |

Groups
| |	        | Either or	                    | "falls|stays"|	
| ()        | Capture and group	            |              |
'''
