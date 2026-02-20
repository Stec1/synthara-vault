---
project: Synthara
module: core
type: note
tags:
  - synthara
  - agent
  - architecture
  - intelligence
layer: core
domain: intelligence
status: active
---



# Agent Submodules Architecture (v1.0)

## Core Rule
All submodules report to Synthara Core.
No submodule publishes independently.

---

## 1️⃣ Morgana — Sentiment & Narrative Scanner
Purpose:
- Track social sentiment
- Detect narrative shifts
- Identify coordinated hype cycles

Inputs:
- Social feeds
- Onchain volume spikes
- News clustering

Outputs:
- Narrative probability score
- Hype vs organic classification

---

## 2️⃣ AI Oracle — Macro Pattern Model
Purpose:
- Identify cycle positioning
- Detect liquidity phase shifts
- Compare with historical structures

Outputs:
- Macro bias
- Risk-on / Risk-off classification

---

## 3️⃣ Crypto Strategist — Tactical Onchain Module
Purpose:
- Wallet tracking
- Smart money movement
- Contract anomalies

Linked to:
- [[09_Signal_Intake_Form]]
- [[12_Alpha_Scoring_Model]]

---

## 4️⃣ Cyber Futurist — AI & Tech Radar
Purpose:
- Track AI infra
- Detect emerging tool shifts
- Map early signals

---

## Integration Flow

Raw Data
↓
Submodule Analysis
↓
Synthara Core
↓
Decision Gates
↓
Publishing
