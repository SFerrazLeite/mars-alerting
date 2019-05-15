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
