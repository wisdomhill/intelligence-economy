---
title: "9. Who Owns the Consumer Agent?"
subtitle: "Funnel collapse, the OS duopoly, and the five-way battle for personalized commerce"
series: "The Intelligence Economy"
number: 9
manuscript-revision: 1
date: 2026-08-24
date-modified: 2026-08-24
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  Discovery, comparison and checkout are collapsing into one conversation.
  Why the consumer control plane is the operating system's action registry
  rather than the model, and which of five players can reach it.

keywords:
  - consumer agent
  - action registry
  - funnel collapse
  - agentic commerce
  - OS duopoly
  - take rate

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
#
# Like Reports 7 and 8, this manuscript numbers its Executive Summary as
# section 1 and its cross-references depend on that, so the numbering is kept
# and the summary stays on the cover and in the PDF rather than becoming a
# chapter page.
published:
  dir: reports/r09/
  pdf: r09-who-owns-the-consumer-agent.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r09/

chapters:
  - manuscript: "2. Framework: Extending the Control Plane Thesis from Enterprise to Consumer"
    published:  "2. Framework"
    fragment:   _01-framework.qmd
    page:       01-framework.qmd
  - manuscript: "3. The OS Layer: A Structural Duopoly Forms First"
    published:  "3. The OS Layer"
    fragment:   _02-os-layer.qmd
    page:       02-os-layer.qmd
  - manuscript: "4. The Demand Side: Five Players, Three Distinct Competitions"
    published:  "4. The Demand Side"
    fragment:   _03-demand-side.qmd
    page:       03-demand-side.qmd
  - manuscript: "5. The Protocol War: Consumer Equivalent of the Enterprise Interoperability Battle"
    published:  "5. The Protocol War"
    fragment:   _04-protocol-war.qmd
    page:       04-protocol-war.qmd
  - manuscript: "6. Comparative Assessment: The Five-Player Scoring Matrix"
    published:  "6. The Scoring Matrix"
    fragment:   _05-scoring-matrix.qmd
    page:       05-scoring-matrix.qmd
  - manuscript: "7. Scenarios and Equilibria (2026–2030)"
    published:  "7. Scenarios and Equilibria"
    fragment:   _06-scenarios.qmd
    page:       06-scenarios.qmd
  - manuscript: "8. Monetization Models of the Agentic Funnel"
    published:  "8. Monetization Models"
    fragment:   _07-monetization.qmd
    page:       07-monetization.qmd
  - manuscript: "9. Investment Implications"
    published:  "9. Investment Implications"
    fragment:   _08-investment.qmd
    page:       08-investment.qmd
  - manuscript: "10. Watch List and Excluded Candidates"
    published:  "10. Watch List"
    fragment:   _09-watch-list.qmd
    page:       09-watch-list.qmd
  - manuscript:
      - "A. Event Timeline (January–June 2026)"
      - "B. Glossary"
      - "C. Methodology Notes"
    published:  "Appendices"
    fragment:   _10-appendices.qmd
    page:       10-appendices.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _11-references.qmd
    page:       11-references.qmd
---
# Who Owns the Consumer Agent?

### Funnel Collapse, the OS Duopoly, and the Five-Way Battle for Personalized Commerce

*The Intelligence Economy — Report 9 of 14*

*Wisdom Hill Research | Thematic Research | July 2026*

---

# 1. Executive Summary

## 1.1. Key Findings and Investment Theses

Over the first half of 2026 the two mobile operating system owners converged on the same architecture for consumer agentic AI: an OS-governed, declarative action layer through which AI agents invoke application functionality. At I/O (May 19), Google expanded and repositioned AppFunctions as a central component of Android's agentic architecture: a permissioned, declarative API through which agents call app capabilities, intended to replace screen-scraping automation. The underlying Jetpack library had been available in alpha since 2025 and remained a pre-stable (alpha) API as of this writing. Apple's counterpart is App Intents, the primary channel through which a rebuilt Siri is designed to reach third-party apps — but Apple's timeline runs materially behind Google's: the Apple–Gemini deal was announced January 12, 2026; a first tranche of context- and screen-aware Siri features is targeted for the iOS 26.4 cycle in spring; and the fully conversational, cross-app-action Siri is not expected until iOS 27 ships alongside the iPhone 18 around September 2026. Apple has committed to delivering the new Siri before year-end 2026, but as of publication it is not yet in users' hands, and the positioning of App Intents as the OS action registry is an announced direction rather than a shipped, enforced reality. The convergence of architecture is nonetheless the single most important structural fact of the period: it tells us the consumer control plane — the layer that mediates between user intent and software action — is forming not at the model layer but at the operating system's action-brokerage layer, exactly as the enterprise control plane formed at the tool/data gateway layer rather than at the model layer (see Part I). Apple's execution risk on this front is treated explicitly in Section 3.1 and 4.6.

Against this backdrop, five companies are contesting the demand side of consumer agentic AI: Google, Apple, Amazon, Meta, and OpenAI. Our central findings are as follows.

First, this is not one competition but three. Intent capture (who receives the user's expressed need), action execution (who completes the transaction, including payment and fulfillment), and context ownership (who holds the personal data that makes an agent's recommendation trustworthy and personalized) are distinct contests with different competitive logics. Google is the only player with material assets in all three, which makes it the structural favorite — but also the player whose victory scenario requires the most aggressive cannibalization of its own advertising economics.

Second, the incumbent consumer triumvirate — Google in search, Meta in social, Amazon in shopping — has historically coexisted because each owned a different stage of the commerce funnel: Meta created demand at the top, Google captured intent in the middle, and Amazon executed transactions at the bottom. Agentic AI collapses that funnel into a single conversation. The competition is therefore best understood as a race by each player to internalize the funnel stages it does not own, while defending the stage it does.

Third, execution has proven far harder than intent capture. OpenAI's Instant Checkout — launched to all U.S. users in February 2026 and effectively retired by late March after fewer than thirty of Shopify's millions of merchants went live — is the clearest evidence that owning the conversation does not automatically confer the ability to close the transaction. Conversely, Amazon's Alexa for Shopping (launched May 2026, merging Rufus and Alexa+) demonstrates that the player with catalog ground truth, payment rails, and fulfillment can move up the funnel more credibly than intent-layer players can move down it.

Fourth, the monetization chokepoint is shifting from the advertising auction to the commerce protocol. OpenAI's Agentic Commerce Protocol (ACP, with Stripe), Google's Universal Commerce Protocol (UCP, announced January 2026), and Amazon's closed stack are competing to become the standard through which agents transact with merchants. The March 2026 federal district-court injunction blocking Perplexity's Comet browser from Amazon's logged-in pages initially looked like a precedent favoring opt-in, protocol-led agentic commerce — but that reading is now premature. The Ninth Circuit stayed the injunction within roughly a week (appellate stays of preliminary injunctions are uncommon; we read the stay as a procedural signal — an inference rather than a merits ruling — that the CFAA theory may not survive), heard oral argument in Seattle on June 11, 2026 with Mozilla and the EFF filing amicus briefs for Perplexity, and has not yet ruled. The legal foundation for platform-level agent exclusion is therefore contested, not settled, and the procedural signals to date tilt modestly toward permissionless agents rather than away from them.

## 1.2. The Central Claim: The Consumer Control Plane Is the Action Registry, Not the Model

Part I of this series argued that in enterprise software, durable value accrues to the control plane — the layer governing how agents access tools, data, and permissions — rather than to the models themselves, which trend toward commoditization. The consumer market is now validating the same thesis in compressed time. Apple's decision to procure Google's frontier model technology — reportedly on the order of $1 billion per year, though the final terms remain unconfirmed — while retaining context, orchestration, and the action registry is the purest expression of this logic: the model is treated as a component, like a display panel or a modem, while the control plane is treated as the franchise. Whether Apple's bet succeeds depends on execution capabilities Apple has not yet demonstrated — but the bet itself reveals where sophisticated capital believes the value sits.

## 1.3. Base-Case Scenario: A Layered Equilibrium, Not a Single Winner

Our base case through 2030 is not a single dominant consumer agent but a layered partition: intent capture distributed across Google, OpenAI, and Meta; transaction execution concentrated in Amazon's fortress plus protocol-mediated coalitions of merchants; and toll collection at the OS layer by the Google–Apple duopoly. Google is the only player that could plausibly consolidate all layers, but its path is constrained by the innovator's dilemma in search advertising and by acute antitrust exposure. The asymmetric upside belongs to OpenAI — the only player with nothing to cannibalize — and the asymmetric downside to advertising-funded intermediaries whose economics depend on the comparison-shopping journey that agents compress away.

---

# 2. Framework: Extending the Control Plane Thesis from Enterprise to Consumer

## 2.1. Recap: The Four-Layer Value Chain from Part I

Part I ("The Control Plane Decade") proposed a four-layer value chain for agentic AI in the enterprise: foundation models at the base; the agent harness and orchestration layer above it; the control plane governing tool, data, and permission access; and the application/workflow surface at the top. The report's core claim was that the control plane is the layer where switching costs, data gravity, and governance requirements compound — and therefore where durable economics concentrate — while the model layer faces commoditization pressure from open weights, distillation, and multi-vendor procurement.

## 2.2. What Changes in B2C: Intent Capture, Context Ownership, and Trust as the Scarce Assets

The consumer market preserves the layer logic but changes which resources are scarce. Enterprises buy agents to reduce labor cost; consumers adopt agents to reduce decision cost. This makes three assets decisive in B2C that have no direct enterprise equivalent. The first is intent capture: the privileged position of being the surface where a consumer first expresses a need ("I need running shoes," "book me a table"). In the search era this was the query box; in the agent era it is whichever conversational surface the consumer habitually addresses. The second is context ownership: the longitudinal personal data — purchase history, location patterns, communications, calendar, health signals — that converts a generic recommendation into a trusted, personalized one. The third is transactional trust: the payment credentials, dispute-resolution track record, and fulfillment reliability that let a consumer comfortably delegate spending authority to software.

The enterprise control plane was a governance artifact; the consumer control plane is a habit-and-trust artifact. This distinction explains why distribution incumbents (Apple, Google, Amazon, Meta) hold stronger defensive positions in B2C than enterprise incumbents did against agentic disruption: habits and stored credentials are stickier than procurement contracts.

