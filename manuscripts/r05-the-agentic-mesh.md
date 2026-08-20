---
title: "5. The Agentic Mesh"
subtitle: "Protocols, control, and settlement in the post-seat software economy"
series: "The Intelligence Economy"
number: 5
manuscript-revision: 1
date: 2026-08-24
date-modified: 2026-08-24
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  Standard protocols are collapsing the integration tax that held enterprise
  software together. What the resulting distributed operating system looks
  like, who wins the contest for its scheduler, and how agents pay each
  other.

keywords:
  - agentic mesh
  - MCP
  - control plane
  - usage pricing
  - agent settlement
  - service-oriented architecture

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
published:
  dir: reports/r05/
  pdf: r05-the-agentic-mesh.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r05/

# Part IV runs long, so the web serves it as two pages while the PDF keeps
# it as one chapter; `covers` records which subsections each page carries.
chapters:
  - manuscript: "Part I. The Protocol Fabric: Three Axes of Interaction"
    published:  "Part I. The Protocol Fabric"
    fragment:   _01-protocol-fabric.qmd
    page:       01-protocol-fabric.qmd
  - manuscript: "Part II. The SOA Redemption: A Twenty-Year-Old Vision, Finally Buildable"
    published:  "Part II. The SOA Redemption"
    fragment:   _02-soa-redemption.qmd
    page:       02-soa-redemption.qmd
  - manuscript: "Part III. The Agentic Mesh: Enterprise Software as a Distributed Operating System"
    published:  "Part III. The Agentic Mesh"
    fragment:   _03-agentic-mesh.qmd
    page:       03-agentic-mesh.qmd
  - manuscript: "Part IV. The Control Plane Stack: Four Scopes, One Contest"
    published:  "Part IV. The Control Plane Stack"
    covers:     "4.1-4.3"
    fragment:   _04-control-plane-stack.qmd
    page:       04-control-plane-stack.qmd
  - manuscript: "Part IV. The Control Plane Stack: Four Scopes, One Contest"
    published:  "Part IV. The Scope Contest"
    covers:     "4.4-Data Notes"
    fragment:   _05-scope-contest.qmd
    page:       05-scope-contest.qmd
  - manuscript: "Part V. The Monetization Reset: From Seats to Settlements"
    published:  "Part V. The Monetization Reset"
    fragment:   _06-monetization-reset.qmd
    page:       06-monetization-reset.qmd
  - manuscript: "Part VI. The Machine-Native Dollar: Settlement Infrastructure for the Agent Economy"
    published:  "Part VI. The Machine-Native Dollar"
    fragment:   _07-machine-native-dollar.qmd
    page:       07-machine-native-dollar.qmd
  - manuscript: "Part VII. The New Value Chain: Energy → Compute → Intelligence → Work → Settlement"
    published:  "Part VII. The New Value Chain"
    fragment:   _08-new-value-chain.qmd
    page:       08-new-value-chain.qmd
  - manuscript: "Part VIII. Value Migration Map: Winners, Losers, and Investable Layers"
    published:  "Part VIII. Value Migration Map"
    fragment:   _09-value-migration-map.qmd
    page:       09-value-migration-map.qmd
  - manuscript: "Part IX. Risks and Counter-Theses"
    published:  "Part IX. Risks and Counter-Theses"
    fragment:   _10-risks.qmd
    page:       10-risks.qmd
  - manuscript:
      - "Appendix A. Protocol Reference"
      - "Appendix B. The SOA-to-Agentic Stack Mapping Table"
      - "Appendix C. Pricing Model Taxonomy with Vendor Case Studies"
      - "Appendix D. The Four-Scope Control Plane Matrix"
      - "Appendix E. Glossary"
    published:  "Appendices"
    fragment:   _11-appendices.qmd
    page:       11-appendices.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _12-references.qmd
    page:       12-references.qmd
---
# The Agentic Mesh

### Protocols, Control, and Settlement in the Post-Seat Software Economy

**The Intelligence Economy — Report 5 of 14**\
**Wisdom Hill Research | Thematic Investment Research | July 2026**

---

## Executive Summary

### Key Theses at a Glance

This report advances six interlocking theses about the structural transformation of the software industry now underway:

**Thesis 1 — The protocol fabric collapses the integration tax.** Three standardized interaction axes — APIs (app-to-app), MCP (agent-to-tool), and A2A (agent-to-agent) — plus an emerging commerce layer (x402, AP2) are replacing the N² point-to-point integration topology that defined the SaaS era with an N-scaling standardized fabric. Integration-based moats, long the deepest defensive asset of incumbent SaaS vendors, erode structurally as a consequence.

**Thesis 2 — This is the Web Services vision, finally buildable.** The service-oriented architecture (SOA) blueprint of 1999–2010 — dynamic discovery, machine-readable contracts, runtime composition — failed for one fundamental reason: the absence of a universal semantic interpreter. Large language models supply precisely that missing component, solving statistically what ontologies failed to solve symbolically. The vision is being realized, but in probabilistic rather than deterministic form, which relocates the engineering of reliability from compile-time contracts to runtime harnesses — and with it, the locus of competitive differentiation.

**Thesis 3 — Enterprise software is reorganizing into a distributed operating system.** Applications become system calls, agents become processes, model routers become schedulers, the converged data substrate becomes the file system, and the protocol fabric becomes inter-process communication. As in operating system history, the entity that owns the scheduler — the control plane — owns the platform and captures the margin.

**Thesis 4 — The control plane is not a layer but a nested stack of scopes, and value pools unevenly across it.** Control planes are being instantiated at four scopes simultaneously — the economy, the industry, the enterprise, and the department — each controlling different assets and supporting a different quality of rent. The enterprise-scope contest is the most advanced (five camps, now joined by a five-way Forward Deployed Engineering arms race); the universal scope is splitting into federated protocols and contested curation gateways (crystallized by the Agentic Resource Discovery specification of June 2026); and the industry scope — sector semantic authority — is, we argue, the most underpriced position in the stack. Our working hypothesis, held to explicit falsifiers: the widest and narrowest scopes disperse value; the middle concentrates it.

**Thesis 5 — Monetization resets from seats to settlements.** Agents do not occupy seats. Pricing migrates along a spectrum from per-seat to hybrid to usage to outcome-based models, with committed-spend contracts and outcome-based drawdown as the probable enterprise equilibrium. Critically, usage pricing transmits inference cost of goods sold into software gross margins, ending the 80%-plus gross margin identity of the SaaS era for vendors that cannot reduce delivery cost faster than realized price.

**Thesis 6 — The agent economy favors programmable dollars over speculative tokens.** Open, low-value machine-to-machine payments are structurally well suited to stablecoin rails because they combine global accessibility, programmability, and low marginal settlement cost. Stablecoins are not the only viable rail: tokenized credentials, prefunded balances, virtual cards, and multi-rail payment networks can also support agent transactions. Their advantage is therefore not technical exclusivity but a more natural fit with permissionless, high-frequency, machine-native commerce. The monetary unit of the agent economy is likely to remain the dollar in programmable form; this report explicitly separates dollar-denominated settlement infrastructure — a genuine, investable buildout — from volatile token speculation that contaminates early adoption data.

### The Causal Chain: Protocols → Architecture → Control → Pricing → Money

These theses are not independent observations; they form a causal sequence. Protocol standardization (Parts I–II) enables architectural reorganization into the agentic mesh (Part III). The mesh concentrates power in the control plane, whose contest plays out across four nested scopes (Part IV). The mesh makes the agent, not the human, the primary consumer of software, which breaks seat-based pricing and forces the monetization reset (Part V). Usage- and outcome-based pricing at machine scale requires settlement infrastructure that conventional per-transaction payment rails are poorly suited to provide, summoning the machine-native dollar (Part VI). And once economic activity is denominated in inference, compute becomes the base commodity of a new value chain running from energy to settlement (Part VII). Each link conditions the next; each is independently verifiable; and the falsification criteria for each are catalogued in Part IX.

A note on timing. This report's central Part was written in the immediate aftermath of a three-week period — June 12 to July 2, 2026 — in which, while market attention was absorbed by new frontier model releases, five structural moves landed on the control plane itself: Google's Open Knowledge Format, Databricks' Agent Bricks platform relaunch, the multi-vendor Agentic Resource Discovery specification, and successive billion-dollar-plus Forward Deployed Engineering commitments from AWS (June 30) and from Microsoft (July 2). We treat that June as an inflection in the contest this report maps.

### Investment Conclusions and Layer-by-Layer Positioning

Value leaks from three layers: integration middleware whose product was the integration tax itself; commoditized, routable model inference; and thin-workflow SaaS whose function an agent can replicate by composing primitives. Value pools in four layers — control planes (routing, orchestration, verification), semantic catalogs and systems of record, trust infrastructure (agent identity, reputation, audit), and settlement rails (metering, netting, stablecoin clearing) — but with a scope-level precision developed in Part IV: enterprise-scope control planes are a large, competitive, replicable instance business; universal-scope gateway rents are real but likely regulator-capped; and industry-scope semantic authority carries the highest-quality durable rents in the stack. The metering–settlement–trust stack should be treated as a distinct investable category, analogous to what payments infrastructure was to e-commerce circa 2005. Part VIII provides the full migration map and scorecard.

---

# Part I. The Protocol Fabric: Three Axes of Interaction

## 1.1 The Integration Tax: Why N² Point-to-Point Integration Defined the SaaS Era

The economic structure of the SaaS era was shaped less by what software did than by how poorly software talked to other software. Every pair of applications that needed to exchange data required a bespoke integration: custom field mappings, authentication plumbing, error handling, and ongoing maintenance as both endpoints evolved. With N applications in an enterprise stack — and the average large enterprise runs several hundred — the potential integration surface scales as N², and the realized integration burden grew large enough to support an entire industry. Integration-platform-as-a-service vendors, systems integrators, and the professional services arms of every major SaaS company monetized this friction directly. We refer to this aggregate cost as the *integration tax*.

The integration tax also functioned as a moat. A SaaS vendor that could advertise hundreds of pre-built connectors raised switching costs for customers and entry barriers for challengers, because replicating an integration catalog took years of partnership development. Strategically, this meant that incumbency compounded: the more integrated a product, the stickier it became, independent of its functional quality. Much of public SaaS valuation implicitly capitalized this dynamic.

Standardized protocols attack the exponent. When every capability provider implements one standard interface, the integration burden scales as N rather than N². The history of computing offers repeated precedents — TCP/IP versus proprietary networking, USB versus device-specific ports, containers versus bespoke deployment — and in each case the standardization event redistributed value away from those who monetized the friction and toward those who orchestrated the newly fluid components. The same redistribution is the central dynamic of this report.

## 1.2 The Vertical Axis — MCP and the Tool-ification of Applications

The Model Context Protocol (MCP), introduced by Anthropic in November 2024, standardizes how an AI agent discovers and invokes external tools and data sources. Its design premise is that the tool is a *passive capability provider*: it exposes functions with schemas and natural-language descriptions, and the agent — the active, reasoning party — decides when and how to call them. This is the vertical axis of the new fabric: intelligence above, capability below.

Adoption has been decisive. By 2026, MCP was running at roughly 97 million monthly SDK downloads and had achieved support from every major AI platform — Anthropic, OpenAI, Google, and Microsoft — effectively winning the agent-to-tool layer (Digital Applied, 2026). The significance of this is hard to overstate: fierce competitors who agree on almost nothing else converged on a single standard for how agents touch the world. The MCP roadmap for 2026 extends toward asynchronous task handling and longer-running operations, addressing gaps that early production deployments exposed around retry semantics and result lifecycle management (Toloka, 2026).

For application vendors, MCP is both an opportunity and a summons. Implementing an MCP server makes a product legible to every agent in the ecosystem — instant distribution into agentic workflows. But it also converts the product from a destination into a callable function, with consequences for pricing power explored in Parts III and V.

## 1.3 The Horizontal Axis — A2A and Peer-Agent Delegation

The Agent-to-Agent (A2A) protocol, launched by Google Cloud in April 2025 with more than fifty enterprise partners including Salesforce, SAP, Accenture, and Deloitte, addresses the orthogonal problem: how autonomous agents from different vendors discover one another, advertise capabilities, delegate tasks, exchange status, and return results. A2A reached v1.0 in early 2026, adding gRPC support, signed Agent Cards, and multi-tenancy (Intuz, 2026).

The architectural distinction from MCP is intent and security model, not transport. MCP assumes the callee is a passive tool; A2A assumes the callee is a *peer with its own reasoning, planning, and autonomy*. Using MCP where A2A is the correct abstraction produces systems in which sub-agents cannot maintain independent state, authentication context, or task lifecycle (Digital Applied, 2026). The signed Agent Card — a machine-readable, cryptographically verifiable capability advertisement — is A2A's most consequential primitive, because it is the seed of an agent identity and trust system (developed in Part VI).

## 1.4 The Legacy Axis — APIs as Deterministic Contracts

Traditional APIs do not disappear in this architecture; they are reframed. An API is a deterministic contract: fixed schema, known semantics, guaranteed behavior within specification. The agentic layers above are probabilistic. The composite system therefore has a characteristic texture — deterministic primitives composed by probabilistic reasoners — and mature architectures will deliberately push invariants (financial postings, inventory mutations, compliance checks) down into the deterministic API layer while letting the agentic layer handle interpretation, planning, and exception handling. The API layer becomes the bedrock; it simply stops being the place where integration intelligence lives.

## 1.5 The Emerging Fourth Layer: Commerce and Payment Protocols

