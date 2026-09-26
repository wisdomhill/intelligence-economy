---
title: "12. The 2025 AI Accelerator Market"
subtitle: "Stock, flow, and the vertical-integration wedge — with a first read on 2026"
series: "The Intelligence Economy"
number: 12
manuscript-revision: 1
date: 2026-09-26
date-modified: 2026-09-26
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  What was actually built. Four years of accelerator deliveries measured in
  H100-equivalents and in dollars, the gap between cost share and capacity
  share, and the wedge vertical integration opens.

keywords:
  - AI accelerator
  - H100-equivalent
  - TPU
  - Trainium
  - vertical integration
  - cost share

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
#
# Unlike Reports 7 to 11, this manuscript leaves its Executive Summary
# unnumbered and starts the numbering at Data and Method, so the summary sits
# on the cover and chapter 1 is the first chapter page. Its single
# cross-reference, to Section 6, means the chapter of that number.
#
# The author right-aligned the numeric columns in the manuscript itself; the
# conversion carries that through and adds only the column widths.
published:
  dir: reports/r12/
  pdf: r12-the-2025-ai-accelerator-market.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r12/

chapters:
  - manuscript: "1. Data and Method"
    published:  "1. Data and Method"
    fragment:   _01-data-and-method.qmd
    page:       01-data-and-method.qmd
  - manuscript: "2. The 2025 Build-Out"
    published:  "2. The 2025 Build-Out"
    fragment:   _02-build-out.qmd
    page:       02-build-out.qmd
  - manuscript: "3. The Supplier Landscape: Dominant Flow, Eroding Stock"
    published:  "3. The Supplier Landscape"
    fragment:   _03-suppliers.qmd
    page:       03-suppliers.qmd
  - manuscript: "4. The Owner Landscape: Cost Share versus Capacity Share"
    published:  "4. The Owner Landscape"
    fragment:   _04-owners.qmd
    page:       04-owners.qmd
  - manuscript: "5. The Vertical-Integration Wedge"
    published:  "5. The Vertical-Integration Wedge"
    fragment:   _05-wedge.qmd
    page:       05-wedge.qmd
  - manuscript: "6. First Read on 2026: Nvidia versus Google in Q1"
    published:  "6. First Read on 2026"
    fragment:   _06-first-read-2026.qmd
    page:       06-first-read-2026.qmd
  - manuscript: "7. Strategic Implications"
    published:  "7. Strategic Implications"
    fragment:   _07-implications.qmd
    page:       07-implications.qmd
  - manuscript: "Appendix A — Data Definitions and Caveats"
    published:  "Appendix A"
    fragment:   _08-appendix.qmd
    page:       08-appendix.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _09-references.qmd
    page:       09-references.qmd
---
# The 2025 AI Accelerator Market

### Stock, Flow, and the Vertical-Integration Wedge — with a First Read on 2026

**The Intelligence Economy — Report 12 of 14**

**Wisdom Hill Research | Thematic Research | July 2026**

---

# Executive Summary

In 2025, the AI accelerator build-out tripled. Within this report's price-covered analytical universe (defined in §1.4), cumulative delivered/allocated compute grew from an estimated 6.51 million H100-equivalents (H100e) at the end of 2024 to 20.08 million at the end of 2025, while cumulative estimated chip purchase cost rose from ~$148B to ~$339B. The pace accelerated within the year — quarterly net additions climbed from +2.5M H100e in Q1 to +4.4M in Q4 — even as the estimated chip cost of new capacity fell, as Blackwell and TPU v6e ramped.

Beneath that headline growth, this report identifies one central structural pattern: **Nvidia dominates the flow of new spending but is losing share of the stock, and the erosion comes from two directions unrelated to merchant-market pricing.** Nvidia captured roughly 79% of 2025 net dollar additions, yet its share of the cumulative installed base fell on both metrics during the year — from 71.1% to 66.8% of compute, and from 83.2% to 80.8% of estimated chip cost. The first source of erosion is hyperscaler in-house silicon: Google TPU gained +4.4pp of cumulative compute share while its cost share slipped −0.3pp, meaning TPU's estimated chip cost per H100e is falling faster than the industry blend. The second is Chinese domestic substitution: Huawei was the largest cost-share gainer of any supplier (+1.8pp) and, within the price-covered universe, captured about 85% of China's 2025 compute additions. Neither shift is a merchant-market decision — one reflects workload ownership, the other export-control policy.

The economics behind the first erosion force are stark. On Epoch's chip-cost estimates, TPU v6e carries an estimated chip cost of ~$4,375 per H100e against ~$25,000 for Nvidia H100/H200 — a ~5.7× gap in estimated chip cost per unit of peak compute. As a gross chip-cost counterfactual (full H100e substitution, chip cost only), Google's TPU fleet corresponds to ~$31–70B of foregone Nvidia chip purchases; Amazon's Trainium2 fleet ~$8–17B. The consequence is visible in the demand-side league table: in a single year, the combined compute share of the two vertically integrated hyperscalers (Google + Amazon) rose from 31.4% to 36.7%, while the merchant-dependent pair (Microsoft + Meta) fell from 30.9% to 28.4% — a 7.8 percentage-point relative swing. Google now holds the largest estimated compute fleet by H100e while ranking only third by estimated chip cost.

