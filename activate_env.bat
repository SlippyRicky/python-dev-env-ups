@echo off
REM Activation script for Windows
REM Usage: activate_env.bat

echo ╔════════════════════════════════════════════════════════════════════════════╗
echo ║              Python Virtual Environment Activation       ║
echo ╚════════════════════════════════════════════════════════════════════════════╝
echo.

echo ℹ️  Activating Python virtual environment...
call venv\Scripts\activate.bat

if %errorlevel% neq 0 (
    echo ❌  Failed to activate virtual environment.
    echo    Please ensure you have run setup_env.sh first.
    echo.
    pause
    exit /b 1
)

echo ✅  Virtual environment activated!
echo.

echo 🐍 Python Version:
python --version

echo 📦 pip Version:
pip --version

echo.
echo 📌 Current working directory: %cd%
echo.

echo ℹ️  Available commands:
echo    • Run the example: python src\example.py
echo    • Run tests: pytest tests\
echo    • Start Jupyter: jupyter notebook
echo    • Format code: black src\
echo    • Check code style: flake8 src\
echo.

echo ⚠️  To deactivate, run: deactivate
echo.

pause
