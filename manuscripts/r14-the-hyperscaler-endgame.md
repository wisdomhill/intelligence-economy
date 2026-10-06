---
title: "14. The Hyperscaler Endgame"
subtitle: "Who inherits the inversion: a two-axis analysis of silicon and capital procurement"
series: "The Intelligence Economy"
number: 14
manuscript-revision: 1
date: 2026-10-06
date-modified: 2026-10-06
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  Who inherits the inversion. Hyperscalers graded on two axes — what a unit
  of compute costs them to buy, and what it costs them to finance — and the
  finding that the first varies by multiples and the second by basis points.

keywords:
  - hyperscaler
  - user cost of capital
  - vertical integration
  - balance-sheet headroom
  - H100-equivalent
  - neocloud

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
#
# Like Reports 7 to 11 and 13, the Executive Summary is numbered section 1 and
# the cross-references depend on it, so the numbering is kept.
#
# This manuscript is the only one with unnumbered chapters ahead of the
# summary — Preface, Scope and Thesis, Data Sources and Attribution. All
# three are front matter in character, so the web edition carries them on the
# cover page with the summary rather than as three short chapter pages. The
# PDF keeps them as chapters, in the author's order.
published:
  dir: reports/r14/
  pdf: r14-the-hyperscaler-endgame.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r14/

cover:
  - manuscript: "Preface: From the Inversion to Its Inheritors"
    fragment:   _00-preface.qmd
  - manuscript: "Scope and Thesis"
    fragment:   _01-scope.qmd
  - manuscript: "Data Sources and Attribution"
    fragment:   _02-data-sources.qmd
  - manuscript: "1. Executive Summary"
    fragment:   _03-executive-summary.qmd

chapters:
  - manuscript: "2. Framework: From the Hyperscaler Trilemma to a Two-Axis Model"
    published:  "2. Framework"
    fragment:   _04-framework.qmd
    page:       01-framework.qmd
  - manuscript: "3. Axis I — Silicon Procurement: The Empirical Cost of Compute"
    published:  "3. Axis I: Silicon Procurement"
    fragment:   _05-silicon.qmd
    page:       02-silicon.qmd
  - manuscript: "4. Axis II — Capital Procurement: The Price of Money and the Capacity to Raise It"
    published:  "4. Axis II: Capital Procurement"
    fragment:   _06-capital.qmd
    page:       03-capital.qmd
  - manuscript: "5. Integration — The Fully-Loaded Cost per H100-Equivalent"
    published:  "5. The Fully-Loaded Cost"
    fragment:   _07-integration.qmd
    page:       04-integration.qmd
  - manuscript: "6. Competitive Positioning: The Unit-Cost × Financing-Capacity Matrix"
    published:  "6. Competitive Positioning"
    fragment:   _08-positioning.qmd
    page:       05-positioning.qmd
  - manuscript: "7. Falsification Criteria and Open Questions"
    published:  "7. Falsification Criteria"
    fragment:   _09-falsification.qmd
    page:       06-falsification.qmd
  - manuscript: "8. Strategic Implications"
    published:  "8. Strategic Implications"
    fragment:   _10-implications.qmd
    page:       07-implications.qmd
  - manuscript: "Appendix A — Data Definitions and Bridging Assumptions"
    published:  "Appendix A"
    fragment:   _11-appendix-a.qmd
    page:       08-appendix-a.qmd
  - manuscript: "Appendix B — Owner-Level Input Table (central case)"
    published:  "Appendix B"
    fragment:   _12-appendix-b.qmd
    page:       09-appendix-b.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _13-references.qmd
    page:       10-references.qmd
---
# The Hyperscaler Endgame

### Who Inherits the Inversion: A Two-Axis Analysis of Silicon and Capital Procurement

*The Intelligence Economy — Report 14 of 14*  
*Wisdom Hill Research | Thematic Research | July 2026*

---

# Preface: From the Inversion to Its Inheritors

Report 13 of this series argued that the market has the AI hardware cycle backwards in time. The prevailing narrative celebrates semiconductor suppliers — memory makers above all — as the structural winners of the AI buildout, rent collectors at today's bottleneck, while treating hyperscale datacenter operators as capital-consuming machines whose free cash flow compresses with every quarter of accelerating capex. Equity markets price accordingly: enthusiasm concentrates on the chip complex, and skepticism on the firms writing the checks. Report 13's three frameworks showed why that reading accurately describes the present and is therefore a poor guide to the future. Semiconductor demand is a derivative of end demand, and turns while end demand still sets records. The binding constraint migrates downstream, from self-resolving fab capacity toward self-intensifying datacenter inputs, and economic rent migrates with it. And the datacenter capex race is a war of attrition whose equilibrium is exit in order of capital cost — a process that consolidates the industry around its strongest balance sheets, which then inherit the scarce asset at the moment it becomes the bottleneck.

That argument was deliberately left at the industry level, and it left open the one question on which its investment translation entirely depends. If the attrition war concentrates durable market power in the survivors, **which operators survive, in what order do the others fold, and how large are the gaps between them?** Report 13 specified the exit rule — participants leave in order of capital cost and staying power — but measured neither variable at the firm level. A war of attrition has exactly two firm-level parameters: the size of the ante each player must post per unit of capacity, and the durability of the funding that posts it.

This final report of the series measures both. The ante per unit is the fully-loaded annual cost of operating one H100-equivalent of compute, which Section 5 constructs owner by owner from a user-cost-of-capital identity. The durability of funding is financing capacity — the price of each owner's capital and, more importantly, the quantity of it that can be raised without eroding the credit standing that sets the price — which Section 4 assesses across four sub-dimensions. Together they answer the question Report 13 posed: **among the firms deploying capital into the intelligence economy's infrastructure, who acquires a unit of compute most cheaply, who can keep acquiring it the longest, and how large is the gap between them?**

---

# Scope and Thesis

