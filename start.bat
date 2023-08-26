@echo off
title Polly
cd %~dp0
pip install discord openai psutil pillow datetime
python loop.py