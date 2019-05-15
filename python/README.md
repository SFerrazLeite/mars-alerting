python
======

1. Make sure you have Python > 3.6.X installed on your system ```python --version```
2. ```python -m venv .venv``` -- creates a local virtual environment
3. Activate venv:
 | Platform	| Shell	| Command to activate virtual environment |
 | Posix	| bash/zsh	| $ source <venv>/bin/activate |
 |          | fish	    | $ . <venv>/bin/activate.fish |
 |          | csh/tcsh	| $ source <venv>/bin/activate.csh |
 | Windows	| cmd.exe	| C:\> <venv>\Scripts\activate.bat |
 | 	        | PowerShell | PS C:\> <venv>\Scripts\Activate.ps1 |
4. ```python -m pip install -U pip setuptools```
5. ```pip install -r requirements.txt```
6. You can then run your app during development with `adev runserver app`

Routes are set up in the `main.py`, whereas the endpoints are implemented in the `views.py` module.

Once the dev server is running, you can open 
* http://localhost:8000/ to see a working html page.
* http://localhost:8000/json to see a working REST call.
