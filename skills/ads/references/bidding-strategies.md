# Bidding Strategy Decision Trees

<!-- Updated: 2026-02-10 -->
<!-- Sources: Google Research PDF 2, Claude Research, Gemini Research -->

## Google Ads Bidding Decision Engine

### Strategy Selection Flow

```
START → How many conversions in last 30 days?

┌─ < 15 conversions ──────────────────────────┐
│  → Maximize Clicks (cold start)             │
│  → Set Max CPC = Target_CPA / (CVR × 1.5)  │
│  → Learning: 3-5 days                       │
│  → Monitor until 15+ conversions achieved    │
│  → OR use Manual CPC if full control needed  │
│  → NOTE: eCPC deprecated March 31, 2025      │
└──────────────────────────────────────────────┘

┌─ 15-29 conversions ─────────────────────────┐
│  → Maximize Conversions (uncapped)          │
│  → Learning: 7-14 days                      │
│  → Transition when CPA SD < 20% over 14d   │
│  → THEN switch to Target CPA               │
└──────────────────────────────────────────────┘

┌─ 30+ conversions, NO dynamic values ────────┐
│  → Target CPA                               │
│  → Strict: 30+ (Google says 15, but 30+     │
│    for reliable performance, 50+ ideal)      │
│  → Set at: 1.1x-1.2x historical CPA        │
│  → Adjust: Max 10% change every 14 days     │
│  → Never lower by more than 15% at once     │
└──────────────────────────────────────────────┘

┌─ 50+ conversions WITH dynamic values ───────┐
│  → Target ROAS                              │
│  → Requires dynamic conversion values        │
│  → Set at: EXACT historical ROAS            │
│  → Formula: Bid = P(conv) × Value × 1/tROAS│
│  → Adjust: Same rules as tCPA              │
└──────────────────────────────────────────────┘

### Smart Bidding Exploration (Google, 2025+)

An opt-in feature for Target ROAS campaigns that temporarily eases
ROAS targets to discover new, untapped search traffic:

- **Effect**: +18% more unique search query categories, +19% more conversions
- **How it works**: Algorithm temporarily relaxes ROAS constraints to
  enter auctions it would normally skip, testing new user segments
- **When to enable**: Stable tROAS campaigns with 50+ conversions/month
  seeking incremental growth beyond current query coverage
- **When to avoid**: Tight-margin accounts or campaigns already spending
  full budget (exploration adds volume, not just efficiency)
- **Available on**: Target ROAS bid strategies only

┌─ Brand Protection campaigns ────────────────┐
│  → Target Impression Share                  │
│  → Target: 95-100% on brand keywords        │
│  → No conversion data requirement           │
│  → Search only (not available elsewhere)     │
└──────────────────────────────────────────────┘

SPECIAL CASES:
- PMax: Always uses Maximize Conversions or Maximize Conv Value
- Demand Gen: Supports Target CPC (new), tCPA, tROAS, Max Clicks
- Display Pay per Conversion: Eligibility required
```

### Attribution Model (Google)
- **DDA (Data-Driven Attribution) is now MANDATORY default** (September 2025)
- Only two models remain: DDA and Last Click
- All rule-based models deprecated (first-click, linear, time decay, position-based)
- No minimum data threshold for DDA
- Impact on bidding: DDA distributes conversion credit across touchpoints, affecting Smart Bidding signals

### Portfolio Bid Strategies

When to use portfolios:
- Multiple campaigns each with <15 conv, but combined >30
- Need cross-campaign budget optimization
- **CPC Cap Hack**: Only way to set max CPC bid on tCPA/tROAS

Rules:
- Minimum 3 campaigns per portfolio for meaningful data
- Group campaigns with similar target CPAs/ROAS
- Never mix brand and non-brand in same portfolio

### Transition Triggers (Google)

| From | To | Trigger |
|------|----|---------|
| Maximize Clicks | Maximize Conversions | 15+ conversions in 30 days |
| Maximize Conversions | Target CPA | CPA SD <20% over 14 days + 30+ conv |
| Target CPA | Target ROAS | 50+ conv + dynamic values available |
| Manual CPC | Maximize Clicks | Ready to test automation |
| Any | Target Impression Share | Brand protection need identified |

---

## Meta Ads Bidding Decision Engine

### Auction Formula

```
Total Value = Bid × Estimated Action Rate + User Value
```

### Strategy Selection

