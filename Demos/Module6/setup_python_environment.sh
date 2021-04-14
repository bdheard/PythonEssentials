# stops the execution of a script if a command or pipeline has an error 
# which is the opposite of the default shell behaviour, which is to ignore errors in scripts.
set -e

#To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:
python -m venv .venv

#https://code.visualstudio.com/docs/python/environments

.\.venv\Scripts\activate

python -m pip freeze > requirements.txt
