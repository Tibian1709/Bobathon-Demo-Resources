# Plan: IBM Bob First-Time User Tutorial Document

## Top-Level Overview

**Goal:** Produce a polished, IBM-branded `.docx` tutorial document aimed at first-time Bob users with little or no technical background. The document will be used in demos and workshops where the audience is mixed (technical and non-technical). It is a **feature reference** — each Bob capability gets its own clearly labelled section with a short plain-language explanation, a practical example, and callout boxes (Tips/Notes). Screenshot placeholders are included throughout. A glossary section is included at the end.

**Format:** Microsoft Word (.docx), IBM blue colour scheme, IBM logo in the header, professional footer.

**Scope:** Chat interface → Modes → Context Mentions → Slash Commands → Approving/Rejecting Changes → Literate Coding → Auto-Approve → Rules & Memory. Plus a cover page, introduction, glossary, and a "Where to Learn More" closing section.

**Out of scope:** Deep configuration (MCP servers, custom modes/skills, hooks), CLI/shell variant of Bob, advanced topics like orchestrator or custom mode creation.

---

## Sub-Tasks

### Sub-Task 1 — Document Skeleton & IBM Branding

**Intent:** Create the base `.docx` file with IBM branding so all later content is added into an already-styled shell.

**Expected Outcomes:**
- A `.docx` file exists at `Demos/Resources/IBM Bob Tutorial.docx`
- Document has a cover page: IBM logo placeholder, document title "Getting Started with IBM Bob", subtitle "A First-Time User Guide", and a version/date line
- IBM blue (`#0043CE`) is applied to headings
- A header on every interior page showing "IBM Bob — Getting Started Guide"
- A footer on every interior page showing "IBM Confidential / Internal Use" and a page number
- A Table of Contents page (as a placeholder/list — Word can auto-generate TOC later)

**Todo List:**
1. Use `office_edit` batch to create the `.docx` with a cover page shape (title, subtitle, date) and a second page (TOC stub)
2. Set heading styles to IBM blue for H1 and H2
3. Add header and footer text

**Relevant Context:**
- Target path: `Demos/Resources/IBM Bob Tutorial.docx`
- IBM blue hex: `#0043CE`
- Use `office-insights` skill before editing

**Status:** [ ] pending

---

### Sub-Task 2 — Introduction Section

**Intent:** Orient the reader — what Bob is, why it exists, and what this document covers. Written in plain language for a non-technical reader.

**Expected Outcomes:**
- Section titled "What is IBM Bob?"
- 2–3 short paragraphs explaining Bob as an AI coding assistant built into VS Code, how it understands natural language, and that it helps with tasks like understanding code, planning changes, and writing new code
- A "Note" callout box: "You don't need to be a developer to use Bob. This guide will walk you through everything step by step."
- A screenshot placeholder labelled `[SCREENSHOT: Bob panel open inside VS Code]`

**Todo List:**
1. Add the "What is IBM Bob?" H1 heading and introductory body paragraphs
2. Insert a styled "Note" callout box paragraph
3. Insert a screenshot placeholder paragraph

**Relevant Context:**
- Source: Bob documentation — "Welcome to IBM Bob > Key capabilities"
- Tone: Plain language, welcoming, no assumed technical knowledge

**Status:** [ ] pending

---

### Sub-Task 3 — The Chat Interface Section

**Intent:** Explain the core UI components a user will interact with every time they use Bob.

**Expected Outcomes:**
- Section titled "The Chat Interface"
- Labelled list of all key UI components: Chat history, Input field, Action buttons, Auto-approve toolbar, Slash commands, Send button, New chat button, Settings button, Mode selector
- Each component gets a one-sentence plain-language description
- A "Tip" callout: "Start every new topic with the New Chat button to keep Bob focused on one task at a time."
- Screenshot placeholder: `[SCREENSHOT: Annotated chat interface with callouts for each component]`

**Todo List:**
1. Add "The Chat Interface" H1 heading
2. Add a labelled list (bold term + plain description) for all 9 components
3. Insert Tip callout and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Chat interface > Components of the chat interface"

**Status:** [ ] pending

---

### Sub-Task 4 — Modes Section

**Intent:** Explain Bob's three built-in modes in plain language so users know when to use each one.