A fabric in which agents discover and invoke arbitrary services immediately raises the question of payment. A fourth protocol layer is forming to answer it: x402 (Coinbase's revival of the HTTP 402 "Payment Required" status code, enabling in-band stablecoin payment for web resources), AP2 (Google's Agent Payments Protocol, launched September 2025 with x402 embedded and 60+ partners including Coinbase, Cloudflare, and Circle), and commerce-specific protocols such as ACP and UCP for agent-mediated transactions (Indoneo, 2026; Digital Applied, 2026). A complete enterprise agent stack in 2026 is increasingly described as using all layers together: MCP for tool access, A2A for agent coordination, and a payment protocol for settlement (Digital Applied, 2026). Part VI treats this layer in depth; here we note only that its existence distinguishes the current buildout from the failed Web Services era, which never solved payment at all.

## 1.6 Complementary, Not Competing: The Consensus Stack of 2026

The most common analytical error in protocol coverage is framing MCP and A2A as rivals. They are layers: MCP gives an agent hands; A2A gives agents colleagues. Most enterprise architectures designed in 2026 plan to use both — individual agents access tools via MCP while task delegation between agents flows through A2A (Toloka, 2026). An April 2026 industry overview by HonestAI reported enterprise deployments involving both MCP and A2A at more than one hundred organizations — although no underlying company list or survey methodology was disclosed — with the MCP/A2A/WebMCP three-layer stack emerging as a consensus architecture (HonestAI, 2026). Governance of the major protocols under open foundations with RFC processes further reduces the standards-fragmentation risk that destroyed the WS-* stack a generation ago.

The strategic fact to retain from Part I is this: the fabric is no longer speculative. The standards exist, are governed, are multi-vendor, and are deployed. What remains uncertain is not whether software components can interoperate cheaply, but who captures the value released when they do.

---

# Part II. The SOA Redemption: A Twenty-Year-Old Vision, Finally Buildable

## 2.1 The Web Services Blueprint (1999–2010): UDDI, WSDL, BPEL, and the Semantic Web

The vision now being realized is not new. Between roughly 1999 and 2010, the software industry articulated — in remarkable detail — a future in which fine-grained software components, exposed as web services, would be dynamically discovered, understood, and composed into applications at runtime. The blueprint had named parts. UDDI (Universal Description, Discovery and Integration) provided public registries where services would advertise themselves. WSDL (Web Services Description Language) provided machine-readable interface contracts. SOAP provided the messaging envelope. BPEL (Business Process Execution Language) provided orchestration — the static scripting of multi-service workflows. And the Semantic Web project, with OWL-S as its service ontology, aimed at the final step: enabling machines to understand what a service *meant*, so that discovery and composition could proceed without human intervention.

Reading these specifications today is an uncanny experience. Substitute "agent" for "service consumer" and "MCP registry" for "UDDI," and entire passages of early-2000s SOA literature describe the 2026 agentic stack. The vision was correct. The implementation failed completely. Understanding why it failed — and which failure conditions have actually been lifted — is the most reliable way to assess whether the current buildout will share its fate.

## 2.2 Three Failure Modes: The Semantic Bottleneck, Complexity Collapse, and the Missing Economic Layer

**The semantic bottleneck.** For a machine to discover and invoke an unfamiliar service, it must understand what the service does. The SOA era attacked this problem symbolically: meaning would be hand-encoded in formal ontologies (OWL-S, UDDI taxonomies) that machines could process logically. The approach failed on economics and brittleness. Ontology authorship was expensive, required rare expertise, decayed as services evolved, and was never adopted at scale. In practice, the semantic interpretation of every service was performed by human developers reading human documentation and writing glue code — which meant the entire premise of *dynamic* discovery and composition was void. And once humans were the integrators, REST plus JSON beat SOAP plus WSDL decisively, because simplicity for human readers mattered more than machine-readability that no machine could use. REST's victory was not a technical verdict; it was a verdict on where integration intelligence actually resided.

**Complexity collapse.** The WS-* specification stack (WS-Security, WS-Transaction, WS-Coordination, WS-ReliableMessaging, and dozens more) grew by committee far faster than adoption could absorb, until the cost of standards compliance exceeded the cost of bespoke integration the standards were meant to eliminate.

**The missing economic layer.** Dynamic discovery presupposes answers to questions the SOA era never answered: Who operates the registry, and why? Who vouches for service quality? How does a consumer pay for a single invocation costing a fraction of a cent? The public UDDI registries operated by IBM, Microsoft, and SAP were quietly shut down in 2006 — a fitting tombstone. Without trust and settlement, discovery was a feature without an economy.

## 2.3 The Missing Part Arrives: LLMs as the Universal Semantic Interpreter

The large language model resolves the first and most fundamental of these failures, and it does so by inverting the approach. Where the Semantic Web tried to rewrite the world's service descriptions into machine-processable logic, the LLM is a machine that reads the world's descriptions as written. An MCP tool description is prose. API documentation written for human developers is now, without modification, machine-readable. The statistical interpreter succeeded where the symbolic encoder failed because it shifted the cost of semantics from the millions of service authors (who would never pay it) to a handful of model trainers (who already have).

This is the single load-bearing fact of the entire agentic thesis. Every other component of the 2026 stack — registries, schemas, orchestration, payment — existed in some form in 2004. The universal semantic interpreter did not. Its arrival is what converts a twenty-year-old architecture diagram from fantasy into roadmap.

A live design exhibit of this inversion arrived on June 12, 2026, when Google Cloud published the Open Knowledge Format (OKF) — an open, vendor-neutral specification representing organizational knowledge as directories of markdown files with YAML frontmatter, formalizing the "LLM wiki" pattern that practitioners had been reinventing ad hoc. OKF is, in effect, the anti-OWL: it requires exactly one metadata field, leaves links untyped (asserting that two concepts relate without defining how), and instructs consumers to tolerate broken links and unregistered types. A specification this permissive is only coherent because an LLM is presupposed as the interpreter — the statistical reader supplies the semantics the format deliberately omits. Where the Semantic Web demanded that meaning be encoded before machines could act, the post-LLM knowledge format assumes meaning will be inferred. The design philosophy of the 2026 stack has internalized the lesson of 2.2. (OKF remains a v0.1 specification; the adoption conditions attached to it are catalogued among the signposts of Part IX.)


## 2.4 Mapping the Old Stack to the New

The correspondence between the SOA blueprint and the agentic stack is close enough to be tabulated (full table in Appendix B): UDDI's dynamic discovery returns as MCP registries and A2A Agent Cards; WSDL's machine-readable contract returns as MCP tool schemas wrapped in natural-language descriptions; SOAP's envelope returns as JSON-RPC over MCP transports; BPEL's orchestration returns as the agent's runtime planning loop; OWL-S's semantic matching returns as the latent semantic space of the model itself; and WS-Security's federated identity ambitions return as OAuth flows plus signed Agent Cards and emerging agent identity standards. The missing economic layer — UDDI's fatal gap — returns as the x402/AP2 payment protocols and the trust infrastructure of Part VI.

## 2.5 The Critical Difference: Deterministic Contracts vs. Probabilistic Composition

One substitution in this mapping changes everything around it. BPEL composed services *deterministically*: a workflow, once authored and tested, executed identically every time. An agent composes services *probabilistically*: it generates a plausible plan, and "plausible" is a statistical property, not a guarantee. The SOA vision promised contractual reliability; the agentic implementation delivers stochastic best-effort.

This difference relocates the engineering of reliability. In the deterministic paradigm, correctness was established at design time — type checking, contract validation, integration testing. In the probabilistic paradigm, correctness must be established at *runtime*: through evaluation harnesses, output verification, guardrails, retry-and-repair loops, human escalation policies, and audit trails. Reliability becomes an operations discipline rather than a compilation property.

## 2.6 Why Harness Engineering Becomes the Locus of Reliability — and Differentiation

The strategic consequence follows directly. If models are increasingly interchangeable (routable commodities, per Part III) and protocols are open standards available to all, then neither models nor protocols can be the durable differentiator. What differentiates is the *harness*: the engineered envelope of verification, recovery, observability, context management, and permissioning within which probabilistic composition becomes dependable enough for production. Comparative evaluation of leading AI assistants supports this thesis empirically — observed capability differences increasingly trace to harness engineering rather than raw model quality. The harness is to the agentic era what the relational engine was to the database era: the unglamorous layer where reliability is manufactured and margins are defended. Investors should read vendor claims about "model quality" with this substitution in mind.

---

# Part III. The Agentic Mesh: Enterprise Software as a Distributed Operating System

## 3.1 The OS Analogy: Apps as Syscalls, Agents as Processes, Routers as Schedulers

The clearest way to comprehend the emerging architecture is by analogy to an operating system — not as metaphor but as structural correspondence. Applications, once they expose themselves as MCP servers, become *system calls*: discrete capabilities invoked by higher-level processes. Agents become *processes*: units of execution with their own state, lifecycle, and resource consumption. The model/agent router becomes the *scheduler*: the component that decides which execution unit handles which task, under what cost and latency budget. The converged data substrate (Section 3.5) becomes the *file system*. The protocol fabric of Part I becomes *inter-process communication*. And the enterprise itself becomes the machine on which this distributed operating system runs.

The analogy earns its keep through its predictions. Operating system history teaches that (a) application-level profit migrates toward whoever controls scheduling and distribution; (b) the platform owner sets the terms of trade for everything above it; and (c) once an OS achieves critical mass, its interface conventions become nearly impossible to displace. Each prediction is already legible in the agentic buildout.

## 3.2 The Orchestration Layer: Model/Agent Routing and the Control Plane Thesis

Heterogeneous agents and models — varying in capability, cost, latency, and specialization — must be matched to tasks. This routing function is rapidly formalizing. Research frameworks such as MoMA (Mixture of Models and Agents) treat routing as a learned capability: profiling the competence of each model and agent in a resource pool, recognizing query intent, and adaptively assigning execution units to optimize the cost–performance frontier (arXiv:2509.07571). Parallel work on explainable routing benchmarks models across the full cost-capability spectrum — frontier models for hard reasoning, small models for routine extraction — and selects per-task (arXiv:2604.03527).

The router is the scheduler, and the scheduler is the throne. We designate the layer that owns workflow decomposition, execution-unit assignment, result verification, and exception handling as the **control plane**, and we identify it as the principal locus of value capture in the agentic era: as model inference commoditizes into a routable input, margin migrates structurally from the model layer to the routing and orchestration layer above it. But "the control plane" in the singular is a simplification this report can no longer afford. The contest for it involves five distinct camps, is fought at four nested scopes with different assets and different rent quality at each, and accelerated visibly in June 2026. Part IV is devoted to it in full; this Part completes the architectural picture first.

## 3.3 The Re-definition of the App: Headless Capability Providers and Conditional UI

When the agent becomes the primary user of software, the application bifurcates into two personas. The first is the *headless capability provider*: an MCP server exposing the product's functions to any authorized agent. The second is the *conditional UI*: an interface summoned only when a human must see, decide, or approve. This is the tool-ification of the application — not the death of the interface, but its demotion from default to exception.

Tool-ification carries a hard commercial edge. A product invoked as one function among hundreds in an agent's plan has no surface on which to differentiate through experience, build habit, or upsell. Its brand is invisible at the moment of use. Its pricing power compresses toward the marginal value of its function relative to the next-best callable alternative — a comparison the routing agent performs continuously and dispassionately, in a way no human buyer ever did.

The pattern has a twenty-year-old prototype worth naming, because it demonstrates that the headless capability provider is a proven business form rather than a speculative one. Google's Maps API (2005) was precisely this: a capability sold as a callable component, invoked inside other parties' experiences, with no destination surface of its own at the moment of use — and it seeded the Web 2.0 mashup economy. What the mesh does is generalize to *all* software the form that Google's consumer-web components pioneered, which is one reason (developed in Section 4.5) that the company with the deepest portfolio of such components enters the agentic era structurally pre-adapted on the supply side.


## 3.4 Platform Apps vs. Point Solutions: Diverging Fates

The same force that demotes point solutions elevates platforms. An application that owns the *starting point* of workflows — the system of record where intent originates, or the surface where the human meets the agent — occupies the position of the shell in the OS analogy: the gateway through which agent traffic flows. Such platforms gain bargaining power over every capability invoked downstream. The result is a barbell: workflow-originating platforms and deeply differentiated capability providers (proprietary data, regulated functions, physical-world integration) retain pricing power, while the thin middle — single-feature SaaS whose function an agent can replicate or substitute — faces commoditization. The vulnerability of any given SaaS category can be scored on attributes including workflow position, data gravity, substitutability of function, and regulatory shelter; this scoring discipline, developed in earlier reports in this series, becomes the basic hygiene of software equity analysis in the agentic era.

## 3.5 The Data Substrate: OLTP/OLAP Convergence and the Agentic Feedback Loop

Beneath the agents, the data layer is undergoing its own unification, and the driver is the agent's work pattern itself. Agentic applications require tight feedback loops between transactional writes and analytical reads: a single natural-language request to an AI analyst can trigger dozens of concurrent SQL queries as the agent explores datasets and reasons through hypotheses — a high-concurrency, low-latency analytical load that batch-oriented warehouses were never designed to serve, occurring in the same loop as transactional state updates (ClickHouse, 2026). The wall between OLTP and OLAP, maintained for forty years by physics and pricing, is being dismantled because the dominant new workload refuses to respect it.

## 3.6 Converged vs. Composable: Lakebase, HTAP Patterns, and the Open-Catalog Endgame

