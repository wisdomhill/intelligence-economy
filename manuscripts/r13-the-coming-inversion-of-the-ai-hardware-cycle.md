---
title: "13. The Coming Inversion of the AI Hardware Cycle"
subtitle: "The second derivative: stock-flow dynamics, migrating bottlenecks, and opposite games"
series: "The Intelligence Economy"
number: 13
manuscript-revision: 1
date: 2026-09-28
date-modified: 2026-09-28
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

# This manuscript writes real TeX math — see Appendix A. The conversion keeps
# $...$ math for it; the series default is off, because the other reports
# quote dollar amounts far more often than they write equations.
tex-math: true

description: >-
  Why the hardware cycle turns before demand does. Derived demand is a
  derivative, bottlenecks migrate to whatever cannot expand, and the
  cash-rich overbuild — three mechanisms pointing the same way.

keywords:
  - accelerator principle
  - bottleneck migration
  - HBM
  - capital cycle
  - derived demand
  - rotation

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
#
# Like Reports 7 to 11, this manuscript numbers its Executive Summary as
# section 1 and its cross-references depend on that, so the numbering is kept
# and the summary stays on the cover and in the PDF rather than becoming a
# chapter page.
#
# Chapter 7 is 3,013 words against 358 to 1,979 for every other chapter, so it
# is served as two web pages split at 7.5, where the structural argument gives
# way to the capacity timetable. Both are numbered 7, the way Report 5 serves
# its Part IV; the PDF keeps it as one chapter.
#
# The figure is the author's, referenced by bare filename, so a copy sits in
# reports/r13/ next to the qmd that includes it. See HANDOFF.md.
published:
  dir: reports/r13/
  pdf: r13-the-coming-inversion-of-the-ai-hardware-cycle.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r13/

chapters:
  - manuscript: "2. Framework I — Derived Demand Is a Derivative"
    published:  "2. Framework I: Derived Demand"
    fragment:   _01-derived-demand.qmd
    page:       01-derived-demand.qmd
  - manuscript: "3. Framework II — Bottleneck Migration"
    published:  "3. Framework II: Bottleneck Migration"
    fragment:   _02-bottleneck-migration.qmd
    page:       02-bottleneck-migration.qmd
  - manuscript: "4. Framework III — Capital Dynamics"
    published:  "4. Framework III: Capital Dynamics"
    fragment:   _03-capital-dynamics.qmd
    page:       03-capital-dynamics.qmd
  - manuscript: "5. The Integrated Model — Two Terminal Mechanisms, One Accelerant"
    published:  "5. The Integrated Model"
    fragment:   _04-integrated-model.qmd
    page:       04-integrated-model.qmd
  - manuscript: "6. Case Study — The Datacenter–NVIDIA Dyad"
    published:  "6. The Datacenter–NVIDIA Dyad"
    fragment:   _05-dyad.qmd
    page:       05-dyad.qmd
  - manuscript: "7. Additional Consideration — Memory (7.1–7.4)"
    published:  "7. Memory: The Structural Case"
    fragment:   _06-memory-structure.qmd
    page:       06-memory-structure.qmd
  - manuscript: "7. Additional Consideration — Memory (7.5)"
    published:  "7. Memory: The 2026–28 Ramp"
    fragment:   _07-memory-ramp.qmd
    page:       07-memory-ramp.qmd
  - manuscript: "8. Stress-Testing the Inversion Thesis"
    published:  "8. Stress-Testing the Thesis"
    fragment:   _08-stress-tests.qmd
    page:       08-stress-tests.qmd
  - manuscript: "9. Monitoring and Implications — A Conditional Rotation, Not a Timing Call"
    published:  "9. Monitoring and Implications"
    fragment:   _09-monitoring.qmd
    page:       09-monitoring.qmd
  - manuscript: "Appendix A — Mathematical Formulation"
    published:  "Appendix A"
    fragment:   _10-appendix-a.qmd
    page:       10-appendix-a.qmd
  - manuscript: "Appendix B — Historical Analogue Table"
    published:  "Appendix B"
    fragment:   _11-appendix-b.qmd
    page:       11-appendix-b.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _12-references.qmd
    page:       12-references.qmd
---
# The Coming Inversion of the AI Hardware Cycle

### The Second Derivative: Stock-Flow Dynamics, Migrating Bottlenecks, and Opposite Games

*The Intelligence Economy — Report 13 of 14*  
*Wisdom Hill Research | Thematic Research | September 2026*

---

# 1. Executive Summary

The prevailing market narrative holds that the semiconductor suppliers of the AI buildout — NVIDIA above all, and the memory makers behind it — are its structural winners, while hyperscale datacenter operators are capital-consuming machines whose free cash flow compresses with every quarter of accelerating capex. This report argues that the narrative has the cycle exactly backwards in time: it accurately describes the present and is therefore a poor guide to the future. The economic logic that makes the chip supplier today's rent collector is the same logic that positions it for the sharpest reversal, and the capital attrition that makes datacenter operators today's source of investor anxiety is the same process that will concentrate market power in the hands of the survivors.

**The causal chain in one line.** Contestability → defensive capacity commitments → chip flow outruns energized capacity → inventory and margin adjustment → rent migrates toward power, sites, and the surviving operators. The three frameworks below supply, in order, the reason each arrow follows from the one before it.

The argument rests on three interlocking frameworks. **Framework I** establishes that semiconductor demand is a *derivative* of end demand: chips are purchased not in proportion to the level of AI usage but in proportion to its rate of change. Because technology adoption follows an S-curve, the flow of new chip demand peaks near the adoption inflection point — when headline AI demand is still making all-time highs — and declines thereafter even as end demand continues to grow. The industry does not need demand to fall in order to suffer; it only needs demand to decelerate. **Framework II** establishes that the binding constraint on AI supply migrates downstream over time. Fab capacity is a self-resolving bottleneck: it takes years to build, but once built it generates a durable, cumulative production flow whose sustaining cost is small relative to its creation cost. Datacenter capacity is a self-intensifying bottleneck: it must be re-expanded every year against depleting inputs — power, grid access, permitted sites — whose marginal cost rises as the best locations are consumed. Effective AI supply is the minimum of two flows, and a crossing of those flows — a scenario to monitor rather than a mechanical certainty — would mark a regime change in which economic rent migrates from chips toward power and sites. **Framework III** establishes that the two industries are playing opposite games with opposite capital positions. Cash-rich chip suppliers are locked in a prisoner's dilemma in which pre-emptive capacity expansion is the dominant strategy precisely because no participant faces a financing constraint. Cash-consuming datacenter operators are locked in a war of attrition in which exit proceeds in order of capital cost, concentrating the industry around its strongest balance sheets.

The overexpansion mechanism that links the three frameworks becomes strongest when the accelerator market is contestable. A supplier facing no credible substitute can absorb much of the demand derivative through price and margin rather than capacity — building only to the output that maximizes its own profit, letting the gap between supply and demand widen, and collecting a rising rent — which mutes and delays the cycle. A supplier that can lose share transmits the same derivative more fully into volume, capacity commitments, and inventory risk. This is why the AI accelerator market, dominated for two years by a single supplier, behaved as it did — persistent shortage and expanding margins — and why the memory oligopoly, in which competition has always been real, is the industry the frameworks have historically described best. The report's central observation is that the accelerator market has now crossed the threshold. Hyperscalers' in-house silicon has become a credible substitute; the merchant leader has responded not by rationing output but by expanding it aggressively to defend deployment share; and its share of installed compute has fallen despite that expansion. With the market contestable, the frameworks bind on accelerators with the force they have long had in memory. None of them yet signals distress. What they signal is that the seeds of the cycle's inversion have been planted in the market where it was least expected.

The synthesis is a cycle whose peak is determined by whichever of two terminal mechanisms arrives first — a sign change in the second derivative of end demand, or the crossing of chip output and datacenter absorption capacity — with credit cracks in the attrition tier acting as an accelerant that can pull the crossing forward. None of these triggers can be timed in advance, but all three are monitorable, and this report closes with a dashboard of leading indicators and a trigger-based framework for rotation rather than a timing call.

**What is observed, and what is not.** The distinction matters more than any single claim in this report. *Observed today:* captive silicon taking compute share from the merchant leader; the merchant responding with aggressive capacity commitment rather than output discipline; power, grid, and siting constraints binding in a growing share of projects; and vendor support structures spreading through the neocloud tier. *Not yet observed:* accelerator inventory accumulating between delivery and energization; a deceleration in merchant order growth; and credit rupture in the attrition tier. *Would falsify:* a durable reversal of captive silicon's share of accelerator flow, or datacenter absorption capacity expanding faster than fab output compounds. The report's claim is that the conditions for inversion have formed, not that inversion has begun.

The case study applies the three frameworks to the relationship at the center of the cycle — the hyperscale datacenter and NVIDIA — and to the development that activated them: the customer who becomes a competitor. For a fabless rent collector, inversion takes the form of margin compression, volume displacement, and inventory adjustment rather than commodity price collapse, and the obvious defense, rationing output to protect price, is a trap that releases leading-edge foundry and packaging capacity to the very programs doing the displacing. Memory is treated as an additional consideration. It is the layer where the fixed-cost mechanics of Framework III bind hardest and where three incumbents racing for share have committed major capacity programs whose production milestones cluster in 2027–28; yet it is structurally better placed than logic, because memory density improves far more slowly than logic density, so that keeping pace with the accelerator requires proportionally more wafers, more equipment, and more fab space — capacity that carries lead time and therefore lags. Memory is the system's slower-moving complement and, for that reason, its recurring bottleneck. Its cycle nonetheless remains derived from accelerator flow: rising memory content per unit of compute may delay and soften memory's turn, but cannot prevent it.

A final word on what this report is and is not. It is not a near-term forecast. It does not predict that AI demand will decelerate within the next year or two, and it does not date the peak of the AI hardware cycle; Framework I explains why that date is unknowable in principle, not merely in practice. What the report offers instead is the structural sequence through which the cycle will eventually invert — a medium-to-long-term account of where economic rent sits today, why it will move, and what the movement will look like in observable data when it begins. The frameworks specify order and mechanism; the closing chapter specifies the indicators that will reveal timing when timing becomes knowable.

