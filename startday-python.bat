@echo off
setlocal enableextensions disabledelayedexpansion

set DAY=%1

if "%DAY%"=="" goto BadParam

SET "var="&for /f "delims=0123456789" %%i in ("%1") do set var=%%i
if defined var (
	echo Error: Not a number
	goto Done
) else (
	echo.
)

if exist python\day%DAY%.py (
	echo File day%DAY%.py already exists !
	goto Done
)

echo Starting Day %DAY%

echo Paste the input data for day %DAY% here > input-day%DAY%.txt

set textfile=template.py.txt
set newfile=python\day%DAY%.py
if exist "%newfile%" del /f /q "%newfile%"

set search={DAY}
set replace=%DAY%

for /F "delims=] tokens=1*" %%a in ('type "%textfile%"^|find /v /n ""') DO (
   set line=%%b
   if defined line (
      setlocal EnableDelayedExpansion
      >> "%newfile%" echo(!line:%search%=%replace%!
      endlocal
   ) else (
      >> "%newfile%" echo(
   )
)

git add python\day%DAY%.py
git add input\input-day%DAY%.txt
git commit -m "Starting day %DAY%" > nul

echo.
echo Created day%DAY%.py, input-day%DAY%.txt
echo.

goto Done

:BadParam
echo Missing parameter

:Done

