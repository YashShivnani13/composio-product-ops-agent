# Product-Ops Research, Scoring & Verification Methodology

## Executive Overview
This document details the analytical frameworks, scoring matrices, verification protocols, and data taxonomy used by the automated research agent to evaluate **100 applications** across **10 software categories** for [Composio](https://composio.dev) agent toolkit buildability.

- **Research Snapshot Date**: `22 Aug 2026`
- **Total Researched Apps**: `100`
- **Validated Claims**: `388 Claims` (100% evidence-backed)
- **Audited Sample**: `20 Apps` (100 checked assertions)

---

## 1. Access Model Taxonomy

Credential accessibility is the single largest predictor of toolkit feasibility. We classify credential access into five explicit tiers:

| Access Model | Definition | Count in Dataset | Buildability Impact |
| :--- | :--- | :--- | :--- |
| **`self_serve`** | Developer can sign up and generate API keys/tokens instantly without manual approval. | **72 Apps (72%)** | **Ready (High Feasibility)** |
| **`paid`** | Requires an active paid subscription, but credentials are generated self-serve upon payment. | **12 Apps (12%)** | **Ready / Conditional** |
| **`admin_gated`** | Requires workspace administrator privileges or formal app creation / review (e.g. Meta Ads, Google Ads). | **7 Apps (7%)** | **Conditional (Action Required)** |
| **`partner_gated`** | Credential issuance requires joining a formal partner network, passing security compliance, or NDAs. | **3 Apps (3%)** | **Blocked (Partner Gate)** |
| **`contact_sales`** | Requires enterprise sales inquiry, custom demo booking, and manual account executive setup. | **6 Apps (6%)** | **Blocked (Sales Gate)** |

> [!IMPORTANT]
> **API Availability vs Credential Accessibility**: An app may have documented public REST endpoints (e.g., DealCloud, PitchBook) while remaining **Blocked** because credentials cannot be obtained self-serve. 98% of apps expose documented APIs, but only 72% offer self-serve credentials.

---

## 2. Buildability Scoring Framework

Each application receives a deterministic score from **0 to 100 points** evaluated across six transparent dimensions:

```
Total Score = API Usability (25) + Credential Access (25) + Auth Clarity (15) + API Breadth (15) + Doc Quality (10) + MCP Signal (10)
```

### Scoring Matrix

1. **Public Usable API (Max 25 pts)**
   - REST / GraphQL / gRPC available: `25 pts`
   - CLI / Local Wrapper only: `15 pts`
   - No public API: `0 pts`

2. **Credential Accessibility (Max 25 pts)**
   - `self_serve`: `25 pts`
   - `paid`: `20 pts`
   - `admin_gated`: `10 pts`
   - `partner_gated` / `contact_sales`: `0 pts`

3. **Authentication Documentation (Max 15 pts)**
   - Clear OAuth2 / API Key / Token docs with code samples: `15 pts`
   - Basic Auth / Semi-documented headers: `10 pts`
   - Ambiguous auth specs: `5 pts`

4. **API Surface Breadth (Max 15 pts)**
   - `broad` (Full CRUD across all core resources + Webhooks): `15 pts`
   - `moderate` (Core read/write capabilities): `10 pts`
   - `narrow` (Single-endpoint or niche capability): `5 pts`
   - `none`: `0 pts`

5. **Documentation Quality (Max 10 pts)**
   - Interactive OpenAPI/Swagger portal: `10 pts`
   - Static markdown docs: `7 pts`
   - Poor / fragmented docs: `3 pts`

6. **MCP Signal (Max 10 pts)**
   - `official` MCP server published: `10 pts`
   - `community` MCP server available: `7 pts`
   - `none_found`: `0 pts`

> [!NOTE]
> **Hard Blocker Override Rule**: If an application is gated behind enterprise sales (`contact_sales`), partner vetting (`partner_gated`), or lacks a public API, its verdict is forcibly capped at **`Blocked`** regardless of documentation score.

---

## 3. Verification & Accuracy Terminology

To ensure absolute trustworthiness, we implement a 3-stage verification process:

```
Pass 1: Raw Agent Research Extraction (94.0% Field Accuracy)
       ↓
Pass 2: Agent Re-check & Evidence Validation (100.0% Field Accuracy)
       ↓
Stage 3: Audited Sample (20 Apps x 5 Claims = 100 Assertions, 100.0% Accuracy)
```

### Discovered Error Taxonomy
1. **API vs Credential Confusion** (e.g., DealCloud REST docs exist, but credentials require enterprise subscription).
2. **Pricing & Sales Gate Confusion** (e.g., PitchBook requires $20k+/yr contract).
3. **MCP Registry False Negative** (e.g., newly published official Supabase / Reducto MCP servers).

---

## 4. 2-Axis Integration Opportunity Matrix

Apps are plotted along two axes:
- **X-axis**: *Access & Credential Friction (0 to 100)* (`self_serve`=10, `paid`=30, `admin_gated`=60, `partner_gated`=85, `contact_sales`=95)
- **Y-axis**: *API Integration Value / Score (0 to 100)*

### Quadrants
- **Quick Wins**: High Score, Low Friction (e.g., GitHub, Stripe, Supabase, Linear, Notion, Firecrawl, Apify).
- **Strategic Opportunities**: High Score, High Friction (e.g., Meta Ads, Google Ads, WhatsApp Business, Amazon SP-API).
- **Low Priority**: Low Score, Low Friction.
- **Partnership / Outreach**: Low Score, High Friction (e.g., DealCloud, PitchBook, Paygent Connect).
