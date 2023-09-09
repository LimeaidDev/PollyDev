@echo off
cd %~dp0
@echo off
set env_folder=venv

REM --add the following to the top of your bat file--


@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
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
start ui.vbs