Hyperscalers face what has become known as a trilemma: securing accelerator silicon, securing power and data-center sites, and securing the capital to pay for both. This report holds the second constraint constant, and the reason follows directly from Report 13's architecture. Power and site scarcity is the *industry-level* term of the min-function — the self-intensifying constraint that determines *when* the bottleneck crosses downstream and therefore when the survivor's premium activates (the explicit condition on which Report 13's Section 7.2 made the market-power thesis contingent). But it binds all large buyers in broadly similar ways: the same interconnection queues, the same turbine backlogs, the same permitting frictions. It sets the ceiling on the race; it does not rank the racers. The two constraints on which firms genuinely diverge — and which therefore decide the attrition ordering — are **the cost at which silicon is procured (Axis I)** and **the cost and capacity at which capital is procured (Axis II)**.

The central claim of this report is that these two axes combine multiplicatively into a single economic quantity — the annualized, fully-loaded cost of operating one H100-equivalent (H100e) of compute — and that when the combination is actually performed, the two axes turn out to play **asymmetric roles**. The silicon axis moves the fully-loaded unit cost in *multiples*; within the investment-grade cohort, the capital axis moves it in *basis points*. The capital axis instead exerts its force on a different margin entirely: not on the cost of the installed stock, but on the **sustainable velocity of net additions** — the financial capacity to keep adding capacity at all. In the vocabulary of Report 13, Axis I prices the ante and Axis II measures the staying power; the attrition equilibrium is decided by both, and one firm, and only one, currently leads on both.

The analysis covers the four major U.S. hyperscalers (Google, Microsoft, Amazon, Meta), Oracle, and the U.S. neocloud cohort (CoreWeave, xAI).

---

# Data Sources and Attribution

All H100-equivalent capacity figures and deployed-cost estimates in this report derive from **Wisdom Hill's own analysis of data downloaded from Epoch AI's public databases** — the *AI Chip Sales* datahub and the companion *AI Chip Owners* explorer (epoch.ai, licensed CC BY). We downloaded the underlying chart data (H100e and Cost Estimate series, by owner and by chip supplier, quarterly) and performed the stock/flow decomposition, share calculations, unit-cost derivations, and counter-factual estimates presented here ourselves. Epoch AI's figures are best-effort median estimates — anchored in vendor earnings disclosures and analyst reconstructions — of chips *delivered to and owner-attributed for* each operator, not of capacity independently verified as installed and online; confidence intervals typically span roughly a factor of two, and minor revisions to the source data should be expected over time. Accordingly, this report's conclusions are framed at the level of **rankings, gap multiples, and structural direction** rather than precise dollar figures. Where we describe the resulting ordering as robust, we mean robust under the report's normalization and central assumptions to revisions of the magnitude Epoch itself indicates — a well-supported central scenario, not a claim that the exact ordering survives every possible joint or platform-specific error.

All capital-market, credit, and financial-statement facts are drawn from SEC filings, rating-agency actions, and financial press coverage, cited individually in the References.

---

# 1. Executive Summary

Report 13 established that the datacenter capex race is a war of attrition whose survivors inherit durable market power, and that exit proceeds in order of capital cost and staying power. This report measures those two variables — the fully-loaded unit cost of compute and the capacity to finance its expansion — for every major U.S. owner, and ranks the field.

- **The framework.** The annualized cost of operating one H100e is approximated by a user-cost-of-capital identity: UC = δ_chip·P + δ_infra·K + r·(P + K), where P is the owner's chip acquisition cost per H100e (measured from the Epoch-derived dataset), K is non-chip infrastructure capex per H100e (assumed uniform across owners), r is the owner's after-tax marginal cost of capital, and δ is the economic depreciation rate of each asset class. Silicon procurement determines P; capital procurement determines r; technology cadence determines δ.
- **Axis I is measured, and the gap is a multiple.** At Q4 2025, cumulative blended chip cost per H100e ranges from **$9,714 (Google)** to **$18,666 (Microsoft)** among the Big Four — a **1.92×** spread produced almost entirely by in-house silicon. Google's TPU fleet carries a per-H100e cost 2.9–5.7× below merchant Nvidia pricing; Amazon's Trainium 2.4–4.1× below. Nvidia's ~75% gross margin is the arithmetic source of the wedge.
- **Axis II prices in basis points — but rations in dollars.** Rough after-tax marginal funding costs across the Big Four span only ~30–40bp (Microsoft ~3.6% to Meta ~4.0%). Inserted into the user-cost identity, that spread moves the fully-loaded unit cost by ~1–2%. The silicon spread moves it by ~30–60%. Within investment grade, the price of capital is a second-order variable. Outside investment grade (neoclouds at ~8–10%), it becomes first-order again.
- **The fully-loaded leaderboard.** Under central assumptions (chip share of capex 55%, chip δ 30%, infrastructure δ 10%), the approximate annualized user cost per H100e is: **Google ~$5,000 < Amazon ~$6,400 < Meta ~$7,600 < Oracle ~$7,900 ≈ Microsoft ~$8,000 < xAI ~$9,600 < CoreWeave ~$9,900**. Google's chip-level 1.92× advantage over Microsoft dilutes to roughly **1.6×** on a fully-loaded basis once uniform non-chip infrastructure is added — a decisive gap that holds at 1.55–1.63× across the plausible assumption range under the report's central inputs.
- **The real function of Axis II is capacity, not price.** The 2025–2026 funding-model inflection — hyperscaler bond issuance of ~$121B in 2025, roughly four times the prior five-year average, with Morgan Stanley projecting ~$400B of hyperscaler borrowing in 2026 — shifted the binding constraint from the income statement to the balance sheet. On that margin the cohort diverges sharply: Amazon enters the cycle with ~$170B of debt and lease obligations and a free cash flow that has collapsed to roughly break-even, while Alphabet demonstrated access to every layer of the capital structure in a single half-year (an equity capital program of up to ~$85B, ~$45B of it raised at announcement, and the technology sector's first century bond since 1997).
- **Composite verdict.** Google is the only owner graded A-tier on both axes. Microsoft pairs the strongest financing profile (AAA/Aaa, net cash, off-balance-sheet fund structures) with the weakest silicon position among the Big Four — and carries a distinct counterparty-concentration risk through its 27% OpenAI stake and OpenAI's $250B Azure purchase commitment, a circular structure in which Azure's growth, Microsoft's equity value, and OpenAI's solvency are mutually referencing. Amazon pairs the second-best silicon position with the most constrained balance sheet in the Big Four — a constraint that originates not in its AI strategy but in the structural capital intensity of its e-commerce and logistics business. Meta occupies the middle of both axes. Oracle and the neoclouds are disadvantaged on both simultaneously.

---

# 2. Framework: From the Hyperscaler Trilemma to a Two-Axis Model

## 2.1 Why power is held constant

Power and site scarcity is real, binding, and — for the purpose of ranking firms — largely undifferentiating. All large buyers bid in the same interconnection queues, face the same multi-year substation and turbine lead times, and increasingly co-locate behind the same utility constraints. Differences of execution exist, but they are second-order relative to the two constraints this report isolates, and they lack the firm-level, decade-long structural character of silicon design ownership or balance-sheet composition. We therefore treat power as a common industry ceiling on aggregate build-out pace, not as a competitive axis.

The division of labor with Report 13 is exact. There, the datacenter absorption flow A_DC — throttled by power, sites, and grid access — is the industry-level curve whose crossing with fab output defines the regime change; its trajectory determines *when* rent migrates downstream and how valuable the survivors' energized capacity becomes. Here, conditional on that common trajectory, we ask which owners reach the crossing in the strongest position. The one channel through which the power constraint does differentiate firms is capital: Report 13 noted that A_DC is a function of capital-market conditions as well as physical inputs, and at the firm level the capital-market term is precisely Axis II. An owner's share of the industry's constrained absorption capacity is, at the margin, purchased with balance-sheet headroom.

## 2.2 The user-cost formulation

The economics of holding a capital asset are summarized by the user cost of capital in the tradition of Jorgenson (1963): the annualized cost of one unit of capital equals its price multiplied by the sum of the financing rate and the depreciation rate. Applied per H100-equivalent and separated by asset class:

> **UC_i = δ_chip · P_i + δ_infra · K + r_i · (P_i + K)**

where, for owner *i*:

- **P_i** — the blended chip acquisition cost per H100e of the installed fleet. This is the empirical heart of the report: it is measured directly, owner by owner, from our analysis of the Epoch AI datasets (Section 3).
- **K** — non-chip infrastructure capex per H100e (data-center shell, power and cooling systems, non-accelerator IT). Assumed uniform across owners (Declaration 2 below) and derived from the chip-share-of-capex assumption (Declaration 1).
- **r_i** — the owner's after-tax marginal cost of capital, estimated roughly from credit ratings and observed issuance (Section 4).
- **δ_chip, δ_infra** — economic depreciation rates by asset class, estimated deliberately roughly (Section 5.1).

The identity makes the report's structure transparent: Section 3 measures P_i, Section 4 estimates r_i and — more importantly — the *quantity* dimension of capital that the identity does not capture, Section 5 assembles the pieces, and Section 6 converts the result into a competitive verdict.

## 2.3 Stock versus flow

Following the stock/flow discipline established in Report 13 — where the distinction carried the entire accelerator argument, semiconductor revenue being the flow that serves the datacenter stock — we distinguish throughout between the **cumulative installed base** (the stock: what a fleet cost to build and what it costs annually to hold) and **net additions** (the flow: what is being added each quarter and how it is being paid for). The δ·K replacement term of Report 13's derived-demand identity reappears here from the buyer's side: the economic depreciation rate estimated in Section 5.1 is simultaneously the floor under the chip industry's future revenue and the recurring charge inside every hyperscaler's user cost. The two axes map onto this distinction asymmetrically. Axis I governs the unit economics of both stock and flow — a cheap chip is cheap on the day of purchase and every day thereafter. Axis II barely differentiates the unit economics of the stock (Section 5.4) but decisively governs the *sustainability of the flow*: when capex outruns operating cash flow, the ability to keep adding capacity is rationed by balance-sheet headroom, not by a few basis points of coupon.

## 2.4 Methodological declarations and confidence grading

The following assumptions are declared explicitly. Each input in this report carries a confidence grade: **[A]** measured/disclosed, **[B]** reconstructed from disclosed data, **[C]** judgment-based estimate.

1. **Chip share of AI capex: 55% (range 50–60%). [C]** Accelerator silicon is assumed to constitute 55% of total AI data-center capex, with the remaining 45% comprising shell, power and cooling infrastructure, and non-accelerator IT (CPUs, memory, storage, networking).
2. **Non-chip cost parity. [C]** All owners are assumed to procure non-chip infrastructure at identical cost per H100e. Networking topologies, power-purchase terms, and construction efficiency differ in practice, but not with the persistence or magnitude of the silicon wedge. Under this assumption, all inter-owner differences in fully-loaded cost originate in chip procurement and capital procurement — which is precisely the isolation the two-axis framework requires.
3. **In-house silicon valued at manufacturing cost; design cost ignored. [C]** For internally designed chips (Google TPU, Amazon Trainium), cost reflects manufacturing/supplier-revenue economics (e.g., Broadcom's revenue from Google for TPU production). This is the correct economic basis: the relevant question is what a unit of in-house compute costs its owner to obtain. Design and NRE expenditures are real but, amortized over multi-million-unit deployment volumes, are not a large share of per-unit economics; we declare them ignored rather than pretending to estimate them.
4. **Nvidia margin stated as ~75%. [A]** Nvidia's GAAP gross margin was 73.4% in FY2026 Q3 (quarter ended October 2025), with guidance around the mid-70s; we describe the normalized data-center margin as approximately 75% throughout.
5. **Depreciation estimated roughly. [C]** Given the depth of uncertainty about the pace of technology development, δ is estimated to first-order precision only (Section 5.1). Because the same δ applies to every owner, rankings are invariant to this parameter; only levels move.
6. **Cost of capital estimated roughly. [C]** r_i is approximated from rating tiers and observed issuance yields; no full WACC construction is attempted, since Section 5.4 shows the identity is insensitive to refinements of this input within investment grade.
7. **Source-data revision tolerance.** The underlying chip-cost dataset is subject to minor future revision. All conclusions are therefore stated at the level of rankings, multiples, and direction.
8. **Geographic scope.** The analysis covers U.S.-headquartered hyperscalers and neoclouds.

---

# 3. Axis I — Silicon Procurement: The Empirical Cost of Compute

## 3.1 The Nvidia margin structure and what buyers actually pay

The arithmetic origin of the silicon axis is a single disclosed number: Nvidia sells data-center accelerators at a gross margin of approximately 75% (GAAP 73.4% in FY2026 Q3, on data-center revenue of $51.2B in that quarter alone) [A]. A buyer of merchant Nvidia silicon therefore pays roughly four dollars for every dollar of manufacturing cost embedded in the device. A buyer that designs its own accelerator and pays only the foundry-and-packaging supply chain acquires the same silicon content at cost. This margin — colloquially, the "Nvidia tax" — is not a grievance but a price for genuine value: CUDA, networking integration, and the fastest architecture cadence in the industry. The question this report asks is not whether the margin is justified but what it does to the relative cost positions of buyers who pay it and buyers who do not.

The dataset answers precisely. At Q4 2025, per-H100e acquisition cost by chip platform (cumulative delivered/owner-attributed base) [B, Wisdom Hill analysis of Epoch AI data]:

| Platform | $/H100e (cumulative) | Note |
|---|---:|---|
| Nvidia H100/H200 | $25,000 | Hopper-era merchant benchmark |
| Nvidia B300 | $17,024 | Blackwell Ultra, ramping |
| Nvidia B200 | $14,658 | Blackwell volume SKU |
| AMD MI300X | $9,460 | Cheapest large-volume merchant part |
| Amazon Trainium2 | $6,094 | In-house, manufacturing-cost basis |
| Google TPU v7 (Ironwood) | $5,147 | In-house, manufacturing-cost basis |
| Google TPU v6e (Trillium) | $4,419 | The lowest-cost volume platform in the dataset |

TPU v6e at $4,419 per H100e is 5.7× cheaper than the Hopper benchmark and 3.3× cheaper than B200. Trainium2 sits at 4.1× below Hopper and 2.4× below B200. AMD's MI300X, at roughly 62% below Hopper pricing, defines an intermediate path available without vertical integration.

## 3.2 The owner-level $/H100e leaderboard

Chip platform economics translate into owner economics through fleet mix. At Q4 2025, the cumulative installed base by owner [B]:

| Owner | Installed H100e (M) | Installed cost ($B) | $/H100e blended | H100e per $B |
|---|---:|---:|---:|---:|
| Google | 5.03 | 48.9 | **$9,714** | 102,941 |
| Amazon | 2.44 | 33.5 | **$13,765** | 72,647 |
| Meta | 2.30 | 39.7 | **$17,296** | 57,818 |
| Oracle | 1.14 | 20.1 | **$17,597** | 56,829 |
| xAI | 0.55 | 10.2 | **$18,509** | 54,028 |
| Microsoft | 3.41 | 63.6 | **$18,666** | 53,573 |
| CoreWeave | 0.83 | 15.9 | **$19,161** | 52,189 |

*Installed-cost dollars are rounded to $0.1B for display; $/H100e and H100e-per-$B are computed from unrounded source data, so ratios of the rounded columns may differ in the final digits.*

Google operates the largest fleet by compute (5.03M H100e) while ranking only third by dollars deployed — it extracts 1.92× the compute per cumulative dollar that Microsoft does. Microsoft is the mirror image: the largest dollar deployment ($63.6B) purchasing the second-smallest compute-per-dollar in the cohort. The gap between the two is the silicon axis rendered as a single number.

The flow tells the same story more sharply. On 2025 net additions, Google added 3.65M H100e at $7,384 per H100e — roughly half the industry-average cost of incremental capacity — because 78.2% of its additions came from in-house silicon (TPU v6e and v7). Microsoft added 2.17M H100e at $16,063. Amazon's additions split visibly along its dual-platform strategy: +0.97M H100e from Nvidia at $16,524, +0.71M from Trainium at $6,094.

## 3.3 The vertical-integration wedge, counter-factually

The cleanest measure of what design ownership is worth is the counter-factual: what would the in-house fleets have cost at merchant prices? Applied to the Q4 2025 cumulative in-house installed bases [B]:

| Scenario | Google (3.80M TPU H100e) | Amazon (1.01M Trainium H100e) | Combined |
|---|---:|---:|---:|
| Actual deployed cost | $25.1B | $6.5B | $31.6B |
| At B200 pricing ($14,658/H100e) | $55.7B | $14.8B | $70.5B |
| At H100/H200 pricing ($25,000/H100e) | $95.1B | $25.3B | $120.4B |
| **Capex avoided (vs. B200)** | **$30.6B** | **$8.3B** | **$38.9B** |
| **Capex avoided (vs. H100/H200)** | **$70.0B** | **$18.8B** | **$88.8B** |

Even against the conservative Blackwell benchmark, the two in-house programs have avoided roughly $39B of merchant spend through Q4 2025; against the Hopper prices that actually prevailed during most of the accumulation period, roughly $89B. Returns of this magnitude make multi-billion-dollar annual silicon-design programs straightforwardly rational — and consistent with Declaration 3, they dwarf any plausible estimate of cumulative design cost.

A second, subtler finding strengthens the durability case. During 2025, Google TPU's share of industry-wide installed H100e rose +4.53pp while its share of industry-wide installed *dollars* fell −0.19pp — the in-house platform is gaining capacity share while getting cheaper per unit faster than the industry blend, as v6e/v7 economics compound through the fleet mix. No merchant platform in the dataset exhibits this signature.

## 3.4 The intermediate route: AMD without vertical integration

Meta demonstrates that a meaningful fraction of the wedge is capturable without designing silicon. AMD accounts for 19.9% of Meta's installed H100e at only 11.4% of its installed cost, and Meta's blended $17,296/H100e undercuts Microsoft's $18,666 despite Meta possessing no at-scale in-house silicon in the dataset. MI300X pricing (~$9,460/H100e) sits between the in-house platforms and merchant Nvidia; a buyer with the software capacity to operate ROCm at scale — Meta's open Llama serving stack being the natural case — can harvest part of the discount. The route is real but bounded: it lowers P by thousands of dollars per H100e, not by the 2.9–5.7× multiples available to designers.

## 3.5 Share dynamics as validation

If the silicon axis is economically decisive, it should be visible in market-share physics — and it is. During 2025, among the Big Four, the two vertically integrated owners gained installed-compute share while the two merchant-dependent owners lost it: Google +4.07pp and Amazon +0.60pp, against Meta −0.32pp and Microsoft −1.81pp. Combined, the integrated pair moved from 32.4% to 37.0% of industry H100e while the merchant pair fell from 30.4% to 28.3% — a 6.8pp relative swing in twelve months, achieved with only a +0.5pp swing in dollar share. The divergence is driven by capacity-per-dollar, not by dollars: all four owners roughly tripled their fleets, but the industry grew 3.06×, and only owners whose incremental dollar bought more compute than the blended market price gained ground. This is the demand-side mirror of the supplier-side fact that Nvidia's installed-base share declined on both compute and dollar metrics during 2025 despite capturing the large majority of the year's net spending.

---

# 4. Axis II — Capital Procurement: The Price of Money and the Capacity to Raise It

## 4.1 The funding-model inflection

For the first years of the AI build-out, hyperscaler capex was financed overwhelmingly from operating cash flow. That model has ended. During 2025, the largest hyperscalers issued approximately $121B of bonds — roughly four times the prior five-year average of about $28B per year — and the pace has accelerated sharply since: AI-related issuers had raised roughly $236B of debt by the end of May 2026, about four times the prior-year pace, with Morgan Stanley projecting hyperscaler borrowing of roughly $400B for 2026 and total AI-related issuance approaching $570B [A/B]. The proximate cause is the capex trajectory itself: combined 2026 capital-expenditure guidance across the Big Four reaches approximately $725B — Amazon around $200B, Microsoft tracking toward $190B, Alphabet $175–185B, Meta $125–145B — up roughly 77% from about $410B in 2025 [A].

When capex is internally funded, the capital axis is nearly invisible: money spent from retained cash flow carries no rating scrutiny and no covenant. When capex must be raised externally, two questions that previously did not bind become decisive: *at what price* can each firm raise, and — the question this section argues is the more important one — *how much* can each firm raise before its credit standing, and therefore its price, deteriorates. We treat these as the price dimension and the quantity dimension of Axis II.

## 4.2 The price of capital: ratings and rough marginal funding costs

The rating hierarchy, and the rough after-tax marginal debt cost it implies, is as follows. Marginal financing has shifted decisively toward bonds, so after-tax debt cost serves as the working proxy for the marginal cost of capital; no full WACC construction is attempted (Declaration 6).

| Owner | Rating (S&P / Moody's) | Pre-tax marginal yield (est.) | After-tax r_i (est.) | Confidence |
|---|---|---:|---:|---|
| Microsoft | AAA / Aaa | ~4.4% | **~3.6%** | C |
| Alphabet | AA+ / Aa2 | ~4.6% | **~3.8%** | C |
| Amazon | AA / A1 | ~4.7% | **~3.9%** | C |
| Meta | ~AA− tier | ~4.9% | **~4.0%** | C |
| Oracle | BBB / Baa2 | ~5.6% | **~4.6%** | C |
| CoreWeave, xAI | Sub-investment-grade / asset-backed | ~9–12% | **~8–10%** | C |

Two observations frame everything that follows. First, within the Big Four the entire after-tax spread is on the order of 30–40 basis points — Microsoft's AAA, one of only two among large U.S. corporates and now a notch above the U.S. sovereign itself following Moody's May 2025 downgrade of the United States to Aa1, buys it remarkably little in unit-cost terms (Section 5.4 quantifies how little). Second, the spread becomes structural at the tail: Oracle pays roughly 100bp over the leaders, and the neocloud cohort finances GPU fleets at roughly two to three times the investment-grade rate, frequently against the collateral value of the very hardware whose economic depreciation Section 5.1 estimates at ~30% per year.

**Alphabet's demonstrated market access deserves separate mention, because it upgraded during the period under review — qualitatively and visibly.** In November 2025 Alphabet raised $17.5B in a dollar offering that attracted roughly $90B in orders and included a 50-year tranche, the longest-dated dollar technology bond of that year. In February 2026 it returned with a $20B seven-part dollar offering — upsized from $15B against an order book exceeding $100B, among the largest ever recorded for a corporate bond, with the 40-year tranche compressing 25bp during bookbuilding to price near T+95 — alongside a £1B **100-year sterling century bond, the first century issuance by a technology company since Motorola in 1997**, itself nearly ten times oversubscribed, plus Swiss-franc and euro tranches bringing the week's total to roughly $31.5B. Then in June 2026 Alphabet announced a landmark **equity capital program of up to ~$85B** — approximately $18B of Class A and Class C common stock (upsized from $15B), $16.75B of 6.25% mandatory convertible preferred depositary shares (also upsized), and a $10B private placement, alongside a $40B at-the-market program not expected to commence before Q3 2026; the underwritten and privately placed portion (~$45B) was raised at announcement, with the ATM tranche a forward facility rather than proceeds already in hand [A]. Within eight months, in other words, Alphabet demonstrated jumbo-scale access to every layer of the capital structure — short debt, ultra-long debt in three currencies, hybrid convertible capital, and common equity — at pricing that treats it as long-duration infrastructure rather than cyclical technology. No other owner in this cohort has demonstrated capital access of comparable breadth, and the demonstration itself is information: the quantity dimension of Alphabet's Axis II position is now evidenced rather than assumed.

## 4.3 The quantity of capital I — internal generation

The first quantity sub-dimension is the trajectory of internally generated funding. Here the Big Four have diverged sharply. Alphabet's free cash flow remains positive though compressed — Q1 2026 FCF of $10.1B, down 47% year over year under the capex ramp [A]. Meta's cash generation remains robust in absolute terms but is being consumed at the highest capex-to-revenue ratio in the cohort (approaching the mid-30s in percent). Microsoft's operating cash flow remains enormous and its FCF positive.

Amazon is the outlier. Its trailing-twelve-month free cash flow collapsed from roughly $38B to $1.2B — a 95% decline — as capex accelerated, and sell-side projections for 2026 put Amazon's FCF meaningfully negative, on the order of −$17B (Morgan Stanley) to −$28B (BofA), with the company itself flagging the possibility of additional debt and equity issuance in its disclosures [A/B]. Amazon is thus the first of the Big Four to cross fully from self-funding into structural external dependence: every incremental H100e it adds is, at the margin, a financed H100e.

## 4.4 The quantity of capital II — balance-sheet headroom, and the structure of Amazon's constraint

The second quantity sub-dimension is the stock of existing obligations against which new debt must be layered. Including lease obligations — which for these firms are economically debt, funding fulfillment centers and data centers alike — the picture is starkly uneven [A/B]:

| Owner (FY2025 year-end) | On-balance-sheet borrowings | Lease liabilities (PV) | Total debt + leases | Net position |
|---|---:|---:|---:|---|
| Amazon | ~$68B ($65.6B long-term plus current portion) | **~$103B** | **~$170B** | Net debt (alone in cohort) |
| Meta | $58.7B | modest | ~$65B | Modest net cash |
| Microsoft | ~$45B | sizable (finance leases on data centers) | ~$90B | Large net cash |
| Alphabet | $46.5B | modest | ~$50B+ | **Largest net cash (~$95–100B)** |

*Snapshot as of FY2025 year-end; totals rounded [B]. Meta's borrowings had grown to approximately $84B by Q1 2026 (Section 4.5), eroding but not yet eliminating its net-cash position; the ordering of the table is unchanged at that date.*

Amazon's FY2025 10-K discloses gross lease liabilities of $121.8B ($103B at present value) — its lease book alone exceeds the total borrowings of any other Big Four member [A]. Layered on ~$68B of bonds, Amazon carries roughly $170B of debt-like obligations into a capex cycle it can no longer self-fund, and it is the only Big Four member in a net-debt position. The constraint is already visibly binding on the rating trajectory: Moody's, having moved Amazon's A1 outlook to positive in early 2025, returned it to stable in February 2026, citing the acceleration of capex [B]. An A1/AA credit does not lose market access at these levels — but each incremental $100B of issuance is layered onto the least headroom in the cohort, and headroom is precisely what a multi-year, externally financed capex race consumes.

**The origin of this constraint deserves careful statement, because the obvious narrative is wrong.** It is tempting to read Amazon-versus-Microsoft as a strategic trade-off — as if Amazon's willingness to invest capital in silicon bought its chip advantage at the price of a heavy balance sheet, while Microsoft's asset-light restraint bought its pristine credit at the price of merchant dependence. The data do not support that reading. In the cloud infrastructure business itself, the two firms have been symmetric, aggressive rivals for a decade, and in GPU procurement specifically Microsoft has been the *more* aggressive spender — it is the largest Nvidia customer in the dataset and the largest cumulative dollar deployer of AI compute. The divergence in enterprise-level capital intensity comes from everything *outside* the cloud: Microsoft's non-cloud portfolio is software — Office, Windows, gaming, LinkedIn — with negligible capital requirements, while Amazon's other core business is e-commerce, whose fulfillment and logistics network demands warehouse, vehicle, and facility investment on a scale that has filled its lease book for two decades. Amazon's Axis II constraint, in other words, is a **legacy of retail capital intensity, not a cost of its silicon strategy**; and Microsoft's Axis II strength is a property of its software-weighted portfolio, not a reward for eschewing custom chips. The two axes are causally independent — which is exactly why the framework treats them as separate axes.

## 4.5 The quantity of capital III — off-balance-sheet and not-yet-commenced commitments

The visible balance sheet understates the cohort's true forward obligations. Moody's has flagged that hyperscaler data-center lease commitments signed but not yet commenced — and therefore not yet on any balance sheet — total approximately $662B, a figure larger than the cohort's combined on-balance-sheet debt [B]. The distribution of this shadow book, and of adjacent structures, differentiates the owners:

Meta has moved furthest toward structured external finance: its on-balance-sheet debt roughly doubled during 2025 (from $29.5B to $58.7B, reaching approximately $84B by Q1 2026), and its ~$27B Hyperion data-center project — structured as a joint venture in which Blue Owl-managed funds hold 80% and Meta 20%, shifting the majority of the campus's funding off Meta's consolidated balance sheet rather than the full $27B — moves a large share of its single largest facility outside its own accounts, while multi-year cloud and equipment purchase commitments disclosed in its filings have expanded rapidly [A/B]. None of this is imprudent in isolation — but it means Meta's reported leverage understates its economic leverage more than any other Big Four member's.

Microsoft has used external structures in the opposite direction — defensively. Its participation in the ~$100B AI Infrastructure Partnership places large AI build-out exposure in a fund vehicle (levered at the fund level, not the corporate level), preserving the AAA balance sheet while retaining economic participation [B]. The structure is rating-protective rather than leverage-concealing, and it is part of why Microsoft's price-of-capital advantage is durable.

## 4.6 Counterparty concentration and circular revenue: the Microsoft–OpenAI structure

Report 13 identified circular dealmaking — suppliers taking equity stakes in customers, extending financing, participating in structures where investment returns as revenue — as the upstream's confession that its customers' capital constraint had become the system's weak point, converting income-statement exposure into balance-sheet exposure to the counterparty's survival. The largest such structure in the industry does not, however, sit at the chip layer. It sits inside the demand side itself, one exposure in this cohort that fits none of the standard categories of leverage or liquidity — and it attaches to the owner with the strongest conventional financing profile. Microsoft's position in OpenAI now comprises three mutually referencing elements [A]:

1. **An equity stake of approximately 27%** (as-converted, diluted) in OpenAI Group PBC, valued at approximately $135B at the October 2025 recapitalization — against total funding commitments of $13B, of which $11.8B had actually been funded as of March 2026. The stake is accounted for under the equity method, and its swings are already material to reported earnings: OpenAI losses reduced Microsoft's quarterly net income by $3.1B (41 cents of EPS) in the September 2025 quarter, while the recapitalization's dilution gain contributed to $5.9B of net gains in the following nine months.
2. **A contracted revenue stream:** under the October 2025 agreement, OpenAI committed to purchase an incremental **$250B of Azure services**, even as Microsoft relinquished its right of first refusal as OpenAI's compute provider.
3. **A strategic dependence:** a meaningful share of Azure's growth — the fastest-growing large revenue engine at Microsoft — derives from OpenAI's consumption, and Microsoft's data-center build-out is partly sized to OpenAI's projected demand.

The circularity is structural: Microsoft's equity stake is valuable because OpenAI grows; OpenAI grows by spending enormous sums on Azure; OpenAI funds that spending substantially through external capital raises whose valuations rest on growth expectations; and the $250B purchase commitment vastly exceeds OpenAI's current revenue base, meaning it is a claim on capital OpenAI has not yet raised. In the benign scenario this is a flywheel. In the adverse scenario — an OpenAI funding shortfall, a valuation reset, or a demand disappointment — Microsoft is exposed on three fronts simultaneously: the ~$135B transaction-implied value of the stake (a recapitalization mark, not the equity-method carrying value, but the reference against which a reset would be measured), the Azure revenue and backlog attributed to OpenAI's commitments, and the utilization of capacity built for a counterparty that can no longer pay for it. No other Big Four member carries a single-counterparty concentration of comparable size relative to its cloud growth narrative. This report therefore attaches an explicit qualifier to Microsoft's otherwise top-tier Axis II grade: the price and headroom of Microsoft's capital are the cohort's best, but a non-trivial share of the *earnings power that secures that standing* is referenced to a single private counterparty whose own financing needs are among the largest in corporate history. Oracle carries a directionally similar but even more concentrated version of this exposure through its OpenAI-linked OCI bookings, layered — unlike Microsoft's — on a BBB-tier balance sheet.

## 4.7 The composite Axis II scorecard

Combining the price dimension with the three quantity sub-dimensions and the counterparty overlay:

| Owner | ① Marginal cost | ② Internal generation | ③ Balance-sheet headroom | ④ Off-BS / commitments | **Composite** |
|---|:---:|:---:|:---:|:---:|:---:|
| Microsoft | A+ | A | A | A− (defensive structures) | **A+ †** |
| Alphabet | A | A− (FCF −47% but positive) | A+ (largest net cash; demonstrated full-spectrum access) | A | **A+** |
| Meta | A− | B+ (highest capex/revenue) | B+ | B− (SPV; rapid debt growth) | **B+** |
| Amazon | B+ | C+ (FCF ≈ zero, turning negative) | C+ (net debt; ~$170B incl. leases) | B | **B−** |
| Oracle | C | C | D+ (debt-to-equity near 500%) | C− (OpenAI concentration) | **C−** |
| CoreWeave / xAI | D | D | D | D | **D** |

† Subject to the counterparty-concentration qualifier of Section 4.6.

The scorecard's most consequential feature is not any single grade but the *ordering*: within the Big Four, the Axis II ranking (Microsoft ≈ Alphabet > Meta > Amazon) runs nearly opposite to the Axis I ranking (Google > Amazon > Meta > Microsoft) — with Google the sole owner near the top of both. Section 6 develops what that structure implies.

## 4.8 The neocloud financing model as the fragile tail

The neocloud cohort (CoreWeave, xAI) merits separate treatment because it is the only segment where both axes are adverse *and* interacting. These owners hold pure-Nvidia fleets at the highest unit costs in the cohort ($19,161 and $18,509 per H100e respectively), financed at sub-investment-grade rates, frequently secured against the GPUs themselves. The collateral is depreciating economically at roughly 30% per year (Section 5.1) while the market price of equivalent incremental capacity fell 12% during 2025 alone as Blackwell ramped — meaning the loan-to-value of GPU-backed structures deteriorates from both numerator and denominator. The neocloud model is solvent exactly as long as contracted tenant minimums outrun that depreciation; it is the levered tail of the industry's capital structure, and the first place any demand disappointment will be marked to market. In Report 13's terms, this cohort is the front line of the war of attrition and the watch-point of Trigger 3: the credit crack that contracts industry absorption capacity discontinuously arrives here first, which is why GPU-cloud credit spreads and collateral terms head that report's monitoring dashboard. The present report adds the quantitative reason the front line is where it is: these owners post the largest ante per unit at the highest funding cost — the exact combination the attrition equilibrium eliminates first.

---

# 5. Integration — The Fully-Loaded Cost per H100-Equivalent

## 5.1 Depreciation: a deliberately rough estimate under technological uncertainty

Consistent with Declaration 5, this section fixes δ to first-order precision only. Because the same rates apply to every owner, nothing in the competitive ranking depends on them; they set levels, and they determine how heavily the financing-rate differences of Section 4.2 are diluted.

**Non-chip infrastructure: δ_infra ≈ 10%.** This figure is not an assumption but a blend of two disclosed asset classes. Data-center shells, power, and cooling systems have useful lives of fifteen to twenty-five years — an annual rate of roughly 5–6% — while the non-accelerator IT inside them (CPU servers, memory, storage, networking) is depreciated over five to six years under the schedules the major clouds converged on by 2023–2024, roughly 17–20% per year [A]. Weighting the two components within the 45% non-chip capex share (facility-type assets roughly 25 points, IT-type assets roughly 20 points) yields a blended rate of approximately 10–11% per year.

**Accelerators: δ_chip ≈ 30%.** Three reference points bracket this choice. The floor is set by accounting policy: the large clouds carry server assets, including GPUs, at five- to six-year straight-line lives (Amazon shortened a subset from six years to five effective January 2025, explicitly citing the accelerating pace of AI technology, taking a $0.7B operating-income reduction plus $920M of accelerated depreciation; Meta simultaneously extended to five and a half years, booking a $2.9B depreciation reduction — identical hardware, opposite accounting conclusions) — implying 17–20% per year [A]. The ceiling is set by the pessimist case, argued most publicly by Michael Burry, that the true economic life of frontier GPUs is two to three years, implying 33–50% per year and, on his arithmetic, roughly $176B of understated industry depreciation across 2026–2028 [B]. Between the two sits the operational reality both camps partly acknowledge: a value cascade in which accelerators serve frontier training in years one and two, migrate to high-value inference in years three and four, and finish in batch and legacy workloads in years five and six — economically productive for six years, but shedding a large step of value every two [B]. A 30% declining-balance rate reproduces this cascade almost exactly: residual value of ~49% after two years, ~24% after four, ~12% after six. It also matches the observed market repricing — B200 delivered H100e capacity at 41% below Hopper pricing roughly two years after Hopper's peak deployment, and secondary rental rates for prior-generation parts have fallen far faster than accounting schedules imply. We emphasize that 30% is an *economic* depreciation rate; the accounting rates the owners report are materially lower, which is precisely why reported earnings are an unreliable guide to the user cost of compute.

Blended across the 55/45 capex split, industry-level economic depreciation runs at roughly 20% per year (0.55 × 30% + 0.45 × 10%). Sensitivity to this parameter is shown in Section 5.3.

## 5.2 The user-cost calculation: the fully-loaded leaderboard

The final input is K, the uniform non-chip capex per H100e. Under Declaration 1 (chip share 55%), K follows from the industry-wide blended chip cost — approximately $15,400 per H100e at Q4 2025, computed across all owners in the dataset rather than only this report's seven-owner cohort, whose own blend is roughly $14,800 [B] — inverted through the capex split: K = $15,400 × (45/55) ≈ **$12,600 per H100e** (range $10,300–$15,400 across the 50–60% chip-share band). Anchoring K to the cohort blend instead would lower it to roughly $12,100, shifting every owner's level down slightly without changing any ranking or materially moving any ratio.

Assembling UC_i = 0.30·P_i + 0.10·K + r_i·(P_i + K):

| Owner | P_i (chip $/H100e) | P_i + K (total capex) | r_i | **UC_i ($/H100e·yr, approx.)** | vs. Google |
|---|---:|---:|---:|---:|---:|
| **Google** | 9,714 | 22,314 | 3.8% | **~5,000** | 1.00× |
| **Amazon** | 13,765 | 26,365 | 3.9% | **~6,400** | 1.28× |
| **Meta** | 17,296 | 29,896 | 4.0% | **~7,600** | 1.52× |
| **Oracle** | 17,597 | 30,197 | 4.6% | **~7,900** | 1.58× |
| **Microsoft** | 18,666 | 31,266 | 3.6% | **~8,000** | 1.59× |
| **xAI** | 18,509 | 31,109 | ~9% | **~9,600** | 1.91× |
| **CoreWeave** | 19,161 | 31,761 | ~9% | **~9,900** | 1.96× |

*All values are rough estimates carrying uncertainty of at least ±20%; only rankings and multiples are asserted. Microsoft and Oracle are statistically indistinguishable — Oracle's slightly cheaper fleet mix offsets its ~100bp funding disadvantage almost exactly.*

Under central assumptions, operating one H100e for one year costs Google approximately $5,000 and Microsoft approximately $8,000. Scaled to Google's 5.03M-H100e fleet, the annualized gap versus Microsoft's cost structure is on the order of $15B per year — a recurring annual saving equal to roughly half the one-time B200-basis capex avoidance of Section 3.3; the counter-factual advantage, in other words, now re-accrues about every two years.

One further computation closes the stock/flow discipline of Section 2.3. The cumulative P_i is a *stock* price, weighted down by Hopper-era purchases for merchant buyers and by early-generation TPUs for Google; the ante in the attrition war going forward is the *flow* price. Rerunning the identity on 2025 net-addition chip costs (Google $7,384, Microsoft $16,063, uniform K) widens the Google–Microsoft fully-loaded ratio from 1.59× to roughly 1.7×. The stock-based leaderboard above is therefore the *conservative* version of the report's central result: at the margin, the gap is wider than the installed base shows.

## 5.3 The dilution effect, and its sensitivity

An honest framework must report what the integration *weakens* as well as what it confirms. At the chip level, Google's advantage over Microsoft is 1.92×. Passing it through the uniform non-chip layer K — which every owner buys at the same assumed price — dilutes the fully-loaded advantage to approximately **1.59×**. This is the framework's self-correction against the maximalist reading of vertical integration: custom silicon does not make compute five times cheaper end-to-end, because silicon is only 55% of the bill and the remaining 45% is competitively undifferentiated by assumption. What survives the dilution is nonetheless decisive — Microsoft's annual unit cost still runs roughly 60% above Google's — and it is robust: varying the chip share across 50–60% moves the ratio between 1.55× and 1.63×, and varying δ_chip across 25–35% moves it between 1.55× and 1.62×. No plausible parameterization brings the merchant-dependent cost structure within a third of the integrated one.

## 5.4 The asymmetry result: multiples versus basis points

The identity also quantifies the relative force of the two axes, and the result is stark. Within the Big Four, the entire after-tax financing spread (~30–40bp on a capex base of $22,000–31,000 per H100e) moves the annual user cost by roughly $90–125 per H100e — about 1.5–2% of the total. The chip-cost spread moves it by roughly $2,700–3,000 per H100e — over half of Google's entire unit cost. Microsoft's AAA rating, the best credit standing in global technology, offsets less than one-twentieth of the disadvantage created by its silicon position. **Within investment grade, Axis I operates in multiples and Axis II in basis points.**

The asymmetry inverts at the rating boundary. For the neocloud cohort, the ~500bp financing gap contributes roughly $1,600 per H100e of annual cost — about a third of their total disadvantage versus Google — making capital a first-order variable exactly where the credit spectrum ends. The capital axis, in short, is second-order *inside* investment grade and first-order *outside* it.

## 5.5 Reframing Axis II: financing capacity as the constraint on net-addition velocity

If the price of capital barely moves the unit cost of the stock, is Axis II a minor axis? No — its force applies to a different variable. In an externally financed capex regime, what capital procurement determines is the **sustainable rate of net additions**: how many quarters of $50–60B industry-wide adds each owner can underwrite before balance-sheet headroom, rating thresholds, or equity-market patience binds. On that variable the Section 4.7 scorecard is decisive rather than marginal. Amazon holds the second-best unit economics in the industry but the least financing headroom in the Big Four — its ability to *realize* its Axis I advantage at scale is the open question, because every marginal Trainium rack is now a financed rack. Alphabet, by contrast, has demonstrated funding access across the entire capital structure and secured a large tranche of its trajectory in advance. Microsoft can finance essentially any build-out it chooses, subject to the Section 4.6 qualifier that the demand underwriting part of that build-out is concentrated in a single counterparty. The stock is priced by silicon; the flow is rationed by capital. This is the two-axis restatement of Report 13's attrition equilibrium: exit proceeds in order of staying power, and staying power is jointly determined by how much each round of the game costs a player (Axis I) and how many rounds the player can fund (Axis II).

---

# 6. Competitive Positioning: The Unit-Cost × Financing-Capacity Matrix

## 6.1 The two-axis grade matrix

| Owner | Axis I — Silicon (unit cost of compute) | Axis II — Capital (financing capacity) | Verdict |
|---|:---:|:---:|---|
| **Google** | **A** ($9,714/H100e; TPU 75.6% of fleet) | **A+** (Aa2; largest net cash; full-spectrum market access) | **The only dual-axis leader** |
| **Amazon** | **A−** ($13,765; Trainium 41.6% of fleet) | **B−** (net debt; FCF turning negative) | Best-in-class flow economics, most constrained flow financing |
| **Meta** | **B** ($17,296; AMD-optimized merchant fleet) | **B+** (strong cash generation; rising structured leverage) | The ceiling of the non-integrated path |
| **Microsoft** | **C+** ($18,666; no at-scale in-house silicon) | **A+ †** (AAA/Aaa; net cash; counterparty qualifier) | Cheapest money, most expensive compute |
| **Oracle** | **C** ($17,597; 94.5% Nvidia) | **C−** (Baa2; ~500% debt-to-equity; OpenAI concentration) | Leveraged exposure on both axes |
| **CoreWeave / xAI** | **C−** ($18.5–19.2k; 100% Nvidia) | **D** (sub-IG, GPU-collateralized) | The fragile tail |

† Subject to the Microsoft–OpenAI counterparty-concentration qualifier (Section 4.6).

*Axis I grades rank current blended unit cost adjusted for structural trajectory: an at-scale in-house program (Google, Amazon) or a funded pipeline toward one (Microsoft's Maia, Meta's MTIA) grades above a structurally merchant position at similar or even lower current cost (Oracle, the neoclouds). This is why Microsoft's C+ sits above Oracle's C and xAI's C− despite Microsoft's higher blended $/H100e today (Section 6.6): the grade prices the option on exiting merchant dependence, which Oracle and the neoclouds do not hold.*

The matrix's structural signature is the near-inversion noted in Section 4.7: among the Big Four, silicon rank and capital rank run in nearly opposite order, with Google the lone exception near the top of both. It bears repeating (Section 4.4) that this inversion is a *coincidence of portfolio composition, not a trade-off*: Microsoft's capital strength comes from its software-weighted non-cloud businesses, Amazon's capital constraint from its logistics-weighted one, and neither is a consequence of the firm's silicon strategy. The practical implication of the inversion is nonetheless real: each of the three non-Google majors enters the next phase of the build-out with one strong axis compensating for one weak one, while Google alone compounds two advantages multiplicatively.

## 6.2 Google — the only dual-axis leader

Google's position is the report's central empirical fact. On Axis I it operates the industry's largest compute fleet at the industry's lowest unit cost, with the in-house share of the fleet still rising (68.6% → 75.6% during 2025) and the in-house platform's unit economics improving faster than the industry blend. On Axis II it holds the cohort's largest net cash position, an Aa2/AA+ rating, and — after the November 2025 and February 2026 debt programs and the June 2026 equity program of up to ~$85B — a demonstrated ability to fund at jumbo scale in every instrument class, including the sector's first century bond in a generation. In user-cost terms Google operates compute at roughly 60% of Microsoft's unit cost while enjoying financing capacity at least Microsoft's equal in quantity terms. The two advantages multiply: cheaper units, financed more durably, compounding into installed-base share (+4.07pp in 2025 alone, the largest single-owner gain in the dataset). If the trajectory of this report has a single terminal sentence, it is that the intelligence economy's cost floor is currently being set in one company's fleet.

## 6.3 Microsoft — cheapest money, most expensive compute

Microsoft's profile is coherent once decomposed. Its Axis II position is, on conventional metrics, the best in global technology: AAA/Aaa (a notch above the U.S. sovereign since May 2025), large net cash, defensive off-balance-sheet structures, and effectively unlimited market access. Its Axis I position is the weakest of the Big Four: the dataset shows no at-scale contribution from Maia through Q4 2025, leaving Microsoft the largest Nvidia customer in the industry ($61.0B of cumulative Nvidia spend, 22.3% of Nvidia's installed-base value) with 43% of its cumulative spend sitting in Hopper-generation assets that Blackwell pricing has repriced by roughly 40% per unit of compute. The result is the cohort's most expensive large-scale compute at the cohort's cheapest funding — and, per Section 5.4, the funding advantage recovers less than one-twentieth of the silicon disadvantage.

Two forward variables dominate Microsoft's trajectory. The first is Maia's time-to-volume: every year of delay compounds the installed-base gap, because the competitors' in-house fleets are accumulating at manufacturing cost while Microsoft accumulates at merchant cost. The second is the OpenAI structure (Section 4.6): a 27% stake valued near $135B against $11.8B actually funded, a $250B Azure purchase commitment from a counterparty that must raise historic amounts of external capital to honor it, and a cloud-growth narrative in which that counterparty is the single largest thread. Microsoft's financing strength is real, but a material share of the earnings power underwriting it is referenced to one private company's solvency; a severe OpenAI funding failure would strike Microsoft's equity account, its Azure backlog, and its capacity-utilization assumptions simultaneously. The qualifier does not change Microsoft's grade within Axis II's four financing sub-dimensions; it bounds the confidence with which that grade can be extrapolated.

## 6.4 Amazon — the tension case: superior unit economics on the cohort's tightest balance sheet

Amazon holds the industry's second-best silicon economics — a $13,765 blended fleet, Trainium2 additions at $6,094, a dual-platform strategy that scales in-house and merchant silicon in parallel — attached to the Big Four's weakest financing position: the only net-debt balance sheet, roughly $170B of debt and lease obligations, free cash flow at approximately zero and projected negative through 2026, and a rating outlook already trimmed on capex grounds.

As established in Section 4.4, this pairing is not a strategic trade-off but a portfolio inheritance. In cloud and in GPUs Amazon has spent shoulder-to-shoulder with Microsoft; what differs is that Amazon's second core business is a fulfillment and logistics network whose warehouses, vehicles, and facilities have accumulated a $103B lease book, while Microsoft's second core business is software that accumulates almost no capital at all. Amazon's constraint is thus older than its AI program and independent of it — which cuts both ways. It means the constraint is not evidence against the Trainium strategy (the strategy is, on the contrary, the cheapest incremental capacity any owner deployed in 2025 outside Google). But it also means the constraint cannot be strategized away: the retail business's capital intensity is permanent, and every dollar of AI capex now competes with it for balance-sheet room. Amazon is therefore the owner for whom Section 5.5's reframing matters most: its Axis I advantage is realized only at the velocity its Axis II capacity permits, and that capacity is the cohort's scarcest. The bull case is that AWS margins and Trainium unit economics grow into the balance sheet; the bear case is that Amazon becomes the first Big Four member forced to choose between capex velocity and its rating.

## 6.5 Meta — the ceiling of the non-integrated path

Meta demonstrates both the reach and the limit of optimizing within a merchant fleet. Its AMD allocation (19.9% of installed compute at 11.4% of installed cost) buys it a blended unit cost below Microsoft's without a silicon program of its own, and its advertising engine remains a formidable cash generator. But the path has a ceiling — AMD pricing sits far above manufacturing-cost silicon — and Meta is financing the gap with the cohort's fastest-rising leverage: debt roughly doubling in a year, the ~$27B Hyperion campus structured as an 80/20 Blue Owl–Meta joint venture that keeps most of its funding off Meta's balance sheet, and the highest capex-to-revenue ratio among the four. Meta's B/B+ pairing is the profile of a firm buying time: enough cost discipline to stay competitive, enough financing capacity to stay in the race, and a declared intention (MTIA) to eventually exit merchant dependence — but with the integrated pair's compounding advantage running against it each year the exit is deferred.

## 6.6 Oracle and the neoclouds — leveraged exposure on both axes

Oracle combines a nearly pure-merchant fleet (94.5% Nvidia by cost) with the cohort's weakest investment-grade balance sheet (debt-to-equity near 500% after $61.5B of issuance across 2022–2025 and a further $25B in early 2026) and the most concentrated OpenAI counterparty exposure relative to its size, embedded in OCI's contracted bookings. Its fully-loaded unit cost happens to sit near Microsoft's, but it arrives there from the opposite direction — a slightly cheaper fleet financed roughly 100bp wider — and with none of Microsoft's balance-sheet insulation. Oracle is running the industry's most leveraged version of the merchant strategy.

The neoclouds are the same position taken to its limit, as detailed in Section 4.8: the highest unit costs in the cohort, financed at the highest rates, against collateral depreciating at roughly 30% per year. Their user costs (~1.9–2.0× Google's) are the industry's marginal cost of compute — which is precisely why they are the natural shock absorbers of any demand disappointment.

## 6.7 Scenario horizon through 2027

Three trajectories follow from the framework if 2025's proportions persist. First, the installed-base share gap between the integrated pair and the merchant pair — 8.7pp at Q4 2025 — widens at roughly 6–7pp per year, since the integrated owners' incremental dollar buys 1.9–2.7× the compute. Second, the financing gap compounds in the same direction: at ~$725B of 2026 Big Four capex, an owner operating at Google's cost structure needs roughly 30% fewer dollars per H100e than one at Microsoft's on a fully-loaded basis (and over 50% fewer on the accelerator bill alone, at 2025 net-addition prices) to add the same capacity, so Axis I advantage feeds directly back into Axis II headroom. Third, the tail tightens first: neocloud and Oracle economics are the shortest fuse, because their unit costs are highest, their funding costs rise fastest under stress, and their demand books are the most counterparty-concentrated. The framework's summary prediction is not that merchant-dependent owners fail — their franchises are vast — but that the cost floor of the intelligence economy migrates toward the integrated fleets, and pricing power over compute migrates with it.

Read against Report 13, these trajectories supply the missing half of the rotation framework. Report 13's dashboard specifies *when* to rotate — synchronized equipment orders, the legacy/leading-edge price spread, the first credit deterioration in the GPU-cloud tier — but a rotation needs a destination, and the destination is a ranking of survivors. This report's matrix is that ranking. If the inversion arrives on schedule, the attrition war resolves in the order the grades imply: the levered tail first (Trigger 3 firing where Section 4.8 locates it), the double-C profiles next, and the endgame contested among owners whose weak axis is compensated by a strong one — with the single dual-axis leader inheriting the largest share of the consolidated prize. And if the market's present preference structure — enthusiasm for the rent collectors, skepticism toward the capex spenders — persists into that resolution, the repricing of the survivors is the residual alpha the two reports jointly describe.

---

# 7. Falsification Criteria and Open Questions

The two-axis thesis is falsifiable, and symmetric treatment requires stating the conditions under which it fails.

**Conditions under which the silicon wedge closes.** (i) Microsoft's Maia or Meta's MTIA reaching multi-million-H100e volume at TPU-class unit economics within two to three years would compress the P_i spread that drives every result in Section 5; the Google–Amazon time-to-volume advantage is measured in years, not in kind. (ii) A structural collapse in Nvidia's gross margin — under competitive pressure from AMD, in-house silicon, and its own Blackwell-era pricing — would shrink the wedge from the merchant side; the 2025 data already show Nvidia's blended net-add price falling 12% within the year. (iii) Persistent CUDA lock-in on frontier training workloads could cap the in-house share of fleets well below 100%, bounding the realized advantage below the platform-level wedge. Against this, the observed 2025 trajectory — in-house platforms gaining capacity share while their unit costs fall faster than the industry's — currently runs opposite to all three closure paths.

**Conditions under which the capital axis becomes first-order inside investment grade.** The basis-points result of Section 5.4 holds at 2025–2026 rate levels and spreads. A credit repricing of AI-linked issuance — spreads widening from tens to hundreds of basis points, as several institutional investors have warned is underpriced at current levels — would push the investment-grade cohort toward the regime the neoclouds already inhabit, and the quantity constraint of Section 5.5 would bind earlier and harder, first for Amazon and Oracle. Conversely, a sustained demand disappointment would flip the report's entire framing from "who adds capacity cheapest" to "who carries stranded capacity cheapest" — a question the same user-cost identity answers, with the same ranking, but with δ doing the damage instead of r.

**Known data limitations.** The chip-cost dataset underlying P_i consists of median estimates subject to revision; the H100e normalization does not capture memory bandwidth, interconnect, or software efficiency, and therefore neither does the user cost built on it; K, r_i, and δ are declared rough. The report's claims are calibrated accordingly: rankings and multiples, not point values.

---

# 8. Strategic Implications

1. **The cost floor of the intelligence economy is set by vertically integrated fleets, and the gap is a multiple, not a margin.** Under any parameterization within the declared ranges, the fully-loaded annual cost of an H100e differs by roughly 1.55–1.63× between the best-positioned and worst-positioned major hyperscaler. Every downstream economic thesis of this series — token pricing, agent unit economics, inference-cost deflation — inherits this floor.

2. **Credit quality is not a compute-cost strategy.** The best balance sheet in world technology recovers less than one-twentieth of the cost disadvantage created by merchant silicon dependence. Capital strategy determines who can *keep building*; silicon strategy determines *at what cost*. Investors and counterparties should score the two independently, and be suspicious of narratives that let strength on one axis stand in for the other.

3. **Financing capacity is the binding constraint of the externally funded era — and it is unevenly distributed for reasons unrelated to AI.** Amazon's constraint is a legacy of retail capital intensity; Microsoft's headroom is a property of a software-weighted portfolio; Alphabet's is the product of an advertising cash engine plus a deliberately demonstrated, full-spectrum funding program. The 2026 capex race will be decided as much by these inheritances as by any AI-specific decision.

4. **Counterparty circularity is the cohort's least-priced risk.** The Microsoft–OpenAI structure — equity value, contracted cloud revenue, and capacity planning all referencing a single private counterparty with historic external funding needs — and its more leveraged Oracle analogue concentrate an unusual share of the industry's reported growth in the solvency of one customer. The exposure sits, notably, on the two balance sheets most and least able to absorb it.

5. **The marginal cost of compute lives in the tail, and the tail is levered.** Neocloud unit costs at roughly twice the integrated floor, financed against collateral depreciating ~30% annually, make that cohort the industry's shock absorber. The repricing of any demand disappointment will appear there first — in GPU-backed credit, not in hyperscaler equity.

6. **For the series' terminal question — who profits from the intelligence economy — the answer at the infrastructure layer is now empirical.** Report 13 argued that the market's celebration of the chip complex and its skepticism toward the capex spenders describe the present phase of the cycle, not its resolution: rent migrates downstream, and the attrition war concentrates the downstream around its strongest players. This report completes the argument by naming them. Profit pools migrate toward whoever operates compute below the market-clearing user cost and can fund its expansion the longest; at Q4 2025 that is, by a wide and widening margin, the owners who design their own silicon and deploy it from a position of balance-sheet strength. One firm currently satisfies both conditions — and the distance between it and the rest of the field is the single most underpriced fact in the infrastructure layer of the intelligence economy.

---

# Appendix A — Data Definitions and Bridging Assumptions

**H100-equivalent (H100e).** Compute capacity normalized to one Nvidia H100, computed from peak dense 8-bit throughput (FP16/BF16 where 8-bit is unsupported). A peak-throughput proxy: it does not capture memory bandwidth, interconnect quality, or workload-specific software efficiency.

**Cumulative installed base vs. net additions.** All fleet values are cumulative through the stated quarter; net additions are differences between cumulative snapshots (annual: Q4-over-Q4; quarterly: sequential).

**Chip cost (P_i).** Deployed chip cost per H100e, blended across the owner's cumulative fleet. For merchant silicon this reflects estimated purchase prices; for in-house silicon (TPU, Trainium), manufacturing/supplier-revenue cost (Declaration 3). Comparing internal-transfer cost to merchant list price slightly overstates the wedge; ignored design cost slightly understates owner-side burden; the two biases partially offset and neither approaches the magnitude of the 2.9–5.7× platform-level gaps.

**Non-chip capex (K).** Derived, not measured: K = (industry-wide blended chip $/H100e, computed across the full dataset — see Section 5.2) × (1 − s)/s at chip share s = 55%. K ≈ $12,600/H100e; range $10,300–15,400 for s ∈ [0.50, 0.60]. Assumed uniform across owners (Declaration 2). K covers shell, power, cooling, and non-accelerator IT; it excludes land banking and energy procurement contracts.

**Cost of capital (r_i).** After-tax marginal debt cost by rating tier, confidence C. Not a WACC; Section 5.4 establishes that refinement within investment grade would not change any conclusion.

**Depreciation (δ).** Economic, not accounting, rates: δ_chip ≈ 30% (declining-balance equivalent of the two-year training → inference → legacy cascade over a six-year service life), δ_infra ≈ 10% (blend of 15–25-year facility assets and 5–6-year IT assets). Owner-uniform by construction.

**2026 data.** Fleet analysis ends at Q4 2025; source data for 2026 was not yet finalized at the time of analysis. Capital-market events through June 2026 are included in Axis II.

---

# Appendix B — Owner-Level Input Table (central case)

| Owner | P_i ($/H100e) [B] | K ($/H100e) [C] | r_i (after-tax) [C] | δ_chip [C] | δ_infra [C] | UC_i ($/H100e·yr) |
|---|---:|---:|---:|---:|---:|---:|
| Google | 9,714 | 12,600 | 3.8% | 30% | 10% | ~5,000 |
| Amazon | 13,765 | 12,600 | 3.9% | 30% | 10% | ~6,400 |
| Meta | 17,296 | 12,600 | 4.0% | 30% | 10% | ~7,600 |
| Oracle | 17,597 | 12,600 | 4.6% | 30% | 10% | ~7,900 |
| Microsoft | 18,666 | 12,600 | 3.6% | 30% | 10% | ~8,000 |
| xAI | 18,509 | 12,600 | ~9% | 30% | 10% | ~9,600 |
| CoreWeave | 19,161 | 12,600 | ~9% | 30% | 10% | ~9,900 |

---

# References

1. Epoch AI (2026), "AI Chip Sales" and "AI Chip Owners" datasets. Published online at epoch.ai (https://epoch.ai/data/ai-chip-sales; https://epoch.ai/data/ai-chip-owners), licensed CC BY 4.0. All H100e capacity and cost-estimate figures in this report are Wisdom Hill Research's own calculations from data downloaded from these databases.
2. NVIDIA Corporation, "Financial Results for Third Quarter Fiscal 2026" (November 2025) — GAAP gross margin 73.4%, data-center revenue $51.2B.
3. Amazon.com, Inc., Annual Report / Form 10-K for fiscal year 2025 (SEC EDGAR) — Note 4 (Leases): gross lease liabilities $121.8B, present value ~$103B; long-term debt $65.6B.
4. Amazon.com, Inc., Form 10-K for fiscal year 2024 and Form 10-Q filings (2025) — change in useful life of a subset of servers and networking equipment from six years to five effective January 1, 2025, citing the pace of AI technology development; ~$0.7B 2025 operating-income impact and $920M accelerated depreciation in Q4 2024.
5. Microsoft Corporation, Form 10-Q for the quarter ended September 30, 2025 (SEC EDGAR) — Note 17: OpenAI recapitalization, ~27% as-converted diluted stake, $13B total funding commitment, incremental $250B Azure purchase contract, relinquishment of compute right of first refusal.
6. Microsoft Corporation, Form 10-Q for the quarter ended March 31, 2026 (SEC EDGAR) — $11.8B of the OpenAI commitment funded; $5.9B nine-month net gains on OpenAI investments including the recapitalization dilution gain.
7. CNBC, "Microsoft's OpenAI investment led to $3.1 billion drop in net income" (October 29, 2025).
8. Fortune, "OpenAI completes for-profit restructuring and grants Microsoft a 27% stake" (October 28, 2025); Data Center Dynamics, "OpenAI completes for-profit move" (2025–2026).
9. Alphabet Inc., Form 8-K and free-writing prospectus, June 2026 — concurrent public offerings of Class A/C common stock ($18B, upsized) and Series A/B 6.25% mandatory convertible preferred depositary shares ($16.75B, upsized), part of a total equity capital raise upsized beyond $80B, plus ATM program.
10. CNBC, "Why Alphabet's 100-year sterling bond is raising new fears over debt-fuelled AI arms race" (February 12, 2026); Global Finance, "Alphabet Taps Debt Markets With 100-Year Issuance" (2026); Euronews (February 10, 2026).
11. Yahoo Finance / Barchart, "What Does Alphabet's $31.5 Billion Bond Sale Really Mean" (February 2026) — $20B seven-part dollar offering, order books, November 2025 $17.5B offering with 50-year tranche and ~$90B of orders.
12. Yahoo Finance, "Meta, Alphabet, Amazon, and Microsoft are getting hooked on debt to fuel AI boom" (June 2026) — 2026 capex guidance by owner (~$725B combined); Meta total debt trajectory to ~$84B.
13. Tech Times, "Big Tech AI Spending Tops $725 Billion: Free Cash Flow Hits Zero This Summer" (June 2026) — Amazon TTM FCF decline from ~$38B to $1.2B; Alphabet Q1 2026 FCF −47%; Morgan Stanley AI-related issuance tracking (~$236B by May 31, 2026; ~$570B projected 2026); Moody's estimate of ~$662B of not-yet-commenced hyperscaler lease commitments.
14. Tomasz Tunguz, "Is Your AI Funded by Junk Bonds?" (December 2025) — 2025 hyperscaler bond issuance ~$121B vs. ~$28B five-year average; Meta–Blue Owl ~$27B Hyperion joint venture (Blue Owl 80% / Meta 20%), majority off Meta's consolidated balance sheet; Microsoft AI Infrastructure Partnership structure; Oracle issuance history and leverage.
15. Moody's Ratings — downgrade of the United States to Aa1 (May 2025); Amazon.com outlook actions (positive, March 2025; returned to stable, February 2026, citing accelerated capex); hyperscaler issuer ratings.
16. S&P Global Ratings and Fitch Ratings — issuer credit ratings for Microsoft (AAA), Alphabet (AA+), Amazon (AA / AA−), Oracle (BBB), as publicly reported.
17. SiliconANGLE / theCUBE Research, "Resetting GPU depreciation: Why AI factories bend, but don't break, useful life assumptions" (November 2025) — convergence of hyperscaler server schedules to six years by 2023–2024; three-stage GPU lifecycle framework (training years 1–2, real-time inference years 3–4, batch years 5–6); neocloud schedule comparison.
18. Deep Quarry (O. Usvyatsky), "Depreciation of GPUs: between useful lives and useful myths" (December 2025) and "Amazon revises server lifespan amid AI shift" (2025) — history of useful-life changes across Amazon, Alphabet, Meta, Microsoft, Oracle; Meta extension to 5.5 years with ~$2.9B depreciation reduction.
19. MBI Deep Dives, "Why I don't worry (as much) about big tech's depreciation schedule" (October 2025) — Azure GPU-generation retirement precedents of roughly 7–9 years; value-cascade deployment model.
20. Press coverage of Michael Burry's depreciation critique (Bloomberg, CNBC, November 2025) — claim of ~$176B understated depreciation across 2026–2028 under 2–3-year economic lives.

