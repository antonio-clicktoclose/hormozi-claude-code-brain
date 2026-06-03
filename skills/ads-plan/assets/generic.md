<!-- Updated: 2026-02-11 -->
# Generic Paid Advertising Template

## Overview

This template applies to businesses that don't fit neatly into SaaS, e-commerce, local service, B2B enterprise, info products, mobile app, real estate, healthcare, finance, or agency categories. Customize based on your specific business model, goals, and audience.

## Platform Selection Questionnaire

Answer these to determine the right platform mix:

| Question | If Yes → Platform |
|----------|-------------------|
| Do people actively search for your product/service? | Google Search (primary) |
| Do you sell physical products with a catalog? | Google Shopping / PMax |
| Is your audience B2B with specific job titles? | LinkedIn |
| Is your product visual or lifestyle-oriented? | Meta (FB/IG), TikTok |
| Does your audience skew 18-34? | TikTok, Meta (IG) |
| Does your audience skew 35-64? | Google, Meta (FB), Microsoft |
| Is your target audience professional/high-income? | LinkedIn, Microsoft |
| Do you have video content or can produce it? | YouTube, TikTok, Meta |
| Is your budget under $3,000/month? | Focus on 1-2 platforms only |
| Are you in a regulated industry? | Check compliance requirements first |

## Universal Campaign Architecture

```
Account
├── Brand Campaign (always-on)
│   └── Brand name, branded terms, common misspellings
├── Prospecting — High Intent
│   ├── Ad Group/Set: [Product/service] + commercial intent
│   ├── Ad Group/Set: [Category] + buying keywords
│   └── Ad Group/Set: Competitor terms (if strategic)
├── Prospecting — Mid Intent
│   ├── Ad Group/Set: Problem-aware searches
│   └── Ad Group/Set: Category research queries
├── Retargeting
│   ├── Website visitors (7-30 days)
│   ├── Engaged users (video viewers, social engagers)
│   └── Cart abandoners / form starters
└── Testing (10% of budget)
    └── New platforms, audiences, creative formats
```

## Universal Creative Principles

### Ad Copy Framework
Every ad should include:
1. **Hook**: grab attention in first line/3 seconds
2. **Benefit**: lead with what the customer gets (not features)
3. **Proof**: social proof, numbers, credentials
4. **CTA**: clear, specific action ("Get Your Free Quote", not "Learn More")

### Creative Format Priorities
| Priority | Format | Where |
|----------|--------|-------|
| P1 | Short video (15-30s) | Meta, TikTok, YouTube Shorts |
| P2 | Static images with copy | Google, Meta, LinkedIn |
| P3 | Long-form video (60-180s) | YouTube, Meta Feed |
| P4 | Carousel/collection | Meta, LinkedIn |
| P5 | Text-only (RSA) | Google Search, Microsoft |

### Extensions / Enhancements (Google/Microsoft)
- **Sitelinks** (≥4): key pages (pricing, about, contact, reviews)
- **Callouts** (≥4): unique selling points (free shipping, 24/7 support, etc.)
- **Structured snippets**: types, services, brands
- **Call extension**: if phone leads matter
- **Location extension**: if physical location exists
- **Image extension**: product or service visuals

## Universal Targeting Principles

### Start Narrow, Then Expand
1. **Month 1**: exact/phrase match keywords (Google), tight interests (Meta), narrow audiences
2. **Month 2-3**: add broad match with smart bidding (Google), expand interest stacks (Meta)
3. **Month 4+**: test broad targeting, let algorithms optimize with sufficient conversion data

### Universal Negative Keywords (Google/Microsoft)
Add these to every account:
- **Job seekers**: jobs, salary, hiring, careers, internship, resume
- **Information seekers**: what is, Wikipedia, definition, history, PDF
- **Free seekers**: free, cheap, DIY (unless you offer free products)
- **Students**: assignment, homework, essay, university project

### Audience Exclusions
- Existing customers (unless running upsell/retention campaigns)
- Employees and competitors (by company domain or IP exclusion)
- Non-converters with high frequency (Meta: frequency >8 = stale audience)

## Budget Allocation Framework