---

# 2. Framework I — Derived Demand Is a Derivative

## 2.1 Stock versus flow: the structural relationship between the two industries

The semiconductor industry and the datacenter industry stand in a supplier–customer relationship, but the economically decisive feature of that relationship is not who sells to whom. It is that the two sides of the transaction live in different dimensions of the same variable. Datacenter capacity is a *stock*: an accumulated quantity of installed compute, measured at a point in time. Semiconductor output is a *flow*: a rate of production, measured per unit of time. The relationship is most visible at its center: hyperscale datacenter operators accumulate a stock of installed accelerators, and NVIDIA, as the dominant merchant supplier, sells the flow that changes it. Every chip sold either adds to the stock (new capacity) or maintains it (replacement of depreciated equipment). The chip supplier's revenue line is therefore not a picture of how much AI computing the world does; it is a picture of how fast the world is *changing* how much AI computing it does.

This distinction, elementary as it sounds, is the single most consequential fact in the economics of the AI hardware cycle, because it means semiconductor demand is mathematically a derivative of end demand — and derivatives are more volatile than the functions they are taken from. One qualification governs how forcefully the derivative reaches the supplier. A firm that must build to defend share takes the derivative into volume and capacity commitments; a firm facing no credible substitute can take more of it into price and margin, smoothing its own revenue and leaving the volatility with its customers. The mechanism operates either way; its amplitude depends on how contestable the market is — a condition Chapter 6 examines for accelerators.

## 2.2 The accelerator principle

Let $Y(t)$ denote demand for datacenter services and let the capacity stock required to serve it be proportional: $K^*(t) = vY(t)$, where $v$ is the capital coefficient. Chip demand decomposes into a new-investment term and a replacement term:

$$
D_{semi}(t) \;=\; \underbrace{v \cdot \frac{dY}{dt}}_{\text{net capacity additions}} \;+\; \underbrace{\delta \cdot K(t)}_{\text{replacement demand}}
$$

where $\delta$ is the depreciation rate of installed equipment. The first term is the heart of the matter. Because it is proportional to the *time derivative* of end demand, the semiconductor industry does not require end demand to decline in order to experience a contraction. It only requires end demand to decelerate. If datacenter service demand downshifts from 30 percent annual growth to 15 percent annual growth — a trajectory most observers would describe as robustly healthy — the new-investment component of chip demand, holding the demand level constant, falls by half. Across consecutive periods the larger demand base partly offsets the lower growth rate — demand rising from 100 to 130 adds 30, and a subsequent 15 percent year adds 19.5, a decline of roughly a third rather than half — but the qualitative point stands: a mere halving of the *growth rate* produces an outright contraction in the *level* of new-investment chip demand. This is the accelerator principle, formulated by Clark (1917) and later integrated with the multiplier by Samuelson (1939) — "accelerator" here in its century-old macroeconomic sense, unrelated to the AI accelerator chips discussed elsewhere in this report — and it is the fundamental reason capital-goods industries exhibit wider cyclical amplitude than the final-demand industries they serve.

The replacement term $\delta K$ provides a floor under the flow, and its size matters for the depth of any downturn. Two features of the current cycle make this floor higher than in past hardware cycles: AI accelerators depreciate quickly relative to general-purpose servers, raising $\delta$, and the installed stock $K$ is growing rapidly. The floor rises — but a floor is not a ceiling, and the cyclical violence lives in the first term.

## 2.3 The S-curve and its derivative: why the peak arrives early

Technology adoption empirically follows a logistic (S-shaped) path (Rogers 2003): slow initial uptake, an acceleration phase, an inflection, deceleration, and saturation. Write adoption as

$$
Y(t) = \frac{L}{1 + e^{-r(t - t_0)}}
$$

where $L$ is the saturation level, $r$ the adoption speed, and $t_0$ the inflection point. The derivative —

$$
\frac{dY}{dt} = \frac{rL \, e^{-r(t - t_0)}}{\left(1 + e^{-r(t - t_0)}\right)^2}
$$

— is a bell-shaped curve (formally, the density of the logistic distribution, closely resembling a Gaussian). The decisive property is the location of its peak: the flow of new demand reaches its maximum at $t_0$, the moment adoption passes 50 percent of its eventual ceiling, and declines monotonically thereafter even as cumulative adoption continues to rise toward $L$.

The implication is the one markets most consistently misread. The statements "AI demand continues to grow" and "semiconductor demand is contracting" are not in tension; they describe the same moment on the curve. What determines the fate of the chip supplier is not the level of end demand, nor even its first derivative in isolation, but the *sign of the second derivative*. At the inflection point — where $d^2Y/dt^2$ turns negative — every headline indicator of end demand is still setting records. Usage is at all-time highs, growth remains strong by any historical standard, and the deceleration is visible only in second differences that are noisy in real time and confirmed only in hindsight. The pressure on new-capacity chip demand begins at precisely the moment the end-demand narrative appears most secure.

![The logistic adoption curve and its derivative](fig_scurve.png)

**Exhibit 1. The stock and its flow.** The end-demand curve $Y(t)$ (solid, left axis) rises monotonically toward saturation, yet the flow of new-capacity demand $dY/dt$ (dashed, right axis) is bell-shaped and peaks at the adoption inflection — the point at which cumulative adoption reaches roughly half of its eventual ceiling. Beyond that point, new-capacity chip demand declines in absolute terms even as end demand continues to set record highs. The divergence of the two curves is the analytical core of the cycle: the flow peaks and turns down while the stock is still climbing. The new-capacity component of chip demand turns while the customer's usage is still setting records; total semiconductor demand and supplier revenue follow with a lag shaped by replacement demand, pricing, and market share.

## 2.4 The amplification chain: derivatives stacked on derivatives

The derivative relationship does not operate once; it compounds at each upstream step of the value chain. End demand for AI services drives datacenter capacity investment, which is the first derivative. Chip orders respond to capacity investment with the additional distortions of inventory cycles and double-ordering, layering the bullwhip effect (Forrester 1961; Lee, Padmanabhan, and Whang 1997) on top of the accelerator. Semiconductor equipment orders, in turn, respond to *chip-capacity* investment — a derivative of a derivative of end demand. Each step upstream therefore exhibits greater amplitude than the one below it, which is why equipment makers have historically been the most violent cyclicals in the chain and why their order books function as the most sensitive leading indicator of the whole system. One further link matters for what follows: high-bandwidth memory is not sold into the datacenter on its own but bundled onto the accelerator, so its AI demand is derived from the accelerator flow rather than from the datacenter directly — a derivative one step further removed, with consequences developed in Chapter 7.

Two information pathologies amplify the chain further. During shortages, customers double-order across suppliers to secure allocation, so the demand signal reaching chip makers overstates true end demand at exactly the moment capacity decisions are being made. During slowdowns, customers work down inventory before placing new orders, so the signal understates true demand at exactly the moment capitulation pressure peaks. The supply chain thus transmits not the derivative of demand but an *exaggerated* derivative — and capacity, once built in response to the exaggeration, does not go away.

---

# 3. Framework II — Bottleneck Migration

## 3.1 Two kinds of constraints: self-resolving versus self-intensifying

At any moment, the expansion of AI compute is limited by the slowest link in a serial chain: chips must exist before they can be racked, and racks must have buildings, power, and cooling before chips can run. The binding link already varies by region and project: leading-edge fabrication, advanced packaging, and high-bandwidth memory — which take two to three years from groundbreaking to volume output, and which have been the constraints rationing NVIDIA's own shipments — remain the limiting factor in many deployments, while power availability, grid connection, and permitting already bind in others; the IEA estimates that grid constraints could delay around 20 percent of global datacenter capacity planned for construction by 2030 (IEA 2025). But the two candidate bottlenecks are not symmetric in kind, and the asymmetry determines how the constraint migrates over time.

Fab capacity is a **self-resolving** constraint. It is expensive and slow to create, but once created it generates a durable production *flow* rather than a one-time output. The flow is not literally free to sustain — fabs require continuous maintenance and sustaining capex, manufacturing equipment carries accounting lives of only three to eight years, and effective output can fall through utilization cuts, node transitions, or equipment retirement (Intel Corporation 2026; ASML n.d.) — but relative to the datacenter side the asymmetry holds: the incremental cost of *continuing* an existing fab's flow is small relative to the cost of *creating* it, and yield learning typically raises effective output over a fab's life. The semiconductor bottleneck thus behaves like a toll paid largely up front: over multi-year horizons, the industry's aggregate output capability ratchets upward as previously committed fabs reach volume. The ratchet has a governor: the pace at which new fabs can be equipped is set by the manufacturing-equipment and materials suppliers upstream of the fab, an oligopoly whose own position at the far end of the amplification chain (Section 2.4) makes it rationally slow to expand. Fab capacity resolves, but at a pace set upstream.

Datacenter capacity is a **self-intensifying** constraint. The datacenter layer must *absorb* the chip flow — convert it into installed, powered, operating stock — and absorption requires new inputs every single year: another building, another power contract, another permitted site, another grid connection. Last year's datacenter housed last year's chips; this year's chips need this year's construction. The constraint renews itself annually, and, critically, its inputs deplete. The cheapest power, the most permissive jurisdictions, and the grid interconnections with available headroom are consumed first, so the *n*-th datacenter is structurally more expensive and slower to deliver than the (*n−1*)-th.

## 3.2 Effective supply as a min-function

Formally, the growth of installed AI compute is governed by the lesser of two flows:

$$
\frac{dK_{AI}}{dt} \;=\; \min\left( F_{semi}(t),\; A_{DC}(t) \right)
$$

where $F_{semi}(t)$ is the chip output flow — driven upward over multi-year horizons by the cumulative stock of committed fabs, though not strictly monotonic period by period — and $A_{DC}(t)$ is the datacenter absorption flow, a function of newly secured power, sites, and capital, whose growth faces structural ceilings. Early in the buildout, $F_{semi} < A_{DC}$: chips are scarce, datacenter shells wait for silicon, and the chip maker is the binding constraint and the rent collector. Because one curve is fed by an accumulating stock while the other must be renewed each year against depleting inputs, the structural pressure is toward reversal of the inequality — a crossing that is a scenario to monitor rather than a mathematical certainty, since supply-side discipline or absorption-side relief can defer it. If and when it occurs, the crossing point is a regime change: chips become abundant relative to the places they can be plugged in, unabsorbed flow accumulates as inventory, and inventory is the transmission mechanism from physical imbalance to price.

