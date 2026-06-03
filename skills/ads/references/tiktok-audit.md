# TikTok Ads Audit Checklist

<!-- Updated: 2026-02-11 -->
<!-- Sources: Google Research PDF 1 (T01-T25), Claude Research, Gemini Research -->
<!-- Total Checks: 25 | Categories: 5 | See scoring-system.md for weights and algorithm -->

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Creative Quality | 30% | T05-T10 + T20-T25 (12 checks) |
| Technical Setup | 25% | T01-T02 (2 checks) |
| Bidding & Learning | 20% | T11-T13 (3 checks) |
| Structure & Settings | 15% | T03-T04 + T14-T16 (5 checks) |
| Performance | 10% | T17-T19 (3 checks) |

---

## Creative Quality (30% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T05 | Creative volume | Critical | ≥6 creative assets per ad group | 3-5 creatives | <3 creatives per ad group |
| T06 | Vertical video format | Critical | All video assets 9:16 (1080x1920) | Mixed ratios with some vertical | No vertical video (landscape only) |
| T07 | Native-looking content | High | Ads look organic / creator-style (not polished corporate) | Semi-native style | Clearly corporate/polished ads |
| T08 | Hook strategy | High | First 1-2 seconds have attention-grabbing hook | Decent hook but not optimized | No clear hook in opening |
| T09 | Creative lifespan | High | No creative active >7 days with declining CTR | 7-14 days with minor decline | >14 days with significant CTR decline |
| T10 | Spark Ads utilization | High | Spark Ads (creator content) tested and active | Tested but paused | No Spark Ads tested (~3% CTR vs ~2% standard) |
| T20 | TikTok Shop integration | Medium | Shop catalog connected (for e-commerce) | — | Eligible but not connected |
| T21 | Video Shopping Ads (VSA) | Medium | VSA tested for product catalog accounts | — | Not tested despite eligible catalog |
| T22 | Caption SEO | High | Captions include high-intent keywords for search discovery | Some keywords in captions | No keyword optimization in captions |
| T23 | Sound/music usage | Medium | Trending or engaging audio used | Licensed audio but not trending | Silent ads (TikTok is sound-on platform) |
| T24 | CTA button | Medium | Appropriate CTA button selected (not default) | — | Default CTA without customization |
| T25 | Safe zone compliance | High | Key content within safe zone (X:40-940, Y:150-1470) | Minor elements outside safe zone | Key text/CTA in UI overlay zones |

---

## Technical Setup (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T01 | TikTok Pixel installed | Critical | Pixel firing on all relevant pages | Firing on most pages (>90%) | Pixel not installed or broken |
| T02 | Events API + ttclid | High | Server-side events via Events API with ttclid passback | Events API active but no ttclid passback | No server-side tracking |

### ttclid Critical Note
The TikTok Click ID (`ttclid`) comes in landing page URL parameters and MUST be:
1. Captured on first page load
2. Stored in session/cookie
3. Sent back with ALL conversion events

Without ttclid, attribution breaks for many conversions. This is TikTok's key technical difference from other platforms.

---

## Bidding & Learning (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T11 | Bid strategy | High | Lowest Cost for volume; Cost Cap for efficiency | — | Bid Cap set too aggressively (severe under-delivery) |
| T12 | Budget sufficiency | High | Daily budget ≥50x target CPA per ad group | 20-49x CPA | <20x CPA per ad group |
| T13 | Learning phase | High | Ad groups achieving ≥50 conversions/week | 25-50 conversions/week | <25 conversions/week (stuck in learning) |

### Learning Phase Rules
- Exit criteria: ~50 conversions in 7 days per ad group
- Campaign minimum budget: $50/day
- Ad group minimum budget: $20/day
- Daily budget should be ≥50x target CPA for sufficient learning room
- Avoid changes during learning (resets the phase)

---

## Structure & Settings (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T03 | Campaign structure | High | Separate campaigns for prospecting vs retargeting | — | Prospecting and retargeting mixed |
| T04 | Smart+ utilization | Medium | Smart+ campaigns tested with modular automation (per-module: targeting, budget, creative, placement) | — | Not tested (42% adoption, 1.41-1.67 median ROAS; modular since Oct 2025) |
| T14 | Search Ads Toggle | High | Search Ads Toggle enabled for all campaigns | — | Search Ads Toggle OFF |
| T15 | Placement selection | Medium | Appropriate placements selected (TikTok, Pangle, etc.) | Default placements without review | — |
| T16 | Dayparting | Low | Ad schedule aligned with target audience activity | — | No schedule despite clear patterns |

---

## Performance (10% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T17 | CTR benchmark | High | CTR ≥1.0% for in-feed ads | CTR 0.5-1.0% | CTR <0.5% |
| T18 | CPA target | High | CPA within target range | CPA 1.5-3x target | CPA >3x target (trigger 3x Kill Rule) |
| T19 | Video completion rate | Medium | Average video watch time ≥6 seconds | 3-6 seconds | <3 seconds average watch time |

---

## Quick Wins (TikTok)

| Check | Fix | Time |
|-------|-----|------|
| T14 — Search Ads Toggle | Enable Search Ads Toggle in campaign settings | 2 min |
| T06 — Vertical video | Convert existing assets to 9:16 format | 10 min |
| T24 — CTA button | Select appropriate CTA (not default) | 2 min |
| T10 — Spark Ads | Whitelist top creator/organic content as Spark Ads | 10 min |
| T22 — Caption SEO | Add high-intent keywords to ad captions | 5 min |
| T25 — Safe zone | Verify key content within X:40-940, Y:150-1470 | 5 min |

---

## TikTok-Specific Context

| Fact | Value |
|------|-------|
| Smart+ adoption | 42% of US TikTok performance campaigns (surged from 9% in early 2025) |
| Smart+ capacity | 30 ad groups/campaign, 50 creatives/asset group |
| GMV Max | Default for TikTok Shop Ads (July 2025) |
| TikTok Shop CVR | >10% (vs 0.46-2.4% standard) |
| CPM advantage | 40-60% cheaper than Meta |
| Spark Ads CTR | ~3% vs ~2% standard In-Feed |
| Spark Ads CPA | ~$60 vs ~$100 standard |
| Engagement rate | 5-16% (far exceeds FB 0.09%, IG 1.22%) |
| Search Ads | Launched 2025 for Web Conversion + Traffic |
| Safe zone | X:40-940px, Y:150-1470px (900x1320px usable) |
| Available markets | 11 countries (US, UK, key Asian/European) |

---

## TikTok Safe Zone Diagram

```
┌──────────────────────────────┐
│  0-150px: Status bar, account│  ← TOP UNSAFE
├──────────────────────────────┤
│                         │    │
│    SAFE ZONE            │140 │  ← RIGHT: Like, comment,
│    X: 40-940px          │ px │     share, profile icons
│    Y: 150-1470px        │    │
│    (900×1320px)         │    │
│                         │    │
├──────────────────────────────┤
│  0-450px: Caption, music,    │  ← BOTTOM UNSAFE
│  CTA, navigation bar         │
└──────────────────────────────┘
```

All critical text, logos, and CTAs MUST be within the safe box.
