---
project: synthara
---
# Synthara Local Orchestrator (v1)

## Purpose
Automate 80% of Synthara workflow.

## How to run

1. Place request in `_inbox/`
2. Run:
   python agent/orchestrator.py
3. Check `_outbox/` for response

Future:
- Integrate real LLM call
- Connect to Nansen API
- Auto-log to Decision Log