A subtle but important corollary: the downstream bottleneck does not merely slow AI deployment — it *accelerates the upstream glut*. Chip makers expanding against (exaggerated) demand signals are building flow that the absorption layer cannot take. The supply-demand crossing can therefore arrive *before* the end-demand inflection point of Framework I. The cycle has two independent ways to end, and the earlier one governs.

## 3.3 Diverging long-run cost trajectories

The migration is reinforced by a divergence in the two industries' long-run cost trajectories — two different cost concepts moving in opposite directions. On the semiconductor side, the *long-run unit cost of compute* falls over time: learning curves (Wright 1936), yield ramps, and node shrinks deliver more compute per dollar every year, because the industry's decisive inputs are manufactured goods whose supply is expandable with capital. On the datacenter side, the *marginal cost of incremental supply* rises: its inputs are location-bound and depletable, and several carry lead times longer than fabs themselves. In the United States, the median time from interconnection request to commercial operation for generation projects completed in 2023 was five years (Lawrence Berkeley National Laboratory 2024); gas turbines carry multi-year order backlogs; new generation takes five years for combined-cycle gas and a decade or more for nuclear; even transformers have become multi-year lead-time items. Non-technical constraints — permitting, community opposition, political resistance to electricity price increases, water availability — are not relievable by capital at all and tend to *tighten* as datacenter density rises. One industry's cost of delivering compute falls over time; the other's cost of expanding capacity rises. Relative scarcity, and with it relative pricing power, migrates accordingly.

## 3.4 Rent follows the binding constraint

The theory of constraints (Goldratt & Cox 1984) carries a clean economic corollary: in a serial production system, economic rent accrues to whoever owns the binding constraint, because scarcity is where pricing power lives. The extraordinary margins currently earned by the merchant accelerator leader — gross margins far above any historical norm for a merchant semiconductor supplier — and, behind it, in advanced memory, are not a reward for technological brilliance in the abstract; they are the rent attached to today's bottleneck. When the bottleneck migrates, the rent migrates with it — toward contracted power capacity, grid access rights, permitted and energized sites, the power-equipment supply chain (turbines, transformers, switchgear), and the operators who locked in electricity before scarcity repriced it. The accelerator margin, as the largest single concentration of rent in the chain, is the quantity with the furthest to fall. For the investor, this is the time-axis translation of the thesis: the locus of alpha moves downstream as the buildout matures.

---

# 4. Framework III — Capital Dynamics

## 4.1 Cash-flow asymmetry: rent collectors versus J-curve spenders

The picks-and-shovels metaphor has a precise financial content: it is a statement about *when cash converts*. The chip supplier, owning today's bottleneck, converts immediately — revenue is collected at historically elevated margins, and in the tightest tiers customers pay to secure allocation before delivery, through prepayments, capacity reservations, and multi-year take-or-pay agreements, so that cash arrives before production. Free cash flow accumulates, and in the merchant accelerator leader's case it accumulates on a scale that finances not only its own expansion but, as Section 4.5 shows, its customers'. The datacenter operator faces the opposite sequence: capex leaves now, revenue arrives later, and the monetization of AI services has so far lagged the growth rate of the investment required to serve them. The gap between capex and operating cash flow must be financed — with debt, leases, special-purpose vehicles, or equity — and so the datacenter layer's expansion capacity $A_{DC}$ becomes a function not only of power and sites but of *capital market conditions*. Interest rates, credit spreads, and shareholder tolerance for free-cash-flow compression all enter the absorption curve as additional brakes.

## 4.2 Fixed costs, marginal-cost pricing, and cyclical amplitude

The severity of a semiconductor downturn is not principally a demand phenomenon; it is a consequence of the industry's cost structure, and stating the microeconomics precisely is warranted because it explains why oversupply in this industry produces price collapse rather than gentle adjustment.

A fabrication plant's costs are overwhelmingly fixed and sunk. The depreciation, financing, and maintenance of a facility costing tens of billions of dollars are incurred regardless of how many wafers pass through it, while variable costs — silicon wafers, process chemicals, electricity, consumables — scale with output but constitute a modest share of total cost per unit. A profit-maximizing producer expands output up to the point where price equals marginal cost, and continues to supply as long as price exceeds marginal cost. Because marginal cost in a fab is low relative to average total cost, this condition is satisfied at prices far below the level that would cover full cost. In a glut, therefore, producers keep running and keep supplying even while price has fallen well beneath average total cost — that is, while they are recording sustained accounting losses. The price at which output is withheld is set by marginal cost, not by full cost, and marginal cost lies far beneath it.

The consequence for cyclical behavior is decisive. When overcapacity emerges, the price floor is not the level at which producers begin to lose money; they will endure sustained losses long before any capacity leaves the market, because withholding output is rational only once price falls to marginal cost. A commodity product compounds the problem: with little differentiation, no producer can defend price through quality, and all are driven toward the same marginal-cost floor at once.

The mechanism binds directly on whoever owns the fab — the foundry and the memory maker. It binds on the fabless accelerator designer indirectly, but not weakly. Capacity reserved at the foundry and the packaging house, and memory secured under long-term agreements, are contractual fixed costs: take-or-pay commitments and prepayments incurred regardless of end demand. A fabless supplier facing a demand deceleration therefore confronts the same choice as a fab owner — honor the commitments into a glut or write them down — in contractual rather than physical form. The operating leverage changes shape; it does not disappear.

This cost structure is also the reason the semiconductor industry is exceptionally cyclical *relative to manufacturing generally*. The amplitude of a cyclical industry's earnings swings is governed by its operating leverage — the ratio of fixed to variable costs — which determines both how far price can fall below full cost before output is withdrawn and how violently margins move for a given change in price or volume. Semiconductor fabrication carries a fixed-cost share far above that of most manufacturing, where materials and labor dominate and price tracks full cost far more closely. The larger the fixed-cost share, the wider the gap between the marginal-cost floor and full cost, and the deeper and longer the loss-making trough a downturn can produce. The industry's sensitivity to the business cycle is therefore not incidental but structural, and disproportionately greater than that of manufacturing sectors with more balanced cost structures. This is the supply-side mechanism that converts the demand deceleration of Framework I into a price collapse rather than a soft landing: Framework I explains why capacity overshoots demand, and the cost structure explains why the resulting glut clears through prices driven toward marginal cost and through prolonged losses rather than through prompt supply withdrawal.

## 4.3 The prisoner's dilemma of the cash-rich: why abundant cash produces overexpansion

The capacity decision facing a small number of well-capitalized chip suppliers has the structure of a prisoner's dilemma. If all participants restrain expansion, industry profits are maximized — the collusive optimum. But if rivals expand while one firm abstains, the abstainer permanently cedes share; in markets where customer qualification and long-term agreements lock in allocation for a product generation, the loss compounds. Expansion is therefore close to a dominant strategy, and the Nash equilibrium is industry-wide overexpansion. Capacity, moreover, functions as a commitment device in the sense of Dixit (1980): building ahead of demand credibly threatens to flood the market, deterring rivals' expansion — which is precisely why each player races to build first.

The dilemma requires at least two players who can take each other's share. A supplier facing no credible substitute plays a different game: it expands capacity only to the output that maximizes its own profit, and the widening gap between demand and supply is the source of its rent rather than a cost it bears. The demand derivative of Framework I and the bottleneck migration of Framework II still reach such a firm — no supplier is exempt from its customers' deceleration, or from their inability to energize what it ships — but it can absorb more of both in price and margin rather than in capacity, and nothing compels it to overbuild, because there is no one to lose share to. The overexpansion mechanism is therefore the part of the system that depends on contestability, and the question of whether it is live in a given chip market reduces to whether the leading supplier can still be displaced. In memory the answer has always been yes: three incumbents of comparable capability have contested share for two decades, and the memory cycle is the textbook case of the dilemma. In accelerators the answer was, until recently, no. Chapter 6 shows that it has changed, and that the merchant leader's behavior has changed with it — from rationing output as a monopolist to expanding it as a competitor whose largest customers have become its rivals.

What historically interrupted this equilibrium was the financing constraint. In past semiconductor shakeouts the game ended when the weakest players ran out of cash and exited, restoring supply discipline by subtraction. The current cycle's distinguishing feature is that *every* supplier at the table — merchant designer and memory incumbent alike — is accumulating record cash from the boom itself. A prisoner's dilemma played by participants with unconstrained balance sheets resolves the way the theory predicts: everyone expands. Financial discipline — the historical circuit breaker — is not wired into this cycle.

## 4.4 The datacenter war of attrition

The datacenter investment race has the opposite game structure: a war of attrition (Maynard Smith 1974). Remaining in the game requires posting an enormous ante — tens of billions in annual capex — every year. Cumulative losses grow with time in the game, and the prize concentrates on whoever remains when others fold. The equilibrium of a war of attrition is exit in order of staying power, which here means exit in order of capital cost. The most exposed tier is the **neocloud** segment — independent operators such as CoreWeave that rent accelerator capacity to AI developers and hyperscalers and finance their fleets with chip-collateralized debt — doubly fragile because the collateral itself is a fast-depreciating asset whose resale value falls fastest exactly when credit conditions tighten. Next come second-tier operators whose core businesses cannot internally fund the AI capex race. The top hyperscalers, funding the war from massive non-AI operating cash flows, remain last.

The asymmetry between the two games is central. Oligopolistic competition in chips resolves toward *overcapacity and price collapse*. The war of attrition in datacenters resolves toward *capacity consolidation and concentration*. If, as Framework II holds, the binding constraint is migrating toward the datacenter layer, the attrition survivors inherit precisely the scarce asset — energized, permitted, contracted capacity — at the moment it becomes the bottleneck. The more rivals exit, the larger the survivor's premium.

## 4.5 The self-defeating loop: expensive picks bankrupt the miners