### 70/20/10 Rule
| Tier | Allocation | Purpose |
|------|-----------|---------|
| Proven (70%) | Platforms/campaigns with confirmed ROI | Revenue engine |
| Scaling (20%) | Platforms showing promise, need more data | Growth engine |
| Testing (10%) | New platforms, audiences, creatives | Innovation |

### Minimum Viable Budgets
| Platform | Minimum Monthly | Why |
|----------|----------------|-----|
| Google Search | $1,000 | Need 15+ conversions/month for smart bidding |
| Meta | $600-$800 | Need 50 conversions/week per ad set for learning |
| LinkedIn | $3,000 | High CPCs ($5-$35) require scale |
| TikTok | $300 | Low CPMs but need creative volume |
| Microsoft | 20-30% of Google | Proportional to search volume share |

## Tracking Setup (Universal)

### Before Launching Any Ads
- [ ] Google Tag Manager installed
- [ ] Google Analytics 4 configured with conversion events
- [ ] Platform pixels installed (Meta, TikTok, LinkedIn, Microsoft)
- [ ] Server-side tracking configured (Meta CAPI, Google Enhanced Conversions)
- [ ] UTM parameter structure defined
- [ ] CRM integration tested (if applicable)
- [ ] Phone call tracking configured (if applicable)
- [ ] Test conversions fired on all platforms

### UTM Structure
```
utm_source=[platform]
utm_medium=paid-[type]
utm_campaign=[campaign-name]
utm_content=[ad-name]
utm_term=[keyword] (search only)
```

## Bidding Strategy Selection

### Google/Microsoft
| Monthly Conversions | Recommended Strategy |
|--------------------|--------------------|
| <15 | Maximize Clicks (cap CPC) |
| 15-29 | Maximize Conversions |
| 30+ | Target CPA |
| 50+ with dynamic values | Target ROAS |

### Meta
| Scenario | Recommended Strategy |
|----------|---------------------|
| Volume priority | Lowest Cost (default) |
| Efficiency priority | Cost Cap |
| Maximum control | Bid Cap |
| Revenue tracking | ROAS Goal |

### Key Rules
- Never change bidding strategy during learning phase
- Wait for 50+ conversions before switching to target-based bidding
- Allow 7-14 days after changes before evaluating results

## Implementation Roadmap

### Phase 1 — Foundation (Weeks 1-2)
- Install tracking (pixels, tags, server-side)
- Set up conversion events and goals
- Build campaign structure and audiences
- Produce first batch of creative
- Launch on primary platform

### Phase 2 — Learn (Weeks 3-6)
- Gather data with conservative budgets
- Identify top-performing campaigns, ads, audiences
- Add negative keywords (search)
- Test 2-3 creative variations

### Phase 3 — Optimize (Weeks 7-12)
- Kill underperformers (3x Kill Rule)
- Scale winners (20% rule)
- Launch secondary platform
- A/B test landing pages
- Upgrade bidding strategy (if conversion threshold met)

### Phase 4 — Scale (Months 4-6)
- Increase budget on proven campaigns
- Expand to testing platforms (10% budget)
- Implement advanced features (PMax, Advantage+, TLA)
- Monthly performance reviews

## KPI Targets

| Metric | Month 1 | Month 3 | Month 6 | Month 12 |
|--------|---------|---------|---------|----------|
| ROAS | Baseline | Target -20% | Target | Target +20% |
| CPA | Baseline | Target +30% | Target | Target -10% |
| CVR | Baseline | +10% | +20% | +30% |
| CTR | Baseline | +15% | +25% | +30% |
| Budget Phase | Testing | Optimizing | Scaling | Maintaining |

## Common Pitfalls

- Launching on too many platforms at once with limited budget
- Not installing conversion tracking before spending money
- Optimizing for vanity metrics (clicks, impressions) instead of conversions
- Changing too many variables at once (can't identify what worked)
- Pausing campaigns during learning phase (resets the algorithm)
- No negative keywords (Google/Microsoft) — paying for irrelevant searches
- Not refreshing creative (fatigue kills performance on all platforms)
- Ignoring mobile experience (82.9% of ad clicks come from mobile devices)
- Measuring platform-reported ROAS without blended MER check
- No retargeting — missing the easiest, highest-converting audience
