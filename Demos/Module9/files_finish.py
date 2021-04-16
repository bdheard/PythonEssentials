#
# Files
#

# open a file for writing and create it if doesn't exist
f = open("textfile.txt", "w+")

# write to file
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")

# close the file
f.close()

# open the file for appending text to the end 
f = open("textfile.txt", "a")

# write additional data to file
for i in range(10):
    f.write("This is line " + str(i) + "\r\n")

f.close()

# open a file for reading if it was opened successfully the whole thing in one go
f = open("textfile.txt", "r")

if f.mode == "r":
    content = f.read()
    print(content)

# read one line at a time
print("Read one line at a time")
f = open("textfile.txt", "r")
if f.mode == "r":
    lines = f.readlines()
    for line in lines:
        print(line)
