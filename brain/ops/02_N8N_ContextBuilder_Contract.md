---
project: Synthara
module: ops
type: system
tags: [n8n, workflow, context, contract]
---

## 1) Purpose
Define the workflow contract for the N8N Context Builder so upstream inputs are converted into a stable, validated payload for downstream automation.

## 2) Required Manual Inputs
Provide the following fields before execution:
- `session_id` (string)
- `asset_symbol` (string, e.g., BTC, ETH)
- `timeframe` (string, e.g., 1D, 1W)
- `analysis_scope` (string)
- `priority` (string: low | medium | high)

## 3) Normalized JSON Output Schema
```json
{
  "context_id": "string",
  "created_at": "ISO-8601 datetime",
  "session_id": "string",
  "asset": {
    "symbol": "string",
    "timeframe": "string"
  },
  "analysis": {
    "scope": "string",
    "priority": "low|medium|high"
  },
  "status": "ready"
}
```

## 4) Validation Rules
- All required manual inputs must be present and non-empty.
- `priority` must be one of: `low`, `medium`, `high`.
- `created_at` must be valid ISO-8601 UTC datetime.
- `status` must be exactly `ready` before handoff.
- Reject payload if unknown top-level keys are present.

## 5) Downstream Workflow Contract (WF_10_MarketAnalysis)
Context Builder must pass a single normalized JSON object to `WF_10_MarketAnalysis` with:
- `context_id` for traceability.
- `asset.symbol` and `asset.timeframe` for market data selection.
- `analysis.scope` and `analysis.priority` for execution behavior.
- `status=ready` as a hard gate; any other status blocks downstream execution.
