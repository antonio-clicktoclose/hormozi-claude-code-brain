<!-- Updated: 2026-02-11 -->
# Marketing Agency Paid Advertising Template

## Industry Characteristics

- Multi-client management — each client has different goals, budgets, and industries
- White-label reporting and branding requirements
- Standardized processes needed for scalable delivery
- Client retention depends on measurable results (ROAS, CPA, pipeline)
- Platform expertise across Google, Meta, LinkedIn, TikTok, Microsoft required
- Agency margin pressure — efficiency and automation are critical
- Client onboarding is a make-or-break phase (first 90 days)
- Continuous education required (platform updates happen weekly)

## Client Onboarding Checklist

### Discovery Phase (Week 1)
- [ ] Business type identified (map to industry template)
- [ ] Goals defined: brand awareness, leads, sales, app installs
- [ ] Current advertising status: platforms, spend, performance history
- [ ] Target audience: demographics, interests, behaviors, company size (B2B)
- [ ] Competitive landscape: top 3-5 competitors identified
- [ ] Budget confirmed: monthly, quarterly, and annual
- [ ] Creative assets inventory: existing images, videos, copy
- [ ] Brand guidelines provided: colors, fonts, tone, do/don't list
- [ ] Access granted: ad accounts, Google Analytics, CRM, product feed

### Technical Setup (Week 2)
- [ ] Tracking audit: pixels, tags, conversions events verified
- [ ] CAPI / server-side tracking configured (Meta, TikTok)
- [ ] Enhanced Conversions enabled (Google, Microsoft)
- [ ] UTM parameter structure defined
- [ ] Google Tag Manager setup verified
- [ ] CRM integration tested (offline conversion import)
- [ ] Attribution model selected and documented
- [ ] Reporting dashboard configured

### Campaign Launch (Weeks 3-4)
- [ ] Campaign architecture built (from industry template)
- [ ] Ad copy written and client-approved
- [ ] Creative assets produced or received
- [ ] Landing pages reviewed (message match, speed, mobile)
- [ ] Audiences built (custom, lookalike, keyword lists)
- [ ] Bid strategy set (conservative for learning phase)
- [ ] Budget pacing configured
- [ ] Conversion tracking verified (test conversion fired)

## Client Industry Template Selection

Map each client to the appropriate industry template:

| Client Type | Template | Key Considerations |
|------------|----------|-------------------|
| SaaS | `saas.md` | Long sales cycle, demo/trial conversions |
| E-commerce | `ecommerce.md` | Product feed, ROAS focus, seasonal |
| Local Service | `local-service.md` | Call tracking, LSA, geo targeting |
| B2B Enterprise | `b2b-enterprise.md` | ABM, LinkedIn, long attribution |
| Info Products | `info-products.md` | Funnel-based, Meta/YouTube primary |
| Mobile App | `mobile-app.md` | MMP required, LTV optimization |
| Real Estate | `real-estate.md` | Special Ad Category, dual audience |
| Healthcare | `healthcare.md` | HIPAA, LegitScript, compliance |
| Finance | `finance.md` | Special Ad Category, disclosures |
| Other | `generic.md` | Adapt based on specifics |

## Agency Platform Selection Matrix

### Client Budget → Platform Recommendations
| Monthly Budget | Recommended Platforms | Reasoning |
|---------------|----------------------|-----------|
| $1,000-$3,000 | Google Search only | Focus on highest-intent channel |
| $3,000-$5,000 | Google + Meta | Add prospecting/retargeting |
| $5,000-$10,000 | Google + Meta + 1 secondary | Based on industry fit |
| $10,000-$25,000 | 3-4 platforms | Full funnel coverage |
| $25,000+ | Full platform mix | Platform-specific optimization |

## Reporting Framework

### Weekly Report (Internal)
- Spend pacing (budget vs actual)
- Key metric trends (CPA, ROAS, CTR, CVR)
- Anomaly alerts (sudden performance drops)
- Action items for the week

### Monthly Client Report
- Executive summary (3-5 key takeaways)
- KPI dashboard (target vs actual)
- Platform-by-platform performance
- Top-performing campaigns, ad groups, creatives
- Recommendations and next steps
- Budget allocation review

### Quarterly Business Review (QBR)
- Goal progress (are we on track?)
- MER analysis (blended efficiency)
- Competitive landscape changes
- Platform updates and new opportunities
- Budget reallocation recommendations
- Next quarter strategy and goals

### Key Metrics by Client Type
| Client Type | Primary KPI | Secondary KPIs |
|------------|-------------|----------------|
| E-commerce | ROAS, MER | AOV, New Customer %, CVR |
| SaaS | Pipeline, CPA | MQL→SQL rate, Demo bookings |
| Lead Gen | CPL, Lead Quality | Show rate, Close rate |
| Local Service | Cost/Booked Job | Call volume, Map actions |
| Brand Awareness | Reach, Frequency | Brand lift, Search volume |

## Agency Operations

### Campaign Naming Convention (Standardized)
```
[Client]_[Platform]_[Objective]_[Audience]_[Geo]_[Date]
```
Example: `ACME_META_CONV_Lookalike1pct_US_2026Q1`

### QA Checklist (Before Launch)
- [ ] Naming convention followed
- [ ] Budget set correctly (daily/lifetime)
- [ ] Targeting verified (geo, audience, exclusions)
- [ ] Ad copy proofread (no typos, brand-compliant)
- [ ] Landing page URL correct and loads <3s
- [ ] Conversion tracking verified (test event)
- [ ] UTM parameters attached
- [ ] Negative keywords added (Search)
- [ ] Ad schedule set (if applicable)
- [ ] Client approval documented

### Optimization Cadence
| Frequency | Action |
|-----------|--------|
| Daily | Spend pacing check, anomaly detection |
| 2x/week | Bid adjustments, creative performance review |
| Weekly | Search term review, negative keyword updates |
| Bi-weekly | Creative refresh assessment, audience review |
| Monthly | Full performance analysis, budget reallocation |
| Quarterly | Strategy review, platform mix evaluation, QBR |

### LinkedIn Accelerate (for B2B Clients)
- Auto-optimized campaigns with 42% lower CPA and 21% lower CPL (LinkedIn benchmarks)
- Recommend for SaaS, B2B Enterprise, Finance, and Agency clients
- Combine with Thought Leader Ads for best results

### 3x Kill Rule (Agency Standard)
Apply across all clients:
- CPA >3x target for 7+ days → pause ad group/campaign
- No conversions after $100 spend or 50 clicks → pause and diagnose
- CTR >50% below benchmark after 1,000 impressions → kill creative
- Creative running >2x refresh cadence → flag for replacement

## Scaling Client Accounts

### When to Scale (Green Light)
- CPA consistently below target for 2+ weeks
- Client satisfied with lead/sale quality
- Creative pipeline can support increased volume
- Landing pages can handle increased traffic
- Budget approved for increase

### 20% Rule (Applied Per Client)
- Never increase budget >20% per week
- Monitor 3-5 days after each increase
- Document performance at each scale step
- Roll back if CPA exceeds target by 30%+

## Common Pitfalls

- No standardized onboarding — every client setup is different (causes errors)
- Not using industry templates — reinventing strategy for every client
- Reporting vanity metrics (impressions, clicks) instead of business outcomes
- Not having a creative production pipeline (creative dies → performance dies)
- Over-promising in sales process (unrealistic ROAS/CPA targets)
- Not tracking MER — per-platform ROAS masks true efficiency
- Skipping the QA checklist — one wrong decimal in budget = client trust destroyed
- Not documenting what works — tribal knowledge leaves with departing team members
