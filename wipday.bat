@echo off

set DAY=%1

if "%DAY%"=="" goto BadParam

SET "var="&for /f "delims=0123456789" %%i in ("%1") do set var=%%i
if defined var (
	echo Error: Not a number
	goto Done
) else (
	echo.
)

if exist day%DAY%.py (
   git add day%DAY%.py
)

if exist input-day%DAY%.txt (
   git add input-day%DAY%.txt
)

git commit -m "Day %DAY% WIP" > nul
echo Day %DAY% work committed

goto Done

:BadParam
echo Missing parameter

:Done