## 2.3. The Funnel Collapse Hypothesis: Discovery → Comparison → Checkout in a Single Conversation

The organizing hypothesis of this report is that agentic AI collapses the consumer commerce funnel. In the pre-agent economy, a purchase journey traversed separately owned stages: inspiration and demand creation (social feeds, video, display advertising), active intent and comparison (search, marketplaces, review sites), and transaction and fulfillment (retailer checkout, payment networks, logistics). Each stage supported its own monetization model — brand advertising at the top, auction-based performance advertising in the middle, take rates and sponsored placement at the bottom — and each stage had a dominant owner.

An agent that receives a need, researches options, compares them against the user's stored preferences, and completes checkout performs the entire journey inside a single conversational session. Every handoff that disappears is a monetization event that disappears with it: the impression, the click, the search ad, the affiliate link, the marketplace search ranking. Funnel collapse does not destroy the value of the journey; it relocates that value to whoever operates the agent and whoever owns the protocol through which the agent transacts.

## 2.4. Mapping the Incumbent Triumvirate to Funnel Stages

The three strongest consumer applications of the last two decades map cleanly onto the funnel: Meta owns demand creation (roughly 3.4–3.5 billion daily active people across Facebook, Instagram, WhatsApp, and Messenger, monetized through the most sophisticated demand-generation advertising machine ever built); Google owns intent capture (the search query as the canonical expression of commercial intent, monetized through the keyword auction); and Amazon owns transaction and fulfillment (the default purchase endpoint in most Western markets, monetized through marketplace take rates and a sponsored-products advertising business that has grown into one of the largest ad platforms in the world). Advertising and commerce were already converging before agents arrived — retail media networks, social commerce, and shoppable video all blurred the stage boundaries. Agentic AI accelerates this convergence to its logical endpoint: a single mediated decision.

The strategic question for each incumbent is identical in form: can it extend its franchise into the funnel stages it does not own faster than agents erode the stage it does?

## 2.5. The Harness Thesis Revisited: Why Orchestration Beats Raw Model Capability in Consumer

Our prior comparative work on Claude, ChatGPT, and Gemini concluded that harness engineering — the scaffolding of tools, memory, context management, and reliability engineering around a model — has become the primary competitive differentiator in the agentic era, ahead of raw model capability. The consumer market is the strongest confirmation of this thesis to date. Apple is explicitly betting that frontier intelligence can be procured while the harness (Siri orchestration, App Intents, on-device context) is owned. Amazon's Alexa for Shopping competes not on model quality but on grounding: real inventory, real delivery estimates, real purchase history. Google's Gemini Spark is described by Google itself as a Gemini base model wrapped in an agentic harness derived from its Antigravity platform. In consumer agentic AI, the model answers; the harness acts. Consumers pay for action.

It must be said, however, that the harness thesis cuts both ways for Apple specifically: if orchestration is the differentiator, then Apple's 2024–2025 Siri failures were harness failures, and Apple's harness engineering capability remains the least proven among the five players analyzed here.

---
# 3. The OS Layer: A Structural Duopoly Forms First

## 3.1. WWDC 2026 — Apple's Asymmetric Bet: Procured Intelligence, Owned Context

### 3.1.1. The Gemini Arrangement: Reported Terms, Shipped Architecture, and the Limits of the Price Comparison

Bloomberg reported in November 2025 that Apple was finalizing an arrangement of roughly $1 billion per year under which a custom Gemini model of approximately 1.2 trillion parameters would power the new Siri. By WWDC 2026 (June 8, Tim Cook's final keynote before handing the CEO role to John Ternus in September), however, Apple described the deployed foundation models as Apple-owned models developed with the aid of Gemini technology, and post-keynote reporting stated that the final models contain no Google code. The reported economic terms — and the extent to which the originally reported supply arrangement survived unchanged into the shipped architecture — remain unconfirmed.

With that caveat stated, the reported figure invites comparison with the estimated ~$20 billion Google pays Apple annually for search default placement. The asymmetry is directionally consistent with a market in which frontier intelligence has become abundant enough to be procured at component prices while default access to two billion devices remains scarce. It should not, however, be read as a like-for-like market valuation of models versus distribution: the two figures reflect negotiations of different vintages and structures, and the search payment bundles considerations — regulatory exposure, search distribution, cloud support — that have no counterpart in a model-supply arrangement.

### 3.1.2. App Intents as Emerging Action Registry; SiriKit Deprecation

The structural core of Apple's strategy is not the model deal but the action layer. In Apple's design, App Intents becomes the principal channel through which Siri invokes third-party app functionality, with several SiriKit intent domains on a deprecation path — meaning an app that does not expose its core actions as intents risks being, in developer-community shorthand, invisible to the new Siri. Developer commentary has compared the direction to App Tracking Transparency: a unilateral platform rule that re-architects the ecosystem's economics. The rebuilt Siri is described as both a standalone app (with conversation history synced via iCloud) and a system-wide presence with on-screen awareness, able to chain multi-step actions across applications. Two caveats matter for analysis, both a function of timing. First, the cross-app-action capability is the part of Siri that has slipped repeatedly since its 2024 preview and is now tied to the iOS 27 wave (roughly September 2026), so the registry's centrality is a stated destination whose enforcement has not yet been observed in the wild. Second, the early-partner list frequently cited (Uber, Amazon, Temu, YouTube, WhatsApp, Facebook, Threads, AllTrails) reflects reported onboarding rather than a shipped, GA integration set. The analytical point stands — Apple is building an OS-level action registry — but it is a stated destination, not yet a locked-in reality.

Two observations on this partner list. First, its breadth across categories (mobility, marketplace, social, content) signals that Apple is seeding the registry horizontally rather than focusing on a single high-value vertical. Second, and more telling, the list is light on high-value transactional categories — airlines, hotels, financial services — where the economics of becoming a "callable endpoint" inside someone else's agent remain unresolved. Aggregators have weak incentives to volunteer for disintermediation before transaction-fee structures are settled. This is the largest near-term bottleneck for the monetization of any OS-level action registry.

### 3.1.3. Private Cloud Compute and the Data Firewall Against Google

Apple's privacy architecture is competitively load-bearing. On-device execution for the most common tasks, with Private Cloud Compute handling overflow, means that — by design — the model supplier does not accumulate user context from iOS interactions. Google supplies intelligence to Apple's agent but is structurally prevented from harvesting the interaction data that would normally be the strategic compensation for supplying intelligence below cost. Apple keeps the customer relationship, the context graph, and the trust positioning (user data is processed on-device or, when necessary, within Apple's attested Private Cloud Compute environment), which is precisely the asset bundle this report identifies as the consumer control plane.

### 3.1.4. Open Question: Apple Foundation Models — Licensed Gemini or Co-Developed Apple IP?

Reporting on the architecture is genuinely contradictory and the distinction matters. Bloomberg-lineage reporting frames the arrangement as Apple licensing a custom Gemini model. AppleInsider, by contrast, reports that the shipped Apple Foundation Models "don't contain a drop of Gemini" — that Google provided technology and assistance in developing models that are Apple's own, running on-device and in Private Cloud Compute. If the latter framing is closer to the truth, Apple's model dependency is substantially weaker than the headline suggests: a co-development/distillation arrangement with exit optionality rather than a perpetual supply relationship. We flag this as an unresolved factual question with direct implications for how durable Google's iOS beachhead is, and recommend monitoring developer-facing documentation (the Foundation Models framework now exposes a model abstraction layer that can reportedly swap Apple's on-device model, Gemini, or Claude with minimal code changes — itself evidence that Apple is engineering for supplier interchangeability).

## 3.2. Google I/O 2026 — Android as a Full-Stack Agentic Platform

### 3.2.1. Gemini Intelligence, Android Halo, and Gemini Spark

Three weeks earlier (I/O, May 19, 2026), Google announced Gemini Intelligence for Android 17: system-level agentic capability that can navigate apps, execute multi-step tasks in the background, and act on on-screen context, debuting on Samsung Galaxy S26 and Pixel 10 devices. Agentic task execution had already been previewed earlier in the year — Gemini booking rides and ordering food by operating apps in a virtualized window with user oversight and final-confirmation gates on checkout. Alongside the OS work, Google introduced Gemini Spark, a 24/7 agentic personal assistant built from Gemini base models and an agentic harness derived from Google Antigravity, reachable by email through a dedicated Gmail address, able to act on the web through Chrome, integrated with external services over MCP, with progress on mobile surfaced through the new Android Halo system.

### 3.2.2. AppFunctions: From Screen-Scraping to Declarative Action APIs

The Android equivalent of App Intents is AppFunctions: a platform API (with Jetpack libraries) through which apps expose capabilities to agents, assistants, and other authorized callers, with the system managing permissions, call boundaries, and security constraints, and simplifying MCP integration. Maturity matters here: the Jetpack library entered alpha in May 2025 and, as of July 2026, its latest release remained an alpha version rather than a stable API — I/O 2026 repositioned and expanded the framework rather than shipping it as a finished platform surface. The significance is architectural: the design is intended to reduce mobile automation's reliance on recognizing screens, simulating taps, and retrying after UI changes. Apps declare what they can do; agents call those capabilities with authorization. Future Android apps will need not only human-facing UIs but agent-callable capability surfaces — the same redefinition of "what an app is" that App Intents imposes on iOS.

## 3.3. Convergent Architecture: Why Both OS Owners Are Building the Same Declarative Action Layer

That Apple and Google publicly converged on similar declarative action architectures within weeks of each other — albeit at different stages of maturity and deployment — is not coincidence; it is convergent strategy under identical incentives. A declarative action registry solves three problems simultaneously for an OS owner. It makes agent actions reliable (screen-scraping is brittle; declared APIs are not). It makes them governable (the OS mediates permissions and can gate which agents may call which intents). And — potentially decisively — it makes them governable at the point of access: the OS owner mediates which agents may call the registry. As of mid-2026, first-party agents (Siri, Gemini) are best positioned to exploit these registries. Android's published AppFunctions design, however, explicitly contemplates access by AI assistants more broadly, and the degree of functional parity or OS-level privilege ultimately extended to third-party agents remains to be observed. Excludability, in other words, is a capability the OS owners are building rather than an outcome already locked in — but it is the mechanism by which the duopoly could convert its distribution incumbency into agentic-era incumbency.

## 3.4. The 2008 App Store Analogy: Distribution Gatekeeping → Execution-Surface Gatekeeping

In 2008, the App Store inserted the OS owner between developers and users at the point of distribution, and the resulting toll (30%, later tiered) financed a decade of platform economics. In 2026, the action registry inserts the OS owner between agents and apps at the point of execution. Developer-facing analysis has already framed it in exactly these terms: developers build App Intents, and the platform owns the AI execution surface — same pattern, same harness, different era. The open question is what the toll will be — and here one asymmetry with 2008 must be stated plainly. The App Store's 15–30% commissions apply to digital goods and services; under current rules, both Apple and Google explicitly exempt ordinary physical-goods and physical-services transactions from those commissions, and neither company has announced any agentic transaction toll. What both have built is infrastructure that would make future monetization possible — Apple through Apple Pay plus the App Intents registry, Google through UCP, payments, and the ad system — most plausibly via payment facilitation, discovery services, or sponsored placement rather than a direct extension of app-store commissions to physical commerce.

## 3.5. Structural Consequences: Third-Party Assistants Demoted to "Apps Within the OS Agent"

For Meta, Amazon, and OpenAI, the duopoly's action-layer enclosure has a common consequence: on mobile, their agents are apps inside someone else's agent-capable OS. They can be reached by user habit (opening the ChatGPT or Amazon app) but currently lack comparable OS-level orchestration reach. This single constraint explains an otherwise heterogeneous set of strategic behaviors: Meta's smart-glasses program, OpenAI's hardware ambitions, and Amazon's continued investment in Echo devices are all, at root, OS-bypass strategies — attempts to own a hardware surface where their agent is the system agent. It also explains why all three are simultaneously protocol entrepreneurs (ACP, Amazon's merchant-facing stack): if you cannot own the device action layer, you try to own the commerce action layer.

