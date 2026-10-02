# Retail Sales Interactive Dashboard — Plan

## Overview

Build a single self-contained `Retail Sales Dashboard.html` file in `Demos/Tier 3/Finished Project Example/`. The file should open directly in any modern browser with no server required. It targets a non-technical business audience, so the experience must be visually polished, intuitive, and "wow-factor" ready for stakeholder demos.

All data is hardcoded from `Demos/Resources/Datasets/Retail Sales Data Set.csv` (1,000 transactions, full-year 2023). The existing `Retail Sales Charts.html` is left untouched.

**Stack:** Single HTML file · ECharts 5.4.3 (CDN) · Vanilla JS · CSS variables for theming

---

## Data Reference

| Dimension | Values |
|---|---|
| Product Category | Electronics, Clothing, Beauty |
| Gender | Male, Female |
| Age Group | Adolescent, Middle Age, Old |
| Date Range | Jan 2023 – Dec 2023 |
| Total Revenue | $456,000 · Avg Order $456 |
| Category Revenue | Electronics $156,905 · Clothing $155,580 · Beauty $143,515 |
| Monthly Units | Jan 199, Feb 214, Mar 194, Apr 214, May 259, Jun 197, Jul 176, Aug 227, Sep 170, Oct 252, Nov 205, Dec 207 (Total 2,514) |
| Age Group Units | Middle Age 1,254 · Adolescent 745 · Old 515 |
| Gender Split | 51% Male / 49% Female (approx, from raw data) |

---

## Sub-Tasks

---

### Sub-Task 1 — Page Shell and Design System

**Status:** [x] done

**Intent:**
Establish the visual foundation — layout grid, color palette, typography, and CSS variables — that all subsequent components will build on. Getting this right first means every widget and chart feels cohesive without per-component styling work.

**Expected Outcomes:**
- A responsive full-screen layout with a left sidebar (filters) and a main content area.
- A **light theme** with a clean white/off-white page background and light-grey card surfaces.
- IBM-inspired accent colours used for highlights, active states, and chart series.
- **Glassy "Windows Aero" style** for filter chips and interactive buttons: frosted-glass appearance using `backdrop-filter: blur()`, semi-transparent backgrounds, subtle inner-highlight border on top edge, and soft box-shadow.
- CSS custom properties for all colors, spacing, and shadow tokens.
- A top header bar with dashboard title, subtitle, and a "last updated" badge.

**Colour Palette:**

| Token | Value | Usage |
|---|---|---|
| `--bg` | `#f4f6fb` | Page background |
| `--surface` | `#ffffff` | Card / sidebar background |
| `--surface-glass` | `rgba(255,255,255,0.55)` | Glassy chip / button base |
| `--border` | `#dde1ea` | Card and sidebar borders |
| `--text-primary` | `#161616` | IBM Carbon near-black |
| `--text-muted` | `#6f6f6f` | Secondary labels |
| `--ibm-blue` | `#0f62fe` | Primary accent, active chips |
| `--ibm-red` | `#da1e28` | Danger / negative indicators |
| `--ibm-green` | `#24a148` | Positive / success indicators |
| `--ibm-yellow` | `#f1c21b` | Warning / highlight indicators |
| `--ibm-teal` | `#009d9a` | Chart series 2 |
| `--ibm-purple` | `#8a3ffc` | Chart series 3 |

**Todo List:**
1. Create `Retail Sales Dashboard.html` with valid HTML5 boilerplate.
2. Include the ECharts CDN script tag.
3. Define all CSS variables from the palette table above.
4. Build a two-column layout: fixed 240px left sidebar + flexible main content area.
5. Add a top header bar spanning the full width with title "Retail Sales Dashboard", subtitle "Full-Year 2023 · 1,000 Transactions", and a styled "2023" badge.
6. Define a reusable `.glass` CSS class: `background: rgba(255,255,255,0.55); backdrop-filter: blur(12px) saturate(180%); -webkit-backdrop-filter: blur(12px) saturate(180%); border: 1px solid rgba(255,255,255,0.7); border-top-color: rgba(255,255,255,0.9); box-shadow: 0 2px 12px rgba(0,0,0,0.10), inset 0 1px 0 rgba(255,255,255,0.8);` — this is the core Aero effect applied to chips, the sidebar, and the header.
7. Add a footer with "Made with IBM Bob".

