# Platform Creative Specifications

<!-- Updated: 2026-02-10 -->
<!-- Sources: Google Research PDF 3, Claude Research -->

## Google Ads

### Responsive Search Ads (RSA)
| Component | Min | Max | Char Limit |
|-----------|-----|-----|------------|
| Headlines | 3 | 15 | 30 chars each |
| Descriptions | 2 | 4 | 90 chars each |
| Display Paths | — | 2 | 15 chars each |
| Final URL | 1 | 1 | Required |

Best practice: 8-10 headlines, 2-3 descriptions (Claude), 12-15 for Excellent (Google).

**Pinning Rules:**
- Pin 1 headline to Position 1 (brand/main keyword)
- Pin 1 headline to Position 2 (secondary angle)
- Each pinned position: provide 2-3 variants
- Leave Position 3 unpinned
- Never pin all positions (kills Ad Strength)

**Dynamic Insertion:**
```
{KeyWord:Default Text}              # Keyword insertion
{COUNTDOWN(YYYY/MM/DD HH:MM:SS)}   # Countdown timer
{LOCATION(City)}                    # Location insertion
{CUSTOMIZER.attribute:default}      # Ad customizer
```

### Performance Max Asset Groups
| Asset Type | Spec | Max Per Group |
|-----------|------|---------------|
| Marketing Image | 1200×628 (1.91:1) | 20 total |
| Square Image | 1200×1200 (1:1) | (in 20) |
| Portrait Image | 960×1200 (4:5) | (in 20) |
| Logo (landscape) | 1200×300 (4:1) | 5 total |
| Logo (square) | 1200×1200 (1:1) | (in 5) |
| Video (landscape) | 1920×1080 (16:9) | 5 total |
| Video (square) | 1080×1080 (1:1) | (in 5) |
| Video (vertical) | 1080×1920 (9:16) | 5 vertical |
| Headlines | 30 chars | 5 |
| Long Headlines | 90 chars | 5 |
| Descriptions | 90 chars | 5 |
| Short Description | 60 chars | 1 |
| Business Name | 25 chars | 1 |

**Image:** Min 128×128, max 5120×5120, max 5MB, JPG/PNG
**Video:** Min 10s, rec 60s, min 480p, rec 1080p+, MP4/MOV, max 256MB

### YouTube Ad Formats
| Format | Ratio | Resolution | Duration | Skip |
|--------|-------|-----------|----------|------|
| Skippable In-Stream | 16:9 | 1920×1080 | 12s-3min (rec 15-30s) | After 5s |
| Non-Skippable | 16:9 | 1920×1080 | 15-60s (expanded 2025) | No |
| Bumper | 16:9 | 1920×1080 | ≤6s | No |
| In-Feed | 16:9 | 1920×1080 | Any | N/A |
| YouTube Shorts | 9:16 | 1080×1920 | ≤60s | Swipe |

**YouTube Shorts Safe Zone:** Center 1080×1420px. Bottom 480px = UI overlay.

### Google Extensions / Assets
| Type | Char Limit | Max Count | Notes |
|------|-----------|-----------|-------|
| Sitelink | 25 text, 35 desc ×2 | 20 | Min 4 rec; +3.5% conv with 6 |
| Callout | 25 chars | 20 | Min 4 rec |
| Structured Snippet | 25 chars | 2 sets | Predefined headers |
| Image | 1:1 or 1.91:1 | 20 | Min 1MB |
| Call | Phone number | 1 | With call tracking |
| Lead Form | 30 headline, 200 desc | 1 | Privacy URL required |
| Price | 25 header, 25 desc | 8 items | Min 3 |
| Promotion | 20 item | 1 | Schedulable |

### Ad Strength Scoring
- Headline uniqueness (Levenshtein distance)
- Keyword inclusion in headlines
- 3-7 headlines = Poor/Average, 8-10 = Good, 11-15 = Excellent
- "Excellent" → ~12-15% more conversions (diagnostic, not direct factor)

---

## Meta Ads

### Image Specs
| Placement | Ratio | Size | Max |
|-----------|-------|------|-----|
| Feed (preferred) | 4:5 | 1080×1350 | 30MB |
| Feed (supported) | 1:1 | 1080×1080 | 30MB |
| Stories/Reels | 9:16 | 1080×1920 | 30MB |
| Right Column | 1:1 | 1080×1080 | 30MB |
| Min width: 600px (1080px rec). No hard 20% text rule but AI penalizes heavy text.

### Video Specs
| Placement | Ratio | Resolution | Max Duration | Max Size |
|-----------|-------|-----------|-------------|----------|
| Feed | 4:5 (pref) | 1080×1350 | 241 min | 4GB |
| Feed | 1:1 | 1080×1080 | 241 min | 4GB |
| Stories | 9:16 | 1080×1920 | 120s | 4GB |
| Reels | 9:16 | 1080×1920 | 90s (rec 15-30s) | 4GB |
| In-Stream | 16:9 | 1920×1080 | 15 min | 4GB |

**Reels Safe Zone:** Center 1080×1300px. Bottom 35% (~670px) = CTA, caption, reactions.

### Text Limits
| Component | Recommended | Max |
|-----------|------------|-----|
| Primary Text | 125 chars | 2200 |
| Headline | 27-40 chars | — |
| Description | 20 chars (carousel) | — |
| Reels Primary | 72 chars | — |