Combining the three frameworks exposes a reflexive loop. The higher the chip supplier's margins, the faster the datacenter layer's cash depletes; the faster that cash depletes, the sooner attrition-tier players fold and absorption capacity $A_{DC}$ decelerates; the slower absorption grows, the sooner chip flow crosses it and the upstream glut begins. The chip industry, locked by its own game theory into expansion, is in effect financing its future overcapacity by exhausting its customers' balance sheets. Sell the picks too dear, and the miners go broke; when the miners go broke, pick demand evaporates.

The clearest evidence that the upstream is aware of this loop is the emergence of vendor support and overlapping supplier–shareholder–customer structures — chip suppliers taking equity stakes in their cloud customers or committing to purchase capacity from them. The current cycle already provides a disclosed example: NVIDIA is simultaneously CoreWeave's GPU supplier, a shareholder, and — under a 2025 agreement — obligated to purchase up to $6.3 billion of CoreWeave's unsold cloud capacity through 2032, while CoreWeave's borrowing capacity is itself tied to the depreciated value of its GPU collateral (CoreWeave 2025a, 2025b). Economically, vendor support of this kind is a partial refund of the rent: an attempt by the upstream to relax its customers' capital constraint and keep the game going. It is also a confession, because it converts income-statement exposure to its weakest customers' demand into balance-sheet and contractual exposure to their survival.

## 4.6 Precedent: telecom, 1999–2001

The pattern has precedent. In the telecom bubble, equipment vendors were the picks-and-shovels rent collectors, and carriers were the capex-burning stock builders racing to lay fiber. The equipment vendors of that cycle occupy the position NVIDIA occupies in this one: the rent-collecting systems supplier that ends up financing its own customers' capacity race. As carrier cash depleted, vendors extended aggressive financing to sustain their own order books — Nortel's customer-financing commitments alone exceeded $5 billion in 2000, against which it took large provisions as customers failed (Nortel Networks 2002). When the carriers' war of attrition produced cascading exits, equipment demand did not decline; it evaporated, and the vendors, holding receivables tied to failed customers, fell 80 to 95 percent from their peaks. Two features of the episode carry directly into the present cycle. First, *credit indicators cracked before volume indicators did*: junk-bond spreads had widened by more than 300 basis points between early 2000 and mid-2001 (Federal Reserve Bank of San Francisco 2001) while equipment order books still appeared record-strong. Second, capacity built in the bubble did not disappear with its builders — the fiber glut persisted for years, and its cheap capacity became the substrate on which a new generation of companies was built. One feature does *not* carry over, and Section 8.2 develops it: the carriers of 1999 faced no constraint on laying fiber comparable to the power and site constraints that bound the datacenter layer today, so both layers of the telecom chain ended in overcapacity together.

---

# 5. The Integrated Model — Two Terminal Mechanisms, One Accelerant

The three frameworks converge into a single statement about how this cycle ends. The peak of the AI hardware cycle will be set not by the peak of AI demand but by whichever of two terminal mechanisms arrives first — a turn in the demand derivative, or a crossing of chip output and datacenter absorption capacity. A third condition, a credit crack in the attrition tier, is not a separate ending but an accelerant that can pull the crossing forward. The three are distinct in what they look like and causally linked in how they operate:

**Trigger 1 — the demand derivative (Framework I).** End-demand growth decelerates as adoption passes its inflection point; the second derivative turns negative; new-capacity chip demand contracts in absolute terms while headline usage still sets records.

**Trigger 2 — the physical crossing (Framework II).** Cumulative fab output capability, compounding quarter by quarter, overtakes the datacenter layer's absorption capacity, throttled by power, sites, and grid access. Chips outrun racks; inventory accumulates; price follows inventory.

**Accelerant — the credit crack (Framework III).** The attrition tier of the datacenter market loses access to capital — spreads widen, collateral terms tighten, a marquee casualty resets risk appetite — and absorption capacity contracts discontinuously rather than smoothly, dragging the crossing of Trigger 2 forward. This is the mechanism by which the cycle can end well before end demand decelerates.

The coupling runs in one principal direction: expensive chips accelerate customer cash depletion (the accelerant), which slows absorption (Trigger 2), which can force the glut before demand ever decelerates (Trigger 1). The peak they jointly determine is the peak of the accelerator flow — the flow that NVIDIA and its captive competitors supply to the datacenter stock. Memory's cycle is derived from that flow, not independent of it, and is treated accordingly as an additional consideration in Chapter 7. A rigorous formulation of the inversion thesis therefore does not predict *which* mechanism ends the cycle or *when*; it specifies what each looks like in observable data and defines the response in advance. Chapter 9 develops that framework.

---

# 6. Case Study — The Datacenter–NVIDIA Dyad

## 6.1 From uncontested supplier to contested market

The overexpansion mechanism of this report requires a supplier that can lose share, and for the first two years of the AI buildout the accelerator market had none. A single merchant designer held a share of installed compute above 70 percent, controlled allocation of a product for which no volume substitute existed, and behaved as the theory of monopoly predicts: it expanded output, but not to the point of clearing the market, and the persistent shortage that resulted expressed itself in gross margins without precedent for a merchant semiconductor supplier. That configuration is the one in which the mechanism lies dormant — the derivative of demand accrues to the dominant supplier as rent rather than as capacity risk, and no prisoner's dilemma exists because there is no one to lose share to.

The configuration has changed, and the change is measurable. Report 12 of this series estimates that NVIDIA's share of installed AI compute, in H100-equivalents, fell from roughly 71 percent at the end of 2024 to roughly 67 percent at the end of 2025 — a year in which its own installed base nearly tripled and in which it supplied roughly two-thirds of the industry's net compute additions. Share fell, that is, *despite* the most aggressive volume expansion in the company's history, which is the signature not of a monopolist rationing supply but of a competitor defending position. The share did not go to merchant rivals; AMD's share of installed compute fell over the same period. It went to hyperscalers' in-house silicon — Google's TPU line added more compute share in 2025 than any other supplier — and, inside China, to Huawei. The customers had become the competitors, and the merchant leader's response was the one Section 4.3 predicts of a firm that can now be displaced: expand capacity ahead of demand, secure foundry and packaging allocation for generations not yet shipping, and buy deployment share with volume.

That response is what activates the frameworks. A supplier that builds to defend share builds to the derivative of demand, and so inherits the derivative's volatility (Framework I); a supplier that pre-commits foundry, packaging, and memory capacity for future generations converts its cash into contractual fixed cost (Framework III); and the flow it thereby creates must be absorbed by a datacenter layer whose own expansion is constrained by power and sites (Framework II). None of these mechanisms is yet producing distress. Margins remain elevated, order books are full, and the share loss to date is a few percentage points of a very large base. The correct reading is not that the accelerator cycle has turned but that the condition for it to turn has been met: the market that was insulated by the absence of a credible substitute is no longer insulated, and the seeds of the sequence described in Chapters 2 through 5 have been planted in it.

## 6.2 The customer who becomes a competitor

The prisoner's dilemma of Framework III is usually played among sellers. In the accelerator layer it is played across the transaction: the hyperscaler that buys the merchant chip also builds its own. Google is the fullest case. Its TPU program supplies roughly three-quarters of Google's installed compute at roughly half of Google's estimated chip cost, at a cost per unit of compute that Report 12 places between a third and a fifth of the merchant equivalent depending on generation. Amazon's Trainium is the second case, supplying roughly two-fifths of Amazon's 2025 compute additions at a comparable discount. Microsoft and Meta are the control group: their in-house programs have not reached volume in the data, both remain merchant-dependent buyers, and both lost compute share in 2025 as the integrated pair gained it. AMD occupies a different position altogether — a merchant second source whose share the data show contracting — and is not the axis along which the accelerator layer is being reorganized.

The economics of the wedge determine the merchant's time horizon. A captive program does not need to match the merchant chip's performance; it needs to deliver compute at a cost per unit low enough that the hyperscaler's own workloads justify the engineering. At the cost gaps Report 12 documents, that threshold is met for the two largest buyers, and the merchant's remaining pricing power is bounded by the rate at which captive capacity can be brought up — a rate that is neither smooth nor assured, since each captive generation must clear its own design, foundry, and software transitions. The merchant's response, observed in the data, is the one Section 4.3 predicts: expand volume to hold deployment share while the price umbrella lasts. That response is rational, and it is also the mechanism by which the accelerator layer manufactures its own overshoot. Each generation the merchant ships to defend share adds to a stock whose owners are simultaneously building the means to replace it.

## 6.3 Rent without a fab — and the trap of cutting output

A fabless supplier does not undergo inversion the way a fab owner does. It holds no sunk fabrication capacity that must be run at marginal cost, so a demand deceleration does not force it to sell into a collapsing price; it can cut wafer orders. Its inversion takes three other forms. The first is margin compression: the rent of Section 3.4, accrued as gross margin far above any merchant-semiconductor norm, is the quantity that falls as scarcity ends, and it can fall a long way before unit price does. The second is volume displacement, as captive programs absorb growth the merchant would otherwise have shipped. The third is inventory: when end demand decelerated in 2022, NVIDIA recorded inventory and purchase-commitment charges exceeding $1 billion in a single quarter as product built for one demand level met another (NVIDIA Corporation 2022). Together these are what the derivative looks like on a fabless income statement — no marginal-cost floor, but no marginal-cost shelter either.

The obvious defense is the one available only to a fabless supplier: cut orders and protect price. That defense is a trap, for a reason that follows directly from Framework II. Leading-edge foundry and advanced-packaging capacity is a self-resolving constraint whose flow, once created, persists. If the merchant reduces its draw on that capacity, the capacity does not disappear; it becomes available — and, in a downturn, cheaply available — to the foundry's other customers, who include the very captive programs displacing the merchant. The survivor's premium of Section 4.4 — the winner acquires the loser's capacity at distressed prices — would in that case be realized against the merchant rather than for it. Rationing therefore buys price at the cost of ceding the manufacturing base that captive silicon needs in order to scale; it converts a volume problem into a structural one. The foundry itself, with a diversified customer base and a monopoly at the leading edge, is the party least exposed to the sequence: it fills the capacity with whichever customer is growing. The prisoner's dilemma of Section 4.3 does not bind on a single dominant foundry. It binds on the merchant designer whose customers hold the option to leave.