**Relevant Context:**
- ECharts 5.4.3 from `https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js`.
- The Aero glass effect requires a visible background layer beneath the element to show the blur; a subtle gradient or frosted-glass texture on `--bg` helps.

---

### Sub-Task 2 — KPI Metric Cards

**Status:** [x] done

**Intent:**
Give business users an immediate at-a-glance summary of the most important numbers before they touch any chart or filter. KPI cards are the first thing eyes go to in a dashboard and set the "wow" impression.

**Expected Outcomes:**
- A row of 4 KPI cards pinned below the header in the main content area.
- Each card shows: icon, label, primary value, and a short supporting note.
- Cards animate in (fade + slide up) on page load.

**Cards to build:**

| Icon | Label | Value | Note |
|---|---|---|---|
| 💰 | Total Revenue | $456,000 | FY 2023 |
| 🛒 | Total Transactions | 1,000 | All categories |
| 📦 | Units Sold | 2,514 | Across 3 categories |
| 💵 | Avg Order Value | $456 | Per transaction |

**Todo List:**
1. Create a `.kpi-row` container with CSS Grid (4 equal columns, 16px gap).
2. Style each `.kpi-card` with rounded corners, white surface background, `1px solid var(--border)` border, soft `box-shadow`, and a left-side accent stripe (4px wide) in the card's assigned IBM colour.
3. Assign accent colours: Revenue → `--ibm-blue`, Transactions → `--ibm-teal`, Units Sold → `--ibm-green`, Avg Order → `--ibm-yellow`.
4. Add a CSS keyframe `fadeSlideUp` animation triggered on page load with staggered delays (0ms, 80ms, 160ms, 240ms).
5. Populate the 4 cards with values above.

**Relevant Context:**
- Values sourced directly from the dataset summary row in the CSV.

---

### Sub-Task 3 — Filter Sidebar

**Status:** [x] done

**Intent:**
Allow business users to slice the data interactively by the three main dimensions. Filters must be visually obvious, feel responsive, and should update all charts and KPI cards simultaneously when applied.

**Expected Outcomes:**
- Left sidebar contains three filter groups: Product Category, Gender, Age Group.
- Each group uses styled toggle/chip buttons (not dropdowns) so all options are always visible.
- An "All" option per group that clears that dimension's filter.
- A "Reset All Filters" button at the bottom of the sidebar.
- Selecting a filter immediately re-renders all 4 charts and recalculates KPI cards based on the filtered dataset.

**Filter Options:**

| Group | Options |
|---|---|
| Product Category | All · Electronics · Clothing · Beauty |
| Gender | All · Male · Female |
| Age Group | All · Adolescent · Middle Age · Old |

**Todo List:**
1. Build a `<nav>` sidebar with a "Filters" heading and three `.filter-group` sections. Apply the `.glass` class to the sidebar panel itself.
2. Style filter chips as pill buttons using the `.glass` class for their base appearance (frosted-glass, semi-transparent). Inactive state: glass bg, `--text-primary` text, soft shadow. Active state: `background: var(--ibm-blue)`, white text, stronger shadow — the Aero "pressed glass" look.
3. Style the "Reset All Filters" button the same way: `.glass` base, red text (`--ibm-red`) on hover to signal a destructive action.
4. Implement JS `activeFilters` object `{ category: null, gender: null, ageGroup: null }`.
5. On chip click: update `activeFilters`, toggle active CSS class, call `applyFilters()`.
6. Write `applyFilters()`: filter the master `transactions` array using `activeFilters`, then call each chart's update function and `updateKPIs()`.
7. Wire "Reset All Filters" to reset `activeFilters` and deselect all chips.

**Relevant Context:**
- The master `transactions` array (built in Sub-Task 5) must be defined at module scope so all filter and chart functions can access it.
- ECharts instances can be updated via `chart.setOption()` with new data — no need to destroy and re-init.

---

