# Budget Allocation & Scaling Framework

<!-- Updated: 2026-02-10 -->
<!-- Sources: Google Research PDF 2, Claude Research, Gemini Research -->

## Platform Selection Matrix by Business Type

| Business Type | Platform 1 | Platform 2 | Platform 3 | Other | Min Monthly | Primary KPI | Time to Profit |
|--------------|------------|------------|------------|-------|-------------|-------------|---------------|
| SaaS B2B | Google 35-45% | LinkedIn 30-40% | Meta 15-25% | YouTube 10% | $5,000 | Pipeline ROI, LTV:CAC | 3-6 months |
| E-commerce DTC | Meta 50-68% | Google PMax 23-30% | TikTok 5-15% | Email 5% | $3,000 | ROAS, MER, POAS | 0-2 months |
| Local Service | Google LSA/Search 60% | Meta 30% | Bing 10% | — | $1,500 | Cost Per Lead/Booking | 1 month |
| B2B Enterprise | LinkedIn 39-60% | Google 20-35% | ABM Display 15-20% | Programmatic 11% | $10,000 | Pipeline, SQLs | 6-12 months |
| Info Products | YouTube 40% | Meta 40% | Email 20% | — | $2,000 | ROAS, Webinar CPL | 1-3 months |
| Mobile App | Apple Search 30% | Google App 30% | Meta/TikTok 40% | — | $5,000 | CPI, LTV, D7 Retention | 3-6 months |
| Real Estate | Meta Lead Forms 50% | Google Search 40% | LinkedIn 10% | — | $2,500 | Cost Per Lead | 2-4 months |
| Healthcare | Google Search 55% | Meta 20% | Microsoft 10% | YouTube/Display 15% | $4,000 | Cost Per Patient | 2-5 months |
| Finance/Fintech | Google Search 40-50% | LinkedIn 20-30% | Meta 15% | YouTube/Display 10% | $8,000 | CAC, LTV:CAC | 4-8 months |
| Agency (Own) | LinkedIn 50% | Meta 30% | Google 20% | — | $1,500 | Cost Per Lead | 1-3 months |
| B2C / DTC | Meta 50% | Google 20% | TikTok 30% | — | $2,000 | ROAS, CAC | 1-3 months |

## Budget Distribution Rule: 70/20/10

```
70% → Proven performers (campaigns with established positive ROAS/CPA)
20% → Promising growth (campaigns showing traction, need scale)
10% → Experiments (new platforms, audiences, formats)
```

## Scaling Decision Tree

### 20% Rule (Scale Up)
```
IF actual_CPA < target_CPA by > 10%
AND conversions_last_7d >= learning_threshold
AND campaign NOT in learning phase
THEN increase budget by 20%
→ Wait 3-5 days before next increase
→ Never increase more than 20% at once on Meta (triggers learning reset)
```

### 3× Kill Rule (Pause)
```
IF spend > 3× target_CPA
AND conversions == 0
THEN pause ad/ad set/campaign immediately
→ Review: creative, targeting, landing page, tracking
→ Don't restart without changes
```

### Decreasing Returns Detection
```
IF CPA increased > 15% after last budget increase
THEN roll back to previous budget level
→ Wait 7 days
→ Try horizontal scaling instead (new audiences, platforms)
```

### Saturation Signals
| Platform | Signal | Threshold | Action |
|----------|--------|-----------|--------|
| Google | Impression Share | >80% | Diminishing returns; diversify |
| Meta | Frequency (7-day) | >4.0 | Audience exhausted; refresh creative or expand |
| TikTok | Frequency | >3.0 | Creative fatigue; replace assets |
| LinkedIn | Audience penetration | >50% | Audience exhausted; expand targeting |

## Marketing Efficiency Ratio (MER)

```
MER = Total Revenue / Total Ad Spend (all platforms combined)
```

| Business Type | Healthy MER | Excellent MER | Danger Zone |
|--------------|-------------|---------------|-------------|
| E-commerce | 3.0-5.0 | >5.0 | <2.0 |
| SaaS | Use LTV:CAC (3:1 target) | >4:1 | <2:1 |
| Lead Gen | Revenue/Lead × CVR / CPL | — | <1.5 |

**Why MER over ROAS:**
- ROAS is platform-reported (overclaims by 20-40%)
- MER captures true business economics
- Cross-platform; not inflated by attribution overlap

## Seasonality Adjustments

### Q4 (October-December)
- CPMs increase 30-50%
- Reduce ROAS targets by 20%
- Front-load creative testing in September
- Increase budgets 40-60% for Black Friday / Cyber Monday
- Meta: Advantage+ Sales performs best during peaks

### Q1 (January-March)
- CPMs decrease 20-30% post-holiday
- Best time for new campaign testing
- Aggressive customer acquisition (lower competition)
- Meta Jan 2026 CPC: $0.85 (24% below prior January)

### Q2 (April-June)
- Steady CPMs, good testing window
- Mother's Day / Father's Day spikes for retail

### Q3 (July-September)
- LinkedIn CPC peaks in Q3 ($15.72 average)
- Back-to-school surge for education
- Good time to build retargeting pools for Q4

## Incrementality Testing (Geo-Lift)

### Setup
- Duration: 2-4 weeks minimum
- Holdout: 10% of geographic regions (matched pairs)
- Method: Compare conversion rates exposed vs holdout
- Statistical significance: p < 0.05

### Tools
- Meta: Robyn (R-based, open source) — best for ~80% of orgs
- Google: Meridian (Python, Bayesian, geo-level)
- Advanced: PyMC-Marketing (fully customizable)
- Budget: Significant — allocate 10% of monthly spend for testing

### Post-Purchase Surveys
- Fill ~30% of attribution gap that digital tracking misses
- Question: "How did you first hear about us?"
- Implement on order confirmation page
- Weight responses against platform-reported data

## Minimum Viable Budgets

| Platform | Minimum Monthly | Rationale |
|----------|----------------|-----------|
| Google Ads | $1,000 | 15+ conv/month minimum for Smart Bidding |
| Meta Ads | $600-$800 | 50 conv/week/ad set × $CPA |
| LinkedIn Ads | $3,000 | High CPCs; $10/day minimum × multiple campaigns |
| TikTok Ads | $300 | $50/day campaign min × creative testing needs |
| Microsoft Ads | $200-$300 | 20-30% of Google budget |

## Cross-Platform Attribution Hierarchy

```
Source of Truth (best → worst):
1. CRM Data (actual revenue, closed deals, LTV)
2. MER (total revenue / total ad spend)
3. Post-Purchase Surveys ("How did you hear about us?")
4. Google Analytics 4 (cross-channel, multi-touch)
5. Platform-Reported Data (always overclaims 20-40%)

RULE: Never trust platform-reported ROAS alone.
Always cross-reference with ≥2 other data sources.
```
