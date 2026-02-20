---
project: Synthara
module: ops
type: system
tags:
  - ops
  - synthara
---


# Brain Reorganization Summary Report

## Files moved by module

### core
- 00_Synthara_Genesis.md
- 01_Identity_Soul.md
- 02_Brain_Intelligence.md
- 06_MOC_Synthara.md
- 07_Cognitive_Core.md
- 11_Agent_Submodules.md
- 14_Cognitive_Safeguards.md
- 15_Brain_Profile_From_Questionnaire.md
- 17_Signal_Memory_Engine.md

### market
- 04_Economy_Strategy.md
- 10_Nansen_Playbook.md
- 11_Onchain_Sources.md
- 12_Alpha_Scoring_Model.md
- 13_Wallet_Watchlists.md
- 16_Performance_Intelligence_Engine.md
- 18_Morgana_Sentiment_Module.md
- 19_Oracle_Macro_Module.md
- 24_Strategist_Onchain_Core.md
- 25_Futurist_AI_Infra_Module.md
- 40_Tokenomics_Working_Draft.md
- 41_IAO_Launch_Playbook.md

### content
- 05_Content_Matrix.md
- 08_Post_Assembly_Line.md
- 09_Signal_Intake_Form.md
- 10_Performance_Feedback_System.md
- 13_Draft_Generator_Engine.md
- 30_IG_Reels_System.md
- 31_X_Thread_Playbook.md
- 32_Farcaster_Growth_System.md

### visual
- 03_Body_Production.md
- 20_ComfyUI_Workflows.md
- 21_LoRA_Identity_Standard.md
- 22_Higgsfield_Reels_SOP.md
- 23_NanoBanana_Lookdev_Library.md

### ops
- 12_Semi_Automation_Blueprint.md
- 42_Clawbot_Gating_Roles.md
- 43_Moltbook_Office_Structure.md
- 90_Sprints_And_OKRs.md
- 91_Decision_Log.md
- 92_Risk_Register.md
- _inbox/00_REQUEST_TEMPLATE.md -> brain/ops/00_REQUEST_TEMPLATE.md
- _inbox/01_LIVE_TEST_TEMPLATE.md -> brain/ops/01_LIVE_TEST_TEMPLATE.md
- _ops/00_PIPELINE_MAP.md -> brain/ops/00_PIPELINE_MAP.md
- _ops/01_DAILY_OPERATOR_CHECKLIST.md -> brain/ops/01_DAILY_OPERATOR_CHECKLIST.md
- _outbox/00_RESPONSE_TEMPLATE.md -> brain/ops/00_RESPONSE_TEMPLATE.md
- agent/README.md -> brain/ops/README.md

## Duplicate / overlapping content flagged
1. Market intelligence overlap:
   - 10_Nansen_Playbook.md
   - 11_Onchain_Sources.md
   - 24_Strategist_Onchain_Core.md
   **Suggestion:** Consolidate into a single `market/onchain_intelligence_framework.md` and keep the others as source-specific appendices.

2. Content workflow overlap:
   - 08_Post_Assembly_Line.md
   - 13_Draft_Generator_Engine.md
   - 10_Performance_Feedback_System.md
   **Suggestion:** Merge into unified `content/content_lifecycle_system.md` (draft -> publish -> evaluate loop).

3. Visual production overlap:
   - 20_ComfyUI_Workflows.md
   - 22_Higgsfield_Reels_SOP.md
   - 23_NanoBanana_Lookdev_Library.md
   **Suggestion:** Create one `visual/visual_pipeline_master.md` with tool-specific sections.

4. Governance overlap:
   - 90_Sprints_And_OKRs.md
   - 91_Decision_Log.md
   - 92_Risk_Register.md
   **Suggestion:** Bundle into an `ops/governance_pack/` pattern for quarterly reviews.

## Missing modules
- None. All required modules (`core`, `market`, `content`, `visual`, `ops`) are populated.

## n8n compatibility notes
- Folder-based modular retrieval is now explicit under `/brain/<module>/...`.
- `brain_manifest.json` provides machine-readable routing metadata for deterministic retrieval nodes.
- Suggested next step: expose module path + tags as n8n lookup keys (`module`, `tags[]`, `filename`).
