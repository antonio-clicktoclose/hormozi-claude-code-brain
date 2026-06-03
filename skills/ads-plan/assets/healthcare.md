<!-- Updated: 2026-02-11 -->
# Healthcare Paid Advertising Template

## Industry Characteristics

- **HIPAA compliance** governs all marketing involving patient data
- Restricted ad policies on all major platforms (health conditions, treatments)
- LegitScript certification required for addiction treatment and pharmacy ads
- Trust and credibility are paramount — patients research extensively
- High CPCs ($40+ for competitive medical terms)
- Phone calls are a primary conversion (appointment booking)
- Local focus for practices, national for health systems and telehealth
- Insurance acceptance and cost transparency influence decisions

## Compliance Requirements

### HIPAA Marketing Rules
- Never use patient data for ad targeting without explicit written authorization
- Customer Match lists: use ONLY for exclusions, never for targeting with health data
- Retargeting pixel data: cannot be combined with health condition data
- Landing pages: must have privacy policy, cannot collect PHI in ad forms
- Meta CAPI / Google Enhanced Conversions: ensure no PHI transmitted

### Platform-Specific Restrictions
| Platform | Restriction | Certification |
|----------|------------|---------------|
| Google | Healthcare & medicines policy, LegitScript for rehab/pharmacy | LegitScript required for addiction treatment |
| Meta | Restricted targeting for health conditions, no symptom targeting | N/A but policy-reviewed |
| LinkedIn | Less restrictive, B2B healthcare marketing allowed | N/A |
| TikTok | Health misinformation policy, no prescription drug ads | N/A |
| Microsoft | Similar to Google, LegitScript for pharmacy | LegitScript required |

### LegitScript Certification
- **Required for**: addiction treatment, online pharmacy, telehealth prescribing
- **Process**: application, documentation review, site inspection (4-8 weeks)
- **Cost**: $1,000-$2,000 annually
- **Without it**: Google and Microsoft will reject healthcare ads in these categories

## Recommended Platform Mix

| Platform | Role | Budget % | Why |
|----------|------|----------|-----|
| Google Search | Primary | 50-60% | High-intent health queries, local search |
| Meta (FB/IG) | Secondary | 20-25% | Awareness, community building, retargeting |
| YouTube | Secondary | 10-15% | Patient education, doctor introductions, facility tours |
| Microsoft | Testing | 5-10% | Google import, older demographic (45-64: 38% of Bing) |

## Campaign Architecture

```
Account — Google
├── Brand
│   └── [Practice/hospital name], [doctor names]
├── Service-Specific
│   ├── Campaign: [Specialty A] (e.g., "Orthopedics")
│   │   ├── Ad Group: [condition] treatment [city]
│   │   ├── Ad Group: [specialty] doctor near me
│   │   └── Ad Group: [specific procedure]
│   ├── Campaign: [Specialty B]
│   │   └── Same structure
│   └── Campaign: Urgent/Walk-In
│       ├── Ad Group: urgent care near me
│       └── Ad Group: walk in clinic [city]
├── Location Campaigns
│   ├── Ad Group: [practice name] [location A]
│   └── Ad Group: [practice name] [location B]
├── Retargeting (RLSA)
│   └── Website visitors searching health terms
└── YouTube
    └── Doctor introductions, patient education

Account — Meta
├── Awareness
│   ├── Doctor/provider introduction videos
│   ├── Patient success stories (with consent)
│   └── Health education content
├── Lead Generation
│   ├── New patient appointment (Lead Form)
│   ├── Free health screening offer
│   └── Insurance acceptance info
├── Retargeting
│   ├── Website visitors (service page viewers)
│   └── Video viewers (doctor intro, facility tour)
└── Community
    └── Health tips, seasonal wellness, events
```

## Creative Strategy

### What Works for Healthcare
- **Doctor-to-camera videos**: builds trust, shows bedside manner
- **Facility tours**: clean, modern environments reassure patients
- **Patient testimonials**: with explicit consent, specific outcomes (within HIPAA)
- **Educational content**: "5 signs you need to see a [specialist]"
- **Staff introductions**: humanize the practice
- **Insurance/cost transparency**: "We accept [insurance]", "Affordable payment plans"

