#
# Regex
#


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
