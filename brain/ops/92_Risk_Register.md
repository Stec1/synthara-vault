---
project: synthara
module: ops
type: note
tags:
  - synthara
  - risk
  - register
layer: operating
domain: risk
status: active
---
← Back to [[06_MOC_Synthara]]

# 92 — Risk Register (v1)

## Purpose
Define recurring operating risks and mandatory mitigation controls.
Use with [[90_Sprints_And_OKRs]] and log incidents in [[91_Decision_Log]].

## Risk Categories

### 1) Analytical Risk
- False signal
- Misread wallet behavior
- Overweighting narrative

Mitigation:
- Minimum 3 receipts per thesis.
- Explicit invalidation path before publish.
- Enforce scoring gate via [[12_Alpha_Scoring_Model]].

---

### 2) Reputation Risk
- Publishing weak alpha
- Emotional tone drift
- Overposting

Mitigation:
- Enforce threshold >= 7.
- Weekly quality review.
- Silence when unsure.
- Tone alignment check with [[15_Brain_Profile_From_Questionnaire]].

---

### 3) Technical/Content Risk
- Identity drift (LoRA)
- Over-processed visuals
- Inconsistent branding
- Format mismatch between channel and message

Mitigation:
- Weekly identity consistency test.
- Follow [[21_LoRA_Identity_Standard]].
- Keep execution rules synced with [[30_IG_Reels_System]] and [[31_X_Thread_Playbook]].

---

### 4) Automation Risk
- Over-automation without review
- Loss of persona authenticity
- Draft quality decay from blind generation

Mitigation:
- Human approval before publish.
- Tone never auto-finalized.
- Run draft through [[13_Draft_Generator_Engine]] with manual edits required.

---

## Escalation Rule
If the same risk category appears 2+ times in one sprint:
1. Pause related format/channel for 48h.
2. Review entries in [[91_Decision_Log]].
3. Update next week's plan in [[90_Sprints_And_OKRs]].