## 6.4 Circular financing and the credit channel

The credit accelerant of Chapter 5 reaches the merchant directly. The structures described in Section 4.5 — equity stakes in neocloud customers and commitments to purchase their unsold capacity — expose the merchant's balance sheet and contractual obligations to the attrition tier's survival, in addition to its income statement's exposure to that tier's demand. When the neoclouds' credit cracks, the merchant absorbs the impact on both sides: demand from the weakest customers evaporates, and the value of the equity and the utility of the capacity commitments deteriorate with them. This is the position the telecom equipment vendors occupied in 2000 (Section 4.6), and the sequence there is the one to expect here: credit indicators deteriorate first, order books remain record-strong until they do not, and the vendor's provisions arrive after the customer's failure rather than before it. The datacenter–NVIDIA dyad is, in this respect, not a supplier–customer relationship at all but a shared exposure to one capital cycle, in which the supplier has elected to hold the customer's risk in order to keep the customer buying.

---

# 7. Additional Consideration — Memory

## 7.1 Why memory, and why second

Memory enters this report for two reasons, and the order matters. First, memory is the layer where the fixed-cost mechanics of Framework III bind hardest and where the contestability condition of Section 4.3 has always been satisfied. The product is close to homogeneous — DRAM of a given specification is a commodity, differentiated at the margin by qualification and packaging rather than by function. The market is a concentrated oligopoly of three profit-maximizing incumbents (Samsung Electronics, SK hynix, Micron) of comparable capability, small enough for game-theoretic interaction to dominate outcomes and cash-rich enough that none faces a financing constraint: in the tightest tier, multi-year take-or-pay agreements with substantial customer deposits mean cash arrives before production — Micron alone discloses roughly $22 billion of expected deposits and financing commitments under such contracts (Micron Technology 2026a). And the cost structure is the fixed-cost-dominant one analyzed in Section 4.2, whose operating leverage makes memory among the most cyclical of all manufacturing industries. Second, memory is the largest single cost the accelerator layer passes through to the datacenter: with high-bandwidth memory bundled onto every accelerator and memory now a material share of a high-end system's price, memory pricing is a second-order channel into the datacenter's capex efficiency and hence into the demand path of Framework I.

What memory is not is an independent cycle. Its AI demand is derived from the accelerator flow analyzed in Chapter 6, and its trajectory is ultimately bounded by that flow, even if rising memory content allows memory demand to peak later. The sections that follow develop the memory-specific structure — the accelerator race as demand amplifier, the fourth player, the broken exit, the capacity wave now under construction — and close with the structural reason memory is nonetheless better placed than logic within the chip layer.

## 7.2 The accelerator layer as a demand amplifier

The demand reaching memory makers today is not a single customer's order book but the output of the competitive race analyzed in Chapter 6. The merchant leader faces credible volume competition from hyperscalers' in-house silicon programs, each of which procures high-bandwidth memory directly and at scale. The value chain runs in series — hyperscaler capex funds accelerator purchases or internal programs; accelerator production, merchant or captive, pulls HBM — so competition at the accelerator layer transmits directly into memory order books.

Two consequences follow. First, accelerator competition is itself a capacity race: each contender expands production to avoid ceding deployment share, and that race has materially broadened and enlarged HBM demand — a structural reason memory's pricing power has strengthened beyond what a single dominant buyer would have produced. The merchant leader's compulsion to expand volume in defense of deployment share (Section 6.2) is, seen from the memory maker's side of the transaction, simply demand: the merchant's game-theoretic bind is the memory oligopoly's order book. Second, the same linkage means memory now sits at the end of *two* stacked races — the hyperscalers' deployment race and the accelerator makers' production race — both funded from one underlying capex pool. The amplification chain of Section 2.4 acquires an extra link: when the underlying capex cycle turns, the deceleration propagates through the accelerator layer into memory with the usual derivative magnification, plus whatever double-ordering the accelerator race has injected along the way.

## 7.3 The fourth player problem: a soft budget constraint at the table

Section 4.3 observed that the financing constraint historically ended the expansion game by subtraction; in memory the record is specific. The shakeouts of 2007–2012 took the industry from eight DRAM makers to three, with Qimonda exiting in 2009 and Elpida in 2012. The 2022–23 downturn appears to tell a different story: all three surviving incumbents cut output despite the fixed-cost logic, and prices recovered within roughly eighteen months — which one reading takes as evidence that three players in a repeated game, observing each other's utilization in near real time, have learned the cooperative equilibrium that folk-theorem logic permits. The record fits independent cost-driven adjustment better than coordination. Prices in that downturn fell below full cost; SK hynix announced in late 2022 that it would cut 2023 capex by more than half and reduce output of low-margin products; Micron cut wafer starts by roughly 20 percent in November 2022; Samsung held out longest, acknowledging "production adjustment" only in 2023 after its own profits had collapsed (SK hynix 2022; Micron Technology 2022; Samsung Electronics 2023). Staggered capitulation in order of financial pain is what marginal-cost logic predicts of independent firms; it is not the synchronized restraint of a cartel. But even the strongest version of the discipline reading does not survive a change in who sits at the table.

The entry of CXMT breaks the inference, not because the table now seats four, but because the fourth player is a different *kind* of player. The characterization requires precision. CXMT is not state-controlled in the strict corporate-law sense — its 2026 listing prospectus reports no controlling shareholder or actual controller — but its largest shareholders include a Hefei municipal-government-controlled investor, the National Integrated Circuit Industry Investment Fund II, and Anhui Investment Group, and it benefits from semiconductor-specific tax and tariff incentives (CXMT 2026). "State-backed" is therefore accurate; "state-directed" is not established. What the state backing plausibly implies is a softer financing constraint (Kornai 1986) than privately financed incumbents face: capacity plans less sensitive to near-term profitability, expansion less likely to pause in downturns, and domestic-substitution policy supporting home demand. Whether CXMT would in fact hold output through a price collapse is an analytical hypothesis, not an observed fact — public evidence does not establish indifference to profit. But the game-theoretic point does not require the strong version. Repeated-game cooperation survives on the exchange of present restraint for future profits, and that exchange is degraded — even if not annihilated — by a participant whose survival does not depend on those profits. With one such participant at the table, restraint by the other three is no longer reliably cooperation; it risks being donation of share, and the incumbents must act on that risk.

The incumbents' rational response completes the mechanism. The textbook strategy against an entrant climbing a learning curve is pre-emptive expansion and price pressure — deny the entrant the volume and cash flow it needs to descend its cost curve (the entry-deterrence logic of Dixit 1980, applied dynamically). CXMT's presence thus lowers the payoff to restraint and raises the payoff to expansion for all three incumbents simultaneously. The observed result — synchronized incumbent capex into an already-hot market — is not indiscipline; it is the new equilibrium.

## 7.4 The broken exit mechanism and the bifurcation endgame

The deeper structural change is what CXMT does to the *bottom* of the cycle. Historically, the deepest memory downturns were corrected through some combination of capacity exit or ownership consolidation, utilization cuts, capex restraint, inventory normalization, and demand recovery — with the sharpest corrections resolved by the marginal producer running out of cash and ceasing to set prices independently. Qimonda's 2009 failure removed capacity outright; Elpida's 2012 bankruptcy removed a decision-maker rather than a fab, its capacity continuing under Micron's ownership. The fixed-cost structure of Section 4.2 already makes memory troughs long, because exit requires either the physical write-off of sunk capacity or the financial failure of an operator, both of which lag the onset of losses by quarters or years. A state-backed entrant weakens one of those adjustment mechanisms: the expectation that sustained losses will eventually force the marginal producer to withdraw capacity or surrender strategic autonomy. A player backed by patient state-linked capital is far less likely to fail in the relevant sense, so the capitulation mechanism — the historical floor-builder of memory cycles — is weakened, plausibly to the point of failure, for whatever share of capacity the entrant represents. This converts part of the bear case from cyclical to structural: the next trough risks being longer, not merely deeper, because glut capacity no longer exits at the bottom.

The operative precedents are not memory's own history but LCD panels and solar — two industries that ran the identical sequence of state-backed Chinese capacity entry, defensive incumbent expansion, structural price collapse in the commodity tier, and eventual full incumbent retreat from that tier (Appendix B). In LCD, the Korean leaders ultimately abandoned commodity panels entirely and retreated to premium OLED. The analogous endgame in memory is bifurcation: a legacy-node commodity tier progressively ceded to the entrant, and a premium tier — HBM and leading-edge nodes — defended behind qualification, packaging (TSV), and customer-integration barriers. The strategic problem with the retreat is that all three incumbents retreat to the *same* refuge, concentrating their combined capacity in the premium tier and accelerating its commoditization. Retreat shrinks the shelter.

The bifurcation is already visible in the incumbents' own reallocation. CXMT's prospectus states that it ceased producing DDR4 from the end of 2024 as it migrated to DDR5 (CXMT 2026), and the incumbents accelerated their own DDR4 end-of-life and moved capacity toward HBM and DDR5 — a reallocation that absorbs disproportionate wafer capacity for the bits it yields, for reasons developed in Section 7.5. Whatever its proximate trigger, that reallocation is a preview of the endgame: retreat from a commodity tier judged structurally indefensible into a premium tier that all three are entering at once.

## 7.5 The 2026–28 capacity ramp — and why memory is still better placed than logic

