# Google Ads Audit Checklist

<!-- Updated: 2026-02-11 -->
<!-- Sources: Google Research PDF 1 (G01-G61), Claude Research (74-item extended), Gemini Research -->
<!-- Total Checks: 74 | Categories: 7 | See scoring-system.md for weights and algorithm -->

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Conversion Tracking | 25% | G42-G49 (8 checks) + G-CT1 through G-CT3 (3 extended) |
| Wasted Spend / Negatives | 20% | G13-G19 (7 checks) + G-WS1 (1 extended) |
| Account Structure | 15% | G01-G12 (12 checks) |
| Keywords & Quality Score | 15% | G20-G25 (6 checks) + G-KW1, G-KW2 (2 extended) |
| Ads & Assets | 15% | G26-G35 (10 checks) + G-AD1, G-AD2 (2 extended) |
| Settings & Targeting | 10% | G50-G61 (12 checks) |
| Performance Max | — | G-PM1 through G-PM5 (5 checks, scored within Ads & Assets) |

---

## Conversion Tracking (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G42 | Conversion actions defined | Critical | ≥1 primary conversion action configured | — | No active conversion actions |
| G43 | Enhanced conversions enabled | Critical | Enhanced conversions active for primary conversions | Enabled but not verified | Not enabled |
| G44 | Server-side tracking | High | Server-side GTM or Google Ads API conversion import active | Planned but not deployed | No server-side tracking |
| G45 | Consent Mode v2 (EU/EEA) | Critical | Consent Mode v2 implemented with Advanced mode | Basic mode only | Not implemented (if serving EU/EEA) |
| G46 | Conversion window appropriate | Medium | Window matches sales cycle (7d ecom, 30-90d B2B, 30d lead gen) | Default 30d without validation | Window mismatched to sales cycle |
| G47 | Micro vs macro separation | High | Only macro conversions (Purchase, Lead) set as "Primary" for bidding | Some micro events as Primary | All events including micro (AddToCart, TimeOnSite) as Primary |
| G48 | Attribution model | Medium | Data-driven attribution (DDA) selected | Last Click (intentional) | Rule-based model still active (deprecated Sep 2025) |
| G49 | Conversion value assignment | High | Dynamic values for ecom; value rules for lead gen | Static values assigned | No conversion values |
| G-CT1 | No duplicate counting | Critical | GA4 + Google Ads not double-counting same conversion | — | Both GA4 import and native tag counting same action |
| G-CT2 | GA4 linked and flowing | High | GA4 property linked, data flowing correctly | Linked but data discrepancies | Not linked |
| G-CT3 | Google Tag firing | Critical | gtag.js or GTM firing correctly on all pages | Firing on most pages (>90%) | Tag missing or broken on key pages |

---

## Wasted Spend / Negatives (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G13 | Search term audit recency | Critical | Search terms reviewed within last 14 days | Reviewed within 30 days | Not reviewed in >30 days |
| G14 | Negative keyword lists exist | Critical | ≥3 theme-based lists (Competitor, Jobs, Free, Irrelevant) | 1-2 lists exist | No negative keyword lists |
| G15 | Account-level negatives applied | High | Negative lists applied at account or all-campaign level | Applied to some campaigns only | Not applied |
| G16 | Wasted spend on irrelevant terms | Critical | <5% of spend on irrelevant search terms (last 30d) | 5-15% on irrelevant terms | >15% on irrelevant terms |
| G17 | Broad match + smart bidding pairing | Critical | No Broad Match keywords running on Manual CPC | — | Broad Match + Manual CPC active |
| G18 | Close variant pollution | High | Exact/Phrase match not triggering irrelevant close variants | Minor close variant issues | Significant irrelevant close variant spend |
| G19 | Search term visibility | Medium | >60% of search term spend is visible (not hidden) | 40-60% visible | <40% visible |
| G-WS1 | Zero-conversion keywords | High | No keywords with >100 clicks and 0 conversions | 1-3 such keywords | >3 keywords with >100 clicks, 0 conversions |

---

