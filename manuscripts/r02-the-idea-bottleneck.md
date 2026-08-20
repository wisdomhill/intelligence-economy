---
title: "2. The Idea Bottleneck"
subtitle: "Why agentic AI's productivity dividend hides in data, not code"
series: "The Intelligence Economy"
number: 2
manuscript-revision: 1
date: 2026-08-24
date-modified: 2026-08-24
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  Agentic AI made execution abundant, but the productivity dividend is
  almost nowhere in the financial statements. Why the constraint moved
  upstream to the idea, why deployment pooled where it helps least, and
  where the dividend is structurally available.

keywords:
  - productivity paradox
  - idea bottleneck
  - execution-first industries
  - agentic misallocation
  - data intelligence
  - causal inference

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
published:
  dir: reports/r02/
  pdf: r02-the-idea-bottleneck.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r02/

chapters:
  - manuscript: "1. Introduction: The Productivity Paradox of Agentic AI"
    published:  "1. The Productivity Paradox"
    fragment:   _01-productivity-paradox.qmd
    page:       01-productivity-paradox.qmd
  - manuscript: "2. The Missing Signal: Where the Returns Are Not"
    published:  "2. The Missing Signal"
    fragment:   _02-missing-signal.qmd
    page:       02-missing-signal.qmd
  - manuscript: "3. The Creative Industries Under AI: Supply Without Captured Value"
    published:  "3. The Creative Industries Under AI"
    fragment:   _03-creative-industries.qmd
    page:       03-creative-industries.qmd
  - manuscript: "4. A Theory of the Bottleneck"
    published:  "4. A Theory of the Bottleneck"
    fragment:   _04-theory-of-the-bottleneck.qmd
    page:       04-theory-of-the-bottleneck.qmd
  - manuscript: "5. The Topology of Industries: Two Orderings of Idea and Labor"
    published:  "5. The Topology of Industries"
    fragment:   _05-topology-of-industries.qmd
    page:       05-topology-of-industries.qmd
  - manuscript: "6. The Great Misallocation: Agents Under the Streetlight"
    published:  "6. The Great Misallocation"
    fragment:   _06-great-misallocation.qmd
    page:       06-great-misallocation.qmd
  - manuscript: "7. The Data Analytics Exception — Data as an Idea Factory"
    published:  "7. The Data Analytics Exception"
    fragment:   _07-data-analytics-exception.qmd
    page:       07-data-analytics-exception.qmd
  - manuscript: "8. Implications: Data Intelligence as Economic Necessity"
    published:  "8. Data Intelligence as Economic Necessity"
    fragment:   _08-data-intelligence.qmd
    page:       08-data-intelligence.qmd
  - manuscript: "9. Conclusion: The Bottleneck Always Moves to Judgment"
    published:  "9. The Bottleneck Always Moves to Judgment"
    fragment:   _09-conclusion.qmd
    page:       09-conclusion.qmd
  - manuscript:
      - "Appendix A — Data Sources and Statistical Methods"
      - "Appendix B — Limitations, Identification Caveats, and Falsification Conditions"
    published:  "Appendices"
    fragment:   _10-appendices.qmd
    page:       10-appendices.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _11-references.qmd
    page:       11-references.qmd
---
# The Idea Bottleneck

### Why Agentic AI's Productivity Dividend Hides in Data, Not Code

**The Intelligence Economy — Report 2 of 14**

**Wisdom Hill Research | Thematic Research | July 2026**

---

## Executive Summary

Agentic AI coding tools—Claude Code, Codex, and their peers—have achieved extraordinary adoption. At firms that disclose usage, a majority of committed code now originates from AI, and the tools have spread faster than budgets anticipated. Yet a stubborn puzzle remains: this micro-level productivity is almost nowhere visible in the quarterly or annual financial statements of the firms deploying it. Report 1 documented the supply-side revolution and closed on exactly this question; this report answers it, and arrives at a structural answer with a constructive implication.

The organizing device is a four-stage pipeline of knowledge production: **Idea → Execution → Verification → Adoption**. Agentic AI has made the second stage—execution—hyper-abundant. By the elementary logic of constraints, the throughput of the pipeline is now governed by its scarcest remaining stage, and this report interrogates the upstream node: the idea. (Reports 3 and 4 interrogate the downstream nodes; Report 5 proposes the architecture that unblocks the pipeline end to end.)

The core finding is twofold—one structural claim and one compositional claim, whose product is the paradox.

**The structural claim.** Agentic AI compresses the cost of *execution* but cannot manufacture the scarce input of creative industries—the *idea*. Where value originates in a fresh idea and execution merely realizes it (consumer software and games, music, books, film), AI floods the market with competent variations of existing concepts without expanding the quality frontier. Because industry revenue in these markets is set by demand—attention, wallets, hours—not by supply, producing hundreds of similar products more efficiently is business stealing, not market expansion: a zero-sum reallocation of a fixed pool, whose gains, where they exist at all, accrue to consumers rather than to producers. Only frontier-moving originals—products that create demand that did not previously exist—grow these industries, and frontier-moving originality is precisely what distribution-centered generation does not supply.

**The compositional claim.** Agentic AI adoption has concentrated, so far, in exactly these idea-first domains—code and content—because that is where verification is native, workflows are digital, and deployment is frictionless. The domains where execution genuinely is the binding constraint—customer operations, back-office processing, commerce, the execution-bound majority of general industry—are where the latent productivity gains are largest, and they are precisely where agents have barely arrived, because that work lives inside enterprise software that agents cannot yet inhabit. The paradox is therefore, in its second half, a routing problem: the capability pooled where deployment was easy, not where value was large.

The report formalizes a **topology of industries** based on the causal ordering of idea and labor—and shows that the topology runs *through* the software industry itself: consumer content and games are idea-first, while enterprise software and commerce are efficiency-weighted, which inverts where agentic AI's contribution potential actually lies. A firm-level case anchors the argument in audited data: **Uber**, the heaviest disclosed spender on Claude Code, shows revenue growth oscillating within the same +14–20% band before and after the tool's firm-wide rollout—no break, in the post-rollout data available to date, that the deployment can be credited with. The mirror-image prediction—that a financial ROI footprint should appear instead in execution-bound work such as customer operations, back-office processing, and commerce—is developed in Sections 5 and 6; reported experience at firms like Klarna is consistent with it, but no public case yet supplies clean causal identification.

The constructive implication concerns the one mechanism that attacks the idea bottleneck directly. AI cannot *originate* the out-of-distribution idea, but in data-rich domains ideas need not be imagined—they can be *found*. Agentic analytics industrializes the search for them, which is why the productivity dividend hides in data, not code. But scaled search mass-produces spurious findings alongside genuine ones, so the binding constraint relocates from labor to *judgment*: the scarce, non-delegable capability of critical interpretation we call **Data Intelligence**. It must become universal—not as tool fluency, which AI has commoditized, but as a discipline of inference. It is not a complement to AI value in analytics; it is its precondition.

*This report develops the argument in nine sections. Readers primarily interested in the empirical core may begin with Section 5.4 (the firm-level evidence) and Section 6 (the misallocation evidence); those interested in the human-capital conclusion may turn to Section 8.*

---

# 1. Introduction: The Productivity Paradox of Agentic AI

## 1.1 The puzzle — explosive adoption, invisible macro returns

By mid-2026, agentic coding tools have crossed from novelty to infrastructure. Industry surveys place AI-tool use among developers at roughly four in five—about 84% including those planning adoption, with nearly two-thirds using the tools daily or weekly—while autonomous coding agents proper, at roughly three in ten developers in 2025 surveys, are earlier in the curve but climbing steeply; at firms that disclose internal telemetry the share of AI-authored code routinely exceeds two-thirds. Anthropic's Claude Code and OpenAI's Codex are the leading exemplars of a new category: tools that do not merely autocomplete but read entire codebases, plan multi-step changes, run tests, and open pull requests with diminishing human oversight.