### Sub-Task 4 — Chart Suite

**Status:** [x] done

**Intent:**
Replace the static charts from `Retail Sales Charts.html` with fully dynamic versions that re-render based on the active filter state. The four charts cover every key business question from the brief.

**Expected Outcomes:**
- Four charts in the main content area, below the KPI row.
- A 2×2 grid layout with equal-sized chart cards.
- All charts re-render correctly when filters change.
- Smooth ECharts animation on every update.
- Dark-themed axes, tooltips, and legend to match the overall design.

**Charts to build:**

| # | Title | Type | Primary Dimension |
|---|---|---|---|
| A | Revenue by Category | Horizontal bar | Product Category → sum of Total Amount |
| B | Units Sold by Month | Line + area fill | Month → sum of Quantity |
| C | Transactions by Age Group | Donut | Age Group → count of transactions |
| D | Revenue by Gender | Vertical bar | Gender → sum of Total Amount |

**Todo List:**
1. Create a `.charts-grid` CSS Grid (2 columns, equal width, 20px gap) below the KPI row.
2. Add 4 `.chart-card` containers each with a `<h3>` title and a `<div>` chart mount point.
3. Initialize four ECharts instances in JS: `chartCategory`, `chartMonth`, `chartAge`, `chartGender`.
4. Write four render functions: `renderCategoryChart(data)`, `renderMonthChart(data)`, `renderAgeChart(data)`, `renderGenderChart(data)`. Each accepts an already-filtered transactions array, computes aggregations internally, and calls `chart.setOption()`.
5. Style all charts to match the light design system: white/transparent chart background, light-grey gridlines (`#eaedf2`), `--text-primary` axis labels, and IBM accent colours for series fills and lines.
6. Add descriptive tooltips showing both the dimension label and formatted value.
7. Call all four render functions on page load with the full dataset.

**Relevant Context:**
- All four render functions must be callable from `applyFilters()` (Sub-Task 3) with the filtered subset.
- Use the same color palette tokens as in Sub-Task 1.
- Monthly aggregation: group by `Date.getMonth()`, show all 12 months even if count is 0.
- Gender revenue split from raw data: Male ≈ $233,580 · Female ≈ $222,420 (computed from individual transaction rows).

---

### Sub-Task 5 — Embedded Dataset and Wiring

**Status:** [x] done

**Intent:**
Embed the full 1,000-row transaction dataset as a JavaScript array inside the HTML file so the dashboard is truly self-contained with no file-read dependencies. Wire all components together so the page is fully functional on load.

**Expected Outcomes:**
- A `const transactions = [...]` array of 1,000 objects, each with keys: `id`, `date`, `gender`, `age`, `ageGroup`, `category`, `quantity`, `pricePerUnit`, `total`.
- All four charts and KPI cards render correctly on `DOMContentLoaded`.
- Filters update everything correctly.
- Charts resize correctly if the browser window is resized.

**Todo List:**
1. Write a Python script (run once, discard) to parse `Retail Sales Data Set.csv` and emit the JS array literal — only the first 9 columns are needed (skip the summary columns).
2. Paste the generated array into the `<script>` block of the HTML file.
3. On `DOMContentLoaded`: call `applyFilters()` (which internally calls all render functions and `updateKPIs()` with the full unfiltered dataset).
4. Add `window.addEventListener('resize', ...)` to call `.resize()` on all four ECharts instances.

**Relevant Context:**
- Only columns 1–9 of the CSV are needed: Transaction ID, Date, Gender, Age, Age Group, Product Category, Quantity, Price per Unit, Total Amount.
- The summary data in columns 18–24 is redundant — exclude it to keep the embedded JS array clean.
- The generated array will be approximately 80–100 KB of inline JS, which is acceptable for a single-file demo.

---

## File Output

| File | Action |
|---|---|
| `Demos/Tier 3/Finished Project Example/Retail Sales Dashboard.html` | Create (new) |
| `Demos/Tier 3/Finished Project Example/Retail Sales Charts.html` | Leave untouched |
| `Demos/Tier 3/Finished Project Example/retail-sales-dashboard-plan.md` | This file |