## 3.6. Constraints on the Duopoly: Cold Start, Regulatory Exposure, and Launch Gaps

Three forces limit how completely the OS owners can enclose the consumer control plane. First, the cold-start problem: as sell-side commentary (MoffettNathanson) framed it ahead of WWDC, Siri only becomes credibly agentic if developers adopt App Intents at scale, but developers rationally wait for evidence of consumer usage before investing — a chicken-and-egg dynamic that early partner programs are designed to break but have not yet broken, particularly in high-value transactional verticals. Second, regulation: the consumer Siri AI features are not launching in the EU or China at launch (developer APIs ship; consumer features do not). Under the DMA, an architecture in which only the gatekeeper's own agent enjoys system-level action access is an obvious enforcement target; a plausible medium-term scenario is mandated third-party agent access to App Intents/AppFunctions on equal terms, which would convert the registries from proprietary moats into common carriage — radically improving the position of OpenAI and Meta in Europe first. Third, the trust burden runs both ways: an OS agent with reach into every app and payment credential is also the maximal privacy and security attack surface, and consumer-sentiment data on agentic features consistently shows enthusiasm lagging executive enthusiasm by wide margins.

---
# 4. The Demand Side: Five Players, Three Distinct Competitions

## 4.1. Competition Map: Intent Capture vs. Action Execution vs. Context Ownership

Treating "consumer agentic AI" as a single race obscures more than it reveals. We decompose it into three competitions with distinct winning conditions. Intent capture is won by habit and surface placement: being the default place a need is expressed. Action execution is won by infrastructure: catalog ground truth, payment rails, fulfillment, fraud and dispute handling — the infrastructure counterpart of the transactional trust that Section 2.2 identified as the third scarce consumer asset. Context ownership is won by data position and trust: holding the longitudinal personal graph and the consumer's permission to use it. The consumer control plane, properly defined, is the bridge across all three — the system that takes a captured intent, enriches it with owned context, and executes it through trusted rails. No player currently operates the full bridge. The remainder of this section assesses each player against that standard.

## 4.2. Google — The Full-Stack Favorite with the Largest Self-Cannibalization Problem

### 4.2.1. Assets Across All Three Competitions

Google is the only company with material positions in all three contests. In intent capture it holds both the legacy surface (Search, now agent-augmented through AI Mode) and the emerging one (the Gemini app and Gemini Spark). In context it holds Gmail, Calendar, Maps, Photos, YouTube history, and Android-level signals — arguably the only personal context graph comparable to Apple's device graph, and one that is cloud-native and therefore agent-accessible by default. In execution it holds Google Pay, the merchant relationships of Google Shopping, and now UCP, its coalition-backed commerce protocol announced in January 2026 and being wired into Search AI Mode and Gemini. Layer on top the Android action registry (AppFunctions), the iOS model-supply beachhead (whose durability Section 3.1.4 flags as contested), and a frontier model family (Gemini 3.5 generation as of I/O 2026) and the conclusion is unavoidable: on assets alone, Google is the most complete candidate to dominate B2C agentic AI. The questions are all about constraints.

### 4.2.2. The Innovator's Dilemma Quantified

Google's search advertising business — on the order of $200 billion annually — monetizes precisely the funnel stage that agents compress: the comparison journey between intent expression and decision. Every query that an agent resolves conversationally, with a small number of grounded recommendations and no auction page, removes inventory from the keyword auction. Google's countermeasures (ads within AI Overviews and AI Mode, sponsored placements in agent recommendations, UCP take rates) are real but unproven at substitution scale: agent-mediated monetization must replace auction yield roughly one-for-one for the P&L to hold, and no disclosed data yet demonstrates that it can. The strategic consequence is pacing: Google must move fast enough to deny OpenAI the intent-capture franchise, but every increment of agent adoption it drives is an increment of auction erosion it absorbs. Google's dominance scenario is therefore gated less by capability than by how hard it is willing to press the accelerator on its own disruption. Amazon faces the same dilemma in sponsored products; Google's version is simply an order of magnitude larger.

### 4.2.3. Antitrust as a Binding Constraint

Google approaches this competition immediately after search-monopoly remedies litigation in the U.S. and under active DMA supervision in Europe. A vertically integrated structure combining the OS action registry, the default agent, the model layer, the commerce protocol, and the ad system is close to a textbook description of what gatekeeper regulation exists to prevent. We treat regulatory drag not as a tail risk but as a standing tax on the speed and exclusivity of Google's integration — and as the principal mechanism by which the "Google consolidates everything" scenario fails even if Google executes flawlessly.

## 4.3. Amazon — Fortress at the Bottom of the Funnel

### 4.3.1. Alexa for Shopping: Merging Rufus and Alexa+

On May 13, 2026, Amazon launched Alexa for Shopping, retiring the Rufus brand and combining Rufus's product expertise and shopping-history grounding with the personalized context of Alexa+, deployed across the Amazon app, website, and Echo devices, and embedded directly in the main search bar rather than confined to a chatbot widget. Rufus had assisted over 300 million customers during 2025; Alexa+ rides on hundreds of millions of devices. The product can compare items, track prices, automate routine purchases, and answer with grounded inventory and delivery information. Amazon's leadership has been explicit about the competitive logic: its agent is superior where it matters because it has the data — reviews, catalog, stock status, delivery estimates — that general-purpose assistants lack.

### 4.3.2. Walled-Garden Defense: Amazon v. Perplexity

Amazon paired the product offensive with a legal one. In March 2026 a federal district judge granted Amazon a preliminary injunction barring Perplexity's Comet browser from accessing the logged-in portions of Amazon on users' behalf, on a Computer Fraud and Abuse Act theory that user permission does not equal platform authorization. The strategic *intent* is clear — force external agents (ChatGPT, Gemini, Perplexity) to negotiate for catalog access or route around it — and Amazon separately enforces exclusion at the technical layer, blocking roughly 100 agents via robots.txt and bot-detection. But the legal durability of the exclusion is now genuinely uncertain. The Ninth Circuit stayed the injunction roughly a week after it issued, let Comet keep operating on Amazon's logged-in pages during appeal, and heard oral argument in Seattle on June 11, 2026; digital-rights groups (Mozilla, EFF) filed for Perplexity, and appellate stays of preliminary injunctions are uncommon — a procedural signal, though an inference rather than a merits ruling, that the panel sees a real chance the CFAA theory fails. We therefore treat Amazon's walled garden as *defensible in practice today* (technical blocking works regardless of the ruling) but *legally unsettled*, with a Ninth Circuit reversal representing the single largest risk to the opt-in-only model of agentic commerce.

### 4.3.3. Outbound Expansion: Shop Direct, Buy for Me, and ASA on AWS

Amazon's posture is not purely defensive. Shop Direct surfaces products from external stores across the web; Buy for Me executes parts of external purchase flows on the user's behalf, positioning Amazon's agent as an intermediary between consumers and independent merchants — an inversion in which Amazon's agent shops *outside* Amazon while outside agents are barred from shopping *inside* it. In parallel, Amazon has productized its agentic shopping architecture as the Agentic Shopping Assistant (ASA) on AWS, selling the stack to rival retailers — the classic Amazon pattern of commercializing internal infrastructure, extending its AI layer into storefronts that compete with its own marketplace.

### 4.3.4. Ground Truth as Moat

The durable asset is epistemic. An agent recommending a product must know, with transactional confidence, that the item exists, is in stock, is authentic, will arrive Tuesday, and can be returned. That knowledge lives in Amazon's catalog, review corpus, logistics network (over one billion items delivered same-day or overnight in early 2026, per the company), and three decades of transaction data. Frontier models are abundant; ground truth at this fidelity exists in one place. This is why we judge Amazon's bottom-of-funnel fortress more defensible against intent-layer attackers than the intent layer is against Amazon's upward expansion.

### 4.3.5. The Sponsored-Products Dilemma