China is the mirror image of this efficiency story. Its ~$46B cumulative estimated chip cost — the fourth largest of any cohort — corresponds to only 1.12M H100e, an estimated ~$41,200 per H100e. On Epoch's estimates, that is roughly **2.7× the rest-of-sample average** of ~$15,400/H100e — a descriptive gap of about $29B, not a causal estimate of the cost of export controls, since product mix, supplier pricing, and procurement timing are not controlled for.

This edition adds a first read on 2026. Epoch AI's quarterly shipment data for Q1 2026 currently covers only Nvidia and Google — the single most consequential competitive axis on the supply side. The new data complicates the 2025 narrative: **Nvidia re-accelerated while Google's TPU shipment flow stalled in a generational transition.** Nvidia shipped 3.39M H100e in Q1 2026 (+14.5% QoQ, 100% Blackwell, with B300 approaching one million units), while Google shipped 0.85M (+2.1% QoQ) as collapsing v6e volumes offset a steep v7 (Ironwood) ramp. Google's share of the two-player compute flow has declined for two consecutive quarters — from 25.3% in Q3 2025 to 20.0% in Q1 2026 — and its *cumulative* two-player compute share ticked down for the first time in the dataset. The per-H100e chip-cost wedge (~3.3×) and TPU's power-efficiency advantage remain fully intact, so the question Q1 2026 poses is about *volume trajectory*, not unit economics. Section 6 states falsification criteria for both readings, observable within two quarters.

Unless otherwise stated, every number in this report refers to the price-covered analytical universe defined in §1.4, not to all chips tracked by Epoch AI. All figures are median estimates from Epoch AI's public datasets. Unit-count and H100e estimates generally carry 90% intervals (typically spanning ~2×); chip-cost estimates do not. H100e reflects peak arithmetic throughput only and does not credit HBM memory capacity (§1.2), so it understates Nvidia's effective position and overstates Google's cost advantage on memory-bound workloads. Findings should be read as directional and structural, not unit-precise.

---

# 1. Data and Method

## 1.1 Sources

This report combines two Epoch AI public datasets: **Data on AI Chip Owners** (owner × chip-type cumulative snapshots; May 2026 snapshot) and **Data on AI Chip Sales** (quarterly shipments by designer × chip; July 2026 snapshot). Owner data is used for the cumulative stock analysis (§2–5); shipment data for the Q1 2026 flow analysis (§6). Epoch AI is a non-profit research institute; its datasets are published under CC BY with methodology notebooks and are anchored against primary disclosures (Nvidia data-center revenue, AMD Instinct commentary, Broadcom TPU-related revenue).

A conflict-of-interest note: Epoch AI discloses funding and contractual relationships with organizations affected by AI, including large AI companies (e.g., Google), and partnered with OpenAI on the FrontierMath benchmark; its principal funder, formerly Open Philanthropy, was renamed Coefficient Giving in November 2025. Since Google, Nvidia, and Amazon are the subjects of this analysis, readers should weight the estimates accordingly. The datasets remain the most complete public reconstruction of the global AI compute stock, and have been cited or visualized by third parties including Visual Capitalist.

## 1.2 The H100e metric and cost basis

Compute is normalized in **H100-equivalents**: each chip's peak dense 8-bit throughput divided by the H100's, multiplied by unit count. A TPU v7 counts as ~2.3 H100e; a TPU v6e ~0.93. H100e is a peak-throughput proxy — it does not capture memory bandwidth, interconnect, or workload-specific software efficiency, and therefore overstates the workload-equivalence of chips with weaker memory systems.

One dimension of this limitation deserves emphasis, because it works against Nvidia — and in Google's favor — throughout this report. **H100e reflects only peak arithmetic throughput (FLOPs) and assigns no credit to HBM memory capacity.** Nvidia chips frequently pair a given level of compute with substantially more HBM than same-generation alternatives: the B300, for example, carries similar peak throughput to the B200 and to Google's TPU v7, but a markedly larger HBM stack. For memory-bound workloads — long-context inference, large KV caches, and mixture-of-experts serving — an H100e of Nvidia capacity can therefore deliver more effective performance than an H100e of TPU capacity. This report's central finding is that TPU compute is cheaper per H100e; because H100e credits only peak compute and ignores Nvidia's larger memory, that finding overstates Google's true cost advantage and understates Nvidia's effective position. The vertical-integration wedge in §5 should be read with this bias in mind.

