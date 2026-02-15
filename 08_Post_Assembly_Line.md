---
type: system
project: synthara
layer: core
domain: distribution
status: active
tags: [synthara, system, pipeline, layer/core, domain/distribution, status/active]
---

# Post Assembly Line (v1.0)

## Inputs (Signal Intake)
Link and define required inputs:
- [[09_Signal_Intake_Form]] — structured intake before drafting
- [[10_Nansen_Playbook]] (signal discovery)
- [[11_Onchain_Sources]] (secondary validation)
- [[13_Wallet_Watchlists]] (context)
- [[12_Alpha_Scoring_Model]] (score)
- [[92_Risk_Register]] (risk framing)

## Gate System (Publish Decision)
Define explicit gates (checkbox format):
- [ ] Gate 1: Signal validity confirmed (2 sources minimum)
- [ ] Gate 2: Alpha score >= threshold (reference [[12_Alpha_Scoring_Model]])
- [ ] Gate 3: Risk framing included (reference [[92_Risk_Register]])
- [ ] Gate 4: Format chosen (reference [[05_Content_Matrix]])
- [ ] Gate 5: “Receipts attached” (what proof is shown)

## Output Formats (Pick One)
Provide 3 output “recipes”:
A) IG Reel (30–45s) → link [[30_IG_Reels_System]] + [[22_Higgsfield_Reels_SOP]]
B) IG Carousel (5–8 slides) → link [[05_Content_Matrix]]
C) X Thread (6–10 tweets) → link [[31_X_Thread_Playbook]]

## Draft Template (Structured)
Provide a template in code block:

```text
SIGNAL:
- Asset/Contract:
- Chain:
- What happened (1 line):

EVIDENCE:
- Wallets/labels:
- Tx links (placeholders):
- Timing:

INTERPRETATION:
- Who is accumulating/distributing:
- Why now:
- What is the market phase:

RISK:
- What would invalidate:
- What to watch next 24–72h:

CTA:
- What viewers should do (non-financial advice phrasing):
```

## Human-in-the-loop (Roles)
Define roles explicitly:
- Yurii: visual taste, humor, final approval, face/scene choice
- Synthara system: structure, analysis framing, scripting, checklists

## Minimum cadence rule (Low-frequency / High-signal)
- Publish only when gates pass.
- Default max: 3–4 deep posts/week.

## Links
Include links back:
- [[00_Synthara_Genesis]]
- [[07_Cognitive_Core]]
- [[02_Brain_Intelligence]]
- [[03_Body_Production]]
- [[04_Economy_Strategy]]
- [[91_Decision_Log]]