Amazon's version of the innovator's dilemma is concentrated in sponsored products — the listings-promotion business that constitutes the bulk of its advertising revenue (roughly $56–69 billion in 2025 depending on source and scope, and by J.P. Morgan's estimate about one-third of Amazon's operating income in 2026). An agent that recommends two well-grounded options destroys the economics of paying for placement in a results page no one scrolls. Amazon's advertising organization is already repositioning for conversational discovery, introducing Sponsored Products and "Brand Prompts" formats inside its own agentic experience, but the transition risk to third-party seller economics — and therefore to Amazon's highest-margin revenue line — is the central bear case on the company's agentic strategy.

Prime Day 2026 (June 23–26) supplied the first large-scale empirical read on this dilemma, and it cuts in a direction that should worry Amazon. Per Adobe Analytics, U.S. shoppers spent a record ~$26.4 billion across all retail during the four-day event, and for the first time in Prime Day history the highest-converting cohort was shoppers arriving from AI chatbots — 40% more likely to complete a purchase than visitors from search, email, or social. The reversal is the analytically important part: in prior years AI-referred shoppers were the *least* likely to convert, reflecting the friction of early agentic workflows; the flip to highest-converting suggests assistants have crossed a reliability threshold at which users arrive pre-decided. Two structural cautions keep this from being a rout. First, scale: agentic AI still drives under 1% of traffic across major online stores, and Amazon's own share is the lowest of the group at ~0.4% — by design, since Amazon keeps external agents out. Second, and revealingly, Amazon itself bought sponsored placements *inside* ChatGPT to promote Prime Day (directing clicks back to Amazon.com rather than enabling in-chat purchase), while continuing to deny ChatGPT organic access to its catalog. Analysts read the ad buy as an experiment in broad awareness rather than a performance commitment; the tell to watch is whether Amazon begins bidding on individual product listings inside ChatGPT, which would signal it has validated the channel as a genuine acquisition surface. The larger point for the report's thesis: the funnel-collapse hypothesis (Section 2.3) now has its first hard data point, and it favors whoever operates the high-converting agent — a position Amazon is structurally conflicted about occupying on anyone's platform but its own.

## 4.4. Meta — The Advertiser Agent, Not the Shopper Agent

### 4.4.1. Supply-Side Agentification: Advantage+ and the URL-plus-Budget Endgame

Meta's agentic investments concentrate not on a consumer shopping agent but on automating the advertiser. The Advantage+ suite progressively removes manual decisions from campaign management — Meta reports roughly 22% higher ROAS for Advantage+ campaigns versus manually managed ones, with generative-AI tool adoption among advertisers growing from one million to over four million in six months — and the publicly stated end-state is a system in which an advertiser supplies a product URL and a budget, and AI generates creative, targeting, placement, and budget allocation across Facebook, Instagram, Messenger, and WhatsApp. This is rational specialization: Meta is agentifying the side of the market where it has overwhelming data advantage (auction and creative-performance data) rather than the side where it has none.

### 4.4.2. Muse Spark and Meta AI Monetization

Meta's consumer AI posture changed materially in spring 2026. Following the standalone Meta AI app (April 2025), Meta introduced a new flagship model, Muse Spark (development codename "Avocado"), and in late May began testing a paid subscription tier for Meta AI offering greater task capacity and complex-request handling — its first direct AI monetization and an explicit entry into paid-assistant competition with OpenAI, Google, and Anthropic. Strategically, this completes Meta's transition from "AI as a feed feature" to "AI as a standalone business," and gives Meta the same structural archetype as xAI: a proprietary social-data corpus fused with a frontier-model ambition and an assistant embedded in the feed (see Section 10.1 for why we nonetheless exclude xAI from the core framework).

### 4.4.3. The Missing Stack

What Meta lacks is everything below the inspiration layer: no checkout infrastructure at scale (the Shops initiative underperformed), no transaction data corpus, no product-catalog ground truth, no logistics, and no payment habit among Western consumers. A Meta shopping agent would have to recommend without inventory truth and transact without rails. Meta's realistic role in the agentic funnel is therefore not to operate the agent that buys, but to remain the place where wants are *formed* — and to sell that demand-formation capability, increasingly in agent-legible form, to whoever does operate the buying agent.

### 4.4.4. WhatsApp Business as the Underpriced Agentic Commerce Asset

The exception to "no rails" is WhatsApp. In India and Brazil, WhatsApp Business already functions as conversational-commerce infrastructure, with merchant catalogs, business messaging at enormous scale, and payment integration in select markets. Business messaging is also Meta's fastest-developing monetization line outside the feed. If agentic commerce in emerging markets routes through messaging rather than through OS assistants or marketplace apps — a plausible path given existing behavior — WhatsApp is the one Meta property positioned at the *execution* layer rather than the inspiration layer. We regard it as the most underpriced agentic asset in Meta's portfolio and a key monitoring item.

### 4.4.5. Scenario Bifurcation

Meta's outcome distribution is the widest of the five. In the scenario where discovery remains social — humans continue to want inspiration, status signaling, and serendipity from feeds and creators — agents become *buyers* of Meta's demand signal, and Meta's upper-funnel toll survives the transition intact or strengthened (agent-legible ad formats could even raise yield by improving attribution). In the scenario where delegated, needs-based purchasing generalizes — the agent restocks, replaces, and selects with minimal human browsing — the inspiration stage itself is bypassed for growing categories of spend, and Meta's funnel share structurally shrinks. Which scenario dominates is largely a function of category: delegation plausibly wins in replenishables and utilities; social discovery plausibly persists in fashion, beauty, travel, and identity-adjacent consumption, which happen to be Meta's strongest ad verticals. The blended outcome is survivable; the tail risk is not trivial.

### 4.4.6. Hardware Hedge: Glasses as OS Bypass

Meta's smart-glasses line is best understood in this report's framework as an intent-capture and OS-bypass play: a hardware surface where Meta's agent is the system agent, capturing needs at the moment of formation (visual context, real-world triggers) without passing through the iOS/Android action-layer toll. Through the first half of 2026 this shifted from strategic option to shipping product. On June 23, 2026, Meta launched its first own-brand AI glasses — the Adventurer and Fury lines plus a Kylie Jenner collaboration — starting at $299 (roughly $80 below the prior Ray-Ban Meta generation), each launching with Meta AI powered by Muse Spark. The category is inflecting: shipments of display-free smart glasses rose 167% year-over-year in Q1 2026, Meta held 69.2% of the smart-glasses market per IDC (with some alternative trackers estimating higher), and Zuckerberg has stated daily glasses users tripled year-over-year. The move to Meta's own brand (manufacturing still via EssilorLuxottica) is strategically the point — it transfers control of pricing, distribution, and the product narrative to Meta, the prerequisites for treating the device as a proprietary control-plane surface rather than a licensed accessory.

Two facts discipline the bull case. First, distribution of the *assistant* still lags badly: Pew Research Center's June 2026 survey of ever-use penetration among U.S. adults — the share who report having ever used each assistant, not regular usage or preference — puts ChatGPT at 44%, Gemini at 24%, and Meta AI at 14%, so Meta is seeding a hardware surface for an assistant most consumers do not yet reach for. Owning the glasses does not by itself close that gap; it wagers that a new form factor resets the assistant-choice moment before rivals arrive. Second, the competitive window is closing: Google and Samsung are expected to ship Android XR glasses with Gemini integration in late 2026, and OpenAI has a hardware program in development — meaning Meta's roughly 70% share reflects a market it currently has largely to itself, not a defended position. The glasses remain the only credible path by which Meta could own a device-level control plane, and their option value rises in direct proportion to how aggressively the OS duopoly encloses the mobile action layer — but that value is now being priced against imminent entry by the very OS owners doing the enclosing.

## 4.5. OpenAI — New Intent Surface, Unproven Execution

### 4.5.1. The Instant Checkout Post-Mortem

OpenAI's 2026 provides the cleanest natural experiment on the difficulty gradient between intent and execution. On February 16, 2026, OpenAI launched "Buy it in ChatGPT" — Instant Checkout, powered by the Agentic Commerce Protocol co-developed with Stripe — to all U.S. users including the free tier, with Etsy live, over a million Shopify merchants in the onboarding pipeline, and a reported 4% fee for participating Shopify merchants (OpenAI's own announcement referred only to a "small fee"). By March 24, OpenAI had retreated: native checkout was effectively retired, with the company stating the initial version "did not offer the level of flexibility we aspire to provide." Industry reporting indicates fewer than thirty of Shopify's millions of merchants ever went live, and that OpenAI and Shopify were unprepared for the operational complexity of AI-native checkout — inventory sync, variants, shipping logic, fraud, returns, disputes. The episode validates this report's core decomposition: ChatGPT had captured intent at extraordinary scale (on the order of 800–900 million weekly active users and tens of millions of shopping-related queries per day, per company-adjacent estimates), and intent capture still could not be converted into execution by protocol fiat.

### 4.5.2. Pivot to Discovery-First

The revised posture is discovery-first: merchants share product feeds and promotions so their products are fully represented in ChatGPT, checkout happens on merchant-controlled experiences, and deeper integrations migrate into ChatGPT apps where merchants retain control. Target, Sephora, Nordstrom, Lowe's, Best Buy, The Home Depot, and Wayfair are among retailers integrated with ACP for discovery; Walmart's ChatGPT app is the template for the deeper path. In funnel terms, OpenAI has consolidated at the intent/comparison stage and outsourced execution to merchants — a humbler architecture, but one that conveniently positions ChatGPT as the neutral demand source that every retailer *except* Amazon has an incentive to feed (Amazon blocks external agents; non-Amazon retail sees ChatGPT as its best chance to recapture demand that currently defaults to Amazon).

### 4.5.3. Structural Gaps

OpenAI's deficits are the inverse of the incumbents': no payment rails of its own (Stripe is a partner, not a captive), no fulfillment, no catalog ground truth, no longitudinal purchase history, no OS action surface on mobile, and a personal-context graph limited to conversation memory. Its hardware program (the io/Ive device effort) and its protocol entrepreneurship (ACP) are the two structural remedies in motion; both are multi-year propositions.

### 4.5.4. The Capex Clock

