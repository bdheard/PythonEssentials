#
# Regex
#

import re

# Search for pattern 
str = 'an example word:cat!!'

match = re.search(r'word:\w\w\w', str)
if match:
    print('found', match.group())
else:
    print('did not find')

# . = any char but \n
match = re.search(r'..g', 'piiig')
match

# Find email address
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print(email)