And yet, when one turns from the micro evidence—time saved per task, pull requests merged—to the macro evidence of industry revenue and firm-level financial statements, the productivity dividend largely disappears. Software-industry revenue growth has decelerated, not accelerated, through the very period of fastest adoption. The firms spending most aggressively on coding agents cannot point to a corresponding inflection in their own results. This is the paradox the report sets out to explain — the question Report 1's Coda posed and could not resolve from the supply side alone.

## 1.2 Scope and method: what "evidence" means here

This report applies a deliberately strict evidentiary standard. We distinguish three tiers of claim, and privilege the last:

- **Anecdotal** — "Tool X saved engineer Y two hours." Abundant, but unfalsifiable at the level of economic outcomes.
- **Project-level** — "Migration Z completed in days, not weeks." Real, but not traceable to the income statement.
- **Financial-statement identification** — a revenue or operating-income effect that can be causally attributed to AI in quarterly or annual data. This is the standard we hold throughout.

This standard is demanding by design. As we show, it is met by almost no firm outside the small group that *sells* AI rather than merely uses it—and that scarcity is itself the central piece of evidence.

## 1.3 The framework: Idea → Execution → Verification → Adoption

Knowledge work, viewed as a production process, passes through four stages. An **idea** must exist—a conception of what is worth making and why anyone would value it. The idea must be **executed**—turned into an artifact: code, a document, a track, an analysis. The artifact must be **verified**—confirmed to be correct, safe, and fit for purpose. And the verified artifact must be **adopted**—integrated into the workflows, systems, and habits of the people and organizations it is meant to serve. Value is realized only at the end of the pipeline, and the throughput of the pipeline is governed, as in any serial process, by its scarcest stage:

**Value throughput ≈ min( Idea, Execution, Verification, Adoption )**

The significance of 2025–2026, established in Report 1, is that agentic AI made the second stage hyper-abundant. Execution—once the costly, time-consuming center of knowledge work—became cheap, fast, and parallelizable. But making one stage of a serial pipeline abundant does not raise throughput; it *relocates the constraint*. The economic question of the agentic era is therefore not "how capable are the agents?" but "which stage binds now, where, and for whom?"

This question organizes the next four reports of the series:

| Report | Pipeline node | Question |
|---|---|---|
| **2 — The Idea Bottleneck** *(this report)* | **Idea** | Why does abundant execution fail to create value where the idea is the scarce input — and where does the idea constraint *not* bind? |
| 3 — The Token Economics of Coding Agents | Execution → Verification | How did software uniquely close the verification loop by machine, and how does the loop get cheaper (from tokenmaxxing to valuemaxxing)? |
| 4 — The SaaS Apocalypse Question | Adoption | Why does today's enterprise-software gateway block agentic capability from reaching the work it could transform? |
| 5 — The Agentic Mesh | The pipeline entire | What architecture unblocks all four stages at once? |

Two clarifications guard against misreading. First, the stages are not equally automatable: execution has been industrialized, verification has been industrialized *in one domain* (software—Report 3), while idea and adoption remain, for now, dominated by human inputs and human institutions. Second, the constraint is not the same everywhere. Which stage binds depends on the structure of the industry—the subject of Section 5—and mapping that variation correctly is what dissolves the apparent paradox.

## 1.4 The central thesis — and its rivals

The thesis of this report is a conjunction of two claims:

**Structural:** *Agentic AI lowers the cost of execution but cannot supply the idea; where the idea is the binding input, abundant execution multiplies copies without expanding value, and industry revenue—set by demand, not supply—does not move.*

**Compositional:** *Agentic adoption has so far concentrated precisely in those idea-bound domains, while the execution-bound work of general industry—where the same capability would bind against the true constraint—remains largely unreached, because it lives behind an enterprise-software gateway the agents cannot yet pass.*

The paradox is the product of the two: the capability landed where it helps least and has not yet arrived where it would help most. Its one systematic exception—data analytics, where execution is the *input* to the idea—is where the dividend becomes structurally available, and it is gated by judgment rather than labor (Sections 7–8).