OpenAI's compute commitments make monetization urgency a strategic forcing function. This is usually framed as weakness; in competitive-dynamics terms it is also OpenAI's greatest asset. Alone among the five, OpenAI has no advertising auction to protect, no marketplace take rate to defend, no installed margin structure that agentic commerce can cannibalize. It can price take rates to win, accept thin commerce margins for share, and weaponize the incumbents' dilemmas against them. We expect OpenAI to remain the most aggressive actor in the field — and the most likely to force the pace for everyone else, exactly as Instant Checkout (however operationally premature) forced Google's UCP timeline and Amazon's Alexa for Shopping consolidation.

## 4.6. Apple — The Tax Collector, Not the Competitor

### 4.6.1. App Intents + On-Device Context + Apple Pay

Apple is not building a shopping agent, an ad network of consequence, or a marketplace. Its position is upstream of all of those: it owns the device context graph (the most intimate permissioned dataset in consumer technology — location, health, payments, messages — across roughly two billion active devices), the action registry through which agents reach iOS apps, and a stored-credential payment instrument (Apple Pay) sitting one biometric gesture from any agentic transaction. The strategy visible in WWDC 2026's architecture is to let others fight the demand war while Apple ensures that, on its half of the world's premium devices, every agentic interaction passes through surfaces Apple controls and can eventually toll.

### 4.6.2. Low-Ambition, High-Certainty

This is the lowest-variance strategy among the five. Its principal risks are execution (Apple's harness-engineering credibility after the 2024–2025 Siri failures remains the open question; the Gemini partnership is an admission, not a solution, on this front) and regulation (the EU launch gap previews a world where the toll position itself is the enforcement target). Its principal limitation is ambition: Apple's design wins it a percentage of agentic commerce, not leadership of it. For investors, Apple in this framework is a royalty on the ecosystem's growth rather than a bet on any contestant.

---
# 5. The Protocol War: Consumer Equivalent of the Enterprise Interoperability Battle

## 5.1. ACP vs. UCP vs. Amazon's Closed Stack

Beneath the agent competition runs a standards competition that will determine who sets the economics of agent-mediated transactions. Three architectures are in the field. OpenAI's Agentic Commerce Protocol (ACP), co-developed with Stripe and live since late 2025, defines how agents discover products from merchant feeds and (in its original ambition) execute checkout through a standardized session API; after the Instant Checkout retreat, ACP's center of gravity has shifted to the discovery layer, with checkout devolved to merchants. Google's Universal Commerce Protocol (UCP), announced in January 2026 with a retail coalition, is being integrated into Search AI Mode and Gemini, and is paired with Google's separate Agent Payments Protocol (AP2) work on the settlement side. Amazon's stack is deliberately closed on the demand side — external agents are excluded from the catalog — while being commercialized on the supply side through ASA on AWS.

For merchants, the practical consequence is dual (or triple) implementation: industry guidance through the spring of 2026 has converged on supporting both ACP and UCP, since they capture different traffic — ACP excels at conversational discovery, UCP at high-intent search-adjacent queries — and structured product data increasingly determines visibility inside every agent surface.

## 5.2. Payment-Network Protocols: The Settlement Layer

The card networks and payment processors are running a parallel race to become the trust layer for agent-initiated payments: Visa's agentic-commerce credentialing work, PayPal's ACP server (bringing tens of millions of small businesses into agent-discoverable inventory), and Stripe's position inside ACP itself. The settlement layer matters because it is where delegation risk is underwritten — fraud rules, chargeback rights, and agent-authorization standards will define how much spending consumers are actually willing to delegate. Whoever's credentialing standard wins functions as the de facto licensing authority for shopping agents.

## 5.3. Amazon v. Perplexity: The Unsettled Hinge

Amazon v. Perplexity is the legal hinge of the protocol war, and its outcome is open — a fact easily lost in early commentary that treated the March 2026 district-court injunction as a settled precedent for platform-level agent exclusion. The procedural posture as of this writing: the district court found Amazon likely to succeed on a CFAA/CDAFA theory (user permission ≠ platform authorization, leaning on *Facebook v. Power Ventures*) and enjoined Comet from Amazon's logged-in pages; the Ninth Circuit then stayed that injunction within about a week, allowing Comet to keep operating during appeal; oral argument was heard in Seattle on June 11, 2026; Mozilla and the EFF filed amicus briefs supporting Perplexity; no appellate ruling has issued. The appellate stay is itself the signal — such stays of preliminary injunctions are uncommon, and the first stay factor is likelihood of success on the merits, so granting it suggests the panel regards Perplexity's position as non-frivolous — an inference from procedure, not a ruling on the merits. Two divergent worlds branch from the ruling. If the Ninth Circuit affirms, retailers gain a durable legal basis to exclude unauthorized agents, and the opt-in, protocol-mediated model is ratified — favoring walled gardens, protocol owners, and incumbent aggregators with negotiating leverage. If it reverses (or narrows the CFAA reading to exclude user-delegated access), permissionless agents are re-legalized at the merchant layer, protocol adoption becomes a convenience rather than a gatekeeping necessity, and insurgent agents regain leverage. This is the single highest-value binary in the entire consumer-agent landscape, and it remains unresolved rather than decided.

## 5.4. Who Sets the Take Rate

The endgame of the protocol war is rate-setting power. Early reference points: the reported 4% fee for participating Shopify merchants at Instant Checkout launch; marketplace referral fees and affiliate commissions (mid-single-digit to mid-teens percentages depending on category); and payment networks' ~2–3% interchange as the floor case. Apple's 15–30% app-store commission is not a valid ceiling reference here: under current rules neither Apple nor Google applies digital-goods commissions to physical-commerce transactions. Our working assumption is that agentic take rates settle in the low-to-mid single digits for protocol-mediated transactions — commerce margins cannot bear app-store-scale percentages — additive to existing payment costs, and that placement/sponsorship *inside* agent recommendations, rather than the transaction fee itself, becomes the larger revenue pool (see Section 8).

## 5.5. Parallel to MCP Standardization in Enterprise

Structurally, this is the consumer reprise of the enterprise interoperability battle documented in Part I: MCP standardized agent-to-tool connection in the enterprise and shifted value toward whoever governed the connection registry. ACP/UCP are attempting the same standardization for agent-to-merchant connection. The lesson from Part I carries over: the protocol that wins is rarely the most technically elegant; it is the one bundled with the largest existing distribution. By that criterion UCP (bundled with Search and Android) starts ahead, with ACP's counter-asset being ChatGPT's conversational volume and Stripe's merchant penetration.

---

# 6. Comparative Assessment: The Five-Player Scoring Matrix

## 6.1. Methodology

We score each player on six attributes, rated 0–3 (3 = decisive advantage). *Intent capture* measures default position at the moment of need expression. *Context/data* measures the depth and permission status of the personal graph. *Execution* measures payment, catalog ground truth, and fulfillment. *OS action surface* measures privileged access to a device-level action registry. *Model capability* measures frontier-model position including procurement optionality. *Self-cannibalization burden* is scored inversely (3 = little or nothing to lose; 0 = maximal conflict between agentic success and existing P&L).

## 6.2. Matrix Results

| Attribute                                      | Google | Apple  | Amazon | Meta  | OpenAI |
| ---------------------------------------------- | ------ | ------ | ------ | ----- | ------ |
| Intent capture                                 | 3      | 1      | 1      | 2     | 3      |
| Context / data                                 | 3      | 3      | 2      | 2     | 1      |
| Execution (payment, ground truth, fulfillment) | 1      | 1      | 3      | 0     | 0      |
| OS action surface                              | 3      | 3      | 0      | 0     | 0      |
| Model capability                               | 3      | 1      | 1      | 2     | 3      |
| Self-cannibalization burden (inverse)          | 0      | 3      | 1      | 1     | 3      |
| **Total (unweighted)**                         | **13** | **12** | **8**  | **7** | **10** |

*The scores are illustrative qualitative judgments, not statistically estimated quantities; one-point differences in totals should not be read as measured advantages.*

Three readings of the matrix. First, Google's raw-asset lead is real, and its single zero — cannibalization burden — sits on an attribute that bears on _willingness_, not _ability_. Google's integration effort has not in fact been restrained by it, so asset totals that include this attribute may understate its potential to consolidate the full stack. Second, Apple's score is inflated by defensive attributes (context, OS, little-to-lose) and deflated by the two attributes that win demand (intent, model); this is the quantitative signature of a toll strategy. Third, OpenAI and Amazon are mirror images on the merits — OpenAI scores 6/6 on the demand-side attributes Amazon lacks, Amazon scores 3/0 against OpenAI on execution — yet the relationship between them is not clean antagonism. It is a *layer-selective* posture: the two are simultaneously capital-and-compute partners (Amazon's up-to-$50B investment in OpenAI announced February 27, 2026, plus a large AWS Trainium/Bedrock/Frontier compute agreement), commerce adversaries (Amazon continues to block roughly 100 agents, ChatGPT included, from its catalog), and — most tellingly — advertiser-and-platform (Amazon bought sponsored placements *inside* ChatGPT to promote Prime Day in late June 2026). The $50B deal is an infrastructure and equity arrangement, not a commerce alliance, so it does not soften Amazon's catalog exclusion; the two engage on the axes where cooperation is non-cannibalizing (compute, awareness-stage advertising) while walling each other off on the axis where it is existential (organic access to Amazon's product graph). The durable strategic fact survives — ChatGPT remains the natural demand ally of *non-Amazon* retail, since Amazon still refuses to let ChatGPT recommend Amazon products organically — but the two are best modeled as selective counterparties, not pure antagonists.

Sensitivity: weighting execution and context 2x (on the thesis that habit and trust dominate late-stage adoption) lifts Amazon and Apple relative to OpenAI; weighting intent 2x (on the thesis that the front door takes all) concentrates the contest on the two intent-capture leaders, Google and OpenAI — Apple's arithmetic total survives that reweighting (tying OpenAI at 13 against Google's 16), but a front-door-takes-all world is precisely the one in which Apple's intent score of 1 is disqualifying, whatever its defensive attributes sum to. The base case in Section 7 deliberately avoids resolving this weighting question, because the funnel itself is partitioning along exactly these lines.

## 6.3. Vulnerability Analysis: Which App Categories Get Disintermediated

