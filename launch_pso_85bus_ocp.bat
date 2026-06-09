@echo off
REM Launch the 85-bus PSO Flask application from the project folder.
cd /d "%~dp0"
call "venv\Scripts\Activate.bat"
python web_app.py
pause
