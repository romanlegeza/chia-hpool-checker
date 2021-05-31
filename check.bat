@echo off

:1
python checker.py
timeout 6000
goto :1
