# Reset Demo Resources — Plan

## Overview

Create a double-click reset script (one for macOS, one for Windows) that restores the `Demos/Resources/` folder to its last committed Git state. The scripts live in a new top-level folder called `RESET DEMO RESOURCES/`. Presenters run the appropriate script after each demo session to wipe any changes participants may have made inside the Resources folder.

The reset uses `git restore` (modern Git syntax) to restore tracked files and `git clean -fdx` to remove any untracked or generated files (e.g. new files, `__pycache__`). Scope is strictly limited to `Demos/Resources/` — nothing outside that path is touched.

---

## Sub-Tasks

### Sub-Task 1 — Create macOS reset script

**Intent:** Provide a double-clickable `.command` file that macOS Terminal can open and execute.

**Expected Outcomes:**
- `RESET DEMO RESOURCES/Reset Demo Resources.command` exists
- Double-clicking it in Finder opens Terminal, runs the restore, prints a success message, and waits for the user to press Enter before closing
- The `cd` uses a path relative to the script's own location so it works on any machine regardless of where the repo is cloned

**Todo List:**
1. Create folder `RESET DEMO RESOURCES/`
2. Create `Reset Demo Resources.command` with the following logic:
   - `cd` to the repo root using `$(dirname "$0")/..`
   - Print a header message
   - Run `git restore --source=HEAD --staged --worktree -- "Demos/Resources/"`
   - Run `git clean -fdx "Demos/Resources/"`
   - Print a success message
   - `read -p` pause so Terminal stays open until the user presses Enter
3. The file must have the execute bit set (`chmod +x`) — note this for the agent: use `execute_command` to set it after creation

**Relevant Context:**
- Repo root is one level above the `RESET DEMO RESOURCES/` folder
- macOS `.command` files open in Terminal.app on double-click only if they are marked executable
- `git clean -fdx` removes untracked files AND ignored files (like `__pycache__`) — the `x` flag is intentional to clean Python cache artefacts

**Status:** [x] done

---

### Sub-Task 2 — Create Windows reset script

**Intent:** Provide a double-clickable `.bat` file for Windows users.

**Expected Outcomes:**
- `RESET DEMO RESOURCES/Reset Demo Resources.bat` exists
- Double-clicking it opens a Command Prompt window, runs the restore, prints a success message, and pauses so the window stays open for the user to read

**Todo List:**
1. Create `Reset Demo Resources.bat` in the same folder with the following logic:
   - Use `%~dp0..` to `cd` to the repo root (works regardless of clone location)
   - Print a header message using `echo`
   - Run `git restore --source=HEAD --staged --worktree -- "Demos/Resources/"`
   - Run `git clean -fdx "Demos/Resources/"`
   - Print a success message
   - `pause` so the window stays open

**Relevant Context:**
- `%~dp0` expands to the directory of the `.bat` file itself — `%~dp0..` navigates one level up to the repo root
- No execute bit is needed on Windows; `.bat` files are executable by default
- Git must be installed and on the system PATH for the script to work (standard assumption for this project)

**Status:** [x] done

---

### Sub-Task 3 — Add README for presenters

**Intent:** Give presenters a one-line explanation of what the scripts do and when to run them.

**Expected Outcomes:**
- `RESET DEMO RESOURCES/README.md` exists with brief, non-technical instructions

**Todo List:**
1. Create `README.md` in `RESET DEMO RESOURCES/` explaining:
   - What the scripts do (reset `Demos/Resources/` to its clean state)
   - When to run them (after each demo session)
   - Which file to use per OS (`.command` for macOS, `.bat` for Windows)
   - That Git must be installed for the scripts to work

**Status:** [x] done
