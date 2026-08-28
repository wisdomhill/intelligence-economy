---
title: "10. The Functional Anatomy of Consumer AI Demand"
subtitle: "Generative media economics, world models, and the conquest of physical-life context, 2026–2028"
series: "The Intelligence Economy"
number: 10
manuscript-revision: 1
date: 2026-08-28
date-modified: 2026-08-28
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  The consumer demand function the token lens cannot see. Generative media
  measured in GPU-hours across five segments with disjoint suppliers, and
  the world models and wearables the same model lineage leads to.

keywords:
  - generative media
  - GPU-hours
  - world models
  - smart glasses
  - performance ad creative
  - creator economy

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
#
# Like Reports 7 to 9, this manuscript numbers its Executive Summary as
# section 1 and its cross-references depend on that, so the numbering is kept
# and the summary stays on the cover and in the PDF rather than becoming a
# chapter page.
#
# Chapter 5 is 4,193 words against 295 to 1,198 for every other chapter, so it
# is served as two web pages, both numbered 5 the way Report 5 serves its
# Part IV. The PDF keeps it as one chapter, headed "5. The Functional
# Anatomy of Media Demand" — neither page title, because each names only
# its own half.
published:
  dir: reports/r10/
  pdf: r10-the-functional-anatomy-of-consumer-ai-demand.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r10/

chapters:
  - manuscript: "2. Introduction: The Second Demand Function"
    published:  "2. Introduction"
    fragment:   _01-introduction.qmd
    page:       01-introduction.qmd
  - manuscript: "3. The Analytical Framework Extended: Sensory-Parallel Verification, the Monetization Cap, and the GPU-Hour Unit of Account"
    published:  "3. The Framework Extended"
    fragment:   _02-framework.qmd
    page:       02-framework.qmd
  - manuscript: "4. The Supply Side: The Multi-Polar Video War"
    published:  "4. The Supply Side"
    fragment:   _03-supply-side.qmd
    page:       03-supply-side.qmd
  - manuscript: "5. The Functional Anatomy of Media Demand: Five Segments, Five Logics (5.1–5.5)"
    published:  "5. Media Demand: Method and Segments 1–3"
    fragment:   _04-media-demand-method.qmd
    page:       04-media-demand-method.qmd
  - manuscript: "5. The Functional Anatomy of Media Demand: Five Segments, Five Logics (5.6–5.11)"
    published:  "5. Media Demand: Segments 4–5 and Totals"
    fragment:   _05-media-demand-totals.qmd
    page:       05-media-demand-totals.qmd
  - manuscript: "6. Beyond Content: World Models and the Physical-Context Frontier"
    published:  "6. Beyond Content"
    fragment:   _06-beyond-content.qmd
    page:       06-beyond-content.qmd
  - manuscript: "7. Risks, Sensitivities, and Unmodeled Factors"
    published:  "7. Risks and Sensitivities"
    fragment:   _07-risks.qmd
    page:       07-risks.qmd
  - manuscript: "8. Tracking Indicators for H2 2026 and Beyond, with a Closing Synthesis"
    published:  "8. Tracking Indicators"
    fragment:   _08-tracking-indicators.qmd
    page:       08-tracking-indicators.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _09-references.qmd
    page:       09-references.qmd
---
# The Functional Anatomy of Consumer AI Demand
### Generative Media Economics, World Models, and the Conquest of Physical-Life Context, 2026–2028

The Intelligence Economy — Report 10 of 14

Wisdom Hill Research | Thematic Research | July 2026

---

# 1. Executive Summary

Report 8 of this series mapped enterprise AI demand across seven business functions, all sharing a common unit of account — the LLM token — and a common economic logic: agents priced against the labor budgets of knowledge work. This report maps the demand function that the token lens cannot see. Generative media and its successors run on a different unit of account (GPU-hours of visual and audio generation, not convertible to tokens), a different verification regime (the human visual cortex, or the advertising auction, rather than the compiler), a different model architecture (compute-bound parallel diffusion rather than memory-bandwidth-bound autoregressive decode), a largely disjoint supplier set (Google, ByteDance, Alibaba, Kuaishou, and independents; Anthropic is absent), and a different monetization pool — consumer attention, advertising, and subscription dollars rather than wages. Because the supplier and measurement ecosystems are disjoint, LLM-derived usage statistics structurally undercount this entire economy.

Three headline results organize the analysis. First, **the media demand function grows roughly eight-fold over the forecast window, from approximately 215 million GPU-hours in 2026 to 1,681 million in 2028** — an equivalent fleet expanding from roughly 49,000 to 384,000 H100-equivalent inference accelerators at an assumed 50% utilization — driven by generated video volume rising nine-fold from approximately 416 million to 3,710 million minutes per year, plus image generation scaling from 50 to 150 billion units and voice and music from 0.5 to 2.5 billion hours. Every video figure is built forward from a stated reference anchor in the existing online-video economy — advertiser accounts, marketplace listings, creator populations, professional production flows, and organizational counts — with explicit penetration paths; because production throughput and adoption are only partially observable, the totals should be read as an order-of-magnitude conditional scenario under the stated assumptions, plausibly varying by several-fold, rather than as a point forecast. The trajectory is far faster in relative terms than the enterprise LLM track: a near-eight-fold expansion in GPU-hours against the roughly two-fold growth of compute-weighted B2B token demand, and — on the conversion assumptions of the companion infrastructure volume — a 2028 fleet equal to roughly 60% of the entire B2B LLM inference fleet and approaching the scale of the coding category alone.

Second, **the structure of the demand inverts the intuitions imported from both the LLM market and the traditional media industry.** The 2026 volume leader — and the structural volume engine — is not entertainment but performance-advertising creative — the one media workload whose final verifier is not a human but the platform's A/B auction — a scalable statistical verifier that lets variant volume escape the human-review bottleneck, as the verification framework of the companion enterprise report anticipates. The "Netflix intuition" fails on a minutes basis: professional media and entertainment contributes only 6–8% of generated minutes yet roughly 39–46% of video GPU-hours through premium generation intensity — and, counter-intuitively, carries the *highest* unit-basis penetration rate in the model, because its denominator is a pure flow of live, budgeted productions adopting through a nearly risk-free pre-visualization entry point. The fastest-growing segment is neither of these but the creator economy — YouTube, short-form, and video-podcast producers — whose demand is driven not by a rising head-count but by rising *generation depth* per video, and which overtakes advertising as the largest volume segment from 2027, reaching 42% of generated minutes by 2028. Each segment is built forward from an observable base in the existing online-video economy (Meta's ~11 million advertisers, YouTube's ~500-hours-per-minute upload firehose and ~15 million regular creators, the ~2 billion marketplace listings, ~60,000 annual professional productions, and ~4 million organizations) with an explicit penetration logic — the platform-injected advertising curve, the GMV-weighted commerce reading under which e-commerce ends the forecast as the most-penetrated function in commercial terms, and the genre-fit ceiling that bounds creator adoption. And the supply side is genuinely multi-polar where the LLM market was not — Google's Gemini Omni Flash currently holds the top leaderboard position while Chinese vendors (ByteDance, Alibaba, Kuaishou) fill most of the remaining top tier, reflecting the short-video giants' possession of unusually large proprietary video datasets and the distribution channels that monetize the output; OpenAI, meanwhile, has exited consumer video entirely.

