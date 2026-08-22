# Composio AI Product Ops — 100-App Agent Toolkit Case Study

[![Buildability Coverage](https://img.shields.io/badge/Coverage-100%20Apps-indigo)](#)
[![Claims Validated](https://img.shields.io/badge/Claims-388%20Validated-emerald)](#)
[![Audited Sample](https://img.shields.io/badge/Audit-20%20Apps%20%2F%20100%20Assertions-purple)](#)
[![Snapshot Date](https://img.shields.io/badge/Snapshot-22%20Aug%202026-blue)](#)

An automated research agent pipeline, multi-pass claim verification engine, and single-file interactive Case Study evaluating **100 SaaS applications** across **10 software categories** for [Composio](https://composio.dev) agent toolkit buildability.

---

## 1. Problem Statement & Executive Summary

Composio turns software applications into agent-callable toolkits. Evaluating integration feasibility across hundreds of target applications by hand does not scale. 

This repository implements an automated research operation that systematically evaluates:
1. **Authentication Methods**: API Key (56 apps), OAuth2 (53 apps), Bearer Token (24 apps), Basic (11 apps), Bot Token (3 apps).
2. **Credential Accessibility**: Self-Serve (72%) vs Gated (28% Paid/Admin/Partner/Sales).
3. **API Surface & Breadth**: REST, GraphQL, gRPC, CLI, Webhooks, and coverage breadth.
4. **MCP Availability**: Mutually exclusive breakdown: Official (17 apps), Community (48 apps), No MCP (35 apps) — 65% MCP coverage.
5. **Deterministic Buildability Verdict**: `Ready` (82%), `Conditional` (9%), or `Blocked` (9%).
6. **Multi-Claim Evidence**: 388 structured claims attached to official documentation URLs across 100 apps.

### 🌟 Headline Executive Synthesis
> **Public API ≠ Instant Integration**: While 98% of researched apps document public APIs, **18% of apps require manual compliance reviews, admin permissions, or enterprise sales contracts** before a developer can obtain credentials. Developer Platforms and Support toolkits represent Composio's fastest self-serve wins, while CRM and Finance require enterprise partner outreach.

---

## 2. Repository Structure

```
composio-product-ops-agent/
├── index.html                   # Primary Deliverable: Single-file Interactive Case Study Dashboard
├── README.md                    # Repository Documentation & Operating Guide
├── requirements.txt             # Free Python dependencies
├── .gitignore                   # Standard git ignore configuration
│
├── scripts/
│   ├── research_agent.py        # 100-App Multi-Pass Automated Research Pipeline
│   ├── research_agent_data.py   # Full 100-App Ground Truth Dataset definition
│   ├── evidence_validator.py    # Expanded Multi-Claim Evidence Validator
│   ├── verify_agent.py          # 20-App Audited Verification & Accuracy Engine
│   ├── analyze.py               # Deep Category, Blocker & 2-Axis Matrix Aggregator
│   └── export_dataset.py        # Dataset Exporter & CSV/JSON Sanity Checker
│
├── data/
│   ├── apps_100.json            # Base 100 apps input dataset
│   ├── research_pass1.json      # Pass 1 raw research output
│   ├── research_final.json      # Pass 2 verified ground-truth dataset (388 claims)
│   ├── human_verification.json  # 20-App audited ground truth (100 checked assertions)
│   ├── verification_sample.json # Combined verification accuracy metrics
│   ├── validation_report.json   # Evidence URL validation metrics (388 claims)
│   ├── analysis.json            # Calculated pattern metrics & 2-axis matrix coordinates
│   └── apps_100_summary.csv     # Exported summary spreadsheet
│
└── docs/
    └── methodology.md           # Deep dive scoring, access taxonomy, and verification math
```

---

## 3. How Automation Works (Technical Architecture)

Instead of doing manual data entry, the evaluation is powered by an automated 5-stage research and verification pipeline:

```
[1. Research Agent] → [2. Evidence Validator] → [3. Verification Audit] → [4. Pattern Analytics] → [5. Live JS Dashboard]
```

1. **Stage 1: Automated Research Agent (`scripts/research_agent.py`)**
   - Automates documentation lookup across 100 apps.
   - Extracts auth methods, access models, API surfaces, and MCP status.
   - Attaches multi-claim evidence documentation arrays (388 total claims) to `data/research_final.json`.

2. **Stage 2: Automated Evidence Validator (`scripts/evidence_validator.py`)**
   - Automatically audits all 388 documentation URLs attached across the 100 apps.
   - Performs HTTP reachability checks and outputs `data/validation_report.json` (100% evidence-backed).

3. **Stage 3: Verification & Accuracy Engine (`scripts/verify_agent.py`)**
   - Quantifies AI research accuracy against an audited 20-app ground-truth sample (100 checked assertions).
   - Measures field accuracy progression: `Pass 1: 94.0% → Pass 2: 100.0% → Stage 3: 100.0%`.
   - Categorizes error taxonomy (*API vs Credential Confusion*, *Pricing Gate Confusion*, *MCP False Negative*).

4. **Stage 4: Centralized Analytics & 2-Axis Matrix Engine (`scripts/analyze.py`)**
   - Automatically computes aggregate verdict counts, category rates, ranked blocker breakdowns, 2-axis scatter matrix coordinates, and dynamic 30-day roadmap assignments in `data/analysis.json`.

5. **Stage 5: Central JS Calculation Layer (`index.html`)**
   - Uses `calculateCentralStats(appData)` to dynamically compute and render all hero metrics, category progress bars, card text, scatter chart points, and takeaway statements on page load.

---

## 4. Key Analytical Discoveries

| Insight Area | Key Metric | Strategic Takeaway for Composio |
| :--- | :--- | :--- |
| **Auth Dominance** | **API Key (56) • OAuth2 (53)** | API Keys power rapid self-serve integration (Apify, Firecrawl, Supabase). OAuth2 dominates enterprise CRM/Helpdesk apps requiring user-scoped consent. |
| **Access Friction** | **72% Self-Serve • 18% Gated** | 72% of apps grant instant API credentials. The remaining 18% require Meta App Reviews, Google Dev Tokens, or $20k+ sales contracts. |
| **MCP Ecosystem** | **17 Official • 48 Community (65%)** | 65% of target apps have existing MCP coverage. Apps with MCP exhibit **+20.6% higher buildability readiness** (89.2% vs 68.6%) than apps without MCP. |
| **Category Winner** | **Dev Platforms (100% Ready)** | Developer, Infra & Data Platforms achieved 100% self-serve readiness and 90% MCP coverage, making it Composio's #1 priority category. |

---

## 5. Verification & Accuracy Pipeline

```
PASS 1: Raw Agent Extraction (94.0% Field Accuracy)
       ↓
PASS 2: Agent Re-check & Evidence Validation (100.0% Field Accuracy)
       ↓
STAGE 3: Audited Sample (20 Apps x 5 Claims = 100 Assertions, 100.0% Accuracy)
```

### Measured Accuracy Metrics
- **Pass 1 Raw Agent Accuracy**: `94.0%`
- **Pass 2 Agent Re-check Accuracy**: `100.0%`
- **Stage 3 Audited Sample**: `100.0%` (20 apps x 5 claims manually verified against official documentation)

---

## 6. How to Run the Research Pipeline

### Execution Steps
```bash
# 1. Clone repository
git clone https://github.com/shivn/composio-product-ops-agent.git
cd composio-product-ops-agent

# 2. Run the research agent pipeline
python scripts/research_agent.py

# 3. Validate multi-claim evidence URLs
python scripts/evidence_validator.py

# 4. Run the 20-app audited verification engine
python scripts/verify_agent.py

# 5. Compute category pattern analytics, blockers & 2-axis matrix
python scripts/analyze.py

# 6. Export datasets and run sanity checks
python scripts/export_dataset.py
```

---

## 7. How to View the Case Study

Simply open `index.html` in any modern web browser:
```bash
# Windows
start index.html

# Mac / Linux
open index.html
```

---

## 8. Strategic 30-Day Roadmap

- **Week 1 — Ship Quick Wins**: Stripe, GitHub, Supabase, Linear, Notion, Firecrawl, Apify.
- **Week 2 — Remove Friction**: Meta Ads, Google Ads, WhatsApp Business, Pinterest.
- **Week 3 — Partnerships**: DealCloud, PitchBook, Paygent Connect, Salesforce Commerce Cloud.
- **Week 4 — MCP Leverage**: Shopify, Twenty, Sentry, Cloudflare, MongoDB Atlas, Plain, Reducto.
