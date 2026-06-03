# LinkedIn Ads Audit Checklist

<!-- Updated: 2026-02-11 -->
<!-- Sources: Google Research PDF 1 (L01-L25), Claude Research, Gemini Research -->
<!-- Total Checks: 25 | Categories: 5 | See scoring-system.md for weights and algorithm -->

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Technical Setup | 25% | L01-L02 (2 checks) |
| Audience Quality | 25% | L03-L09 (7 checks) |
| Creative & Formats | 20% | L10-L13 (4 checks) |
| Lead Gen Forms | 15% | L14-L15 (2 checks) |
| Bidding & Budget | 15% | L16-L17 (2 checks) |
| Structure & Performance | — | L18-L25 (8 checks, scored across categories) |

---

## Technical Setup (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L01 | Insight Tag installed | Critical | LinkedIn Insight Tag firing on all pages | Firing on most pages (>90%) | Tag not installed or broken |
| L02 | Conversions API (CAPI) | High | Server-side conversion tracking active (launched 2025) | Planned but not deployed | No server-side tracking |

---

## Audience Quality (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L03 | Job title targeting precision | High | Specific job titles matching ICP (not just functions) | Broad function targeting only | No job title targeting |
| L04 | Company size filtering | Medium | Company size matches ICP | Includes all sizes | — |
| L05 | Seniority level targeting | High | Seniority appropriate for offer (C-suite for enterprise, Manager for mid-market) | Broad seniority targeting | Mismatched seniority level |
| L06 | Matched Audiences | High | Website retargeting + contact list audiences active | One type active | No matched audiences |
| L07 | ABM company lists | Medium | Target company lists uploaded (up to 300,000) for ABM | Partial list uploaded | No ABM lists for enterprise campaigns |
| L08 | Audience expansion setting | Medium | OFF for precise targeting, ON for scale (intentional) | — | Default ON without review |
| L09 | Predictive audiences | Medium | Predictive audiences tested (replaced Lookalikes Feb 2024) | — | Not tested for eligible campaigns |

---

## Creative & Formats (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L10 | Thought Leader Ads (TLAs) | High | TLAs active, receiving ≥30% of budget for B2B | TLAs tested but <30% budget | No TLAs (CPC $2.29-4.14 vs $13.23 standard) |
| L11 | Ad format diversity | High | ≥2 formats tested (single image, video, document, carousel) | 1 format only | — |
| L12 | Video ads present | Medium | Video ads tested | — | No video tested |
| L13 | Creative refresh cadence | Medium | Creative refreshed every 4-6 weeks | Refreshed every 6-10 weeks | Same creative >10 weeks |

---

## Lead Gen Forms (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L14 | Lead Gen Form optimization | High | ≤5 fields (reduce friction); 13% CVR benchmark | 6-8 fields | >8 fields (high friction) |
| L15 | Lead Gen Form CRM integration | High | Form synced to CRM in real-time | Synced within 24hrs | Manual CSV download only |

---

## Bidding & Budget (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L16 | Bid strategy appropriate | High | CPS for Message Ads; Maximum Delivery or Manual for Sponsored Content | — | Manual CPC without experience to manage |
| L17 | Budget sufficiency | High | Daily budget ≥$50 for Sponsored Content | $25-$50/day | <$25/day ($10 minimum, insufficient for learning) |

---

## Structure & Performance (scored across categories)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L18 | Campaign objective alignment | High | Objective matches funnel stage | — | Objective mismatched to goal |
| L19 | A/B testing active | Medium | Active A/B test on creative or audience | Test planned | No testing |
| L20 | Frequency monitoring | High | Message frequency ≤1 per 30-45 days per user | 1 per 20-30 days | >1 per 20 days (inbox fatigue) |
| L21 | CTR benchmark | High | Sponsored Content CTR ≥0.44% | CTR 0.30-0.44% | CTR <0.30% |
| L22 | CPC benchmark | Medium | CPC within industry benchmark ($5-7 avg, senior $6.40+) | CPC 20-50% above benchmark | CPC >50% above benchmark |
| L23 | Lead quality tracking | High | Lead-to-opportunity rate tracked (not just CPL) | CPL tracked only | No lead quality metrics |
| L24 | Conversion tracking attribution | Medium | 30-day click / 7-day view window configured | Default window without review | Attribution not configured |
| L25 | Demographics report review | Medium | Job title and company breakdown reviewed monthly | Reviewed quarterly | Never reviewed |

---

## Quick Wins (LinkedIn)

| Check | Fix | Time |
|-------|-----|------|
| L01 — Insight Tag | Install/verify Insight Tag on all pages | 10 min |
| L10 — Thought Leader Ads | Create TLA using employee organic posts | 10 min |
| L14 — Lead Gen Form fields | Reduce form to ≤5 fields | 5 min |
| L08 — Audience expansion | Review and set intentionally (OFF for precision) | 2 min |
| L20 — Message frequency | Set frequency cap to 1 per 30-45 days | 2 min |
| L24 — Attribution window | Configure 30-day click / 7-day view | 2 min |

---

## Context Notes

- **Connected TV Ads (2025)**: LinkedIn extended reach to CTV inventory via partnerships, allowing B2B brand campaigns on streaming platforms.
- **BrandLink (2025)**: Premium video placement alongside trusted publisher content on LinkedIn. Ideal for awareness-stage B2B campaigns.
- **Live Event Ads (2025)**: Sponsored LinkedIn Live events with built-in registration and reminder flows. Effective for webinar-driven lead gen.
- **Accelerate campaigns**: LinkedIn's AI-optimized campaign type delivers 42% lower CPA and 21% lower CPL on average. Recommended for advertisers with sufficient conversion history.

---

## LinkedIn-Specific Context

| Fact | Value |
|------|-------|
| Minimum audience for delivery | 500 members |
| Recommended audience size | 50,000-300,000 |
| Predictive Audiences seed | 300+ members |
| Company list upload limit | 300,000 |
| Lookalike audiences | Discontinued Feb 29, 2024 |
| Lead Gen Form CVR benchmark | 13% (3.25x landing pages) |
| B2B ROAS benchmark | 113% ($1.13 per $1 spent) |
| Accelerate campaigns | 42% lower CPA, 21% lower CPL |
| TLA CPC advantage | $2.29-4.14 vs $13.23 standard |
| Campaign hierarchy (Oct 2025) | "Campaign Groups" → "Campaigns"; "Campaigns" → "Ad Sets" |
