---
type: module
project: synthara
layer: core
tags:
  - synthara
  - core
  - status/active
---

---


```markdown
#  Body — Production Layer

> [!abstract]
> Visual identity + Video generation stack.

---

##  ComfyUI (Linux Setup)

### Required Modules
- SDXL Base
- Synthara LoRA (ID consistency)
- ControlNet (Pose / Depth)
- IPAdapter (optional references)

### Stability Rules
- Use fixed seed for ID retention
- Face correction: only if drift >10%
- Render: 9:16 format (1080x1920)

---

## Nano Banana Prompt Structure

### Visual Identity
- Cyberpunk data analyst
- Dark minimalist background
- Subtle holographic UI overlays
- Confident neutral posture

### Clothing Variations
- Tactical blazer
- Minimal black top
- Subtle tech jewelry

---

## Higgsfield Reel Pipeline

1. Import rendered keyframe
2. Add micro head movement
3. Add camera subtle handheld effect
4. Insert overlay text (data points)
5. Add subtitle sync
6. Export 15–25 sec Reel

---

## Production Flow

```mermaid
flowchart LR
    JSON --> Prompt
    Prompt --> ComfyUI
    ComfyUI --> Higgsfield
    Higgsfield --> Instagram