Three incumbents contesting share, none financially constrained, and a fourth player whose presence raises the payoff to expansion for all of them (Section 7.3) produce the outcome Section 4.3 predicts: synchronized, very large capacity commitment. The multi-year programs announced in 2026 — Samsung's KRW 2,655 trillion of long-term domestic investment, of which KRW 2,030 trillion relates to semiconductor clusters, and SK hynix's KRW 1,100 trillion mid-to-long-term strategy (Samsung Electronics 2026; SK hynix 2026) — cover different scopes and horizons and are not additive, but their order of magnitude is the point. The disclosed schedules cluster, though they mark different stages of the same process: Samsung's Pyeongtaek P4 points to a phased ramp already beginning in 2026 while P5 targets operation in 2028; SK hynix's first Yongin cleanroom is scheduled to open in February 2027, with M15X producing DRAM earlier; Micron's Idaho fabs target first wafer output in mid-2027 (ID1) and late 2028 (ID2); and CXMT's disclosed equipment installation and process-upgrade projects run through 2026–28 (Samsung C&T Corporation 2022; Seoul Economic Daily 2026; SK hynix 2025, 2024; Micron Technology 2026b; CXMT 2026). These are milestones rather than volume output — cleanroom openings, first wafers, and qualified volume are separated by tooling, yield ramps, and customer qualification, and the pace of tooling is governed by the equipment suppliers upstream (Section 3.1). But the direction is unambiguous: material capacity additions, committed by four players each seeking share from the others, begin to arrive across 2027–28, although the timing of qualified volume will vary substantially by site. This report makes no claim about whether demand will have decelerated by then. It observes that one of the two curves in Framework II's min-function is, for memory, already visible.

Against that supply risk stands a structural asymmetry that favors memory over logic, and it deserves stating carefully because it is the reason memory's position within the chip layer is stronger than its cyclical history suggests. Memory and logic are complements: an accelerator's transistors are useful only in proportion to the bytes they can address at speed, so as logic transistor counts grow, memory bit counts must grow with them. The two do not, however, grow the same way, and the decisive fact is that their relative order has reversed. For most of the industry's history DRAM was the *faster* scaler, doubling bit density roughly every eighteen months against logic's twenty-four, which is what made memory a relentlessly deflationary commodity. That is no longer true. DRAM bits per chip grew at roughly 45 percent a year through the early 2000s but slowed to roughly 20 percent a year through the 16-gigabit generation that reached volume in 2016, while leading-edge logic in the same window continued to compound at rates above 40 percent a year (Semiconductor Digest 2020, reporting IC Insights data); a survey of five decades of shipped DRAM finds the exponential growth rate of per-chip capacity falling by roughly a fifth between 1970–2000 and 2000–2020, with the deceleration concentrated after 2010 (Patel et al. 2024); and industry analysis puts DRAM's density gain over the most recent decade at roughly a doubling, against more than a hundredfold per decade in its scaling era, even as cost per transistor has continued to fall at the leading foundry nodes (SemiAnalysis 2026). The physical cause is well understood: the storage capacitor cannot shrink at the pace of a logic transistor without losing the charge it must hold. The consequence is that the gap between what logic requires and what memory density supplies widens with every generation — a divergence visible at the system level, where peak compute has scaled roughly 3.0× every two years over the past two decades while DRAM bandwidth has scaled only 1.6× (Gholami et al. 2024).

The gap must be filled with silicon. When bit density lags the growth in bytes an accelerator requires, the shortfall is made up by building more of it — more dies per stack, more stacks per package — which is why the memory content of a flagship accelerator has more than doubled across the last two generations. A second penalty compounds the first, and it is specific to high-bandwidth memory. HBM does not merely use more area for more bits; it yields fewer usable bits from the area it uses. Through-silicon vias and the wide interface they serve consume die area that stores nothing, the base die and thicker peripheral circuitry add further overhead, and stacking eight or twelve dies imposes compounding yield loss on a product that must be assembled from known-good die. The result is that producing a given quantity of bits in HBM form consumes materially more wafer capacity than producing the same bits as commodity DRAM. The figure most often cited for this penalty is roughly three to one for HBM3E against DDR5 on the same node (Micron Technology 2024); industry-wide estimates imply a somewhat lower but comparable ratio, and, more importantly, a persistent one. TrendForce estimates that among the three incumbents HBM will absorb approximately 18, 22, and 30 percent of total DRAM wafer input by the end of 2025, 2026, and 2027, while yielding only about 8, 9, and 13 percent of total DRAM bit supply (TrendForce 2026). Two things follow from those pairs. The penalty is not a transitional yield problem that learning will retire: the implied wafer-to-bit ratio holds near two and a half across all three years, because each generation's larger die and taller stack consume whatever manufacturing learning the previous one delivered. And the crowding-out is severe: by 2027 roughly a third of the industry's wafer capacity will be producing about an eighth of its bits, so total DRAM bit supply grows substantially more slowly than wafer capacity does — capital buys conversion and process upgrades before it buys bits. This is where the asymmetry becomes a supply constraint rather than an engineering inconvenience. The difference is one of degree, but a large one. A logic producer can obtain a substantial share of its compute-density growth through node migration, tool conversion, and productivity gains within existing facilities — leading-edge logic builds new fabs too, and on an enormous scale, but each new node delivers a meaningful density gain on every wafer processed. A memory producer, because bit-density scaling is slower and HBM is wafer-intensive, must rely far more heavily on incremental wafer starts and the cleanroom additions that house them. New fab capacity carries a lead time measured in years, is rationed by the equipment and materials oligopoly upstream, and can be committed only in large indivisible increments. Memory supply therefore expands more slowly than logic supply even when both industries are investing at the limit of their ability, and the difference is structural, not cyclical. In a system whose two components must grow together, the component that grows more slowly is the recurring bottleneck, and the rent of Section 3.4 accrues to it. That is the mechanism behind the present episode: companies building servers under contract for the largest datacenter operators have reportedly notified their customers that prices for systems containing NVIDIA accelerators will rise by more than 15 percent in many cases, with soaring memory costs cited as the driver (Bloomberg 2026), and device makers with the strongest purchasing power in the industry have described the memory price rise as without precedent in their experience (CNBC 2026). Within the datacenter's dollar, the split is moving from the accelerator designer toward the memory maker because memory supply tends to lag the growth of leading-edge compute, making it a recurring candidate for bottleneck status.

The asymmetry has a ceiling. Memory's advantage over logic is an advantage in the *division* of the datacenter's dollar, not in whether that dollar keeps growing. High-bandwidth memory has no AI demand of its own; it is bundled onto the accelerator, qualified per accelerator generation, and sold into the same flow whether the accelerator is merchant or captive. Whichever mechanism of Chapter 5 ends the cycle, the accelerator flow's peak is the memory flow's peak with a lag — a lag that rising memory content per unit of compute lengthens and softens, but does not remove. If the accelerator layer peaks first, HBM demand falls with it, and the memory maker's leverage becomes the leverage of a supplier whose customer has stopped growing. If the capacity ramp were instead to run ahead of accelerator demand, the consequence would be lower system costs and a wider merchant margin, not a change in the cycle's shape. Memory is better placed than logic within the chip layer; the chip layer as a whole is still governed by the dyad of Chapter 6.

---

# 8. Stress-Testing the Inversion Thesis

A thesis is only as robust as its treatment of the arguments against it. This chapter subjects the inversion thesis to its three strongest objections and states what survives each.

## 8.1 Test 1 — Could the merchant leader restore an uncontested position?

The overexpansion mechanism operates on the accelerator market only because its leading supplier can now be displaced (Section 6.1). The first objection is that the displacement may prove temporary: captive silicon programs are large engineering undertakings that must clear design, foundry, packaging, and software transitions at every generation, and a stumble at any of them returns the marginal workload to the merchant. If the hyperscalers' programs stall, the merchant's share loss reverses, its behavior reverts from share defense to output discipline, and the mechanism returns to dormancy — the shortage persists, the margin rises, and the inversion is deferred indefinitely.

The objection identifies a real path, and the thesis must carry it as a condition. Three considerations bound its probability. First, the displacement to date has come from the two buyers with the deepest engineering resources and the largest internal workloads, and for both the cost gap documented in Report 12 is wide enough that a generation's delay changes the timing of substitution, not its economics. Second, the merchant's own response — pre-committing foundry, packaging, and memory capacity for future generations — is now a sunk position that is rational only if the market remains contested; a merchant that expected to face no substitute would ration, not expand. Its capacity behavior is the market's own assessment that the door will not close. Third, the software barrier that historically protected the merchant's platform is the object of sustained, well-funded engineering by the same buyers, and each captive generation that reaches volume lowers it further. *Verdict: re-monopolization would suspend the thesis rather than refute it, and it is the principal accelerator-side condition to monitor; the evidence weighs against it, but the test is observable — a reversal of the captive share of accelerator flow for more than a transitional period.*

## 8.2 Test 2 — Could the datacenter layer overbuild, as the carriers did?

The telecom precedent of Section 4.6 ended with overcapacity on both sides of the transaction: the equipment vendors collapsed, but so did the carriers, because fiber could be laid faster than demand could fill it and nothing in the carriers' environment stopped them. If the datacenter layer can overbuild in the same way, the survivor's premium of Section 4.4 is illusory — the survivors inherit a glutted asset, cheap compute lowers the barrier to entry, and the lasting beneficiaries are new entrants building on distressed capacity, as the search engines and streaming platforms did on fiber priced at cents on the dollar.

The precedent does not transfer, and the reason is Framework II. The carriers of 1999 faced no power, grid, or siting constraint on their expansion; the binding constraint on fiber deployment was capital, and capital was abundant until it was not. The datacenter layer today expands against constraints that capital cannot relieve on any relevant horizon — interconnection queues of five years and more, multi-year backlogs for turbines and transformers, permitting and community resistance that tighten as density rises (Section 3.3). An industry that cannot obtain power and sites fast enough to absorb the chips it is offered cannot overbuild; its problem is the opposite one. The consequence for the cycle is asymmetric and specific: because the datacenter layer's capacity is constrained, the upstream chip layer — whose fabs, once built, produce regardless — meets oversupply first and alone. The glut forms in silicon inventory between delivery and energization rather than in empty datacenters, so the first and sharpest price adjustment is likely to occur in the chip layer, while continued high utilization of energized capacity protects the datacenter layer. The survivors of the attrition war inherit an asset that remains scarce precisely because it could not be overbuilt. *Verdict: the telecom outcome is the one the datacenter layer would face if its physical constraints relaxed; so long as they bind, the datacenter layer is protected from overcapacity and the chip layer is exposed to it alone. The market-power leg of the thesis is conditional on those constraints, and should be stated as such.*

## 8.3 Test 3 — Could cheaper compute expand demand enough to absorb the glut?

