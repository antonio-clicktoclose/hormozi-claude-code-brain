<!-- Updated: 2026-02-11 -->
# B2B Enterprise Paid Advertising Template

## Industry Characteristics

- Long sales cycles (3-12+ months)
- Multiple decision makers per deal (6-10 stakeholders average)
- High deal values justify very high CPA ($200-$1,000+)
- Account-based marketing (ABM) is the dominant strategy
- Content consumption heavy — whitepapers, webinars, case studies
- LinkedIn is the primary social platform for B2B decision makers
- Pipeline and revenue metrics matter more than lead volume

## Recommended Platform Mix

| Platform | Role | Budget % | Why |
|----------|------|----------|-----|
| LinkedIn | Primary | 40-55% | Decision-maker targeting by title, company, industry, ABM |
| Google Search | Secondary | 25-35% | High-intent category and solution queries |
| ABM Display | Secondary | 10-15% | Programmatic account-based display targeting |
| Meta | Supporting | 5-10% | Retargeting, lookalikes of closed-won accounts |
| YouTube | Testing | 5% | Thought leadership, product demos, webinar promotion |

## Campaign Architecture

```
Account — LinkedIn
├── ABM — Target Account List
│   ├── Tier 1 Accounts (named accounts, highest spend)
│   ├── Tier 2 Accounts (ICP match, moderate spend)
│   └── Tier 3 Accounts (broader ICP, lower spend)
├── Thought Leader Ads (TLA)
│   ├── CEO/Founder content
│   ├── Subject matter expert content
│   └── Customer success stories
├── Demand Gen
│   ├── Whitepaper/guide offers
│   ├── Webinar registration
│   └── Industry report downloads
├── Retargeting
│   ├── Website visitors (matched audiences)
│   └── Content engagers (video views, lead form opens)
└── Always-On Brand
    └── Company page content promotion

Account — Google
├── Brand Search
├── High-Intent Category
│   ├── [Solution category] + software/platform/solution
│   ├── Enterprise [category]
│   └── [Industry] + [solution type]
├── Competitor
│   ├── [Competitor] alternative
│   └── [Competitor] vs
└── Retargeting (RLSA)
    └── Past visitors searching category terms
```

## Creative Strategy

### What Works for B2B Enterprise
- **Thought Leader Ads (LinkedIn)**: exec-authored content (CPC $2.29-$4.14 vs $13.23 standard)
- **Customer case studies**: specific metrics (ROI, time saved, revenue impact)
- **Industry research**: original data and insights (gated as lead magnet)
- **Product demos**: 60-90s focused on enterprise-grade capabilities
- **Webinar promotion**: live events with industry experts
- **Document Ads (LinkedIn)**: gated content preview — native PDF viewer

### Content by Buyer Stage
| Stage | Content Type | Platform |
|-------|-------------|----------|
| Awareness | Industry insights, trend reports | LinkedIn TLA, YouTube |
| Consideration | Whitepapers, ROI calculators, webinars | LinkedIn, Google |
| Decision | Case studies, product demos, free trial | Google, LinkedIn, Meta retargeting |
| Expansion | Feature updates, customer advisory | Meta retargeting, LinkedIn |

### ABM Creative Personalization
- Company-name personalization in ad copy (LinkedIn matched audiences)
- Industry-specific pain points for vertical campaigns
- Role-specific messaging (IT vs Finance vs Operations)
- Stage-specific offers (awareness: report → consideration: demo → decision: pilot)

## Targeting Strategy

### LinkedIn (Primary)
- **Job titles**: VP, Director, C-suite of [target function]
- **Company size**: 500-1000, 1000-5000, 5000+ (match your ICP)
- **Industries**: your top-converting verticals
- **ABM lists**: upload CRM account lists (matched audiences)
- **Seniority + Function**: layer seniority on top of job function
- **Exclusions**: competitors, existing customers, job seekers

### Google
- **Keywords**: enterprise [solution], [solution] for [industry], [competitor] alternative
- **RLSA**: bid up 50-100% for past website visitors searching category terms
- **Audience layers**: in-market audiences for B2B software, business services

### Account-Based Marketing Tiers
| Tier | Accounts | Budget/Account | Personalization |
|------|----------|----------------|-----------------|
| Tier 1 | 10-50 | $500-2,000/mo | Fully personalized |
| Tier 2 | 50-200 | $100-500/mo | Industry personalized |
| Tier 3 | 200-1,000 | $20-100/mo | ICP personalized |

## Budget Guidelines

| Metric | B2B Enterprise Benchmark |
|--------|------------------------|
| LinkedIn CPC | $5-$35 (TLA: $2.29-$4.14) |
| LinkedIn CPL | $60-$150+ |
| LinkedIn CPM | $31-$38 |
| Google CPC (B2B) | $4.50-$8.00 |
| Google CPL (B2B SaaS) | $100-$200 |
| Meta CPM (B2B) | $35.00 |
| Pipeline:Spend Ratio | 5-10x |
| Min monthly budget | $10,000+ (LinkedIn + Google minimum viable for ABM) |

### Budget Allocation for ABM
| Component | % of Budget |
|-----------|-------------|
| LinkedIn ABM + TLA | 40% |
| Google Search (high intent) | 30% |
| Retargeting (cross-platform) | 15% |
| Content promotion (YouTube, Meta) | 10% |
| Testing | 5% |

## Bidding Strategy Selection

| Platform | Monthly Conversions | Recommended Strategy |
|----------|--------------------|--------------------|
| LinkedIn | Default | Maximum Delivery |
| LinkedIn | Efficiency priority | Manual CPC or Cost Cap |
| LinkedIn | Accelerate campaigns | Auto-optimized (42% lower CPA, 21% lower CPL) |
| Google | <15 | Maximize Clicks (cap CPC) |
| Google | 15-29 | Maximize Conversions |
| Google | 30+ | Target CPA |
| Meta | Default | Lowest Cost (retargeting focus) |

## Attribution & Measurement

- **Attribution window**: 90-day click minimum (enterprise sales cycles)
- **Multi-touch attribution**: track every touchpoint across LinkedIn + Google + direct
- **CRM integration**: map ad interactions to Salesforce/HubSpot pipeline stages
- **Key metrics**: pipeline generated > leads generated (quality > quantity)
- **Influence reporting**: how many deals had ad touchpoints (even if not first/last touch)
- **MQA (Marketing Qualified Account)**: account-level qualification, not just lead-level

## KPI Targets

| Metric | Month 1 | Month 3 | Month 6 |
|--------|---------|---------|---------|
| MQL Volume | Baseline | Stable | Stable |
| MQL → SQL Rate | Track | 15%+ | 25%+ |
| Pipeline Generated | Track | 5x spend | 8x spend |
| Cost per MQA | Baseline | Optimize | Target |
| LinkedIn TLA CTR | Track | 1.0%+ | 1.5%+ |

## Common Pitfalls

- Optimizing for MQL volume instead of pipeline/revenue (MQL farming)
- LinkedIn targeting too narrow (<50K audience) — algorithm can't optimize
- Not using Thought Leader Ads — paying 3-5x more for standard Sponsored Content
- Same content for all buyer stages (one-size-fits-all nurture)
- Ignoring the buying committee — targeting only one persona
- No CRM integration — can't measure true pipeline impact
- Running ABM without a sales alignment plan (marketing generates, sales ignores)
- Short attribution windows (7-day) for 6-month sales cycles (undercounts everything)
