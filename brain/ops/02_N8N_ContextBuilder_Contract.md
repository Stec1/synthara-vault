# 02 — N8N ContextBuilder Contract

## 1) Purpose
`WF_01_ContextBuilder` builds a compact brain context for downstream workflows by selecting files from `brain_manifest.json`, then extracting small snippets relevant to the request.

## 2) Inputs (from user/operator)
```json
{
  "task_type": "market_analysis | post_generator | photo_prompt | research",
  "topic": "string",
  "tickers": ["optional", "array"],
  "chain": "optional string",
  "timeframe": "optional string",
  "audience_level": "optional string"
}
```

## 3) Selection logic (using `brain_manifest.json`)
1. Load and parse `brain/brain_manifest.json`.
2. Always include required core docs (in this order):
   - `00_Synthara_Genesis.md`
   - `01_Identity_Soul.md`
   - `02_Brain_Intelligence.md`
   - `07_Cognitive_Core.md`
   - `14_Cognitive_Safeguards.md`
3. Module inclusion by `task_type` (match by `module` field in manifest):
   - `market_analysis` → `market`
   - `post_generator` → `content`
   - `photo_prompt` → `visual`
   - `research` → `core`
4. Budget rules:
   - `max_files = 8` total (core + module)
   - `max_chars = 12000` total snippet text
   - Keep all required core docs first, then add highest-relevance module files by `topic`/optional fields until budget is reached.

## 4) Output format (STRICT)
```json
{
  "context_bundle": {
    "core": ["filename.md"],
    "module": ["filename.md"],
    "snippets": [
      {
        "filename": "filename.md",
        "text": "short extracted text"
      }
    ]
  }
}
```

## 5) Safety gates
- `14_Cognitive_Safeguards.md` must always be present in `context_bundle.core`.
- Never produce buy/sell signals, trade calls, or financial advice language.

### Tiny example (input → output)
```json
{
  "input": {"task_type": "market_analysis", "topic": "ETH liquidity", "chain": "ethereum"},
  "output": {
    "context_bundle": {
      "core": ["00_Synthara_Genesis.md", "14_Cognitive_Safeguards.md"],
      "module": ["19_Oracle_Macro_Module.md"],
      "snippets": [{"filename": "19_Oracle_Macro_Module.md", "text": "Liquidity regime framing..."}]
    }
  }
}
```