This thesis competes with at least four rival explanations of the missing productivity: that the gains are real but *unmeasured or lagged* (the J-curve reading); that adoption is simply *too early* (the diffusion reading); that the gains are real but *competed away* into consumer surplus; and that the spending is real but the value is not (the capital-cycle reading Report 1's Coda flagged). Section 2.5 confronts each. We do not claim they are wrong so much as insufficient: each explains a piece of the null result, but only the idea-bottleneck-plus-misallocation reading predicts the *pattern*—where returns appear, where they do not, and why the exceptions look the way they do.

---

# 2. The Missing Signal: Where the Returns Are Not

## 2.1 Software industry revenue: deceleration, not acceleration

If coding agents were materially lifting the software industry's output, the simplest place to see it would be revenue. Instead, the data show the opposite trajectory. Median revenue-growth rates for public SaaS companies, after a temporary re-acceleration in 2021, resumed a decade-long deceleration. Private B2B SaaS benchmarks are starker still: between Lighter Capital's successive benchmark editions, median annual revenue growth fell from 47% to 28%—a 40% reduction. The 2025 edition reflects connected-company data through 2024, so the deceleration *predates* the 2025 agent surge—which strengthens rather than weakens the point: cheap code arrived into a market already decelerating for reasons of its own.

The cause of this deceleration is demand-side, not supply-side. The dominant driver identified across benchmark studies is a sharp slowdown in new-customer acquisition—a function of macro rates and buyer behavior, not of how cheaply software can be built. Cheaper production of code does not, by itself, create the demand that produces revenue.

## 2.2 The app economy: supply decoupled from demand

Mobile app stores separate *supply* (titles published) from *demand* (consumer spending) with unusual clarity. If an execution-cost collapse expanded the market, the ledger should show it. In 2025, combined gross consumer spend across the App Store and Google Play reached $167 billion, up 10.6% year over year. On its face, a healthy figure. But total downloads rose only 0.8%, and the top 1% of apps captured 92.2% of all in-app-purchase revenue. Supply and engagement plateaued while a sliver of incumbents absorbed the spend. This is not the signature of an execution-cost collapse expanding the market; it is the signature of a market whose value lives in a frontier that did not move.

The experiment is, in substantial part, a *games* experiment: games account for roughly half of global consumer app spend, and the concentration at the top of the charts is most extreme there. Section 3.3 examines the games market directly, because it is the largest creative-software category and the one where AI-assisted production has penetrated fastest.

## 2.3 A statistical interlude: testing for a structural break

Was the 2025 app-spend figure a genuine break from trend, or noise? We tested this directly. Taking annual year-over-year growth rates from 2020 through 2024 as the prior distribution (mean 12.5%, standard deviation 12.7%, n = 5) and asking whether 2025's 10.6% growth represents a significant departure, a prediction-interval test returns t = −0.14, p = 0.90. The 2025 value sits almost exactly on the prior mean—slightly below it. A log-linear trend extrapolation reaches the same verdict: 2025 actuals fall comfortably inside the 95% prediction interval. The methodological point matters as much as the result: with a short, high-variance annual series, the burden of proof for "acceleration" is high, and 2025 does not meet it.

| **Test design** | **Trend (null)** | **2025 actual** | **p-value** | **Verdict (95%)** |
| --- | --- | --- | --- | --- |
| Prior YoY rates (2020–24) vs 2025, prediction interval | 12.5% mean | 10.6% | 0.90 | Not significant |
| 2020–24 log-linear trend → 2025 point forecast | $156.9B | $167B | 0.49 | Inside interval |

## 2.4 Reading the null correctly

A statistically insignificant result is not proof of no effect. The correct reading is *underpowered identification*: at this sample size and aggregation level, any coding-agent effect is indistinguishable from the far larger demand-side cycle in which it is embedded. The honest statement is not "agentic AI raised no revenue" but "any effect is too small, too lagged, or too confounded to be identified in these data." That distinction governs the rest of the report.

## 2.5 Weighing the rival explanations

Four rival readings of the missing signal deserve explicit treatment, because each is partially right and none is sufficient.

**The J-curve (measurement-lag) reading.** General-purpose technologies have historically delivered their statistical dividend with long delay—decades, in the case of electrification—because output gains require complementary reorganization that first appears as cost, not productivity. This is surely part of the story, and it predicts intangible investment surges of the kind now visible. What it does not predict is the *cross-sectional pattern* documented below: supply explosions with per-unit value collapse in creative markets (Section 3), gains that land with consumers rather than producers in books (Section 3.2), and a firm-level case (Uber, Section 5.4) where broad tool deployment left no discernible break in the revenue-growth trajectory. Lag explains absence of gains; it does not explain the presence of these specific distortions.

**The diffusion (too-early) reading.** Adoption is indeed early in most of the economy—Section 6 shows exactly that, and builds it into the thesis. But the reading fails precisely where adoption is *not* early: among software developers, AI-tool penetration approaches saturation—roughly four in five use or plan to use the tools, and AI authors the majority of committed code at disclosing firms, while autonomous-agent use (about three in ten overall) is concentrated precisely at the heavy-spending firms Section 5 examines—and the null result persists *within* the most-diffused domain on earth. Whatever is limiting returns in software, it is not insufficient diffusion.

**The competed-away-surplus reading.** Efficiency gains under competition flow to consumers as lower prices and better products, vanishing from producer revenue while raising unmeasured welfare. This mechanism is real, and in books it demonstrably operates: consumer surplus rose about 7% even as producer revenue stagnated (Section 3.2). But conceding the mechanism is not conceding the explanation, for two reasons. First, it does not generalize: in music the transfer ran to *fraud* rather than to listeners (Section 3.1), and in apps spend concentrated in incumbents rather than dissipating into consumer surplus. Second, and more decisively, it does not reach the enterprise evidence at all—where AI is most heavily deployed, neither producer returns nor any identified consumer windfall appears (Section 2.4). A hypothesis that explains one creative market while leaving the central null untouched is a component of the answer, not the answer.

**The capital-cycle reading.** Report 1's Coda flagged the bear interpretation: enterprises are buying expenditure, not outcomes, and the revenue curves of the AI sellers are the signature of a capital cycle. This report's evidentiary standard (Section 1.2) takes the reading seriously—clean financial-statement identification is indeed concentrated among firms that *sell* AI. But the reading is not the whole story: the mechanism-level case for analytics (Section 7) shows a channel through which AI raises measured output that a pure capital cycle would not predict, and the topology predicts that execution-bound processes—not the AI sellers—are where operating leverage should eventually surface. A pure bubble story predicts effects nowhere real; the structural account predicts them in specific, identifiable places.

The idea-bottleneck-plus-misallocation thesis subsumes what is true in each rival and adds the one thing they lack: a prediction of *where* returns appear and where they do not. The remainder of the report tests that prediction.

---
# 3. The Creative Industries Under AI: Supply Without Captured Value

If software is too confounded to read cleanly, the creative industries provide a sharper test, because here AI's effect on *supply* is dramatic and measurable. Output has exploded. The question is whether revenue—and consumer welfare—followed.

## 3.1 Music — sixty thousand tracks a day, zero hits

On the supply side, the surge is unambiguous. By January 2026 a single streaming service, Deezer, reported receiving more than 60,000 fully AI-generated tracks per day. On the revenue side, the picture is one of mature, sub-trend growth. Global recorded-music revenue grew 6.4% in 2025 to $31.7 billion—an eleventh consecutive year of growth, but a rate that sits below most of the prior decade (which ran 7–18% in most years). The 2024 figure of 4.8% was the weakest since 2015.

Two facts puncture any AI-driven narrative. First, the growth that did occur was driven by paid subscription streaming (+8.8%, 837 million subscribers), not by new AI supply. Second, AI supply is *subtracting* from artist revenue rather than adding: of all streams on AI-generated music, an estimated 85% are fraudulent—artificially generated plays that attempt to siphon royalties away from human creators; Deezer reports detecting and demonetizing these streams and excluding them from the royalty pool, so the flood's principal product is fraud-policing cost, not music revenue. Economic studies cited by the industry project that up to 23% of music creators' revenue is at risk from generative AI by 2028. The best-selling work of 2025 remained a human one. The quality frontier did not move; the bottom of the distribution simply filled with noise.

## 3.2 Books — the +32.5% title surge and the per-title revenue collapse

Books present the cleanest decoupling of supply from producer value in this report. In 2025 the United States registered 4.17 million ISBN titles, a 32.5% single-year jump—one of the largest in publishing history—driven by a 38.7% rise in self-published titles. Reimers and Waldfogel (2026) estimate that the diffusion of LLMs tripled new book releases between 2022 and 2025, with AI-containing titles topping half of 2025 releases.

Revenue did not remotely track this volume—though the two series must be read on their own terms, because they measure different populations. On the industry side, revenue reported by AAP's participating publishers rose only 0.4% year-to-date, with print units down 1.6% in the first half; these figures include backlist and all formats, and a single title can carry several ISBNs across formats, so the ISBN count cannot simply be divided into the revenue line. The per-title collapse is instead identified where the sample is internally consistent: in Reimers and Waldfogel's Amazon e-book data, new releases roughly tripled while average per-title readership declined, and AI-containing titles account for the quality decline—they cluster at the lower end of the distribution. The direction is the same on every measure: supply expanded by an order of magnitude more than the revenue pool it competes for, and the economics of the marginal title deteriorated accordingly. Roughly 75% of self-published authors earn under $1,000 per year.

Consumer welfare, however, moved in the opposite direction from producer revenue—and this is the instructive part. Reimers and Waldfogel's nested-logit calibration finds that AI books *raised* consumer surplus by roughly 7% in 2025: average quality fell, but the sheer increase in releases widened the right tail enough that readers, on net, gained. They further find that AI has not displaced authors active before LLMs. The book market is thus not a story of value destroyed but of value *relocated*: abundant supply delivered real gains to readers while producer revenue stayed flat and per-title economics collapsed.

That dissociation is precisely what the idea-bottleneck thesis predicts, and it sharpens rather than softens the argument. Cheap execution does generate value; what it does not do is generate value *the producer can capture*. The gains accrue to consumers because supply expansion competes away the surplus it creates—which is why the publishing industry's P&L registers nothing while readers are measurably better off. The music case shows the same input producing a different distribution: there the loss is borne as fraud rather than diffused as consumer gain, because a curation layer intermediates discovery.

## 3.3 Games — the imitation flood and the chart that would not move

Games are the largest creative-software market and the segment of software production where AI assistance has penetrated fastest—asset generation, code, localization, and level content are all inside current tool capability. The supply response is visible in the release data: new titles published on Steam set another record in 2025, extending a multi-year surge, and the share of new releases disclosing generative-AI use in their production has climbed to a substantial minority and is rising every quarter. Production cost per title, for a given quality tier, has fallen sharply.

Demand did not follow supply, and the composition of demand is the tell. Consumer spend in games remains extraordinarily concentrated in a small set of incumbent live-service titles—many of them five to ten years old—whose grip on the top of the charts the AI-assisted flood has not loosened. The overwhelming majority of new releases earn de minimis revenue, and the AI-disclosed cohort clusters, as in books, toward the bottom of the distribution. Meanwhile, what production-cost deflation *has* demonstrably done is help incumbents accelerate their content cadence—more seasons, more events, more cosmetics for the same titles—which deepens, rather than disrupts, the existing concentration.

The industry's own growth history states the frontier thesis in positive form. The episodes that genuinely expanded gaming revenue were not catalog expansions but frontier movements: new genres and category hybrids that created demand which had not existed—the battle-royale wave, the open-world gacha model, breakout original IPs that pulled non-players into the market. Hundreds of competent variations on existing games redistribute a fixed pool of playtime and spend; a new category enlarges the pool. As of this writing, no AI-originated title has produced such a movement. The chart, like the frontier, has not moved.

## 3.4 The firm-level mirror: Duolingo's content-explosion experiment

One public company ran the books experiment inside a single firm, with disclosed data. In April 2025 Duolingo launched 148 new language courses in a single release—roughly doubling a catalog that had taken more than a decade to build—stating explicitly that generative AI had collapsed course-production time from years to months. It was as clean a demonstration of execution-cost collapse as the market has produced: the marginal cost of a *course* fell by an order of magnitude or more.

The revenue consequences are instructive in both directions. Duolingo's growth remained strong through 2025—but the disclosed drivers were not the long-tail catalog. Monetization continued to concentrate in the same core language pairs, and the incremental revenue the company attributed to AI came from *frontier-moving product features*—the premium Max tier's conversational Video Call capability chief among them—rather than from catalog breadth. Meanwhile the episode carried real costs: an "AI-first" positioning triggered consumer backlash, and by late 2025 a deceleration in daily-active-user growth produced one of the sharper share-price drawdowns in the application-software cohort, as the market repriced engagement rather than content supply.

Read against Section 3.2, the case replicates the books experiment inside a single firm—illustrative rather than controlled (Appendix B.1), but pointed. Catalog quantity is execution; the engagement frontier is the idea. The 148-course expansion multiplied the catalog without moving the frontier and left the revenue trajectory largely untouched—while the one AI deployment that *did* move revenue was the one that moved the frontier (a genuinely novel product capability). The firm-level pattern is thus consistent with the thesis from both directions at once.

Film and video follow the same logic in muted form, and we treat them in a note rather than the main text. Film and video diverge only in that the consumer-facing "AI content flood" channel remains weak; AI revenue there appears instead as B2B *tooling* (AI video generators, ~$0.79B in 2025, growing ~20% annually) rather than as content consumers pay more for. Global box office (~$33.5B in 2025) is in slow post-pandemic recovery, not acceleration, and the AI-tooling market amounts to roughly 2% of theatrical revenue—and a far smaller share of the film-and-video economy once streaming and television are included—too small to move the industry curve.

---

# 4. A Theory of the Bottleneck

## 4.1 Value as a function of idea and execution

Let the value of a creative work be a function of two inputs: the idea and its execution. The observations of Sections 2 and 3 are explained at once if these inputs are **complements in the strong (Leontief) sense**—where the binding input determines the outcome—rather than additive substitutes. Under a Leontief relation, holding the idea fixed while driving the cost of execution toward zero does not raise value; it merely multiplies the number of copies of the same idea.

## 4.2 Why the frontier, not the catalog, determines value — and why the game is zero-sum

Consumer utility derives not from the *count* of available works but from the *quality of the best available option*—the frontier of the distribution. If the best work in a catalog scores 100, adding 900,000 works scoring 50 leaves the frontier, and thus utility, essentially unchanged. "No mainstream hit among AI works" is precisely the empirical statement that the frontier did not move, and it is the proximate reason revenue did not follow supply.

The demand side completes the mechanism. In creative markets, industry revenue is set by the size of the demand pool—hours of attention, entertainment wallets, disposable time—which is approximately fixed in the short run. Producing hundreds of similar products more efficiently therefore does not expand the industry; it reallocates shares of a fixed pool. In the language of industrial organization, an execution-cost collapse without frontier movement is **business stealing, not market expansion**: privately rational for each entrant, collectively zero-sum for the industry. Consumers may still gain from the flood—in books, measurably so—but that gain is precisely what the producers do not capture; it is the surplus escaping the industry, not accruing to it.

The contrapositive is the positive law of these industries, and it deserves equal emphasis: **the only thing that grows a creative industry's revenue is a frontier-moving original—a product whose quality or novelty creates demand that did not previously exist.** The historical growth episodes of every market examined in Section 3 conform: recorded music's revenue expansions came from format and business-model frontiers (the subscription-streaming category itself), publishing's growth pockets from breakout genres that recruited new readers, gaming's step-changes from new categories that enlarged the playing population. Catalog volume has never done this; frontier movement always has. An efficiency technology that multiplies the catalog while leaving the frontier fixed is therefore, for industry revenue purposes, a null operation—executed at real cost.

## 4.3 Why AI compresses execution but cannot manufacture the tail

A fresh idea is, by definition, an outlier—far from the center of the training distribution. A model trained to predict the most probable next token exhibits a structural regression toward the mean, which is why its output tends toward the competent average rather than the surprising tail. AI does not fail to execute; it fails to *originate*. This is not a temporary limitation of scale so much as a property of distribution-centered generation.

## 4.4 The talent-pool problem

A natural rejoinder is that AI amplifies the creative output of skilled practitioners. This is true but insufficient, and on closer inspection it cuts the other way. If AI multiplies a skilled creator's output by a factor k while the size of the skilled set S is fixed, total creative output rises only linearly, as k · |S|. Worse, AI may *erode the pipeline* that produces new skilled practitioners. Skill is formed through friction—the trial and error of doing the work oneself. If an agent absorbs that friction, the inflow of new experts falls, |S| shrinks over time, and AI's creative contribution contracts rather than compounds. The benefit accrues to a small, and possibly diminishing, set of incumbent talents.

## 4.5 The theory in the pipeline

Sections 2–4 can now be restated in the framework of Section 1.3. The agentic wave made Execution abundant; in idea-first markets the binding stage is Idea; therefore min(Idea, Execution, Verification, Adoption) did not move, and neither did value. This locates the present report precisely—and delimits it. Even where the idea *does* exist, two further gates stand between execution and realized value: the artifact must be verified (a gate that software alone has learned to pass by machine—Report 3), and it must be adopted into organizational workflows (a gate that today's enterprise-software structure holds shut—Report 4). The idea bottleneck is the first constraint, not the only one; this report explains why abundance failed upstream, and hands the downstream gates to its successors.

---

# 5. The Topology of Industries: Two Orderings of Idea and Labor

The decisive variable is not whether an industry contains ideas and execution—all do—but the **causal order** in which they occur.

## 5.1 Idea-first industries — where delegation severs discovery

In idea-first industries—consumer software products, music, books, film—the idea must exist before execution acquires meaning: idea → execution → value. AI cheapens the second arrow while the bottleneck sits at the first node. There is a further, subtler cost. Because ideas in creative work are often discovered *in* the act of building—the dead ends and "why won't this work?" moments that yield insight—delegating execution to an agent can sever the discovery channel itself. Driving the cost of execution to zero can drive the *input to idea-generation* to zero as well. This is the paradox at the heart of idea-first work: the friction AI removes was load-bearing.

## 5.2 Execution-first industries — where labor is the input to insight

In execution-first industries—most clearly data science and analytics—the order inverts: labor (ETL, data cleaning, pipeline construction, repeated analysis) → insight → value. Here repetitive labor is the *input* to the idea, not its prerequisite. One must run many analyses to surface one insight; the idea is the *output* of the labor, not its precondition. In this regime AI amplifies exactly the input whose severing damaged the idea-first case—and the same tool that destroyed value in one topology creates it in the other.

## 5.3 Software is not one industry: the internal topology

The topology does not stop at the software industry's border; it runs through the middle of it, and recognizing this resolves a confusion that runs through most commentary on coding agents.

**Consumer content software—games, media, entertainment apps—is idea-first.** Its value is hit-driven; its demand pool is attention; its frontier is aesthetic and conceptual novelty. Applying agentic execution here runs directly into the zero-sum wall of Section 4.2, and Section 3.3 showed the result: record supply, unmoved charts.

**Enterprise software and commerce are efficiency-weighted.** Demand for enterprise software derives from business processes, not from novelty; the purchase criterion is measurable—cost reduced, revenue operations improved, errors eliminated—and the outcomes are contractible. Commerce is more extreme still: catalog management, pricing, fulfillment coordination, seller support, and customer service are execution all the way down, and their value is the distribution's *center* done reliably at scale, not its tail. In these segments, "hundreds of similar implementations, produced efficiently" is not a bug but the entire point.

The implication inverts the prevailing intuition about where agentic AI matters inside software. Coding agents applied to *producing more consumer software* multiply a catalog whose frontier they cannot move. The same capability applied to *operating* enterprise processes and commerce attacks a genuine execution bottleneck—the configuration this report's synthesis (Section 5.5) identifies as the necessary condition for financial ROI. The potential of agentic AI within the software economy is therefore greatest precisely in its least glamorous quarters: enterprise software and commerce, where efficiency is the product. That the technology's actual deployment concentrated at the opposite pole is the subject of Section 6.

## 5.4 Firm-level case study: Uber and the timing of Claude Code

Uber is the heaviest disclosed spender on coding agents, and the statistics of its deployment are unambiguous. Per-engineer AI API costs ran $500–$2,000 per month; 95% of engineers used AI tools monthly; roughly 70% of committed code originated from AI; AI-related costs rose roughly sixfold since 2024, and the company exhausted its entire 2026 AI budget in four months, driven by Claude Code. R&D expense rose 9% to $3.4 billion in 2025.

The revenue series, read against this deployment, shows no identifiable break. Across Q1 2024–Q1 2026, growth oscillated within a +14% to +20% year-over-year band. Claude Code launched publicly in May 2025, rolled out firm-wide in December 2025, and reached 84% of engineers only in March 2026; the one broadly deployed quarter, Q1 2026—itself a partial post-period, with adoption still ramping from 32% to 84% within the quarter—printed +14%, inside the pre-existing range.

| **Quarter** | **Revenue YoY** | **Claude Code firm-wide?** |
| --- | --- | --- |
| Q1 2024 | +15% | No |
| Q2 2024 | +16% | No |
| Q3 2024 | +20% | No |
| Q4 2024 | +20% | No |
| Q1 2025 | +14% | No |
| Q2 2025 | +18% | No (public launch May 2025) |
| Q3 2025 | +20% | No |
| Q4 2025 | +20% | Rollout begins (firm-wide, Dec 2025) |
| Q1 2026 | +14% | Yes—ramping (32%→84% of engineers, Feb–Mar) |

Management reports the same absence. Uber's president and COO stated that the link between rising Claude Code use and consumer-facing output "is not there yet," and that it is "very hard to draw a line" from usage statistics to more useful features. The cost side offers no more traction: quarterly operating income is volatile (coefficient of variation near 53%), and the bottom line is dominated by one-off items such as the Q3 2025 $4.9B tax-valuation release recognized through the tax provision. No evidence of a productivity effect on Uber's financial results is identifiable in the post-rollout data available; Appendix B.2 names the quarters—Q2 2026 onward—that would force reassessment.

## 5.5 Synthesis: where an ROI footprint should appear

Uber locates the negative case: heavy coding-agent deployment into an idea-first product, with no financial break to show for it. The positive prediction is its structural mirror—a financial ROI footprint should appear only where two conditions hold jointly: (a) value lives in execution (the distribution's center is the right answer), *and* (b) that execution is the binding constraint. In Uber's engineering the second condition fails—execution has value, but it is not the binding constraint; both conditions hold in the execution-bound work of customer operations, back-office processing, and commerce (Section 6).

Reported experience in routine customer service is consistent with this prediction, though no public case yet supplies clean identification. Klarna is the most-cited illustration: the company attributes a step-down in customer-service cost per transaction to AI automation, and its filings tie a falling headcount to "leveraging AI." But the case is a cautionary one as much as a confirming one—the figures are management-attributed rather than audited as a causal effect and cannot be separated from a concurrent industry-wide cost-discipline cycle, and after an aggressive automation push the firm publicly rebalanced back toward human agents for quality-sensitive cases. It supports the narrow point that routine support work is automatable at lower cost; it does not establish that full automation converts cleanly into durable financial ROI. The evidentiary weight of Section 5 therefore rests on Uber's null, not on any single positive case.

| **Case** | **(a) Value in execution?** | **(b) Execution is the bottleneck?** | **Pipeline node that binds** | **Financial ROI footprint?** |
| --- | --- | --- | --- | --- |
| Uber — coding agents | Yes | No (bottleneck is product decisions) | Idea | None identifiable ✗ |
| Apps / books / music / games — creation | No (value in idea) | No | Idea | None identifiable ✗ |
| Execution-bound ops (CS, back-office, commerce) | Yes | Yes | Execution (relieved) | Predicted, not yet cleanly identified |

---
# 6. The Great Misallocation: Agents Under the Streetlight

The structural argument of Sections 3–5 explains why abundant execution created little value *where it was deployed*. This section supplies the second half of the paradox: *where it was deployed* is itself the anomaly. Agentic capability has pooled in the domains least able to convert it, and barely touched the domains most able to.

An old parable describes a man searching for his keys under a streetlight—not because he lost them there, but because that is where the light is. Agentic AI's first deployment wave followed the light: it went where verification was native, workflows were digital, and adoption required no one's permission. It did not go where the value was.

## 6.1 Where the agents actually went

The concentration is measurable from several independent directions.

**Usage composition.** Occupation-level analyses of AI-assistant usage—Anthropic's Economic Index being the most granular public source—consistently find computer and mathematical occupations absorbing the largest share of all AI conversations by a wide margin, at a multiple of several times those occupations' share of employment. Software development is not merely the leading use case; it is over-represented relative to its labor-market weight by roughly an order of magnitude.

**Revenue composition.** Report 1 documented the same skew from the seller's side: the fastest-scaling agentic product in history is a *coding* agent, API traffic skews roughly 77% toward automation patterns, and the enterprise customers driving the revenue explosion are overwhelmingly buying software-engineering capacity.

**The other side of the ledger.** Against this saturation stands the adoption picture in general industry. Official business surveys through 2025–2026 place formal AI adoption at roughly one firm in five across the U.S. economy—the Census Bureau's Business Trends and Outlook Survey reports about 18% in its late-2025 waves and just under 20% by May 2026, led by the information sector near 40% and finance and insurance near 34%; and the most widely cited enterprise study of 2025 found the overwhelming majority of corporate generative-AI pilots—on the order of 95%—producing no measurable P&L impact. Developer AI-tool penetration (use or planned use) runs at roughly 80% economy-wide—with 95% monthly active use at heavy adopters such as Uber; the median firm in the broader economy has not adopted at all.

The distribution of the capability, in short, is close to the inverse of the distribution of the opportunity.

## 6.2 Why they pooled there

Three selection variables, none of them "where is the value largest?", determined the deployment order.

**Verifiability.** Report 1 (Section 2.1.3) established that domains acquire agentic automation roughly in order of their verifiability, because both the RL training loop and the deployment loop need an objective success signal. Code compiles or it does not; a test passes or it fails. Nothing in a claims-processing workflow or a merchandising decision verifies itself—yet.

**Digital-native workflows.** A developer can meet an agent at the terminal, hand it a repository, and let it work; the entire working context is already machine-legible. The general-industry knowledge worker's context lives in ERPs, CRMs, ticketing systems, and document stores—behind authentication, permissions, and vendor boundaries.

**Deployment friction.** Coding agents spread bottom-up through individual adoption—a developer with a subscription—bypassing procurement, integration projects, and change management entirely. Execution-bound enterprise work admits no such path: deploying an agent into an order-to-cash process is an organizational project, not a download.

Code and content sat at the maximum of all three variables simultaneously. They were also, by the topology of Section 5, precisely the domains where execution abundance converts worst into value. The correlation is not accidental—verifiable, digital, frictionless domains are disproportionately the *making-artifacts* domains, and making artifacts is where the idea binds. The light and the keys are in different places by construction.

## 6.3 Where the latent gains live

The mirror image of the misallocation is the map of unrealized potential: the execution-bound work of general industry, where both conditions of Section 5.5 hold and agents have barely arrived.

The contours are visible in every services organization: routine customer operations of the kind now being automated at scale; back-office processing—reconciliation, claims, compliance documentation, invoice and exception handling; commerce operations—catalog and content management, pricing, seller and partner support, fulfillment coordination; supply-chain administration and scheduling; the reporting and documentation layer that consumes a large fraction of professional time in every function. This work shares three properties: its value is the distribution's center done reliably (no frontier problem), human labor is demonstrably its binding constraint (queues, backlogs, headcount-linear scaling), and it is measured in wage bills, not attention.

The aggregate stakes follow from composition: execution-bound functions of this kind account for a large majority of the knowledge-work wage bill, dwarfing the creative-origination occupations where agents currently concentrate. A function-by-function quantification of this demand—which processes, in which order, at what depth—is the subject of Report 8; here it suffices to establish the direction: the economy's agentic upside is concentrated exactly where its agentic deployment is not.

## 6.4 The gateway: productivity must travel through work software

Why, then, have the agents not simply gone where the value is? Because execution-bound general-industry work has an address, and the address is enterprise software. Order-to-cash lives in the ERP; customer operations live in the CRM and the contact-center stack; commerce operations live in the platform; claims live in the claims system. The workers who perform this execution-bound labor cannot meet an agent at a command line, because their work does not pass through one. For agentic capability to reach the general economy, it must pass *through or around* the enterprise software layer in which that economy's work is embedded.

This reframes the productivity paradox in its final form. The first half of the paradox is structural: where agents went, the idea binds (Sections 3–5). The second half is a routing failure: where execution binds, the gateway is closed. Today's enterprise-software incumbents guard that gateway with captive, siloed agents that operate only within their own walls—and, as Report 4 will argue, are structurally disinclined to open it, because a genuinely effective agent threatens the per-seat economics of the software itself. Diagnosing why the gateway fails is Report 4's task; designing its replacement is Report 5's. This report's contribution is to establish that the gateway is where the economy-wide dividend now waits.

---

# 7. The Data Analytics Exception — Data as an Idea Factory

## 7.1 Why analytics inverts the creative-industry logic

Section 5 located one execution-first domain where AI's contribution should turn positive: data analytics. The inversion is precise. In creative work, the friction AI removes (the act of building) is where ideas are born, so removing it destroys value. In analytics, the friction AI removes (ETL, cleaning, pipeline plumbing) is *not* where ideas are born—insight arises later, in the interpretation of results. Friction and discovery are *separable* in analytics and *fused* in creation. That single structural difference is why the same agent helps here and harms there.

## 7.2 A search model of insight

Model insight generation as search. Let p be the (small) probability that a single analysis surfaces a meaningful insight, and n the number of analyses a practitioner can run. The probability of at least one insight is 1 − (1 − p)ⁿ. Human labor constrains n to a handful per day, keeping this probability low. An agent that raises n a hundredfold drives 1 − (1 − p)ⁿ toward 1.

The crucial distinction from the creative case is what n counts. In analytics, n counts *analyses*—and insight is the direct output of that search, so scaling n scales discovery. In idea-first creation, the n that AI scales counts *implemented copies* of an idea, not ideas themselves; scaling it yields the "more copies, same frontier" outcome of Sections 2–3.

## 7.3 Origination versus discovery: how AI relieves a bottleneck it cannot break

At this point the report's two central claims appear to collide. Section 4.3 argued that AI cannot supply the idea—distribution-centered generation regresses to the mean and cannot manufacture the tail. This section argues that agentic analytics is the most powerful idea-generation mechanism available. Both are true, and the distinction between them is the most important conceptual move in the report.

Ideas reach the pipeline by two different routes. **Origination** produces the out-of-distribution conception—the new genre, the unprecedented product—by an act of imagination that has no search space to enumerate. This is what AI does not do, and Section 4 stands. **Discovery** produces the idea by *finding* it: the pattern is already latent in the world—in transaction data, telemetry, experiments, customer behavior—and becoming aware of it is a matter of searching a space that very much can be enumerated. Discovery is execution-intensive by nature: hypotheses must be formulated in bulk, tested in bulk, discarded in bulk. It is, in the terms of Section 5, execution-first idea generation—and that is precisely the configuration agents amplify.

The economic significance is that discovery is the only *industrializable* relief of the idea bottleneck. Origination scales with the talent pool (Section 4.4), which is fixed or shrinking. Discovery scales with n—with the number of analyses run against the organization's data—and n is exactly what agentic AI multiplies without limit. An enterprise cannot order up a visionary; it can order up a hundredfold expansion of systematic search over its own data, and harvest ideas as *outputs* of that search. This—not coding—is where the technology attacks the binding constraint of Section 4 directly, and it is the precise sense in which the productivity dividend hides in data, not code.

## 7.4 The new bottleneck: from labor to judgment

But scaling n has a cost that the search model makes visible. Running a hundredfold more analyses mass-produces not only genuine insights (p) but also *false positives*—the multiple-comparisons problem. At large n, many results will appear statistically significant by chance alone. For AI's net contribution in analytics to remain positive, a new capability must select genuine insight from the inflated pool of candidates: critical interpretation, causal reasoning, and the discipline to distinguish statistical from substantive significance.

When AI dissolves the labor bottleneck in analytics, the bottleneck does not vanish—it moves to **judgment**. And judgment, unlike code, cannot be delegated to the agent that created the surplus of candidates in the first place.

---

# 8. Implications: Data Intelligence as Economic Necessity

## 8.1 Defining Data Intelligence

We use **Data Intelligence** to denote the capability that becomes binding once AI commoditizes analytical execution. It is broader than "data literacy" as commonly used and distinct from Gartner's "decision intelligence." It is the meta-capability of recognizing the differences and proper uses of descriptive, predictive, and causal methods—and deploying the right methodology, in the right place, to reach the most effective decision. It is a discipline of inference, not a toolkit.

## 8.2 The methodological triad: descriptive, predictive, causal

The core of Data Intelligence is fluency in the distinctions among three modes of analysis that are routinely conflated, each answering a different question:

- **Descriptive** — what happened? Summary, comparison, distribution. Answers about the past.
- **Predictive** — what is likely next? Correlational structure exploited for forecasting, valid only while the data-generating process is stable.
- **Causal** — what would happen if we intervened? The only mode that licenses action, and the one most often illegitimately inferred from the other two.

Knowing which question is being asked—and refusing to answer a causal question with a predictive method—is the discriminating skill. AI will generate the code for any of the three on request; it will not, reliably, tell the user which one the situation demands.

## 8.3 Why it must be universal, not specialized

The conclusion is a claim about human capital across all roles, and it follows directly from the bottleneck argument. If AI performs analytical execution but cannot perform interpretive judgment, then the scarce capability in an AI-saturated economy is not the ability to *run* an analysis but the ability to *interrogate* one. Because every function will increasingly receive AI-generated analysis as an input to its decisions, every function must be able to interrogate it. Data Intelligence cannot remain the preserve of a data-science team; the surplus of AI-generated analysis is distributed across the organization, and so must be the judgment to evaluate it.

## 8.4 What it is not: tool fluency AI has already commoditized

This is where the argument most often goes wrong. "Everyone must become data literate" is too readily translated into "everyone must learn SQL, Python, and chart-reading." The bottleneck argument implies the opposite. If AI already performs the execution—writing queries, building pipelines, generating charts—then teaching execution is teaching what AI has commoditized. The capability that remains scarce is interpretive: Is this correlation causal? Is the sample representative? Are confounders controlled? Is this effect size practically meaningful (statistical ≠ substantive significance)? Is this a false positive from multiple comparisons? Does the analysis answer the question I actually asked?

Train judgment, not tools. In a world where AI has democratized technical execution, the scarce skill is not knowing how to use the instrument but knowing whether to believe what it returns.

## 8.5 The organizational stakes

The final point elevates Data Intelligence from a training recommendation to an economic precondition. Because scaled analysis mass-produces spurious findings alongside genuine ones (Section 7.4), an organization without interpretive capability does not merely fail to capture AI's analytical upside—it actively accelerates *systematic error*, making more confident decisions on more false signals. Data Intelligence is therefore not a complement to AI value in analytics; it is the condition under which that value is positive rather than negative. The same abundance-without-discernment dynamic that collapsed per-title economics in the book market operates inside the firm—except that a firm, unlike a reader, has no wider market to diffuse the cost of bad signals into.

## 8.6 The machinery question

Data Intelligence is a human capability, but it does not operate on air. Systematic discovery at the scale Section 7 describes presupposes an enterprise data layer the agents can actually search—governed, semantically coherent, and organized for interrogation rather than for reporting. The architecture of that layer—semantic models, ontologies, and the platforms on which agentic analytics runs—is the subject of Reports 6 and 7, and the function-level demand it must serve is quantified in Report 8. This report establishes what the layer is *for*: it is the factory floor of the idea factory.

---

# 9. Conclusion: The Bottleneck Always Moves to Judgment

The argument of this report is a single chain, now with two links where the original puzzle suggested one. Coding agents do not appear in macro or firm-level financial results because, in idea-first industries, they cheapen execution while the binding constraint is the idea—and because industry revenue in those markets is set by demand, multiplying similar products is business stealing within a fixed pool, not market expansion. Only frontier-moving originals grow such industries, and delegating execution can even sever the channel through which frontier ideas are discovered. That is the structural half. The compositional half is that agentic capability pooled, by the logic of verifiability and deployment friction, in precisely these idea-bound domains—under the streetlight—while the execution-bound work of general industry, where the same capability meets its true constraint, waits behind an enterprise-software gateway that remains closed. The paradox is the product of a topology and a misallocation.

The domain where the logic inverts is data analytics, where repetitive labor is the input to insight and AI's scaling of that labor genuinely raises the probability of discovery—the one industrializable relief of the idea bottleneck, resting on the distinction between origination (which AI cannot do) and discovery (which it multiplies). But there the bottleneck does not disappear; it relocates from labor to judgment—to the interpretive discipline of distinguishing genuine signal from the spurious correlations that scaled analysis inevitably produces.

Three questions leave this report open, by design, and become the mandates of its successors. The verified-artifact question—how software alone taught machines to close the verification loop, and how that loop sheds its waste—is Report 3's. The gateway question—why the enterprise-software layer blocks agentic capability from the execution-bound work that needs it—is Report 4's. And the accumulating requirements for Report 5's architecture now number two: *it must industrialize idea discovery while economizing scarce human judgment* (this report's structural lesson), and *it must deliver agentic capability to the execution-bound work of general industry through an open gateway* (this report's compositional lesson).

The deepest lesson is one this report's own method illustrates. Throughout, the decisive moves were not computational but interpretive: testing a headline growth figure against the right prior, refusing to read an insignificant result as proof of no effect, recognizing that a signal indistinguishable from pre-existing variation is no signal at all. AI can perform the calculation; it cannot, on its own, decide whether the calculation answers the right question. As AI dissolves one bottleneck after another, the constraint that remains—and the human capability that matters—is judgment.

---

# Appendix A — Data Sources and Statistical Methods

Software and SaaS revenue: SaaS Capital long-term growth studies; Lighter Capital 2025 B2B SaaS benchmarks; ChartMogul retention reports. App economy: Sensor Tower State of Mobile 2025 and 2026; State of AI 2026. Music: IFPI Global Music Report 2025 and 2026; Billboard, Music Business Worldwide, Variety coverage; Deezer disclosures. Books: R.R. Bowker self-publishing and ISBN registration data; Reimers and Waldfogel (2026), NBER Working Paper 34777; AAP StatShot; Circana BookScan. Games: Steam release and generative-AI disclosure series (SteamDB-derived analyses); Sensor Tower mobile-games spend data; platform chart-concentration reporting. Duolingo: company investor-relations releases, shareholder letters, and contemporaneous coverage of the April 2025 course expansion and the late-2025 engagement repricing. Usage and adoption composition: Anthropic Economic Index; U.S. Census Bureau Business Trends and Outlook Survey (AI supplement); MIT Project NANDA enterprise GenAI study (2025). Firm financials: Uber SEC filings and earnings releases (Q1 2024–Q1 2026); Klarna Group plc investor relations releases and S-1; reporting by The Information, Fortune, TechCrunch.

Statistical methods: prior-distribution prediction-interval tests use Student's t with n−1 degrees of freedom and the standard error inflated by √(1+1/n) for a single new observation; log-linear trend extrapolation uses ordinary least squares on log revenue with a 95% prediction interval. All app-spend series are annual gross consumer spend (App Store + Google Play; iOS only for China), inclusive of store commissions.

# Appendix B — Limitations, Identification Caveats, and Falsification Conditions

## B.1 Limitations and identification caveats

- **Small-sample power.** Annual macro series (n = 5–6) are underpowered to detect a single-year break; statistical insignificance reflects identification limits, not proven absence of effect.
- **Reconstructed values.** Certain app-spend years (2022–23) and global book-revenue figures are reconstructed or vary across sources; perturbing them widens prior variance and weakens, rather than strengthens, any acceleration claim.
- **Confounding.** Firm-level margin improvements (Klarna and others) coincide with a 2024–26 cost-discipline cycle across technology; cleanly separating AI from layoffs and burn reduction would require a difference-in-differences design against non-adopting peers, which public data do not yet support.
- **Provider-specific usage data.** Occupation-share figures from the Anthropic Economic Index measure the usage composition of one provider's assistant, not of all AI systems; the developer skew is directionally corroborated by revenue composition (Report 1) but the precise multiples should not be over-read.
- **Attribution in the Duolingo case.** The decomposition of Duolingo's 2025 results into catalog-driven versus feature-driven revenue relies on management disclosure and reasonable inference, not on a counterfactual; the case is presented as an illustration of the frontier logic, not as causal identification.
- **Selling vs. using AI.** Clear financial acceleration is concentrated in firms that sell AI (hyperscalers, model and tooling vendors); this report concerns firms that use it, where identification is structurally harder.

## B.2 Falsification conditions

Consistent with the series' method, the report states what would invalidate its theses:

- **Against the structural claim (Sections 3–4):** an AI-originated work moving a creative-industry frontier—a chart-topping AI-native game, album, or bestseller that demonstrably recruits new demand rather than redistributing existing spend—would falsify the regression-to-the-mean argument in its strong form.
- **Against the timing argument (Section 5.4):** subsequent full post-rollout quarters for heavy coding-agent adopters (e.g., Uber Q2 2026 onward) showing revenue or margin growth breaking above the pre-deployment range and cleanly attributed to engineering productivity would require reassessment.
- **Against the compositional claim (Section 6):** broad general-industry deployment of agents into execution-bound processes that *fails* to produce execution-bound operating leverage would falsify the latent-gains map; conversely, a macro TFP inflection arriving *without* any redistribution of agentic deployment toward execution-bound work would indicate the composition mechanism is not load-bearing.
- **Against the analytics exception (Section 7):** if scaled agentic analysis in mature deployments produces predominantly false-positive-driven decision degradation despite interpretive investment, the "discovery" route would be narrower than claimed.

## B.3 Pre-publication verification queue

New data points introduced in this edition, to be verified against primary sources before institutional distribution: games-share of 2025 consumer app spend (Sensor Tower); Steam 2024–2025 release counts and generative-AI disclosure shares; Duolingo April 2025 course-expansion figures, FY2025 bookings drivers, and the late-2025 drawdown magnitude; Anthropic Economic Index occupation shares (latest edition); MIT Project NANDA 95% figure and its methodology; Klarna KLAR post-listing quarterly figures.

---

# References

*Listed in order of first supporting appearance. Entries flagged in Appendix B.3 remain subject to primary-source verification before institutional distribution.*

1. Stack Overflow. (2025). *2025 developer survey*. https://survey.stackoverflow.co/2025/ (AI tool use or planned use ~84% of respondents, ~65% daily/weekly; AI-agent use ~31%.)
2. Google Cloud & DORA. (2025). *2025 state of AI-assisted software development*. Google Cloud. https://dora.dev/research/2025/ (Adoption and delivery-performance effects of AI tooling.)
3. SaaS Capital. (2025). *2025 growth benchmarks for private SaaS companies*. https://www.saas-capital.com/research/
4. Lighter Capital. (2025). *2025 B2B SaaS benchmark report*. https://www.lightercapital.com/resources (Median private B2B SaaS growth, 2024 vs. 2025.)
5. ChartMogul. (2025). *SaaS growth and retention benchmarks*. https://chartmogul.com/insights/
6. Sensor Tower. (2026, January). *State of mobile 2026*. https://sensortower.com/report/state-of-mobile-2026 (2025 combined App Store / Google Play gross consumer spend of $167B, +10.6%; download growth +0.8%; top-1% revenue concentration 92.2%.)
7. Sensor Tower / data.ai. (2021–2025). *State of mobile* [Annual editions]. https://sensortower.com/report/state-of-mobile-2026 (Prior-year editions via the Sensor Tower reports library; prior-distribution annual growth series used in the Section 2.3 structural-break tests.)
8. Deezer. (2026, January). *Deezer to make its industry-leading AI detection tool available to music streaming services* [Press release]. Deezer Newsroom. https://newsroom-deezer.com/2026/01/ai-generated-music-deezer-selling-detection-tool/ (>60,000 AI tracks submitted daily; ~85% of AI-track streams estimated fraudulent; fraudulent streams demonetized and excluded from the royalty pool.)
9. International Federation of the Phonographic Industry. (2026, March). *Global music report 2026*. IFPI. https://www.ifpi.org/resources/ (2025 global recorded-music revenue of $31.7B, +6.4%; subscription streaming +8.8%, 837M subscribers.)
10. International Federation of the Phonographic Industry. (2025, March). *Global music report 2025*. IFPI. https://www.ifpi.org/resources/ (2024 growth of +4.8%, weakest since 2015.)
11. CISAC & PMP Strategy. (2024). *Study on the economic impact of generative AI in the music and audiovisual industries*. International Confederation of Societies of Authors and Composers. https://www.cisac.org/Newsroom/news-releases/ (Basis of the up-to-23%-at-risk figure for creators' revenue through 2028.)
12. R.R. Bowker. (2026). *U.S. ISBN registration output, 2025*. Bowker. https://www.bowker.com/news/ (4.17M titles, +32.5%; self-published titles +38.7%.)
13. Reimers, I., & Waldfogel, J. (2026). *AI and the quantity and quality of creative products: Have LLMs boosted creation of valuable books?* (NBER Working Paper No. 34777). National Bureau of Economic Research. https://doi.org/10.3386/w34777 (Issued January 2026, revised May 2026.)
14. Association of American Publishers. (2025). *StatShot monthly and annual reports*. AAP. https://publishers.org/data-and-statistics/ (U.S. publishing industry revenue, 2025 year-to-date.)
15. Milliot, J. (2025, July 7). Print book sales slipped in first half of 2025. *Publishers Weekly*. https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/article/98147-print-book-sales-slipped-in-first-half-of-2025.html (Circana BookScan print unit sales, −1.6% in H1 2025.)
16. Gamalytic and related SteamDB-derived analyses. (2026). *Steam annual release counts and generative-AI content disclosures, 2024–2026*. https://gamalytic.com/ (Third-party platform analyses.)
17. Sensor Tower. (2025). *Mobile games consumer-spend composition and chart-concentration data*. https://sensortower.com/blog
18. Duolingo, Inc. (2025, April 30). *Duolingo launches 148 new courses, more than doubling its offering* [Press release]. https://investors.duolingo.com/news-releases
19. Duolingo, Inc. (2025). *Shareholder letters and quarterly reports (Form 10-Q), FY2025*. U.S. Securities and Exchange Commission. https://investors.duolingo.com/financial-information/sec-filings (Max-tier monetization drivers and daily-active-user trajectory.)
20. TechCrunch. (2025, August 7). *The backlash against Duolingo going 'AI-first' didn't even matter*. https://techcrunch.com/2025/08/07/the-backlash-against-duolingo-going-ai-first-didnt-even-matter/ (The "AI-first" memo, the consumer backlash, and the initial financial resilience; the late-2025 engagement-driven share repricing is covered in the filings cited in Reference 19.)
21. Grand View Research. (2025). *AI video generator market size, share & trends analysis report, 2025–2033*. https://www.grandviewresearch.com/industry-analysis/ai-video-generator-market-report (Global market of $788.5M in 2025; ~20.3% CAGR, 2026–2033. Vendor-published market sizing; see Appendix B.3.)
22. Gower Street Analytics. (2026). *Global theatrical box office, 2025*. https://gower.st/ (~$33.5B.)
23. Uber Technologies, Inc. (2024–2026). *Quarterly and annual reports and earnings releases (Forms 8-K, 10-Q, 10-K), Q1 2024–Q1 2026*. U.S. Securities and Exchange Commission. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001543151&type=10-Q (Quarterly revenue and year-over-year growth; R&D expense; operating-income volatility; the Q3 2025 $4.9B tax-valuation release recognized through the tax provision in net income.)
24. *The Information*. (2026, April 14). *Uber CTO shows how Claude Code can blow up AI budgets*. https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets (December 2025 firm-wide rollout; per-engineer API costs; 2026 AI budget exhaustion; 32%→84% engineer adoption, February–March 2026.)
25. *Fortune*. (2026, May 26). *Uber's COO says it's getting harder to justify the company's AI spend: 'That link is not there yet.'* https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/ ("Not there yet"; "very hard to draw a line"; COO and CTO remarks on AI tooling ROI and budgeting.)
26. Klarna Group plc. (2025–2026). *Registration statement (Form F-1) and investor-relations releases*. U.S. Securities and Exchange Commission. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=klarna (Revenue per employee, headcount trajectory, operating-expense growth, and AI attribution in customer service.)
27. Anthropic. (2025–2026). *Anthropic economic index* [Successive editions]. https://www.anthropic.com/economic-index (Occupation-level composition of AI assistant usage; over-representation of computer and mathematical occupations.)
28. U.S. Census Bureau. (2025–2026). *Business trends and outlook survey: Artificial intelligence supplement* [Successive waves]. https://www.census.gov/hfp/btos/ (Firm-level AI adoption ~18% in late-2025 waves, ~19.8% by May 2026; information ~40%, finance and insurance ~34%. See also the Bureau's May 2026 summary: https://www.census.gov/library/stories/2026/05/ai-use-businesses.html)
29. Challapally, A., Pease, C., Raskar, R., & Chari, P. (2025, July). *The GenAI divide: State of AI in business 2025* [Preliminary report]. MIT Project NANDA. https://nanda.media.mit.edu/ (Share of enterprise generative-AI pilots without measurable P&L impact, ~95%; see Appendix B.3 on methodology.)
30. Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, *13*(1), 333–372. https://doi.org/10.1257/mac.20180386
31. David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. *American Economic Review*, *80*(2), 355–361. https://www.jstor.org/stable/2006600 (Papers and Proceedings.)
32. Solow, R. M. (1987, July 12). We'd better watch out. *New York Times Book Review*, 36. (Origin of the productivity-paradox formulation this report's title inherits.)
