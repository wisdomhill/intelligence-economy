---
title: "4. The SaaS Apocalypse Question"
subtitle: "A critical examination of the enterprise SaaS ecosystem in the agentic transition"
series: "The Intelligence Economy"
number: 4
manuscript-revision: 1
date: 2026-08-24
date-modified: 2026-08-24
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  Thirty incumbents, audited. Why the two-front erosion is real but the
  apocalypse is not, why the toll problem squeezes incumbents whichever way
  they turn, and what gridlock hands to the insurgents.

keywords:
  - enterprise SaaS
  - agentic transition
  - toll problem
  - seat pricing
  - interface layer
  - incumbent gridlock

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
published:
  dir: reports/r04/
  pdf: r04-the-saas-apocalypse-question.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r04/

chapters:
  - manuscript: "1. The Question: Anatomy of a Panic"
    published:  "1. Anatomy of a Panic"
    fragment:   _01-the-question.qmd
    page:       01-the-question.qmd
  - manuscript: "2. The Anatomy: Three Layers, Three Leaks"
    published:  "2. Three Layers, Three Leaks"
    fragment:   _02-three-layers.qmd
    page:       02-three-layers.qmd
  - manuscript: "3. The Toll Problem: The First User That Reads the Price List"
    published:  "3. The Toll Problem"
    fragment:   _03-toll-problem.qmd
    page:       03-toll-problem.qmd
  - manuscript: "4. The Thirty: What the Market Already Believes"
    published:  "4. The Thirty"
    fragment:   _04-the-thirty.qmd
    page:       04-the-thirty.qmd
  - manuscript: "5. The Open Facade: From Walled Gardens to Toll Plazas"
    published:  "5. The Open Facade"
    fragment:   _05-open-facade.qmd
    page:       05-open-facade.qmd
  - manuscript: "6. Six Functions Under Audit"
    published:  "6. Six Functions Under Audit"
    fragment:   _06-six-functions.qmd
    page:       06-six-functions.qmd
  - manuscript: "7. The Verdict: Gridlock, Not Apocalypse"
    published:  "7. Gridlock, Not Apocalypse"
    fragment:   _07-verdict.qmd
    page:       07-verdict.qmd
  - manuscript:
      - "Methodological Note"
      - "References"
    published:  "Methodology and References"
    fragment:   _08-methodology-and-references.qmd
    page:       08-methodology-and-references.qmd
---
# The SaaS Apocalypse Question

### A Critical Examination of the Enterprise SaaS Ecosystem in the Agentic Transition

**The Intelligence Economy — Report 4 of 14**\
**Wisdom Hill Research | Thematic Investment Research | July 2026**

---

## Executive Summary

In the first half of 2026, the market did something unusual: it named its own panic. The "SaaSpocalypse" — the violent de-rating of application software that began in late 2025 and accelerated after Anthropic's Claude Cowork professional-plug-in expansion at the turn of February 2026 — wiped roughly $1.8 trillion of market value off twenty of the thirty companies in this report's software universe in six months, even as ten others gained nearly $1 trillion. The question this report examines is whether the panic's underlying thesis is correct.

Our answer is that the apocalypse framing is directionally right about the pressure and wrong about the mechanism. The largest software companies are not being killed by agentic AI, and they are not refusing it. The major incumbents examined in this report have, in the past eighteen months, adopted the open agent protocols — MCP servers at Salesforce and ServiceNow, MCP and A2A gateways at Workday, protocol endorsements across the industry. The walled garden, as a description of incumbent behavior, is dead. What replaced it is subtler and, for investors, more consequential: **openness at the protocol layer, closure rebuilt at the control and price layers.** The flagship incumbents now speak the same protocols, and each demands to be the registry, the trust layer, the meter, and the toll booth through which agent traffic flows. The industry has not built a mesh; it has built N competing tollgates, each declaring itself the center.

This defensive architecture collides with a new economic fact that we call the toll problem: for the first time in software history, the marginal user reads the price list. Human users touch software dozens of times a day and never optimize their own usage costs; agents touch it thousands of times a day and can be programmed to minimize cost per task in real time. Usage-based pricing set at human-era rates — the incumbents' chosen escape route from per-seat decay — is therefore self-defeating: rates high enough to replace seat revenue suppress the very machine-scale usage that consumption models require.

The capitalization table already reflects this. The dividing line in H1 2026 was not vertical versus horizontal, nor AI-exposed versus not. It was **the denomination of revenue**: the H1 gainers were, almost without exception, companies whose revenue scales with the number and activity of machine actors (security, observability, communications infrastructure, data platforms), re-rating upward by 18–94%, while companies whose revenue scales with the number of human seats (CRM, ITSM workflow, HCM, finance applications, productivity suites) de-rated by 15–61% — regardless of the quality of their AI announcements. Machine denomination was close to necessary for a re-rating, not sufficient for one (§4.3).

The report's conclusion for investors is a squeeze theorem: an incumbent that holds the toll line defends margin and loses share; an incumbent that opens to machine-scale pricing defends share and loses margin. Either branch impairs enterprise value, which is why the market has de-rated franchises whose quarterly results continue to beat. Against challengers whose development costs have collapsed with coding agents and whose reservation profit is survival, defending growth and margin simultaneously is close to impossible. The incumbents' gridlock, meanwhile, is itself the strongest force pushing traffic, data, and developers toward the open alternative — the subject of our next report.

---

# 1. The Question: Anatomy of a Panic

## 1.1 The Market Has Already Named It

Financial writing usually supplies the labels after the fact. This time the market coined its own: press coverage of the early-2026 software crash routinely refers to the "SaaSpocalypse" — an investor panic premised on the idea that AI will destroy the business model of application software companies [14]. The sector's benchmark software index had fallen roughly 30% from its late-September 2025 peak by early February, one of the sector's steepest drawdowns outside a broad economic contraction [23]. Within our thirty-company universe (Chapter 4), the aggregate market capitalization fell from approximately $11.41 trillion at the end of 2025 to $10.57 trillion on July 1, 2026 — a decline of 7.4% that conceals the real story: excluding Alphabet, the remaining twenty-nine names fell 18.5% in six months, with twenty decliners losing about $1.79 trillion while ten gainers added roughly $0.95 trillion.

Two features distinguish this episode from an ordinary growth-stock correction. First, its trigger was technological rather than macroeconomic: the February leg of the selloff accelerated following Anthropic's Claude Cowork professional-plug-in expansion — reported in parts of the financial press, loosely, as a new Claude release [12][14], after Intuit — the episode's emblematic casualty — had already entered a correction over the preceding months, sliding roughly a third from early November 2025 to early February 2026 as investors concluded that guided tax and accounting workflows were now directly replicable by general-purpose AI [13]. By June, Intuit had become the worst performer in the S&P 500 for the year, down more than half, with sell-side research explicitly naming AI-native competitors — "Perplexity Tax," "Chime Tax" — as the threat vector [12]. Second, the de-rating has proceeded largely independently of reported fundamentals. Intuit's May quarter beat expectations and management raised guidance; the stock fell anyway [16][17]. The market is not pricing the quarter. It is pricing a structural thesis. This report asks whether that thesis is correct — and finds that the market's instinct is sound but its stated mechanism is not.

## 1.2 Force One — AI as Builder: The Entry Barrier Collapses

The first force is familiar from earlier reports in this series but bears restating because it defines the challenger's economics. Generative development has collapsed the fixed cost of producing credible enterprise software. What required a funded engineering organization in 2020 — a working CRM, a close-automation suite, a service desk — can now be assembled by small teams whose primary workforce is coding agents. The most telling testimony comes not from startups but from the incumbents' own analysts: reviewing Workday's strategy, Josh Bersin observed that after the industry's collective experience with Claude Code, Codex, and Cursor, it has become easy to imagine rebuilding an HCM system from scratch [9]. When the analyst community covering a $32 billion incumbent treats ground-up reconstruction of its category as *imaginable*, the barrier that justified the incumbent's multiple has already moved.

