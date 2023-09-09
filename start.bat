@echo off
set env_folder=venv

rem Check if the Python environment folder exists
if not exist %env_folder% (
    echo Creating Python environment...
    
    rem Create the Python environment (replace this with your actual command)
    python -m venv %env_folder%
)

rem Activate the Python environment (replace this with your activation command)
call %env_folder%\Scripts\activate
pip install discord openai psutil pillow datetime customtkinter aiohttp

rem Your Python script or commands go here
python pollyruntime.py

rem Deactivate the Python environment (optional, depends on your use case)
deactivate