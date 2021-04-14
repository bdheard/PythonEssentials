#
# File system Shell methods
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
   
   # duplicate file
   if path.exists("textfile.txt"):
       # get paths to source and destinaton
       file_source = path.realpath("textfile.txt")
       file_destination = file_source + ".bak"

       # create backup copy
       shutil.copy(file_source, file_destination)

       # create backup copy including metadata
       file_destination = file_source + ".bak2"
       shutil.copy(file_source, file_destination)

       # rename file
       if not path.exists("newfile.txt"):
        os.rename("textfile.txt","newfile.txt")

       # compresed directory into zip file
       file_source = path.realpath("textfile.txt.bak")
       root_dir, tail = path.split(file_source)
       shutil.make_archive("archive_dir","zip", root_dir)

       # create custom zip file
       with ZipFile("custom_zip.zip", "w") as newzip:
           newzip.write("textfile.txt")
           newzip.write("textfile.txt.bak")



if __name__ == "__main__":
    main()