Third, **the content market is the near-term P&L, but it is not the endgame.** The same model lineage extends along a technical continuum from video generation to interactive world models — Google's Genie, already training embodied agents in simulated environments — and the interface war is moving onto the body, with Meta's AI glasses more than tripling to seven million-plus units sold in 2025 and IDC forecasting 13.6 million display-less smart-glasses units for 2026 — roughly a further doubling of the category. Read through the two-axis context framework that closes this report, generative media is the opening battle of a second front: where the enterprise agent conquered *digital work context* and monetizes against labor, multimodal systems, wearables, and world models are the machinery for acquiring *physical life context*, monetizing against attention and commerce today and physical labor tomorrow. The binding constraint throughout is not capacity to generate but capacity to monetize — a constraint applied throughout this report as an economic consistency screen on every volume assumption, and illustrated by OpenAI's exit from consumer video: the Sora app was discontinued in April 2026 with the API scheduled to follow in September, a retreat consistent with — though never officially attributed to — inference economics that one outside estimate placed as high as $15 million per day against negligible revenue. One structural pattern shapes every scenario: Google currently fields the most visibly integrated stack across both axes — consumer distribution, generative video, world models, robotics models, and wearable partnerships — a breadth no single competitor presently matches within one ecosystem.

---

# 2. Introduction: The Second Demand Function

## 2.1 Scope and the meaning of "consumer"

This report is the consumer-side companion to *The Functional Anatomy of Enterprise AI Demand* (Report 8), which partitioned B2B work into seven token-denominated functions and deliberately excluded an eighth — Generative Media — from its quantitative core. This report develops that eighth function in full and extends it to the frontier that follows it.

A definitional note first, because the word "consumer" carries two meanings here and the distinction disciplines the model. Much of the generated-media volume analyzed below is *purchased* by businesses — advertising agencies, e-commerce sellers, corporate learning departments. What makes the demand "consumer" in the economically relevant sense is the pool that ultimately funds it: advertising, subscription, and attention dollars that originate with consumers, rather than the wage and labor budgets that fund the enterprise agent economy. This distinction is not cosmetic. It supplies the single most important constraint in the model — the monetization-pool cap of Section 3.3 — and it explains why the demand function behaves differently from the token economy: enterprise agents are bought against labor costs that total tens of trillions of dollars globally, while generated content competes for a fixed pool of audience attention and the advertising and subscription revenue attached to it.

## 2.2 Why a separate compute track

Three properties compel separate treatment rather than a footnote to the token model. The **unit of account** differs: visual generation is denominated in spacetime patches and audio frames, not language tokens, and no defensible exchange rate converts one into the other; we therefore measure in GPU-hours. The **model architecture** differs: as a general tendency, diffusion-class generation is a compute-bound, massively parallel batch workload, against the memory-bandwidth-bound autoregressive decode of LLMs — modern video and world models span diffusion, autoregressive, and hybrid designs, but the center of gravity of each demand function stresses a different part of the silicon stack, and the two should never be summed naively (the hardware consequences are the subject of the companion infrastructure volume). And the **supplier ecosystem** is disjoint: the leaders are Google, ByteDance, Alibaba, Kuaishou, OpenAI (in retreat, as Section 4 documents), and a set of independents, with the enterprise-agent leaders largely absent — which is precisely why token-based telemetry is blind to this economy.

## 2.3 The integrating frame: two axes of context conquest

The analytical thread that binds generative media to world models and wearables — and binds this report to the rest of the series — is the **Two-Axis Context Map**. Axis 1 is *digital work context*: files, codebases, enterprise systems, conquered through the interface evolution from web chat to IDE to CLI to desktop agent, and monetized against labor budgets. That war — the agentic war — is in its harvest phase, and Reports 3 through 9 of this series measure its economics. Axis 2 is *physical life context*: what people see, hear, and do in the world, conquered through multimodal perception, wearable sensors, and world models, and monetized against attention, commerce, and eventually physical labor via robotics. Axis 2's war is in its sowing phase. Generative media sits at the hinge: commercially, it is a content-production market being repriced today; strategically, the same model families are the entry ramp to world models and embodied AI. The desktop agent is the AI that does your work; the wearable AI is the AI that inhabits your life — high frequency, deep context — and a winner on Axis 2 gains distribution leverage back over Axis 1.

---

# 3. The Analytical Framework Extended: Sensory-Parallel Verification, the Monetization Cap, and the GPU-Hour Unit of Account

## 3.1 Verification at a glance

The enterprise report's foundational law — that the value of generation is gated by the cost and speed of verification — applies with full force here, but the media economy occupies the verification class the enterprise taxonomy touched only in passing: **sensory-parallel human verification**. The human visual system screens an image or video draft in a glance, holistically and in parallel, where a legal memo must be read serially at roughly 200–300 words per minute. The consequence is an iteration economy unlike any text function: visual drafts can be triaged far faster than long-form text, so a creative director can screen a large variant set in the time a research director works through a few pages. Iteration is therefore rapid and cheap on the human side — but a human still sits inside every loop, which caps fully autonomous scaling for most segments.

## 3.2 The exception that drives the volume: the auction as machine verifier

One segment escapes the cap, and it is the segment our model makes the volume engine. In performance advertising, the final verifier of a creative asset is not a person but the platform's A/B auction: publish many variants, and click-through and conversion select the winners. The auction is a *scalable statistical verifier* rather than a deterministic one — outcomes are noisy, delayed, and confounded by targeting, auction conditions, and attribution windows — but it can rank large creative sets with far less human review than any other media workflow, playing for advertising a role loosely analogous to the compiler's in software. This is the media economy's structural rhyme with the coding economy, and it predicts the same outcome in structural terms: the machine-verified segment amplifies fastest *per unit of human review*, escaping the bottleneck that caps every other segment. It is no accident that ad creative is the model's largest allocation at the opening of the window and its 2026 volume leader, nor that e-commerce SKU video — verified by the same conversion metrics — is its companion workhorse. That the creator economy overtakes advertising in raw minutes from 2027 (Section 5.5) is a generation-depth effect, not a verification effect, and leaves the structural claim intact: creator minutes still pass a human inside every loop, and their growth is bought with human screening time that the auction-verified segment does not spend.

## 3.3 The monetization-pool cap

The second framework element is the constraint that disciplines every volume figure in Section 5: **performance-ad creative and the creator economy draw on the same revenue pool.** A YouTube creator's income is a share of the same advertising and subscription dollars that fund ad campaigns; generated content competes for a fixed pool of audience attention and the ad budget attached to it. The segment allocations are therefore *allocative, not additive* — published volume is bounded by what the pool can monetize, and growth within the cap comes from the retake and variant multipliers applied to each published minute, not from unbounded publishing. This is the deepest difference from the enterprise demand function: token demand scales against the labor share of GDP, while media demand scales against the attention share of consumer time and spend, a far smaller and slower-growing pool. The cap is also why the model treats capacity and demand as separate questions: the Sora consumer app demonstrated that users will happily consume coding-scale GPU resources when generation is free — one outside estimate placed peak inference expense as high as $15 million per day against negligible revenue, an estimate built on assumed user activity and per-clip costs rather than disclosed figures, before OpenAI discontinued the consumer app in April 2026 and subsequently announced the shutdown of its API. The shutdown is confirmed; the precise role of inference economics in the decision remains an inference — but the episode frames the category's constraint well. Capacity to consume compute is proven; what gates *realized* demand is monetization, and our volume assumptions are anchored accordingly to the ROI-measurable segments.

## 3.4 The unit of account and the shape of the compute

Because diffusion generation is compute-bound and parallel, its natural capacity metric is the GPU-hour, and its unit economics are anchored to throughput: a saturated H100-hour yields roughly three to seven minutes of 1080p video on efficient open-weight models (0.15–0.30 GPU-hours per minute), while premium-tier generation — 4K, physics consistency, phoneme-level lip-sync — runs at 1–5 GPU-hours per minute, so that a single premium 10-second clip costs $0.50–2.00 in raw compute and consumes the resources of thousands of chat queries. Production routing conventions (roughly 80% of jobs to workhorse models, 20% to premium tiers) yield the segment-differentiated intensity rates of Section 5 and a blended average near 0.4 GPU-hours per generated minute. These are the media economy's equivalents of the tokens-per-task coefficients in the enterprise model, and they carry the same status: explicit, adjustable assumptions disciplined by observed pricing.

---

# 4. The Supply Side: The Multi-Polar Video War

## 4.1 The contenders — and OpenAI's exit

