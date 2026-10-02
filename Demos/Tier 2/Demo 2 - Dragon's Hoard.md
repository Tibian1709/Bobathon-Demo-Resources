# Medium Demo - Dragon's Hoard

This demo uses the Dragon's Hoard Shop Manager — a small, intentionally imperfect Python application. Each exercise below uses IBM Bob to investigate, improve, or extend the codebase. Open the project folder before starting.

## Opening the Project

### Step 1 - Open the project

In VS Code, go to **File → Open Folder** and open the following folder:

```
Demos/Resources/Dragon's Hoard/dragon_shop
```

### Step 2 - Open Bob

Click the Bob icon in the VS Code Activity Bar (the icon panel on the far left). The Bob chat panel will open on the right-hand side of the screen. With the folder open, Bob has full visibility of all the project files and can navigate them on its own.

## Exercises

The following five exercises are designed to be run in sequence. Each one demonstrates a different IBM Bob capability using the same codebase.

### Exercise 1 — Find the Bug

The purchase total calculation contains a bug. Rather than telling Bob where it is, ask Bob to investigate the repository and find it. In the **Ask** mode use this prompt:

> The total being calculated for purchases appears to be incorrect. Investigate the repository, identify the cause, and explain the problem to me. Do not modify anything yet.

Bob will trace the calculation logic in `checkout.py`, pinpoint the incorrect branch, and explain why only purchases of three or more units are affected. Once you have reviewed the explanation, follow up in the **Agent** mode with:

> Fix the calculation issue and show me what you changed.

This exercise demonstrates Bob's ability to read and reason across multiple files to locate a non-obvious bug without being told where to look.

### Exercise 2 — Add a Feature

The shop currently has no loyalty discount. Ask Bob to implement a new pricing rule and update the receipt output to match. Use this prompt:

> Add a feature where purchases over $200 receive a 10% Adventurer Discount. The receipt should display the subtotal, discount, and final total.

Bob will identify the checkout and receipt modules, add the discount calculation, and update the printed receipt to show a subtotal, the discount amount, and the final total — without touching unrelated parts of the code.

### Exercise 3 — Refactor a Messy Function

The `do_checkout` function in `checkout.py` works, but it has accumulated several maintainability problems. Ask Bob to analyse and refactor it:

> Analyse the checkout function. It works, but it has become difficult to maintain. Explain the maintainability problems and refactor it without changing its intended behaviour.

Bob will identify issues such as deeply nested conditionals, vague variable names, mixed responsibilities, and repeated logic. It will then produce a refactored version that is functionally equivalent but significantly easier to read and maintain.

### Exercise 4 — Literate Coding

The `get_low_stock_items` function at the end of `checkout.py` contains a detailed docstring describing the requirements, but the implementation is empty. Using the literate coding function — indicated by the magic wand at the top right of the VS Code — ask Bob to implement it from the description alone:

> Implement the low-stock functionality described by the comments and requirements in the source code.

Bob will read the docstring requirements and generate a correct implementation. This demonstrates how well-written natural-language requirements inside source code can drive code generation — a technique sometimes called literate coding.

### Exercise 5 — Documentation Rescue

The README for this project is intentionally minimal. Ask Bob to read the full repository and produce proper documentation:

> Analyse this repository and create proper project documentation. Update the README to explain what the application does, project structure, requirements, how to run it, menu options, inventory storage, and example usage.

Bob will analyse every source file, infer the architecture and data flows, and produce a complete README covering all requested sections. This exercise shows Bob's ability to generate documentation from code alone — no existing docs required.

### Exercise 6 — Turn This Into a Website (Optional)

This optional exercise shows how Bob can take an application and plan — or even begin building — a web version of it. It is a strong demonstration of Bob's ability to reason about architecture and transformation at scale. Ask Bob:

> Turn this terminal application into a website. Suggest an appropriate Python web framework, describe how you would structure the project, and outline how each part of the existing code would map across to the web version.

Bob will recommend a framework (typically Flask or FastAPI), map the existing modules to routes and templates, and explain how the inventory JSON, checkout logic, and sales history would translate into a web context. You can then follow up with:

> Go ahead and scaffold the project structure and create the first working route.

This exercise has no single correct answer — the value is in watching Bob reason about the transformation from scratch and produce a coherent plan from an unstructured request. From there you can use your creativity to change the designs or functions to however way you can come up with.

---

## Tips for the Demo

- **Run the app first** — before starting, run `python main.py` from the `dragon_shop` folder to show what the application looks like at the terminal.
- **Do the exercises in order** — each exercise builds on or complements the previous one, and the bug fix in Exercise 1 is required before demonstrating the discount feature in Exercise 2.
