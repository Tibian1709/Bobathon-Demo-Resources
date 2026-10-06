# Short Demo — Vehicle Service Tracker

This demo uses the Vehicle Service Tracker — a zero-dependency, single-page web app for tracking WOF, rego, service intervals, and fuel fill-ups for two vehicles (a HiAce and a Polo). Everything lives in the browser's `localStorage`; there is no backend, no database, and no API keys. Open the file in a browser and you are ready to go.

This is an ideal Bob demo because the entire scope fits in one HTML file. You can use **Plan** mode to design the data model, **Agent** mode to build it, and then watch Bob test its own output end-to-end — all in under 10 minutes.

---

## Opening the App

### Step 1 — Open the project folder

In VS Code, go to **File → Open Folder** and open:

```
Demos/Resources/Vehicle Tracker/
```

### Step 2 — Open the app in a browser

Right-click `index.html` in the VS Code Explorer and select **Open with Live Server**, or just double-click the file to open it directly in your default browser. No build step or server is needed.

### Step 3 — Open Bob

Click the Bob icon in the VS Code Activity Bar. With the folder open, Bob has full visibility of `index.html` and can navigate it on its own.

---

## Exercises

The following exercises are designed to be run in sequence. Each one demonstrates a different IBM Bob capability using the same single-file codebase.

### Exercise 1 — Understand the Data Model

Before touching any code, use Bob in **Ask** mode to understand how the app is structured:

> Read `index.html` and explain how the data model works. What gets stored in localStorage, how is it structured, and how does the app calculate fuel economy?

Bob will trace the `STORE_ENTRIES` and `STORE_FUEL` keys, describe the shape of each record, and explain the L/100km calculation across sequential odometer readings. This demonstrates Bob's ability to read and reason across a non-trivial block of vanilla JavaScript with no external dependencies.

---

### Exercise 2 — Scope a New Feature in Plan Mode

Switch Bob to **Plan** mode and ask it to design an extension before writing a single line of code:

> I want to add a mileage-based service reminder. When the current odometer reading is within 500 km of the service interval, it should appear in the due-soon banner alongside date-based reminders. Plan how you would implement this without changing the existing data structure.

Bob will produce a structured plan covering: where the odometer data already lives, how to compute the km-remaining figure, and exactly which render functions need updating. Review the plan with the audience, then switch to **Agent** mode and follow up with:

> Go ahead and implement the plan.

This exercise shows the Plan → Agent workflow: design first, then generate code with confidence.

---

### Exercise 3 — Add a Feature

Ask Bob in **Agent** mode to extend the app with a new vehicle:

> Add a third vehicle called "Campervan" to the app. It should appear on the dashboard alongside the HiAce and Polo, and be selectable in both the service entry and fuel fill-up forms.

Bob will locate every place in the code where the vehicle list is defined or iterated and update all of them consistently — the dropdowns, the dashboard render loop, and the fuel stats grid. This demonstrates Bob's ability to make a coherent multi-location change in a dense single-file codebase.

---

### Exercise 4 — Find and Fix a Bug

The fuel economy calculation silently returns `null` if fewer than two fill-ups exist for a vehicle, but the dashboard currently shows `—` (a dash) with no explanation. Ask Bob to improve the user experience:

> The fuel economy display shows "—" when there isn't enough data, but users don't know why. Investigate the `calcEconomy` function and update the dashboard so it shows a short, helpful message instead — for example, "Add 2+ fill-ups to calculate".

Bob will trace the `calcEconomy` return value through to the dashboard render, identify every place `null` is displayed as a dash, and update the copy. This is a small but realistic bug-fix exercise that showcases Bob's ability to follow a value through render logic.

---

### Exercise 5 — Write Tests (Optional)

Ask Bob to write a test plan for the app using a framework of its choice:

> This app has no tests. Write a suite of unit tests for the core logic functions — `daysUntil`, `statusFor`, `calcEconomy`, and the ICS export string. Use whatever test framework you think is most appropriate for a single HTML file with no build system.

Bob will recommend a lightweight approach (typically extracting the pure functions into a separate module and testing with Vitest or plain `<script>`-based assertions), scaffold the test file, and explain how to run it. This shows end-to-end thinking: from a UI-only app to a testable, maintainable codebase.

---

## Tips for the Demo

- **Open the app first** — add a couple of entries and a fuel fill-up before starting so the audience can see the colour-coded banners and economy figures in action.
- **Use Plan mode for Exercise 2** — switching modes mid-demo is a strong visual signal of how Bob changes its behaviour depending on what you need.
- **Highlight the no-backend story** — the entire app, including all data, lives in one HTML file and the browser. There is nothing to deploy, no API keys to manage, and no server to maintain.
- **Export/Import JSON** — demonstrating the backup buttons during the demo shows that "no backend" does not mean "no data safety".