What has not collapsed is the cost of *running* enterprise software: compliance regimes, uptime, security posture, data custody, enterprise sales. This distinction — build versus run — is the incumbents' remaining structural defense, and Chapters 5 and 6 examine how they are attempting to monetize it. But a defense located in operations rather than in product is a defense of margin structure, not of growth.

## 1.3 Force Two — AI as User: The Definition of Good Software Inverts

The second force is a requirements discontinuity. For thirty years, "good enterprise software" meant a polished graphical interface, trained users, and workflows optimized for human cognition. When the marginal user becomes an agent, every one of those virtues inverts. The GUI that embodied decades of design investment becomes a cost: an agent operating a screen must tokenize it, parse it, and simulate clicks — an interaction mode that is slow, brittle, and expensive relative to structured API access. The training that created human switching costs becomes irrelevant: an agent has no muscle memory to lose. The workflow choreography that differentiated products becomes invisible: an agent does not care where the button was.

Software history suggests that requirement discontinuities of this magnitude structurally favor entrants, because incumbents must retrofit while entrants design natively — and because the incumbent's retrofit cannibalizes the very properties (seats, screens, training) on which its revenue model rests. The agentic discontinuity is unusually severe on this score: it attacks not only the product architecture but the pricing unit itself, a problem developed in full in Chapter 3.

## 1.4 The Two-Front Erosion

These forces attack the incumbent on two fronts simultaneously. Inside the installed base, agents compress the demand for seats — the ratio of work to human operators rises — and procurement gains a credible alternative with which to negotiate price. This front erodes slowly, because migration costs are real; it manifests as decelerating seat growth, discounting, and net-revenue-retention decay rather than as visible churn. At the greenfield edge, the erosion is immediate: new companies, new departments, and new projects — the top of every SaaS land-and-expand funnel — increasingly default to agent-native alternatives, in the same way that a generation of startups defaulted to MySQL and PostgreSQL and simply never became Oracle customers. Oracle did not lose those accounts; it never met them. The database incumbents survived that generational bypass because their installed base was profoundly locked in. The question this report poses function by function is which application franchises enjoy comparable lock-in — and the answer, developed in Chapter 6, is: fewer than their valuations assumed in 2021, and fewer than their managements assert today.

## 1.5 Why Enterprise Value, Not Merely Revenue

The valuation mathematics of growth software punishes this configuration nonlinearly. A SaaS multiple is a compound claim: on the durability of growth (retention plus expansion plus new logos) and on the terminal margin structure (pricing power at scale). The two-front erosion impairs both claims at once — greenfield loss shortens the growth runway while installed-base pressure caps the terminal margin — and a simultaneous impairment of both terms does not subtract from a multiple; it re-bases it. This is why H1 2026 produced declines of 44–61% in franchises whose revenues are still growing: Salesforce (−47%), Workday (−45%), Adobe (−44%), Atlassian (−51%), Intuit (−61%) [1]. The market is not forecasting collapse next quarter. It is repricing the probability distribution of the terminal state.

## 1.6 The Question, Stated Falsifiably

"Apocalypse" is a slogan, not a hypothesis. We restate it as three testable candidates. **Hypothesis A — Extinction:** the application layer dissolves; agents operating on open data substrates absorb its functions; incumbent equity approaches terminal decline. **Hypothesis B — False alarm:** incumbency absorbs the transition; protocol adoption plus installed-base lock-in preserve both growth and margin; the de-rating reverses. **Hypothesis C — Dispersion with defensive closure:** incumbents survive, but by privatizing the agentic transition behind their own gates — defending margin at the expense of share, or share at the expense of margin — while ceding ecosystem leadership; enterprise value settles structurally lower, with wide dispersion by function and by revenue denomination. The remainder of this report audits the evidence. We will conclude for Hypothesis C, and we will state in Chapter 7 what evidence would force us to revise.

---

# 2. The Anatomy: Three Layers, Three Leaks

An enterprise application is a bundle of three assets: an interface, a body of business logic, and an authoritative data store. The bundle commanded a premium because the three reinforced one another — the interface created habit, habit created data, data made the logic hard to replicate. The agentic transition unbundles them, and value leaks from each layer in a different way.

## 2.1 The Interface Layer: From Asset to Liability

The interface was the incumbents' most visible moat: retraining costs, certification ecosystems, administrator guilds, the sheer organizational pain of moving ten thousand employees to a new screen. Agents dissolve this moat by construction — they have no habits — and then invert it into a liability. Serving an agent through a human interface multiplies the cost of every interaction (Chapter 3 quantifies this as the token tax), so the incumbent is compelled to build the headless access paths — APIs, MCP servers, action endpoints — that make its screens optional. The major platforms examined in this report have now done so. But a headless endpoint is a strange kind of moat: it is precisely the interface a competitor's agent, or a customer's own orchestration, uses to treat the incumbent as a replaceable backend. The interface layer's contribution to enterprise value is converging toward zero, and in the transition it is a cost center.

## 2.2 The Logic Layer: Commoditization

The second layer — scoring rules, routing heuristics, approval chains, campaign logic, close checklists — was defensible when encoding it required years of domain-expert engineering. General-purpose models now reproduce the great bulk of horizontal business logic on demand, and undisclosed logic is no longer presumptively superior logic: a frontier model's recommendation engine, drawing on broad data, frequently outperforms a decade-old proprietary heuristic. The surviving exceptions are logic fused to proprietary data feedback loops — fraud models trained on payment flows the challenger cannot see, threat detection trained on telemetry the challenger cannot collect. It is not incidental that the H1 2026 winners in our universe (Chapter 4) cluster exactly there: security and observability franchises whose logic is inseparable from exclusive, continuously refreshed machine data.

## 2.3 The Database Layer: The Real Lock-In and Its Erosion

The deepest layer is the one incumbents rightly call their moat — but the moat was never the database engine. It is the schema, the semantic model, the metadata, and above all the **authoritative write path**: the fact that the incumbent's ledger, employee record, or customer object is the version of reality on which audits, payrolls, and regulators rely. This is genuine lock-in, and it is being eroded from below rather than assaulted from the front. Open table formats and the lakehouse pattern have normalized the expectation that enterprise data lives in customer-controlled substrates; zero-copy sharing arrangements — which nearly every major application vendor has now signed with the data-platform layer — concede the principle that the application's data is queryable outside the application. The concession is asymmetric in an underappreciated way: it opens the *read* path while incumbents retain the *write* path, and write authority — the right to change the record, with the governance that implies — is the hardest asset in this report to disrupt. Chapter 6 scores each function on precisely this axis. But a read-open, write-closed posture has a corollary the incumbents did not intend: it invites exactly the extract-once, analyze-elsewhere behavior that Chapter 3 identifies as the rational response to toll pricing.

## 2.4 Synthesis: A Thinner and Thinner Application

Put the three leaks together and the packaged application becomes structurally thinner: its interface optional, its logic reproducible, its data readable from outside. What remains genuinely scarce is write authority, regulatory embedding, and operational trust — real assets, but narrower than the bundle whose price the 2021 multiples capitalized. The strategic question for each incumbent is how to monetize the narrow assets without accelerating the leaks from the wide ones. Their collective answer, as Chapter 5 documents, has been to open the protocols and meter the gates. Whether that answer can hold is the question of the second half of this report.

---

# 3. The Toll Problem: The First User That Reads the Price List

## 3.1 A Discontinuity of Scale