### Carousel
- 2-10 cards, all 1:1 (1080×1080)
- Per card: Headline 40 chars, Description 20 chars
- Unique URL per card supported

### Advantage+ Creative Enhancements
Auto-adjustments when enabled: brightness/contrast, art filters, aspect ratio crops, music addition, text variations, video from static images. Test via A/B split.

### Quality Rankings
Three signals: Quality Ranking, Engagement Rate Ranking, Conversion Rate Ranking.
Rated: Above Average / Average / Below Average (10th, 35th, 55th percentile).

---

## TikTok Ads

### Video Specs
| Type | Min Resolution | Duration | Max Size | Min Bitrate |
|------|---------------|----------|----------|-------------|
| In-Feed (Non-Spark) | 540×960 (9:16) | 5-60s | 500MB | 516kbps |
| Spark Ads | Organic specs | Organic | N/A | N/A |
| TopView | 720×1280 (9:16) | 5-60s | 500MB | 2500kbps |
| Brand Takeover | 720×1280 | 3-5s | 2MB img / 500MB vid | — |

Recommended: 1080×1920, MP4/MOV, H.264, audio required, captions required.

### TikTok Safe Zone
```
Top:    0-150px   → Status bar, account info
Right:  0-140px   → Like, comment, share, profile
Bottom: 0-450px   → Caption, music, CTA, nav bar

SAFE BOX: X:40-940px, Y:150-1470px (900×1320px)
```
All critical text, logos, CTAs MUST be within safe box.

### Smart+ Specs
- Up to 30 ad groups per campaign
- Up to 50 creatives per asset group
- Symphony AI auto-generates variations

---

## LinkedIn Ads

### Single Image
| Component | Spec |
|-----------|------|
| Image (landscape) | 1200×627 (1.91:1) |
| Image (square) | 1080×1080 (1:1) — better engagement |
| Max file | 5MB, PNG/JPG |
| Intro text | 150 chars rec / 600 max |
| Headline | 70 chars rec / 200 max |
| Description | 100 chars (desktop only) |
| CTA Button | Predefined list |

### Video
| Component | Spec |
|-----------|------|
| Format | MP4 required |
| Size | 75KB - 500MB |
| Duration | 3s - 30min (rec 15-30s) |
| Resolution | 360p min (720p+ rec) |
| Aspect Ratios | 16:9 (landscape), 1:1 (square), 9:16 (mobile only) |

### Document Ads
- PDF, DOC, DOCX, PPT, PPTX
- 100MB max, 300 pages max (10-20 rec)

### Messaging
| Type | Component | Limit |
|------|-----------|-------|
| Message Ad | Subject | 60 chars |
| Message Ad | Body | 1,500 chars |
| Message Ad | CTA | 20 chars |
| Conversation Ad | Intro | 500 chars |
| Conversation Ad | CTA buttons | 5 max, 25 chars each |

### Audience Requirements
- Minimum: 500 members for delivery
- Recommended: 50,000-300,000
- Predictive Audiences seed: 300+ members
- Company list upload: up to 300,000

---

## Microsoft Ads

### RSA (mirrors Google)
| Component | Limit |
|-----------|-------|
| Headlines | 3-15, 30 chars each |
| Descriptions | 2-4, 90 chars each |
| Display Paths | 2, 15 chars each |

### Multimedia Ads (unique)
| Component | Spec |
|-----------|------|
| Image | 1200×628 (1.91:1) |
| Short Headline | 30 chars |
| Long Headline | 90 chars |
| Description | 90 chars |
| Business Name | 25 chars |

### Microsoft-Unique Extensions
| Extension | Description |
|-----------|-------------|
| Action Extension | Predefined action buttons |
| Filter Link Extension | Category-based deep links |
| Review Extension | Third-party review quotes |

---

## Cross-Platform Standards

### Universal Safe Zone (Vertical Video)
For content running across TikTok + Reels + Shorts + Stories:
```
Safe intersection: 900×1000px center
X: 40-940px (900px wide)
Y: 450-1450px (1000px tall)
```

### Character Normalization
| Component | Safe Limit | Strictest Platform |
|-----------|-----------|-------------------|
| Short headline | 30 chars | Google/Microsoft RSA |
| Long headline | 70 chars | LinkedIn recommended |
| Primary description | 90 chars | Google/Microsoft RSA |
| Short description | 25 chars | Extension callouts |

### Video Encoding Standard
| Component | Recommended |
|-----------|-------------|
| Video codec | H.264 High Profile |
| Audio codec | AAC |
| Audio level | -14 LUFS |
| Container | MP4 |
| Frame rate | 30fps |
| Color space | Rec. 709 |
| Bitrate (1080p) | 8-12 Mbps |

### Aspect Ratio Master Chart
| Ratio | Dimensions | Used By |
|-------|-----------|---------|
| 16:9 | 1920×1080 | YouTube, Google Display, LinkedIn Landscape |
| 9:16 | 1080×1920 | TikTok, Reels, Shorts, Stories |
| 4:5 | 1080×1350 | Meta Feed (preferred) |
| 1:1 | 1080×1080 | Meta Feed, LinkedIn, Carousel |
| 1.91:1 | 1200×628 | Google PMax, LinkedIn Single Image |
| 4:1 | 1200×300 | Google Logo (landscape) |