Because the owner dataset does not carry chip cost, **estimated chip cost is computed by applying a single per-chip cost to each chip type** (from Epoch's AI Chip Sales chip-cost estimates) across owner unit counts. This is estimated chip purchase cost only — it excludes servers, networking, power, and facilities, and is not full-system TCO. The custom-versus-merchant comparison is not fully like-for-like: on Epoch's methodology, custom-chip figures estimate payments to supply partners, while merchant-chip figures estimate average end-customer purchase prices. Both exclude server- and facility-level costs.

## 1.3 Stock versus flow

- **§2–5 analyze the stock**: cumulative delivered/allocated compute per owner/supplier. "Net additions" are differences between cumulative snapshots.
- **§6 analyzes the flow**: quarterly shipments per supplier. This is the appropriate lens for the Q1 2026 update, which reports shipments only.

The two reconcile: cumulating shipment data through Q4 2025 matches the cumulative stock totals within ~1%.

## 1.4 Scope, exclusions, confidence

The datasets cover the major designers (Nvidia, Google, Amazon, AMD, Huawei, and Cambricon). **All quantitative analyses in this report — compute volume, ownership and supplier shares, growth, quarterly flows, and cost — are restricted to chip types for which Epoch provides a cost estimate.** Trainium1 and Cambricon Siyuan 590 carry no cost estimate and are therefore excluded from every quantitative calculation; they may be discussed qualitatively but never enter numerical totals or denominators. Together they represent 0.6% of Q4 2025 H100e, so the restriction does not affect any conclusion. We refer to this as the report's *price-covered analytical universe*. Data excludes chips smuggled into China and offshore compute rented by Chinese firms. Ownership tracks who *holds* the chip, not who *uses* it; Epoch attributes cloud-provided compute to the cloud owner, and explicitly cautions against using the ownership data for financial-asset analysis. Q1 2026 shipment data is provisional and covers only Nvidia and Google. Data extracted from Epoch AI: AI Chip Owners (May 2026 snapshot), AI Chip Sales (July 2026 snapshot).

---

# 2. The 2025 Build-Out

## 2.1 Four years of cumulative trajectory

| Year-end (Q4) | Delivered H100e | YoY adds | Cumulative chip cost ($B) | YoY adds ($B) | Blended $/H100e |
|---|---:|---:|---:|---:|---:|
| 2022 | 0.28M | — | 10.1 | — | 36,346 |
| 2023 | 1.57M | +1.30M | 42.1 | +32.0 | 26,774 |
| 2024 | 6.51M | +4.94M | 148.2 | +106.0 | 22,761 |
| **2025** | **20.08M** | **+13.57M** | **338.7** | **+190.6** | **16,870** |

*Note: Price-covered chips only; Trainium1 and Cambricon Siyuan 590 are excluded from all quantitative calculations. YoY adds and blended $/H100e are computed from unrounded source data and may differ marginally from arithmetic on the displayed cumulative figures.*

Delivered compute grew ~72-fold in three years while blended estimated chip cost per H100e fell by more than half. Three forces drove the decline: the Hopper→Blackwell transition (B200 at ~$14,645/H100e vs H100 at $25,000), custom-silicon penetration at ~$4,000–5,000/H100e for the latest TPU/Trainium generations, and AMD's MI300-family pricing in the ~$9,000–11,500 range.

## 2.2 Quarterly momentum within 2025

Net additions accelerated every quarter, ending at a Q4 run-rate of roughly +4.4M H100e and +$60B per quarter. The estimated chip cost of marginal capacity fell across the year, with the steepest improvement mid-year as B200 and TPU v6e hit volume; the decline then flattened into Q4 as costlier chips entered the blend — B300 alongside B200, TPU v7 replacing v6e. This is a composition effect, not like-for-like repricing: Nvidia's own blended flow cost continued to fall through Q4 as Hopper exited the mix (§6.2), and B300's first full-volume quarter arrived only in Q1 2026.

---

# 3. The Supplier Landscape: Dominant Flow, Eroding Stock

## 3.1 The concentration snapshot — and its first derivative

At Q4 2025, Nvidia holds 80.8% of cumulative estimated chip cost but only 66.8% of delivered compute. That ~14pp gap reflects the merchant-silicon premium. Every alternative platform trades at a discount per unit of compute except Huawei, whose premium reflects domestic-substitution pricing rather than market power.

| Supplier | H100e share Q4 2024 | H100e share Q4 2025 | Δ (pp) | Cost share Q4 2024 | Cost share Q4 2025 | Δ (pp) |
|---|---:|---:|---:|---:|---:|---:|
| **Nvidia** | 71.12% | 66.84% | **−4.28** | 83.25% | 80.81% | **−2.45** |
| **Google TPU** | 14.53% | 18.94% | **+4.41** | 7.63% | 7.37% | **−0.26** |
| Amazon Trainium2 | 3.16% | 4.58% | +1.41 | 0.85% | 1.65% | +0.81 |
| AMD | 8.42% | 6.12% | −2.30 | 3.55% | 3.68% | +0.13 |
| **Huawei** | 2.77% | 3.53% | +0.76 | 4.72% | 6.49% | **+1.77** |

*Note: Price-covered chips only; Trainium1 and Cambricon Siyuan 590 are excluded from all quantitative calculations.*

Three patterns carry the supply-side thesis.

**Nvidia lost cumulative share on both metrics while dominating the flow.** Nvidia captured roughly two-thirds of 2025 net compute additions and about four-fifths of net dollar additions — and still ceded 4.3pp of compute share, because TPU and Huawei grew proportionally faster. A methodological note bounds the forward extrapolation: cumulative share converges toward the ongoing flow share. Nvidia's 2025 flow share of net compute additions was below its opening stock share of 71.1%, which pulled cumulative share down to 66.8%. If future flow share holds near its 2025 level, cumulative share converges toward that level — not below it. A sub-60% cumulative outcome would require Nvidia's *future flow share* to fall below 60%, or disproportionate retirement of its installed stock.

**Google TPU's share shift is uniquely asymmetric.** TPU gained +4.41pp of compute share while its cost share slipped −0.26pp — a pattern visible nowhere else. As chips with an estimated ~$4,000–5,000/H100e cost replace v4/v5 generations in the cumulative mix, TPU adds compute more cheaply than the industry blend. Its estimated unit economics are improving faster than the market's — the strongest single signal for the durability of Google's vertical-integration advantage.

**AMD shows the opposite asymmetry.** AMD's compute share fell (−2.30pp) even as its cost share crept up — it added dollars at lower compute-per-dollar than its own 2024 mix. Absent an MI400-class step change or a second hyperscaler anchor, AMD's share trajectory is structurally constrained.

## 3.2 Nvidia — ~$274B of stock, and a Blackwell-only future

Nvidia's cumulative estimated chip cost reached ~$273.7B at Q4 2025, on 13.42M H100e. The composition of its 2025 net additions tells the strategic story:

| SKU | 2025 net H100e adds (M) | 2025 net chip cost ($B) | $/H100e on adds | Cumulative H100e Q4 2025 (M) |
|---|---:|---:|---:|---:|
| B200 | +4.27 | +62.6 | 14,662 | 4.76 |
| B300 | +3.74 | +63.7 | 17,024 | 3.74 |
| H100/H200 | +0.70 | +17.6 | 25,219 | 4.25 |
| H20 (China) | +0.08 | +6.4 | 80,231 | 0.22 |

*Note: Price-covered chips only. A100 is omitted (zero net additions in 2025). Figures use Epoch AI Chip Sales cost estimates applied to owner unit counts.*

Blackwell (B200 + B300) supplied the overwhelming majority of 2025 net additions — roughly $126B of ~$150B, or about 84%. Hopper effectively stopped growing (+0.70M H100e against a 4.25M cumulative base), leaving a large 2024-vintage fleet depreciating against Blackwell-priced marginal capacity. The China-market H20 remains an economic anomaly: about 1.49M cumulative units delivering only ~223k H100e (an effective ~$80,000/H100e).

## 3.3 Google TPU — the industry's cost curve, bent

On Epoch's cost estimates, applying the AI Chip Sales per-chip costs (v6e $4,059/chip, v7 $11,737/chip), Google's TPU program is the most cost-efficient large-scale silicon effort in the dataset:

| TPU generation (cumulative Q4 2025) | H100e (M) | Est. chip cost ($B) | $/H100e |
|---|---:|---:|---:|
| v6e (Trillium) | 2.29 | 10.0 | **4,375** |
| v7 (Ironwood) | 0.69 | 3.5 | **5,034** |
| v5e | 0.47 | 6.5 | 13,616 |
| v5p | 0.31 | 4.0 | 12,982 |
| v4 | 0.04 | 0.9 | 24,388 |

The discontinuity sits between v5p and v6e — roughly a 3× improvement in estimated cost per H100e in one generation. TPU v6e at ~$4,375/H100e is ~5.7× cheaper than H100/H200 and ~3.3× cheaper than B200 per unit of peak compute: the single most disruptive number in this dataset.

## 3.4 Amazon Trainium — the same playbook, two years behind

Trainium2 carries an estimated chip cost of ~$6,100/H100e — 2.4× cheaper than B200, though above TPU v6e. Amazon's entire quantified in-house growth came from Trainium2, whose cumulative H100e **more than quadrupled** during 2025 (0.21M → 0.92M). Within the price-covered universe, Trainium2 supplies ~39% of Amazon's compute at ~17% of its estimated chip cost. (Trainium1, deployed since 2022, is discussed only as qualitative context for the length of AWS's in-house program; because Epoch provides no cost estimate for it, it is excluded from all calculations in this report.) Scale and NRE amortization are plausible contributors to the cost gap versus TPU, but the Epoch dataset does not decompose or causally attribute it.

## 3.5 AMD — one anchor customer, structural ceiling

AMD's ~$12.5B cumulative estimated chip cost (3.7% of industry) is strategically pivotal despite its size: MI300X at ~$9,500/H100e is one of the cheapest large-volume *merchant* accelerators, well below H100/H200. But the customer book exposes the constraint. Meta is the only hyperscaler using AMD at scale (~20% of Meta's compute); Microsoft and Oracle hold modest hedge positions; Google, Amazon, CoreWeave, and xAI are absent — the first two because in-house silicon answers the second-source question, the latter two because of CUDA-locked stacks or Nvidia-only fleets. AMD's constraint is the absence of a second hyperscaler anchor customer approaching Meta's scale; its growth path runs through the "Other" cohort and sovereign buyers.

## 3.6 Huawei — domestic substitution without a price discount

Huawei's fleet sits entirely within China: ~0.71M H100e at ~$22B — a blended ~$31,000 per H100e once earlier-generation Ascend volumes are included. On Epoch's assumptions, the current Ascend 910C is priced roughly at parity with H100/H200 per peak H100-equivalent (~$26,000/H100e vs $25,000) despite its lower per-chip compute (~0.77 H100e/unit) — i.e., Chinese buyers acquire domestic supply at Nvidia-level or higher per-H100e cost, which is the premium visible in §3.1. Within the price-covered universe, Huawei captured about 85% of China's 2025 compute additions and was the industry's largest cost-share gainer (+1.77pp). China has only two domestic accelerator designers in the dataset, Huawei and Cambricon; Cambricon's Siyuan 590 accounts for only ~5% of Chinese-designed H100e and carries no cost estimate, so this report's China figures reflect Huawei alone. They therefore describe domestic Huawei supply, not the entirety of China's domestically designed accelerator base.

The combined supply-side message: **Nvidia's cumulative-stock position is eroding simultaneously from the high-volume end (hyperscaler in-house silicon) and the geopolitical end (domestic substitution)** — neither driven by merchant-market competition.

---

# 4. The Owner Landscape: Cost Share versus Capacity Share

## 4.1 The most diagnostic gap: cost share minus capacity share

For each owner, the gap between share of cumulative estimated chip cost and share of cumulative compute measures procurement efficiency:

| Owner | Delivered H100e (M) | Est. chip cost ($B) | Cost share | Capacity share | Gap (pp) | $/H100e | H100e per $B |
|---|---:|---:|---:|---:|---:|---:|---:|
| Google | **5.03** | 48.7 | 14.4% | **25.1%** | **+10.7** | 9,683 | 103,272 |
| Microsoft | 3.41 | 63.6 | 18.8% | 17.0% | −1.8 | 18,666 | 53,573 |
| Other | 3.36 | 61.8 | 18.2% | 16.7% | −1.5 | 18,389 | 54,379 |
| Amazon | 2.34 | 32.6 | 9.6% | 11.7% | +2.1 | 13,941 | 71,731 |
| Meta | 2.30 | 39.7 | 11.7% | 11.4% | −0.3 | 17,296 | 57,818 |
| Oracle | 1.14 | 20.1 | 5.9% | 5.7% | −0.2 | 17,597 | 56,829 |
| China | 1.12 | 46.1 | 13.6% | 5.6% | **−8.0** | 41,194 | 24,276 |
| CoreWeave | 0.83 | 15.9 | 4.7% | 4.1% | −0.6 | 19,161 | 52,189 |
| xAI | 0.55 | 10.2 | 3.0% | 2.7% | −0.3 | 18,509 | 54,028 |

*Note: Price-covered chips only; Trainium1 and Cambricon Siyuan 590 are excluded from all quantitative calculations. "China" here comprises Huawei's price-covered Ascend chips only; the other domestic designer, Cambricon, is ~5% of Chinese-designed H100e and carries no cost estimate, so it is excluded.*

Google extracts ~103,000 H100e per billion dollars of estimated chip cost — ~1.9× Microsoft's ~53,600. China sits at ~24,300, paying roughly 2.4× its capacity weight in estimated dollars.

By compute, Google ranks #1, Microsoft #2, and the "Other" residual #3; by estimated chip cost, Microsoft ranks #1 and "Other" #2. The "Other" cohort spans Tier-2 clouds, sovereign AI, and enterprise; because Epoch attributes cloud-provided compute to the cloud owner, it does not isolate individual cloud tenants.

## 4.2 The Big Four

**Google** holds the largest estimated compute fleet by H100e while ranking third by estimated chip cost — TPU supplies ~75.6% of its compute at ~51% of its estimated cost. Google also owns an estimated ~1.2M H100e of Nvidia capacity, likely serving a mix of Google Cloud customer workloads and internal applications; the dataset does not identify the workloads assigned to these GPUs.

**Microsoft** is Google's mirror image: the largest cumulative estimated chip-cost deployer (~$64B) extracting roughly half the compute per dollar. Its structural exposure is a large cumulative H100/H200 base — the installed asset most exposed to Blackwell-driven repricing, a capex treadmill Google and Amazon partially escape by self-supplying.

**Amazon** holds the second-best cost position (~$13,900/H100e) on the strength of Trainium2. Amazon is not substituting away from Nvidia but scaling both in parallel: roughly 58% of its 2025 net H100e additions came from Nvidia (merchant frontier compute and EC2 GPU instances) against ~42% from Trainium2 (dedicated large-scale workloads, most prominently Anthropic's Project Rainier training cluster).

**Meta** demonstrates the third route: no in-house silicon at scale, but the heaviest AMD adoption among hyperscalers (~20% of compute at ~11% of cost). The result: Meta's ~$17,300/H100e beats Microsoft's ~$18,700 despite equal dependence on merchant silicon.

## 4.3 The specialty cohort

**Oracle** is executing a leveraged Nvidia bet on OCI bookings, with a moderate AMD hedge. **CoreWeave** is the textbook neocloud profile: 100% Nvidia, the highest unit cost among non-China owners (~$19,200/H100e). **xAI** grew in a single step function in Q3 2025 in Epoch's lumpy, data-center-based allocation; the dataset does not establish the precise deployment event responsible. The **"Other" residual** is quietly a top-cohort by both compute and estimated cost, with healthy AMD penetration.

## 4.4 China — the most expensive compute, substituting fast

China's cumulative estimated chip cost reached ~$46B — larger than Meta's — but corresponds to only 1.12M H100e at ~$41,200 each, roughly 2.7× the rest-of-sample average. Two dynamics run in parallel. First, the H20's punishing arithmetic: ~1.49M cumulative units delivering ~223k H100e implies an effective ~$80,000/H100e. Second, substitution is accelerating: within the price-covered universe, Huawei took about 85% of China's 2025 net compute additions, moving its share of China's cumulative compute from ~36% to ~63% in twelve months.

The 2.7× figure is a descriptive gap (~$29B against the rest-of-sample blended rate), **not a causal estimate of the cost of export controls**, because product mix, supplier pricing, and procurement timing are not controlled for.

---

# 5. The Vertical-Integration Wedge

## 5.1 Unit economics

On Epoch's estimated chip costs, the in-house platforms carry a large advantage in cost per H100e over the merchant Nvidia capacity the same owners buy:

| Owner | In-house platform | $/H100e (in-house) | $/H100e (own Nvidia mix) | Wedge |
|---|---|---:|---:|---:|
| Google | TPU (blended) | 6,562 | 19,330 | 2.9× |
| Google | TPU v6e vs H100/H200 | 4,375 | 25,005 | **5.7×** |
| Google | TPU v7 vs B200 | 5,034 | 14,645 | 2.9× |
| Amazon | Trainium2 (blended) | 6,094 | 19,010 | 3.1× |
| Amazon | Trainium2 vs B200 | 6,094 | 14,645 | 2.4× |

*Note: Q4 2025 cumulative, price-covered chips only; Trainium1 excluded (no cost estimate). "Own Nvidia mix" is the blended $/H100e of the Nvidia chips that same owner holds. B200 rows use the per-chip cost estimate (~$14,645/H100e); the realized figure on Nvidia's 2025 additions (§3.2) differs marginally due to rounding of the unit mix.*

A 2.4–5.7× per-unit advantage is consistent with why both companies sustain large in-house silicon programs, though the dataset does not measure their NRE or full program economics. The comparison is also not fully like-for-like: custom-chip figures estimate payments to supply partners, while merchant-chip figures estimate average end-customer purchase prices; both exclude server- and facility-level costs. And per §1.2, the comparison is on peak compute only — it assigns no value to the larger HBM stacks Nvidia chips typically carry, so it overstates the in-house advantage on memory-bound workloads.

## 5.2 The gross chip-cost counterfactual

Repricing the Q4 2025 in-house fleets (Google TPU 3.80M H100e; Amazon Trainium2 0.92M H100e) at merchant rates, as a **gross chip-cost-only counterfactual assuming full H100e substitution** (it does not reflect memory, networking, software, or real-world performance):

| Scenario | Google | Amazon | Total |
|---|---:|---:|---:|
| Actual estimated chip cost | ~$25.0B | ~$5.6B | ~$30.6B |
| At B200 pricing (~$14,645/H100e) | ~$55.7B | ~$13.5B | ~$69.2B |
| At H100/H200 pricing ($25,000/H100e) | ~$95.1B | ~$23.0B | ~$118.1B |
| **Chip-cost counterfactual (vs B200 / vs Hopper)** | **~$31B / ~$70B** | **~$8B / ~$17B** | **~$39B / ~$88B** |

## 5.3 The share consequence

All four hyperscalers roughly tripled their fleets in 2025, but the industry grew ~3.1× — so each owner's share moved with whether it compounded faster or slower than that benchmark. What separated the two pairs around it was compute per estimated dollar on the margin:

| Owner | H100e share Q4 2024 | H100e share Q4 2025 | Δ (pp) |
|---|---:|---:|---:|
| Google | 21.18% | 25.07% | **+3.88** |
| Amazon | 10.19% | 11.66% | +1.47 |
| Meta | 11.87% | 11.44% | −0.44 |
| Microsoft | 18.97% | 16.97% | **−2.01** |
| **Integrated pair (Google + Amazon)** | **31.37%** | **36.73%** | **+5.36** |
| **Merchant pair (Microsoft + Meta)** | **30.85%** | **28.40%** | **−2.44** |

*Note: Pair rows are computed from unrounded data; components may not sum exactly to pair rows.*

The integrated pair moved from roughly tied with the merchant pair to ~8.3pp ahead. The divergence is driven by capacity per estimated dollar, not by cost intensity — the demand-side mirror of the supplier-side asymmetry in §3.1.

## 5.4 Why Microsoft and Meta lack the same lever

Three plausible reasons, offered as interpretation rather than dataset findings: time-to-volume (Google began TPU production in 2015 and Amazon shipped Trainium1 in 2022, while Maia and MTIA do not yet appear in Epoch's tracked volume data); workload concentration (Google's Search, YouTube, and Gemini each independently amortize a custom chip, whereas Microsoft's tracked fleet remains heavily Nvidia-weighted — the dataset does not identify workload-level or contractual causes); and market positioning (AWS sells Trainium2 externally as a cheaper alternative, a route Microsoft has not taken at tracked scale).

---

# 6. First Read on 2026: Nvidia versus Google in Q1

## 6.1 Basis and coverage

This section uses **quarterly shipment flows** from the AI Chip Sales data, not cumulative stock. Q1 2026 coverage is provisional and includes only Nvidia and Google, so no industry-wide share can be computed. All shares here are two-player shares (Google ÷ [Google + Nvidia]) — defensible because Nvidia versus Google TPU was the principal axis of the 2025 erosion in §3.1 (TPU's +4.4pp was the largest single-supplier compute-share gain of the year); the second axis, Huawei, has no 2026 data yet and is therefore invisible to this section.

## 6.2 The quarterly flow record

| Quarter | Nvidia H100e (M) | Google H100e (M) | Google 2-player share | Nvidia $/H100e | Google $/H100e |
|---|---:|---:|---:|---:|---:|
| Q1 2025 | 1.70 | 0.44 | 20.6% | 18,741 | 5,648 |
| Q2 2025 | 1.90 | 0.63 | 25.0% | 17,362 | 4,579 |
| Q3 2025 | 2.37 | 0.80 | **25.3%** | 16,637 | 4,474 |
| Q4 2025 | 2.96 | 0.83 | 21.9% | 16,237 | 4,741 |
| **Q1 2026** | **3.39** | **0.85** | **20.0%** | 16,404 | 4,931 |

## 6.3 Nvidia re-accelerated — and went all-Blackwell

Nvidia shipped 3.39M H100e in Q1 2026, up 14.5% QoQ and ~99% YoY, worth ~$55.5B — its largest quarterly flow on record. The two-supplier Q1 2026 flow alone (4.24M H100e) nearly matches the aggregate Q4 2025 flow across the five price-covered suppliers analyzed in this report (4.37M). The mix completed a generational turn: Q1 2026 is Nvidia's first quarter with **zero Hopper shipments**. B300 supplied 74% of Nvidia's compute flow (992,874 units), with B200 the remaining 26%. Note that on the H100e metric the B300 registers only marginally above the B200 and Google's TPU v7, because H100e counts peak throughput alone; the B300's substantially larger HBM stack — its principal upgrade — is invisible to this metric (§1.2), so the flow figures understate the effective capability Nvidia shipped.

## 6.4 Google's flow stalled — inside a generational handoff

Google shipped 0.85M H100e, up just 2.1% QoQ (still +92% YoY). The flat headline conceals a mix rotation: TPU v7 (Ironwood) units ramped 51k → 198k → 306k (+55% QoQ) and now carry 84% of Google's compute flow, but v6e shipments collapsed from 397k units to 144k (−64%), and the v7 ramp only just offset the rundown. Because v7 costs more per H100e than v6e, Google's blended flow cost drifted up for two consecutive quarters.

## 6.5 The share inflection

Google's share of the two-player compute flow peaked at 25.3% in Q3 2025 and has since declined for two consecutive quarters, to 21.9% and now 20.0%. A supplier's cumulative share rises only while its flow share exceeds its cumulative share. In Q1 2026 Google's flow share (20.0%) fell below its cumulative two-player share for the first time, and **Google's cumulative two-player compute share ticked down — the first decline in the dataset's history.** (Cumulative two-player shares in this section are obtained by cumulating the shipment dataset itself; owner-snapshot stock shares from §3–5 reconcile with it only to within ~1% (§1.3) and, because the crossover margin is smaller than that tolerance, are not mixed into this comparison.)

What did *not* change: the estimated unit-cost wedge is intact at ~3.3× ($16,404 vs $4,931 per H100e on the flow), and TPU's power efficiency lead persists — Google's Q1 2026 shipments deliver ~2.43 H100e per kW of chip TDP against Nvidia's ~1.87. Nvidia's single-quarter flow embodied ~1.81 GW of aggregate chip-level nameplate TDP against Google's ~0.35 GW (nameplate TDP of shipped chips, not actual power demand). Q1 2026 challenges the *volume trajectory* of the TPU thesis, not its economics.

## 6.6 Two readings, and what would falsify each

**The Nvidia-momentum reading.** Blackwell demand genuinely re-accelerated; B300's full-volume quarter is a step function TPU could not match. On this reading, the 2025 erosion reflected a Hopper-era interregnum that Blackwell has closed.

**The transition-trough reading.** Google's flow is gated by the v6e→v7 handoff, not demand: v7 unit growth of +55% QoQ is among the steepest ramps in the dataset, and external reporting suggests TPU supply may be allocation-constrained at the packaging/HBM level — though the Epoch dataset itself cannot confirm this. On this reading, Q1 2026 is a trough, not a trend break.

The falsification criteria are observable within two quarters. If Google's two-player compute flow share remains below its cumulative share (~21%) through Q3 2026, the transition-trough reading fails and the TPU component of the §3.1 erosion thesis needs downward revision. If the v7 ramp pushes flow share back above 25% by Q3 2026 — its 2025 peak — the momentum reading fails and the 2025 trajectory resumes. An intermediate outcome, flow share between ~21% and 25%, would resume slow cumulative-share gains without restoring the 2025 pace: directional support for the transition-trough reading, but at a magnitude that would still warrant trimming the erosion thesis. Independently, if Huawei's Q1 2026 figures (once published) extend its 2025 trajectory, Nvidia's *industry-wide* share can keep eroding from the geopolitical side even in quarters where it out-ships Google.

---

# 7. Strategic Implications

**1. Nvidia's stock-share erosion paused on one front; the other is unmeasured.** The 2025 record — −4.3pp compute share, −2.5pp cost share despite a record revenue year — established a structural erosion driven by TPU and Huawei. Q1 2026 shows the TPU front stalling in a generational transition while Blackwell re-accelerated; the Huawei front is not yet observable in 2026 data. Because cumulative share converges toward flow share, further erosion requires only that Nvidia's forward flow share sit below its cumulative share — as it did industry-wide in 2025 (~65% of net compute additions against a 71% opening stock share) but did not on the two-player axis in Q1 2026. The v7 ramp trajectory (§6.6) is the swing variable.

**2. The vertical-integration wedge is the decade's dominant capex fact regardless of quarterly noise.** A 2.4–5.7× per-unit estimated-cost gap, ~$39–88B of gross chip-cost counterfactual, and a 7.8pp one-year relative swing between integrated and merchant-dependent hyperscalers make in-house silicon one of the industry's most consequential chip-cost programs — although the dataset does not measure full-stack returns. Q1 2026 confirmed the wedge at ~3.3× on flow pricing.

**3. Microsoft's Hopper base is a large repricing exposure.** With Hopper flow now at zero and marginal capacity priced well below its installed basis, Microsoft faces a capex treadmill that Maia's absence from volume data leaves unhedged. The same logic applies with more leverage to CoreWeave (100% Nvidia, no in-house exit). These are scenario observations from chip-cost data only; a full assessment would require financial statements, debt maturities, GPU useful-life, and lease terms.

**4. AMD's ceiling is a customer-structure problem, not a product problem.** MI300X is one of the cheapest large-volume merchant accelerators available, yet AMD lost compute share in 2025 because it lacks a second hyperscaler anchor approaching Meta's scale. Its path runs through the "Other" cohort and sovereign demand.

**5. China's substitution is past the tipping point.** Huawei's move from ~36% to ~63% of China's price-covered cumulative compute in one year means the Chinese market is functionally lost to U.S. merchant silicon on the margin — while the descriptive ~2.7× per-H100e cost gap remains China's structural handicap.

**6. Power is becoming a binding constraint the H100e metric does not price.** Nvidia's Q1 2026 flow alone embodied ~1.81 GW of aggregate chip-level nameplate TDP — before networking, cooling, and facilities. Google's ~30% compute-per-watt advantage compounds the cost wedge with a siting wedge that grows more valuable as grid interconnection replaces silicon as the bottleneck.

---

# Appendix A — Data Definitions and Caveats

**Stock (§2–5).** Cumulative delivered/allocated compute per owner from Epoch AI's AI Chip Owners data (May 2026 snapshot). Estimated chip cost applies a single per-chip cost per chip type (from AI Chip Sales cost estimates) to owner unit counts. Chip types without a cost estimate (Trainium1, Cambricon Siyuan 590; together 0.6% of Q4 2025 H100e) are excluded from every quantitative calculation — compute, shares, growth, flows, and cost alike — and appear only as qualitative context. Epoch cautions against using ownership data for financial-asset analysis.

**Flow (§6).** Quarterly shipment volumes from AI Chip Sales data (July 2026 snapshot); per-quarter flows, not running totals.

**H100e** normalizes peak dense 8-bit throughput to the H100's; it does not capture HBM memory capacity, memory bandwidth, interconnect, or software efficiency (see §1.2 for why this systematically understates Nvidia's effective position on memory-bound workloads).

**Cost** is estimated chip purchase cost, not full-system TCO. Unit-count and H100e estimates generally include 90% intervals (typically ~2×); chip-cost estimates do not. Counterfactuals are gross chip-cost only.

**Coverage.** Ownership ≠ usage. "Other" is a residual. Q1 2026 figures are provisional and cover Nvidia and Google only.

---

# References

1. Epoch AI (2026). *Data on AI Chip Sales.* Published online at epoch.ai. Retrieved from https://epoch.ai/data/ai-chip-sales [AI Chip Sales, July 2026 snapshot; accessed July 2026].
2. Epoch AI (2026). *Data on AI Chip Owners.* Published online at epoch.ai. Retrieved from https://epoch.ai/data/ai-chip-owners [AI Chip Owners, May 2026 snapshot; accessed July 2026].
3. Epoch AI. *About Epoch AI.* https://epoch.ai/about
4. Epoch AI. *Transparency.* https://epoch.ai/about/transparency [accessed July 2026]
5. Coefficient Giving (2025). *Press Release: Open Philanthropy Becomes Coefficient Giving.* https://coefficientgiving.org/research/press-release-open-philanthropy-becomes-coefficient-giving-expanding-work-with-multiple-donors/
6. Visual Capitalist (2026). *Companies That Sell the Most AI Chips.* (visualization of Epoch AI chip-sales data)

All Epoch AI data is licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

*Disclosure (per Ref. 4, accessed July 2026): Epoch discloses funding and contractual relationships with AI-affected organizations including large AI companies (e.g., Google), and partnered with OpenAI on FrontierMath; its principal funder, formerly Open Philanthropy, was renamed Coefficient Giving in November 2025 (Ref. 5).*

