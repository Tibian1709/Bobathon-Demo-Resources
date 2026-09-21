# Ingram Micro Bobathon Demo Guide & Scenario Catalog

Welcome to the **Ingram Micro Bobathon Demonstration Guide**. This guide provides end-to-end walkthroughs for 8 live demonstrations of IBM Bob, categorized by audience persona and technical depth.

---

## Catalog Summary Matrix

| # | Demo Name | Tier | Target Persona | Key Bob Capabilities | Time |
|---|---|---|---|---|---|
| **1** | Executive Summary & Partner Onboarding Brief | Tier 1 (Short/Easy) | Partner Account Managers, BAs | Unstructured text synthesis, executive framing, SLA tables | 5-7 min |
| **2** | Reseller Tiering & Margin Calculator | Tier 1 (Short/Easy) | Pricing & Commercial Operations | Office CLI / Excel formula automation, business logic modeling | 5-7 min |
| **3** | User Story & Gherkin Spec Generator | Tier 1 (Short/Easy) | Product Managers, Agile POs | Requirements decomposition, acceptance criteria, Gherkin syntax | 5-7 min |
| **4** | Legacy Order Script Refactoring | Tier 2 (Medium) | Backend Software Engineers | Code explanation, typing, modularization, structured logging | 10-12 min |
| **5** | Automated Unit Testing for Inventory Allocation | Tier 2 (Medium) | Developers, QA Engineers | Edge-case discovery, boundary testing, Pytest mocking | 10-12 min |
| **6** | Partner Catalog Sync REST API Scaffold | Tier 2 (Medium) | API & Integration Developers | Pydantic schema validation, FastAPI endpoints, error handling | 10-12 min |
| **7** | Full-Stack Cloud Subscription Management | Tier 3 (Long/Deep) | Full-Stack Engineers, Tech Leads | Multi-step plan execution, DB migration, backend + UI integration | 18-25 min |
| **8** | Monolith-to-Event-Driven Microservices Migration | Tier 3 (Long/Deep) | Enterprise & Cloud Architects | Architecture decomposition, Kafka/RabbitMQ events, security check | 18-25 min |

---

# Tier 1: Short & Easy (Non-Technical & Product Focus)

## Demo 1: Executive Summary & Partner Onboarding Brief Generator
* **Objective**: Transform messy meeting notes and unstructured partner requirements into a structured, executive-ready onboarding brief with clear milestones and SLA commitments.
* **Target Persona**: Partner Account Managers, Channel Operations, Business Analysts.
* **Input Asset**: `demos/tier-1/demo-1-partner-onboarding/meeting_notes.txt`
* **Demo Narrative**:
  1. Show raw, chaotic notes from a new Tier-1 Cloud Solution Provider (CSP) partner onboarding call.
  2. Prompt Bob in Ask/Agent mode to synthesize key technical requirements, API integration prerequisites, credit limits, and launch timelines.
  3. Bob outputs a structured executive brief with a risk matrix and sign-off checklist.
* **"Wow" Factor**: Converting 2 pages of disorganized notes into a clean, executive document with tables and risk ratings in under 10 seconds.

## Demo 2: Reseller Tiering & Margin Calculator with Excel Automation
* **Objective**: Automatically create a reseller discount and margin calculation spreadsheet with built-in formulas, tier brackets (Silver, Gold, Platinum), and partner margin estimates.
* **Target Persona**: Commercial Operations, Finance Analysts, Vendor Programme Managers.
* **Input Asset**: `demos/tier-1/demo-2-reseller-margins/margin_rules.md`
* **Demo Narrative**:
  1. Show business rules detailing annual spend thresholds and volume discount tiers.
  2. Ask Bob to create a Python script or use OfficeCLI to build an Excel sheet calculating gross revenue, Ingram discount, reseller buy-rate, and suggested retail price (MSRP).
  3. Inspect the resulting spreadsheet with formulas and colour-coded tier headers.
* **"Wow" Factor**: Zero manual spreadsheet formula errors; instantly generating business-ready financial models.

## Demo 3: Product Feature Spec & User Story Decomposition from Customer Feedback
* **Objective**: Ingest unfiltered feedback tickets from the Ingram Micro Cloud Marketplace and decompose them into prioritised Agile epics, user stories, acceptance criteria, and Gherkin scenarios.
* **Target Persona**: Product Managers, Product Owners, Scrum Masters.
* **Input Asset**: `demos/tier-1/demo-3-feedback-stories/raw_feedback.json`
* **Demo Narrative**:
  1. Review raw feedback items complaining about complex multi-cloud billing reconciliation.
  2. Ask Bob to analyze the pain points, group them into a cohesive feature epic ("Automated Multi-Cloud Consolidated Invoice Export"), and output standard Agile user stories with Gherkin scenarios (`Given/When/Then`).
* **"Wow" Factor**: Generating full Jira-ready user stories with crisp boundary acceptance criteria from raw user complaints.

---

# Tier 2: Medium Length (Software Engineers & Full-Stack Developers)