The last objection is the Jevons (1865) dynamic: if the price of compute falls far enough, demand may expand enough to absorb the new supply — efficiency gains raising rather than lowering total consumption, and shifting the saturation ceiling $L$ of Framework I upward mid-flight. If the effect is strong enough, the deceleration the frameworks await never arrives and the thesis is wrong rather than early.

The objection presumes that a collapse in chip prices reaches the end user as a collapse in the price of compute. In this cycle it largely will not, for the reason established in Test 2. The price the end user pays is the price of *datacenter* capacity — energized, operating compute — and that price is set by the constrained layer, not the glutted one. When chips are abundant and racks are scarce, the chip price collapses while the rental price of installed capacity falls only as fast as the constrained layer's own costs improve, which is to say gradually, at roughly the pace of technological progress. The Jevons effect requires a large price decline at the point of consumption; a large price decline at a point upstream of the bottleneck is captured as margin by the bottleneck's owner and never reaches the consumer. And even if it did, the constrained layer could not expand supply to meet the induced demand — the whole premise of Framework II is that it cannot. *Verdict: a strong Jevons effect is possible only in the regime in which Framework II fails and datacenter capacity becomes abundant; in the regime the thesis describes, cheap chips produce fat datacenter margins, not a demand explosion. The demand-side escape is therefore not independent of the physical-constraint condition already carried under Test 2.*

## 8.4 What survives

Three conditions govern the thesis, and each is observable. First, the accelerator market must remain contested: so long as captive silicon can take share from the merchant leader, the merchant builds to demand rather than rationing it, and the frameworks operate; a durable reversal of the captive share of accelerator flow would suspend them. Second, the datacenter layer must remain physically constrained: so long as power and sites cannot be obtained as fast as chips can be produced, the glut forms in the chip layer alone, the datacenter layer cannot overbuild, and the survivors' asset remains scarce; a relaxation of those constraints faster than fab output compounds would return the cycle to the telecom pattern in which both layers collapse together. Third — and following from the second — cheap chips must not translate into cheap compute at the point of use; so long as the bottleneck captures the price decline as margin, no Jevons expansion of demand rescues the chip layer.

Under those conditions the thesis is this. *The rent of the AI buildout sits today with the chip suppliers because they own the binding constraint. That constraint is migrating downstream toward power and sites, and the merchant accelerator leader — now defending share rather than rationing output — is building the very capacity that will cross the datacenter layer's ability to absorb it. When the crossing comes, the chip layer meets oversupply alone: the fabless leader through margin compression, displacement by captive silicon, and inventory adjustment; the memory oligopoly, later and more gently, through the commodity price mechanics of a fixed-cost industry whose traditional exit mechanism has been weakened by the presence of a state-backed fourth player. The datacenter survivors inherit an asset that remained scarce because it could not be overbuilt. The report does not say when. It says in what order, and by what signs.*

---

# 9. Monitoring and Implications — A Conditional Rotation, Not a Timing Call

## 9.1 Why timing is unknowable

The frameworks predict sequence, not timing, and this limitation is inherent to the problem rather than a matter of analytical incompleteness. The decisive variable — the economy's current position on the AI adoption S-curve — is unobservable in real time: penetration of a market whose eventual size is itself the unknown $L$ cannot be measured, and the second derivative of demand, the quantity on which everything turns, is identifiable in the data only after several periods of confirmation, by which point the turn is history. Every prior cycle teaches the same lesson in both directions: warnings of telecom overcapacity began in 1997, three years and several hundred percent of equipment-stock appreciation before the peak. In markets, early and wrong are indistinguishable at the position level. The correct response to an unknowable date is not a braver forecast; it is a framework in which the *triggers* are specified in advance and the response is conditional on observing them.

## 9.2 The leading-indicator dashboard

Each framework nominates its own observables, organized here from upstream cause to downstream confirmation.

| Framework | Indicator | What it signals |
|---|---|---|
| Contestability | Captive vs. merchant share of accelerator flow, quarter by quarter, measured over more than one generation transition | Whether the accelerator market remains contested; a durable reversal toward the merchant would suspend the overexpansion mechanism (Test 1) |
| I. Demand derivative | Hyperscaler capex guidance — *revisions and second differences*, not levels | The earliest readable proxy for $d^2Y/dt^2$; watch for deceleration in the growth of guided capex |
| I. Demand derivative | Rental price of installed accelerator capacity vs. chip price | Whether chip-price declines are reaching the point of use (Jevons channel open) or being captured as datacenter margin (Test 3) |
| I / Case study | Merchant supplier's inventory and purchase commitments relative to revenue | The fabless form of overcapacity; commitments rising against decelerating orders preceded the 2022 charges |
| II. Physical crossing | Power contracting (PPA signings, grid-interconnection queue movement) vs. fab ramp schedules | The relative slope of $A_{DC}$ and $F_{semi}$; the gap is the countdown to crossing |
| II. Physical crossing | Turbine, transformer, and switchgear backlogs | Depth of the self-intensifying constraint; a rapid clearing would open the telecom path (Test 2) |
| II. Physical crossing | "Chips awaiting racks" — accelerator inventory accumulating between delivery and energization | The most direct evidence the crossing has occurred |
| II / Case study | Leading-edge foundry and advanced-packaging utilization and customer mix | Whether capacity released by the merchant flows to captive programs (the trap of Section 6.3) |
| III. Credit | Credit spreads and collateral terms in the neocloud tier (LTVs, rates on chip-collateralized debt) | Health of the attrition front line; cracked credit preceded cracked volume in 2000 |
| III. Credit | Vendor support and circular supplier–shareholder–customer deal volume | The upstream's own assessment of its customers' capital constraint |
| III. Credit | The *order* of capex guidance cuts (weakest balance sheets first) | Onset of attrition exits |
| Memory (Ch. 7) | HBM contract pricing and memory's share of accelerator system cost | Memory's leverage over the accelerator layer; a reversal marks the unwinding of the redistribution |
| Memory (Ch. 7) | Equipment orders at newly constructed shells across the four players | The 2026–28 capacity ramp — tools, not groundbreakings, are the commitment |

## 9.3 Trigger-based rotation design

The payoff structure of the inversion thesis punishes early execution on both legs. Exiting the merchant accelerator leader before the peak forfeits what is historically the steepest portion of the up-cycle — late-stage scarcity pricing — while rotating into datacenter operators early means holding maximum free-cash-flow compression and headline risk through the very period the attrition narrative is loudest. The thesis is therefore implementable only as a *conditional* rotation: positioning changes are bound, in advance, to dashboard triggers rather than to calendar views or valuation discomfort. In schematic form: a sustained captive share of accelerator flow, merchant inventory and purchase commitments rising against decelerating orders, a widening gap between chip prices and rental prices for installed capacity, and the first credit deterioration in the neocloud tier together constitute the rotation signal away from accelerator-cycle exposure — and, because memory demand is derived from that flow, the same signal governs memory exposure with a lag. Confirmation of the physical crossing (inventory between delivery and energization) and the onset of ordered capex cuts constitute the signal that the survivor's-premium phase — long the consolidating balance sheets, long the power-and-sites complex of Framework II — has begun.

Equally important is specifying falsification. The thesis is suspended if the accelerator market ceases to be contested — a durable reversal of captive silicon's share of flow, with the merchant leader reverting from expansion to rationing (a return to uncontested supply). It is wrong, not early, if power and site constraints relax faster than fab output compounds, so that the datacenter layer can overbuild and chip-price declines reach the end user (the telecom regime, in which the Jevons channel reopens). A reader who tracks the dashboard is positioned to recognize either within quarters rather than years. What the reader should not expect is a signal that the thesis is *early*: the report's own framework holds that the inflection is invisible until it has passed, and a thesis about medium-to-long-term sequence cannot be falsified by a near-term calendar.

This report is an analytical framework, not investment advice; position sizing, instruments, and suitability are the reader's own determination.

---

# Appendix A — Mathematical Formulation

**Adoption.** End demand follows a logistic path $Y(t) = L / (1 + e^{-r(t - t_0)})$ with ceiling $L$, speed $r$, inflection $t_0$. Its derivative $dY/dt = rL e^{-r(t-t_0)} / (1 + e^{-r(t-t_0)})^2$ is the logistic density: bell-shaped, peaking at $t_0$ (50 percent of ceiling), with value $rL/4$ at peak. The second derivative changes sign at $t_0$; new-capacity demand contracts thereafter while $Y$ continues rising toward $L$. The Bass (1969) diffusion model yields qualitatively identical flow dynamics with an asymmetric bell.

**Derived demand.** With target capacity $K^* = vY$ and depreciation $\delta$, chip demand is $D_{semi} = v\,dY/dt + \delta K$. Since $v\,dY/dt \approx vgY$, growth deceleration in $Y$ from $g_1$ to $g_2$ scales the first term by approximately $g_2/g_1$ *holding $Y$ approximately constant*; across consecutive periods the growing base $Y$ partially offsets the lower rate, so the realized contraction is $1 - (g_2/g_1)(1+g_1)$ — still an absolute contraction requiring no decline in $Y$ whenever $g_2(1+g_1) < g_1$. The replacement floor $\delta K$ rises with the installed stock and with shorter accelerator lifetimes (higher $\delta$).

**Effective supply.** Installed AI compute grows as $dK_{AI}/dt = \min(F_{semi}, A_{DC})$, where $F_{semi}$ rises over multi-year horizons with cumulative fab completions (subject to utilization, node transitions, and retirements, so not strictly monotonic) and $A_{DC}$ is constrained by the annual flow of newly energized capacity, itself a function of power, sites, and capital-market conditions. Inventory accumulates at rate $F_{semi} - A_{DC}$ whenever positive; price adjusts to inventory with the usual commodity dynamics, floored in the short run at marginal cost given the fixed-cost-dominant structure.