**Expected Outcomes:**
- Section titled "Choosing the Right Mode"
- Brief intro paragraph: "Bob works in different modes depending on what you need to do. Think of each mode like a different hat Bob wears."
- Three sub-sections (H2): **Ask Mode**, **Plan Mode**, **Agent Mode** — each with: what it does, when to use it, one example prompt in a styled box
- A simple visual comparison table: Mode | Best For | Can Edit Files?
- A "Tip" callout: "When in doubt, start in Ask mode. Bob will suggest switching when you're ready to make changes."
- Screenshot placeholder: `[SCREENSHOT: Mode selector dropdown in the chat interface]`

**Todo List:**
1. Add "Choosing the Right Mode" H1 and intro paragraph
2. Add three H2 sub-sections with descriptions and example prompts
3. Add a comparison table
4. Insert Tip callout and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Best practices > Understanding and using modes > Built-in modes", "Modes > Comparing the built-in modes"
- Three modes: Agent (write/modify code), Plan (design/plan), Ask (explain/answer)

**Status:** [ ] pending

---

### Sub-Task 5 — Context Mentions Section

**Intent:** Show users how to point Bob at specific files, folders, errors, or URLs so it can give more relevant answers.

**Expected Outcomes:**
- Section titled "Giving Bob Context"
- Plain-language intro: "You can tell Bob exactly what to look at by using the @ symbol in the chat."
- A table of mention types: Type | What to type | What it does | Example
  - Rows: File, Folder, Problems, Terminal, Git Changes, URL
- A "Tip" callout: "Instead of copying and pasting code into the chat, just type @/path/to/your/file — Bob will read it automatically."
- A "Note" callout: "Folder mentions only include files directly inside the folder — they don't go into sub-folders."
- Screenshot placeholder: `[SCREENSHOT: @ mention dropdown appearing in the chat input field]`

**Todo List:**
1. Add "Giving Bob Context" H1 and intro paragraph
2. Add the mentions reference table
3. Insert both callout boxes and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Context mentions > Types of mentions"
- Mention types: `@/file`, `@/folder`, `@problems`, `@terminal`, `@git-changes`, `@https://...`

**Status:** [ ] pending

---

### Sub-Task 6 — Slash Commands Section

**Intent:** Introduce the `/` command system and highlight the most useful built-in commands for new users.

**Expected Outcomes:**
- Section titled "Slash Commands"
- Plain-language intro: "Typing a forward slash / in the chat opens a menu of quick actions — like keyboard shortcuts for common tasks."
- A short table of key built-in commands: Command | What it does
  - Rows: `/review`, `/init`, `/mode ask`, `/mode plan`, `/mode agent`
- A "Tip" callout: "Type / and start typing to search — you don't need to remember the exact command name."
- Screenshot placeholder: `[SCREENSHOT: Slash command menu open with /review highlighted]`

**Todo List:**
1. Add "Slash Commands" H1 and intro paragraph
2. Add the commands reference table
3. Insert Tip callout and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Slash commands > Built-in commands", "Chat interface > Slash commands"
- Key commands: `/review`, `/init`, `/mode <slug>`

**Status:** [ ] pending

---

### Sub-Task 7 — Approving and Rejecting Changes Section

**Intent:** Explain the approval workflow so users understand they are always in control and Bob cannot change their files without permission.

**Expected Outcomes:**
- Section titled "Reviewing Bob's Changes"
- Plain-language intro: "Before Bob edits any file, it shows you exactly what it plans to do and asks for your approval."
- Numbered step-by-step walkthrough: Bob proposes a change → A diff view appears (red = removed, green = added) → Click Accept or Reject → Change is applied or discarded
- A "Warning" callout (styled distinctly): "Think of the Approve button as your signature. Only click it when you have read what Bob is about to do."
- Screenshot placeholder: `[SCREENSHOT: Bob diff view showing red/green changes with Accept/Reject buttons]`

**Todo List:**
1. Add "Reviewing Bob's Changes" H1 and intro paragraph
2. Add numbered approval workflow steps
3. Insert Warning callout and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Chat interface > Action buttons", "Auto-approve > Available actions"
- Keyboard shortcuts: Cmd+Enter (accept), Cmd+Shift+Backspace (reject) on Mac

**Status:** [ ] pending

---

### Sub-Task 8 — Literate Coding Section

**Intent:** Introduce literate coding as a way to give Bob instructions directly inside a file, without using the chat.

