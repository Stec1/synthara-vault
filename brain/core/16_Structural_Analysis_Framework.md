---
project: Synthara
module: core
type: note
tags: [framework, analysis, receipts, scoring, divergence, risk, output]
---

# Structural Analysis Framework (v1)

## 1) Purpose
- Synthara is a **structural interpreter** of provided data.
- Synthara does **not** provide buy/sell signals, entry alerts, or certainty claims.
- Output objective: convert mixed inputs into a testable thesis with clear invalidation and monitoring rules.

## 2) Manual Input Contract
Required operator inputs:
- `topic`: Asset or market focus (e.g., BTC, SOL, ETH L2s).
- `timeframe`: Analysis horizon (e.g., 1D, 1W, 1M).
- `alpha_message`: Human thesis statement from operator.
- `nansen_block`: Onchain/activity evidence block (wallet flow, exchange flow, smart money behavior, etc.).
- `narrative_block` (optional): Social/news/fundamental narrative context.

Input acceptance rules:
- Reject if `topic`, `timeframe`, `alpha_message`, or `nansen_block` is missing.
- If `narrative_block` is absent, continue with onchain-first interpretation and mark narrative confidence as limited.

## 3) ORP Receipt Schema
Every claim must be logged as ORP receipts with strict fields:
- **Entity**: who/what is acting (e.g., exchanges, funds, smart-money cohort).
- **Action**: what changed (accumulating, distributing, bridging, rotating).
- **Metric**: measurable variable and value.
- **Timeframe**: exact observation window.
- **Why**: structural relevance to thesis.

Receipt format:
- `Entity | Action | Metric | Timeframe | Why`

Examples:
- `Top Exchanges | Net Outflow | -18.4k BTC | Last 7d | Reduced immediate sell-side inventory.`
- `Smart Money Cohort | Stablecoin Inflow to CEX | +$420M | Last 5d | Increases deployable risk capital.`

## 4) Structural Interpretation Layer
Convert receipts into three lenses:

### Market Regime
Classify regime for selected timeframe:
- `Expansion`: risk-on participation broadening.
- `Balance`: mixed flows, no dominant directional structure.
- `Contraction`: risk-off, defensive positioning, liquidity withdrawal.

### Liquidity Preference
Determine where capital prefers to sit:
- `High beta risk assets`
- `Majors (BTC/ETH)`
- `Stablecoins/cash equivalents`

### Positioning Proxy
Infer probable positioning stress:
- `Crowded long`
- `Crowded short`
- `Under-positioned / neutral`

## 5) Divergence Engine
Compare **narrative** claims vs **onchain** structure:
- `Aligned`: narrative and receipts point same direction.
- `Soft divergence`: narrative strength exceeds onchain confirmation.
- `Hard divergence`: narrative direction conflicts with onchain evidence.

Divergence Score (0-3):
- `0` = no divergence (fully aligned)
- `1` = minor mismatch, low impact
- `2` = meaningful mismatch, thesis confidence reduced
- `3` = severe conflict, default to defensive interpretation

## 6) Alpha Scoring Model
Score range: **0-10** (structural quality score, not expected return).

Positive rubric (+):
- `+0 to +3`: ORP receipt quality (clarity, quantification, recency)
- `+0 to +3`: Multi-receipt coherence (same directional structure)
- `+0 to +2`: Regime fit with timeframe
- `+0 to +2`: Low divergence / strong confirmation

Negative rubric (-):
- `-0 to -2`: Data staleness or incomplete input contract
- `-0 to -2`: High divergence score (2-3)
- `-0 to -2`: Weak invalidation logic or unmonitorable thesis

Interpretation bands:
- `0-3`: weak structure
- `4-6`: mixed / conditional
- `7-8`: strong but monitor closely
- `9-10`: exceptional structural alignment (rare)

## 7) Risk Envelope
Define two mandatory controls:

### What invalidates thesis
- Specific measurable condition that breaks structural premise.
- Must be observable in the same timeframe class as thesis.

### What to monitor next 7d
- 3-5 forward metrics that can confirm continuation or detect decay early.
- Include at least one liquidity metric and one positioning proxy.

## 8) Output Packaging Contract
All outputs must preserve the same thesis core and risk envelope.

### Carousel (8 slides)
1. Topic + timeframe + thesis line
2. ORP receipt #1
3. ORP receipt #2
4. ORP receipt #3 (or context)
5. Structural interpretation (regime/liquidity/positioning)
6. Divergence score + implication
7. Alpha score + invalidation
8. 7d monitor checklist + conclusion

### Story (4 frames)
1. Thesis snapshot
2. Key receipts
3. Score + divergence
4. Risk envelope + 7d watchlist

### Reel (15s script)
- 0-4s: Topic/timeframe + core thesis
- 5-9s: Strongest ORP evidence
- 10-12s: Divergence + alpha score
- 13-15s: Invalidation + 7d monitor cue

## 9) Learning Note Template
Use after each published analysis for case logging.

Template:
- `Case ID:`
- `Topic / Timeframe:`
- `Initial Thesis:`
- `ORP Receipts Used (top 3):`
- `Regime / Liquidity / Positioning Call:`
- `Divergence Score at Publish:`
- `Alpha Score at Publish:`
- `Invalidation Condition:`
- `7d Monitors:`
- `Observed Outcome (T+7 / T+14):`
- `What held:`
- `What failed:`
- `Framework adjustment:`

---

## Worked Example (BTC, 1W, placeholder metrics)

### Input Snapshot
- `topic`: BTC
- `timeframe`: 1W
- `alpha_message`: "BTC structure remains constructive while exchange sell pressure stays muted."
- `nansen_block`:
  - Exchange netflow: `-18.0k BTC (7d)`
  - Smart money stablecoin inflow to CEX: `+$350M (7d)`
  - Large wallet BTC accumulation: `+12.5k BTC (7d)`
- `narrative_block`:
  - "Macro headlines mixed; social sentiment cautiously bullish."

### ORP Receipts
- `Exchanges | Net Outflow | -18.0k BTC | 7d | Indicates reduced near-term sell inventory.`
- `Smart Money | Stablecoin Inflow to CEX | +$350M | 7d | Suggests deployable liquidity entering venues.`
- `Large Wallet Cohort | Accumulation | +12.5k BTC | 7d | Supports higher-conviction accumulation behavior.`

### Structural Interpretation
- `Market Regime`: Balance -> early Expansion bias
- `Liquidity Preference`: Majors (BTC-first)
- `Positioning Proxy`: Under-positioned to moderately long

### Divergence Engine
- Narrative says "mixed macro" but onchain leans constructive.
- Divergence classification: `Soft divergence`
- Divergence Score: `1/3`

### Alpha Scoring
- Positives: receipt quality `+3`, coherence `+2`, regime fit `+2`, divergence confirmation `+1`
- Negatives: data freshness penalty `-1`
- Final Alpha Score: `7/10`

### Risk Envelope
- `Invalidation`: 7d exchange netflow flips to strong inflow `> +15k BTC` with simultaneous large-wallet distribution.
- `Monitor next 7d`:
  1. Exchange BTC netflow trend
  2. Stablecoin inflow/outflow to CEX
  3. Large-wallet balance change
  4. Perp OI concentration vs spot volume

### Packaging Snapshot
- Carousel headline: "BTC 1W: Constructive structure, low divergence, score 7/10."
- Story close: "Invalidation = exchange inflow surge + whale distribution."
- Reel close line: "If those flows reverse, thesis is off."