The supply landscape has moved materially since early 2026, and in a single direction: toward more competitors, faster model turnover, and lower prices. OpenAI's retreat from consumer video, provisional a quarter ago, is now complete — the Sora web and app experiences were discontinued on April 26, 2026, and OpenAI has announced that the Sora API will follow on September 24, 2026. The withdrawal is consistent with this report's monetization thesis: Sora produced some of the most physically convincing motion in the market yet, by outside estimates, could not cover its inference cost against consumer revenue — one such estimate placed peak spending as high as $15 million per day, though OpenAI disclosed no figures and never attributed the decision to cost — and the company redirected the capital to the agent war. Video generation is easy to generate and hard to monetize; the company with among the strongest claims to frontier generation quality exited the segment rather than fund it.

What remains is a broadening, genuinely multi-polar field. As of mid-2026 the Artificial Analysis text-to-video leaderboard is led by Google's **Gemini Omni Flash**, which holds the top position in both the with-audio and without-audio categories, while Chinese vendors — ByteDance's Seedance family, Alibaba's HappyHorse, and Kuaishou's Kling — fill most of the remaining top tier. Several highly ranked entries are available only through a single app rather than a broad API — a reminder that a leaderboard score one cannot license is a research result rather than a product.

**Gemini Omni Flash and Veo (Google)** anchor the Western supply. Gemini Omni Flash, the fast tier of Google's Omni world-model family, currently tops the leaderboard and extends Google's distribution advantage to conversational, quick-turn generation; the Veo line remains the enterprise-safe workhorse — native 4K, strong prompt adherence, reference-based consistency, and 48kHz synchronized *dialogue* rather than merely sound effects — across Fast, Standard, and Quality tiers ($0.03–0.50 per second) distributed at near-zero acquisition cost through the Gemini app, Google AI subscriptions, and Vertex AI.

**Seedance (ByteDance)** pairs top-tier quality with price destruction. Seedance 2.0 (February 2026) launched with the market's most permissive input grid — up to nine reference images, three video clips, and three audio files per generation — and the successor 2.5 has extended to native 30-second 4K generation with up to fifty reference images. Its aggressive pricing (on the order of $0.05 per second on efficient tiers) first made high-volume commercial generation economical; distribution runs primarily through ByteDance's Doubao and Dreamina apps rather than a broad Western API.

**HappyHorse (Alibaba)** is the consequential new entrant: a model with joint audio-video generation and seven-language lip-sync that ranks second and third on the without-audio board, confirming that the Chinese strength in video is not a two-company artifact but a broad capability grounded in the short-video platforms' data and distribution.

**Kling (Kuaishou)** competes on cinematic motion and value: native 4K/60fps single-pass generation up to fifteen seconds, multilingual lip-sync, shared audio timelines across multi-shot sequences, at mid-market pricing (~$0.10–0.14 per second) that undercuts the Western flagships and supplies several of the leaderboard's top-ten entries.

Two structural shifts deserve emphasis. First, the axis of competition has moved off resolution entirely — essentially every serious model now does 1080p or native 4K — and onto clip length, synchronized dialogue, character consistency across shots, and cost. Second, open-weight models have become genuinely useful: Alibaba's Wan, Lightricks' LTX-2, and Tencent's HunyuanVideo now ship 4K-and-audio capability under permissive licenses, the last of these rendering on a single consumer RTX 4090 — which places a floor under the self-hosting economics that inform this report's GPU-hour assumptions (Section 4.3). Native synchronized audio, a differentiator in 2025, is now a baseline expectation; the frontier has moved to lip-sync precision, shot-to-shot consistency, clip duration, and price.

## 4.2 Why video is multi-polar where LLMs were not

The LLM market repeatedly resolved toward one or two benchmark leaders; video generation in 2026 is genuinely multi-polar: Google leads the current quality rankings, but ByteDance, Alibaba, and Kuaishou occupy most of the remaining top tier — a depth of Chinese co-leadership with no LLM-market parallel. The structural reason is the vertical integration of data and distribution: ByteDance and Kuaishou are the world's largest short-video companies, possessing both unusually large proprietary short-video datasets and distribution feedback (billions of hours of the exact content type being generated) and the channels that monetize the output. In multimodal generation, China is not a fast follower but a co-leader — a fact with direct consequences for the cost curve, since Chinese price competition is the principal force collapsing unit costs, and for measurement, since Seedance distributes primarily through ByteDance's Doubao ecosystem without a public Western API, limiting independent verification of its usage claims. Market behavior mirrors the agent market's multi-homing: professionals pick the model per shot through aggregator platforms, and leaderboard rankings reshuffle on a monthly cadence.

## 4.3 The cost collapse, and the status of the GPU-hour coefficients

Retail generation pricing now spans roughly $0.03–0.50 per second across tiers — a workhorse band near $0.05–0.15 (Seedance efficient tiers, Kling value tiers, Veo Fast, Gemini Omni Flash) and a premium band above it — while self-hosted open-weight inference runs an order of magnitude lower. At current workhorse rates a ten-minute first-pass generation costs roughly $30–90 before retakes and editing; under the further five- to ten-fold price decline this report models, that falls to approximately $3–18 by 2028 — below a stock-footage subscription, the threshold past which generation becomes the default rather than the option (the cost curve of Section 5.8). The first-order losers are stock-footage libraries, small production houses, and the lower tiers of the advertising production chain; the first-order winners are the platforms that monetize distribution and the suppliers of inference compute — video generation being orders of magnitude more compute-intensive per unit of output than text.

A note on the status of the GPU-hour coefficients that convert generated minutes into compute demand in Section 5. The workhorse range of 0.15–0.30 GPU-hours per generated minute — equivalent to roughly three to seven minutes of video per saturated accelerator-hour — and the premium coefficient of 2.5 for professional 4K with physics consistency and phoneme-level lip-sync are **explicit engineering assumptions**, informed by published model throughput and by the retail and managed-API price points above, but not directly identifiable from them: service prices bundle hardware choice, batching, utilization, subsidy, and provider margin, none of which vendors disclose. Managed-API pricing at cents per clip is *consistent with* low underlying generation costs; it cannot pin the coefficient. The resulting GPU-hour totals should therefore be read as conditional capacity scenarios under stated intensity assumptions rather than as measured demand, with the residual risk skewed in one direction — continued efficiency gains and open-weight maturation would bias the coefficients downward, lowering the GPU-hour totals without changing the generated-minute volumes. Because retail prices fall faster than underlying compute cost per minute (margin compression plus efficiency), the demand-side cost collapse driving volume and the supply-side GPU-hour intensity are partly decoupled — which is why falling prices expand generated minutes without proportionally shrinking the fleet the segment requires.

---

# 5. The Functional Anatomy of Media Demand: Five Segments, Five Logics

This is the anatomical core of the report. The media track is not one demand curve but five, each with a distinct function, a distinct content requirement, a distinct customer, a distinct platform owner, and — decisively — a distinct demand-shape: some segments multiply generated **minutes** while others barely register in minutes yet dominate **GPU-hours**. This chapter builds each segment forward from a stated reference anchor in the existing online-video economy, states the penetration logic explicitly, and then screens the resulting total against the monetization constraint of Section 3.3, which operates as a qualitative economic consistency check on the volume assumptions rather than as a computed ceiling.

## 5.1 Method: anchor, penetrate, deepen — then screen against the pool

Each segment is estimated as *generated minutes = installed base × AI-adoption penetration × output per adopter × generation depth*, where generation depth is the retake-and-variant multiplier converting one published minute into several generated ones. The denominators are reference anchors and scenario constructions of differing evidentiary strength rather than uniformly observable statistics: Meta's officially disclosed base of more than 10 million advertising businesses, widened to ~15 million *platform-advertiser accounts* across the major ad platforms (an account basis that tolerates cross-platform duplication, since campaigns generate creative per platform); the ~2 billion live product listings of the global marketplaces; YouTube's upload firehose (~500 hours per minute, roughly 15.8 billion published minutes a year) and its creator hierarchy (~3 million monetizing channels inside a ~15 million weekly-cadence creator population); an order-of-magnitude construction of ~60,000 professional productions completed annually (features, scripted-television episodes, music videos, premium documentaries); and a scenario denominator of ~4 million organizations above fifty employees. The volume coefficients carry wide error bands, and the sections that follow state the confidence attached to each; every input is explicit and adjustable.