Applying Part I's vulnerability taxonomy to consumer app categories: maximal exposure attaches to *aggregation-without-assets* — comparison and affiliate services (travel meta-search, coupon/cashback, review aggregators, SEO-dependent affiliate publishers) whose entire economic function (assembling options for a human to compare) is the function agents internalize. High exposure attaches to *vertical commerce front-ends* (food delivery, ride-hailing, ticketing) which survive as fulfillment networks but lose interface ownership, compressing their ability to upsell, advertise, and cross-promote — the reported App Intents partner list (Uber among them) suggests such players are choosing endpoint status over invisibility. Moderate exposure attaches to *destination retailers with differentiated assets* (inventory, brand, loyalty), who gain a new demand channel (ACP/UCP) even as they cede interface. Lowest exposure attaches to *identity- and entertainment-driven surfaces* (social, video, gaming), where the session is the product and there is no task to delegate — though their *commerce attachment* revenue is exposed per Section 4.4.5.

## 6.4. The Asymmetry of Incumbency

A unifying result across the matrix: in agentic commerce, incumbency is simultaneously the largest asset (context, rails, habit) and the largest liability (every incumbent monetization model is a tax on friction that agents remove). OpenAI's strategic identity is that it is the player least encumbered by an incumbent commerce monetization model — though it remains constrained by compute costs and by the execution assets it lacks — which, given capital-market patience, is historically the profile of the actor that forces an industry transition onto everyone else's P&L.

---
# 7. Scenarios and Equilibria (2026–2030)

## 7.1. Base Case — Layered Partition (probability-weighted: ~50%)

The funnel does not consolidate under one agent; it partitions by layer. Intent capture distributes across Google (search-adjacent and Android-default), OpenAI (conversational habit and the non-Amazon retail alliance), and Meta (inspiration-stage and messaging-commerce in emerging markets). Execution concentrates in Amazon's fortress for marketplace categories, with non-Amazon retail served through ACP/UCP protocol coalitions and merchant-controlled checkout. The OS duopoly collects tolls on context access and action invocation without winning the demand war outright (Siri's agent becomes good enough to keep iOS users inside Apple surfaces, not good enough to displace ChatGPT/Gemini habits). Monetization migrates from auctions toward a blend of placement-inside-agents, protocol take rates, and assistant subscriptions. No player's existing franchise collapses, but ad-auction yield growth decelerates structurally at both Google and Amazon.

## 7.2. Bull Case for Google — Full-Stack Consolidation (~20%)

Google accepts front-loaded auction erosion, presses its three-layer advantage, and Gemini becomes the default agent for the Android installed base plus a large minority of iOS users (via app habit and the model-supply relationship), while UCP becomes the dominant commerce protocol. Required conditions: agent-native ad/placement formats replacing auction yield at better than ~0.7:1, with UCP take rates and assistant-subscription revenue bridging the residual gap to the roughly one-for-one standard Section 4.2.2 sets for the P&L to hold; regulatory remedies that constrain conduct but not architecture; and continued OpenAI execution stumbles on commerce. This is the scenario the user-facing market currently prices most readily, and it is genuinely available to Google — but it requires sustained board-level tolerance for revenue self-disruption that few incumbents in history have demonstrated, which is why we weight it below the partition case.

## 7.3. Disruption Case — Regulation Forces Open Action Surfaces (~15%)

The DMA (first) and U.S. remedies (later) mandate third-party agent access to App Intents/AppFunctions on non-discriminatory terms, converting the OS action registries into common carriage. Third-party agents gain device-level reach; the OS toll position degrades to a utility; OpenAI and Meta are the principal beneficiaries; the intent-capture contest becomes a pure product contest. The EU's exclusion from consumer Siri AI at launch is best read as Apple pre-positioning for exactly this fight. A Ninth Circuit reversal in Amazon v. Perplexity — a live possibility given the appellate stay, not a remote hypothetical — would compound this scenario by re-legalizing permissionless agents at the merchant layer as well, and would raise the probability weighting on this branch relative to the ~15% assigned here.

## 7.4. Hardware Discontinuity Case (~15%)

Glasses, pendants, or an OpenAI-class device achieve a smartphone-adjacent adoption curve in a meaningful demographic, resetting the intent-capture layer at a surface where the smartphone OS duopoly holds no registry. Meta is the best-positioned incumbent (shipping volume, content ecosystem, ad model ready to follow attention); OpenAI is the highest-beta entrant. We assign this scenario real weight precisely because all three non-OS players are spending as if it is their primary long-term remedy — which it is.

## 7.5. Milestones and Falsifiers

For the base case: App Intents adoption breadth in transactional verticals by iOS 27 GA (fall 2026); whether agent-era ad formats appear in Alexa for Shopping and Gemini with disclosed pricing; ACP/UCP merchant counts. Falsifiers for the partition case: a credible relaunch of native checkout inside ChatGPT at four-digit merchant scale (would signal intent-layer players *can* descend the funnel); Amazon opening catalog access to an external agent under negotiated terms (would signal fortress economics failing); Gemini agent share materially penetrating iOS (would signal consolidation). For the regulatory case: any DMA specification decision touching assistant access to action registries.

---

# 8. Monetization Models of the Agentic Funnel

## 8.1. What Replaces CPC?

The keyword auction monetized a measurable, repeated moment of revealed intent. Agents do not eliminate that moment; they internalize it and strip its observability from third parties. Three successor models are visible in current deployments. *Placement-within-recommendation*: sponsored eligibility or ranking inside an agent's consideration set — economically a successor to both search ads and retail media, with the critical difference that an agent presenting two options creates radically scarcer inventory than a results page presenting twenty, implying fewer, more expensive slots and brutal competition for "default eligibility." *Transaction take rates*: protocol- or platform-level fees on completed agentic purchases (the reported 4% Shopify-merchant fee under ACP as the early reference). *Assistant subscriptions*: consumer-paid capacity, now tested by every player (ChatGPT tiers, Google AI Ultra at $100/month for power users, Meta AI's May 2026 subscription test) — significant as margin, but structurally a minority revenue stream next to commerce flows.

## 8.2. Take-Rate Economics vs. Placement Economics

Arithmetic favors placement over take rates as the larger pool. Commerce margins constrain take rates to low single digits at scale, whereas placement pricing is bounded only by the advertiser value of default eligibility inside a radically scarcer consideration set. The strategic implication: the players who can operate an *auction for agent attention* — which requires both volume and a neutral-enough position that merchants will bid — are Google and Amazon (conflicted but equipped) and OpenAI (unconflicted, not yet equipped). Apple's instrument is the take rate and the toll, not the auction. Meta's instrument is upstream: selling demand into other players' agents.

## 8.3. The Measurement Problem

Funnel collapse breaks attribution. When discovery, comparison, and purchase occur inside one opaque session, traditional last-click attribution degrades, and incrementality measurement becomes far more dependent on agent-operator cooperation and protocol-level data; the agent operator becomes the primary owner of journey data, and advertising effectiveness becomes difficult for the buyer to audit independently. Expect (a) a repricing of advertising toward surfaces that can prove agent-influenced conversion, (b) protocol-level attribution standards becoming a UCP/ACP battleground, and (c) the structured-product-data layer (feeds, schemas) becoming the new SEO — visibility inside agents is already documented to depend heavily on machine-legible catalog quality.

---

# 9. Investment Implications

## 9.1. Positioning Summary

**Google (beneficiary with embedded hedge, highest variance among incumbents).** The only full-stack contestant; the long thesis is that it monetizes the transition twice (Android/UCP tolls plus agent ad formats), the short thesis is auction compression outrunning replacement yield. The position is effectively long optionality on management's willingness to self-cannibalize — historically the scarcest input. Antitrust outcomes function as a persistent multiple governor.

**Apple (low-beta royalty on the transition).** Wins a toll on agentic activity across two billion devices in most scenarios without needing to win any contest outright. Key swing factors: harness-execution credibility of Siri AI at iOS 27 GA, and regulatory treatment of the action-registry toll position. The reported economics of the Gemini arrangement, to the extent they are confirmed, support rather than undermine the margin thesis.

**Amazon (execution fortress, advertising at risk).** Ground truth plus fulfillment make it the hardest position to disrupt; sponsored-products exposure makes it the incumbent whose highest-margin line is most directly in the agent's path. Watch the rollout of conversational ad formats and any negotiated external-agent access as the tells on whether ad economics survive the interface shift.

**Meta (widest distribution of outcomes).** Supply-side agentification (Advantage+, URL-plus-budget) defends near-term ad yield; the structural question is whether inspiration-stage demand formation survives delegated purchasing. WhatsApp commerce remains the underpriced execution-layer option; the own-brand glasses (shipped June 2026 at $299, roughly 70% category share per IDC) are now a live OS-bypass bet rather than a latent one, but their value must be marked against imminent Gemini-integrated entry from Google/Samsung and a persistent Meta AI assistant-adoption gap. Muse Spark and AI subscriptions extend the model story without yet changing the commerce story.

**OpenAI (private; relevant to public investors through suppliers, partners, and victims).** The pace-setter and the field's only unconflicted actor. The Instant Checkout failure was operational, not strategic — the discovery-first alliance with non-Amazon retail is, if anything, the more dangerous configuration for incumbents. Public-market expressions: long its compute and payment partners; cautious on businesses whose economics assume the persistence of the comparison journey.

## 9.2. Second-Order Exposures

Payments: Stripe (ACP) and the networks' agent-credentialing programs are direct beneficiaries of protocol-mediated commerce regardless of which agent wins. Ad-tech intermediaries built on auction observability face structural headwinds from the measurement problem (8.3). Affiliate, coupon, meta-search, and SEO-dependent publishers are the clearest structural shorts in the framework (6.3). Vertical commerce front-ends bifurcate on whether they own irreplaceable supply (exposure moderate) or merely interface (exposure severe). Retail media networks outside Amazon gain a narrative (every retailer needs agent-legible catalog and placement infrastructure) — the picks-and-shovels of merchant-side agent readiness are a coherent basket.

## 9.3. Signposts to Monitor (Quarterly Checklist)