A human knowledge worker interacts with a given enterprise application perhaps a few dozen times a day. An agent assigned to the same domain does not "use" the application in that sense at all: it monitors continuously, reconciles across systems, retries, verifies, and analyzes in bulk. Its natural interaction volume is thousands to tens of thousands of calls per day — not because it is inefficient, but because that is what continuous operation of a business process means. The transition from human to agentic usage is therefore not a growth curve; it is a discontinuity of two to three orders of magnitude in the number of billable events, and every pricing decision an incumbent makes must now be evaluated against that discontinuity.

## 3.2 The First Tax: The Token Tax

Before any vendor charge applies, agentic access to seat-era software carries an intrinsic cost premium. An agent that must operate a graphical interface pays in inference: screenshots tokenized, DOM trees parsed, click sequences simulated and re-verified when layouts shift. Interaction for interaction, GUI mediation costs multiples of what a structured API call costs, in both latency and compute. This is the token tax, and it is a design inheritance: software optimized for human eyes charges machine users a surcharge simply for not being human. Incumbents understand this, which is why the flagship platforms have shipped headless access over the last eighteen months. But headless access forces the pricing question they had deferred — because once the agent can reach the system cheaply in compute terms, the only remaining governor on machine-scale usage is the price.

## 3.3 The Second Tax: The Toll Tax

Here the incumbents have converged, with remarkable uniformity, on the same answer: meter it. Workday's Agent Gateway admits external agents over MCP and A2A, while direct calls to Workday's APIs are metered per call — a charge the company frames as capturing previously uncollected value; its broader pricing is shifting from seats to a hybrid of seats plus consumption denominated in "Flex Credits" [9][10]. ServiceNow's Action Fabric exposes the platform's full system of action through a generally available MCP server — and every headless action consumes the same "Assist" currency that meters its native AI SKUs, with consumption metering built into the MCP Server Console alongside identity and audit controls [5][7]. Salesforce's hosted MCP servers are available to Enterprise Edition orgs today, with pricing terms undisclosed, and run inside an entitlement-and-governance regime whose per-user authentication and admin-scoped tool packages make future metering administratively trivial [2].

The economic logic of these meters deserves to be stated plainly. An incumbent converting seat revenue to usage revenue while defending its P&L must set rates that are implicitly reverse-engineered from human-era unit economics: the annual seat fee divided by the annual interaction count of a *human* user. Applied to machine traffic running at a hundred to a thousand times human volume, those rates produce invoices no rational customer will pay for at-scale agentic operation. The toll is human-era pricing applied to machine-era traffic — the per-minute long-distance tariff billed against internet-scale data.

## 3.4 Multiplicative Stacking

The two taxes compound. Where the agent must still traverse interfaces, each interaction is token-expensive; where headless paths exist, each interaction is toll-expensive; across a workflow spanning several incumbent systems, the taxes multiply through every hop. The result is that the economic ceiling on an incumbent application's value to an agentic enterprise is set not by what the software can do but by what access to it costs — a constraint that never bound in the human era, because human usage volumes made per-interaction economics invisible.

## 3.5 The First User That Reads the Price List

The deeper break is behavioral. In the entire history of commercial software, the user has never been price-sensitive at the point of use: the company pays, the employee clicks, and no human has ever chosen not to open a dashboard because the marginal query was expensive. Agents end this. An orchestrator can be programmed — trivially, and increasingly is by default — to minimize cost per completed task: to extract data once and cache it in an open substrate rather than query repeatedly through a toll; to prefer zero-copy read paths the incumbents themselves have signed; to route a task to a cheaper functional equivalent when one exists. Software has acquired, for the first time, a user that reads the price list, compares routes, and remembers. The price elasticity of software usage, effectively zero for forty years, jumps discontinuously — and it jumps precisely at the moment incumbents are re-basing their revenue models onto usage.

## 3.6 The Incumbent's Self-Contradiction

This is why the consumption transition, presented on every earnings call as the escape route from per-seat decay, is better understood as the dilemma restated. For consumption revenue to replace seat revenue, rates must be high; at high rates, machine-scale volume — the only volume there is — routes around the meter, and the consumption line disappoints. At rates low enough to attract machine-scale volume, the revenue replacement fails and the margin structure built under the seat umbrella deflates. The bull case requires high rates *and* high volume from a customer who, for the first time, is algorithmically optimizing against exactly that combination. A high toll is, in the end, a tax the incumbent levies on its own data gravity: every expensive call is an argument for extracting the data once and never calling again.

## 3.7 What Would Falsify This

The toll argument would be materially weakened by the appearance of a successful **agent tier**: machine-traffic pricing set near marginal cost that demonstrably absorbs volume while preserving consolidated margins, disclosed in a consumption mix that grows faster than seat revenue declines. As of this writing, no incumbent in our universe has published such a tier or such a mix; Workday's Flex Credits and ServiceNow's Assist currency are steps toward consumption *accounting*, not yet evidence of consumption *economics* that clear the bar. FY2026 disclosures will be the first test, and Chapter 7 lists this among our watch items.

---

# 4. The Thirty: What the Market Already Believes

## 4.1 Universe Construction

The analysis that follows is anchored to a defined universe: thirty large listed software companies drawn from the CompaniesMarketCap software ranking [1], with market capitalizations recorded at two dates — the last trading day of 2025 and July 1, 2026. Two limits govern what the table can bear. It is a selected universe, not a mechanical top-thirty: the underlying ranking updates continuously, and the thirty names here reflect the categorization and exclusion criteria stated below rather than a snapshot reproducible at either measurement date. And it measures market capitalization, not shareholder return: capitalization moves with share issuance and buybacks as well as with price, so these are not returns. The distortion is material in one case, Palo Alto Networks, whose H1 2026 capitalization change incorporates shares issued for the CyberArk acquisition and therefore overstates its price appreciation; that figure is qualified wherever it appears. The dispersion pattern the table reveals does not rest on the affected magnitudes. Conglomerates whose software franchises are inseparable from their equity story (Alphabet, Microsoft, Oracle, IBM) are included; security vendors are included; firms whose primary business is not software (hardware, industrial systems, measurement, crypto-treasury vehicles) are excluded at source by the ranking's categorization. Each company carries a single functional classification from a fixed taxonomy: **Productivity, Front Office, Back Office, HCM, ITSM, Infrastructure, System Integration, Commerce/Marketing, Data Infra, and Vertical/Engineering.** The first six are this report's analytical subjects; the last four are recorded, discussed where they illuminate the argument, and excluded from the function audits for reasons stated in §4.4.

## 4.2 The Table

