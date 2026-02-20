---
project: Synthara
module: market
type: note
tags:
  - synthara
  - alpha
  - scoring
  - model
  - intelligence
layer: second
domain: intelligence
status: active
---



← Back to [[02_Brain_Intelligence]]
Also listed in [[06_MOC_Synthara]]
Profile: [[15_Brain_Profile_From_Questionnaire]]

# 12 — Alpha Scoring Model (v1)

> [!note] Threshold
> Publish when score >= 7 (per [[15_Brain_Profile_From_Questionnaire]]).

## Scoring Components (0–10 each)
1) Onchain Evidence Quality (weight 30%)
- receipts count + independence + clarity

2) Holder Behavior / Token God Mode (weight 25%)
- cohort shift, distribution risk, concentration change

3) Narrative vs Onchain Divergence (weight 20%)
- narrative says X, onchain shows Y

4) Timing / Market Structure Fit (weight 15%)
- aligns with macro phase (Oracle layer)

5) AI x Crypto Infra Signal Value (weight 10%)
- relevance to AI/agent/compute infra trend

## Quick Compute
FinalScore = 0.30*E + 0.25*H + 0.20*D + 0.15*T + 0.10*A

Where:
E=Evidence, H=Holder behavior, D=Divergence, T=Timing, A=AI-infra relevance

## Rating Guide (fast heuristics)
- 9–10: structural shift with strong receipts + clear invalidation
- 7–8: strong thesis with enough receipts (publishable)
- 5–6: interesting but insufficient proof (HOLD)
- <5: noise (ignore)

## Required Output Fields (for drafts)
- Thesis (1 line)
- Receipts (max 3 bullets)
- Invalidation (2 bullets)
- Watch next 24–72h (3 bullets)

Links:
Use with [[09_Signal_Intake_Form]] → then [[13_Draft_Generator_Engine]].