The industry is answering with two architectures. The *converged* answer is exemplified by Databricks Lakebase, which reached general availability in February 2026, formalizing a new category that pairs Postgres semantics with lakehouse integration — managed synchronization with Delta tables under unified governance — so operational and analytical data coexist with minimal movement; Databricks frames this as the shift "from systems of record to systems of action" (Coeo, 2026). The *composable* answer holds that after a decade of HTAP attempts, the durable pattern is best-of-breed engines stitched tightly: Postgres for transactional state, user context, and vector embeddings; a columnar engine such as ClickHouse for the concurrent analytical queries agents generate — a pattern already in production at AI-native companies (ClickHouse, 2026).

For investors, the adjudication between these matters less than their common denominator: open table formats (Iceberg, Delta) and unified catalog/governance layers as neutral substrate, with the structured/unstructured distinction dissolving into vector indices and semantic layers above. To an agent, a database is not a location; it is a semantic space reached through a catalog and a permission. **The catalog, not the engine, is the strategic high ground of the data layer**, because whoever governs the semantic catalog governs what every agent in the enterprise can know and do.

The thesis received direct corroboration in June 2026. Google rebranded Dataplex as **Knowledge Catalog**, repositioned it as an always-on context engine, and made it the native ingestion point for the Open Knowledge Format (Section 2.3) — a move toward exactly the high ground identified above, and the same pattern Iceberg and Delta established at the table-format layer repeated one level up: neutralize the format, own the point of ingestion. A caveat belongs on the record: if organizational knowledge becomes portable markdown bundles, catalog lock-in at the *format* level weakens — but the catalog's moat was never the file format; it is governance, permissions, and freshness, and format commoditization pushes value toward precisely that enrichment-and-governance tier rather than away from it.

One element of the mesh remains deliberately deferred. The registry — the layer UDDI failed to become, where agents discover tools and other agents, and where discovery bundles with trust certification and payment settlement into app-store economics — has outgrown a section. It is one scope of the control-plane stack, and Part IV (Sections 4.4–4.5) treats it as such.

---

# Part IV. The Control Plane Stack: Four Scopes, One Contest

*Three weeks in June.* Between June 12 and July 2, 2026, while market attention was absorbed by a new wave of frontier model releases — Anthropic's Claude Fable 5 tier chief among them — five moves landed that had nothing to do with model capability and everything to do with the layer above it. On June 12, Google Cloud published the Open Knowledge Format (OKF), a specification for the knowledge that agents consume, and rebranded Dataplex as a "Knowledge Catalog" to ingest it. From June 15–18, Databricks used its Data + AI Summit to relaunch Agent Bricks as a full agent platform wrapped in a runtime governance gateway, an ontology layer, and an open-source meta-harness. On June 17, Google — with Microsoft and Hugging Face as co-authors — published the Agentic Resource Discovery (ARD) specification, a standard for how agents find and verify capabilities across the open web; GitHub and Hugging Face shipped initial reference implementations at launch, while Google announced that native ARD support would follow in its Gemini Enterprise Agent Platform in the coming months. On June 30, AWS committed $1 billion to a dedicated Forward Deployed Engineering organization. On July 2, Microsoft answered with a $2.5 billion, six-thousand-person "Frontier Company."

None of these announcements moved a benchmark score. All of them were bids for context, discovery, governance, and deployment — the four functions this report groups under the control plane. Databricks CEO Ali Ghodsi stated the underlying logic from his own keynote stage: "We don't need more intelligence for AI. We need more context." The market watched the model layer in June 2026; the structural contest was being fought one layer up. This Part maps that contest.

It also corrects a simplification in how the control plane — including in earlier reports in this series — has been discussed. The control plane is not a single layer that one company will "win." It is a **nested stack of control planes at four distinct scopes** — the economy, the industry, the enterprise, and the department — and each scope controls different assets, favors different players, and supports a different quality of economic rent. The question "who captures the control plane" is ill-posed until it is scoped. Sections 4.1–4.3 treat the enterprise scope, where the contest is most advanced; 4.4–4.5 treat the universal scope, where the June announcements concentrated; 4.6 treats the industry scope, which we argue is the most underpriced; 4.7 and 4.8 draw the scenarios and the cross-scope power dynamics together.


## 4.1 From a Layer to a Stack: The Scope Dimension of Control

Part III established *what* the control plane does — workflow decomposition, execution-unit assignment, result verification, exception handling — and *why* it is the locus of value capture as model inference commoditizes into a routable input. What Part III's framing left implicit is *where* that function sits. In practice, orchestration and governance are being instantiated at four different scopes simultaneously, and the instances are complementary rather than substitutive: an enterprise control plane does not compete with an economy-wide discovery gateway any more than a corporate directory competes with DNS.

| Scope | Core assets controlled | Essential function | Structurally advantaged players |
|---|---|---|---|
| **Universal (economy-wide)** | Protocols and standards; agent/tool directories; identity and payment rails | Interoperability and trust across organizational boundaries | Standard-setters and gateway operators (Google, Microsoft; the model labs via MCP influence) |
| **Industry (sector)** | Sector-common ontologies; regulatory mappings; benchmarks; data cooperatives | Shared semantics within a vertical | Sector data authorities (Bloomberg-type, Veeva-type, Epic-type) and platforms descending into verticals |
| **Enterprise** | The firm's own data authority; permissions, governance, audit; fleet-level orchestration | Authority and control inside one organization | Hyperscalers, data platforms, ontology vendors (Microsoft, Google, Palantir, Databricks, Snowflake) |
| **Departmental** | Team workflows; local context; task-specific agents | Execution at the edge | Vertical app vendors and startups; the terminal nodes of the layers above |

Three properties of this stack matter for everything that follows. First, **the controlled asset changes with scope**. At the universal scope the asset is not data at all but standards, discovery, and identity — assets that lose value if any single firm owns them too visibly, which is why they gravitate toward foundations and open licenses. At the enterprise scope the asset is precisely the opposite: proprietary data authority and a governance perimeter that *must* be owned. Conflating the two produces incoherent strategy analysis.

Second, **the network-effect topology changes with scope**. Enterprise control planes are instantiated once per company; each instance is an island, which caps horizontal network effects and keeps the business replicable and competitive. Universal directories and industry ontologies, by contrast, exhibit classic cross-organizational network effects — every additional publisher makes the registry more valuable to every consumer, and every additional bank on a shared sector ontology makes benchmarking and interoperation more valuable to the rest.

Third, **the scopes are locked in a vertical governance contest** — the upper layers attempt to register, constrain, and tax the lower ones — which we take up in 4.8. The winner of the decade may be less the champion of any single scope than the player that spans several and governs downward across them.


## 4.2 The Enterprise Scope I: The Four-Layer Value Chain — and Why "Value Flows to the Model Layer" Is Imprecise

Within a single enterprise, the agentic stack decomposes into a four-layer vertical value chain:

| Layer | Description | Margin character | Defensibility trend |
|---|---|---|---|
| **(A) System of record / authoritative write** | The canonical transactional source of truth | High, annuity-like | The most durable residual moat; strongest in ERP |
| **(B) Application logic + interface** | The packaged app enterprises historically bought | Eroding | Hollowed from both sides; commoditizing |
| **(C) Control plane** | Context, ontology, governance, orchestration of agents | High — the contested prize | Rising fast; the new battleground |
| **(D) Model / inference** | The reasoning engine | Cost-of-goods toll | Unavoidable but commoditizing per token |

The label is no longer analytical shorthand; vendors now use it explicitly. Snowflake markets itself as a control plane for the agentic enterprise, Google describes its consolidated agent platform as a single control plane, and Microsoft frames Fabric IQ as the orchestration and context layer. Databricks' June relaunch (4.3) extends the pattern: its Unity AI Gateway is a control plane by function and, increasingly, by name.

The application profit pool is demonstrably shrinking. ICONIQ's January 2026 State of AI snapshot places average AI-product gross margins near 52% against the ~80% benchmark of mature SaaS, with roughly $230,000 of every $1 million of AI-product revenue exiting as inference cost before any operating expense. That is a literal, mechanical transfer of margin to the model layer — as a **cost of goods**. But the inference line is a *toll, not a throne*: unavoidable, and commoditizing as per-token prices fall across generations. The high-margin tier of the control plane — semantic ontology, the authoritative write path, cross-application governance — favors whoever owns the enterprise's data and decisions, and model providers, lacking both, are structurally furthest from it even as they collect the toll. Capital flows corroborate the vertical migration without resolving the intra-layer contest: of the roughly $297 billion of global venture funding deployed in Q1 2026, an estimated ~81% went to AI companies — overwhelmingly to model infrastructure and adjacent layers [third-party estimate; see Data Notes]. Capital has left the application layer; where it settles within the new stack is precisely the question this Part addresses — and the answer, we will argue, depends on scope.


## 4.3 The Enterprise Scope II: Five Camps Converging on the Throne

The enterprise-scope control plane is contested from five base camps, each carrying a different moat of origin. **Model labs** (OpenAI, Anthropic) descend from harnesses and connector ecosystems into orchestration; their weakness is thinness on data authority and the governance perimeter — the high-margin tier. **Data platforms** (Databricks, Snowflake) ascend from the governed data substrate; their pitch — the best agent lives where the governed data lives — is strongest on the read path and weakest on authoritative write. **Hyperscaler full-stack players** (Microsoft, Google) are the only contenders spanning silicon, data, model, and orchestration. **Ontology/operational vendors** (Palantir) natively bridge layers (A) and (C) — decision-centric ontology with governed write-back — a position no other pure-play holds. **iPaaS/automation vendors** (Workato, Power Platform, UiPath) own the integration graph and are more plausibly absorbed than crowned.

June 2026 materially updated three of these camps and completed a cross-cutting dynamic. We take them in turn.

### Databricks: the substrate camp completes its control plane

Databricks' Data + AI Summit (June 15–18) marked the most complete single-vendor buildout of the four-layer chain outside the hyperscalers. Mapped onto the value chain: on **layer (A)/(C) context**, Unity Catalog now centrally indexes external data models, vector stores, APIs, and dashboards for agent discovery; a Document Intelligence engine parses unstructured formats; a managed agent-memory service runs on Lakebase; and a new **Genie Ontology** grounds agents in enterprise semantics — a direct convergence on the architectural template Palantir established. On **layer (C) governance**, the **Unity AI Gateway** extends Databricks governance from assets to *runtime interactions* — a centralized policy-enforcement proxy across models, agents, MCP services, and tools — with rapidly provisioned Databricks sandboxes for downscoped code execution and, notably, stateful security policies declared in SQL: an agent that touches personally identifiable information is dynamically flagged as tainted and blocked from unverified external actions. This taint-tracking is the most concrete implementation to date of what we have called the context-aware authority tier. On **layer (D)**, Databricks is deliberately commoditizing the model: all frontier models are offered behind one interface — including, as of the Summit, xAI's Grok via a partnership with SpaceX, and Moonshot's Kimi — with intelligent routing that down-routes trivial tasks to cheap models and reserves frontier models for complex orchestration. The open-source **Omnigent** meta-harness (Apache 2.0) extends the commoditization one layer further, wrapping heterogeneous agent harnesses in a uniform API with cost ceilings and contextual policies.

The strategic reading is unambiguous: commoditize (B) and (D), enclose (A) and (C) — a textbook execution of the toll-not-throne logic. Vendor-reported scale (100,000+ agents built on Agent Bricks; over one quadrillion tokens processed annually) is consistent with genuine traction but is unaudited [see Data Notes]. The structural caveat is equally important: Databricks' control plane governs the perimeter of the lakehouse. Its taint policies do not reach data estates outside Unity's gravity, it owns no consumer ecosystem, and it holds no universal-scope assets — which is precisely why it appears among the launch partners of ARD (4.4), hedging its dependence on whoever operates the gateway above it.

### Palantir: the constraint restated

Palantir remains the only pure-play natively occupying the (A)+(C) intersection, and its Q1 2026 results (~85% revenue growth; ~133% U.S. commercial growth) validate the architecture [company-reported; see Data Notes]. But the June developments sharpen the correct statement of its constraint. The constraint is **not** primitive technology — in this framework, frontier models are the commoditizing (D) layer, and their absence is not a strategic deficit — and it is **not** industry experience, of which two decades in defense, government, and manufacturing are the refutation. The constraint is the **scalability of distribution**: an ontology-plus-FDE motion concentrated in high-complexity accounts, now numbering in the hundreds of customers against Databricks' twenty-thousand-plus, whose go-to-market distinctiveness came under direct attack in the very same month (below). Palantir's moat is the *combination* of ontology architecture and embedded deployment; June demonstrated that the deployment half of that combination can be imitated at hyperscaler scale, and that the architecture half is being reverse-engineered (Genie Ontology, Fabric IQ). The falsifiable question for 2026–27 is whether imitation of the parts reproduces the whole.

### Microsoft: distribution plus an embedded context layer — and the broadest cross-scope player

