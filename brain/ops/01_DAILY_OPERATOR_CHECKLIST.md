---
project: synthara
module: ops
type: note
tags:
  - synthara
  - daily
  - operator
  - checklist
layer: operating
domain: management
status: active
---
# Daily Operator Checklist (5–15 min)

## Daily (Mon–Fri)
- [ ] Scan candidate signals (Nansen / watchlists)
- [ ] If signal exists → open [[09_Signal_Intake_Form]]
- [ ] Score it using [[12_Alpha_Scoring_Model]]
- [ ] If score >= 7 → create an Inbox request in `_inbox/`
- [ ] Generate drafts via [[13_Draft_Generator_Engine]]
- [ ] Produce content if scheduled (Reel/Thread)
- [ ] Log publish decision in [[91_Decision_Log]]

## Weekly (Sunday)
- [ ] Review performance via [[16_Performance_Intelligence_Engine]]
- [ ] Update [[90_Sprints_And_OKRs]]
- [ ] Update watchlists [[13_Wallet_Watchlists]]
- [ ] Review risks [[92_Risk_Register]]