App Intents coverage among top-200 iOS apps, especially transactional verticals; AppFunctions adoption post-Android 17 GA; disclosed ACP and UCP merchant counts and any published take-rate schedules; appearance and pricing of sponsored formats inside Alexa for Shopping, Gemini, and ChatGPT; Amazon v. Perplexity appellate ruling; DMA proceedings touching assistant/action-registry access; Gemini app and ChatGPT MAU/engagement on iOS specifically; Meta AI subscription conversion and WhatsApp Business commerce metrics; any OpenAI native-checkout relaunch; OpenAI and Meta hardware milestones.

---

# 10. Watch List and Excluded Candidates

## 10.1. xAI/X: Structural Twin of Meta, Below Materiality Threshold

xAI/X shares Meta's archetype — a proprietary real-time social corpus fused with a frontier-model program and a feed-embedded assistant — and is the candidate most frequently proposed for inclusion in this framework. We exclude it on explicit materiality grounds rather than on structural grounds. Against the analytical target of this report (personalized advertising and shopping agents), X fails every scoring axis at threshold: its user base is an order of magnitude smaller than Meta's family of apps (low hundreds of millions of daily users versus ~3.4–3.5 billion daily people), its advertising revenue is two orders of magnitude smaller, its social graph is an interest/news graph with low commercial-intent density relative to Meta's relationship-plus-commerce-adjacent graph, and its commerce and payment infrastructure is nascent. Furthermore, xAI's strategic vector is model-first — its battlegrounds are the frontier-model race and enterprise/government contracts — with X serving as data and distribution appendage, the inverse of Meta's distribution-first configuration.

**Promotion trigger (explicit):** X Money reaching meaningful payment scale *and* Grok integration closing an intent-to-payment loop inside X. Should the "everything app" configuration materialize, xAI/X would possess the execution axis Meta lacks and would be promoted into the core framework — at that point as a more complete archetype than Meta itself. Until then it is carried on the watch list.

## 10.2. Anthropic, Perplexity, and Vertical Agents

Anthropic's strategic center of gravity remains enterprise and developer surfaces (the Part I battleground); its consumer-commerce relevance is currently indirect (model supply, harness IP, and the developer-side presence in agent tooling, including its appearance alongside Google and OpenAI models in Apple's agentic Xcode). Perplexity matters to this report primarily as the legal test case defining agent access rights; its standalone commerce position is sub-scale. Vertical agents (travel-only, dining-only) face the structural problem that the OS and horizontal agents internalize their category the moment it proves valuable; survivors will be those owning supply-side assets rather than interface alone.

## 10.3. China Parallel Track: The Funnel-Collapse Experiment That Already Ran

The Chinese closed-loop platforms — Alibaba (catalog + payment + logistics + agent), Tencent (messaging + payment + mini-programs), ByteDance (inspiration + commerce fused in one surface), Meituan (local fulfillment) — collectively constitute the world's most advanced preview of funnel collapse, having fused discovery, payment, and fulfillment years before agents. A comparative module would test this report's central propositions against an ecosystem where the experiment has partially run: notably, China's experience suggests that super-app consolidation of the funnel is achievable but tends to partition by category rather than produce a single winner — consistent with our base case. A full comparative treatment of the China track is beyond the scope of this report.

---

# Appendices

## A. Event Timeline (January–June 2026)

