# Module 7 Quiz

**Given the file dog_breeds.txt, which of the following is the correct way to open the file for reading as a text file? Select all that apply.**

1. [ ] open('dog_breeds.txt', 'wb')
1. [X] open('dog_breeds.txt')
1. [X] open('dog_breeds.txt', 'r')
1. [ ] open('dog_breeds.txt', 'rb')
1. [ ] open('dog_breeds.txt', 'w')

**Explanation:**

Consider using the second positional argument, mode. This argument is a string that contains multiple characters to represent how you want to open the file. The default and most common is 'r', which represents opening the file in read-only mode as a text file.


**Whenever possible, what is the recommended way to ensure that a file object is properly closed after usage?**

1. [ ] It doesn’t matter
1. [ ] By using the try/finally block
1. [ ] Making sure that you use the .close() method before the end of the script
1. [X] By using the with statement

**Explanation:**
While the try/finally block is a valid way to ensure that the file is properly closed, it is still recommended to use the with statement because of its readability and ease of use to new users.


**When reading a file using the file object, what method is best for reading the entire file into a single string?**

1. [ ] .read_file_to_str()
1. [ ] .readline()
1. [X] .read()
1. [ ] .readlines()

**Explanation:**
The .read_file_to_str() is not a method of the builtin file object. The easiest option is to use the .read() method. If you pass in a integer value, the entire file is no longer read and instead n number of bytes will be read and returned back, where n is the integer value you passed in.