Microsoft is the only contender present in *every* camp of the enterprise-scope contest — OS (Windows), productivity (Office), data (OneLake/Fabric), model access (Foundry), orchestration (Agent Mesh, Copilot Studio), iPaaS (Power Platform), and an operational application incumbent (Dynamics). Its Microsoft IQ context layer (Work IQ, Fabric IQ, Foundry IQ) grounds agents in enterprise knowledge graphs, and Fabric has absorbed SQL Server, Azure PostgreSQL, and Cosmos DB into a single data plane, reaching even on-premise SQL Server via Azure Arc. The architectural constraint is on the write path: Fabric Data Agents remain read-oriented today — they do not perform mutating operations — so Microsoft's extension toward authoritative write, via "Operations Agents," is still maturing. Its edge is the inverse of Palantir's: unmatched installed-base distribution paired with the consolidation instinct of enterprise buyers (Futurum's 1H 2026 survey of 830 IT decision-makers found the "mostly platform" procurement model rising to 65.9% from 60.0% six months earlier, while best-of-breed fell to 20.7%) [third-party survey; see Data Notes]. In scope terms, Microsoft's structural question is whether distribution can buy the governance tier before ontology-native architectures enclose it — the read-to-write race, run against Palantir's template and Databricks' gateway.

June and early July 2026 added three data points, each double-edged. First, ARD: Microsoft co-authored the discovery specification (its co-author R.V. Guha is the creator of Schema.org), and GitHub's agent finder shipped on day one inside the developer workflow Microsoft owns — making Microsoft the only enterprise incumbent with a credible universal-scope registry position, and the reason Section 4.5 treats the gateway race as, at minimum, a two-contender contest. Second, the Frontier Company: the $2.5 billion, six-thousand-person FDE organization announced July 2 completes Microsoft's entry into the deployment arms race, though with the capital-freshness and reorganization caveats flagged in the Data Notes. Third, the Databricks relationship deepened into a fully dual-track structure, partner and rival at once: Genie now surfaces inside Teams and M365 Copilot, and OneLake federation has reached general availability. Microsoft is thus distributing a control-plane rival through its own installed base — a bet that owning the distribution surface outranks owning every layer beneath it. Consistent with the vertical-contest analysis of Section 4.8, Microsoft has the broadest cross-scope position among the enterprise incumbents, spanning three of the four scopes — universal, enterprise, and departmental; its structural gap is the industry scope, where sector-specific semantic authority is the single asset distribution cannot quickly buy.

### The FDE arms race: five players across three camps

Forward Deployed Engineering completed its transition from Palantir idiosyncrasy to industry-standard go-to-market (GTM) practice in roughly fourteen months, and June closed the loop. In May 2026, OpenAI stood up **The Deployment Company**, a standalone entity majority-owned by OpenAI with more than $4 billion from a private-equity consortium [backer attribution varies across reports; see Data Notes], and Anthropic formed a ~$1.5 billion joint venture with Goldman Sachs, Blackstone, and Hellman & Friedman targeting mid-sized companies, beginning with the sponsors' own portfolios. On June 30, **AWS** committed $1 billion of internal resources to a dedicated FDE organization seeded with thousands of engineers deployed in pods of five to six. On July 2, **Microsoft** announced the **Frontier Company**: $2.5 billion, six thousand people, led by Rodrigo Kede Lima. Google Cloud has opened FDE recruiting. The demand-side driver is well documented: McKinsey's late-2025 global survey found roughly nine in ten organizations using AI in at least one business function, while only about 6% reported significant enterprise-wide value; MIT's Project NANDA, studying pilot outcomes over the same period, put the share of enterprise GenAI pilots delivering no measurable P&L impact at 95%. The deployment gap, not model capability, remains the binding constraint — now underscored by nearly $9 billion of announced headline commitments against it, an aggregate whose non-comparability the closing caveats of this section detail.

But "FDE" is one label covering **three distinct business models**, and the distinction determines what each player is actually buying. For Palantir, FDE is *ontology installation*: the engagement ends with a durable software asset occupying layers (A)+(C). For the model labs, FDE is a *distribution channel* financed off balance sheet with external private-equity capital — a services wrapper around model consumption. For the hyperscalers, FDE is *consumption customer-acquisition cost*: whatever the engagement builds, it is built on the sponsor's cloud, converting services labor into an infrastructure annuity. AWS made the divergence from the Palantir template explicit by design — engagements measured in weeks, with customer self-sufficiency as the declared exit condition — the opposite of sticky embedding, implying a high-volume/low-depth economics whose superiority over Palantir's low-volume/high-depth model is unresolved.

Two skeptical readings must accompany the headline numbers. First, **when five players across three camps run FDE, FDE stops being a moat and becomes a cost of doing business** — a labor-intensive arms race with margin-compression, not margin-protection, characteristics. The test that separates moat from cost is whether an engagement leaves behind a reusable semantic asset or a bespoke agent. Second, the commitments are **structurally non-comparable**: OpenAI's is external capital into a separate entity; AWS's $1 billion is internal resources, not a joint venture or conventional investment; and Microsoft's Frontier Company is not a separate legal entity, its six thousand staff are drawn primarily from existing engineering and consulting organizations (Microsoft already operates Industry Solutions Delivery and FastTrack), and the company declined to say whether the $2.5 billion is fresh capital or repurposed budget. Aggregating these figures as equivalent "FDE investment" would overstate the capital formation involved.

Within the scope framework, the FDE surge is the clearest available evidence of what **Scenario 1 competition** (4.7) looks like in practice: the enterprise-scope control plane must be instantiated one company at a time, by hand, and the arms race prices that instantiation cost. It also feeds the industry scope: the sector templates that FDE teams accumulate across repeated deployments are the raw material of industry ontologies (4.6).


## 4.4 The Universal Scope: From Passive Registry to Curation Gateway

Part II established that the agentic stack is the SOA vision rebuilt with a statistical semantic interpreter, and Part III identified the registry (Section 3.6) — the layer UDDI failed to become — as the second great structural question of the decade, alongside the control-plane contest. The scope framework, and the events of June 17, 2026, allow that question to be posed with much greater precision. The universal scope is not one layer but **two sublayers with opposite economics**:

**The protocol sublayer is federating, by design.** MCP and A2A now sit under the Linux Foundation; MCP has crossed roughly 9,600 public servers and ~97 million monthly SDK downloads and is adopted by every major vendor. Neutralized standards are table stakes, not moats: they set the grammar of the mesh and collect no rent.

**The gateway sublayer is where rent can form.** A *passive registry* — the DNS model: anyone lists, discovery is mechanical, no quality judgment — is a public good and earns nothing. An *active gateway* — the search-plus-app-store model: evaluating quality, safety, and provenance; ranking discovery results; vouching for identity and, eventually, clearing payment — is a market maker collecting two-sided gatekeeper rents. The agent economy makes curation not a nicety but infrastructure: agents act autonomously, delegate to other agents, and will transact — and no machine can self-certify the question "can this capability be trusted?" Whoever answers it at scale decides, in effect, which agents economically exist. The web's page-one logic and the app store's featuring logic reproduce themselves one abstraction higher.

**ARD is the empirical instantiation of exactly this split.** Published June 17, 2026 under Apache 2.0 and built on the Linux Foundation AI Catalog Working Group's data model, the Agentic Resource Discovery specification defines two primitives: a static `ai-catalog.json` manifest that any organization hosts at a well-known path on its own domain, describing the MCP servers, A2A agents, skills, and APIs it offers; and a **registry API** that crawls and indexes published catalogs and returns *ranked* matches to natural-language discovery queries. Trust is anchored in domain ownership plus cryptographic trust manifests, letting an agent or registry verify a publisher's identity before connecting. ARD sits entirely before invocation — it finds the capability, which is then called through its native protocol — and is explicitly not a replacement for MCP, A2A, or skills.

Read against the two-sublayer distinction, the design is precise: **publishing is neutralized; ranking is not.** Any organization can emit a catalog at zero marginal cost; the specification itself anticipates a plurality of competing registries, some optimizing for quality and trust, others for coverage. The catalog format is the commons. The registry — the curation gateway — is the contested position, and the contest opened the day the spec shipped: Google positioned its **Agent Registry**, inside the Gemini Enterprise Agent Platform, as its enterprise discovery and governance layer and announced native ARD support for the coming months, including integration with namespaced URNs, agentic egress policies, and trust-manifest verification through Agent Identity; GitHub launched **agent finder**, letting Copilot dynamically discover and invoke MCP servers, skills, and agents at runtime; Hugging Face wrapped its Hub's semantic search in an ARD-compatible discovery layer. The launch coalition — Cisco, Databricks, GitHub, GoDaddy, Hugging Face, Microsoft, Nvidia, Salesforce, ServiceNow, Snowflake alongside Google — reads as the supply side of a two-sided market assembling itself around a gateway whose operator is not yet determined.

One historical rhyme deserves explicit weight. Among ARD's three co-authors is Microsoft's R.V. Guha — the creator of Schema.org. In 2011, Google, Microsoft, and Yahoo jointly neutralized the *markup* standard for structured web data; the value was then captured individually, above the standard, in ranking and knowledge-graph construction, where Google won decisively. ARD replays the pattern one layer up: standardize publishing jointly, compete on curation individually. The prior is that history rhymes; the open question — taken up next — is whether it rhymes in Google's favor a second time.


## 4.5 The Gateway Contest: Why Google Holds the Structural Advantage — and the Case Against

### The case for Google

Five structural assets, in combination, favor Google at the gateway sublayer.

**Scaled automated quality assessment is a search-native competence.** The gateway's core task is evaluating and ranking a vast, heterogeneous, adversarial population of components. That is functionally what a search engine has done for twenty-five years — assessing the quality, trust, and relevance of hundreds of billions of pages, against active manipulation, algorithmically. Apple's App Store curation, by contrast, is human review at the scale of hundreds of thousands of artifacts. When agents, tools, and data components proliferate the way web pages did, automated evaluation at population scale is the binding capability, and only one company has operated it.

**The two-sided ecosystem exists on both sides.** A gateway monetizes only if it aggregates supply (capability publishers) and demand (enterprises and consumers delegating tasks) simultaneously. Google holds billions of consumer endpoints (Search, Android, Chrome, Workspace) *and* an enterprise franchise (Cloud, BigQuery, Gemini Enterprise). Apple holds consumers without the enterprise, data, or cloud estate; Microsoft holds the enterprise with a structurally weaker consumer web; the model labs hold neither at comparable scale.

**The balancing act is itself an accumulated asset.** A trust gateway survives only by continuously balancing self-interest against ecosystem interest — visibly enough that publishers keep publishing and users keep delegating. Google has operated under exactly that tension, in public, across Search and Play, for longer than any comparable firm. We treat this as a genuine, empirically accumulated capability — while noting immediately (below) that its quality is contested by the very regulators who supervise it.

**Model and control plane, simultaneously.** Google is the only player holding a frontier model family *and* the full gateway apparatus — protocol influence (A2A donated to the Linux Foundation; ARD co-authored), the registry product (Agent Registry), identity and payment rails (billions of accounts, Google Pay, Android device identity), and silicon underneath (TPU) that attacks the inference toll itself. OpenAI and Anthropic hold the model without the context, curation, and trust layers; the June pattern — OKF on June 12 standardizing the knowledge container, ARD on June 17 standardizing the discovery layer, each with an open license and a Google-shaped reference implementation (Gemini-based producers, BigQuery sources, Knowledge Catalog ingestion) — supplies two further data points of a consistent strategy: **open the format, own the gravity.**

**The supply side is already stocked.** A gateway needs shelves, and Google is simultaneously the operator of the registry and the largest first-party merchant on it. The rollout has been rapid and systematic: managed remote MCP servers launched in late 2025 (Maps Grounding Lite, BigQuery, Compute Engine, GKE); expanded in February 2026 to AlloyDB, Spanner, Cloud SQL, Firestore, Bigtable, and a Developer Knowledge server; and by April 2026 every Google Cloud service was MCP-enabled by default, joined by Workspace MCP servers (Gmail, Drive, Calendar, People, Chat) and — notably for Part VI — a Google Pay and Wallet MCP server. At Cloud Next '26 Google put the total at more than fifty managed MCP servers generally available or in preview [vendor-disclosed; see Data Notes], fronted by an open-source CLI agent as the native client. No other contender fields an application-level capability portfolio of comparable breadth — geospatial, web-index grounding, translation, vision, media, productivity, payments — because no other contender spent twenty years operating consumer-web capabilities as services rather than selling packaged software.

The historical framing of this fifth pillar requires precision, because the tempting narrative — that Google "prepared earliest" for the mesh — is only half true. Google's *architecture* was pre-adapted: it never had a packaged-software business to unbundle, and its Maps API (2005) was the prototype of the headless capability provider a full two decades before the term (Section 3.3). But its *business model* was mesh-hostile for those same two decades: the SOAP Search API was retired in 2006 and programmatic access to the crown-jewel capability deliberately restricted ever since, because component-izing Search would have unbundled the advertising aggregation that funded the company; the 2018 Maps API repricing displayed the same ambivalence; and on the producer-platform axis it was Amazon, not Google, that institutionalized internal service interfaces by mandate in the early 2000s. What changed is that the agentic era finally gave Google a monetization path for unbundling — per-call component sales, grounding APIs, and gateway rents — dissolving a twenty-year tension between its service-native architecture and its bundle-dependent economics. That resolution, not foresight, explains the extraordinary velocity of the 2025–26 rollout. The accurate formulation: **structurally pre-adapted, strategically late-blooming** — and the lateness has now ended.

### The case against

Five counter-arguments carry real weight, and the thesis is only as strong as its treatment of them.

*First, the gateway race is now explicitly plural.* ARD was co-authored with Microsoft and Hugging Face, and GitHub's agent finder shipped on day one — inside the developer workflow Microsoft owns. The correct claim is not "Google uncontested" but "Google structurally advantaged in an open, multi-contender registry race." Schema.org's history supports the advantage, not the inevitability.

*Second, the regulatory record cuts against the balancing-act claim.* The EU's Digital Markets Act enforcement and successive search antitrust rulings embody regulators' judgment that Google has *not* reliably balanced self-interest against ecosystem interest. Both statements can be true — the capability exists and its exercise has repeatedly crossed legal lines — but a gateway position for the agent economy would be born under the most intense regulatory supervision in the sector's history, and gateway rents may be capped by that supervision rather than by competition.

*Third, the model labs hold proto-gateways.* Anthropic operates the MCP registry and a connector directory; OpenAI operates an enterprise app directory descended from the GPT store. The claim that labs "have no control plane" is too strong. The defensible version is that these are curation surfaces without two-sided ecosystems at Google's scale and without web-scale automated assessment infrastructure behind them — real footholds, unlikely gateways.

*Fourth, the dual role is itself a liability.* The fifth pillar cuts both ways: a registry operator that is also the largest merchant on its own shelves is the Amazon-marketplace conflict reconstituted one layer up. Every ranking decision the Agent Registry makes between a Google Maps capability and a third-party geospatial competitor is a self-preferencing question, and the DMA-era regulatory apparatus is purpose-built to ask it. The stronger Google's first-party supply advantage, the tighter the ceiling regulators are likely to place on its curation discretion — the two pillars partially cancel.

*Fifth, the gateway rent may federate away.* ARD's own architecture — catalogs on publishers' domains, plural registries, an Apache license, a Linux Foundation data model — keeps Scenario 2 (4.7) live: if no registry achieves default status, curation fragments along ecosystem lines and the universal scope earns thin rents everywhere. The signposts in Part IX (registry adoption shares; whether authenticated publisher onboarding hardens into gatekeeping; whether `ai-catalog.json` publication counts follow a power law toward one index) are the discipline on this thesis.


## 4.6 The Industry Scope: The Underrated Middle

Between the universal commons and the enterprise island sits the scope this framework judges most underpriced: the **industry**. Firms in the same sector share most of their conceptual structure — every bank operates on accounts, transactions, risk-weighted assets, and Basel obligations; every pharmaceutical company on trials, patients, regulatory submissions, and pharmacovigilance. Rebuilding that shared structure from scratch inside every enterprise ontology is waste, and waste at scale invites a standardizing layer: sector-common ontologies, regulatory mappings, and benchmark data offered as product.

Two properties make the industry scope structurally interesting. First, it is the only scope below the universal that generates **horizontal network effects**: each additional firm on a shared sector ontology increases the value of benchmarking, regulatory response, and interoperation for all others — without exposing any individual firm's data. Enterprise-scope control planes, instantiated island by island, have no equivalent. Second, it admits **data cooperatives**: anonymization and federated learning allow a sector to train shared models on pooled scale that no single member could assemble, creating a moat that lives at the industry layer itself.

Three classes of candidates are converging on it. (i) **Vertical data authorities** — the Bloomberg, Veeva, and Epic types — who in effect already own the prototype of their sector's ontology. (ii) **Horizontal data platforms descending** — Databricks' industry lakehouses and Snowflake's industry data clouds packaging sector solutions atop governed substrates. (iii) **Deployment-led accumulators** — Palantir's sector ontology templates and the systems integrators, whose FDE engagements (4.3) compound into reusable sector semantics one deployment at a time. The June infrastructure is relevant here too: OKF's explicit design goal of exchanging knowledge bundles *across organizations* makes it a plausible carrier container for sector ontologies, though this remains speculative at v0.1 [see Data Notes].

This section functions as a caveat to our category-asymmetry analysis elsewhere in the series: vertical SaaS vendors judged vulnerable at the *application* layer may hold their sector's semantic authority — and semantic authority, not the app, is the asset the industry scope monetizes. A Veeva or a Bloomberg losing interface workflows to agents while becoming the licensed ontology beneath those agents is a coherent, and investable, outcome.


## 4.7 Where Does Value Pool? Three Scenarios and a Counterintuitive Conclusion

**Scenario 1 — Enterprise-scope aggregation** (*conservative; closest to the present*). Governance, permissions, and audit prove too firm-specific to standardize; each enterprise gets its own control plane instance, sold by Microsoft, Google, Palantir, or Databricks. Rents are moderate: sticky per instance, but replicable, competitive, and without horizontal network effects. The FDE arms race is this scenario's competition made visible — nearly $9 billion committed to hand-building instances one company at a time.

**Scenario 2 — Universal-scope federation** (*the thin-rent world*). Protocols *and* registries neutralize; ARD's plural-registry architecture holds; discovery fragments along ecosystem lines; no gateway achieves default status. Value disperses into the ecosystem, and the durable rents reduce toward the inference toll plus per-instance enterprise business.

**Scenario 3 — Industry-scope oligopolies** (*highest rents, least priced-in*). Sector ontologies with data cooperatives form genuine horizontal moats; one or two "industry control plane standards" emerge per vertical, evolved from today's sector data authorities. In this world the stickiest value accrues neither to the horizontal platforms nor to the model labs but to sector semantic authorities — a materially different winners' map from the consensus.

The most probable outcome is **coexistence with uneven rent quality**: the universal scope federates at the standards sublayer (low rent) even as one or two curation gateways earn real but regulator-capped rents; the enterprise scope remains a large, competitive, replicable instance business (moderate rent); and the industry scope — where horizontal network effects meet proprietary semantics — concentrates the strongest durable moats (high rent). The counterintuitive conclusion, offered as a hypothesis with signposts rather than a forecast: **the widest and narrowest scopes disperse value; the middle concentrates it.** One reconciliation matters for portfolio construction: gateway rents (discovery and delegation brokerage) and industry rents (semantic authority) are *different value sources in a vertical relationship* — the gateway lists and ranks what the sector authorities author — so Scenarios 2-modified and 3 can be simultaneously true, and the two positions hedge rather than exclude each other.


## 4.8 The Vertical Contest: Who Governs Whom Across Scopes

The scopes are not independent strata; they are locked in a governance contest that runs downward. Enterprise control planes work to register and constrain departmental agents — the shadow-AI tension in which departments adopt bottom-up while IT imposes fleet-level governance top-down, today the single largest source of friction in enterprise control-plane construction. Universal gateways work to make enterprise agents discoverable, verifiable, and ultimately taxable objects of registration. Industry standards work to define the ontologies that enterprise instances must speak. Each layer's ambition is to become the governance surface of the layer below.

Mapped across all four scopes, the positions are asymmetric. **Microsoft** is the only player with credible positions across three of the four scopes — universal through ARD co-authorship and GitHub's agent finder, enterprise through the IQ context layer, Fabric, and distribution, and departmental through Office and Copilot at the edge. The industry scope remains its structural gap: sector-specific semantic authority is the one asset distribution cannot buy quickly. **Google** now spans the universal scope (A2A, ARD, Agent Registry, OKF) and the enterprise scope (Gemini Enterprise Agent Platform) with the strongest gateway apparatus, but is light in departmental workflow ownership and holds no sector ontologies. **Databricks** is an enterprise-scope contender and an industry-scope candidate (industry lakehouses), hedging its universal-scope absence through standards coalitions. **Palantir** is deep at the enterprise scope and quietly accumulating industry-scope templates, with no universal-scope presence. **The model labs** hold the departmental edge through harnesses and proto-gateways above, with the enterprise governance tier — the high-margin middle — as their structural gap.

The synthesis for Part VIII's migration map is this: value pools not at "the control plane" in the singular, but at the intersections — the players to overweight are those positioned to govern *across* scopes, and the single most underpriced position in the stack is sector semantic authority at the industry layer, the one scope where neither hyperscaler distribution nor frontier models confer advantage.


### Data Notes — Part IV

The following claims are vendor-sourced, estimated, or exhibit discrepancies across sources; each is identified here so that readers can weigh it accordingly. (1) Databricks DAIS 2026 metrics — 100k+ agents, 1+ quadrillion tokens/year — are keynote figures, unaudited. (2) Palantir Q1 2026 growth rates are company-reported. (3) The OpenAI Deployment Company's backer composition was reported inconsistently in the first days after announcement; subsequent reporting has converged on a partnership led by the private-equity firm TPG, and this report follows that account. The entity's full capital structure has not been disclosed in primary filings. (4) Microsoft has not disclosed whether the Frontier Company's $2.5B is incremental capital; its ~6,000 staff are drawn primarily from existing organizations, and it is not a separate legal entity. (5) AWS's $1B is internal resource allocation, not external investment. (6) The Q1 2026 capital-flow figures (~$297B total; ~81% to AI) are third-party tallies of venture funding compiled from Crunchbase data and reported via Trending Topics EU; they cover venture funding rather than all capital formation, and the AI share reflects company classification choices that vary across trackers. (7) A2A's ~150-organization production footprint is vendor-reported. (8) OKF is a v0.1 draft: its reference parser requires four frontmatter fields where the spec requires one, and no non-Google catalog vendor adoption is yet evidenced; all OKF-dependent arguments in this report should accordingly be read as conditional on the signposts of Part IX. (9) The shared-sector-concept-structure framing in 4.6 is an analytical hypothesis, not a measured figure, and is worded accordingly in the text. (10) Google disclosed at Cloud Next '26 (April 2026) that more than fifty Google-managed MCP servers were generally available or in preview. Earlier third-party tallies circulated a lower count; this report uses Google's own figure. The characterization of this as the largest official first-party catalog is our assessment from public enumeration, not a ranking any vendor publishes. (11) Google Finance is excluded from the first-party capability portfolio in 4.5: its public API was deprecated circa 2012 and no sellable component has existed since; a Gemini-era rebuild is in progress but not yet a component business. (12) The platform-consolidation figures are from The Futurum Group's "1H 2026 Enterprise Software Decision Maker Survey Report" (830 global IT decision-makers, fielded February 2026); the sampling methodology has not been independently reviewed. The survey measures general enterprise software procurement orientation, not agentic-platform procurement specifically; we treat it as a proxy and the inference is ours. (13) The read-only status of Fabric Data Agents and the maturity of Operations Agents reflect product state as of the second quarter of 2026; this is an actively developing product line, and the constraint may be revised by subsequent releases.


---

# Part V. The Monetization Reset: From Seats to Settlements

## 5.1 Why Agents Break Per-Seat Logic

Per-seat pricing rests on a quiet assumption: that software value scales with the number of humans who access it. The seat was always a proxy — a billing convenience standing in for usage, value, and willingness to pay — but it was a serviceable proxy as long as humans were the only operators of software. Agents void the proxy twice over. First, an agent occupies no seat: an enterprise might accomplish more work in a system with fewer licensed humans, sending seat counts and value delivered in opposite directions. Second, agents make labor itself the comparable: when a vendor's agent completes a task end-to-end, the customer's reference price is no longer a software license but the loaded cost of the human work displaced — typically one to two orders of magnitude larger. Seat pricing simultaneously overcharges relative to access and undercharges relative to value. A pricing structure that errs in both directions at once does not survive.

## 5.2 The Pricing Spectrum: Seat → Hybrid → Usage → Outcome

The transition is best modeled as movement along a spectrum rather than a single switch. *Seat* pricing persists where the human remains the operator. *Hybrid* models — seats plus consumption pools — dominate the current transition, preserving ARR optics while metering agentic work. *Usage* pricing (per token, per task, per conversation) aligns billing with cost but not yet with value. *Outcome* pricing (per resolution, per qualified lead, per closed ticket) aligns billing with value delivered and represents the logical terminus: if what the agent sells is completed labor rather than access, the unit of pricing converges on the unit of completed work.

## 5.3 Early Evidence: Per-Conversation and Per-Resolution Pricing in Production

The terminus is no longer hypothetical. Salesforce launched Agentforce with per-conversation pricing on the order of two dollars; Intercom prices its Fin support agent at approximately ninety-nine cents per *resolution* — billing only when the agent actually solves the customer's issue. These are not experiments at the periphery; they are flagship products of category leaders, and their pricing metrics — conversation, resolution — are units of work, not units of access. Every major SaaS vendor's agentic roadmap now includes a consumption or outcome component, and the pricing conversation across the industry has shifted from whether to migrate to how fast.

## 5.4 Three Frictions Slowing the Transition

Three forces ensure the migration is gradual rather than discontinuous. **Revenue volatility:** public-market investors have paid persistent multiple premia for the predictability of seat-based ARR; usage revenue is inherently noisier, and vendors will defend the optics of recurring revenue as long as they can. **Bill shock:** enterprise buyers exhibit strong aversion to unpredictable invoices — the cloud era's FinOps backlash is the controlling precedent — and procurement organizations will demand caps, commitments, and budget governance before accepting open-ended metering. **Incentive misalignment:** naive usage pricing rewards the vendor for inefficiency (more tokens burned, more revenue), placing vendor and customer interests in direct conflict; outcome pricing resolves this misalignment, which is a structural argument for why the spectrum's terminus is outcome rather than usage.

## 5.5 The Likely Equilibrium: Committed-Spend Contracts with Outcome-Based Drawdown

Synthesizing the pressures and the frictions, the probable enterprise equilibrium mirrors the structure the cloud industry converged on: multi-year committed-spend contracts (restoring revenue predictability for the vendor and budget predictability for the buyer) drawn down against metered consumption, with the metering unit migrating over time from raw usage toward outcomes. A secondary form worth monitoring is the *agent seat* — per-agent-instance pricing that frames the agent as digital labor hired at an FTE-like rate. It preserves recurring-revenue optics and maps cleanly onto labor budgets rather than software budgets, an underappreciated advantage given that labor budgets are typically an order of magnitude larger.

## 5.6 Margin Mechanics: How Usage Pricing Transmits Inference COGS into SaaS Gross Margins

The deepest consequence of the reset is not on the revenue line but on gross margin. Seat-based SaaS enjoyed 75–85% gross margins because the marginal cost of serving an additional seat was negligible. Agentic products have real, metered cost of goods sold: every task consumes inference, and usage-based pricing transmits that COGS directly into the P&L. The software industry is acquiring, for the first time, the margin structure of a business with variable input costs — closer to cloud infrastructure than to classical software.

Margin defense therefore reduces to a race between two rates: the decline of realized price per task (driven by competition) and the decline of delivery cost per task (driven by model efficiency, routing optimization, and harness engineering that minimizes wasted inference). Vendors whose cost curve falls faster than their price curve expand margins in absolute terms even as unit prices collapse; vendors who simply pass hyperscaler inference bills through to customers become resellers with reseller margins. Note the compounding strategic role of the router here: intelligent routing — sending each task to the cheapest adequate model — is not merely an architectural nicety but a primary gross-margin lever, which is one more reason value concentrates in the control plane.

## 5.7 Valuation Implications: Repricing the ARR Predictability Premium

The analytical toolkit of SaaS investing requires renovation. Net revenue retention loses meaning when revenue is consumption-based; "seats" disappear as a KPI; gross margin becomes a dynamic variable requiring inference-cost modeling rather than a stable assumption. The metrics that replace them — cost per completed task, outcome attach rates, consumption commitment coverage, gross-margin-per-task trajectory — resemble the unit economics of infrastructure and marketplaces more than of classical software. Two repricing risks follow. Multiple compression for vendors whose ARR predictability premium dissolves before an outcome-pricing story replaces it; and margin-structure surprise for vendors whose agentic revenue grows faster than their inference efficiency. Conversely, the vendors that demonstrate widening spread between realized price per outcome and delivery cost per outcome will deserve — and likely command — premium multiples on a new basis: not predictability of revenue, but defensibility of the work-completion margin.

---

# Part VI. The Machine-Native Dollar: Settlement Infrastructure for the Agent Economy

## 6.1 What This Is Not: Separating Dollar-Denominated Settlement from Token Speculation

A definitional firewall opens this Part. Its subject is **dollar-denominated, fiat-backed stablecoins functioning as programmable settlement infrastructure for machine-to-machine commerce** — not volatile crypto-assets, whose candidacy as the monetary unit of the agent economy this report rejects on functional rather than ideological grounds: autonomous agents operate under budget policies, spending limits, and accounting logic that presuppose a stable unit of account, and a treasury policy cannot be written against an asset that moves ten percent intraday. The revealed preference of the early agent economy confirms the point — settlement activity has concentrated overwhelmingly in USD stablecoins. The correct name for what is being built is not a "token economy." It is the **machine-native dollar**.

## 6.2 The Cost Floor: Fixed Interchange Economics vs. Sub-Dollar Agent Payments

Traditional card-payment economics impose a practical floor: fixed per-transaction fee components make direct settlement of very small payments uneconomic under conventional merchant-pricing structures. The agent economy is likely to generate many transactions below that floor — Indoneo reported that the average payment made by an AI agent through the x402 protocol was approximately $0.20 as of March 2026, although the underlying calculation methodology was not disclosed (Indoneo, 2026); as a per-payment average, the figure measures a different quantity from the volume-mix shares of 6.4 and should not be chained with them. Stablecoin transfers on efficient chains, particularly when combined with the batching techniques of 6.5, can settle such payments at marginal costs measured in fractions of a cent.

This does not make incumbent payment networks technically incapable of serving the market. Aggregation, tokenized credentials, prefunded balances, virtual cards, and emerging multi-rail systems can reduce or bypass the conventional per-transaction cost structure — Mastercard's Agent Pay for Machines, announced June 10, 2026 with explicit support for fractional-cent, high-frequency machine payments settling across card, bank-account, and stablecoin rails, is the clearest instance to date (Mastercard, 2026). The more defensible conclusion is that direct stablecoin settlement begins with a structural cost and programmability advantage, while incumbent networks must redesign their products to compete for the same transaction flows.

## 6.3 The Structural Advantage: Programmable Wallets as Machine Payment Infrastructure

Fee arithmetic is the shallow half of the argument, because fees can be engineered around. The structural half is *account access*. Bank accounts and cards are issued to legal persons after KYC, so an autonomous agent cannot independently become the legal owner of a conventional financial account. In practice, however, neither a bank credential nor a blockchain wallet makes the agent itself a legal economic principal: both operate under authority delegated by a person or organization.

The difference lies in implementation. A blockchain wallet can be created programmatically, equipped with enforceable spending policies and budget limits, and connected directly to open settlement networks. Traditional credentials can also be delegated to agents, but usually through an issuing institution, payment processor, tokenization service, or platform-specific control layer. Wallets therefore offer a more native and portable account abstraction for autonomous software, even though they are not the only possible one.

This distinction is the load-bearing case for stablecoin rails. Their advantage rests on programmability, openness, low marginal settlement cost, and direct interoperability — not on the claim that alternative payment instruments are technically impossible. Incumbent networks can compete, but doing so requires them to reproduce many of the machine-native properties that stablecoin infrastructure provides by default.

## 6.4 The Protocol Race: x402, AP2, MPP and the Unresolved Standards Competition

Unlike the settled MCP/A2A consensus above it, the settlement layer's protocol contest is genuinely open. x402 (Coinbase) embeds payment into the web's request-response cycle via the revived HTTP 402 status code; Google's AP2 (September 2025, 60+ partners, x402 embedded) extends the model to agent-to-merchant commerce with mandate and authorization semantics; MPP and others contest adjacent ground. Two 2026 developments sharpen the race. First, incumbent rails are entering through the mesh's front door: Google shipped a **Pay and Wallet MCP server** in April 2026, making its payment rail directly agent-invokable — early evidence that big-tech proprietary rails and open stablecoin rails will compete *inside the same protocol surface*. Second, the early on-chain record demands disciplined reading: cumulative x402 transactions on Base passed 100 million by Q1 2026, but the mix shifted decisively as speculative activity cooled — payments of $1 or more rose from 49% of volume in early 2025 to 95% by early 2026, while the 10-cent-to-$1 micro-band collapsed from 46% to 4% (Chainalysis, 2026). The disciplined reading is threefold: the rails demonstrably handle load; a substantial share of headline volume was promotional rather than organic; and the steady-state micro-transaction economy this report forecasts has not yet arrived — its arrival gated less by rails than by the deployment curve of budgeted autonomous agents. Investors should treat the layer as pre-consolidation, with the signposts of Part IX as the monitoring discipline.

## 6.5 Settlement Architecture: Batch Netting, Clearing-House Patterns, and Off-Chain Verification

A common misreading holds that every agent interaction settles on-chain. The production architecture is more conservative and more familiar: many small claims verified off-chain and redeemed in periodic on-chain batches — structurally, a recreation of the clearing house. The value-capture implication is significant: the durable businesses in this layer may not be the chains but the *clearing and treasury layers* above them — entities that net obligations, manage agent balances, enforce spending policy, perform sanctions screening, and produce the audit trails enterprise compliance requires. Payments history suggests clearing functions concentrate into few hands and earn infrastructure-grade margins.

## 6.6 Agent Identity and Trust: Signed Agent Cards, ERC-8004, and Reputation Collateral

Settlement presupposes identity: a payment to an agent is only as trustworthy as the answer to "which agent, operated by whom, with what track record?" The identity stack is assembling from both directions: A2A's signed Agent Cards provide cryptographically verifiable capability claims from the protocol side, while ERC-8004 — a decentralized agent identity standard launched in late January 2026 — registered some 24,000 agents within weeks. On top of identity, economic trust mechanisms become possible: staked service guarantees slashed for non-performance, reputation scores accruing to persistent identities, escrowed task payments. These primitives convert trust from an institutional relationship into a priced, collateralized, machine-verifiable property — and they are the raw material of the curation gateways of Sections 4.4–4.5, which synthesize primitive trust signals into ranked, warranted discovery. The registries that anchor them inherit gatekeeping economics accordingly.

---

# Part VII. The New Value Chain: Energy → Compute → Intelligence → Work → Settlement

## 7.1 Compute Tokens as the Base Commodity of the Agent Economy

Pull the threads of Parts III–V together and a unified value chain comes into focus. Every service in the agent economy is, at the margin, a quantity of inference; every quantity of inference is a quantity of compute; every quantity of compute is a quantity of energy. The chain runs **energy → compute → intelligence (tokens) → completed work → settlement (machine-native dollars)**, and its base commodity is the compute token — the metered unit of machine cognition. The familiar wordplay that "AI tokens" and "crypto tokens" are converging contains, once the speculative reading is discarded (Section 6.1), exactly this kernel of truth: the unit of *production* in the agent economy is the inference token, the unit of *settlement* is the programmable dollar, and the economy's defining exchange rate is the price of intelligence in dollars — dollars per unit of completed cognitive work. The secular trajectory of that exchange rate is downward at a pace with few precedents in economic history, and nearly every investment conclusion in this report is, at bottom, a position on who captures the surplus that decline releases.

## 7.2 Commodity Finance Arrives: Spot/Forward Compute Markets, Hedging, GPU-Collateralized Credit

When something becomes a base commodity, commodity finance follows. The early scaffolding is visible — spot markets for GPU capacity, forward contracting of compute, credit extended against GPU collateral — and the logical completions are capacity futures and options, standardized compute benchmarks as deliverable grades, and inference-cost indices against which outcome-priced contracts (Part V) can be marked. An agentic vendor whose gross margin is the spread between outcome prices and inference costs holds, in effect, a commodity-processing margin — a crack spread — and will demand instruments to manage it. The financialization of compute is not a crypto phenomenon; it is ordinary commodity-market formation around a new input, and it will be built predominantly by conventional financial infrastructure.

## 7.3 New Financial Primitives: Agent Wallets, Budgets, Escrow, and Staked Service Guarantees

Above the commodity layer, the agent itself becomes an economic subject. An agent with a wallet, a budget policy, and revenue-generating capabilities is an entity with a P&L — procuring inputs (inference, data, sub-agent services), delivering outputs, and accumulating retained balance. From this follow primitives with no clean precedent: *agent treasuries* governed by code-enforced spending policy; *escrowed task contracts* releasing payment on verified completion; *staked guarantees* in which an agent posts collateral against service quality, slashed for non-performance; and *reputation capital* attached to persistent agent identities (Section 6.6), convertible into pricing power exactly as credit ratings are. The aggregate is a machine economy in the literal sense — autonomous economic agents transacting under programmable institutions. Its emergence will be gradual and bounded by the liability questions of Part IX, but its primitives are being deployed now, and the firms that operationalize them — agent banking, in effect — are building a category that did not exist in 2024.

## 7.4 Micropayments Redeemed: Monetizing the Long Tail of Capabilities

The micropayment dream of the 1990s internet failed on human psychology: the cognitive cost of approving a 30-cent payment exceeds 30 cents, so the web defaulted to advertising and bundled subscriptions. Agents have no payment anxiety. A budgeted agent evaluates a 20-cent API call against its task value in microseconds, which removes the demand-side obstacle that no payment technology could ever remove. The supply-side consequence is the monetization of the long tail: niche datasets, specialized models, narrow capabilities — assets whose audiences were always too small for subscriptions and too disengaged for advertising — become viable businesses at per-call prices — a forecast whose arrival the mix data of 6.4 show is still ahead, with the Part IX signpost as its test. Aggregate long-tail revenue is the kind of dispersed, gradual accrual that headline analyses miss; it accrues most visibly to the registries and clearing layers that aggregate it.

## 7.5 The Bifurcating Internet: The Human Web of Experience vs. the Machine Web of Capability

The internet economy of the last twenty-five years was built on a single premise: human attention arrives at web pages. Search advertising, display advertising, SEO, affiliate economics, and traffic-based valuation all capitalize that premise. Agentic consumption breaks it. The web bifurcates into a *human web* of experience — destinations humans visit for entertainment, community, and judgment — and a *machine web* of capability — endpoints agents invoke for functions and facts, with WebMCP-style standards formalizing the machine-facing layer. On the machine web, a page view never happens: the agent extracts the answer or executes the transaction, and the attention-monetization apparatus collects nothing. Traffic and value, correlated for a generation, decouple.

## 7.6 Demand Aggregation Reordered: From the Search Box to the Agent — Aggregation Theory Updated

Aggregation theory explained the platform era: control of demand (the user relationship) commands the surplus of fragmented supply. The agent is the next and more total aggregator. Search aggregated demand but returned *links* — it monetized the referral while supply kept the transaction. The agent returns *completed outcomes* — it books the flight, files the claim, procures the component — internalizing the entire path from intent to settlement. Whoever owns the agent relationship therefore aggregates demand more completely than any search box ever did; the curation gateway of Sections 4.4–4.5 is this same position seen from the supply side, since the entity that ranks capabilities for agents is the entity that aggregates agents for capabilities. The re-intermediation threat lands squarely on the businesses built in search's shadow: search advertising itself, marketplace take rates predicated on owning discovery, and comparison/affiliate models whose product was navigation. The defensive responses — owning the agent (hence every platform's assistant urgency), becoming the preferred supply of other agents, or retreating to the human web's experiential moats — define the strategic map of consumer internet for the next decade.

