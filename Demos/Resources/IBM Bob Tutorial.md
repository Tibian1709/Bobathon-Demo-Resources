# Getting Started with IBM Bob

**A First-Time User Guide**

*IBM Internal Use | Demo & Workshop Edition*

---

## Table of Contents

1. [What is IBM Bob?](#1-what-is-ibm-bob)
2. [The Chat Interface](#2-the-chat-interface)
3. [Choosing the Right Mode](#3-choosing-the-right-mode)
4. [Giving Bob Context](#4-giving-bob-context)
5. [Slash Commands](#5-slash-commands)
6. [Reviewing Bob's Changes](#6-reviewing-bobs-changes)
7. [Writing Instructions Directly in Your Code](#7-writing-instructions-directly-in-your-code)
8. [Teaching Bob Your Preferences](#8-teaching-bob-your-preferences)
9. [Glossary](#9-glossary)
10. [Where to Learn More](#10-where-to-learn-more)

---

## 1. What is IBM Bob?

IBM Bob is an AI assistant built directly into Visual Studio Code — the code editor used by developers at IBM. Think of it as a knowledgeable colleague you can chat with right inside your editor. You describe what you want in plain English, and Bob reads your code, understands the context, and responds with explanations, suggestions, or changes.

Bob is not a search engine. It does not just look things up — it actually reads and reasons about your project. It can understand files you have never shown it before, trace logic across multiple files at once, and give answers that are specific to your codebase, not generic examples from the internet.

This guide will walk you through the most useful features of Bob, one at a time.

> **Note:** You don't need to be a developer, or have any technical skills to use Bob. Bob is made to be used by anyone with any background.

---

## 2. The Chat Interface

Everything you do with Bob happens through the chat interface — a panel that sits alongside your code in VS Code. You type in a box, Bob responds, and you can have a back-and-forth conversation just like you would with a messaging app.

Here is what each part of the interface does:

1. **Chat History** — The scrollable area at the top of the panel. It shows everything you have typed and everything Bob has replied, including any file changes Bob has made. You can scroll back at any time to review a previous response.
2. **Input Field** — The text box at the bottom of the panel. This is where you type your question or instruction and press Enter to send it. You can type in plain English — you do not need any special commands.
3. **Action Buttons** — Buttons that appear above the input field when Bob proposes a change to your files. They let you approve or reject the change before anything is saved.
4. **Auto-Approve Toolbar** — A row of toggles above the input field. When switched on, they allow Bob to perform certain actions (like reading or editing files) without asking for your approval each time. Leave these off until you are comfortable with how Bob works.
5. **Mode Selector** — A dropdown to the left of the input field. It lets you switch between Bob's different modes (Ask, Plan, and Agent). See Section 3 for a full explanation of each mode.
6. **New Chat Button** — Located in the top-right corner of the Bob panel. Clicking it starts a completely fresh conversation, clearing the history. Use this when you want to move on to a new topic.
7. **Settings Button** — Also in the top-right corner. Opens Bob's settings where you can adjust behaviour, manage modes, and configure rules.

> **Tip:** Start a new chat whenever possible. Bob works best when conversations are focused on one task at a time. A fresh chat also prevents earlier context from confusing later questions and also helps save on your Bob Coin usage.

---

## 3. Choosing the Right Mode

Bob works in three different modes. Each mode is designed for a different kind of task — think of each one as a different hat Bob wears depending on what you need from it. You switch modes using the dropdown to the left of the chat input field.

### Ask Mode

Ask mode is for getting information. Use it whenever you want to understand something — what a piece of code does, how a feature works, or why an error is appearing. In Ask mode, Bob will not make any changes to your files. It will only read them and explain what it finds.

Example prompt you could type in Ask mode:

> What does this file do, and how does it connect to the rest of the application?

### Plan Mode

Plan mode is for thinking and designing. Use it before making any changes when the task is complex or unfamiliar. Bob will produce a structured, step-by-step plan that you can read and agree with before anything is touched. It will not edit any files in this mode.

> **Important:** At first many people assume the plan mode is unnecessary, but by letting Bob set up a plan first is an important step when doing complex tasks. Even though you may already know what you want and how you want it to work, Bob may not interpret your ideas the way you think it will. By setting up a plan first, you can clearly set out your intentions for Bob, and potentially save time and Bob Coins down the line.

Example prompt you could type in Plan mode:

> We need to add a login page to this application. Create a plan for this.

### Agent Mode

Agent mode is for getting things done. Use it when you are ready to make changes — writing new code, fixing a bug, updating a file, or refactoring something. Bob will work through the task step by step, proposing each change for your approval before saving it.

Example prompt you could type in Agent mode:

> Go ahead and implement the plan from the previous conversation.

### Quick Reference

| Mode | Best For | Can It Edit Files? |
|------|----------|--------------------|
| Ask | Getting explanations, understanding code, answering questions | No |
| Plan | Designing a solution or breaking down a complex task before acting | No |
| Agent | Writing code, fixing bugs, making changes to files | Yes — with your approval |

> **Tip:** When in doubt, start with Ask mode. Bob will often suggest switching to Plan or Agent mode when the task calls for it. You can also switch modes at any point mid-conversation.

---

## 4. Giving Bob Context

By default, Bob is aware of all the files in your open project. But sometimes you want to make sure Bob is looking at exactly the right thing — a specific file, a folder, an error message, or even a webpage. You can do this using the `@` symbol in the chat input.

Type `@` in the input field and a menu will appear showing you the available options. Here is a summary of what you can reference:

| What to type | What it includes | Example use |
|--------------|------------------|-------------|
| `@/path/to/file.py` | The full contents of a specific file | `Explain @/src/checkout.py` |
| `@/path/to/folder` | All files directly inside that folder | `Review the code in @/src/utils` |
| `@problems` | Errors and warnings from the Problems panel | `@problems  Fix all the errors in my code` |
| `@terminal` | The most recent output from the terminal | `@terminal  What went wrong?` |
| `@git-changes` | All uncommitted changes in the project | `Summarise @git-changes for a commit message` |
| `@https://example.com` | The contents of a webpage | `Summarise @https://docs.example.com/api` |

> **Tip:** Instead of describing a file in your message, just type `@/` and Bob will suggest matching files from your project. This is faster and more accurate than typing out a description.

> **Note:** When you use `@/folder`, Bob only looks at files directly inside that folder — it does not go into sub-folders automatically. This keeps responses fast and focused.

---

## 5. Slash Commands

Typing a forward slash ( `/` ) in the chat input opens a menu of quick actions — think of them as keyboard shortcuts for common tasks. You do not need to memorise them. Just type `/` and Bob will show you what is available, and you can search by typing part of the command name.

Here are the most useful built-in commands for new users:

| Command | What it does |
|---------|--------------|
| `/review` | Analyses your recent uncommitted changes and flags bugs, security issues, and style problems |
| `/init` | Sets up a `.bob` folder in your project with configuration files — useful when starting with a new codebase |
| `/ask` | Switches Bob to Ask mode (explanations only, no file changes) |
| `/plan` | Switches Bob to Plan mode (structured planning, no file changes) |
| `/agent` | Switches Bob to Agent mode (ready to write code and edit files) |

> **Tip:** You do not need to remember exact command names. Type `/` and start typing — the menu filters as you go. For example, typing `/re` will show `/review` immediately.

---

## 6. Reviewing Bob's Changes

Before Bob saves any change to your files, it will always show you exactly what it plans to do and ask for your approval. You are always in control. Nothing is written to disk without your say-so.

Here is how the process works, step by step:

### Step 1 — Bob proposes a change

After you ask Bob to do something that involves editing a file, Bob works out what needs to change and presents its proposal in the chat. It will show you which files it wants to edit and a summary of what it plans to do.

### Step 2 — A diff view opens in your editor

When Bob edits a file, Bob will open it in the editor and you can see all the proposed changes. Lines highlighted in red are being removed. Lines highlighted in green are being added.

### Step 3 — You approve or reject the change

Action buttons will appear at the top of the Bob panel asking you to **Accept** or **Reject** the change. You can also use keyboard shortcuts: press `Cmd+Enter` (Mac) or `Ctrl+Enter` (Windows) to accept, or press the Reject button to discard the change entirely. If you reject it, your original file is untouched.

### Step 4 — Bob continues

If a task involves multiple files, Bob will show you one change at a time, waiting for your approval before moving on. You remain in control at every step.

> **Important:** Think of the Accept button as your signature on the change. Only click it once you have read what Bob is doing. If something looks wrong, click Reject and ask Bob to explain its reasoning or try again with a clearer prompt.

---

## 7. Writing Instructions Directly in Your Code

Bob has a feature called **Literate Coding** that lets you give it instructions by typing directly inside a file — right where you want the change to happen — instead of switching to the chat panel. This is especially useful for quick, targeted edits when you already know where in the file you want to make a change.

Here is how to use it:

### Step 1 — Open a file

In the VS Code Explorer panel on the left, click any file to open it in the editor. This works with any file type — code, configuration, plain text.

### Step 2 — Turn on Literate Coding

Click the magic wand icon ( the small wand symbol ) in the top-right corner of the editor toolbar. Alternatively, press `Cmd+I` on a Mac or `Ctrl+I` on Windows.

### Step 3 — Type your instruction in plain English

Click into the file at the point where you want the change to happen, then type your instruction in plain English. It can be a comment, a sentence, or even a rough description. Bob will interpret it as an instruction rather than code. The text you type will appear highlighted.

### Step 4 — Press Generate

Press `Cmd+Enter` (Mac) or `Ctrl+Enter` (Windows), or click the **Generate** button that appears at the bottom of the file. Bob will convert your instruction into working code and show you a diff view of exactly what it wants to add or change.

### Step 5 — Accept or reject the change

Review what Bob has produced. Click **Accept All** if you are happy with it, or **Reject** if you want to try again with a clearer instruction. Then click **Exit** (or press `Cmd+I` again) to leave Literate Coding mode.

> **Tip:** Literate Coding is perfect for quick, targeted changes — no need to explain where in the file the change should go. Just click where you want it and describe what you want in plain English.

---

## 8. Teaching Bob Your Preferences

Bob can be given standing instructions that it follows in every conversation — like a permanent sticky note that it reads before responding to anything you say. These instructions are called **rules**.

Rules are plain text files that you can generate, stored in a folder called `.bob` inside your project. Bob reads them automatically at the start of every session. Here are some examples of what teams use rules for:

- **Coding standards** — "Always use double quotes for strings in Python."
- **Communication style** — "Explain every change you make in plain English before making it."
- **Security requirements** — "Never hardcode credentials. Always use environment variables."
- **Team conventions** — "This project uses the Flask framework. Prefer Flask patterns over alternatives."

> **Note:** If your project already has rules set up by your team, Bob is already following them — you do not need to do anything. Rules are a team-level feature that developers configure once and everyone benefits from automatically.

> **Note:** Bob does not set up the `.bob` folder automatically. You will need to create one for every new project or copy over ones from older projects.

---

## 9. Glossary

This glossary explains the key terms used throughout this guide.

**Agent Mode** — The Bob mode used for writing and editing code. In this mode, Bob can create and modify files, with your approval at each step.

**Ask Mode** — The Bob mode used for getting explanations and information. Bob will only read your files — it will not change anything.

**Auto-Approve** — A setting that allows Bob to perform certain actions (such as reading or editing files) without asking for confirmation each time. Best left off until you are comfortable with how Bob works.

**Chat Interface** — The panel inside VS Code where you type messages to Bob and read its responses. Your primary workspace for working with Bob.

**Context Mention** — A way of pointing Bob at a specific file, folder, error, or web page by typing `@` followed by the reference. Gives Bob more accurate context for its responses.

**Diff View** — A side-by-side editor view that shows what Bob wants to change in a file. Red lines show what is being removed; green lines show what is being added.

**Literate Coding** — A feature that lets you type plain-English instructions directly inside a file at the point where you want a change. Bob converts the instruction into real code and shows you a diff before saving.

**Mode** — One of three operational settings for Bob: Ask, Plan, or Agent. Each mode controls what Bob is allowed to do and how it approaches your requests.

**Plan Mode** — The Bob mode used for designing and planning. Bob produces a structured breakdown of how to approach a task without making any file changes.

**Rules** — Plain-text instruction files that Bob reads before every conversation. Used by teams to enforce coding standards, communication preferences, and project conventions.

**Slash Command** — A quick-action shortcut triggered by typing `/` in the chat input. Examples include `/review` to review your changes and `/init` to set up a new project.

**VS Code** — Visual Studio Code, the code editor used at IBM. Bob runs as an extension inside VS Code. If you can see a window with code files, you are already in VS Code.

---

## 10. Where to Learn More

You can learn more about Bob and how to use Bob through IBM's Bob YouTube Channel.

Helpful playlist of videos for getting started with Bob:
[https://www.youtube.com/watch?v=JKnxSiTlvs8&list=PL-aWPAFzESivt1wnV8_OSmp8t1335ahN6](https://www.youtube.com/watch?v=JKnxSiTlvs8&list=PL-aWPAFzESivt1wnV8_OSmp8t1335ahN6)
