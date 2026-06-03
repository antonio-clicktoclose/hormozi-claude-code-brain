<!-- Updated: 2026-02-11 -->
# SaaS Paid Advertising Template

## Industry Characteristics

- Long sales cycles with multiple touchpoints (30-90+ days)
- Free trial or demo request as primary conversion event
- High customer lifetime value justifies high CPA ($100-$200+)
- Heavy comparison shopping — competitor keyword bidding critical
- Integration and ecosystem considerations influence decisions
- Self-serve (low-touch) vs sales-assisted (high-touch) paths differ significantly

## Recommended Platform Mix

| Platform | Role | Budget % | Why |
|----------|------|----------|-----|
| Google Search | Primary | 35-45% | High-intent keyword capture (trial, demo, pricing queries) |
| LinkedIn | Primary | 30-40% | B2B audience targeting (job title, company, industry) |
| Meta | Secondary | 15-25% | Retargeting, lookalikes, brand awareness |
| YouTube | Testing | 5-10% | Product demos, customer stories, thought leadership |
| Microsoft | Testing | 5% | Google import, desktop-heavy B2B audience |

## Campaign Architecture

```
Account
├── Brand Defense
│   └── Brand terms + competitor "vs" terms
├── Non-Brand — High Intent
│   ├── [Product Category] + software/tool/platform
│   ├── Competitor alternatives (best [competitor] alternative)
│   └── Pricing/comparison queries
├── Non-Brand — Mid Intent
│   ├── Problem-aware searches (how to [solve problem])
│   └── Category research (best [category] tools 2026)
├── Retargeting
│   ├── Free trial → paid conversion (CRM audience)
│   ├── Pricing page visitors (7-day window)
│   └── Blog/resource visitors (30-day window)
├── LinkedIn ABM
│   ├── Target account list (matched audiences)
│   ├── Job title targeting (decision makers)
│   └── Thought Leader Ads (founder/exec content)
└── Testing
    └── New audiences, platforms, content angles
```

## Creative Strategy

### What Works for SaaS
- **Product demos**: 30-60s screen recordings showing key workflows
- **Customer testimonials**: video case studies with specific metrics (ROI, time saved)
- **Comparison content**: side-by-side feature comparisons with competitors
- **Founder/CEO content**: authentic thought leadership (LinkedIn TLA, TikTok)
- **ROI calculators**: interactive tools as lead magnets

### Creative by Funnel Stage
| Stage | Format | Message |
|-------|--------|---------|
| Awareness | Video, carousel | Industry problem → your category exists |
| Consideration | Demo video, comparison | Why your product vs alternatives |
| Decision | Testimonial, case study | Specific results, social proof |
| Retention | Feature update, tips | Drive adoption, reduce churn |

## Targeting Strategy

### Google Keywords
- **Brand**: [brand name], [brand] pricing, [brand] vs [competitor]
- **High intent**: [category] software, best [category] tool, [category] platform
- **Competitor**: [competitor] alternative, [competitor] vs, switch from [competitor]
- **Problem**: how to [problem your product solves], [workflow] automation

### LinkedIn Audiences
- Job titles: VP/Director/Manager of [relevant function]
- Company size: match your ICP (SMB, mid-market, enterprise)
- Industries: your top-performing verticals
- ABM: upload target account lists from CRM

### Exclusions (Critical)
- Existing customers (CRM exclusion list)
- Job seekers (LinkedIn: exclude "Job Seeker" interest)
- Competitors (exclude competitor company employees)
- Students/interns (if targeting decision-makers)

## Budget Guidelines

| Metric | SaaS Benchmark |
|--------|---------------|
| Google Search CPC | $4.50-$8.00 |
| Google Search CTR | 4.28% |
| Google Search CVR | 1.65% |
| Google CPL | $100-$200 |
| LinkedIn CPC | $5-$35 (TLA: $2.29-$4.14) |
| LinkedIn CPL | $125 |
| Meta CPC | $1.50-$3.00 |
| Meta CPM | $35.00 |
| Min monthly budget | $5,000+ (Google + LinkedIn minimum viable) |

## Bidding Strategy Selection

| Platform | Monthly Conversions | Recommended Strategy |
|----------|--------------------|--------------------|
| Google | <15 | Maximize Clicks (cap CPC) |
| Google | 15-29 | Maximize Conversions |
| Google | 30+ | Target CPA (recommended for SaaS) |
| Google | 50+ with dynamic values | Target ROAS (if pipeline value tracked) |
| LinkedIn | Default | Maximum Delivery |
| LinkedIn | Efficiency priority | Manual CPC or Cost Cap |
| LinkedIn | Accelerate campaigns | Auto-optimized (42% lower CPA) |
| Meta | Default | Lowest Cost |
| Meta | Efficiency priority | Cost Cap |

## Attribution Model

- Default: data-driven (Google), 7-day click / 1-day view (Meta)
- Track micro-conversions: pricing page view, demo video watch, feature page visits
- Long attribution windows: 30-90 day click for Google (SaaS sales cycles are long)
- CRM integration: connect ad click → MQL → SQL → closed-won for true ROAS
- MER (Marketing Efficiency Ratio): Total ARR / Total ad spend

## KPI Targets

| Metric | Month 1 | Month 3 | Month 6 |
|--------|---------|---------|---------|
| Trial/Demo CPA | Baseline | Target +30% | Target |
| MQL → SQL Rate | Baseline | +10% | +20% |
| Pipeline Value | Tracking | 3x spend | 5x spend |
| ROAS (pipeline) | Tracking | 3:1 | 5:1 |
| Brand Search Volume | Baseline | +15% | +30% |
| Google QS (weighted avg) | Track | ≥6 | ≥7 |
| Meta EMQ | Track | ≥7.0 | ≥8.0 |

## Common Pitfalls

- Optimizing for trial signups without tracking trial → paid conversion (vanity metric)
- Not excluding existing customers from prospecting campaigns
- Running LinkedIn without Thought Leader Ads (standard ads CPC is 3-5x higher)
- Broad match without smart bidding on Google (budget waste)
- Ignoring competitor keyword bidding while competitors bid on your brand
- Same landing page for all funnel stages (demo page for awareness traffic)
- Not implementing offline conversion import (Google) or CAPI (Meta) for lead quality