| # | Company (Ticker) | Functional Classification | Core Software Segment | Mkt Cap, End-2025 ($B) | Mkt Cap, Jul 1 2026 ($B) | H1 2026 Change |
|---|---|---|---|---|---|---|
| 1 | Alphabet (GOOG) | Productivity | Google Workspace, Cloud Infrastructure, Generative AI | 3,802.00 | 4,367.00 | +14.86% |
| 2 | Microsoft (MSFT) | Productivity | Windows OS, M365 Suite, Azure Cloud, Copilot Ecosystem | 3,625.00 | 2,854.00 | −21.27% |
| 3 | Oracle (ORCL) | Back Office | Enterprise DBMS, Oracle Cloud Infrastructure (OCI), ERP Solutions | 568.85 | 410.46 | −27.85% |
| 4 | Palantir (PLTR) | System Integration | Big Data Analytics Operating Systems & AI Orchestration (AIP) | 449.77 | 301.41 | −32.99% |
| 5 | Palo Alto Networks (PANW) | Infrastructure | Enterprise Zero-Trust Network Cybersecurity Platforms | 131.34 | 286.91 | +118.45% |
| 6 | IBM (IBM) | System Integration | Hybrid Cloud Foundations, IT Consulting, and Watsonx AI | 285.17 | 269.04 | −5.66% |
| 7 | CrowdStrike (CRWD) | Infrastructure | Cloud-Native Endpoint Telemetry & Threat Intelligence Security | 121.30 | 196.71 | +62.17% |
| 8 | AppLovin (APP) | Commerce/Marketing | AI-powered Mobile Ad Matching & App Marketing Automation Platforms | 241.58 | 189.67 | −21.49% |
| 9 | SAP (SAP) | Back Office | Global Enterprise Resource Planning (ERP) Cloud Software | 287.68 | 187.62 | −34.78% |
| 10 | Shopify (SHOP) | Commerce/Marketing | Independent E-commerce Storefront Setup & Omnichannel Operations SaaS | 222.39 | 157.83 | −29.03% |
| 11 | Salesforce (CRM) | Front Office | Customer Relationship Management (CRM) SaaS & Data Cloud | 253.30 | 133.68 | −47.22% |
| 12 | Fortinet (FTNT) | Infrastructure | Unified SASE Architecture & Enterprise Hardware/Software Firewalls | 62.49 | 116.47 | +86.38% |
| 13 | ServiceNow (NOW) | ITSM | Enterprise IT Operating Systems & Cross-Departmental Workflow Automation | 159.79 | 109.11 | −31.72% |
| 14 | Cadence Design Systems (CDNS) | Vertical/Engineering | Electronic Design Automation (EDA) Software & Silicon Emulation | 86.89 | 104.18 | +19.90% |
| 15 | Datadog (DDOG) | ITSM | Multi-Cloud Infrastructure Monitoring, Log Analytics & Observability | 48.50 | 94.14 | +94.10% |
| 16 | Snowflake (SNOW) | Data Infra | Multi-Cloud Unified Data Warehouse & Enterprise Data Cloud Platforms | 76.61 | 90.52 | +18.16% |
| 17 | Automatic Data Processing (ADP) | HCM | Global Human Capital Management (HCM) & Cloud Payroll Outsourcing | 104.85 | 89.52 | −14.62% |
| 18 | Cloudflare (NET) | Infrastructure | Edge Computing Runtimes, Global CDN, and Web Application Security | 70.89 | 87.42 | +23.32% |
| 19 | Synopsys (SNPS) | Vertical/Engineering | Semiconductor Intellectual Property (IP) & EDA Software Tools | 91.28 | 87.03 | −4.66% |
| 20 | Adobe (ADBE) | Productivity | Creative Cloud Design Suites & Digital Experience Marketing SaaS | 150.08 | 83.86 | −44.12% |
| 21 | Intuit (INTU) | Back Office | Consumer/SMB Tax Filing (TurboTax) & Accounting (QuickBooks) Engines | 188.35 | 73.05 | −61.21% |
| 22 | Autodesk (ADSK) | Vertical/Engineering | Industry-Standard 3D Architecture, Engineering, and Manufacturing Design CAD | 64.05 | 42.17 | −34.16% |
| 23 | Constellation Software (CSU.TO) | Vertical/Engineering | Acquisition & Operation Holding Group for Vertical Market Software (VMS) | 51.40 | 39.81 | −22.55% |
| 24 | Workday (WDAY) | HCM | Large Enterprise Cloud Core Human Resources & Financial Management ERP | 58.92 | 32.17 | −45.40% |
| 25 | Twilio (TWLO) | Infrastructure | Developer-First Cloud Communications APIs (Automated SMS, Voice, and Auth) | 21.55 | 31.76 | +47.38% |
| 26 | Veeva Systems (VEEV) | Vertical/Engineering | Life Sciences, Biotech, and Pharmaceutical Specialization Cloud CRM & Data | 36.92 | 28.82 | −21.94% |
| 27 | Fair Isaac (FICO) | Vertical/Engineering | Global Financial Predictive Analytics & Consumer Credit Scoring Models | 42.08 | 27.98 | −33.51% |
| 28 | MongoDB (MDB) | Data Infra | Developer-Centric Distributed NoSQL Cloud Document Database (Atlas) | 35.47 | 27.01 | −23.85% |
| 29 | Zoom (ZM) | Productivity | Global Enterprise Video Architecture, Virtual Telephony, and AI Collaboration | 26.34 | 26.42 | +0.30% |
| 30 | Atlassian (TEAM) | ITSM | Developer Project Management, Issue Tracking (Jira), and Team Collaboration | 42.94 | 21.10 | −50.86% |

*Source: CompaniesMarketCap [1]; classifications per this report's taxonomy. Changes are in market capitalization, not shareholder return (§4.1); PANW's figure incorporates shares issued for the CyberArk acquisition. Aggregates: end-2025 ≈ $11,408B; July 1, 2026 ≈ $10,567B (−7.4%; −18.5% excluding Alphabet).*

## 4.3 Reading the Dispersion

The table rewards careful reading, because the pattern it contains is sharper than the "AI kills SaaS" slogan and different from the one we expected before compiling it.

Begin with what did *not* happen. The dispersion is not vertical versus horizontal: the Vertical/Engineering cohort, whose regulatory embedding and domain-specific logic might have been expected to shelter it, fell almost across the board — Autodesk −34%, FICO −34%, Constellation −23%, Veeva −22%, Synopsys −5% — with Cadence (+20%) the lone gainer on AI-silicon design demand. Nor is it AI-exposure versus AI-absence: Palantir, the market's flagship AI name, fell 33% from an end-2025 capitalization that embodied extreme expectations, and Microsoft — owner of the most heavily marketed AI assistant franchise in enterprise software — fell 21%. The market did not buy "AI stories" in H1 2026; it sold several of the biggest ones.

What it bought, with striking consistency, is a specific revenue structure. Rank the thirty by H1 performance and the gainers are: Palo Alto Networks (+118%, inflated by CyberArk acquisition shares), Datadog (+94%), Fortinet (+86%), CrowdStrike (+62%), Twilio (+47%), Cloudflare (+23%), Cadence (+20%), Snowflake (+18%), Alphabet (+15%), Zoom (flat). Set aside Alphabet (a full-stack AI story of its own) and Cadence (an AI-capex derivative), and every major gainer shares one property: **its revenue is denominated in machine activity, not human seats.** Security platforms bill on the devices, workloads, and — increasingly — non-human identities they protect; agents multiply all three. Observability bills on telemetry volume; agents that act generate machine-scale exhaust to monitor, and Datadog's +94% against ServiceNow's −32% *within the same ITSM classification* is the cleanest natural experiment in the table — the market paying nearly double for the company that watches machine actors while marking down the company that routes human tickets. Twilio bills per message and call; agents that execute workflows send them. Snowflake bills on compute consumed; agents that analyze, query. The mapping runs one way, and the table's own residual proves it: MongoDB, consumption-billed like Snowflake, fell 24% — machine denomination was close to necessary for an H1 re-rating, not sufficient for one.

Now read the decliners: Salesforce −47%, Workday −45%, Adobe −44%, Atlassian −51%, Intuit −61%, SAP −35%, ServiceNow −32%, ADP −15%, Microsoft −21%. Different functions, different qualities of business, one shared property: revenue denominated in human seats or human-performed workflows — the denominator that agentic substitution shrinks. The market's implicit model, in other words, is precisely the toll problem of Chapter 3 read as a valuation rule: *revenue per human* is a melting asset; *revenue per machine action* is an expanding one. The aggregate arithmetic drives the point home. CrowdStrike, Fortinet, and Cloudflare — three security-and-edge names whose capitalizations moved on price rather than on acquisition issuance — gained roughly 57% between them in six months. Add Palo Alto Networks and the four were worth $688B on July 1, more than Salesforce, Adobe, ServiceNow, Workday, Intuit, and Atlassian *combined* ($453B). Five years ago that comparison would have been a misprint.