**Cost structure and cyclical amplitude.** With total cost $TC(Q) = F + V(Q)$, where $F$ is fixed and sunk and $V(Q)$ variable, a profit-maximizing producer chooses output where $P = MC(Q) = V'(Q)$ and supplies wherever $P > MC$. Because $MC$ is low relative to average total cost $ATC(Q) = TC(Q)/Q$ when $F$ is large, output is supplied at prices far below full cost; the producer records an accounting loss whenever $P < ATC$, a region that widens with the fixed-cost share $F/TC$. Operating leverage — the elasticity of operating profit to revenue — rises with the same ratio, so a high-$F$ industry such as semiconductor fabrication exhibits both a wider loss region (deeper, longer troughs before price falls to the marginal-cost floor and output is withheld) and larger margin swings per unit change in price or volume than a variable-cost-dominant manufacturing sector, in which $MC$ and $ATC$ lie close together.

---

# Appendix B — Historical Analogue Table

| Episode | Picks-and-shovels layer | Stock-building layer | What mapped | What did not |
|---|---|---|---|---|
| Railroads, 1870s–1890s | Rail, steel, construction | Railroad operators | Derivative demand; overbuild; bondholder losses; consolidation of survivors | Land grants distorted entry; no oligopoly discipline anywhere |
| Telecom, 1999–2001 | Equipment vendors | Carriers | Vendor financing as confession; credit cracked before volume; glut persisted post-exit | Glutted asset (fiber) was itself the bottleneck asset — benefits flowed to new entrants, not survivors |
| LCD panels, 2000s–2010s | Equipment, glass | Panel makers | State-backed entrant; broken exit mechanism; incumbent retreat to premium tier | Demand was mature, not on an early S-curve |
| Solar, 2005–2013 | Polysilicon, equipment | Module makers | Soft budget constraints; structural price collapse; western exit | Policy-driven demand; no premium-tier refuge existed |
| Memory, 2007–2012 | — | DRAM makers (8 → 3) | Prisoner's dilemma; exit and ownership consolidation restored discipline — Qimonda removed capacity, Elpida's capacity was consolidated under Micron | Loss-driven withdrawal of independent decision-makers functioned — the feature now weakened |

---

# References

Bass, F. M. (1969). "A New Product Growth Model for Consumer Durables." *Management Science*, 15(5), 215–227.

Clark, J. M. (1917). "Business Acceleration and the Law of Demand: A Technical Factor in Economic Cycles." *Journal of Political Economy*, 25(3), 217–235. https://www.journals.uchicago.edu/doi/abs/10.1086/252958

Dixit, A. (1980). "The Role of Investment in Entry-Deterrence." *The Economic Journal*, 90(357), 95–106.

Forrester, J. W. (1961). *Industrial Dynamics.* MIT Press.

Gholami, A., Yao, Z., Kim, S., Hooper, C., Mahoney, M. W., & Keutzer, K. (2024). "AI and Memory Wall." *IEEE Micro*, 44(3), 33–39. https://doi.org/10.1109/MM.2024.3373763

Goldratt, E. M., & Cox, J. (1984). *The Goal: A Process of Ongoing Improvement.* North River Press.

Jevons, W. S. (1865). *The Coal Question: An Inquiry Concerning the Progress of the Nation, and the Probable Exhaustion of Our Coal-Mines.* Macmillan.

Kornai, J. (1986). "The Soft Budget Constraint." *Kyklos*, 39(1), 3–30.

Lee, H. L., Padmanabhan, V., & Whang, S. (1997). "The Bullwhip Effect in Supply Chains." *Sloan Management Review*, 38(3), 93–102.

Maynard Smith, J. (1974). "The Theory of Games and the Evolution of Animal Conflicts." *Journal of Theoretical Biology*, 47(1), 209–221.

Patel, M., Shahroodi, T., Manglik, A., Yağlıkçı, A. G., Olgun, A., Luo, H., & Mutlu, O. (2024). "Rethinking the Producer-Consumer Relationship in Modern DRAM-Based Systems." arXiv:2401.16279. https://arxiv.org/abs/2401.16279

Rogers, E. M. (2003). *Diffusion of Innovations* (5th ed.). Free Press.

Samuelson, P. A. (1939). "Interactions between the Multiplier Analysis and the Principle of Acceleration." *The Review of Economics and Statistics*, 21(2), 75–78.

Wright, T. P. (1936). "Factors Affecting the Cost of Airplanes." *Journal of the Aeronautical Sciences*, 3(4), 122–128.

## Primary sources and industry data — company filings, disclosures, and trade analysis

ASML. (n.d.). *Customer support: Installed base management*. https://www.asml.com/en/en/products/customer-support

Bloomberg. (2026, August 22). *Nvidia customers notified about AI-related price hikes above 15%*. https://www.bloomberg.com/news/articles/2026-08-22/nvidia-customers-notified-about-ai-related-price-hikes-above-15

CNBC. (2026, June 27). *The memory shortage shaking Apple and Microsoft is 'existential crisis' for smaller players*. https://www.cnbc.com/2026/06/27/memory-crunch-shaking-apple-and-microsoft-existential-for-small-guys.html

CoreWeave, Inc. (2025a). *Quarterly report (Form 10-Q) for the quarter ended September 30, 2025*. U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/1769628/000176962825000062/crwv-20250930.htm

CoreWeave, Inc. (2025b). *Current report (Form 8-K): Master services agreement and order form with NVIDIA Corporation*. U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm

CXMT (ChangXin Memory Technologies, Inc.). (2026). *Initial public offering prospectus*. Shanghai Stock Exchange. https://static.sse.com.cn/stock/disclosure/announcement/c/202605/002170_20260527_23QQ.pdf

Federal Reserve Bank of San Francisco. (2001). *Rising junk bond yields: Liquidity or credit concerns?* (FRBSF Economic Letter 2001-33). https://www.frbsf.org/research-and-insights/publications/economic-letter/2001/11/rising-junk-bond-yields-liquidity-or-credit-concerns/

Intel Corporation. (2026). *2025 annual report (Form 10-K): Property, plant and equipment disclosures*. https://www.intc.com/filings-reports/all-sec-filings/xbrl_doc_only/4133

International Energy Agency [IEA]. (2025). *Energy and AI* (World Energy Outlook Special Report), chapter: AI and energy security. https://www.iea.org/reports/energy-and-ai/ai-and-energy-security

Lawrence Berkeley National Laboratory. (2024). *Queued up: 2024 edition — Characteristics of power plants seeking transmission interconnection*. https://emp.lbl.gov/publications/queued-2024-edition-characteristics

Micron Technology, Inc. (2022, November 16). *Micron announces supply reduction* [Press release]. https://investors.micron.com/node/44261

Micron Technology, Inc. (2024). *Fiscal Q3 2024 investor presentation*. https://investors.micron.com/static-files/a531c7f0-fca2-48f3-8f24-79c945aaa2d2

Micron Technology, Inc. (2026a). *Quarterly report (Form 10-Q) for the quarter ended May 28, 2026*. U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm

Micron Technology, Inc. (2026b). *Fiscal Q3 2026 investor presentation*. https://investors.micron.com/static-files/2354ecda-77a0-4ddd-8462-a631eb491356

Nortel Networks Corporation. (2002). *Annual report (Form 10-K) for fiscal year 2001*. U.S. Securities and Exchange Commission. https://www.sec.gov/Archives/edgar/data/72911/000113031902000168/t06646e10-k.htm

NVIDIA Corporation. (2022, August 24). *NVIDIA announces financial results for second quarter fiscal 2023* [Press release]. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2023

Samsung C&T Corporation. (2022, September 22). *P4-PJT FAB building construction work contract* [Disclosure]. https://www.samsungcnt.com/eng/ir/disclosure/view.do?seq=517

Samsung Electronics. (2023). *Samsung Electronics announces third quarter 2023 results* [Press release]. https://news.samsung.com/global/samsung-electronics-announces-third-quarter-2023-results

Samsung Electronics. (2026). *삼성, 미래 성장 위해 2,655조원 투자* [Press release]. Samsung Newsroom. https://news.samsung.com/kr/%EC%82%BC%EC%84%B1-%EB%AF%B8%EB%9E%98-%EC%84%B1%EC%9E%A5-%EC%9C%84%ED%95%B4-2655%EC%A1%B0%EC%9B%90-%ED%88%AC%EC%9E%90

SemiAnalysis. (2026, March 24). *The memory wall: Past, present, and future of DRAM*. https://newsletter.semianalysis.com/p/the-memory-wall

Semiconductor Digest. (2020, March 10). *Transistor count trends continue to track with Moore's Law* (reporting IC Insights data). https://www.semiconductor-digest.com/transistor-count-trends-continue-to-track-with-moores-law/

Seoul Economic Daily. (2026, April 22). *Samsung accelerates P4 line: Mass production moved up by six months*. https://en.sedaily.com/finance/2026/04/22/samsung-accelerates-p4-fab-advances-full-production-by-six

SK hynix. (2022). *SK hynix reports third quarter 2022 results* [Press release]. https://news.skhynix.com/sk-hynix-reports-third-quarter-2022-results/

SK hynix. (2024). *SK hynix to produce DRAM from M15X in Cheongju* [Press release]. https://news.skhynix.com/sk-hynix-to-produce-dram-from-m15x-in-cheongju/

SK hynix. (2025). *New facility investment for Yongin semiconductor cluster* [Press release]. https://news.skhynix.com/new-facility-investment-for-yongin-semiconductor-cluster/

SK hynix. (2026). *Explainer: SK hynix's Mid-to-Long-Term Investment Strategy* [Press release]. https://news.skhynix.com/fact-05/

TrendForce. (2026, June 2). *Tight DRAM supply gives suppliers greater pricing power in HBM, with HBM contract prices expected to surge multiples higher in 2027* [Press release]. https://www.trendforce.com/presscenter/news/20260602-13074.html

Market-share estimates and price series for DRAM cited qualitatively in Chapter 7 rest partly on secondary industry data (e.g., Omdia rankings reproduced in the CXMT prospectus; research-firm price assessments) and are identified as such where used. TrendForce wafer- and bit-share estimates are forward-looking projections by that firm, not realized outcomes. Accelerator stock and flow estimates in Chapter 6 are those of Report 12 of this series.

---

*© 2026 Wisdom Hill Research. For institutional investors only. This document presents an analytical framework and does not constitute investment advice or a recommendation to buy or sell any security.*