| Date | Event | Significance in framework |
|---|---|---|
| Jan 11–12, 2026 | Google unveils UCP with retail coalition at NRF; Apple–Google arrangement announced — Gemini technology to underpin next-gen Apple Foundation Models / Siri (terms earlier reported by Bloomberg at ~$1B/yr for a custom ~1.2T-parameter model; unconfirmed) | Protocol war opens; OS model-supply beachhead set |
| Feb 16, 2026 | OpenAI launches "Buy it in ChatGPT" Instant Checkout (ACP/Stripe) to all U.S. users | Intent layer attempts descent into execution |
| Feb 27, 2026 | Amazon announces up-to-$50B investment in OpenAI + AWS Trainium/Bedrock/Frontier compute pact (compute & equity, not commerce) | Compute-layer partnership coexists with commerce-layer exclusion |
| Mar 9, 2026 | District court enjoins Perplexity Comet from Amazon logged-in pages (CFAA/CDAFA) | Platform-authorization theory wins at trial court |
| Mar 17–30, 2026 | Ninth Circuit stays the injunction pending appeal; Comet keeps operating on Amazon during appeal | Uncommon appellate stay signals CFAA theory may not hold |
| Mar 24, 2026 | OpenAI retires native Instant Checkout (fewer than thirty Shopify merchants ever live); pivots to discovery-first, merchant-controlled checkout, ChatGPT apps | Execution proves harder than intent; "AI discovers, merchant checks out" becomes the 2026 settlement |
| Apr–May 2026 | Meta unveils Muse Spark (codename "Avocado"); begins paid Meta AI subscription test (late May) | Meta completes pivot to standalone AI business |
| May 19, 2026 | Google I/O: Gemini Intelligence on Android 17; AppFunctions repositioned as the agentic action layer (Jetpack library in alpha since 2025); Gemini Spark, Antigravity 2.0, Gemini 3.5 Flash; agentic features preview on Galaxy S26 / Pixel 10 | Android positions itself as full-stack agentic platform |
| May 13, 2026 | Amazon launches Alexa for Shopping (Rufus + Alexa+ merged); ASA offered via AWS; Shop Direct / Buy for Me | Bottom-of-funnel fortress consolidates and expands outward |
| Jun 8, 2026 | Apple WWDC (iOS 27 unveiling; Tim Cook's final keynote before Ternus transition): Siri redesign detailed; App Intents positioned as agent action registry; full conversational Siri targeted for iOS 27 GA (~Sept) | Apple's action registry announced, not yet shipped |
| Jun 11, 2026 | Ninth Circuit hears Amazon v. Perplexity oral argument in Seattle (Mozilla, EFF amicus for Perplexity); no ruling yet | Highest-value binary in consumer agentic commerce remains open |
| Jun 23, 2026 | Meta launches first own-brand AI glasses (Adventurer, Fury, Kylie ed.) from $299 with Meta AI powered by Muse Spark; 69.2% smart-glasses share per IDC; display-free glasses shipments +167% YoY (Q1) | OS-bypass hardware hedge materializes |
| Jun 23–26, 2026 | Prime Day 2026: ~$26.4B U.S. retail spend; AI-chatbot referrals highest-converting cohort (+40% vs search/email/social, a first); Amazon buys sponsored ChatGPT placements while blocking organic agent access | First hard empirical read on funnel collapse |

## B. Glossary

**App Intents** — Apple's framework through which apps declare invocable actions; Apple's stated channel for Siri-to-app invocation in the rebuilt Siri (rolling out through the iOS 26.4–iOS 27 cycle in 2026). **AppFunctions** — Android's platform API for exposing app capabilities to authorized agents; the Android counterpart to App Intents. **ACP (Agentic Commerce Protocol)** — OpenAI/Stripe open standard for agent-merchant product discovery and (originally) checkout. **UCP (Universal Commerce Protocol)** — Google's coalition-backed agent-commerce standard, integrated with Search AI Mode and Gemini. **AP2 (Agent Payments Protocol)** — Google's protocol work on agent-initiated payment settlement. **MCP (Model Context Protocol)** — the open standard for agent-to-tool connection whose enterprise standardization was analyzed in Part I; referenced by both Android AppFunctions integration and Gemini Spark. **Private Cloud Compute** — Apple's attested server-side execution environment preserving on-device privacy guarantees for overflow workloads. **Funnel collapse** — this report's term for the compression of discovery, comparison, and checkout into a single agent-mediated session.

## C. Methodology Notes

This report synthesizes public reporting and primary announcements current through early July 2026. Figures identified as "reported" or "estimated" — including the ~$1B/yr Gemini arrangement, the ~$20B/yr search default payment, ChatGPT weekly-active-user counts, advertising-revenue magnitudes, and cross-platform user-base comparisons — are press-reported or analyst estimates rather than company-disclosed line items, and readers should treat them accordingly. The six-attribute scoring in Section 6 and the scenario probability weights in Section 7 reflect Wisdom Hill Research's qualitative judgment as of publication. Full citations are listed in the References section below; where a claim rests on an analyst estimate or single-source report rather than a company disclosure, that status is noted inline.

---

# References

Sources are grouped by theme and ordered to mirror the report's structure. All URLs were accessible as of July 2026. Primary sources (company announcements, official developer documentation, court filings, official newsrooms) are prioritized; trade and analyst coverage is included where it supplies figures or interpretation not available from primary documents. Figures identified in the body as "reported" rest on press reporting rather than company disclosure.

## OS layer — Apple, the Gemini arrangement, and App Intents

1. Apple Newsroom. "Apple unveils next generation of Apple Intelligence, Siri AI, and more." June 8, 2026. https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/

2. Apple Developer. "Explore new capabilities in App Intents." WWDC26 Session 343. June 2026. https://developer.apple.com/videos/play/wwdc2026/343/

3. Apple Developer Support. "Deprecated SiriKit intent domains." https://developer.apple.com/support/deprecated-sirikit-intent-domains

4. Bloomberg. "Apple Plans to Use 1.2 Trillion-Parameter Google Gemini Model to Power New Siri." November 5, 2025. https://www.bloomberg.com/news/articles/2025-11-05/apple-plans-to-use-1-2-trillion-parameter-google-gemini-model-to-power-new-siri

5. CNBC. "Apple picks Google's Gemini to run AI-powered Siri coming this year." January 12, 2026. https://www.cnbc.com/2026/01/12/apple-google-ai-siri-gemini.html

6. AppleInsider. "Apple's new Foundation Models don't contain a drop of Gemini, as we said they wouldn't." June 8, 2026. https://appleinsider.com/articles/26/06/08/apples-new-foundation-models-dont-contain-a-drop-of-gemini-as-we-said-they-wouldnt

7. MacRumors. "Google Confirms Gemini-Powered Siri Coming Later This Year." April 22, 2026. https://www.macrumors.com/2026/04/22/google-gemini-powered-siri-2026/

8. AppleInsider. "Google confirms context-aware Siri built from Gemini will debut in 2026." April 22, 2026. https://appleinsider.com/articles/26/04/22/google-confirms-context-aware-siri-built-from-gemini-will-debut-in-2026

## OS layer — Google, Android, and AppFunctions

9. Google. "Gemini Intelligence: A new era for Android." May 2026. https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/

10. Android Developers. "AppFunctions — Jetpack release notes." Accessed July 2026. https://developer.android.com/jetpack/androidx/releases/appfunctions?hl=en

11. Google for Developers. "Under the hood: Universal Commerce Protocol (UCP)." 2026. https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/

## Platform commerce and commission policies

12. Apple / Analysis Group. "The Continued Growth and Resilience of Apple's App Store Ecosystem." June 2025. https://www.apple.com/newsroom/pdfs/2024-Apple-Global-Ecosystem-Report-June2025.pdf

13. Google Play Help. "Understanding Google Play's Payments policy." Accessed July 2026. https://support.google.com/googleplay/android-developer/answer/10281818?hl=en

## Amazon — Alexa for Shopping, walled garden, and the OpenAI partnership

14. About Amazon. "Introducing Alexa for Shopping, Amazon's AI shopping assistant." May 13, 2026. https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant

15. About Amazon (AWS). "OpenAI and Amazon announce strategic partnership." February 27, 2026. https://www.aboutamazon.com/news/aws/amazon-open-ai-strategic-partnership-investment

16. OpenAI. "OpenAI and Amazon announce strategic partnership." February 27, 2026. https://openai.com/index/amazon-partnership/

17. About Amazon. "Amazon's $50 billion investment in OpenAI: What to know." February 27, 2026. https://www.aboutamazon.com/news/aws/openai-amazon-partnership-explained

18. GeekWire. "Filings: How Amazon's $50B OpenAI deal actually works, and what they're keeping secret." March 1, 2026. https://www.geekwire.com/2026/filings-how-amazons-50b-openai-deal-actually-works-and-what-theyre-keeping-secret/

19. CNBC. "How Amazon's massive stake in OpenAI could boost its AI and cloud businesses." February 27, 2026. https://www.cnbc.com/2026/02/27/amazon-open-ai-cloud-jassy-altman.html

20. TechCrunch. "OpenAI ends Microsoft legal peril over its $50B Amazon deal." April 27, 2026. https://techcrunch.com/2026/04/27/openai-ends-microsoft-legal-peril-over-its-50b-amazon-deal/

## Prime Day 2026 — funnel-collapse evidence and Amazon's ChatGPT ad buy

21. GeekWire. "Prime Day shows how AI is changing shopping, testing Amazon's bet against ChatGPT and others." June 29, 2026. https://www.geekwire.com/2026/prime-day-shows-how-ai-is-changing-shopping-testing-amazons-bet-against-chatgpt-and-others/

22. TechTimes. "Amazon ChatGPT Ads: AI Shoppers Converted 40% Better Than Search During Prime Day." June 30, 2026. https://www.techtimes.com/articles/319387/20260630/amazon-chatgpt-ads-ai-shoppers-converted-40-better-search-during-prime-day.htm

23. Modern Retail. "Amazon buys ads in ChatGPT to promote Prime Day." June 26, 2026. https://www.modernretail.co/technology/amazon-buys-ads-in-chatgpt-to-promote-prime-day/

24. eMarketer. "Amazon's ChatGPT ad buy reveals a bigger strategy." June 2026. https://www.emarketer.com/content/amazon-chatgpt-advertising-agentic-commerce-strategy

## OpenAI — Instant Checkout, ACP, and the discovery-first pivot

25. OpenAI. "Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol." September 29, 2025. https://openai.com/index/buy-it-in-chatgpt/

26. Stripe. "Stripe powers Instant Checkout in ChatGPT and releases Agentic Commerce Protocol codeveloped with OpenAI." September 29, 2025. https://stripe.com/newsroom/news/stripe-openai-instant-checkout

27. CNBC. "OpenAI revamps shopping experience in ChatGPT after struggling with Instant Checkout offering." March 24, 2026. https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html

28. Modern Retail. "Shopify says purchases are coming 'inside ChatGPT' through agentic storefronts as OpenAI retreats on Instant Checkout." March 12, 2026. https://www.modernretail.co/technology/shopify-says-purchases-are-coming-inside-chatgpt-through-agentic-storefronts-as-openai-retreats-on-instant-checkout/

29. Rye. "OpenAI Scales Back ChatGPT Checkout: Why Agentic Commerce Needs Universal Checkout Infrastructure." March 5, 2026. https://rye.com/blog/openai-chatgpt-checkout-agentic-commerce

30. Checkout.com. "OpenAI's agentic commerce shift: What it means for merchants." April 20, 2026. https://www.checkout.com/blog/openai-agentic-commerce-shift

31. Lengow. "ChatGPT wanted to become the world's biggest shop." March 5, 2026. https://blog.lengow.com/chatgpt-wanted-to-become-the-worlds-biggest-shop/

## Protocols and commerce statistics — ACP, UCP, take rates

32. Opascope. "AI Shopping Assistant Guide 2026: Agentic Commerce Protocols." April 16, 2026. https://opascope.com/insights/ai-shopping-assistant-guide-2026-agentic-commerce-protocols/

33. Ekamoira. "ChatGPT Instant Checkout: ACP Protocol Retailer Guide (2026)." February 17, 2026. https://www.ekamoira.com/blog/chatgpt-instant-checkout-agentic-commerce-protocol-2026

34. Elogic Commerce. "ChatGPT Commerce & Agentic Shopping Statistics 2026." May 14, 2026. https://elogic.co/blog/chatgpt-commerce-statistics/

## Amazon v. Perplexity — CFAA litigation and the Ninth Circuit appeal

35. U.S. District Court, N.D. Cal. "Amazon.com Services LLC v. Perplexity AI, Inc., No. 3:25-cv-09514 — Order Granting Preliminary Injunction (Dkt. 81)." March 2026. https://law.justia.com/cases/federal/district-courts/california/candce/3%3A2025cv09514/459191/81/

36. U.S. Court of Appeals for the Ninth Circuit. "Amazon.com Services LLC v. Perplexity AI, Inc., No. 26-1444." Appellate docket. https://dockets.justia.com/docket/circuit-courts/ca9/26-1444

37. U.S. District Court, N.D. Cal. "Amazon.com Services LLC v. Perplexity AI, Inc., No. 3:25-cv-09514." Docket, CourtListener. https://www.courtlistener.com/docket/71874820/amazoncom-services-llc-v-perplexity-ai-inc/

38. CNBC. "Amazon wins court order to block Perplexity's AI shopping agent." March 10, 2026. https://www.cnbc.com/2026/03/10/amazon-wins-court-order-to-block-perplexitys-ai-shopping-agent.html

39. Cooley LLP. "Court Finds AI Agent May Violate State, Federal Law by Accessing Amazon Accounts Without Authorization." March 17, 2026. https://www.cooley.com/news/insight/2026/2026-03-17-court-finds-ai-agent-may-violate-state-federal-law-by-accessing-amazon-accounts-without-authorization

40. CyberScoop. "Appeals court temporarily pauses order blocking Perplexity's AI shopping agent on Amazon." March 17, 2026. https://cyberscoop.com/perplexity-comet-ai-shopping-agent-amazon-lawsuit-ninth-circuit-stay/

41. Search Engine Journal. "Amazon Vs. Perplexity: The CFAA Case That Decides Whether AI Agents Can Visit Your Website." May 31, 2026. https://www.searchenginejournal.com/amazon-vs-perplexity-the-cfaa-case-that-decides-whether-ai-agents-can-visit-your-website/575499/

42. Courthouse News Service. "Perplexity AI asks Ninth Circuit to allow shopping tool on Amazon." June 11, 2026. https://www.courthousenews.com/perplexity-ai-asks-ninth-circuit-to-allow-shopping-tool-on-amazon/

43. PYMNTS. "Amazon Injunction Could Change the Future of Agentic Commerce." March 12, 2026. https://www.pymnts.com/amazon/2026/amazon-injunction-could-change-the-future-of-agentic-commerce/

## Meta — Muse Spark, glasses, and advertising automation

44. Meta. "Introducing Muse Spark from Meta Superintelligence Labs." April 2026. https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/

45. Meta. "Meta and EssilorLuxottica Partner to Launch Meta Glasses." June 23, 2026. https://about.fb.com/news/2026/06/meta-essilorluxottica-partner-launch-meta-glasses/

46. CNN Business. "Meta is now designing its own, cheaper AI smart glasses." June 23, 2026. https://www.cnn.com/2026/06/23/tech/meta-glasses-price

47. Memeburn. "Meta New $299 AI Smart Glasses: Everything You Need to Know." June 2026. https://memeburn.com/meta-new-299-ai-smart-glasses-2026/

48. The AI Insider. "Meta Positions AI Glasses and Personal Agents at the Center of Its Next Growth Phase." January 29, 2026. https://theaiinsider.tech/2026/01/29/meta-positions-ai-glasses-and-personal-agents-at-the-center-of-its-next-growth-phase/

49. Skift. "Smart Glasses to AI Agents: 4 Shifts for Travel From Meta's Earnings." January 28, 2026. https://skift.com/2026/01/28/meta-earnings-travel-glasses-ai/

50. Engadget. "Meta is reportedly working on an AI pendant and more smart glasses." May 30, 2026. https://www.engadget.com/2184224/meta-developing-ai-pendant-more-smart-glass-models/

51. Fortune. "Meta's multimillion-dollar Super Bowl ad may not just be about its smart glasses." February 8, 2026. https://fortune.com/2026/02/08/meta-mark-zuckerberg-super-bowl-advertisement-meta-ai-glasses-smart-glasses-personal-superintelligence-capex/

## Market and adoption data

52. Pew Research Center. "Americans and AI 2026: Chatbots, Smart Devices and Views on Impact." June 17, 2026. https://www.pewresearch.org/internet/2026/06/17/americans-and-ai-2026-chatbots-smart-devices-and-views-on-impact/

53. IDC. "Smart Glasses Surge: The XR Market Is Rewriting Its Own Rules." 2026. https://www.idc.com/resource-center/blog/smart-glasses-surge-the-xr-market-is-rewriting-its-own-rules/

