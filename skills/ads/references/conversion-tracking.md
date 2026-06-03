# Conversion Tracking Setup & Requirements

<!-- Updated: 2026-02-10 -->
<!-- Sources: Google Research PDF 2, Claude Research, Gemini Research -->

## Google Ads Conversion Tracking

### Required Stack
```
1. Global Site Tag (gtag.js) → all pages
2. Enhanced Conversions → hashed first-party data (email, phone, address, name)
3. Consent Mode v2 → MANDATORY for EU/EEA since March 2024
4. Server-Side GTM → recommended for data durability
5. Offline Conversion Import → for lead gen (CRM → Google Ads)
```

### Enhanced Conversions
- Sends SHA-256 hashed first-party data
- Improves measurement by ~10% more measured conversions
- Required for smart bidding accuracy in cookie-degraded environments
- Setup via gtag.js or Google Tag Manager
- Works alongside standard conversion tracking

### Consent Mode v2
```javascript
// Default (before consent)
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied'
});

// After user grants consent
gtag('consent', 'update', {
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'analytics_storage': 'granted'
});
```
- Enables conversion modeling for unconsented users
- Advanced mode recovers 30-50% of lost conversions
- Without implementation: 90-95% metric drops (enforcement tightened July 2025)
- ~31% of users accept tracking cookies globally

### Attribution
- **DDA (Data-Driven Attribution) is now MANDATORY default** (September 2025)
- Only two models remain: DDA and Last Click
- All rule-based models deprecated (first-click, linear, time decay, position-based)
- No minimum data threshold for DDA
- Windows: Click 1/3/7/30(default)/60/90 days; Engaged-view 3d; View-through 1d

### Customer Match
- Requires 90 days of account history and $50,000+ lifetime spend for full access
- Maximum membership duration: 540 days (changed April 7, 2025; previously infinite)
- Use for RLSA, similar audiences, and Customer Match lists
- First-party data source: CRM emails, phone numbers, addresses

### Conversion Setup Rules
- Use Google Ads native tracking as PRIMARY for bidding (real-time data)
- Import GA4 conversions for observation only
- Never count both (double-counting)
- Separate micro (AddToCart, TimeOnSite) from macro (Purchase, Lead) conversions
- Only macro conversions as "Primary" for bidding optimization

---

## Meta Ads Conversion Tracking

### Required Stack
```
1. Meta Pixel → base code on all pages + standard events
2. Conversions API (CAPI) → server-side event forwarding
3. Event Deduplication → event_id matching between Pixel and CAPI
4. EMQ Optimization → pass email, phone, fbp, fbc, external_id
```

### Event Match Quality (EMQ) Scoring
| Score | Rating | Action |
|-------|--------|--------|
| <4.0 | Critical | Severe data loss; urgent fix needed |
| 4.0-5.9 | Warning | Significant signal gaps |
| 6.0-7.9 | Acceptable | Some optimization possible |
| 8.0-10.0 | Excellent | Maximum signal strength |

**Key parameters by impact:**
- Email: +4.0 points
- Phone: +3.0 points
- External ID: significant
- fbp (browser ID): important
- fbc (click ID): important

**87% of advertisers have poor EMQ** — fixing it improves performance 20-40%.

### Event Deduplication
```
Same event_id + same event_name = deduplicated (correct)
Missing event_id = potential double-counting (broken)

Check: Events Manager > Overview > Deduplication Rate
Target: 90%+ deduplication rate
```

### CAPI Performance Impact
- Without CAPI: 30-40% data loss post-iOS 14.5 (pixel-only tracking is critically insufficient)
- With CAPI: 15-20% performance increase over pixel-only
- Bypasses ad blockers and iOS ATT limitations
- 87% of advertisers have poor Event Match Quality — fixing CAPI improves performance 20-40%
- Offline Conversions API deprecated May 2025 → CAPI replaces

### Standard Events (Use These, Not Custom)
```
Purchase, AddToCart, InitiateCheckout, AddPaymentInfo,
Lead, CompleteRegistration, Subscribe, ViewContent,
Search, AddToWishlist, Contact, CustomizeProduct,
FindLocation, Schedule, StartTrial, SubmitApplication
```

### Attribution
- 7-day click / 1-day view (default and recommended)
- Top 8 events configured in AEM (Aggregated Event Measurement)
- Domain verification required in Business Manager
- Financial Products & Services = new Special Ad Category (Jan 2025)

---

## TikTok Ads Conversion Tracking

### Required Stack
```
1. TikTok Pixel → base code + standard events on all pages
2. Events API → server-side event forwarding
3. ttclid Passback → capture from URL params, send with events
4. Advanced Matching → hashed email/phone
```

### Key Difference: ttclid
- TikTok Click ID (ttclid) comes in landing page URL parameters
- MUST be captured and stored on first page load
- MUST be sent back with all conversion events
- Without ttclid: attribution breaks for many conversions

### Learning Phase
- ~50 conversions in 7 days to exit learning
- Budget ≥50× target CPA per ad group (provides sufficient learning room)

---

## LinkedIn Ads Conversion Tracking

### Required Stack
```
1. LinkedIn Insight Tag → all pages
2. Conversions API (CAPI) → server-side events (launched 2025)
3. Offline Conversion Import → CRM data (opportunity, deal closed)
```

### Best Practice: Track Full Funnel
```
Stage 1: Lead (form submit, content download)
Stage 2: MQL (marketing qualified)
Stage 3: SQL (sales qualified)
Stage 4: Opportunity Created
Stage 5: Deal Closed-Won
```
- Import offline conversions within 90 days of click
- Use for lead quality optimization (bid for SQLs not just leads)
- Lead Gen Forms: 13% CVR (3.25× landing pages) but lower SQL rates

### Attribution
- 30-day click / 7-day view window
- Last touch model default

---

## Microsoft Ads Conversion Tracking

### Required Stack
```
1. UET (Universal Event Tracking) tag → all pages
2. Enhanced Conversions → improved matching
3. Offline Conversion Import → CRM integration
4. Auto-tagging (MSCLKID) → ensure CMS doesn't strip
```

### Import Validation
- If importing from Google: verify conversion goals transferred
- Google-imported goals often break during import
- Always validate conversion tracking after import

---

## Cross-Platform Tracking Health Audit

### Critical Checks (Run for All Platforms)

| Check | Severity | Pass Criteria |
|-------|----------|---------------|
| Primary conversion action exists | Critical | ≥1 active conversion per platform |
| Server-side tracking active | Critical | CAPI/Server GTM/Events API configured |
| Event deduplication | Critical | event_id matching (Meta), no double-counting |
| Consent Mode v2 (EU) | Critical | Implemented if serving EU/EEA |
| Enhanced Conversions / EMQ | High | Google: enabled; Meta: EMQ ≥6.0 |
| Micro vs macro separation | High | Only macro conversions set as Primary |
| Attribution model appropriate | Medium | DDA (Google), 7d/1d (Meta) |
| Conversion window matches cycle | Medium | 7d (ecom), 30-90d (B2B), 30d (lead gen) |
| Offline conversion import | Medium | Active for lead gen / B2B accounts |
| First-party data utilization | High | Customer Match / Custom Audiences from CRM |

### Server-Side Tracking Priority
```
IF business_type IN [ecommerce, lead_gen, saas]:
  server_side_tracking = CRITICAL

IF platform == "Meta":
  CAPI = CRITICAL (30-40% data loss without post-iOS 14.5)

IF region == "EU/EEA":
  consent_mode_v2 = CRITICAL (90-95% metric drops without)

server_side_recovery = 10-30% accuracy improvement
```