One caution belongs in the record. Market prices are a hypothesis, not a verdict; H1 2026 also contains momentum, crowding, and the mechanical violence of multiple compression from extreme starting points (Palantir's decline says as much about its end-2025 valuation as about its prospects). This report treats the table as the market's *claim* — a claim we audit, not one we assume.

## 4.4 Scope Declaration: Horizontal Functions Only

The audits of Chapter 6 cover the six functions where the agentic exposure logic of Chapters 1–3 applies directly and comparably: **Productivity, Front Office, Back Office, HCM, ITSM, and Infrastructure** — eighteen of the thirty companies. The remaining twelve are recorded but not audited, for stated reasons rather than convenience. The Vertical/Engineering cohort (Cadence, Synopsys, Autodesk, Constellation, Veeva, FICO) is excluded because its exposure runs through different machinery: regulatory embedding, decades of domain physics, and coupling to physical-world processes make both the threat model and the defense model non-comparable to horizontal software — though, as §4.3 recorded, exclusion from *this analysis* is not exemption from *the de-rating*, and the cohort's H1 performance should temper any assumption that verticality is safety. Design deserves a sentence of its own: it is a real function with a real agentic story, but Adobe is its only top-30 representative (Figma trades far below the cut), leaving no cohort to audit; we treat Adobe within Productivity per the classification. System Integration (Palantir, IBM) is a services-and-platform model whose economics this series treats separately; Commerce/Marketing (AppLovin, Shopify) monetizes transactions rather than seats and faces the agentic transition as a demand-side question; Data Infra (Snowflake, MongoDB) is the substrate *toward which* the leaks of Chapter 2 flow, and appears throughout this report as context rather than as a subject.

---

# 5. The Open Facade: From Walled Gardens to Toll Plazas

## 5.1 The Walled-Garden Era, as History

Any honest account of the enterprise software ecosystem before 2025 describes an archipelago of gated platforms. Integration ran through certified partners and paid marketplaces; API access was rationed by edition tier and rate limit; data egress was frictional by design; and the N-squared cost of point-to-point connectors — mitigated but never eliminated by the integration-platform industry — functioned as a standing tax on the customer's own data estate, with human employees serving as the middleware of last resort, swivel-chairing context between systems that would not speak to one another. It is important to write this in the past tense, because the standard critique of enterprise incumbents — *they will refuse the open protocols* — is the one thing that demonstrably did not happen.

## 5.2 The Gates Open, 2025–2026

The empirical record of the last eighteen months is a procession of gate-openings. Anthropic published the Model Context Protocol as an open standard in November 2024 [18]; Google followed with the Agent2Agent protocol in April 2025, launching with more than fifty partners, an endorsement list on which the major application incumbents duly appeared [19]. Salesforce piloted hosted MCP servers in spring 2025, took them to beta in October, and shipped general availability in April 2026 — Salesforce-managed endpoints that expose an org's data, flows, Apex actions, and queries to *any* MCP-speaking client, explicitly including Claude and ChatGPT, available to Enterprise Edition orgs [2][3]. ServiceNow, at Knowledge 2026, went further than data access: Action Fabric opens the platform's "full system of action" — flows, playbooks, approvals, catalogs — to any external agent through a generally available MCP server, with Anthropic as first design partner and A2A support alongside [5][21]. Workday announced its Agent Gateway in mid-2025 and took its Agent System of Record to general availability in February 2026, supporting MCP, A2A, and OpenTelemetry [10][11]. Whatever the SaaS apocalypse turns out to be, it will not be a story of incumbents refusing to interoperate. On paper, the agentic mesh's connective tissue now exists at every major node.

## 5.3 Protocol-Open, Control-Closed

Look one layer beneath the protocol announcements, however, and a second pattern appears with equal uniformity. Every opened gate runs through the vendor's own control apparatus. Salesforce's MCP servers execute every transaction as an authenticated user under the org's existing permission model, within admin-scoped tool packages and an entitlement regime — governance as product [2]. ServiceNow routes every Action Fabric call through AI Control Tower, where it is identity-verified, permission-scoped, audited, session-managed — and metered, with headless actions consuming the same Assist currency as native AI SKUs; the MCP Server Console ships with consumption metering as a first-class feature [5][7][22]. Workday admits external agents through Agent Gateway, with direct Workday API calls metered per call [9]. The openings are real, and so is what they are threaded through: registry, allowlist, trust layer, rate limiter, meter. Openness lives at the protocol layer; closure has been rebuilt, with considerable engineering seriousness, at the control and price layers. The toll problem of Chapter 3 is not an accident of pricing; it is the *mechanism* by which the open facade stays economically closed.

## 5.4 N Self-Declared Hubs

Read the incumbents' own framing side by side and the strategic symmetry becomes almost comic. ServiceNow's executive summary of its differentiation: others let agents read and write data; ServiceNow lets agents "execute governed work" — and its CEO describes the company as the "AI agent of agents," arguing openly that the more external agents execute through ServiceNow, the more operational data accumulates in its CMDB, and that the richest execution layer will attract the agents [7][20][22]. Workday positions its Agent System of Record as the registry and payroll of the blended human-digital workforce — the system *other* vendors' agents register with [10][11]. Salesforce's developer organization, announcing MCP general availability, reaches for the same altitude: CRM is "a capability, not a destination" — the destination, by implication, being the Salesforce platform through which every capability is governed [2]. Microsoft extends its governance across an Agent 365 ecosystem; every security vendor in Chapter 6 claims the agent-identity perimeter. Each of these strategies is individually coherent. Collectively they describe an industry in which every major node has declared itself the hub and invited every other node to be a spoke. The protocols solved connectivity; nobody has solved — because every incumbent is contesting — **topology**: who orchestrates whom, whose meter runs, whose registry is authoritative. The walled garden is dead. What stands in its place is N toll plazas, each flying an "open" flag, each priced on the assumption that the traffic has nowhere else to go.

## 5.5 The Audit Rubric

Chapter 6 scores each function's incumbents against this reality on four openness axes and three defensibility axes. Openness: **(i) MCP scope** — read-only, read-write, or governed action; **(ii) external orchestrability** — whether a third-party agent can direct the platform as a peer, or the platform's agents alone may direct others; **(iii) toll structure** — the metering basis and its posture toward machine-scale traffic; **(iv) semantic access** — whether schema, metadata, and business rules are legible to outside agents or reserved for the vendor's own. Defensibility, carried from Chapter 2: **write authority** over records of consequence; **logic specificity** fused to proprietary data loops; **task survival** — whether the function's underlying work grows, persists, or evaporates under agentic execution. The verdicts differ sharply by function; the openness scores barely differ at all — which is itself the finding.

---

# 6. Six Functions Under Audit

## 6.1 Productivity & Collaboration — Alphabet, Microsoft, Adobe, Zoom

The productivity franchises are the most interface-centric businesses in software: their product *is* the surface on which human work happens, priced per human. That was the strongest possible position in the seat era and is the most directly exposed one now, and the H1 tape splits the cohort accordingly. Alphabet (+15%) is the only member whose equity story is dominated by the layers beneath the surface — models, TPUs, cloud, and an advertising business agents do not threaten in the near term. Microsoft (−21%) carries the largest per-seat franchise in software history into the transition; Copilot is the industry's most aggressive attempt to re-price the seat upward before agents re-price it downward, and the market's H1 judgment suggests unresolved doubt that assistant attach rates outrun seat economics' decay. Adobe (−44%) faces the discontinuity in its rawest form: generative creation attacks the tool layer while Experience Cloud is seat-and-suite priced. Zoom (flat) is the cohort's residual — a communications utility whose modest valuation had already absorbed its growth question.

On the rubric: task survival here is genuinely ambiguous — documents, meetings, and messages persist, but the *authoring* of them is exactly what agents absorb first; write authority is weak (a document store is not a ledger); and the strategic significance of the function is shifting from the artifacts to the **context**: whoever holds the corpus of an organization's communication holds the grounding data every agent needs. That is why the most telling challenger signal is not a suite competitor but Glean — the enterprise-knowledge layer — and why Microsoft's and Google's real defense is not the document editor but the graph behind it. Verdict: exposure high and already priced in part; the residual moat is context custody, not seats.

## 6.2 Front Office (CRM & Customer Service) — Salesforce

Salesforce stands alone in the universe's Front Office classification (Microsoft's Dynamics, Oracle's and SAP's CX suites live inside other rows; HubSpot has fallen far below the cut), which makes its −47% the cleanest single-name referendum on application SaaS. It is also, to its credit, the most complete specimen of the open facade: hosted MCP servers at GA for every enterprise org, exposing data, flows, and actions to any client including rival assistants [2]; a Data 360 MCP server — in developer preview as of May 2026, self-hosted and single-client — extending the same posture to the data foundation [4]; and, on reported accounts, distribution of Agentforce experiences inside ChatGPT itself. No incumbent has opened more — and no incumbent's opening is more thoroughly threaded through its own permission model, entitlement regime, and platform gravity. On the rubric, Salesforce scores read-write-action on MCP scope and near the bottom on external orchestrability-as-peer: the architecture assumes Agentforce orchestrates, others contribute.

