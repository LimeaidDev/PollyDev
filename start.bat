@echo off
cd %~dp0
pip install discord openai psutil
python loop.py