## Account Structure (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G01 | Campaign naming convention | Medium | Consistent pattern (e.g., [Brand]_[Type]_[Geo]_[Target]) | Partially consistent | No naming convention |
| G02 | Ad group naming convention | Medium | Matches campaign naming pattern | Partially consistent | No naming convention |
| G03 | Single theme ad groups | High | Each ad group targets 1 keyword theme (≤10 keywords) | 11-20 keywords with consistent theme | Ad groups with 20+ unrelated keywords (theme drift) |
| G04 | Campaign count per objective | High | ≤5 campaigns per funnel stage/objective | 6-8 campaigns per objective | >8 campaigns per objective (fragmented) |
| G05 | Brand vs Non-Brand separation | Critical | Brand and non-brand in separate campaigns | — | Brand and non-brand mixed in same campaign |
| G06 | PMax present for eligible accounts | Medium | PMax active for accounts with conversion history | PMax tested but paused | No PMax tested despite eligibility |
| G07 | Search + PMax overlap | High | Brand exclusions configured in PMax when Search brand campaign exists | Partial brand exclusions | No brand exclusions in PMax alongside brand Search |
| G08 | Budget allocation matches priority | High | Top-performing campaigns not budget-limited | Minor budget constraints on top performers | Top performers severely budget-limited |
| G09 | Campaign daily budget vs spend | Medium | No campaigns hitting budget cap before 6PM | 1-2 campaigns hitting cap early | Multiple campaigns capped before noon |
| G10 | Ad schedule configured | Low | Ad schedule set if business has operating hours | — | No schedule despite clear business hours |
| G11 | Geographic targeting accuracy | High | "People in" (not "People in or interested in") for local | — | "People in or interested in" for local business |
| G12 | Network settings | High | Search Partners and Display Network disabled for Search (unless intentional) | Search Partners ON (monitored) | Display Network ON for Search campaign |

---

## Keywords & Quality Score (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G20 | Average Quality Score | High | Account-wide impression-weighted QS ≥7 | QS 5-6 | QS ≤4 |
| G21 | Critical QS keywords | Critical | <10% of keywords with QS ≤3 | 10-25% with QS ≤3 | >25% with QS ≤4 |
| G22 | Expected CTR component | High | <20% of keywords with "Below Average" expected CTR | 20-35% Below Average | >35% Below Average |
| G23 | Ad relevance component | High | <20% of keywords with "Below Average" ad relevance | 20-35% Below Average | >35% Below Average |
| G24 | Landing page experience | High | <15% of keywords with "Below Average" landing page exp. | 15-30% Below Average | >30% Below Average |
| G25 | Top keyword QS | Medium | Top 20 spend keywords all have QS ≥7 | Some top keywords at QS 5-6 | Top keywords with QS ≤4 |
| G-KW1 | Zero-impression keywords | Medium | No keywords with 0 impressions in last 30 days | <10% zero-impression | >10% of keywords with 0 impressions |
| G-KW2 | Keyword-to-ad relevance | High | Headlines contain primary keyword variants | Partial keyword inclusion | No keyword variants in ad headlines |

---

## Ads & Assets (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G26 | RSA per ad group | High | ≥1 RSA per ad group (≥2 recommended) | 1 RSA per ad group | Ad groups without any RSA |
| G27 | RSA headline count | High | ≥8 unique headlines per RSA (ideal: 12-15) | 3-7 headlines | <3 headlines |
| G28 | RSA description count | Medium | ≥3 descriptions per RSA (ideal: 4) | 2 descriptions | <2 descriptions |
| G29 | RSA Ad Strength | High | All RSAs "Good" or "Excellent" | Some "Average" | Any RSA with "Poor" Ad Strength |
| G30 | RSA pinning strategy | Medium | Strategic pinning (1-2 positions, 2-3 variants each) | Over-pinned (all positions) | — |
| G31 | PMax asset group density | Critical | ≥20 images, ≥5 logos, ≥5 videos per group (maximum density) | 5-19 images, 1-4 logos, or 1-4 videos | <5 images OR 0 logos OR 0 video |
| G32 | PMax video assets present | High | Native video in all formats (16:9, 1:1, 9:16) | 1-2 formats only | No native video (auto-generated only) |
| G33 | PMax asset group count | Medium | ≥2 asset groups per PMax (intent-segmented) | 1 asset group | — |
| G34 | PMax final URL expansion | High | Configured intentionally (ON for discovery, OFF for control) | — | Default ON without review |
| G35 | Ad copy relevance to keywords | High | Headlines contain primary keyword variants | Partial keyword inclusion | No keyword relevance in headlines |
| G-AD1 | Ad freshness | Medium | New ad copy tested within last 90 days | — | No new ads in >90 days |
| G-AD2 | CTR vs industry benchmark | High | CTR ≥ industry average | CTR 50-100% of industry average | CTR <50% of industry average |

---