## 7.7 Content Economics: From Ad-Funded Attention to Machine-Access Licensing

For content owners, bifurcation forces a business-model substitution. If agents consume content without delivering page views, advertising cannot fund creation; the replacement is *machine-access licensing* — charging agents and their operators for programmatic access, whether per-crawl, per-query, or via bulk licensing of corpora for training and retrieval. The infrastructure for this is arriving from the CDN and payments layers (per-crawl charging mechanisms, x402-style in-band payment for content endpoints), and early licensing markets between content owners and AI operators are establishing reference prices. The transition will be brutally uneven: commodity content loses pricing power entirely (agents substitute freely), while differentiated, verifiable, continuously updated content — exactly the kind institutional research produces — gains a direct monetization channel that the advertising web never offered it. The deeper shift is conceptual: content stops being a destination and becomes a *capability* — priced, licensed, and invoked like any other service on the machine web.

---

# Part VIII. Value Migration Map: Winners, Losers, and Investable Layers

## 8.1 Where Value Leaks

Three layers face structural value leakage. **Integration middleware** monetized the N² topology directly; as the protocol fabric collapses integration cost, the addressable friction shrinks beneath the category. Survivors will reposition as governance and observability layers for agent traffic — a real but smaller and more contested market. **Commoditized model inference** faces the router: when a learned scheduler continuously arbitrages across a heterogeneous model pool, undifferentiated inference is priced like the commodity it has become, and margin migrates to whoever performs the arbitrage. Frontier capability retains scarcity pricing only at the moving edge, and only until the edge is matched. **Thin-workflow SaaS** — products whose essential function is a workflow wrapper around data the customer already owns — faces replication by agents composing primitives, with the vulnerability gradient steepest where workflow position is shallow, data gravity is low, and the function is legible enough for an agent to perform. Category-by-category vulnerability scoring along these attributes is developed in earlier reports in this series and is assumed here.

