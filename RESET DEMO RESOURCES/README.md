# Reset Demo Resources

Run this after each demo session to restore the `Demos/Resources/` folder to its clean state, removing any changes or new files created during the session.

## How to use

| Operating System | Script to run |
|---|---|
| macOS | Double-click `Reset Demo Resources.command` |
| Windows | Double-click `Reset Demo Resources.bat` |

A terminal window will open, reset the resources, and wait for you to press Enter before closing.

## What it does

- Restores all files in `Demos/Resources/` to their last committed state
- Removes any new files or folders created during the session
- Clears any Python `__pycache__` folders

**Note:** Git must be installed and available on your system PATH for these scripts to work.
