@echo off
REM Activation script for Windows
REM Usage: activate_env.bat

echo Activating Python virtual environment...
call venv\Scripts\activate.bat

echo Virtual environment activated!
python --version
pip --version
echo.
echo To deactivate, run: deactivate
echo Current working directory: %cd%