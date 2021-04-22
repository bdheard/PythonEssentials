#
# Working with the OS
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Print the name of the OS
    print(os.name)

    # Check for if an item exists and what is its type
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Item is a file:" + str(path.isfile("textfile.txt")))
    print("Item is directory:" + str(path.isdir("textfile.txt")))

    # work with file paths
    file_path = str(path.realpath("textfile.txt"))
    print("File path: " + file_path)
    print("File path and name: " + str(path.split(file_path)))


    from pathlib import Path

cwd = Path.cwd()
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# Get the file name
print(demo_file.name)

# Get the extension
print(demo_file.suffix)

# Get the folder
print(demo_file.parent.name)

# Get the size
print(demo_file.stat().st_size)




if __name__ == "__main__":
    main()
