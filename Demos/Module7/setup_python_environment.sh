# stops the execution of a script if a command or pipeline has an error 
# which is the opposite of the default shell behaviour, which is to ignore errors in scripts.
set -e

# Install virtualenv globally
pip install virtualenv

# To create a virtual environment, use the following command, where ".venv" is the name of the environment folder:
python -m venv .venv

#https://code.visualstudio.com/docs/python/environments

# activate virtual environment within the terminal
.\.venv\Scripts\activate.ps1

# when you want to write to a file your packages you have installed already so you can re-install them automaticall in another computer.
python -m pip freeze > requirements.txt
