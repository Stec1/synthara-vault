---
project: Synthara
module: visual
type: note
tags:
  - synthara
  - lora
  - identity
  - standard
layer: second
domain: production
status: active
---



← Back to [[03_Body_Production]]  
Also listed in [[06_MOC_Synthara]]  
Profile: [[15_Brain_Profile_From_Questionnaire]]

# 21 — LoRA Identity Standard (v1)

## Identity Non-Negotiables
- No face morphing
- No identity blending
- No “beautify” drift
- Preserve: bone structure, proportions, micro-texture

Principle: consistency is credibility. If identity shifts, trust drops.

## Prompt Locks (copy-paste)
### Identity Lock (short)
IDENTITY LOCK: use the exact same woman from the reference / trained LoRA. No morphing, no blending.

### Negative Lock
no identity change, no face swap artifacts, no plastic skin, no doll face, no exaggerated eyes, no symmetry lock

## Strength Guidelines (practical)
- Start: 0.75–0.95
- If drift: increase slightly
- If overfit artifacts: decrease slightly

## Consistency Test (weekly)
Generate 6 images:
- 3 lighting conditions
- 2 focal lengths (35/50)

Pass criteria:
- face remains unmistakably identical across all 6

## Failure Protocol
- Fail = do not publish the asset.
- Retrain / recalibrate before next batch.
- Log drift pattern briefly for future prompt updates.

## Links
- Identity style must reflect: [[15_Brain_Profile_From_Questionnaire]]
- Messaging alignment: [[07_Cognitive_Core]]
- Integrates with: [[08_Post_Assembly_Line]]
- Assets chosen from drafts in: [[13_Draft_Generator_Engine]]
