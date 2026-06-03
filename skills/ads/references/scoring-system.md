# Ad Account Audit Scoring System

<!-- Updated: 2026-02-10 -->
<!-- Sources: Google Research PDF 1, Claude Research, Gemini Research -->

## Weighted Scoring Algorithm

```
S_total = Σ(C_pass × W_sev × W_cat) / Σ(C_total × W_sev × W_cat) × 100
```

- `C_pass` = check passed (1) or failed (0); WARNING = 0.5
- `W_sev` = severity multiplier of the individual check
- `W_cat` = category weight for that platform
- Result: 0-100 Health Score

## Severity Multipliers

| Severity | Multiplier | Criteria |
|----------|-----------|----------|
| Critical | 5.0 | Immediate revenue/data loss risk. Remediation urgent. |
| High | 3.0 | Significant performance drag. Fix within 7 days. |
| Medium | 1.5 | Optimization opportunity. Fix within 30 days. |
| Low | 0.5 | Best practice, minor impact. Nice to have. |

## Scoring Per Check Item

| Result | Points Earned |
|--------|--------------|
| PASS | Full severity × category weight |
| WARNING | 50% of full points |
| FAIL | 0 points |
| N/A | Excluded from total possible |

## Category Weights by Platform

### Google Ads
| Category | Weight | Rationale |
|----------|--------|-----------|
| Conversion Tracking | 25% | Foundation for all optimization; Enhanced Conv + Consent Mode |
| Wasted Spend / Negatives | 20% | Direct money leak; search terms, negative lists |
| Account Structure | 15% | Campaign organization, brand/non-brand separation |
| Keywords & Quality Score | 15% | QS directly impacts CPC; average QS ≥7 target |
| Ads & Assets | 15% | RSA strength, PMax asset completeness, extensions |
| Settings & Targeting | 10% | Location, network, audiences, landing pages |

### Meta Ads
| Category | Weight | Rationale |
|----------|--------|-----------|
| Pixel / CAPI Health | 30% | 87% of advertisers have poor EMQ; foundational signal |
| Creative (Diversity & Fatigue) | 30% | Creative = 70% of campaign results per Meta |
| Account Structure | 20% | Learning phase, CBO/ABO, campaign consolidation |
| Audience & Targeting | 20% | Overlap, exclusions, Advantage+ testing |

### LinkedIn Ads
| Category | Weight | Rationale |
|----------|--------|-----------|
| Technical Setup | 25% | Insight Tag + CAPI essential for B2B attribution |
| Audience Quality | 25% | LinkedIn's targeting precision is its differentiator |
| Creative & Formats | 20% | TLA + format diversity; video efficiency varies |
| Lead Gen Forms | 15% | 13% CVR (3.25× landing pages); CRM integration |
| Bidding & Budget | 15% | High CPCs ($5-$35) require careful management |

### TikTok Ads
| Category | Weight | Rationale |
|----------|--------|-----------|
| Creative Quality | 30% | Native-feel content is #1 success factor |
| Technical Setup | 25% | Pixel + Events API + ttclid passback |
| Bidding & Learning | 20% | 50 conv/week to exit learning; budget sufficiency |
| Structure & Settings | 15% | Smart+, Search Toggle, Shop integration |
| Performance | 10% | CTR, CPA, completion rate benchmarks |

### Microsoft Ads
| Category | Weight | Rationale |
|----------|--------|-----------|
| Technical Setup | 25% | UET tag, import validation, Enhanced Conv |
| Syndication & Bidding | 20% | Partner network control, Copilot placement |
| Structure & Audience | 20% | LinkedIn targeting (unique), campaign structure |
| Creative & Extensions | 20% | Multimedia Ads, Action/Filter Link Extensions (unique) |
| Settings & Performance | 15% | CPC advantage tracking, conversion rate comparison |

## Grading Thresholds

| Grade | Score | Label | Action Required |
|-------|-------|-------|-----------------|
| A | 90-100 | Excellent | Minor optimizations only |
| B | 75-89 | Good | Some improvement opportunities |
| C | 60-74 | Needs Improvement | Notable issues need attention |
| D | 40-59 | Poor | Significant problems present |
| F | <40 | Critical | Urgent intervention required |

## Quick Wins Logic

```
IF severity == "Critical" OR severity == "High"
AND estimated_remediation_time < 15 minutes
THEN flag as "Quick Win"
PRIORITY: Quick Wins sorted by (severity × estimated_impact) DESC
```

Quick Win examples:
- Enable Enhanced Conversions (Critical, 5 min)
- Turn on Search Ads Toggle in TikTok (High, 2 min)
- Add negative keyword lists (Critical, 10 min)
- Fix location targeting method (Critical, 2 min)
- Enable Advantage+ Placements (Medium, 2 min)

## Weighting Rationale

Category weights are calibrated for paid advertising accounts where conversion tracking infrastructure is the highest-impact factor (25-30% weight across platforms). This differs from generic scoring systems because:
- Broken tracking invalidates all optimization decisions downstream
- Creative and targeting quality follow tracking in priority
- Settings and compliance are important but have lower direct revenue impact
- Weights sum to 100% per platform, enabling direct cross-platform comparison

The grading thresholds (A=90-100, B=75-89, C=60-74, D=40-59, F=<40) use wider bands than academic-style scoring because ad account health is typically distributed lower — a score of 75+ represents genuinely well-managed accounts.

---

## Cross-Platform Aggregate Score

When auditing multiple platforms, calculate per-platform scores then aggregate:

```
Aggregate Score = Σ(Platform_Score × Platform_Budget_Share)

Example: Google (82) × 40% + Meta (71) × 35% + LinkedIn (90) × 25%
       = 32.8 + 24.85 + 22.5 = 80.15 → Grade B
```