## 8.2 Where Value Pools

Four layers concentrate value. **Control planes** — the routing, orchestration, and verification layer — capture the scheduler's structural rent and compound it through the gross-margin lever of Section 5.6. **Semantic catalogs and systems of record** govern what agents can know and do; data gravity survives the agentic transition better than any other incumbent moat, because agents amplify rather than reduce the value of governed, authoritative data. **Trust infrastructure** — agent identity, reputation, compliance, audit — is the institutional layer every other layer presupposes; like legal and accounting systems in the human economy, it earns durable rents precisely because it is boring and mandatory. **Settlement rails** — metering, netting, clearing, stablecoin issuance and treasury — inherit the economics of payments infrastructure, with the clearing layer (Section 6.5) the likeliest point of concentration.

Part IV obliges one refinement to this list: "control planes" is a plural spanning four scopes, and the rent quality differs by scope. Enterprise-scope control planes are the largest near-term revenue pool but a replicable, competitive instance business whose customer-acquisition cost the FDE arms race is currently bidding up (Section 4.3). Universal-scope gateway rents are potentially enormous but likely regulator-capped and contested at minimum two ways (Section 4.5). Industry-scope semantic authority — sector ontologies with horizontal network effects and cooperative data moats — carries the highest-quality durable rents and the least market recognition (Section 4.6). Positioning should therefore distinguish *which* control plane a vendor is building, not merely whether it is building one.