## Settings & Targeting (10% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G50 | Sitelink extensions | High | ≥4 sitelinks per campaign | 1-3 sitelinks | No sitelinks |
| G51 | Callout extensions | Medium | ≥4 callouts per campaign | 1-3 callouts | No callouts |
| G52 | Structured snippets | Medium | ≥1 structured snippet set | — | No structured snippets |
| G53 | Image extensions | Medium | Image extensions active for search campaigns | — | No image extensions |
| G54 | Call extensions (if applicable) | Medium | Call extensions with call tracking for phone-based businesses | Call extension without tracking | No call extension for phone-based business |
| G55 | Lead form extensions | Low | Lead form tested for lead gen accounts | — | Not tested |
| G56 | Audience segments applied | High | Remarketing + in-market audiences in Observation mode | Some audiences applied | No audience signals |
| G57 | Customer Match lists | High | Customer Match list uploaded, refreshed <30 days | List >30 days old | No Customer Match lists |
| G58 | Placement exclusions | High | Account-level placement exclusions (games, apps, MFA sites) | Campaign-level only | No placement exclusions |
| G59 | Landing page mobile speed | High | Mobile LCP <2.5s (ideal <2.0s) | LCP 2.5-4.0s | LCP >4.0s |
| G60 | Landing page relevance | High | Landing page H1/title matches ad group theme | Partial relevance | No relevance to ad group |
| G61 | Landing page schema markup | Medium | Product/FAQ/Service schema present | — | No schema markup |

---

## Performance Max Extended (scored within Ads & Assets)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G-PM1 | Audience signals configured | High | Custom audience signals per asset group | Generic signals only | No audience signals |
| G-PM2 | PMax Ad Strength | High | "Good" or "Excellent" | "Average" | "Poor" |
| G-PM3 | Brand cannibalization | High | <15% of PMax conversions from brand terms | 15-30% from brand terms | >30% from brand terms |
| G-PM4 | Search themes | Medium | Search themes configured (up to 50 per asset group) | <5 search themes | No search themes |
| G-PM5 | Negative keywords | High | Brand + irrelevant negatives applied (up to 10,000) | Some negatives applied | No negative keywords in PMax |

---

## Context Notes

- **ECPC deprecation (March 2025)**: Enhanced CPC is no longer available for new campaigns. Existing ECPC campaigns should migrate to Target CPA, Target ROAS, or Maximize Conversions.
- **Call Campaigns sunset (Feb 2026)**: Google stopped allowing creation of new Call campaigns in February 2026; existing Call campaigns continue serving until February 2027. Migrate to Search campaigns with call assets (call extensions, call-only ad format) before the serving deadline.
- **Power Pack framework**: Google recommends running PMax + Demand Gen + AI Max for Search as a unified campaign stack for maximum coverage across all inventory.
- **AI Max for Search (2025)**: Extends broad match and automated creative to Search campaigns. Evaluate adoption if account has sufficient conversion data.

---

## Bidding & Budget (scored within Settings & Targeting)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G36 | Smart bidding strategy active | High | All campaigns with ≥15 conv/30d use automated bidding | Partially automated | Manual CPC on campaigns with sufficient data |
| G37 | Target CPA/ROAS reasonableness | Critical | Targets within 20% of historical performance | Targets 20-50% off historical | Target CPA <50% of actual CPA |
| G38 | Learning phase status | High | <25% of campaigns in "Learning" or "Learning Limited" | 25-40% in learning | >40% in learning |
| G39 | Budget constrained campaigns | High | Top performers show "Eligible" not "Limited by Budget" | Minor budget limitation | Top performers severely budget-limited |
| G40 | Manual CPC justification | Medium | Manual CPC only on campaigns with <15 conv/month | Manual CPC with 15-30 conv/month | Manual CPC with >30 conv/month |
| G41 | Portfolio bid strategies | Medium | Low-volume campaigns grouped into portfolios | — | Multiple <15 conv campaigns running independently |

---

## Quick Wins (Google)

Items flagged as Quick Win when severity is Critical or High AND fix takes <15 minutes:

| Check | Fix | Time |
|-------|-----|------|
| G43 — Enhanced conversions | Enable in Google Ads conversion settings | 5 min |
| G11 — Location targeting | Switch to "People in" your targeted locations | 2 min |
| G14 — Negative keyword lists | Create initial themed negative lists | 10 min |
| G17 — Broad match + Manual CPC | Switch to Smart Bidding or Exact Match | 5 min |
| G12 — Network settings | Disable Display Network on Search campaigns | 2 min |
| G05 — Brand separation | Split brand keywords into separate campaign | 10 min |
| G50 — Sitelink extensions | Add 4+ sitelinks to campaigns | 10 min |