## Demo 4: Legacy Order Processing Script Refactoring
* **Objective**: Take an untyped, monolithic Python script handling order ingestion, apply modern Python 3.11+ type hints, break it into clean domain modules, and replace insecure practices with structured logging.
* **Target Persona**: Backend Engineers, Application Modernization Teams.
* **Input Asset**: `demos/tier-2/demo-4-legacy-refactor/legacy_order_processor.py`
* **Demo Narrative**:
  1. Open `legacy_order_processor.py` showing global variables, nested `try/except` blocks, `print` statements, and lack of type hints.
  2. Ask Bob to explain the flaws and vulnerabilities in the script (including credential hardcoding and lack of input validation).
  3. Use Bob to refactor the code into a clean `OrderService` class with dataclasses, Pydantic validation, structured JSON logging, and IBM security compliance (localhost binding, no hardcoded secrets).
* **"Wow" Factor**: Instant transformation from technical debt to modern, production-grade clean code following enterprise security rules.

## Demo 5: Automated Unit Testing & Edge-Case Coverage for Inventory Allocation
* **Objective**: Automatically analyze complex inventory allocation logic (handling partial allocations, warehouse priority, reserved stock, and backorders) and generate a comprehensive `pytest` suite.
* **Target Persona**: QA Engineers, Core Backend Developers.
* **Input Asset**: `demos/tier-2/demo-5-inventory-tests/inventory_allocator.py`
* **Demo Narrative**:
  1. Review the allocation algorithm in `inventory_allocator.py` which has multiple branching conditions.
  2. Ask Bob to identify missing edge cases (e.g., negative stock requests, zero quantity, race conditions, split shipments across multiple distribution centres).
  3. Bob generates `test_inventory_allocator.py` with parameterized test cases, mocks, and fixtures achieving 100% branch coverage.
  4. Run `pytest` live to show all green tests.
* **"Wow" Factor**: Finding subtle edge-case boundary bugs that human developers often overlook.

## Demo 6: OpenAPI / REST API Endpoint Generation for Partner Catalog Sync
* **Objective**: Build a high-performance, secure FastAPI endpoint for syncing third-party vendor catalogs into the Ingram Micro Cloud Marketplace with schema validation, rate limiting, and standard error envelopes.
* **Target Persona**: API Engineers, Integration Specialists.
* **Input Asset**: `demos/tier-2/demo-6-api-catalog-sync/catalog_spec.json`
* **Demo Narrative**:
  1. Review the incoming vendor catalog JSON schema.
  2. Ask Bob to scaffold a FastAPI router with request/response models, input sanitization, pagination, and OpenAPI documentation tags.
  3. Demonstrate how Bob ensures compliant HTTP status codes, health checks, and secure localhost binding.
* **"Wow" Factor**: End-to-end API scaffold with OpenAPI schema, Pydantic validation, and documentation in a single step.

---

# Tier 3: Long & In-Depth (Lead Engineers & Enterprise Architects)

## Demo 7: Full-Stack Cloud Marketplace Subscription Management
* **Objective**: Walk through an end-to-end feature delivery: database schema migration (SQLAlchemy/Alembic), backend business logic for recurring seat licensing, and a responsive frontend dashboard component.
* **Target Persona**: Senior Full-Stack Engineers, Tech Leads.
* **Input Asset**: `demos/tier-3/demo-7-fullstack-subscription/`
* **Demo Narrative**:
  1. Start in **Plan Mode** to create an execution plan for adding "Seat Tier Upgrades & Prorated Billing" to an existing subscription service.
  2. Switch to **Agent Mode** to execute subtasks sequentially:
     - Step A: Update the database model and generate migration script.
     - Step B: Implement the prorated billing calculation engine with currency rounding.
     - Step C: Create the REST API endpoints (`/subscriptions/{id}/upgrade`).
     - Step D: Scaffold the HTML/JS frontend dashboard widget with status badges and tier selectors.
  3. Validate the feature end-to-end.
* **"Wow" Factor**: Demonstrating Bob's multi-step planning capability (`create-plan`), maintaining context across the entire stack from database to frontend UI.

## Demo 8: Monolith-to-Event-Driven Microservices Migration
* **Objective**: Decompose a tightly coupled monolithic order fulfilment system into an asynchronous, event-driven architecture using Kafka/RabbitMQ events, complete with architectural Mermaid diagrams, domain events, and decoupled consumer services.
* **Target Persona**: Enterprise Architects, Principal Engineers, Cloud Architects.
* **Input Asset**: `demos/tier-3/demo-8-event-driven-migration/monolith_order_system.py`
* **Demo Narrative**:
  1. Inspect the legacy monolith where order creation directly triggers synchronous database writes, ERP calls, email notifications, and warehouse allocation in one blocking transaction.
  2. Ask Bob to analyze the architectural bottlenecks (single point of failure, latency spikes, tight coupling).
  3. Bob generates an event-driven architecture blueprint with a Mermaid sequence diagram.
  4. Bob scaffolds the decoupled event publisher (`OrderPlacedEvent`), the asynchronous Inventory Worker, and the Notification Consumer.
  5. Validate the system with an event-bus simulation script.
* **"Wow" Factor**: Producing enterprise architecture diagrams, decoupling strategies, and working event-driven code in minutes.