## 8.3 Layer-by-Layer Scorecard

**Hyperscalers** enter with distribution, data center economics, and enterprise relationships; their risk is that open protocols neutralize the bundling advantages that cloud-era lock-in provided. Their natural prize is the converged data substrate plus the agent platform. **Frontier labs** enter with the best harnesses and the fastest capability iteration; their risk is COGS exposure and the absence of incumbent enterprise systems of record. Their natural prize is the control plane reached top-down from the assistant relationship. **Incumbent application platforms** enter with workflow ownership and systems of record; their risk is the innovator's dilemma in pricing — outcome models cannibalize seat revenue before replacing it. Their natural prize is the vertical control plane within their own data gravity. **Data platforms** enter holding the catalog high ground of Section 3.6, and as of June 2026 have completed full control-plane productization (Databricks' runtime governance gateway, ontology layer, and managed agent memory; Section 4.3); their risks are hyperscaler absorption and the boundedness of their governance to their own data gravity. **Sector data authorities** (the Bloomberg, Veeva, Epic class) enter holding their vertical's de facto ontology; their risk is application-layer erosion outrunning their conversion into licensed semantic infrastructure — but if the industry-scope scenario of Section 4.7 obtains, they hold the stickiest prize on this scorecard. **Payment networks and stablecoin issuers** split the settlement prize: issuers and clearing layers begin with the structural advantage in machine-native flows, while incumbent networks must re-engineer their products — multi-rail systems such as Mastercard's Agent Pay for Machines are the first such moves — to compete for transactions below their conventional per-transaction pricing floor. Across all six, the recurring pattern is that *position* (workflow origin, catalog governance, clearing function) beats *capability* (model quality, feature breadth) as the durable source of rent.

## 8.4 The Metering–Settlement–Trust Stack as a Distinct Investment Category

The report's most actionable synthesis is that metering (usage measurement and billing), settlement (netting and machine-native payment), and trust (identity, reputation, compliance) form a single coherent stack — the financial plumbing of the agent economy — and deserve coverage as a distinct category, exactly as payments infrastructure deserved distinct coverage in 2005 before the market priced it as such. Each component is individually necessary, the three are architecturally intertwined (billing requires identity; settlement requires metering; trust requires audit of both), and the category currently sits across the seams of existing coverage universes — part software, part payments, part crypto-infrastructure — which is precisely where mispricing lives.

---

# Part IX. Risks and Counter-Theses

## 9.1 The Governance Gap: Production Readiness Lagging Protocol Adoption

The widest near-term gap is between protocol adoption and production readiness. Industry warnings that a large share of agentic AI projects — Gartner has suggested over 40% — could be cancelled by 2027 on unclear value, rising costs, and weak governance (Toloka, 2026) quantify the risk that enterprise enthusiasm outruns enterprise capability. If the gap persists, the timeline of every thesis in this report extends, and the transition-period winners skew toward consulting and governance tooling rather than the structural layers of Part VIII.

## 9.2 The Closed-Bundle Scenario: Vertical Integration Defeating the Open Mesh

The open-fabric assumption can fail. A vertically integrated stack — one vendor's models, harness, data substrate, and distribution, optimized jointly — may simply outperform heterogeneous open composition, as integrated mobile platforms outperformed the open web on its own promised terrain. In that world, A2A-style horizontal protocols become the standard of the second-place coalition, registries fragment along ecosystem lines, and the value migration of Part VIII still occurs but concentrates within one or two walled meshes. We assess this scenario's probability as material rather than residual; the mitigant is that enterprise buyers, unlike consumers, structurally resist single-vendor dependence for core operations.

## 9.3 Security as the Pacing Variable

An open mesh of dynamically discovered, payment-enabled services is, by construction, a supply-chain attack surface: prompt injection propagating through agent chains, confused-deputy privilege escalation across delegation hops, malicious tools in registries, and now-monetizable exfiltration via agent wallets. The state of defense is immature relative to the state of deployment. A single landmark incident — an agent chain moving real money at scale for an attacker — could freeze open-discovery adoption into a semi-closed equilibrium: discovery open, execution allow-listed. Security maturity, more than any technical capability, sets the clock speed of the entire thesis.

## 9.4 Probabilistic Reliability Limits and the Reversion to Static Integration

For workflows where error cost is high and tolerance is near zero, probabilistic composition may never clear the bar, and enterprises will revert to (or never leave) statically engineered integrations — agents proposing, deterministic pipelines disposing. The realistic end-state is a portfolio: dynamic composition for long-tail, low-stakes work; hardened static paths for the regulated core. The investable question is where the boundary settles, since the control plane's addressable market is everything on the dynamic side of it.

## 9.5 The Regulatory Overhang: AML/KYC for Autonomous Wallets and Liability Attribution

Two unresolved legal questions overhang Part VI specifically. First, anti-money-laundering and sanctions frameworks presuppose identifiable human or corporate principals; permissionless agent wallets transacting autonomously do not fit, and the compliance architecture that reconciles them — verified operator registration behind agent identities, policy-enforced wallets, transaction screening at the clearing layer — is being assembled but is not settled law in any major jurisdiction. Second, liability attribution for autonomous transactions (who is bound when an agent contracts badly?) lacks doctrine everywhere. Regulatory resolution is the single largest swing factor on the settlement stack's adoption slope; the base case is accommodation-with-controls, because the dollar-extension logic of machine-denominated settlement gives the largest regulatory jurisdiction a strategic reason to accommodate.

## 9.6 The Scope Thesis Under Stress: What Would Falsify Part IV

The scope framework and its counterintuitive conclusion (edges disperse, middle concentrates) are hypotheses under monitoring, not settled findings. The falsifying and confirming signals, by scope: *Universal/gateway* — whether ARD registry adoption concentrates (Google Agent Registry vs. GitHub agent finder vs. Hugging Face Discover market shares); whether authenticated publisher onboarding hardens into genuine gatekeeping or remains formality; whether `ai-catalog.json` publication counts follow a power law toward one dominant index or distribute across many; whether the MCP registry acquires ranking and certification functions. Failure of any registry to achieve default status by 2028 shifts probability mass to Scenario 2 and thins the gateway thesis. *Industry* — whether Veeva-, Bloomberg-, or Epic-class vendors productize explicit sector ontologies; whether any non-Google catalog vendor (Snowflake, Databricks, Collibra) natively adopts OKF within twelve months; whether data-cooperative structures appear in regulated verticals. Absence of all three by end-2027 would deflate the industry-scope thesis to a footnote. *Enterprise/FDE* — whether hyperscaler FDE engagements are paid or subsidized (loss-leader pricing signals commoditization of the motion); whether engagements leave reusable semantic assets or bespoke agents; whether Palantir's U.S. commercial growth decelerates materially as hyperscaler FDE takes share; disclosed margin impact of FDE labor at AWS and Microsoft; the rate at which enterprises absorb departmental shadow AI into fleet governance. *Cross-scope* — whether Microsoft converts its uniquely broad three-scope presence into cross-scope governance, or the scopes prove genuinely separable markets.

## 9.7 Signposts and Falsification Criteria