**Table 1. Generated video volume by segment: bases, penetration paths, and generation intensity**

| Video segment | Base (anchor) | Penetration 26→28E | 2026E | 2027E | 2028E | GPU-hr/min |
|---|---|---|---:|---:|---:|---:|
| 1. Performance ad creative | ~15M platform-advertiser accounts | 15% → 55% | 160 | 460 | 1,155 | 0.25 |
| 2. E-commerce SKU video | ~2,000M live marketplace listings | 5% → 28% of stock (~35% → ~88% GMV-weighted) | 60 | 220 | 505 | 0.15 |
| 3. Creator economy / UGC | ~15M weekly-cadence creators | 12% → 40% | 140 | 585 | 1,560 | 0.30 |
| 4. Professional M/E | ~60K professional productions/yr | 25% → 75% (any-use) | 25 | 120 | 250 | 2.50 |
| 5. Corporate internal | ~4M organizations (50+ employees) | 5% → 30% | 31 | 120 | 240 | 0.20 |
| **Video total (M generated minutes)** | | | **416** | **1,505** | **3,710** | **0.38–0.43 blended** |

Two headline movements inside the table deserve immediate notice. Generated minutes expand roughly nine-fold over two years, faster than any single segment because breadth and depth compound. And the volume leadership changes hands: performance advertising leads in 2026 (38% of minutes), but the creator economy overtakes it from 2027 and holds 42% of minutes by 2028 — advertising's growth is bounded by advertiser count and fatigue-cycle economics, while creator demand compounds on generation depth per video. The sections below derive each row.

## 5.2 Why the penetration rates differ: denominators, deciders, and forcing functions

Read naïvely, the penetration column is counter-intuitive: professional studios — the most quality-sensitive, rights-sensitive customers in the market — carry the highest rate, while e-commerce and corporate video, seemingly the easiest use cases, carry the lowest. The paradox dissolves once three structural variables are made explicit, because the five rates are defined over different kinds of denominator and driven by different adoption mechanics.

The first variable is the **nature of the denominator** — whether it is a *flow* of live projects that all make a tooling decision this year, or a *stock* that includes a dormant long tail which no rational actor would ever address. The second is the **decision structure** — whether adoption is decided by a few thousand concentrated professional organizations or by millions of heterogeneous small businesses and individuals. The third is the presence or absence of a **forcing function** — whether the platform injects the technology from the supply side, or competitive cost pressure compels it, or adoption is a purely voluntary pull that requires creating a workflow that did not previously exist.

| Segment | Denominator | Decision structure | Forcing function | Resulting pace |
|---|---|---|---|---|
| 4. Professional M/E | Flow — every unit is a live, budgeted project | Highly concentrated (thousands of studios/VFX houses) | Competitive cost pressure (five-figure VFX shots vs. cents) | Fastest |
| 1. Ad creative | Near-flow (active advertisers) | Dispersed, but the platform decides on their behalf | Supply-side injection (Advantage+ / PMax auto-generation) | Fast |
| 3. Creator economy | Flow (weekly uploaders) | Fully dispersed individuals | None — cost and quality pull only | Moderate |
| 5. Corporate internal | Stock — most organizations have no video function today | Dispersed, plus procurement friction | None — a new workflow must be created | Slow |
| 2. E-commerce SKU | Stock — dominated by a dormant listing tail | Platform-concentrated, but application is traffic-weighted | Partial (platform auto-conversion) | Lowest on stock; highest on GMV |

The rest of this chapter applies this framework row by row; the apparent paradoxes in the table are resolved cases of it.

## 5.3 Segment 1 — Performance Ad Creative: supplier-push, not customer-pull

