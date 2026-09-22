# Ingram Micro Bobathon: Presenter Copy-Paste Prompt Cheat Sheet

Keep this file open on a second monitor during your live Bobathon session. Each demo has a primary prompt, follow-up prompt, and fallback prompt.

---

## TIER 1: SHORT & EASY (Non-Technical & Product Audience)

### Demo 1: Executive Summary & Partner Onboarding Brief
* **Recommended Mode**: Ask or Agent
* **Context File**: `demos/tier-1/demo-1-partner-onboarding/meeting_notes.txt`
* **Primary Live Prompt**:
  ```text
  Please read the partner onboarding meeting notes in demos/tier-1/demo-1-partner-onboarding/meeting_notes.txt and generate a professional, executive-ready Partner Onboarding Brief.
  Include:
  1. Executive Summary & Partner Profile
  2. Commercial & Credit Agreement Summary Table
  3. Key Technical Integration Prerequisites (APIs, SLAs, Webhooks)
  4. Security & Compliance Checklist (SOC 2, MFA, Tokenization)
  5. Milestones & Target Launch Schedule
  Format the output cleanly in markdown with tables and status checkboxes.
  ```
* **Follow-up Prompt (The "Wow" Add-on)**:
  ```text
  Add a Risk & Mitigation section highlighting potential bottlenecks regarding credit limit approvals and API rate limits, with recommended mitigation actions.
  ```

---

### Demo 2: Reseller Tiering & Margin Calculator with Excel
* **Recommended Mode**: Agent
* **Context File**: `demos/tier-1/demo-2-reseller-margins/margin_rules.md`
* **Primary Live Prompt**:
  ```text
  Review the reseller tiering and discount rules in demos/tier-1/demo-2-reseller-margins/margin_rules.md.
  Generate a Python script or spreadsheet model that calculates:
  1. Ingram Buy Rate and Reseller Buy Price for all listed SKUs across Standard, Silver, Gold, and Platinum tiers.
  2. Dollar and percentage margins for both Ingram Micro (distributor) and the Reseller Partner.
  3. Output the result in a clean, formatted ASCII table or export a CSV summary.
  ```
* **Follow-up Prompt**:
  ```text
  If a Gold Partner orders 250 seats of Microsoft 365 Business Premium and 100 seats of Cisco Duo MFA, calculate their total monthly spend, their quarterly rebate amount, and Ingram Micro's gross margin.
  ```

---

### Demo 3: User Story & Gherkin Spec Generator from Feedback
* **Recommended Mode**: Plan or Agent
* **Context File**: `demos/tier-1/demo-3-feedback-stories/raw_feedback.json`
* **Primary Live Prompt**:
  ```text
  Analyze the partner feedback tickets in demos/tier-1/demo-3-feedback-stories/raw_feedback.json.
  Synthesize the pain points and generate:
  1. An overarching Feature Epic Name & Business Rationale.
  2. 3 prioritised Agile User Stories following the format: 'As a [partner persona], I want [capability] so that [business benefit]'.
  3. Strict Acceptance Criteria for each story.
  4. At least 2 Gherkin test scenarios (Given / When / Then) for mid-cycle license proration and automated webhook dispatch.
  ```

---

## TIER 2: MEDIUM LENGTH (Software Engineers & Developers)

### Demo 4: Legacy Order Script Modernization & Refactoring
* **Recommended Mode**: Agent
* **Context File**: `demos/tier-2/demo-4-legacy-refactor/legacy_order_processor.py`
* **Primary Live Prompt**:
  ```text
  Examine demos/tier-2/demo-4-legacy-refactor/legacy_order_processor.py.
  Explain the key architectural flaws, anti-patterns, and security concerns in this script.
  Then refactor it into clean, modular, production-ready Python 3.11+ code with:
  1. Pydantic request/response models and dataclasses.
  2. Proper decimal currency handling (avoiding floating-point errors).
  3. Structured JSON logging instead of print statements.
  4. Tiered business rule strategy pattern for partner discounts.
  5. Full compliance with IBM security rules (no hardcoded secrets, localhost safe execution).
  ```

