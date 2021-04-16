import os
import runpy

path = r'Demos'

#python_file = 'C:/src/GIT/PythonEssentials/async_finish.py'
#runpy.run_path(python_file)

for (path, dirs, files) in os.walk(path):

    python_files = [file for file in files if file.endswith(".py")]
    
    for python_file in python_files:
        runpy.run_path(os.path.join(path, python_file))