The function's fundamentals explain the market's severity. Task survival in customer service is the weakest in enterprise software — support interaction is the single most demonstrably agent-absorbable workload in the economy — and the challenger existence proof is unusually strong: Sierra sells outcome-priced customer-service agents; Clay and Attio rebuild the go-to-market stack agent-natively. What survives is the customer record's write authority and the surrounding compliance surface — real, but a narrow keep compared with the seat-and-cloud empire the multiple once capitalized. Verdict: the market's harshest application-layer judgment, and on this audit, not an irrational one.

## 6.3 Back Office (Core ERP & Finance) — Oracle, SAP, Intuit

Here sits the strongest defensive asset in the horizontal universe — and H1's most instructive contradiction. The ERP ledger is write authority in its purest form: the auditable record of money, embedded in regulation, the last system any CFO rips out. Agentic architectures to date overwhelmingly *overlay* the ledger rather than replace it, and both SAP (Joule and its agent program) and Oracle (agents across Fusion) are executing the overlay playbook, gated and metered in the pattern of Chapter 5. Yet SAP fell 35% and Oracle 28% — the market repricing not survival but *surplus*: an unbreachable system of record whose interaction layer, analytics, and expansion SKUs are being peeled away by agents leaves a smaller economic claim even if the core never churns.

Intuit (−61%) is the chapter's cautionary tale and the panic's epicenter. Its franchise looked reg-embedded — tax code, payroll compliance, accountant networks — but its actual product value lay in *guiding humans through* regulated workflows, and guided workflow is precisely what frontier models replicate; the stock had slid into a correction over the closing months of 2025 on exactly this fear [13], the decline steepened after the Cowork expansion at the turn of February [12][14], and by June sell-side research was naming AI-native tax entrants while the stock became the S&P 500's worst performer despite beating and raising [12][16][17], with the disruption narrative rather than the print driving the tape [15]. The lesson generalizes: regulatory embedding protects the *record*; it does not protect the *workflow around the record*, and most Back Office revenue is workflow. Challenger signal: the AI-native close (Numeric and peers) attacks exactly that seam. Verdict: strongest write authority in the report, weakest protection for everything wrapped around it.

## 6.4 Human Capital Management — Workday, ADP

HCM's problem is arithmetic before it is architectural: the function's pricing denominators — employees managed, payrolls run, seats provisioned — are the precise quantities agentic substitution shrinks. A sticky product on a contracting base can post flawless retention while its invoice declines; this is task-survival erosion in its purest financial form, and the market marked Workday −45% and ADP −15% (the gap reflecting ADP's payroll-processing annuity against Workday's enterprise-seat concentration).

Workday's response is the universe's most explicit toll architecture, and this report treats it as the reference case rather than an outlier: an Agent System of Record positioning Workday as registrar and governor of *everyone's* agents; an Agent Gateway admitting external agents via MCP and A2A while metering direct API calls per-call; a pricing shift to seats-plus-consumption via Flex Credits; and a Sana-based conversational front door intended to keep the interaction layer in-house [9][10][11]. Bersin's framing of the bet is candid — stop paying per employee for a system rarely used; pay for its actions instead [9] — and Chapter 3 has already stated why the bet is unstable: action-pricing at rates engineered to replace per-employee revenue is exactly the toll that machine-scale usage routes around. The absorption of Sana into Workday's front door, like Moveworks' into ServiceNow's, doubles as this function's challenger evidence: the challengers were valuable enough to buy. Rippling's compound, agent-forward architecture stands as the remaining independent existence proof. Verdict: the function where the denominator problem and the toll response meet head-on; the audit sides with the denominator.

## 6.5 IT Service Management & Operations — ServiceNow, Datadog, Atlassian

No classification in the universe contains a starker internal spread: Datadog +94%, ServiceNow −32%, Atlassian −51%. The spread is the thesis. Datadog sells *observation of machine activity* — telemetry, traces, logs — a demand that scales with the number of acting agents; it is machine-denominated revenue in nearly pure form. ServiceNow and Atlassian sell *coordination of human work* — tickets, queues, approvals routed among people — the workload agents absorb rather than generate.

ServiceNow's counter-strategy is the boldest in the report and deserves to be described in its own terms. At Knowledge 2026 it opened its full system of action to any external agent through a GA MCP server (Action Fabric), signed Anthropic as first design partner, consolidated Moveworks (acquired for $2.85B) into a unified front door, integrated Armis ($7.75B) and Veza into an agent-and-asset governance stack, extended AI Control Tower across even Microsoft's agent ecosystem [6][8], and articulated the endgame without embarrassment: govern and meter every agent in the enterprise, whoever built it — "Others let agents read and write data. We let agents execute governed work" [5][7][21][22]. It is the purest expression of the N-hubs strategy: if the service desk evaporates, become the tollgate through which its replacements are governed. The audit's reservation is the one that runs through this entire report: the tollgate earns its keep only if agent traffic consents to route through it at ServiceNow's meter, and every Assist-denominated headless action is a price signal to an orchestrator that reads prices. Verdict: the function contains both the transition's cleanest winner (observability) and its most sophisticated defensive architecture — and the market, for now, is paying for the former and discounting the latter.

## 6.6 Cybersecurity & Infrastructure — Palo Alto Networks, CrowdStrike, Fortinet, Cloudflare, Twilio