---

### Demo 5: Automated Unit Testing for Inventory Allocation
* **Recommended Mode**: Agent
* **Context File**: `demos/tier-2/demo-5-inventory-tests/inventory_allocator.py`
* **Primary Live Prompt**:
  ```text
  Read the inventory allocation engine in demos/tier-2/demo-5-inventory-tests/inventory_allocator.py.
  Identify all subtle edge cases and boundary conditions (including negative quantities, priority buffer borrowing, multi-warehouse splits, and zero stock).
  Write a comprehensive pytest test suite in demos/tier-2/demo-5-inventory-tests/test_inventory_allocator.py achieving 100% branch and edge-case coverage.
  Include parameterized tests and clear assertion docstrings.
  ```
* **Execution Prompt (Live Validation)**:
  ```text
  Run pytest on demos/tier-2/demo-5-inventory-tests/test_inventory_allocator.py and verify that all test suites pass.
  ```

---

### Demo 6: OpenAPI / FastAPI Partner Catalog Sync Scaffold
* **Recommended Mode**: Agent
* **Context File**: `demos/tier-2/demo-6-api-catalog-sync/catalog_spec.json`
* **Primary Live Prompt**:
  ```text
  Using the specification in demos/tier-2/demo-6-api-catalog-sync/catalog_spec.json, scaffold a complete, production-grade FastAPI router for vendor product catalog synchronization.
  Include:
  1. Pydantic models with field validators (e.g. SKU regex, positive price checks, currency enums).
  2. Batch processing logic with partial error reporting (so one invalid SKU does not fail the entire batch).
  3. OpenAPI summary and description tags.
  4. Standardized error handling envelope and health check route.
  ```

---

## TIER 3: LONG & IN-DEPTH (Lead Developers & Architects)

### Demo 7: Full-Stack Cloud Subscription Management
* **Recommended Mode**: Plan mode first, then switch to Agent
* **Context File**: `demos/tier-3/demo-7-fullstack-subscription/feature_spec.md`
* **Step 1 (Plan Mode Prompt)**:
  ```text
  We are implementing the feature described in demos/tier-3/demo-7-fullstack-subscription/feature_spec.md for Ingram Micro Cloud Marketplace.
  Use the create-plan workflow to create an implementation plan with sub-tasks covering:
  1. Data models and ledger schemas.
  2. Daily proration calculation service.
  3. REST API endpoint for seat upgrade simulation and execution.
  4. HTML/Tailwind frontend preview component.
  ```
* **Step 2 (Agent Mode Execution Prompt)**:
  ```text
  Execute Sub-Task 1 & 2: Implement the SQLAlchemy database models and the ProrationCalculationEngine in Python with unit tests verifying exact day-rate arithmetic.
  ```

---

### Demo 8: Monolith to Event-Driven Microservices Migration
* **Recommended Mode**: Plan / Agent
* **Context File**: `demos/tier-3/demo-8-event-driven-migration/monolith_order_system.py`
* **Step 1 (Architecture Blueprint Prompt)**:
  ```text
  Inspect the monolithic order processing script in demos/tier-3/demo-8-event-driven-migration/monolith_order_system.py.
  Identify the critical architectural bottlenecks and failure modes.
  Design an event-driven target architecture decomposing this into:
  - Order Ingestion API & Event Publisher
  - Event Bus (Kafka / RabbitMQ topics)
  - Inventory Allocation Consumer
  - Vendor Provisioning Worker
  - Notification Service
  Provide a Mermaid sequence diagram showing the asynchronous event flow.
  ```
* **Step 2 (Scaffolding Prompt)**:
  ```text
  Scaffold the event schemas (using dataclasses/Pydantic) for OrderPlacedEvent, InventoryAllocatedEvent, and ProvisioningCompletedEvent, along with an in-memory asynchronous EventBus pub/sub demonstrator.
  ```
