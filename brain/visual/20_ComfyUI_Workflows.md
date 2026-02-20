---
project: synthara
module: visual
type: note
tags: []
layer: second
domain: production
status: active
---

← Back to [[03_Body_Production]]  
Also listed in [[06_MOC_Synthara]]  
Profile: [[15_Brain_Profile_From_Questionnaire]]

# 20 — ComfyUI Workflows (v1)

## Purpose
Stable character production on Linux for:
- Identity consistency (LoRA)
- Pose/scene control (ControlNet)
- Upscale + detail pass

Operating mode: low-frequency, high-signal output only. No “daily spam” batches.

## Workflow Blocks (standard)
1) **Identity Lock**
- Load LoRA identity
- Fixed seed optional for reproducibility

2) **Composition Control**
- ControlNet: pose / depth / lineart (as needed)
- Camera framing guardrails (avoid too-close AI face)

3) **Quality Pass**
- Hi-res fix / upscale
- Skin texture preservation (avoid plastic)

4) **Export**
- 1080x1350 (feed) / 1080x1920 (stories/reels cover)
- Save prompt + seed to notes (optional)

## Minimal “Stable Run” Checklist
- [ ] LoRA loaded (correct strength)
- [ ] Negative prompt includes: no face morphing / no identity blending
- [ ] ControlNet used only when needed (avoid overconstraining)
- [ ] Output checked at 100% zoom (skin + eyes)
- [ ] Visual supports one clear thesis from [[07_Cognitive_Core]]

## When to use ComfyUI vs NanoBanana
Use ComfyUI for:
- high consistency identity
- complex pose/scene control
- hard cases (hands, perspective)

Use NanoBanana for:
- fast lookdev
- outfits/location iteration

## Signal Filter (publish gate)
- Keep only assets that strengthen one post-level argument.
- Reject outputs that look impressive but add no receipt value.

## Links
- Thought source: [[07_Cognitive_Core]]
- Draft source: [[13_Draft_Generator_Engine]]
- Production feed into: [[08_Post_Assembly_Line]]
- Profile constraints: [[15_Brain_Profile_From_Questionnaire]]