**Expected Outcomes:**
- Section titled "Writing Instructions Directly in Your Code (Literate Coding)"
- Plain-language intro: "Instead of describing a change in the chat, you can write a plain-English instruction directly in your file and Bob will turn it into real code."
- Step-by-step numbered instructions:
  1. Open a file in the editor
  2. Click the magic wand icon (or press Cmd+I / Ctrl+I) to turn on Literate Coding
  3. Type your instruction in plain English — it appears highlighted in blue
  4. Press Cmd+Enter or click Generate
  5. Review the diff, then Accept or Reject
- A "Tip" callout: "Great for quick, targeted changes — no need to describe where in the file the change should go."
- Screenshot placeholder: `[SCREENSHOT: Literate coding mode active with blue-highlighted instruction in editor]`

**Todo List:**
1. Add "Writing Instructions Directly in Your Code" H1 and intro
2. Add numbered steps list
3. Insert Tip callout and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Literate coding > Getting started > Basic usage", quickstart tutorial
- Shortcut: Cmd+I (Mac) / Ctrl+I (Windows) to toggle; Cmd+Enter to generate/accept

**Status:** [ ] pending

---

### Sub-Task 9 — Rules & Memory Section

**Intent:** Briefly explain that Bob can be given standing instructions it follows in every conversation, without this being overly technical.

**Expected Outcomes:**
- Section titled "Teaching Bob Your Preferences (Rules)"
- Plain-language description: "Rules are like a sticky note you leave for Bob — instructions it reads before every conversation."
- Two use-case bullets: team coding standards, personal communication preferences
- A "Note" callout: "If your team has already set up rules, Bob is already following them — you don't need to do anything."
- No step-by-step setup instructions (out of scope for non-technical audience)
- Screenshot placeholder: `[SCREENSHOT: .bob/rules folder in the VS Code file explorer]`

**Todo List:**
1. Add "Teaching Bob Your Preferences" H1, intro, and use-case bullets
2. Insert Note callout and screenshot placeholder

**Relevant Context:**
- Source: Bob docs — "Standardize Bob's behavior", "Custom rules > Adding custom rules"
- Rules live in `.bob/rules/` in the project folder

**Status:** [ ] pending

---

### Sub-Task 10 — Glossary & Where to Learn More Section

**Intent:** Provide a reference glossary for non-technical readers, and a closing section pointing to further learning.

**Expected Outcomes:**
- Section titled "Glossary"
- Definitions for: Agent Mode, Ask Mode, Plan Mode, Auto-Approve, Chat Interface, Context Mention, Diff View, Literate Coding, Mode, Rules, Slash Command, VS Code
- Section titled "Where to Learn More"
- Three bullet links (as styled text since hyperlinks in .docx may not render in all print contexts):
  - IBM Bob Documentation: `https://ibm.com/docs/bob`
  - Bob Quickstart Tutorial
  - IBM Bob Tutorial Series (Galaxium Travels)

**Todo List:**
1. Add "Glossary" H1 with all 12 term/definition pairs as a definition list or table
2. Add "Where to Learn More" H1 with three bulleted resource entries

**Relevant Context:**
- Keep definitions under 25 words each — plain language, no jargon

**Status:** [ ] pending

---

## Document Section Order (Final)

1. Cover Page
2. Table of Contents (stub)
3. What is IBM Bob?
4. The Chat Interface
5. Choosing the Right Mode
6. Giving Bob Context
7. Slash Commands
8. Reviewing Bob's Changes
9. Writing Instructions Directly in Your Code (Literate Coding)
10. Teaching Bob Your Preferences (Rules)
11. Glossary
12. Where to Learn More

---

## Design Decisions

- **Callout box styles:** Three types — Tip (blue background), Note (light grey background), Warning (amber/yellow background). Implemented as styled paragraph blocks with bold labels.
- **Screenshot placeholders:** Formatted as a shaded paragraph with italic text, e.g., `[SCREENSHOT: description]`, so they are visually distinct and easy to find-and-replace later.
- **Tone:** Plain language throughout. Technical terms are explained the first time they appear and included in the Glossary.
- **IBM branding:** IBM Blue (#0043CE) for headings and callout borders. IBM logo on cover page as a placeholder text `[IBM LOGO]` since the actual logo file is not available programmatically.
- **Page setup:** A4 or Letter, with 2.5 cm / 1 inch margins.
