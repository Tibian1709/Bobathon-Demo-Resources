# Ingram Micro Bobathon Demo Strategy & Catalog Plan

## Top-Level Overview

This plan defines a structured catalog of 8 live demo scenarios for the upcoming Ingram Micro Bobathon. The scenarios are structured across three difficulty tiers and tailored to distinct personas ranging from non-technical business/product roles to full-stack engineers and enterprise architects. Each demo includes targeted personas, core Bob features showcased (e.g., natural language document generation, OfficeCLI editing, code explanation, refactoring, test generation, and multi-step architectural planning), prompt templates, and starter assets.

## Tier Breakdown & Persona Alignment

1. **Tier 1: Short & Easy (3 Scenarios) — Business, Product, & Citizen Developers**
   - Focus: Zero-code to low-code productivity, natural language documentation, spreadsheet/deck manipulation via Office tooling, and rapid requirements drafting.
2. **Tier 2: Medium Length (3 Scenarios) — Software Engineers & Full-Stack Developers**
   - Focus: Code explanation, legacy code modernization/refactoring, bug triage, unit test suite generation, and API schema design for distribution/reseller workflows.
3. **Tier 3: Long & In-Depth (2 Scenarios) — Lead Engineers & Enterprise Architects**
   - Focus: End-to-end feature planning and scaffolding, legacy system migration (e.g., monolithic ERP/order service to event-driven microservices), and secure multi-component integration with IBM compliance guardrails.

---

## Sub-Tasks

### Sub-Task 1: Catalog Definition & Demo Guide
- **Intent**: Formulate the full 8-demo catalog document with objectives, persona breakdowns, timing guidelines, live speaker scripts, and key "wow-factor" moments for each scenario.
- **Expected Outcomes**:
  - Comprehensive guide covering all 8 demos with exact step-by-step speaker cues.
  - Clear mapping to Ingram Micro business domains (B2B eCommerce, Cloud Marketplace, Partner Provisioning, ERP integrations).
- **Todo List**:
  - [ ] Detail Tier 1 Demo 1: Executive Summary & Partner Onboarding Brief Generator (`docx`/Markdown).
  - [ ] Detail Tier 1 Demo 2: Reseller Tiering & Margin Calculator with Excel Automation (`xlsx`).
  - [ ] Detail Tier 1 Demo 3: Product Feature Spec & User Story Decomposition from Unstructured Customer Feedback.
  - [ ] Detail Tier 2 Demo 1: Legacy Order Processing Script Refactoring & Python Type-Safety Enhancement.
  - [ ] Detail Tier 2 Demo 2: Automated Unit Testing & Edge-Case Coverage for Inventory Allocation Logic.
  - [ ] Detail Tier 2 Demo 3: OpenAPI / REST API Endpoint Generation & Validation for Partner Catalog Sync.
  - [ ] Detail Tier 3 Demo 1: Full-Stack Cloud Marketplace Subscription Management Feature (Frontend + Backend + DB Migration).
  - [ ] Detail Tier 3 Demo 2: Monolith-to-Microservices Architecture Migration Plan & Scaffold (Event-Driven Order & Shipment Notification Service).
- **Relevant Context**: `docs/bobathon-demo-guide.md`
- **Status**: [ ] pending

### Sub-Task 2: Starter Code & Sample Data Scaffolding
- **Intent**: Create lightweight, runnable starter files, mock data, and broken/legacy code snippets so presenters can run the demos live without friction.
- **Expected Outcomes**:
  - Ready-to-use directory structure under `demos/` organized by tier (`tier-1/`, `tier-2/`, `tier-3/`).
  - Mock datasets (e.g. sample partner lists, catalog orders, legacy order functions) that require zero complex external dependencies.
- **Todo List**:
  - [ ] Scaffold `demos/tier-1/` containing sample feedback text and mock reseller spreadsheet structure.
  - [ ] Scaffold `demos/tier-2/` containing legacy order processing code and un-tested inventory manager.
  - [ ] Scaffold `demos/tier-3/` containing starter architecture specs, monolithic order models, and target microservice definitions.
- **Relevant Context**: `demos/` directory
- **Status**: [ ] pending

### Sub-Task 3: Ready-to-Run Prompt Cheat Sheets & Slide Deck Outline
- **Intent**: Supply copy-paste prompt sequences for live presenters to minimize typing errors and ensure predictable live execution.
- **Expected Outcomes**:
  - Presenter-ready cheat sheet with exact sequential prompts and expected output checkpoints.
  - Bobathon introduction & demo agenda slide outline.
- **Todo List**:
  - [ ] Write prompt copy-paste sequences with fallback prompts for each scenario.
  - [ ] Add presenter tips on live mode selection (Plan vs Agent vs Ask) and subagent exploration highlights.
  - [ ] Create `docs/presenter-cheat-sheet.md` and `docs/bobathon-slides-outline.md`.
- **Relevant Context**: `docs/presenter-cheat-sheet.md`
- **Status**: [ ] pending
