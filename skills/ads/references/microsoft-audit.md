# Microsoft Ads Audit Checklist

<!-- Updated: 2026-02-11 -->
<!-- Sources: Google Research PDF 1 (MS01-MS20), Claude Research, Gemini Research -->
<!-- Total Checks: 20 | Categories: 5 | See scoring-system.md for weights and algorithm -->

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Technical Setup | 25% | MS01-MS03 (3 checks) |
| Syndication & Bidding | 20% | MS04-MS07 (4 checks) |
| Structure & Audience | 20% | MS08-MS10 (3 checks) |
| Creative & Extensions | 20% | MS11-MS13 + MS19-MS20 (5 checks) |
| Settings & Performance | 15% | MS14-MS18 (5 checks) |

---

## Technical Setup (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| MS01 | UET tag installed | Critical | Universal Event Tracking tag firing on all pages | Firing on most pages (>90%) | UET tag not installed or broken |
| MS02 | Enhanced conversions | High | Enhanced conversions enabled for improved matching | — | Not enabled |
| MS03 | Google Ads import validation | High | If imported: all settings verified (URLs, extensions, bids) | Minor discrepancies found | Import errors not resolved (broken URLs, missing goals) |

### Import Validation Critical Note
Google Ads imports are the most common Microsoft Ads setup method. Common import issues:
- Conversion goals often break during import
- Tracking templates may not transfer
- Extensions may be partially imported
- Bid adjustments may not match
- ALWAYS validate conversion tracking after import

---

## Syndication & Bidding (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| MS04 | Brand syndication control | Critical | Brand campaigns excluded from syndicated partners OR low-performers excluded | Partners enabled, monitored regularly | Brand campaigns on syndicated partners, never reviewed (massive budget waste risk) |
| MS05 | Audience Network settings | Medium | Audience Network enabled only if testing intentionally | — | Audience Network ON by default without review |
| MS06 | Bid strategy alignment | High | Strategy matches goal + conversion volume; targets 20-35% lower than Google | Strategy matches but targets not adjusted for Bing | Mismatched strategy for conversion volume |
| MS07 | Target New Customers (PMax) | Medium | "Target New Customers" enabled for growth campaigns (Beta 2026) | — | Not tested for eligible PMax campaigns |

---

## Structure & Audience (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| MS08 | Campaign structure | High | Mirrors Google structure (if imported) or follows best practices | Minor structural issues | Disorganized structure, no naming convention |
| MS09 | Budget allocation | Medium | Budget proportional to Bing search volume (typically 20-30% of Google) | Slightly over/under-allocated | Budget >50% of Google budget (over-investment) |
| MS10 | LinkedIn profile targeting | High | LinkedIn targeting utilized for B2B (company, industry, job function) | Partial LinkedIn targeting | No LinkedIn targeting for B2B campaigns (unique advantage missed) |

---

## Creative & Extensions (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| MS11 | RSA asset count | High | ≥8 headlines, ≥3 descriptions per RSA | 3-7 headlines, 2 descriptions | <3 headlines (minimum) |
| MS12 | Multimedia Ads | Medium | Multimedia Ads tested (unique rich visual format) | — | Not tested |
| MS13 | Ad copy uniqueness | Medium | Ad copy optimized for Bing demographics (older, affluent, educated) | Same copy as Google, untested | — |
| MS19 | Action Extension | Medium | Action Extension utilized (unique to Microsoft) | — | Not tested |
| MS20 | Filter Link Extension | Medium | Filter Link Extension tested for product/service categories | — | Not tested |

### Microsoft-Unique Formats
These extensions are ONLY available on Microsoft Ads:
- **Action Extension**: Predefined action buttons (clickable CTAs)
- **Filter Link Extension**: Category-based deep links (product filters)
- **Multimedia Ads**: Rich visual search ads (image + headline + description)
- **Review Extension**: Third-party review quotes in ads

---

## Settings & Performance (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| MS14 | Copilot placement | Medium | Copilot chat placement enabled for PMax campaigns | — | Not enabled (73% higher CTR opportunity) |
| MS15 | Conversion goals | High | Goals configured natively (not relying on Google-imported goals) | Imported goals verified and working | Imported goals not verified |
| MS16 | CPC vs Google comparison | Medium | Microsoft CPC 20-40% lower than Google for same keywords | CPC within 0-20% of Google | CPC equal to or higher than Google |
| MS17 | Conversion rate comparison | Medium | Microsoft CVR comparable to Google | CVR 25-50% lower | CVR >50% lower than Google |
| MS18 | Impression share | Medium | IS tracked for brand and top non-brand terms | Partially tracked | Not tracked |

---

## Quick Wins (Microsoft)

| Check | Fix | Time |
|-------|-----|------|
| MS10 — LinkedIn targeting | Enable LinkedIn profile targeting for B2B campaigns | 5 min |
| MS14 — Copilot placement | Enable Copilot chat placement in PMax settings | 2 min |
| MS04 — Partner network | Review syndicated partner performance, exclude low-performers | 10 min |
| MS19 — Action Extension | Add Action Extension to campaigns | 5 min |
| MS12 — Multimedia Ads | Create Multimedia Ad from existing assets | 10 min |
| MS03 — Import validation | Verify conversion goals and tracking post-import | 10 min |

---

## Microsoft-Specific Context

| Fact | Value |
|------|-------|
| Average CPC | $1.20-$1.55 (20-35% discount vs Google) |
| Average CTR | 2.83-3.1% (higher than Google's ~2.0%) |
| US desktop share | 16.75-17.58%; with partners ~25% |
| Copilot CTR lift | 73% higher than traditional search |
| Copilot CVR lift | 16% stronger conversion rates |
| Copilot journey | 33% shorter customer journeys |
| Purchase intent | 194% more likely to purchase in Copilot |
| Copilot Checkout | Launched Jan 2026 (in-conversation commerce) |
| 37% of advertisers | Report higher ROAS vs Google |
| Bing users click paid ads | 25% more often than Google users |
| Audience skew | Affluent (~50% top 25% HHI), educated (34% degrees), older (45-64: 38%) |
| Import options | Quick Import, Smart Import, Advanced Import (Feb 2025) |
| API version | v13 stable, SOAP-based with REST emerging |

---

## Copilot Integration (2026)

Microsoft's Copilot represents the biggest unique advantage:

1. **Copilot Chat Placement** — Ads appear within conversational search
2. **Copilot Checkout** (Jan 2026) — Full commerce within conversations
3. **Higher engagement** — 73% CTR lift, 16% CVR lift, 33% shorter journeys
4. **Shopping intent** — Users 194% more likely to purchase
5. **Launch partners** — Urban Outfitters, Etsy, Ashley Furniture

Ensure PMax campaigns have Copilot placement enabled to capture this growing channel.
