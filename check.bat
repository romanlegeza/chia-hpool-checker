@echo off

:1
python checker.py
timeout 3600
goto :1
