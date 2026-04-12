# startup-investment

> 🇰🇷 [한국어 README](./README.ko.md)

**Startup investment encyclopedia and decision engine — covers the full lifecycle from angel rounds to IPO/exit, with diagnostic, strategy, judgment, and inquiry modes.**

## Prerequisites

- **Claude Cowork or Claude Code** environment
- Web search access (for real-time regulatory/tax verification)

## Goal

Startup fundraising is a maze of legal, financial, and strategic decisions that shift at every stage. This skill encodes the entire lifecycle — 7 stages (Pre-Seed through Secondary), 3 perspectives (strategy, legal, financial), 5 cross-cutting axes (cap table, governance, global structure, failure patterns, investor-founder dynamics), and a dedicated valuation module — into a structured knowledge base with 236 battle-tested patterns. Instead of generic advice, it pattern-matches your specific situation against success/failure pairs with explicit validity conditions.

## When & How to Use

The skill auto-detects one of four modes based on your input:
- **Describe your situation** ("We're preparing for Series A") → **Diagnosis** mode kicks in with gap analysis
- **Ask a directional question** ("How do I raise valuation?") → **Strategy** mode with conditional recommendations
- **Present a fork in the road** ("Sell now or raise another round?") → **Judgment** mode with risk matrix
- **Ask a concept question** ("What are anti-dilution types?") → **Inquiry** mode with direct answer + pattern pair

No manual mode selection needed. For complex scenarios, modes chain automatically (e.g., diagnosis → strategy).

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Seed round readiness check | `"SaaS MRR $50K, 2 cofounders 50:50, no ESOP — seed ready?"` | Diagnosis: loads L2 + X1 spokes, runs gap analysis, flags cap table and ESOP issues with pattern contrast |
| Valuation strategy | `"ARR $3M, NRR 130%, Series A valuation strategy"` | Strategy: loads L3 + VX, recommends ARR multiple × NRR premium approach with validity conditions |
| Exit decision | `"$50M M&A offer vs Series C — 18 months runway left"` | Judgment: loads L3 + L6 + X4 + cross-analysis, builds risk matrix with runway as key variable |
| Quick reference | `"What's the difference between SAFE and convertible note?"` | Inquiry: loads L1, answers directly with [US]/[KR] jurisdiction tags + one contrast pattern pair |
## Key Features

- **Hub-spoke architecture** — 9.6KB hub (SKILL.md) orchestrates 16 reference spokes totaling 127K tokens of compressed domain knowledge
- **236 conditional patterns** — every success pattern is paired with a failure counterpart, each with explicit validity/invalidity conditions to prevent survivorship bias
- **Auto mode detection** — no manual switching; the engine infers diagnosis/strategy/judgment/inquiry from your input
- **3-phase ping-pong** — gathers context (current state → objective → constraints) before producing output, avoiding premature recommendations
- **Dual jurisdiction** — all legal and tax content tagged [KR] or [US] with base-year markers, reflecting Delaware flip structures and Korean regulatory reality
- **Cross-analysis layer** — 6 contradictions, 5 reinforcement loops, 9 gap areas, and an exit matrix connecting patterns across stages

## Works With

- **[bp-guide](https://github.com/jasonnamii/bp-guide)** — hands off to BP writing after fundraising strategy is set
- **[biz-skill](https://github.com/jasonnamii/biz-skill)** — business strategy patterns; this skill absorbs the capital and exit subsets
- **[holdings-consulting](https://github.com/jasonnamii/holdings-consulting)** — post-exit holding company structuring
- **[research-frame](https://github.com/jasonnamii/research-frame)** — deep research mode for novel edge cases

## Installation

```bash
git clone https://github.com/jasonnamii/startup-investment.git ~/.claude/skills/startup-investment
```

## Update

```bash
cd ~/.claude/skills/startup-investment && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.