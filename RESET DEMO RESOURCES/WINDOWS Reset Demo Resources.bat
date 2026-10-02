@echo off

REM Navigate to the repo root (one level above this script's folder)
cd /d "%~dp0.."

echo.
echo =========================================
echo    Resetting Demos/Resources/ ...
echo =========================================
echo.

REM Restore all tracked files in Demos/Resources/ to their last committed state
git restore --source=HEAD --staged --worktree -- "Demos/Resources/"

REM Remove any untracked or generated files (including __pycache__)
git clean -fdx "Demos/Resources/"

echo.
echo =========================================
echo    Done! Demos/Resources/ has been reset.
echo =========================================
echo.

pause
