# Long Demo - Analysing and Visualising a Dataset

This demo uses an example retail sales dataset included in the workspace. You will use IBM Bob to read and explain the data in plain English, create visual charts, and then plan (and optionally build) an interactive dashboard app. Just follow the steps below.

There is also a completed version of this demo that can be viewed in the Demo folder.

## Opening the Dataset

### Step 1 - Open the dataset folder

In VS Code, go to **File → Open Folder** and open the following folder:

```
Demos/Resources/Datasets
```

This opens the datasets folder as the workspace. Bob can see the CSV directly and will find it automatically when you start prompting.

### Step 2 - Open Bob

Click the Bob icon in the VS Code Activity Bar (the icon panel on the far left). The Bob chat panel will open on the right-hand side of the screen.

## Understanding the Data

In this first part, you will ask Bob to read the dataset and explain what it contains - no jargon, no formulas, just clear business language.

### Step 3 - Explain the data in business language

Type the following prompt into the Bob chat using **Ask** mode and press Enter:

> Analyse the CSV file in this project and explain what it contains in simple business language. Who are the customers, what are they buying, and what does the data tell us about sales performance?

Bob will read the file and return a plain-English summary covering the date range, product categories (Electronics, Clothing, Beauty), customer age groups, sales totals, and any patterns it can identify. You do not need to understand the raw data yourself - Bob translates it into a business-readable narrative.

You can follow up with questions such as:

- Which product category generates the most revenue?
- What age group spends the most on average?
- Are there any seasonal trends in the data?

### Step 4 - Create charts and visualisations

Now ask Bob to turn the data into visual charts directly in the chat. Use this prompt in **Agent** mode:

> Based on this dataset, generate charts showing: (1) total sales revenue by product category, (2) sales volume by month, and (3) a breakdown of purchases by customer age group. Use clear labels and make them easy to read.

Bob will produce interactive charts directly in the chat panel. These are rendered in real time - no spreadsheet software or data tools needed.

Try following up with a customisation request to show how easy it is to iterate:

> Can you show the same category breakdown as a pie chart instead? And highlight which category has the highest average order value.

## Planning an Interactive App

In this second part, you will ask Bob to think like a product designer and plan out a proper interactive application built around this data. This is a great way to show how Bob can bridge the gap between data and a working product concept.

### Step 5 - Plan a dashboard application

Ask Bob to design an app that would make this data accessible and useful for a business user. Switch Bob to **Plan** mode first (click the mode selector above the chat input), then use this prompt in **Plan** mode:

> I want to turn this retail sales data into an interactive dashboard that a non-technical business user could use. Plan out what the application should look like, what features it should have, and how it should be built. Think about things like filters, charts, key metrics, and how users would navigate it.

Bob will respond with a structured plan covering the app's purpose, the key screens or views (e.g. a summary dashboard, a category breakdown page, a trends view), suggested filters (date range, product category, age group), and the key metrics to surface (total revenue, average order value, top-selling category). Plan mode is designed for this kind of structured thinking - Bob will produce a clean, organised output.

## Optional Exercise - Build and Customise the App

This optional section takes the plan from Step 5 and turns it into a real, working application. Switch Bob back to **Agent** mode, then use this prompt:

> Go ahead and build the dashboard application you planned. Create the files, set up the project, and make sure it runs. Use the retail sales CSV as the data source.

Bob will generate all the necessary files - the application code, any configuration, and instructions to run it. Once it is running, try personalising it with a follow-up prompt:

> Update the dashboard to use a dark theme and add a headline card at the top showing total revenue for the year.

There is no single correct outcome here - the goal is to see how quickly Bob can go from a dataset to a running product, and how easy it is to steer the result through natural conversation rather than code changes.

---

## Things to Try

- **Try asking follow-up questions in your own words** - Bob does not need formal language. Anything you would ask a colleague works just as well.
- **Use Plan mode for Step 5** - it produces a structured, readable plan before any code is written.