### Compliance-Safe Creative Guidelines
| Do | Don't |
|----|-------|
| Show facility and equipment | Guarantee specific medical outcomes |
| Feature consenting patient testimonials | Use before/after for medical procedures (platform-specific) |
| Educate about conditions generally | Diagnose or provide medical advice |
| Mention accepted insurance plans | Target by specific health condition |
| Highlight board certifications | Make superiority claims without evidence |

### Ad Copy Framework
- **Headline**: [Specialty/Condition] + [Location] + [Differentiator]
- **Description**: [Benefit] + [Trust signal] + [CTA]
- **Example**: "Board-Certified Orthopedic Surgeons in [City] | Same-Week Appointments | Call Now"

## Targeting Strategy

### Google
- **Location**: radius around practice locations (5-20 miles)
- **Keywords**: [condition] treatment [city], [specialty] doctor near me, [procedure] cost
- **Negative keywords**: home remedies, DIY, Wikipedia, jobs, salary, nursing school
- **Ad schedule**: match office hours + evening research (common for health)

### Meta (Restricted Targeting)
- **Cannot target**: specific health conditions, symptoms, medications
- **Can target**: age ranges (general), geography, general wellness interests
- **Retargeting**: website visitors, video viewers, lead form openers
- **Lookalike/Special Ad Audiences**: based on existing patients (email list, with consent)

### Call Tracking
- Dedicated tracking numbers per campaign
- Call recording (check state consent laws — one-party vs two-party)
- Minimum call duration for qualified lead (30+ seconds)
- Track call → appointment → patient acquisition

## Budget Guidelines

| Metric | Healthcare Benchmark |
|--------|---------------------|
| Google CPC | $10-$40+ (specialty dependent) |
| Google CTR | 4.90% |
| Google CVR | 3.10% |
| Meta CPM | $28-$36.82 |
| Meta CPL | $15-$50 (appointment request) |
| Cost per new patient | $100-$500 (specialty dependent) |
| Patient LTV | $1,000-$10,000+ |
| Min monthly budget | $4,000+ (Google-first approach) |

### Budget by Practice Type
| Practice Type | Monthly Budget | Notes |
|-------------|---------------|-------|
| Single-provider practice | $2,000-$5,000 | Google Search focused |
| Multi-location group | $5,000-$20,000 | Per-location campaigns |
| Hospital system | $20,000-$100,000+ | Service line campaigns |
| Telehealth | $5,000-$15,000 | National Google + Meta |
| Dental | $2,000-$5,000 | Lower CPC ($7.85), higher CVR |

## Bidding Strategy Selection

| Platform | Monthly Conversions | Recommended Strategy |
|----------|--------------------|--------------------|
| Google | <15 | Maximize Clicks (cap CPC) |
| Google | 15-29 | Maximize Conversions |
| Google | 30+ | Target CPA (recommended for healthcare) |
| Meta | Default | Lowest Cost |
| Meta | Efficiency priority | Cost Cap at target CPL |

## KPI Targets

| Metric | Month 1 | Month 3 | Month 6 |
|--------|---------|---------|---------|
| CPL (appointment) | Baseline | Target +20% | Target |
| Cost per New Patient | Track | Baseline | Optimize |
| Call Volume | Track | +20% | +40% |
| Show Rate (appt → visit) | Track | 70%+ | 80%+ |
| Patient Acquisition Cost | Track | <20% of patient LTV | <15% of patient LTV |

## Common Pitfalls

- Violating HIPAA in retargeting (combining health page visits with ad targeting)
- Not obtaining LegitScript certification for addiction/pharmacy (ads rejected)
- Running health condition ads with restricted targeting (policy violations)
- Sending ad traffic to generic homepage instead of condition-specific landing page
- No call tracking — can't measure patient acquisition from ads
- Promising specific medical outcomes in ad copy (policy and legal risk)
- Ignoring after-hours calls — patients searching for urgent care won't wait
- Not tracking appointment show rate — high no-show rates inflate true CPA
- Patient testimonials without proper HIPAA authorization (legal liability)