Infrastructure is the exception that proves the rule. Task survival here does not erode under agents — it compounds: every deployed agent is a new identity to govern, a new credential surface, a new source of machine-speed action requiring machine-speed defense; every agentic workflow generates communications (Twilio's meter), traffic (Cloudflare's), and endpoints and identities (the security trio's). This is machine-denominated revenue by construction, and H1 2026 priced it as such: the cohort re-rated sharply upward across the board, and Palo Alto Networks — its CyberArk-extended identity franchise sitting squarely on the non-human-identity problem — posted the table's largest capitalization gain, part of it the CyberArk shares themselves. The market's single most consistent H1 statement is that in an economy of acting machines, the scarce products are trust, identity, and observation of the machines.

The audit's caveat is symmetry: the winners are building gates too. Every security platform in the cohort is racing to declare itself *the* perimeter for agent identity and governance — the same self-designation pattern, one layer down the stack. For now the function's demand tailwind is strong enough that the topology contest is a growth story rather than a gridlock story; whether the security layer ultimately becomes the mesh's trust fabric or merely its best-compensated toll collector is a question this report hands to its successor. Verdict: the universe's clearest structural beneficiary — and the strongest evidence that the market's H1 model is revenue denomination, not "AI exposure."

## 6.7 The Cross-Function Scorecard

Assemble the six audits and the scorecard is lopsided in a specific way. On the *defensibility* axes, the functions genuinely differ: write authority is fortress-grade in Back Office ledgers, meaningful in HCM and CRM records, weak in Productivity; task survival ranges from compounding (Infrastructure) to evaporating (service desks, support desks, guided workflows). On the *openness* axes, they barely differ at all: the flagship platforms have converged on read-write-action MCP, external orchestration-as-peer is almost nowhere, metering is attached wherever it can be, semantic layers are held close. Eighteen companies, six functions, one posture — protocol-open, control-closed — and one shared assumption: that agent traffic will pay human-era tolls because the data gravity leaves it no choice. The challengers named in these audits — Sierra, Clay, Attio, Glean, Numeric, Rippling, and the absorbed Sana and Moveworks — matter to this report less for their revenues, which are small, than for what they demonstrate: machine-scale pricing, API-first architecture, and thin applications on open substrates are *shippable today*, at development costs the incumbents' own analysts describe as trivial. They are the existence proof that the traffic has somewhere else to go.

---

# 7. The Verdict: Gridlock, Not Apocalypse

## 7.1 Answering the Question

Return to the hypotheses of §1.6. **Hypothesis A — extinction — is rejected.** Write authority over records of consequence, regulatory embedding of the ledger, and a security function whose task base compounds under agents are real assets, and no evidence in this audit suggests the application layer dissolves. **Hypothesis B — false alarm — is rejected with equal confidence.** The de-rating is not a sentiment accident: it tracks a coherent structural variable (revenue denomination) across thirty names, it has survived beat-and-raise quarters, and the incumbents' own strategic behavior — eighteen months of gate-building around newly opened protocols — is the behavior of managements who believe the threat. **Hypothesis C is confirmed:** the incumbents are surviving the agentic transition by privatizing it — each executing a closed transition behind its own registry, trust layer, and meter — and the cost of that survival strategy is the subject of the rest of this chapter.

## 7.2 The Value Squeeze: Heads, Growth Loses; Tails, Margin Loses

State the incumbent's choice precisely, because the precision is the point. Enterprise value in software is, to first order, a function of two variables: the durability of growth and the terminal margin. The agentic transition forces every seat-era incumbent onto one of two branches, and each branch sacrifices one variable to defend the other.

**The closed branch — hold the toll line.** Price agent access at rates reverse-engineered from seat economics; defend the P&L's margin structure; keep the meter running. The consequence, per Chapter 3, is that machine-scale usage — the only growth there is — is suppressed or routed around: orchestrators extract once and cache, prefer zero-copy paths, favor agent-native alternatives at the greenfield edge. Margin is defended; share, and with it the growth term, decays. The market prices the decay into the multiple today.

**The open branch — price for the machines.** Set agent-tier rates near marginal cost; win the volume; defend share and relevance in the agentic economy. The consequence is that revenue per unit of work collapses toward the challenger's price, while the incumbent's cost structure — enterprise sales, success organizations, decades of accumulated platform surface — cannot compress at the same rate. Share is defended; the margin term deflates. The market prices the deflation into the multiple today.

The squeeze theorem is that **both branches impair enterprise value, and the market does not need to know which branch management will choose in order to de-rate the equity — it needs only to know that these are the branches.** This is the resolution of the puzzle in §1.1: franchises beating and raising while their stocks halve. The quarter measures the seat era's annuity running off; the multiple measures the expectation over the two branches; and H1 2026 marked the moment the market stopped averaging in a third branch — the one where the incumbent defends growth *and* margin simultaneously — because the audit of Chapters 5 and 6 shows why that branch barely exists.

It barely exists because of who is on the other side. The challenger enters with development costs collapsed by coding agents — the fixed-cost barrier of §1.2 is gone — with no installed-base P&L to protect, no seat revenue to cannibalize, no margin structure to defend. Its reservation profit is survival. For such an entrant, the incumbent's price umbrella is not an obstacle; it is the business plan: any toll the incumbent charges above the entrant's near-zero marginal cost of serving is the entrant's addressable margin, and any price war the incumbent starts destroys the incumbent's own P&L first, since the incumbent is the only party in the fight with revenue to lose. Riding the broader agentic-mesh wave — open protocols, open substrates, orchestration layers hungry for cheap tools — the challenger does not need to beat the incumbent's product. It needs the incumbent's *pricing* to remain rational for the incumbent, which it must. Defending growth and margin at once against an adversary with nothing to lose and nearly nothing to spend is not a strategy problem. It is an arithmetic problem, and the arithmetic does not close.

The honest exceptions define the squeeze's boundary rather than refute it. Where task survival compounds (Infrastructure), the growth term is defended by demand itself and the squeeze does not bind — hence the security cohort's sharp aggregate re-rating (§4.3). Where write authority is fortress-grade (core ledgers), the squeeze binds the surrounding workflow revenue but not the record itself — hence Back Office incumbents de-rated severely yet nobody forecasts their churn. Everywhere else in the application layer, the theorem is the base case, and the H1 tape is what the theorem looks like when a market internalizes it.

## 7.3 The Prisoner's Dilemma

Zoom out from any single incumbent and the industry-level structure comes into focus. Each hub strategy documented in Chapter 5 is individually rational: given that rivals are building registries and meters, building one's own is dominant — the vendor that opens unilaterally donates its traffic data and its pricing power to whichever rival's control tower governs the flow. But the collective result of thirty individually rational defenses is N self-declared centers, zero settled topology, and an interoperability that exists at the protocol layer while being taxed and contested at every layer above it. This is a textbook prisoner's dilemma: the cooperative equilibrium — genuine peer interoperability, settlement-grade trust, tolls competed toward cost — would enlarge the agentic market for every participant, and no participant can move toward it unilaterally without being exploited. Enterprise software has solved its coordination problems before, but only when a layer *beneath* the combatants imposed the standard (TCP/IP, HTTP, SQL). No such layer has yet imposed itself on agent topology. Until one does, the gridlock is the equilibrium.

## 7.4 Why the Gridlock Feeds the Insurgents

The gridlock is not stable, however, because it manufactures its own opposition. Every human-era toll is a subsidy to the route around it: each expensive metered call strengthens the case for extracting the data once into an open substrate; each registry that demands the agent enroll on the vendor's terms strengthens the case for orchestration layers that treat every application as a commodity tool; each closed semantic layer strengthens the case for rebuilding the semantics in the open, where every agent can read them. The challengers of Chapter 6 are not succeeding despite the incumbents' defenses; they are arbitraging them. And the deepest irony of the audit is that the incumbents have already built the insurgency's on-ramps — the MCP servers, the A2A endpoints, the zero-copy shares — because protocol openness was the table stakes of appearing modern. The doors are real. The tolls are the only thing holding the traffic back, and Chapter 3 has argued that tolls, uniquely in the agentic era, are the one defense the customer's own software is programmed to defeat.

## 7.5 Falsification Conditions

This report's thesis — dispersion plus defensive closure resolving into value-destroying gridlock — would be materially weakened by any of the following, which we commit to monitoring: **(i)** cross-platform A2A delegation between *rival* incumbents at production volume, evidencing genuine peer topology rather than hub competition; **(ii)** incumbent MCP servers extending to broad, non-privileged write and action scope without meter escalation; **(iii)** published agent-traffic rate cards collapsing toward marginal cost under competitive pressure; **(iv)** a disclosed consumption mix in which machine-denominated revenue grows faster than seat revenue declines *while consolidated margins hold* — the agent tier of §3.7 actually working; **(v)** sustained re-rating of seat-denominated franchises against the pattern of §4.3, which would indicate the market abandoning the revenue-denomination model this report endorses.

## 7.6 Watch Items

For ongoing coverage, the highest-signal indicators are: consumption-revenue disclosures and Flex-Credit/Assist-currency attach rates at Workday and ServiceNow; new-logo cohort data — who is winning the companies founded after 2024; the action-scope of each successive incumbent MCP release; agent-tier pricing announcements, the squeeze's clearest tell; absorption M&A cadence (the Sana/Moveworks route), which converts challenger evidence into incumbent front doors and marks the price incumbents pay to buy time; Intuit's trajectory as the panic's bellwether in both directions; and the security cohort's multiple, which now embeds the assumption that agent governance accrues to the security layer — the one crowded trade this report's own analysis endorses, and therefore the one to watch most skeptically.

## 7.7 Coda: The Question the Gridlock Cannot Answer

End where the audit ends. The protocols exist. The endpoints exist. The challengers exist, and the economics that feed them strengthen with every toll. What does not yet exist is the thing all of them are groping toward: an architecture in which agents, tools, and data substrates transact as *peers* — where discovery does not require enrolling in a rival's registry, where trust does not require a vendor's control tower, where settlement between an agent that needs work done and a service that can do it clears at prices set by competition rather than by the defense of a legacy P&L. Every incumbent audited in this report is betting that no such architecture arrives in time, and every challenger is betting that it does. The gridlock described in this chapter is precisely the vacuum such an architecture would fill — which raises the questions this report has deliberately left open. What would the topology of a genuine agentic software mesh look like? Who provides its trust fabric, its discovery layer, its settlement rails, when no single vendor owns the center — and what happens to the toll plazas when the traffic finds it? That is the subject of the next report in this series: **Report 5 — The Agentic Mesh.**

---

# Methodological Note

Market capitalization data for the thirty-company universe are drawn from the CompaniesMarketCap software ranking [1], recorded at the close of the last trading day of 2025 and at July 1, 2026, and cross-checked by Wisdom Hill Research; §4.1 states the limits of the universe's construction and of capitalization as a performance measure. Aggregate figures in the text are computed from the table in §4.2. Functional classifications follow this report's fixed taxonomy and involve judgment for multi-segment firms; each company carries a single primary classification. Vendor product, protocol, and pricing-structure claims are sourced to the primary announcements and documentation cited. A small number of claims rest on secondary industry accounts rather than vendor documentation — notably the distribution of Agentforce experiences inside third-party assistants — and are attributed as such in the text rather than asserted. Vendor rate cards for machine-scale traffic are not publicly disclosed by any incumbent in the universe; statements about toll levels are therefore structural arguments about pricing logic, not claims about published rates. Challenger references are limited to independently confirmed facts of existence and category; private valuations are omitted. Forward-looking statements are analytical judgments, not predictions, and §7.5 states the evidence that would revise them. This report is not investment advice.

# References

[1] CompaniesMarketCap. "Largest Software Companies by Market Cap." https://companiesmarketcap.com/software/largest-software-companies-by-market-cap/

[2] Salesforce Developers Blog. "Salesforce Hosted MCP Servers Are Now Generally Available." April 2026. https://developer.salesforce.com/blogs/2026/04/salesforce-hosted-mcp-servers-are-now-generally-available

[3] Salesforce Developers Blog. "Salesforce Hosted MCP Servers Are in Beta Today." October 2025. https://developer.salesforce.com/blogs/2025/10/salesforce-hosted-mcp-servers-are-in-beta-today

[4] Salesforce. "Introducing the Data 360 MCP Server — Your Unified Data, Ready for Any Agent." May 2026. https://www.salesforce.com/blog/introducing-the-data-360-mcp-server-your-unified-data-ready-for-any-agent/

[5] ServiceNow Newsroom. "ServiceNow Opens Its Full System of Action to Every AI Agent in the Enterprise." May 2026. https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-opens-its-full-system-of-action-to-every-AI-Agent-in-the-enterprise/default.aspx

[6] diginomica. "ServiceNow Knowledge 2026 — AI Control Tower Expands, Autonomous Workforce Reaches Every Function." May 2026. https://diginomica.com/servicenow-knowledge-2026-ai-control-tower-expands-autonomous-workforce-reaches-every-function-and

[7] Reworked. "ServiceNow Wants to Be the Control Layer for Every AI Agent in the Enterprise." May 2026. https://www.reworked.co/digital-workplace/servicenow-launches-action-fabric-major-overhaul-of-ai-control-tower/

[8] ERP Today. "ServiceNow Repositions Around AI Security and Governance at Knowledge 2026." May 2026. https://erp.today/servicenow-ai-security-governance-knowledge-2026/

[9] Bersin, Josh. "The Reinvention of Workday: From System of Record to Platform of Agents." April 2026. https://joshbersin.com/2026/04/the-reinvention-of-workday-from-system-of-record-to-platform-of-agents/

[10] Workday Newsroom. "Workday Announces New AI Agent Partner Network and Agent Gateway." June 3, 2025. https://newsroom.workday.com/2025-06-03-Workday-Announces-New-AI-Agent-Partner-Network-and-Agent-Gateway-to-Power-the-Next-Generation-of-Human-and-Digital-Workforces

[11] Workday Blog. "The Workday Agent System of Record Is Now Generally Available." February 2026. https://blog.workday.com/en-us/managing-ai-powered-future-of-work.html

[12] Roush, Tyler. "Intuit Becomes S&P 500's Worst Performer This Year — Here's Why." Forbes, June 2, 2026. https://www.forbes.com/sites/tylerroush/2026/06/02/intuit-becomes-sp-500s-worst-performer-this-year-heres-why/

[13] Great Speculations. "What's Behind Intuit's 30% Correction." Forbes, February 4, 2026. https://www.forbes.com/sites/greatspeculations/2026/02/04/whats-behind-intuits-30-correction/

[14] IndexBox. "Early AI Adoption Fails to Shield Intuit in 'SaaSpocalypse' Market Panic." 2026. https://www.indexbox.io/blog/early-ai-adoption-fails-to-shield-intuit-in-saaspocalypse-market-panic/

[15] International Business Times (AU). "Intuit Stock Turbulence: AI Disruption." 2026. https://www.ibtimes.com.au/intuit-stock-turbulence-ai-disruption-1871597

[16] The Motley Fool. "Intuit Stock Was Absolutely Hammered After a Beat." May 21, 2026. https://www.fool.com/investing/2026/05/21/intuit-stock-was-absolutely-hammered-after-a-beat/

[17] Sherwood News. "Intuit Plummets After Reporting Slowing Revenue Growth." 2026. https://sherwood.news/markets/intuit-plummets-after-reporting-slowing-revenue-growth/

[18] Anthropic. "Introducing the Model Context Protocol." November 2024. https://www.anthropic.com/news/model-context-protocol

[19] Google Developers Blog. "Announcing the Agent2Agent Protocol (A2A): A New Era of Agent Interoperability." April 2025. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

[20] Digital Today. "ServiceNow Launches Action Fabric, Opens Platform to External AI Agents." May 2026. https://www.digitaltoday.co.kr/en/view/55228/servicenow-launches-action-fabric-opens-platform-to-external-ai-agents

[21] NowBen. "ServiceNow Launches Action Fabric to Open 'Full System of Action' to Any AI Agent." May 2026. https://nowben.com/servicenow-launches-action-fabric-to-open-full-system-of-action-to-any-ai-agent/

[22] Efficiently Connected. "ServiceNow Knowledge 2026: AI Governance Takes Center Stage." May 2026. https://www.efficientlyconnected.com/servicenow-knowledge-2026-ai-governance-control-tower/

[23] Muir, Don. "$300 Billion Evaporated. The SaaS-Pocalypse Has Begun." Forbes, February 4, 2026. https://www.forbes.com/sites/donmuir/2026/02/04/300-billion-evaporated-the-saaspocalypse-has-begun/

---