**Function, content, customer.** Short performance-marketing video — feed ads, Reels, Shorts, and TikTok placements — typically eight to fifteen seconds, produced in large variant sets for continuous A/B testing. The requirement is volume and freshness rather than cinematic polish, so workhorse-tier generation (0.25 GPU-hours per minute) is fully sufficient. The customer base is the ~15 million platform-advertiser accounts across the major platforms (anchored on Meta's officially disclosed base of more than 10 million advertising businesses, plus the Google, TikTok, and Amazon account bases, counted with cross-platform duplication since creative is generated per platform), overwhelmingly SMBs for whom video production was previously uneconomic; a $10 generation budget now yields dozens of usable clips, dropping video creation to roughly the cost structure of copywriting.

**The verification logic.** This is the one media workload whose final verifier is not a human but the platform's A/B auction: publish many variants and let click-through and conversion select winners, with human review shrinking to brand-safety screening. As Section 3.2 argued, the market plays the role the compiler plays in software — and creative-fatigue cycles (ad sets decay in two to four weeks on short-form platforms) then make continuous refresh rational, so that when the marginal cost of a variant approaches zero the profit-maximizing variant count rises.

**The penetration logic (15% → 55%).** The steepest non-professional ramp in the model rests on the observation that adoption here is not a customer decision but a platform decision. Meta disclosed as early as September 2024 that more than one million advertisers were using its generative ad tools, generating fifteen million ads in a single month; Meta's Advantage+ and Google's Performance Max increasingly generate video variants server-side from an advertiser's existing assets, which means that by 2028 the operative definition of penetration shifts from "adopted" to "did not opt out." The 55% ceiling reflects the residual: categories adequately served by static imagery, regulated verticals (pharmaceutical, financial) whose creative-approval chains block automated variants, and the low-activity advertiser tail that supplies no usable source assets. Our 2026 figure of 2.25 million *video-specific* AI advertisers is a deliberate subset of the larger disclosed any-generative-AI base.

**Parameters.** Advertisers using AI video rise 2.25M → 4.5M → 8.25M; published AI clips per advertiser rise 120 → 160 → 200 per year on the fatigue-refresh logic; average published clip ~12 seconds (0.2 minutes); and the generation-to-published multiplier runs 3.0 → 3.2 → 3.5 as variant testing widens. Product: **160 → 460 → 1,155 million generated minutes.**

**The platform reading.** Meta and Google own this segment three times over: the auction that verifies the creative, the advertising pool that monetizes it, and increasingly the generation model that produces it. The supply-side injection that drives the penetration curve exists precisely because of that vertical integration — a platform that owns both the model and the monetization pool has every incentive to generate the creative itself, a dynamic this series' analysis of consumer agentic platform competition among Google, Meta, and Amazon develops at length.

## 5.4 Segment 2 — E-commerce SKU Video: lowest penetration of stock, highest penetration of commerce

**Function, content, customer.** Conversion of static product listings into short demonstration and lifestyle clips — five to ten seconds, templated, lightly retaken — verified by the listing's own conversion rate, hence machine-graded and priced at the cheapest tier in the model (0.15 GPU-hours per minute). The decision-relevant customers are the platforms and their seller bases: Amazon's ~1.6 million active sellers and its advertising console (whose AI video generator has been offered to advertisers at no charge since 2024), Shopify's ~4.9 million stores, and the Chinese marketplaces, several of which already run listing-image-to-video conversion at platform scale. The *unit*, however, is the SKU: roughly 2 billion live listings globally (the weakest-grade anchor in the model), of which Amazon alone accounts for several hundred million.

**The penetration logic (5% → 28% of stock; ~35% → ~88% of GMV).** The intuition that e-commerce should be the most-penetrated segment is correct — the low figure in the table is a denominator effect, not a slow-adoption claim. Video creates value only where there is traffic to convert, so the economically rational application order is GMV-weighted from the top: under the marketplace-typical Pareto structure in which the top decile of listings carries roughly 85% of merchandise value, our 2028 stock coverage of 28% decomposes as the entire top decile plus roughly a fifth of the dormant tail — which is approximately **88% of GMV-weighted commerce** (85% + 0.2 × 15%). On the measure that matters commercially, this segment ends the forecast as the *most* penetrated function in the taxonomy; the stock-based figure is retained in the table because GPU-hours are generated per listing, not per dollar. One reconciling note: the 2026 GMV figure of ~35% embeds imperfectly traffic-ordered early application — platform auto-conversion sweeps mid-tail listings alongside the head — rather than a strict top-down fill, which at 5% stock coverage would imply roughly 42% of GMV. The dormant tail below the traffic line is not late-adopting; it is rationally never addressed.

**Parameters.** Covered SKUs rise ~100M → ~300M → ~560M (5% → 15% → 28% of stock); annual generated minutes per covered SKU run 0.6 → 0.73 → 0.9 (two to three clips of ~10 seconds at retake multiples of 1.4–1.8). Product: **60 → 220 → 505 million generated minutes.** Amazon is this segment's platform owner in the West on the same triple logic as Meta in advertising — it owns the traffic, the conversion data that verifies the creative, and now the generation tooling — with Taobao and Douyin commerce playing the equivalent role in China.

## 5.5 Segment 3 — Creator Economy / UGC: the depth-driven leader from 2027

**Function, content, customer.** The individual and small-business creator economy: YouTube channels, short-form operators, the video-podcast wave that Spotify and YouTube are both pushing, and independent musicians. Content spans B-roll and intros today, graduating toward assembled segments and AI-hosted formats; mixed intensity is modeled at 0.30 GPU-hours per minute. The base is the ~15 million creators publishing on a weekly cadence — anchored on YouTube's ~3 million monetizing channels and widened to regular non-monetizing uploaders, video podcasters, and short-form businesses, while deliberately excluding the ~65 million casual-creator figure whose long tail publishes too irregularly to matter for volume.

**The penetration logic (12% → 40%): no forcing function, and a genre-fit ceiling.** Adoption here is fully dispersed individual decision-making with no platform injection, so the curve is pure cost-and-quality pull — and its ceiling is set by genre structure rather than by willingness. A large share of creator output is in genres where AI generation is structurally inapplicable or only marginally applicable: gaming (the screen capture is the content), vlogging and IRL formats (authenticity is the product), reaction and commentary. Treating the high-applicability genres — education and explainers, ambient and music channels, kids' content, listicle and documentary-style formats — as roughly 50–60% of serious-creator output, and assuming adoption within that applicable pool reaches ~70% by 2028, yields the 40% aggregate: the headline rate is the product of genre fit and within-genre adoption, not a free-hand S-curve. The 2026 figure of 12% reflects that the tooling is already trivially accessible to this population and that platform integration is underway — YouTube has embedded Veo-powered generation directly into Shorts — but that full-video workflows remain immature.

**Why depth, not breadth, is the growth engine.** The creator base is roughly stable and upload cadence is fixed by format (~52 videos per creator-year), so this segment's growth is carried almost entirely by *generation depth*: minutes generated per video rising 1.5 → 3 → 5 as the technology traverses the insert-to-segment-to-full-generation progression of Section 5.8, with retakes included. The product — 15M × 12%/25%/40% × 52 × 1.5/3/5 — yields **140 → 585 → 1,560 million generated minutes**, a near-elevenfold rise that overtakes advertising in 2027 and reaches 42% of all generated minutes by 2028. A scale check disciplines the optimism: 1,560 million generated minutes divided by a retake multiple of ~2.5 implies ~620 million *published* AI minutes in 2028 — roughly 2–3% of the current annual upload volume of YouTube and the short-form platforms combined, comfortably inside any plausible slop-saturation ceiling.

**The platform reading.** Google is this segment's vertically integrated owner: YouTube supplies the distribution, the Partner Program supplies the monetization pool (a share of the same advertising dollars that fund Segment 1 — the double-counting the cap of Section 3.3 exists to prevent), and Veo, embedded in the creation surface, increasingly supplies the generation itself. No other player holds all three layers of any segment this completely.

## 5.6 Segment 4 — Professional M/E: the highest headline penetration and the Netflix counter-intuition

**Function, content, customer.** Studios, streamers, and music-video production: VFX shots, pre-visualization, concept work, B-roll, and increasingly generated final footage, at the top of the quality ladder — 4K mastering, physical consistency, phoneme-level lip-sync — modeled at 2.5 GPU-hours per minute, eight to seventeen times the workhorse rates. The customer set is tiny: roughly 60,000 professional productions a year globally (on the order of 9,000 feature films, 35–40,000 scripted-television episodes, and the music-video and premium-documentary flow).

**The penetration logic (25% → 75%, any-use): why the most demanding customer adopts fastest.** The rate that most offends intuition is the most structurally over-determined in the model, for three reasons drawn directly from the Section 5.2 framework. First, the denominator is a pure *flow*: every one of the 60,000 units is a live, budgeted project whose team makes toolchain decisions this year — there is no dormant stock diluting the base, unlike the listings tail or the video-less corporate majority. Second, the *any-use threshold* is low and nearly risk-free: a production counts as penetrated if AI generation appears anywhere in its pipeline, and the earliest entry points — pre-visualization, concept frames, temp B-roll — never reach the final screen, so the hallucination-and-rights risk that gates final footage does not gate adoption itself, while the cost differential is immediate and large — with the caveat that this compares finished-shot budgets against raw generation compute, before labor, compositing, quality control, and rights costs, so it is directional rather than like-for-like. Third, the decision structure is concentrated: a few thousand studios, VFX houses, and production companies under identical competitive cost pressure diffuse innovations at professional-market speed, the same dynamic that made AI coding tools near-universal among professional developers within roughly two years (84% using or planning to use them, per Stack Overflow's 2025 survey). The public record confirms the mechanism is already operating: Lionsgate's partnership with Runway and Netflix's disclosure of its first generative-AI final footage in a released title mark the majors' transition from experimentation to production use. The economic substance of this segment, however, is carried not by the penetration rate but by *depth per adopting title*, which rises from ~1,700 to ~5,550 generated minutes as usage expands from pre-viz into VFX and scene generation.

**The counter-intuition, made precise.** The instinct that streaming and film drive media-AI demand is false on a minutes basis and true on a compute basis. A feature's final runtime is ~120 minutes; even at aggressive retake ratios a title generates thousands, not millions, of minutes, and the whole segment totals only **25 → 120 → 250 million generated minutes — 6–8% of the track.** Yet at premium intensity that sliver consumes **39–46% of video GPU-hours in every forecast year** (62.5 of 160 million in 2026; 625 of 1,506 million in 2028). Localization — one title regenerated across a dozen or more dubbing languages — adds a further multiplier and is the principal B2B driver of the voice track in Section 5.10. This is the media economy's own token-versus-compute divergence: the segment nearly invisible in volume statistics dominates the compute bill, and analysts reading generated-minutes as a compute proxy will misread the market exactly as naïve token counts misread the LLM market.

## 5.7 Segment 5 — Corporate Internal: the structural laggard, honestly sized

**Function, content, customer.** Internal learning-and-development modules, corporate communications, policy explainers, and presentation video, replacing template stock footage and talking-head shoots. Avatar-led synthesis dominates the workload, and because avatar pipelines are computationally lighter than full-scene diffusion, the segment carries the lowest video intensity in the model at 0.20 GPU-hours per minute. The base is the ~4 million organizations above fifty employees.

**The penetration logic (5% → 30%): why the "easiest" use case moves slowest.** This is the mirror image of Segment 4 on all three framework variables. The denominator is a *stock* in which most organizations have no video-production function today — no budget line to redirect, no incumbent cost to undercut. There is no forcing function: a company that produces no internal video loses nothing visible by continuing not to; adoption requires creating a workflow, not substituting within one. And the decision path runs through procurement and IT approval, the highest-friction channel in the taxonomy. The 2026 starting point is disciplined against vendor reality: the category leader's disclosed customer base sits near 50,000 enterprises (including most of the Fortune 100), and the dedicated-vendor installed base across the category plausibly totals 100–200 thousand organizations. Our figure of 200,000 adopting organizations (5%) therefore embeds one further assumption, which recent product history supports: video generation is ceasing to be a procured product and becoming a bundled feature of software organizations already own — Google Workspace now ships Vids with Gemini generation, Canva has folded AI video into the most widely deployed design tool in the mid-market, and Microsoft 365's trajectory points the same way. Bundling removes precisely the procurement friction that makes this segment slow, which is what carries the curve from a vendor-anchored 5% to 30% by 2028 — still the second-lowest endpoint in the table, because bundled availability creates capability, not the communications practice that uses it.

**Parameters.** Adopting organizations rise 0.2M → 0.6M → 1.2M at ~155 → ~200 generated minutes per organization-year: **31 → 120 → 240 million generated minutes.** This is the one segment funded from operating budgets rather than the attention pool — partially outside the monetization cap — and it is modeled conservatively for exactly that reason: its constraint is organizational habit, not monetization.

## 5.8 The three compounding curves behind every path

Each segment's year-over-year trajectory is the product of three curves stated here once. *(a) Technical completeness — insert → segment → full generation.* The 2026 limits (5–15-second clips, unstable face-and-hand consistency, ~15-second multi-shot windows, partial native audio) confine current practice to inserting AI B-roll into filmed video; as character consistency, minute-scale scenes, and audio synchronization mature, 2027 supports generating roughly half of a piece and 2028 supports fully generated formats. This is the depth multiplier, and it is why the creator segment — depth-driven rather than count-driven — accelerates hardest. *(b) Cost — crossing the stock-footage line.* Retail generation spans roughly $0.03–0.50 per second (workhorse tiers near $0.05–0.15), with self-hosted open-weight inference at $0.007–0.022; a ten-minute first-pass generation therefore costs roughly $30–90 today, and the modeled further 5–10x decline takes it to approximately $3–18 by 2028 — at the lower end, below a stock-footage subscription, past which generation becomes the default rather than the option. *(c) Social acceptance — from "AI slop" to normalization.* The 2025–26 viewer backlash and platform labeling mandates are treated as transitional friction that relaxes as quality crosses detection thresholds and music-licensing disputes settle into royalty structures; acceptance operates on the *ceilings* of the penetration curves above, and it is the model's most falsifiable assumption (Sections 7–8).

## 5.9 The platform synthesis: three pool-owners, one two-axis competitor

Mapped against the platform war among Google, Meta, and Amazon that this series analyzes on the consumer side, the five segments resolve into spheres of vertical integration. Meta and Google own performance advertising (Segments 1 and, for Google, the search-and-YouTube ad surfaces) — the auction, the ad-dollar pool, and now the server-side generation. Google separately owns the creator economy through YouTube — distribution, the Partner Program's monetization pool, and Veo embedded in the creation surface. Amazon owns Western commerce video — the traffic, the conversion telemetry, and free generation tooling for its sellers and advertisers — with the Chinese platforms playing the equivalent integrated role in their market. The pattern is uniform: **supply-side injection, the strongest forcing function in the penetration framework of Section 5.2, appears exactly where a platform owns both the generation model and the monetization pool.** It is also asymmetric in one direction that the rest of this report keeps encountering: Google alone appears in three of the five segments (advertising, creator, and — through Workspace Vids — corporate internal), before counting the world-model and wearable positions of Section 6. The media demand function, read at the platform layer, repeats the same structural pattern: no other single company currently spans as many of these segments within one ecosystem.

## 5.10 The image and audio tracks

Two non-video tracks complete the demand function, dominated by the same customers. **Image generation** — advertising visuals and e-commerce product imagery leading commercial volume — scales ~50 → ~150 billion units at ~0.001 GPU-hours each, contributing 50 → 150 million GPU-hours. **Voice and music** — TTS narration for the creator and corporate segments, AI background music, and the dubbing-localization demand that Segment 4 generates — scales ~0.5 → ~2.5 billion output hours at ~0.01 GPU-hours per hour, contributing 5 → 25 million. Both are workhorse-priced and conversion- or sensory-verified; neither reshapes a total that video dominates throughout.

## 5.11 Totals and the fleet equivalent

**Table 2. Media-track GPU-hours and fleet equivalent (conditional mid-case scenario under the stated intensity assumptions)**

| Item | 2026E | 2027E | 2028E |
|---|---|---|---|
| Video (5 segments, M GPU-hours) | 160 | 648 | 1,506 |
| Image generation (M GPU-hours) | 50 | 90 | 150 |
| Voice & music (M GPU-hours) | 5 | 12 | 25 |
| **Total (M GPU-hours)** | **215** | **750** | **1,681** |
| **Fleet equivalent ('000 H100-equivalent accelerators, at an assumed 50% utilization)** | **49** | **171** | **384** |

The trajectory is a near-eight-fold expansion in GPU-hours over two years — against the roughly two-fold growth of compute-weighted B2B token demand in the companion enterprise model — and, on the conversion assumptions of the companion infrastructure volume, a 2028 fleet equal to roughly 60% of the entire B2B LLM inference fleet and approaching the scale of the coding category alone. The fleet figures are H100-equivalent units at an assumed 50% utilization; production systems mix GPUs, TPUs, and ASICs, so the row measures compute scale, not a chip count. Two cautions attach. This is a conditional mid-case scenario, not a point forecast — plausibly varying by several-fold given the limited observability of production throughput and creator adoption — screened against the advertising-and-subscription monetization pool of Section 3.3 from above and anchored by the segments already in production from below, with the dominant sensitivities being creator generation depth (1.5 → 5 minutes per video), creator adoption (12 → 40%), and the advertising adoption path (2.25 → 8.25 million video-active advertisers) — the three levers carrying the widest uncertainty bands. And the two demand functions should be treated as independent by investors: they respond to different price curves (visual-generation unit costs collapsing on Chinese competition), different supplier sets, and different chip preferences — sustained dense compute for the diffusion-centered media stack against memory bandwidth for autoregressive decode, subject to the center-of-gravity caveat of Section 2.2 (several leading video and world models are themselves autoregressive or hybrid) — a divergence whose hardware consequences the infrastructure volume develops.

---

# 6. Beyond Content: World Models and the Physical-Context Frontier

## 6.1 From video models to world models: Google's integrated path

Video models predict plausible next frames; world models predict how an environment evolves *in response to actions*. The two sit on one technical continuum — a world model is video generation plus physical consistency plus interactivity — and Google currently operates the most visibly integrated position along its full length — the Omni family's fast tier anchoring the consumer video market of Section 4 at one end, the dedicated Genie line examined here at the other — though not alone on any single stretch of it: NVIDIA's Cosmos family positions open foundation models for physical AI, and Meta, World Labs, Waymo, and a range of robotics developers compete on individual layers. Project Genie, opened to Google AI Ultra subscribers in January 2026 and worldwide by May, is built on Genie 3, an autoregressive world model generating navigable interactive environments in real time at 720p/24fps (Google DeepMind has not disclosed its parameter count; the frequently cited 11-billion figure belongs to the original 2024 Genie research model). At I/O 2026 Google connected Street View to Genie, enabling simulation of real-world streets.

The strategic purpose is not entertainment but **training infrastructure**. DeepMind's SIMA 2 agent demonstrably improves at tasks inside Genie-generated worlds without new human examples — the arrangement DeepMind's leadership calls the "Infinite Training Loop" — and Google explicitly positions Genie as a training and evaluation environment for robots and autonomous systems, feeding the Gemini Robotics family of vision-language-action models already collaborating with partners such as Boston Dynamics and Apptronik. The investment translation is a change of market denomination: video generation is a content-market game measured in tens of billions of dollars; world models are a bid on the *training infrastructure of physical AI*, a market plausibly measured in trillions. The caveats are equally important and equally load-bearing: Genie 3 sustains only minutes of consistent interaction, SIMA 2 still struggles with long-horizon tasks, and reliable sim-to-real transfer remains unproven. The metric to track — directly analogous to the autonomous task horizon that governed the digital-agent economy — is **simulation consistency time**.

## 6.2 Glasses and microphones: the interface war moves onto the body

AI-native wearables crossed their commercial threshold in 2025: EssilorLuxottica reported sales of more than seven million Meta AI glasses in the year, more than triple the prior year, with demand for the display-equipped Ray-Ban model strong enough that Meta paused international expansion on inventory constraints. On IDC's category series, 2.25 million display-less smart glasses shipped in Q1 2026, with Meta holding 69.2% of the category, against a full-year 2026 forecast of 13.6 million units and roughly $5.1 billion in revenue. Two measurement caveats attach and are load-bearing for any use of these figures: the seven-million disclosure is a single-source vendor statement (the manufacturing partner of one product line) rather than an industry series, and such statements do not always distinguish cumulative shipments from in-year sales; the IDC series, for its part, covers the display-less category only and is not additive with display-equipped devices. Samsung has confirmed Android XR glasses for 2026, and Apple is widely expected to enter by 2027.

Google's entry defines the strategic logic of the category. Its first consumer Android XR glasses — co-developed with Samsung, styled by Gentle Monster and Warby Parker, launching fall 2026 with iPhone support confirmed — deliberately ship with *no display*: cameras, microphones, and speakers only, with Gemini handling translation, navigation, identification, summarization, and messaging by voice. The design choice reveals the thesis: rather than wait for the hard problem of all-day AR displays, ship the mature components now — always-worn cameras and microphones as **context-collection devices**, voice as the output channel. The essence of the smart-glasses race is not the display; it is the sensor. Whoever is worn all day acquires the deepest personal context, and context is where the durable moat of the AI economy now lives — subject to a real adoption constraint the category has yet to resolve: privacy, consent, on-device processing, and data-retention norms for always-worn cameras and microphones will shape how much of that context can actually be collected and used. Positioning has already split along familiar lines — Meta social-first, Google productivity-and-ecosystem-first — and the wearable is to physical-life context what the desktop agent was to digital-work context: the harness through which the model reaches the substrate.

## 6.3 The two-axis synthesis

The full arc of this report resolves into the frame introduced in Section 2.3. On Axis 1 — digital work context — the war is in its harvest phase: text-centric, verification-rich, monetized against labor, with strengths favoring Anthropic and OpenAI, and its economics measured token by token in the companion enterprise report. On Axis 2 — physical life context — the war is in its sowing phase: perception- and latency-centric, hardware-distributed, monetized against attention and commerce today and physical labor via robotics tomorrow, with strengths favoring Google and Meta. Generative media is Axis 2's first monetizable beachhead; world models are its training infrastructure; wearables are its sensor network. The expansion of AI "from desktop to mobile" is therefore not a form-factor shift but a bifurcation of the battlefield — and the two axes are linked, because a winner on Axis 2 gains distribution leverage back over Axis 1. Google currently fields the most visibly integrated two-axis position — consumer distribution, generative video, interactive world models, robotics models, and wearable hardware partnerships within a single ecosystem. It is not the only serious participant on any individual layer, but no competitor presently covers all of them at once — in this report's judgment, among the most under-priced structural facts in the 2026 landscape.

---

# 7. Risks, Sensitivities, and Unmodeled Factors

**The monetization cap is the model.** Every volume figure in Section 5 is bounded by the advertising-and-subscription pool; the model's largest single vulnerability is therefore not technical but economic. If attention monetization per generated minute falls faster than generation costs (a plausible outcome of "slop" saturation), realized volume undershoots even as capacity soars — the Sora consumer episode in miniature, replayed at industry scale. Conversely, if agentic commerce routes more purchasing through generated content, the transaction volume that content mediates grows, and the cap rises with it. But the same shift cuts both ways: it makes generated video necessary in more places while threatening to make what that video does — persuade — beside the point.

**Volume coefficients carry the widest error bars in this series.** The unit-cost side of the model (GPU-hours per minute, per image, per audio-hour) is informed by observed pricing and published throughput but is not directly measurable from either, and the image and audio coefficients additionally combine technically distinct workloads (TTS and music generation share one coefficient) at coarse resolution. As Section 4.3 states, these are engineering assumptions informed by published throughput and pricing but not identifiable from service prices; the residual risk is one-directional, since continued efficiency gains and open-weight self-hosting would bias the coefficients downward over the forecast, lowering the GPU-hour totals without changing the generated-minute volumes. The volume side — creator adoption rates and generated-minutes-per-published-video above all — rests on adoption judgments with order-of-magnitude bands, materially wider than any coefficient in the enterprise token model. The segment allocation is more defensible than the total.

**The social-acceptance assumption is falsifiable and could fail.** The model treats labeling mandates and the anti-slop backlash as transitional friction normalizing through 2027–28. A durable regulatory or platform-policy regime that suppresses AI-generated content distribution — mandatory prominent labeling with demonstrated engagement penalties, for instance — would bind the creator-economy and ad-creative segments directly.

**Supply-side measurement asymmetries.** Seedance distributes primarily through ByteDance's Doubao ecosystem without a public Western API at the time of writing, limiting independent verification of usage and pricing claims; leaderboard positions reshuffle monthly; and several capability claims circulate through promotional secondary sources. Wearables data carries the single-source and cumulative-versus-in-year caveats noted in Section 6.2. Institutional use of any single figure herein should rest on primary-source triangulation rather than any single vendor disclosure, per the caveats flagged in Sections 4.3, 6.2, and this section.

**World-model risk is concentrated in two unproven links.** The trillion-dollar framing of Section 6.1 requires both extended simulation consistency (currently minutes) and reliable sim-to-real transfer (currently undemonstrated at scale). Until both are shown, world models should be valued as an option, not a discounted cash flow.

**Interaction with the enterprise track.** The two demand functions are modeled as independent, but they compete for the same accelerator supply at the margin. A media demand surprise on the upside would tighten the inference-capacity market that the enterprise track also draws on — a channel the companion infrastructure volume quantifies.

---

# 8. Tracking Indicators for H2 2026 and Beyond, with a Closing Synthesis

The model is built to be falsified on a short horizon. On the content economy: the per-clip and per-second generation cost curve, where each step down pulls forward the media fleet; video-model leaderboard churn and the share of professional workflows on multi-model aggregators; the generated share of published video minutes on major platforms, the direct read on the insert-to-segment-to-full-generation progression; and ad-platform disclosures of AI-generated creative share in auction volume, the cleanest confirmation of the machine-verified volume engine. On monetization: effective CPM and revenue-per-generated-minute trends for AI-heavy channels versus baseline, the live read on the cap; and any repeat of the Sora pattern — consumer generation products shut or throttled for burn — which marks the cap binding. On the physical-context frontier: simulation consistency time and documented sim-to-real transfers, the Axis-2 task-horizon analogue; smart-glasses unit shipments and platform shares as Android XR launches and Apple's entry timing resolves; and robotics-partnership commercialization milestones in the Gemini Robotics ecosystem.

A closing synthesis. The enterprise report argued that 2026–2028 would be remembered as the interval in which "which industries adopt AI" gave way to "which verification mechanisms automate next." This report extends the sequence off the desktop: the advertising auction automated first among media workloads because its verifier was already a machine; the segments verified by human senses follow as cost and quality cross their thresholds; and the frontier beyond content — world models and wearables — is the machinery by which AI acquires the physical context that no document ever contained. Token demand was the shadow the first front cast on the infrastructure market. GPU-hours are the shadow of the second — and the companion infrastructure volume reads both shadows onto silicon together.

---

# References

Artificial Analysis. "Text-to-Video Leaderboard" and "Video Model Comparisons" (Seedance, HappyHorse, Kling, Veo Arena Elo and per-minute pricing). Accessed July 2026. https://artificialanalysis.ai/video/leaderboard/text-to-video

BuildMVPFast. "Best Text-to-Video AI Generators July 2026: Top 10 Models Ranked" (Sora shutdown dates; Seedance 2.5, Kling 3.0 Turbo, Gemini Omni Flash pricing). July 2026. https://www.buildmvpfast.com/articles/best-llms-2026-guide/video-generation-ai

GMI Cloud. "GPU Cloud Cost for AI Inference at Scale in 2026" (managed-inference video pricing ~$0.07/clip; H100 on-demand rates). March 2026. https://www.gmicloud.ai/en/blog/gpu-cloud-cost-ai-inference-at-scale

AI/ML API. "Best AI Video Generators 2026: Veo 3.1, Kling, Sora 2, Seedance & More Compared." April 2026. https://aimlapi.com/blog/best-ai-video-generators-2026-veo-3-1-kling-sora-2-seedance-more-compared

Amazon seller and marketplace statistics. Marketplace Pulse and Seller Assistant, "Amazon Statistics for Sellers 2026" (~1.6M active sellers; third-party GMV). April 2026. https://www.sellerassistant.app/blog/amazon-statistics-for-sellers-in-2026-key-insights/


Atlas Cloud. "Seedance vs Kling vs Sora vs Veo: Head-to-Head Comparison." May 2026. https://www.atlascloud.ai/blog/guides/seedance-vs-kling-vs-sora-vs-veo

Campus Technology. "Google Unveils Android XR Smart Glasses, Powered by Gemini AI." May 22, 2026. https://campustechnology.com/articles/2026/05/22/google-unveils-android-xr-smart-glasses-powered-by-gemini-ai.aspx

CoderSera / CatDoes / Composio (agentic-war context for OpenAI resource reallocation): "Claude Code vs OpenAI Codex" comparison series. April–June 2026. https://codersera.com/blog/claude-code-vs-openai-codex-2026/

DevTk.AI. "AI Video API Pricing 2026." February 2026. https://devtk.ai/en/blog/ai-video-generation-pricing-2026/

The Gadgeteer. "Google AI Smart Glasses Introduced" (EssilorLuxottica 7M+ Meta AI glasses sold in 2025). April 2026. https://the-gadgeteer.com/2026/04/27/google-android-xr-ai-smart-glasses/

Forbes (Liu, P.). "How Much OpenAI May Be Spending on AI-Generated Sora Videos" (outside estimate of Sora inference costs and its stated assumptions). November 10, 2025. https://www.forbes.com/sites/phoebeliu/2025/11/10/openai-spending-ai-generated-sora-videos/

Google. "Android XR at I/O 2026" (consumer AI glasses: fall 2026 launch, audio-first design, Android and iPhone support). May 2026. https://blog.google/products-and-platforms/platforms/android/android-xr-io-2026/

Google Blog. "Project Genie: AI world model now available for Ultra users." January–February 2026. https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/

Google Blog. "Project Genie Expands" (worldwide Ultra availability; Street View integration). May 2026. https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/

Google DeepMind. "Genie 3: A New Frontier for World Models" (720p/24fps real-time interactive environments; parameter count undisclosed). https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/

IDC. "Smart Glasses Surge: The XR Market Is Rewriting Its Own Rules" (Q1 2026 display-less shipments 2.25M; Meta share 69.2%; 2026 forecast 13.6M units, ~$5.1B). 2026. https://www.idc.com/resource-center/blog/smart-glasses-surge-the-xr-market-is-rewriting-its-own-rules/

Google Blog. "I/O 2026 developer highlights: Antigravity, Gemini API, AI Studio." May 2026. https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/

Google DeepMind. "Gemini Robotics" model pages and blog series (2025–2026). https://deepmind.google/models/gemini-robotics/

Google DeepMind. "Gemini Robotics ER-1.6." April 2026. https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/

Meta Platforms. "Meta's AI Product News from Connect" (more than 1 million advertisers using generative AI ad tools; 15 million ads generated in one month). September 2024. https://about.fb.com/news/2024/09/metas-ai-product-news-connect/

Meta Platforms. "Performance Talks: How Zenith and Farfetch Are Using AI to Drive Results" (more than 10 million advertising businesses). https://about.fb.com/news/performance-talks-how-zenith-and-farfetch-are-using-ai-to-drive-results/

Netflix. Second Quarter 2025 Earnings Interview (first generative-AI final footage in a released title). July 2025. https://ir.netflix.net/investor-news-and-events/investor-events/event-details/2025/Netflix-Second-Quarter-2025-Earnings-Interview-2025--ZzeVaVp2V/default.aspx

NVIDIA. "NVIDIA Launches Cosmos 3, the Open Frontier Foundation Model for Physical AI." 2026. https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai

OpenAI. "What to Know About the Sora Discontinuation" (app discontinued April 26, 2026; API September 24, 2026). 2026. https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation

Runway. "Runway Partners with Lionsgate." September 2024. https://runwayml.com/news/runway-partners-with-lionsgate

Lushbinary. "AI Video Generation 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 Compared." April 2026. https://lushbinary.com/blog/ai-video-generation-sora-veo-kling-seedance-comparison/

Memeburn. "Google AI Smart Glasses 2026: Gemini, iPhone Support, Meta Rival." May 2026. https://memeburn.com/google-ai-smart-glasses-2026-gemini-iphone-meta/

Notebookcheck. "Google Android XR smart glasses launching this fall with Gemini AI." May 2026. https://www.notebookcheck.net/Google-Android-XR-smart-glasses-launching-this-fall-with-Gemini-AI.1300619.0.html

Pinggy. "Best Video Generation AI Models in 2026." May 2026 (leaderboard details as of the May snapshot). https://pinggy.io/blog/best_video_generation_ai_models/

Stack Overflow. "2025 Developer Survey: AI" (84% of professional developers use or plan to use AI tools; 51% daily use). 2025. https://survey.stackoverflow.co/2025/ai

Pixflow. "Best AI Video Generator in 2026." June 2026. https://pixflow.net/blog/best-ai-video-generator/

Shopify. "Global Ecommerce Sales Growth Report 2026" (global e-commerce base and SKU context). 2026. https://www.shopify.com/blog/global-ecommerce-sales

Teleprompter. "2025 YouTube Statistics: Global Overview and Key Trends" (~500 hours uploaded per minute; ~65M active creators). December 2025. https://www.teleprompter.com/blog/2025-youtube-statistics

YouTube Official Blog. "Second Chances on YouTube" (more than 3 million channels in the YouTube Partner Program). https://blog.youtube/inside-youtube/second-chances-on-youtube/

TechCrunch. "Google's Genie world model can now simulate real streets with Street View." May 19, 2026. https://techcrunch.com/2026/05/19/googles-genie-world-model-can-now-simulate-real-streets-with-street-view/

TechTimes. "DeepMind World Models Train Robots in Imagined Worlds: SIMA Practices Inside Genie 3." June 6, 2026. https://www.techtimes.com/articles/317932/20260606/deepmind-world-models-train-robots-imagined-worlds-sima-practices-inside-genie-3-model.htm

UploadVR. "Google Gemini Smart Glasses Launching in Fall to Take on Ray-Ban Meta." June 2026. https://www.uploadvr.com/gemini-smart-glasses-are-launching-in-fall-to-take-on-ray-ban-meta/

---

*Disclaimer: This report is for informational purposes only and does not constitute investment advice. Quantitative estimates herein are order-of-magnitude modeling assumptions, not measured data, and are documented as adjustable inputs in the media sheet of the companion workbook (Agentic AI Token Demand Model workbook: Section C and the Media Model derivation sheet). Vendor-disclosed figures (pricing, unit shipments, leaderboard positions) carry the verification caveats noted in Sections 6–7.*
