<!-- Updated: 2026-02-11 -->
# Local Service Business Paid Advertising Template

## Industry Characteristics

- Geographic-focused with tight radius targeting (5-30 miles)
- Phone calls are the primary conversion (60%+ of leads)
- High intent — emergency/urgent service needs drive immediate action
- Reviews and trust signals heavily influence decisions
- Mobile-first user behavior (82.9% of local searches on mobile)
- Seasonal demand patterns (HVAC, plumbing, roofing, landscaping)
- Competitive local markets with limited keyword volume

## Recommended Platform Mix

| Platform | Role | Budget % | Why |
|----------|------|----------|-----|
| Google Local Services Ads (LSA) | Primary | 40-50% | Pay-per-lead, Google Guaranteed badge, top placement, cheapest CPL ($25-$75) |
| Google Search PPC | Primary | 20-25% | High-intent local queries ("near me", "[service] [city]") |
| Meta (FB/IG) | Secondary | 15-20% | Local awareness, retargeting, seasonal promotions |
| Microsoft/Bing | Testing | 5-10% | Google import, older demographic alignment |

## Campaign Architecture

```
Account — Google
├── LSA (Local Services Ads)
│   └── Google Guaranteed — all services listed
├── Brand Search
│   └── Brand name + brand + city terms
├── Service-Specific Campaigns
│   ├── Campaign: [Service A] (e.g., "Plumbing")
│   │   ├── Ad Group: Emergency [service]
│   │   ├── Ad Group: [service] + [city]
│   │   └── Ad Group: [specific sub-service]
│   └── Campaign: [Service B]
│       └── Same structure
├── Competitor Campaign
│   └── Competitor brand names (if strategic)
└── Seasonal/Promotional
    └── Seasonal offers, maintenance specials

Account — Meta
├── Local Awareness
│   └── 10-20 mile radius, age 25-65
├── Retargeting
│   ├── Website visitors (30 days)
│   └── Engaged Facebook/IG users
└── Seasonal Promotions
    └── Time-sensitive offers, maintenance reminders
```

## Creative Strategy

### What Works for Local Services
- **Before/after photos**: transformation content (roofing, landscaping, painting)
- **Team/truck photos**: real people, real vehicles, builds trust
- **Video testimonials**: local customers sharing their experience
- **Offer-driven**: "$50 off first service", "free estimate", seasonal pricing
- **Emergency messaging**: "Same-day service", "24/7 available", "Call now"
- **Review highlights**: screenshot or quote from Google reviews

### Ad Copy Priorities
| Element | Priority | Example |
|---------|----------|---------|
| Location | Must have | "Serving [City] & Surrounding Areas" |
| Phone number | Must have | Call extensions on every campaign |
| Offer | High | "$50 Off First Visit" or "Free Estimate" |
| Trust signal | High | "Licensed & Insured", "4.9★ (200+ Reviews)" |
| Urgency | Medium | "Same-Day Service Available" |

### Extensions (Google)
- **Call extension**: on every campaign (primary conversion)
- **Location extension**: linked to Google Business Profile
- **Sitelinks**: services, reviews, about us, contact
- **Callout**: licensed, insured, free estimates, X years experience
- **Structured snippets**: service types offered

## Targeting Strategy

### Google
- **Location**: 10-20 mile radius around service area (or specific ZIP codes)
- **Keywords**: [service] + [city], [service] near me, emergency [service]
- **Match type**: Exact and Phrase (Broad only with smart bidding and sufficient data)
- **Negative keywords**: DIY, jobs, salary, training, how to (informational intent)
- **Ad schedule**: match business hours unless 24/7 emergency service

### Meta
- **Radius targeting**: 10-20 miles from business location
- **Age**: 25-65 (homeowners, decision makers)
- **Interests**: homeownership, home improvement, recently moved
- **Exclusions**: renters (if targeting homeowners), existing customers (if new-only)

### Call Tracking (Critical)
- Google forwarding numbers on all ads
- Separate tracking numbers for LSA vs Search vs Meta
- Call recording enabled (legal compliance check per state)
- Minimum 30-second call = qualified lead
- Track call → appointment → completed job for true CPA

## Budget Guidelines

| Metric | Local Service Benchmark |
|--------|----------------------|
| Google Search CPC | $7.85-$30 (varies by service type) |
| Google Search CTR | 5.50-6.37% |
| Google Search CVR | 7.33-15.0% |
| Google CPL | $90.92 |
| LSA CPL | $25-$75 (varies by service) |
| Meta CPM | $18.00 |
| ROAS | 5.0x (high margin services) |
| Min monthly budget | $1,500+ (Google Search + LSA) |

### Budget by Service Type (Monthly Minimums)
| Service Type | Google Min | LSA Min | Meta Min |
|-------------|------------|---------|----------|
| HVAC | $2,000 | $500 | $500 |
| Plumbing | $1,500 | $500 | $300 |
| Roofing | $2,500 | $500 | $500 |
| Landscaping | $1,000 | N/A | $500 |
| Cleaning | $800 | $300 | $300 |
| Pest Control | $1,000 | $300 | $300 |

## Bidding Strategy Selection

| Platform | Monthly Conversions | Recommended Strategy |
|----------|--------------------|--------------------|
| Google | <15 | Maximize Clicks (cap CPC) |
| Google | 15-29 | Maximize Conversions |
| Google | 30+ | Target CPA (recommended for local) |
| LSA | N/A | Pay-per-lead (no bidding strategy — set max CPL) |
| Meta | Default | Lowest Cost |
| Meta | Efficiency priority | Cost Cap at target CPL |

## KPI Targets

| Metric | Month 1 | Month 3 | Month 6 |
|--------|---------|---------|---------|
| CPL (Search) | Baseline | Target +20% | Target |
| CPL (LSA) | Baseline | Optimize | <$50 |
| Call Volume | Track | +20% | +40% |
| Booked Job Rate | Track | 30%+ | 40%+ |
| Cost per Booked Job | Track | <2x CPL | <1.5x CPL |

## Seasonal Strategy

| Season | Action |
|--------|--------|
| Spring | Ramp up: HVAC tune-ups, landscaping, spring cleaning |
| Summer | Peak: AC repair, outdoor services, pest control |
| Fall | Transition: heating prep, gutter cleaning, winterization |
| Winter | Emergency focus: heating repair, pipe freeze, snow removal |
| Pre-season | Increase budget 30% in month before peak (learning phase) |

## Common Pitfalls

- Under-investing in LSA — should be 40-50% of budget (cheapest leads for local services)
- Targeting too wide a radius (30+ miles when you serve 15 miles)
- No call tracking — can't measure true lead volume or quality
- Running ads outside business hours without after-hours answering
- Same bid for emergency keywords and non-emergency (emergency CPC tolerance is higher)
- Not linking Google Business Profile to Google Ads (location extensions, LSA)
- Ignoring seasonality — flat budget year-round instead of scaling with demand
- Sending Meta traffic to homepage instead of dedicated landing page with phone number