```
DEFAULT (90% of campaigns):
  → Lowest Cost (no cap)
  → Best for: Most campaigns, volume maximization
  → Risk: CPA can spike during high-competition (Q4)

IF need cost predictability:
  → Cost Cap
  → Set at: 1.2x - 1.5x target CPA
  → Best for: Scaling with margin protection
  → Risk: Under-delivery if cap too aggressive

IF need strict cost control:
  → Bid Cap
  → Set at: 2x - 3x target CPA
  → Best for: Experienced advertisers with clear unit economics
  → Risk: Significant under-delivery if too low

IF e-commerce with revenue tracking:
  → ROAS Goal
  → Best for: Advantage+ Sales Campaigns
  → Requires: Purchase event + dynamic values

IF high-value diverse products:
  → Highest Value
  → Prioritizes high-value conversions
  → Best for: Wide AOV range
```

### CBO vs ABO Decision

```
IF daily_budget < $100:
  → ABO (manual control for testing)

IF daily_budget $100-$500:
  → Test both; CBO if similar audiences, ABO if diverse

IF daily_budget > $500:
  → CBO (Advantage+ Campaign Budget)
  → Let Meta optimize distribution

NOTE: Advantage+ Sales/Leads auto-enable CBO
```

### Learning Phase Rules

**Exit criteria:** 50 conversions per week per ad set

**Reset triggers (avoid during learning):**
- Budget change >20%
- Any targeting change
- Creative edit (even text)
- Bid strategy change
- Pausing >7 days

**If "Learning Limited":**
1. Broaden audience
2. Increase budget
3. Switch to higher-funnel event (AddToCart instead of Purchase)
4. Consolidate ad sets
5. Ensure daily budget ≥5× target CPA

---

## LinkedIn Ads Bidding

### Strategy Selection

```
Sponsored Content:
  → Maximum Delivery (recommended default)
  → Manual Bidding (for CPC control, experienced only)
  → Minimum daily budget: $10/day (recommend $50+)

Message Ads:
  → CPS (Cost Per Send) — bid aggressively
  → Frequency cap: 1 per 30-45 days per user
  → Win the auction for limited inbox slot

Lead Gen Forms:
  → Lowest Cost or Manual CPC
  → 13% CVR benchmark (3.25× landing pages)

Conversation Ads:
  → CPS — similar to Message Ads
  → 10-12% CTR benchmark

TLA (Thought Leader Ads):
  → Allocate ≥30% budget
  → CPC $2.29-$4.14 (vs $13.23 standard)

Accelerate Campaigns:
  → AI-powered end-to-end
  → 42% lower CPA, 21% lower CPL
```

---

## TikTok Ads Bidding

### Strategy Selection

```
DEFAULT:
  → Lowest Cost (volume maximization)
  → Most common, good starting point

IF margin protection needed:
  → Cost Cap
  → Set target CPA, system tries to stay near

IF strict cost control needed:
  → Bid Cap
  → Controls maximum bid per auction (not average CPA)
  → Set at 2-3x target CPA initially
  → Best for: retargeting, competitive niches (Q4/BFCM)
  → Risk: significant under-delivery if set too aggressively

IF Smart+ campaign:
  → Modular automation (choose per module)
  → Up to 30 ad groups, 50 creatives per asset group

GMV Max (TikTok Shop):
  → Default/only for Shop campaigns (July 2025)
  → Optimizes for Gross Merchandise Value
```

### Budget Rules
- Campaign minimum: $50/day
- Ad group minimum: $20/day
- Budget should be ≥50× target CPA per ad group (provides sufficient learning room)
- Learning phase: ~50 conversions in 7 days

---

## Microsoft Ads Bidding

### Strategy Selection

```
IF importing from Google:
  → Match Google bid strategy
  → Validate settings transferred correctly
  → Adjust targets (typically 20-35% lower CPC on Bing)

IF native campaign:
  → Same strategy framework as Google
  → Lower CPC targets (expect $1.20-$1.55 avg)
  → Enable Copilot placement for PMax

PMax on Microsoft:
  → Enable "Target New Customers" (Beta 2026)
  → Copilot chat placement: 73% higher CTR
  → LinkedIn profile targeting (unique)
```

---

## Cross-Platform Bidding Red Flags

| Red Flag | Severity | Platform | Action |
|----------|----------|----------|--------|
| Broad Match + Manual CPC | Critical | Google | Switch to Smart Bidding or Exact Match |
| tCPA <50% of actual CPA | Critical | Google | Unrealistic target; set at 1.1-1.2× historical |
| Smart Bidding with <15 conv/month | High | Google | Use Manual CPC or Maximize Clicks |
| >50% ad sets "Learning Limited" | Critical | Meta | Consolidate, broaden audience, increase budget |
| Cost Cap below historical CPA | High | Meta | Set at 1.2-1.5× target, not below |
| Daily budget <5× CPA | High | Meta | Increase budget or switch to higher-funnel event |
| Budget < $50/day campaign | High | TikTok | Increase to minimum or consolidate |
| No negative keywords with Broad Match | Critical | Google | Add themed negative lists immediately |
| No Portfolio strategy for low-vol campaigns | Medium | Google | Group <15 conv campaigns into portfolio |
