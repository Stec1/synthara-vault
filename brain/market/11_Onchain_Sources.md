---
type: module
project: synthara
layer: second
domain: intelligence
status: active
tags:
  - synthara
  - onchain
  - sources
  - intelligence
---

← Back to [[02_Brain_Intelligence]]
Also listed in [[06_MOC_Synthara]]
Profile: [[15_Brain_Profile_From_Questionnaire]]

# 11 — Onchain Sources (v1)

## Purpose
List the minimal set of sources Synthara trusts for receipts.

## Primary (Receipts-grade)
- Nansen (wallet labels, smart money behavior, token/contract activity)
- Block explorers (Base + relevant chains): tx proof / contract verification
- DEX / liquidity views: liquidity depth, swaps, pool changes

## Secondary (Context)
- Market structure dashboards (dominance, stablecoins, volatility)
- Protocol docs (verify token mechanics / unlocks)
- Dev activity hints (careful; used as context only)

## Receipt Rule
Minimum receipts = per profile: 3 sources OR 2 sources + onchain confirmation.
Always include invalidation path.

## Intake Mapping
Any signal must be captured into [[09_Signal_Intake_Form]] with:
- 2+ receipts
- 24–72h watchlist
- invalidation

## What we ignore by default
See: [[15_Brain_Profile_From_Questionnaire]] → “What is NOT a signal”.
