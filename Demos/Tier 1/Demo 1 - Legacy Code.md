# Short Demo - Dealing with Legacy Code

This guide walks you through a short, hands-on IBM Bob demo using the example code files included in this workspace, written in COBOL, Java, or RPGL. No setup required — just follow the steps below.

## 1. Opening the Example Code in Bob

### Step 1 - Open the example code

In VS Code, go to **File → Open Folder** and open the following folder:

### Step 2 — Navigate to the example code

In the VS Code Explorer panel (left sidebar), expand the following folder path to find the example files:

```
Demos/Resources/Example Code/COBOL/shamrice - Examples/COBOL-Examples/merge_sort
```

This opens the merge sort project as the workspace, so Bob has direct visibility of its files. Other language examples are also available under the Java and RPGL folders if you'd prefer to use those instead.

### Step 2 - Open the file in the editor

Single-click `merge_sort_test.cbl` in the Explorer panel to open it in the editor. You should see the COBOL source code displayed in the main editor area.

> **Tip:** You can open multiple files using right-click → **Open to the Side** to keep them visible at the same time.

## 2. Starting a Conversation with Bob

### Step 3 - Open Bob

Click the Bob icon in the VS Code Activity Bar (the icon panel on the far left). The Bob chat panel will open on the right-hand side of the screen.

## 3. Example Prompt - Explain This Code

Type the following prompt into the Bob chat using the **Ask** mode input and press Enter:

> Explain this code

Bob will read the COBOL source and return a plain-English explanation covering what the program does, the key data structures, and how the merge sort logic works. This is a good way to demonstrate Bob's ability to understand legacy and mainframe languages instantly.

You can follow up with more specific questions, such as:

- What does the "CopyBooks" section do?
- What are the input and output files in this program?
- Are there any potential issues or improvements in this code?

## 4. Optional Exercises

The following exercises go further and showcase Bob's code modernisation and transformation capabilities. These are optional but recommended for a fuller demo.

### 4.1 — Plan a Migration to Python

Ask Bob in the **Plan** mode to produce a structured migration plan without writing any code yet:

> Create a plan to migrate this program to Python. Identify the key components that need to be re-implemented, any legacy-specific features that have no direct Python equivalent, and suggest a step-by-step approach.

Bob will produce a plan covering data structure mappings, file I/O equivalents, sorting library options (e.g. Python's built-in `sorted()`), and a recommended migration sequence. Review the plan with the audience before proceeding to the next step.

To execute the plan and generate the Python code, follow up in the **Agent** mode with:

> Go ahead and implement the plan.

### 4.2 — Modernise the Code Style

Ask Bob to refactor the COBOL itself to use modern COBOL conventions:

> Refactor this COBOL program to use modern best practices — improve variable naming, remove any redundant paragraphs, and add inline comments explaining each major section.

This demonstrates Bob's ability to improve legacy code quality without changing its behaviour — useful for teams maintaining inherited COBOL codebases.

### 4.3 — Generate Unit Tests

Ask Bob to generate a test plan or test scaffolding for the code:

> Write a set of unit tests for the Python version of this program using pytest. Cover normal sort/merge behaviour, empty file inputs, and duplicate records.

This shows end-to-end modernisation: from legacy → explained → planned → migrated to Python → tested.

### 4.4 — Use the Java Calculator Example

Alternatively, open `CalculatorUI.java` located at:

```
Demos/Resources/Example Code/Java/HouariZegai - Calculator/Calculator/src/main/java/com/houarizegai/calculator/ui/CalculatorUI.java
```

Then try the following prompts as exercises:

- Explain what CalculatorUI does and how the UI is constructed.
- What design patterns are used in this code? Are there any improvements you would suggest?
- Rewrite this class to use JavaFX instead of Swing.

---

## Tips for the Demo

- **Keep it conversational** — Bob is a chat interface, not a form. Follow-up questions work exactly as they would with a colleague.
- **Use Plan mode** — switch Bob to Plan mode for the migration exercise (click the mode selector above the input box) to get a structured multi-step response before generating code.
- **Highlight the speed** — from zero context to a full Python migration plan in seconds is the core value proposition for legacy modernisation.
