@echo off

set activateScript=.\env\Scripts\activate.bat

:: Create Python virtual environment
echo Creating Python virtual environment...
python -m venv env
echo Virtual environment created.

:: Install dependencies
>nul find "pip install" %activateScript% || (
    :: Install dependencies
    echo echo Installing dependencies...>> %activateScript%
    echo pip install -r requirements.txt>> %activateScript%
    echo echo Virtual environment set up.>> %activateScript%
    :: Clear screan
    echo cls>> %activateScript%
    :: Run CLI
    echo python cli.py>> %activateScript%
    :: Deactivate virtual environment on exit
    echo .\env\Scripts\deactivate>> %activateScript%
)

:: Activate virtual environment
%activateScript%