Each thesis carries observable falsifiers. *Thesis 1 (fabric):* failure of MCP/A2A registries to consolidate by 2027, or major vendors shipping proprietary forks, would signal re-fragmentation. *Thesis 2 (probabilistic composition):* sustained enterprise reversion to static integration outside regulated cores would cap the paradigm. *Thesis 3 (control plane):* if routing margins compress as fast as model margins — routers becoming commodities themselves — the scheduler thesis fails and value re-concentrates in data gravity alone. *Thesis 4 (scope stack):* the full battery of Section 9.6. *Thesis 5 (pricing):* if hybrid seat-plus-consumption proves a stable equilibrium rather than a waypoint through 2028, the monetization reset stalls at half-depth. *Thesis 6 (settlement):* the critical signpost is the small-transaction share of agentic payment volume — the 10¢–$1 band that collapsed to 4% in early 2026 (Section 6.4) must durably re-expand as genuine machine commerce replaces speculative traffic; failure to re-expand by 2027–28 would indicate that batch invoicing on conventional rails suffices and the machine-native dollar remains niche. A second signpost tracks the rail competition directly: the relative share of agent payment volume settling on direct stablecoin rails versus incumbent multi-rail products (Mastercard's Agent Pay for Machines and successors) — sustained incumbent share gains at comparable economics would falsify the structural-advantage claim, not merely qualify it. These signposts are the basis on which subsequent reports in this series will revisit the theses above.

---

# Appendices

## Appendix A. Protocol Reference

**MCP (Model Context Protocol).** Introduced by Anthropic, November 2024. Standardizes agent-to-tool interaction: tool discovery, schema-described invocation, resources, and prompts, over JSON-RPC transports. Adopted across Anthropic, OpenAI, Google, and Microsoft platforms; 97M+ downloads by 2026. 2026 roadmap: asynchronous tasks, long-running operations, multi-agent primitives. Governance: open specification with community RFC process.

**A2A (Agent-to-Agent Protocol).** Launched by Google Cloud, April 2025, with 50+ enterprise partners; v1.0 in early 2026 with gRPC, signed Agent Cards, multi-tenancy. Standardizes peer-agent discovery, capability advertisement, task delegation, and status exchange. Governance: open-foundation stewardship.

**x402.** Coinbase-developed payment protocol reviving HTTP status 402: server returns a payment specification; agent settles a stablecoin micropayment on-chain (or via batched off-chain verification) and resubmits with receipt. 100M+ cumulative transactions on Base through Q1 2026; multi-chain deployments expanding.

**AP2 (Agent Payments Protocol).** Google, September 2025; 60+ launch partners including Coinbase, Cloudflare, Circle; embeds x402 for stablecoin settlement. Adds mandate/authorization semantics for agent-to-merchant commerce.

**ARD (Agentic Resource Discovery).** Published June 17, 2026; co-authored by Google, Microsoft, and Hugging Face; Apache 2.0, built on the Linux Foundation AI Catalog WG data model. Two primitives: a static `ai-catalog.json` manifest at a well-known path on the publisher's domain describing offered MCP servers, A2A agents, skills, and APIs; and a registry API that crawls, indexes, and returns ranked matches to natural-language queries. Trust anchored in domain ownership plus cryptographic trust manifests. Sits before invocation; protocol-agnostic. Launch partners include Cisco, Databricks, GitHub, GoDaddy, Nvidia, Salesforce, ServiceNow, and Snowflake.

**OKF (Open Knowledge Format).** Published by Google Cloud, June 12, 2026; v0.1 draft, Apache 2.0. Represents organizational knowledge as directories of markdown files with YAML frontmatter; one required metadata field; untyped links; consumers instructed to tolerate broken links. Presupposes an LLM interpreter. Natively ingested by Google's Knowledge Catalog (rebranded Dataplex).

**ERC-8004.** Decentralized agent identity standard, launched late January 2026; ~24,000 agents registered within weeks. Provides verifiable agent credentials underpinning trusted agent commerce.

## Appendix B. The SOA-to-Agentic Stack Mapping Table

| SOA-Era Component (1999–2010) | Function | Agentic-Era Successor (2024–2026) | Key Difference |
|---|---|---|---|
| UDDI registry | Dynamic service discovery | ARD catalogs + registries; MCP registries; A2A Agent Cards | Bundled with trust + payment |
| WSDL | Machine-readable contract | MCP tool schemas + natural-language descriptions | Prose is now machine-readable |
| SOAP | Messaging envelope | JSON-RPC over MCP transports | Radically simpler |
| BPEL | Workflow orchestration | Agent runtime planning loop | Probabilistic, not scripted |
| OWL-S / Semantic Web | Machine understanding of meaning | LLM latent semantics | Statistical, not symbolic; zero authoring cost |
| WS-Security / WS-* | Identity, reliability, transactions | OAuth + signed Agent Cards + ERC-8004 + harness verification | Runtime-enforced, not schema-enforced |
| (absent) | Payment & settlement | x402, AP2, batch clearing | The layer whose absence killed UDDI |

## Appendix C. Pricing Model Taxonomy with Vendor Case Studies

| Model | Unit | Alignment | Exemplars | Failure Mode |
|---|---|---|---|---|
| Per-seat | Human license | Access | Classical SaaS | Voided when agents do the work |
| Hybrid | Seats + consumption pool | Transitional | Most 2025–26 enterprise SaaS | Unstable waypoint; dual-metric complexity |
| Usage | Token / task / conversation | Cost | Salesforce Agentforce (per conversation) | Rewards vendor inefficiency; bill shock |
| Outcome | Verified result | Value | Intercom Fin (~$0.99/resolution) | Outcome attribution disputes |
| Agent seat | Per agent instance | Digital labor | Emerging | Decouples from work volume |
| Committed spend + drawdown | Pre-purchased capacity | Predictability | Cloud-style enterprise agreements | Likely equilibrium structure |

## Appendix D. The Four-Scope Control Plane Matrix

| Scope | Core assets | Rent character | Leading positions (mid-2026) | Key 2026 events |
|---|---|---|---|---|
| Universal — protocols | MCP, A2A, payment protocols | Neutralized; table stakes | Linux Foundation stewardship; Anthropic/Google influence | MCP ~9,600 servers; A2A v1.0 |
| Universal — curation gateway | Registries, ranking, trust manifests, identity/payment rails | High but contested and likely regulator-capped | Google Agent Registry; GitHub agent finder; HF Discover; labs' proto-gateways | ARD spec (June 17); OKF (June 12) |
| Industry | Sector ontologies, regulatory mappings, benchmarks, data cooperatives | Highest quality; horizontal network effects; least priced-in | Bloomberg/Veeva/Epic class; industry lakehouses; Palantir sector templates | OKF as candidate carrier; FDE template accumulation |
| Enterprise | Data authority, governance perimeter, fleet orchestration | Moderate; sticky per instance, replicable across instances | Microsoft, Google, Palantir, Databricks, Snowflake | Agent Bricks/Unity AI Gateway (June 15–18); FDE arms race (~$9B announced, May–July) |
| Departmental | Team workflows, local context, task agents | Thin; execution edge | Vertical apps, startups; labs via harnesses | Shadow-AI absorption contest |

## Appendix E. Glossary

**Agentic mesh** — the composite architecture of agents, tool-ified apps, routers, and converged data interacting over standardized protocols. **Control plane** — the layer owning workflow decomposition, routing, verification, and exception handling. **Harness** — the engineered envelope (verification, recovery, observability, permissioning) that renders probabilistic agents production-reliable. **Integration tax** — aggregate economic cost of N² point-to-point integration. **Machine-native dollar** — fiat-backed stablecoin functioning as programmable settlement money for machine-to-machine commerce. **Tool-ification** — the conversion of applications into headless, agent-callable capability providers. **Metering–settlement–trust stack** — the financial plumbing category comprising usage measurement, payment clearing, and agent identity/compliance. **Scope stack** — the four nested levels (universal, industry, enterprise, departmental) at which control planes are instantiated. **Curation gateway** — an active registry that evaluates, ranks, and warrants capabilities, collecting two-sided gatekeeper rents; contrasted with a passive (DNS-model) registry. **FDE (Forward Deployed Engineering)** — embedded-engineer deployment as go-to-market; three variants distinguished in Section 4.3 (ontology installation, distribution-channel JV, consumption CAC). **Sector semantic authority** — ownership of an industry's de facto shared ontology.

---

# References

1. Anthropic. "Introducing the Model Context Protocol." November 2024. https://www.anthropic.com/news/model-context-protocol
2. Google Developers Blog. "Announcing the Agent2Agent Protocol (A2A): A New Era of Agent Interoperability." April 2025. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
3. Google Cloud. "Announcing the Agent Payments Protocol (AP2)." September 2025. https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol
4. Coinbase. "x402: An Open Protocol for Internet-Native Payments." 2025. https://www.x402.org
5. Chainalysis. "Inside x402: 100M Agentic Payments on Base." June 2026. https://www.chainalysis.com/blog/x402-agentic-payments-adoption/
6. Toloka. "The Future of MCP: 2026 Roadmap, Enterprise Adoption, and What Comes Next." May 2026. https://toloka.ai/blog/the-future-of-mcp-enterprise-adoption/
7. Digital Applied. "AI Agent Protocol Ecosystem Map 2026: MCP, A2A, ACP, UCP." March 2026. https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp
8. Intuz. "MCP vs A2A: AI Agent Protocol Comparison (2026)." April 2026. https://www.intuz.com/blog/mcp-vs-a2a
9. HonestAI. "MCP & A2A Agent Protocols: How Enterprises Are Creating Truly Interoperable AI Systems." April 2026. https://www.honestai.us/blogs/mcp-a2a-agent-protocols-how-enterprises-are-creating-truly-interoperable-ai-systems
10. OneReach. "Guide: Choosing MCP vs A2A Protocols for Multi-Agent Collaboration." April 2026. https://onereach.ai/blog/guide-choosing-mcp-vs-a2a-protocols/
11. ClickHouse Engineering. "Unifying OLTP and OLAP: HTAP Databases, Zero-ETL, and Best-of-Breed Architectures." March 2026. https://clickhouse.com/resources/engineering/unifying-oltp-and-olap
12. Coeo. "Lakebase Explained: Why Databricks Is Blending OLTP, Analytics and AI." February 2026. https://www.coeo.com/2026/02/lakebase-explained-why-databricks-is-blending-oltp-analytics-and-ai-and-what-that-means-for-your-architecture/
13. Qubika. "Bringing OLTP into Your Lakehouse: Why Databricks Lakebase Is a Game Changer." September 2025. https://qubika.com/blog/oltp-lakehouse-databricks-lakebase/
14. Zhang et al. "Towards Generalized Routing: Model and Agent Orchestration for Adaptive and Efficient Inference (MoMA)." arXiv:2509.07571. September 2025. https://arxiv.org/abs/2509.07571
15. "Explainable Model Routing for Agentic Workflows." arXiv:2604.03527. April 2026. https://arxiv.org/abs/2604.03527
16. "Permission Manifests for Web Agents." arXiv:2601.02371. January 2026. https://arxiv.org/abs/2601.02371
17. Stablecoin Insider. "Agentic Payments and Stablecoins: How AI Agents Are Revolutionizing Autonomous Machine-to-Machine Transactions in 2026." May 2026. https://stablecoininsider.org/agentic-payments-and-stablecoins-how-ai-agents-are-revolutionizing-autonomous-machine-to-machine-transactions-in-2026/
18. Stablecoin Insider. "AI Agents for Stablecoins in 2026: Architecture, Use Cases, x402 Payments, and Real-World Data." February 2026. https://stablecoininsider.org/ai-agents-for-stablecoins-in-2026/
19. Nevermined. "40 Stablecoin Payments for AI Agents Statistics." June 2026. https://nevermined.ai/blog/stablecoin-payments-ai-agents-statistics
20. Indoneo. "A $0.20 Payment Just Rewired Asia's Financial Infrastructure: Google AP2, x402, and Stablecoin Payment Rails." July 2026. https://www.indoneo.com/tech-ai/google-ap2-x402-stablecoin-asia-payment-rails/
21. Autheo. "x402 and Gasless Stablecoins in 2026: A Practical Guide to AI-Agent Micropayments, Batch Settlement, and Compliance." May 2026. https://www.autheo.com/blog/x402-gasless-stablecoins-ai-agent-micropayments-batch-settlement-2026/
22. The Elec. "EDB Unveils 'Agentic Lakehouse' Vision to Bring AI Directly to Enterprise Data." June 2026. https://www.thelec.net/news/articleView.html?idxno=11084
23. Databricks. "Lakebase" (product documentation; GA announced February 2026). https://www.databricks.com/product/lakebase
24. Google Cloud Blog. "How the Open Knowledge Format can improve data sharing." June 12, 2026. https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing/
25. GoogleCloudPlatform/knowledge-catalog. OKF SPEC.md (v0.1). GitHub, Apache 2.0. https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
26. Google Developers Blog. "Announcing the Agentic Resource Discovery specification." June 17, 2026. https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/
27. AgenticResourceDiscovery.org. ARD specification and working-group documentation. 2026. https://agenticresourcediscovery.org/
28. Guha, R. V. "Introducing the Agentic Resource Discovery specification." Microsoft Command Line Blog, June 17, 2026. https://commandline.microsoft.com/agentic-resource-discovery-specification-ard/
29. Hugging Face Blog. "Agentic Resource Discovery: Let agents search." June 2026. https://huggingface.co/blog/agentic-resource-discovery-launch
30. Databricks Blog. "Agent Bricks: Data + AI Summit 2026." June 2026. https://www.databricks.com/blog/agent-bricks-dais-2026
31. SpaceXAI. "Grok on Databricks." June 18, 2026. https://x.ai/news/grok-databricks
32. About Amazon. "AWS invests $1 billion to embed AI forward deployed engineers with customers." June 30, 2026. https://www.aboutamazon.com/news/aws/aws-1-billion-forward-deployed-ai-engineers
33. CNBC. "AWS puts $1 billion into new AI unit to embed engineers with customers, joining growing wave." June 30, 2026. https://www.cnbc.com/2026/06/30/aws-amazon-ai-forward-deployed-engineers.html
34. GeekWire. "Microsoft unveils $2.5B 'Frontier Company' to embed AI engineers inside customers." July 2, 2026. https://www.geekwire.com/2026/microsoft-announces-2-5b-frontier-company-to-embed-ai-engineers-inside-customers/
35. Althoff, J. "Microsoft Frontier Company: AI engineering that amplifies and protects your intelligence." The Official Microsoft Blog, July 2, 2026. https://blogs.microsoft.com/blog/2026/07/02/microsoft-frontier-company-ai-engineering-that-amplifies-and-protects-your-intelligence/
36. QuantumBlack, AI by McKinsey. "The state of AI in 2025: Agents, innovation, and transformation." Global survey, November 5, 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
37. ICONIQ Growth. "State of AI: Bi-Annual Snapshot." January 2026 (AI-product gross margin data). https://www.iconiq.com/growth/reports/2026-state-of-ai-bi-annual-snapshot
38. Trending Topics EU / Crunchbase data, as reported in "Q1 2026 Venture Capital Hits $297B: AI Captures 81% of Record Funding." June 2026. Third-party tally; see Data Notes, Part IV. https://tech-insider.org/q1-2026-venture-capital-297-billion-ai-startup-funding-record/
39. Challapally, A., Pease, C., Raskar, R., & Chari, P. "The GenAI Divide: State of AI in Business 2025." MIT Project NANDA, July 2025. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
40. Bachman, M., & Berenberg, A. "Announcing Model Context Protocol (MCP) support for Google services." Google Cloud Blog, December 10, 2025. https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services
41. Google Cloud Blog. "Managed MCP servers for Google Cloud databases." February 2026. https://cloud.google.com/blog/products/databases/managed-mcp-servers-for-google-cloud-databases
42. Google Cloud Blog. "Google-managed MCP servers are available for everyone." April 29, 2026. https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone
43. google/mcp repository (list of Google's official MCP servers). GitHub, Apache 2.0. https://github.com/google/mcp
44. Palantir Technologies. "Connecting Agents to Decisions." Palantir Blog, April 2026. https://blog.palantir.com/connecting-agents-to-decisions-277dee8ddb40
45. The Futurum Group. "1H 2026 Enterprise Software Decision Maker Survey Report" (830 global IT decision-makers). Summary: "41% of Firms Plan App Consolidation; Best-of-Breed Procurement Falls to 20.7%." May 2026. https://futurumgroup.com/press-release/41-of-firms-plan-app-consolidation-best-of-breed-procurement-falls-to-20-7/
46. Microsoft. "What is Fabric IQ?" and related Microsoft IQ documentation (Fabric IQ, Work IQ, Foundry IQ, Fabric Data Agents). Microsoft Learn, 2026. https://learn.microsoft.com/en-us/fabric/iq/overview
47. Databricks. "Databricks Sandbox." Product documentation, last updated July 1, 2026. https://docs.databricks.com/aws/en/compute/serverless/sandbox
48. Mastercard. "Mastercard Launches Agent Pay for Machines to Unlock Super-Fast, Always-On Payments." June 10, 2026. https://www.mastercard.com/my/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html

*Note on sourcing: Statistics cited via secondary sources (including industry survey data and third-party estimates) are identified as such in the text and in the Data Notes. Figures on x402 transaction volumes and mix derive from Chainalysis and Nevermined on-chain analyses as of Q1–Q2 2026 and are subject to revision as those datasets are updated.*
