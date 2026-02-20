---
type: system
project: synthara
layer: operating
domain: memory
status: active
tags:
  - synthara
  - signal
  - memory
  - consistency
---

← Back to [[06_MOC_Synthara]]  
Connect: [[91_Decision_Log]] · [[12_Alpha_Scoring_Model]]

# 17 — Signal Memory Engine (v1)

## Purpose

Maintain structural consistency across time.

Prevent:
- Thesis duplication
- Narrative contradiction
- Signal drift
- Overposting same structure

---

## Signal States

Each published signal must be categorized as:

- 🟢 Active (still valid)
- 🟡 Monitoring (uncertain / evolving)
- 🔴 Invalidated
- 🔵 Completed (thesis resolved)

---

## Pre-Publish Check

Before publishing a new signal:

1. Is a similar thesis already Active?
2. Does this contradict an Active thesis?
3. Is this an update or a new narrative?

If contradiction detected:
→ escalate to manual review

---

## Conflict Resolution Logic

If two signals conflict:

- Compare Alpha score
- Compare Onchain evidence strength
- Compare timing (older vs new structural data)

Higher structural strength wins.

---

## Memory Review Routine

Weekly:

- Review all Active signals
- Move invalidated to 🔴
- Update evolving ones

Connect review to:
[[16_Performance_Intelligence_Engine]]
