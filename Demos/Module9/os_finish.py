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




if __name__ == "__main__":
    main()
