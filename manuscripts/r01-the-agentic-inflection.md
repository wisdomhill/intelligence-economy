---
title: "1. The Agentic Inflection"
subtitle: "How AI crossed from conversation to labor"
series: "The Intelligence Economy"
number: 1
manuscript-revision: 5
date: 2026-08-24
date-modified: 2026-08-24
author: "Wisdom Hill Research"
publisher: "Wisdom Hill"
license: "CC BY-NC-ND 4.0"

description: >-
  The four-stage phase transition from chatbot to agent, and the three-way
  contest for the agentic value layer. Why user share and value capture have
  decoupled.

keywords:
  - agentic AI
  - task horizon
  - agent harness
  - context lock-in
  - model commoditization

# Where this manuscript is published. The fragments under `dir` are this
# file split by chapter. The `published` titles are shortened for the
# sidebar and the previous/next labels, so they differ from the manuscript
# headings by design; everything else in the two must match exactly.
published:
  dir: reports/r01/
  pdf: r01-the-agentic-inflection.pdf
  url: https://wisdomhill.github.io/intelligence-economy/reports/r01/

chapters:
  - manuscript: "Part I. The Phase Transition: Four Stages of Generative AI (2022–2026)"
    published:  "Part I. The Phase Transition"
    fragment:   _01-phase-transition.qmd
    page:       01-phase-transition.qmd
  - manuscript: "Part II. Anatomy of an Agent: Why the Explosion Happened Now"
    published:  "Part II. Anatomy of an Agent"
    fragment:   _02-anatomy-of-an-agent.qmd
    page:       02-anatomy-of-an-agent.qmd
  - manuscript: "Part III. The Competitive Landscape: Three Value Dimensions and the Commoditization Pincer"
    published:  "Part III. The Competitive Landscape"
    fragment:   _03-competitive-landscape.qmd
    page:       03-competitive-landscape.qmd
  - manuscript: "Part IV. The Three-Way Agentic War: Outlook to 2027"
    published:  "Part IV. The Three-Way Agentic War"
    fragment:   _04-agentic-war.qmd
    page:       04-agentic-war.qmd
  - manuscript: "Part V. Integrated Investment Framework"
    published:  "Part V. Integrated Investment Framework"
    fragment:   _05-investment-framework.qmd
    page:       05-investment-framework.qmd
  - manuscript: "Coda. The Paradox This Report Cannot Resolve"
    published:  "Coda"
    fragment:   _06-coda.qmd
    page:       06-coda.qmd
  - manuscript:
      - "Appendix A. Data Sources, Measurement Caveats, and Cross-Verification Notes"
      - "Appendix B. Glossary"
      - "Appendix C. Timeline of Key Events (Nov 2022 – Jul 2026)"
    published:  "Appendices"
    fragment:   _07-appendices.qmd
    page:       07-appendices.qmd
  - manuscript: "References"
    published:  "References"
    fragment:   _08-references.qmd
    page:       08-references.qmd
---
# The Agentic Inflection

### How AI Crossed from Conversation to Labor

**The Intelligence Economy — Report 1 of 14**

**Wisdom Hill Research | Thematic Research | July 2026**

---

## Executive Summary

Three and a half years after the launch of ChatGPT, the generative AI industry has crossed a phase boundary. The product category that defined 2023–2024 — the chatbot — has been superseded by a fundamentally different economic object: the autonomous agent. The unit of value has shifted from *answers sold* to *tasks completed*, and with it, the reference price for AI has migrated from software subscription fees toward the cost of human labor itself.

This report traces how that transition happened, who is winning it, and where the competitive frontier moves next. Four theses organize the analysis:

**Thesis 1 — Task horizon is the master variable.** The defining difference between the four stages of generative AI (chatbot → copilot → reasoning model → agent) is not intelligence per se but the length of work an AI system can complete autonomously without failure. Autonomous task horizons have been doubling every four to seven months. Because the addressable stock of knowledge work grows with the integral of tasks that fit inside the horizon, capability growth that looks incremental on benchmarks translates into exponential expansion of automatable labor.

**Thesis 2 — The harness, not the model, made agents possible.** Large language models are probabilistic; agents require reliability across hundreds of unsupervised steps. The breakthrough of 2025 was architectural: wrapping probabilistic models in deterministic software harnesses — agent loops, tool execution, context management, sandboxing, skills, and orchestration. Claude Code's record-setting growth (a $1B run-rate within six months of launch, $2.5B+ within nine) demonstrated the commercial power of model–harness co-evolution, and the January 2026 launch of Claude Cowork extended the pattern from coding to general knowledge work — its February professional-plug-in expansion triggering an estimated $285B single-day sell-off across software, financial-services, and asset-management equities, the first time public markets priced agentic substitution as a present-tense risk.

**Thesis 3 — Leadership has rotated twice, because the game itself changed twice — leaving three value dimensions with three different leaders.** OpenAI created the category and still holds the largest consumer base (1B monthly active users, reached faster than any mobile app in history), but its share of AI-assistant users fell below 50% in March 2026 for the first time since launch, reaching 46.4% by May — the end of a majority it had held since November 2022. Google's Gemini seized momentum from late 2025 on multimodal capability multiplied by zero-marginal-cost distribution. In 2026, Anthropic captured the agentic value layer with roughly 8% of consumer web traffic (about 10% of users) — yet it wins roughly 70% of head-to-head matchups against OpenAI among first-time business AI buyers, and in May 2026 passed OpenAI in overall U.S. business adoption (Ramp AI Index). User share and value capture have decoupled — the single most important fact for investors evaluating this market.

**Thesis 4 — The three-way agentic war commoditizes everything except accumulated context.** OpenAI's GPT-5.6 family and Anthropic's Fable 5 now trade benchmark leadership depending on which test is consulted; Google's Antigravity 2.0 and Gemini 3.5 Flash attack on price-performance while its quality-tier successor remains unshipped. Managed-agent APIs are commoditizing the harness layer itself. Convergence is therefore *asymmetric and axis-dependent*: well established between the two labs contesting the agentic frontier, provisional as to the third, which leads decisively in generative media while its coding gap has widened. As model quality and harness engineering converge, the durable moat migrates to *context lock-in*: the organizational knowledge, skills, memory, and workflow integration an agent accumulates over months of deployment — the one asset that today transfers only incompletely when a customer switches providers. Two caveats sit on the horizon: capability is descending the price curve faster than context accumulates, and the U.S. government has begun intervening directly in the availability of frontier models.

A second front — multimodal perception, video generation, world models, and the wearable hardware through which AI acquires physical-life context — is opening beyond the desktop. It is deliberately excluded from this report and treated in full in Report 10 (*The Functional Anatomy of Consumer AI Demand*).

Within the series architecture set out in the Prologue, this report documents the **supply side** of the intelligence economy's formation: what agents can now do, why the capability arrived when it did, and who is capturing the value. Parts I and II establish *what changed* — the phase boundary from conversation to labor, and the harness architecture that made the crossing possible. Parts III and IV establish *who is fighting over it*, and Part V converts both into an investment framework. The report closes with the demand-side puzzle it cannot resolve — the gap between exploding output and stagnant measured productivity — which is the subject of Report 2.

---

# Part I. The Phase Transition: Four Stages of Generative AI (2022–2026)

The development of generative AI since November 2022 is best understood not as a sequence of smarter models but as a sequence of *longer-lived* ones. Each stage is distinguished by the time horizon of work the system can complete autonomously, and by where the human sits in the loop.

## 1.1 Stage One — Chatbots: The Courier Problem (2022–2023)

The original ChatGPT paradigm was single-turn question answering. A human composed a prompt, the model returned text, and the human carried the result back into their actual working environment — pasting code into an editor, copying prose into a document. The model was a pure probabilistic text generator with a task horizon of seconds to minutes, and the human served as a *courier* between the AI and the real work, paying a friction tax on every interaction.

The economic consequence was structural: because the unit of value was a single answer, pricing anchored to software subscriptions ($20/month), and the product captured only a sliver of the productivity it enabled.

## 1.2 Stage Two — Copilots and RAG: Assistance Without Agency (2023–2024)

The second stage connected models to external knowledge (retrieval-augmented generation) and embedded them inside human workflows — most successfully GitHub Copilot inside the IDE (Integrated Development Environment, the editor a programmer works in). The model gained access to context (the codebase, the document corpus) but not initiative: it proposed, the human accepted. The paradigm remained an extension of autocomplete. Value capture improved but remained bounded by the human review bottleneck — every output still passed through a person, so throughput scaled with human attention, not compute.

## 1.3 Stage Three — Reasoning Models: The Prerequisite for Autonomy (2024–2025)

The third stage — inference-time reasoning, exemplified by OpenAI's o-series and Anthropic's extended thinking — mattered less for benchmark scores than for what it made possible. Reinforcement learning began rewarding models for *completing tasks* rather than imitating reference text. Models learned to plan multi-step work, detect their own errors mid-stream, and self-correct. These are precisely the capabilities an autonomous agent requires; reasoning was the load-bearing prerequisite for everything that followed.

## 1.4 Stage Four — Agentic AI: The Value Unit Shifts (2025–present)

In the fourth stage, the model operates a loop: plan, call tools, read and write files, execute code, observe results, retry on failure — for hours, without supervision. The unit of value becomes the *completed task*, and this changes the business model categorically. An answer is priced against a software subscription; a completed task is priced against the wage of the worker who would otherwise have done it. The gap between those two reference prices — roughly two orders of magnitude — is the economic engine of the agentic explosion.

## 1.5 The Master Variable: Task Horizon

The transition is quantifiable. Research by METR (Model Evaluation & Threat Research, a nonprofit AI evaluation lab) on autonomous task completion shows the length of tasks AI agents can reliably finish doubling every four to seven months, with the doubling period accelerating toward roughly four months through 2024–2025. The implication is non-linear: automating a 30-second task is a convenience; automating a four-hour task is labor substitution. As the horizon extends, the total addressable market does not grow with capability — it grows with the *integral* of work that fits inside the horizon, which is why revenue curves in this industry have repeatedly outrun even their owners' forecasts.

---

# Part II. Anatomy of an Agent: Why the Explosion Happened Now

## 2.1 The Architecture Shift: Probabilistic Models + Deterministic Harnesses

### 2.1.1 The Error-Compounding Problem

Large language models (LLMs) are inherently probabilistic. The same input can yield different outputs; hallucination is endemic; errors accumulate over long sequences. In the chatbot era this was a tolerable defect, because a human inspected every output. An agent enjoys no such safety net. Simple arithmetic exposes the problem: a system that succeeds 99% of the time per step completes a 100-step task only 37% of the time. **A probabilistic model alone cannot be an agent.** Early autonomous-agent experiments (the AutoGPT wave of 2023) failed on exactly this point — the models were weak, but more fatally, nothing deterministic surrounded them.

### 2.1.2 Six Components of the Harness

The solution is the *harness*: a deterministic software layer wrapped around the probabilistic model. Its six core components:

1. **The agent loop.** Plan → act → observe → re-plan is deterministic code; the model supplies only the judgment inside each step.
2. **Tools and execution environments.** File I/O, shell execution, search, browsers. Critically, code execution converts probabilistic output into deterministically *verifiable* output — a program compiles or it does not; a test passes or it fails.
3. **Context management.** Context windows are finite. Compaction, sub-agent delegation, and external memory files determine how long a task an agent can sustain; memory architecture, more than model size, sets the practical task horizon.
4. **Permissions and sandboxing.** File-system scoping, network egress controls, and human-approval gates. These are not compliance afterthoughts; they are the precondition of enterprise adoption.
5. **Skills and procedural knowledge.** Verified procedures packaged as documents and code, so the model does not re-derive workflows from scratch — and the channel through which an organization's tacit knowledge is installed into its agents.
6. **Orchestration.** Multi-agent decomposition, parallelization, and rollback on failure.

The division of labor is clean: **the model supplies judgment; the harness supplies reliability.** As model quality converges among the vendors currently shipping at the agentic frontier, competitive differentiation migrates toward the harness — a thesis this report's competitive sections repeatedly confirm. The full architecture of this layer, and why the control plane rather than the model is becoming the economic center of gravity of agentic software, is the subject of Report 5 (*The Agentic Mesh*).

### 2.1.3 Code as the First Killer App: Verifiability as the Hidden Variable

It is not an accident that coding became the first commercial breakthrough for agents. Software is the rare knowledge-work domain with *built-in verification*: compilers, type checkers, and test suites give the agent (and its RL training process) an objective success signal at every step. Domains acquire agentic automation roughly in order of their verifiability — coding first, then data analysis and finance, then law and general office work — a sequencing that has held throughout 2025–2026 and is a useful predictor of where agents land next.

## 2.2 The Interface as Agency: Web → IDE → CLI → Desktop

The evolution of AI interfaces looks like a user-interface story but is really a story about *how much of the world the AI is allowed to touch*.

- **Web chat** isolated the AI in a conversation pane; the human couriered context in and results out.
- **IDE integration** gave the AI access to the codebase but kept it subordinate to the human's visual workspace.
- **The CLI** (Command-Line Interface, the text-based terminal) was the paradoxical leap. The terminal appears primitive, but it is the universal interface to everything a computer can do — file systems, processes, version control, networks. Choosing the CLI meant giving the agent *the computer itself* rather than a human-shaped window onto it. Claude Code's success is a direct consequence of this agent-native design decision.
- **The desktop app** generalizes CLI-grade agency to non-developers. Claude Cowork — launched in research preview in January 2026, with professional plug-ins following in February — brings the same autonomous, file-system-level execution into a consumer desktop application: point it at a folder, and it reads, edits, creates, and organizes multi-step deliverables without terminal literacy.

The endpoint of interface evolution is not a better chat box. It is an AI that shares the human's working environment — files, applications, browsers — as a colleague would.

## 2.3 Case Study — Claude Code and Cowork: The Proof of Concept at Scale

### 2.3.1 Growth Data

Claude Code, publicly launched in mid-2025, became by several measures the fastest-scaling commercial software product on record: a $1 billion annualized run-rate within six months of launch, surpassing $2.5 billion by February 2026 — a 2.5x jump in roughly three months. Anthropic's company-wide annualized revenue rose from $87 million in January 2024 to roughly $30 billion by April 2026, a pace CEO Dario Amodei described as 80x annualized growth in Q1 2026, eight times the company's own plan. Usage statistics corroborate the revenue: by mid-2026 Claude Code was writing approximately 4% of all public GitHub commits, with the average developer-user spending around 20 hours per week in the tool, and enterprise subscriptions quadrupling in early 2026.

### 2.3.2 The Model–Harness Co-Evolution Flywheel

The durable insight from the case is not the growth rate but its mechanism. Anthropic trains its models *inside its own harness*; the model becomes optimized for that harness's tools, and the harness is iterated against the model's observed failure modes. This co-evolution flywheel explains why third parties consuming the same model via API have struggled to reproduce the product's performance — and why "harness engineering" displaced "model capability" as the operative competitive variable in 2025–2026.

### 2.3.3 February 3, 2026: The First Market Repricing Event

Cowork's expansion update — including eleven professional plug-ins spanning legal, finance, sales, and data work — was followed within the same trading session by an estimated $285 billion decline in the market capitalization of global software, financial-services, and asset-management equities — the selling opening in legal- and data-services names before spreading outward, with the Goldman Sachs basket of U.S. software stocks closing down 6%, its steepest one-day fall since April 2025. Whatever one thinks of the magnitude, the event marked the first time public markets treated agentic substitution of SaaS and professional services as a present-tense, repricing-grade risk rather than a distant narrative.

## 2.4 Four Curves That Crossed in 2025

The explosive growth was overdetermined: four independent curves crossed within roughly the same twelve months.

1. **Capability threshold.** RL-trained reasoning pushed task horizons from minutes to hours — across the line where automation becomes labor substitution rather than convenience.
2. **Harness maturity.** The deterministic layer caught up to the model, converting capability into reliability.
3. **Agent-native interfaces.** CLI and desktop form factors, plus the MCP standard for tool connectivity, gave agents access to real working context.
4. **Labor-referenced pricing.** Once the value unit became the completed task, willingness-to-pay re-anchored from software budgets to wage bills. Roughly 80% of Anthropic's revenue now comes from enterprise and API customers, whose API usage skews ~77% toward automation — direct evidence of the pricing migration.

Remove any one of the four and the explosion likely does not happen. This is also why the 2023 agent experiments failed and the 2025 products succeeded: the difference was never a single breakthrough, but a conjunction.

---

# Part III. The Competitive Landscape: Three Value Dimensions and the Commoditization Pincer

The market has not seen one hegemon dethroned by another; it has fractured into three distinct value dimensions — consumer scale, ecosystem distribution, and agentic value capture — each with a different leader. Leadership "rotated" because the game itself changed twice.

## 3.1 Act One — OpenAI: Category Creation, Consumer Scale, and Erosion

OpenAI created the industry and remains its consumer giant: in May 2026 ChatGPT became the fastest mobile application ever to reach one billion monthly active users, on a $25 billion annualized revenue run-rate. But the share trajectory turned decisively, and in March 2026 it crossed the threshold that had defined the category since its creation. On Sensor Tower's *True Audience* metric — unique users across mobile app, mobile web, and desktop web — ChatGPT's share of AI assistants fell below 50% for the first time in March, settling at 46.4% by the end of May, against Gemini's 27.7% and Claude's 10.3%. The decline is a trend, not an event: the same series records 65.3% in December 2024 and 52.8% in December 2025. Claude was the standout challenger, its True Audience up roughly 452% year-over-year in May and its U.S. share rising from 4.4% to nearly 14%. Web-traffic methodologies show the same slope from a higher base: Similarweb has ChatGPT falling from 87.2% to 68% in the twelve months to January 2026.

Two features of the decline matter more than the milestone. First, the slope is steady rather than event-driven: the crossing is the tail of a slide underway since at least December 2024, not a shock. Second, ChatGPT's absolute usage never stopped growing — the market expanded faster than OpenAI captured it. Nor has the category fragmented: three assistants still account for nearly 90% of time spent in AI assistant apps. What ended in March 2026 was not concentration but *singularity* — the era in which one product was a serviceable proxy for the category.

## 3.2 Act Two — Gemini's Counterattack: Multimodal Edge × Free Distribution

From the Gemini 3 generation (November 2025) onward, Google converted a genuine model advantage in multimodality into share gains at a speed only distribution can explain: Gemini web visits grew roughly 644% year-over-year on Similarweb's February 2026 reading, to an estimated 1.1–1.35 billion monthly; the Gemini app reached 950 million monthly active users as disclosed in Alphabet's Q2 2026 results, with daily actives tripling year-over-year; and — separately, and not additively — Gemini-powered AI Overviews reach more than 2 billion users per month inside Google Search. Deep integration across Android, Chrome, Search, and Workspace created discovery paths competitors cannot replicate. The strategic point: Gemini's moat is *zero-marginal-cost distribution*, which persists even if its model edge does not.

## 3.3 Act Three — Anthropic: Winning the Value Layer from a Consumer Minority

The 2026 chapter belongs to Anthropic, and it exposes the decoupling at the heart of this market. Claude holds roughly 8–10% of the consumer market globally (8.2% of web visits; 10.3% of True Audience users), rising to nearly 14% in the United States, yet on Ramp's transaction data across 50,000+ U.S. businesses it wins roughly 70% of head-to-head matchups against OpenAI among firms buying AI services for the first time — and in May 2026, on the same data, it passed OpenAI in overall business adoption for the first time (34.4% vs. 32.3%). The consumer figure has more than tripled in a year without disturbing the underlying asymmetry: a minority of consumer attention coexists with a leading position among paying businesses. Survey evidence points the same direction, with a caveat of instrument. Menlo Ventures' year-end surveys estimate Anthropic's share of enterprise LLM *spend* at 12% (2023), 24% (2024), and 40% (2025), against OpenAI's fall from 50% to 27%; Menlo's separate mid-2025 reading — which measures production *usage*, not spend — put Anthropic at 32% versus OpenAI's 25%. Usage and spend are different denominators and cannot be chained into one series, but both instruments rank Anthropic first. The mechanism is visible one level down: the year-end survey gives Anthropic 54% of enterprise *coding* spend against OpenAI's 21%; the mid-year usage-based reading had put the same figure at 42% — a different instrument again, but pointing the same direction. The highest-value workload pulled the aggregate. Claude Code's $2.5B+ run-rate and Cowork's expansion translated a small traffic footprint into the largest position in the highest-value segment. **Consumer user share and enterprise value capture have decoupled** — the chatbot era's headline metric, monthly active users (MAU), measures the wrong game.

The resulting structure is a genuinely three-strategy market: consumer scale (OpenAI), ecosystem distribution (Google), enterprise agentic precision (Anthropic).

## 3.4 The Challengers: xAI and Meta

**xAI** is the fastest-rising consumer challenger — U.S. daily mobile share up from 1.6% to 15.2% in a year (a daily-mobile basis not comparable with the True Audience shares cited above) on the strength of X-platform integration and aggressive compute build-out, though on cross-platform audience measures it remains below 5% globally — but its presence in the enterprise/agentic value chain remains limited.

**Meta** is strategically squeezed. Its open-source standard-bearer strategy lost its crown when Alibaba's Qwen family overtook Llama in cumulative Hugging Face downloads; reports that Meta is considering a shift toward closed models signal the strategy's exhaustion. Meta's remaining strength — a 3-billion-user social graph and the leading AI-wearables franchise (examined in Report 10) — points it toward consumer ambient AI rather than the frontier-lab race per se.

## 3.5 China's Ascent: From Distillation to Indigenous Innovation

### 3.5.1 The Capability Gap

Chinese labs (DeepSeek, Alibaba/Qwen, Moonshot/Kimi, Zhipu/GLM) initially closed the gap through distillation and fast-following, running roughly four to six months behind the Western frontier. By 2026 the picture is more nuanced: the absolute frontier remains held by closed Western models (a ~36-point gap to the best Chinese entrant as of Q2 2026 on LMArena's Elo scale, which ranks models by head-to-head human preference), but Chinese open-weight models have crossed the "frontier threshold" on many axes — and the catch-up mechanism has evolved beyond imitation. DeepSeek's sparse-attention architecture, Kimi's agent-swarm orchestration (coordinating up to 100 parallel sub-agents), and Zhipu's training of a frontier-class model entirely on Huawei Ascend silicon are indigenous innovations, not derivatives. Chinese-developed models now account for roughly 30% of global open-model downloads.

### 3.5.2 The Order-of-Magnitude Price Wedge and Cascade Routing

The competitive shock is price. Chinese frontier-class models are consistently priced an order of magnitude or more below Western equivalents — roughly 9–36x on input tokens, depending on which models are compared. DeepSeek V3.2 runs at ~$0.28 per million input tokens against ~$2.50 for a mid-tier Western model (about 9x) and ~$10 for a frontier one (about 36x). The practical consequence is the rise of *cascade routing*: production systems route bulk, low-stakes workloads to cheap open-weight models and reserve Western frontier models for the hardest steps, with illustrative cascade calculations suggesting cost reductions of up to roughly 90% for mixed workloads. Model-agnostic architecture has become the default enterprise posture — a structural ceiling on every Western lab's pricing power for undifferentiated workloads.

## 3.6 The Commoditizers: NVIDIA Nemotron and Google Gemma

Two players with no need to monetize models directly are accelerating the price collapse from a different direction. NVIDIA's Nemotron 3 family (Nano/Super/Ultra, with open weights, training data, and RL environments) is a classic *commoditize-the-complement* strategy: cheaper, more abundant models mean more inference demand for NVIDIA hardware, and Nemotron's differentiation is explicitly inference efficiency on NVIDIA silicon rather than peak capability. Google's Gemma 4 plays the same role at the edge — small, fast, omni-capable open models that defend the on-device tier and deny low-end share to Chinese open weights. Together with Chinese labs, these players form a pincer that is commoditizing the entire mid-tier of model capability.

## 3.7 Emerging Market Structure: The Barbell

The synthesis is a barbell. At the bottom, commoditized intelligence: open weights, cascade routing, prices trending toward inference cost. At the top, premium agentic systems where the purchase criterion is trust, reliability, and accumulated context rather than token price — and where willingness-to-pay references labor, not software. Value drains from the middle. The capability half-life problem makes this structural: a frontier capability built for billions of dollars is replicated in open weights within months, so *excess returns on raw model capability now decay faster than the investment cycle that produces them*. Durable returns accrue to whatever does not replicate: model–harness co-evolution flywheels (the process of Section 2.3.2 — not the harness artifact itself, which Section 4.2.3 shows commoditizing), distribution, enterprise trust — and, increasingly, accumulated customer context (Part IV).

---

# Part IV. The Three-Way Agentic War: Outlook to 2027

## 4.1 The Front Line Today: Benchmark Parity

The performance gap that defined 2025 has closed.

**OpenAI / GPT-5.6.** By mid-2026 the frontier comparison had moved a generation. Anthropic restored Fable 5 to general availability on July 1 — its Mythos-tier sibling remains limited to approved partners — and OpenAI shipped the GPT-5.6 family on July 9. Neither leads outright. OpenAI takes the aggregate agentic-coding and terminal benchmarks; Anthropic holds a wide margin on SWE-bench Pro, the contamination-resistant variant, where the gap runs to roughly fifteen points; on broad-intelligence measures the two sit within a point of each other. Pricing runs the other way, with OpenAI's flagship undercutting Anthropic's materially and its mid-tier undercutting that again. The direction matters more than the decimals: capability differences that were decisive a year ago are now benchmark-specific and, in several cases, inside the noise band — while price dispersion widens. Quality-vs-cost has replaced better-vs-worse, and many practitioners report running both.

Two disclosures from the same week caution against reading any of it too precisely. OpenAI published an audit finding roughly 30% of SWE-bench Pro tasks defective and retracted its own recommendation of the benchmark — the one measure on which Anthropic leads decisively. Separately, the independent evaluator METR reported that OpenAI's flagship exploited its agentic evaluation at the highest rate that organization has recorded. Each finding cuts toward its publisher's interest; neither is settled. Together they establish something more durable than any score: **the harness moves the result as much as the model, and the benchmark now moves it as much as either** — the strongest available evidence for Thesis 2, a warning that vendor-reported benchmarks are not comparable across labs, and the reason §4.2.1 treats cost per completed task rather than leaderboard position as the operative purchasing metric.

**Google / Antigravity 2.0 + Gemini 3.5 Flash.** At I/O 2026 Google launched Gemini 3.5 Flash — an agent- and coding-optimized model that outperforms Google's own previous frontier model (3.1 Pro) on nearly all benchmarks while running roughly four times faster, sustaining multi-hour autonomous runs — alongside Antigravity 2.0, a ground-up rebuild bundling a desktop IDE, a Go-based command-line tool, and an agent SDK (Software Development Kit), priced on compute rather than per-prompt limits. Most consequentially, Google introduced Managed Agents in the Gemini API: a single API call now provisions a complete agent — reasoning, tool use, code execution, persistent state — inside an isolated container. Gemini 3.5 Pro, the quality-tier model designed to pair with Flash, was announced for June at I/O and had not shipped as of late July, with no revised date published; reporting attributes the delay to coding capability, and Google's current top Pro model dates to February. The asymmetry this creates is the more useful observation. In agentic coding — the beachhead this report identifies — Google's distance from the frontier has widened rather than closed over the quarter. In generative media it has not: Google's image and video families remain the reference standard for quality and for cost per generated asset, and the integration of image generation into the video pipeline is a workflow advantage no competitor currently matches. Google is therefore not converging toward the frontier uniformly; it is diverging on the axis this report measures and leading on an axis Report 10 measures — where demand is denominated in GPU-hours rather than tokens, and where the physical-infrastructure consequences are, if anything, larger.

**Anthropic / Sonnet 5.** On June 30 — a fortnight before the current frontier tier arrived on either side — Anthropic released Claude Sonnet 5, which reaches 63.2% on SWE-bench Pro against the then-flagship Opus 4.8's 69.2% at roughly half the price. Near-frontier agentic capability priced into the mid-tier, executed against its own premium line: the clearest evidence to date that the commoditization Thesis 4 anticipates is already underway. Both rivals have since mirrored the move, OpenAI shipping three tiers at once.

The strategic reading: the harness thesis of 2025 is now the explicit strategy of all three players. When a differentiator is universally adopted, it becomes table stakes — which forces the question of where the moat moves next. One variable now sits outside the competitive frame: government intervention in frontier-model availability became a live constraint in June 2026, with both Anthropic and OpenAI seeing top-tier releases restricted on cyber-capability grounds.

## 4.2 Six Structural Shifts

**4.2.1 KPI replacement: from benchmark scores to cost per completed task.** With SWE-bench differences inside the noise band, purchasing decisions shift to total cost of task completion — model price × token efficiency × retry rates. Gemini 3.5 Flash's positioning (near-frontier quality at Flash economics) targets exactly this metric, as does OpenAI's mid-tier, which reaches near-parity on terminal work at roughly half its own flagship price; compute-based and task-based pricing experiments are displacing seat- and token-based billing.

**4.2.2 The margin war.** The three players' pricing strategies are diverging head-on: Anthropic has fenced usage (restricting third-party agent access on consumer plans) to defend premium economics; OpenAI has loosened Codex limits to win volume; Google has entered with a $100 Ultra tier carrying 5x capacity. Premium pricing survives only while the quality gap justifies it; with published comparisons suggesting Opus-class models can consume 3–4x the tokens per task, the price-elastic majority of workloads is structurally exposed to the volume players. Expect successive rounds of subscription and capacity price cuts through 2026–2027, and structural margin compression in the model layer — offset, at the industry level, by Jevons-style volume growth that benefits inference infrastructure.

**4.2.3 Harness commoditization and the migration of the moat to context lock-in.** Managed-agent APIs turn the harness itself into a purchasable commodity, shortening the half-life of harness engineering just as open weights shortened the half-life of model capability. The durable asset that remains is **accumulated context**: an agent's learned knowledge of a customer's codebase conventions, procedures (skills), work history, and preferences compounds over months and *does not transfer* between vendors. Context lock-in is to the agent era what data lock-in was to the SaaS era; the maturity of each vendor's context-accumulation machinery (memory architecture, skills ecosystem, enterprise knowledge integration) is the leading indicator of future share defensibility. The data architecture through which context accumulates — memory systems, semantic layers, and enterprise knowledge integration — is examined in depth in Report 6 (*The Data Layer Reforged*).

**4.2.4 Vertical expansion: from developers to all knowledge work.** Coding was merely the most verifiable beachhead. All three players are porting their harnesses upward: Anthropic via Cowork's professional plug-ins; Google citing banks and fintechs automating multi-week workflows on 3.5 Flash; OpenAI folding Codex into ChatGPT. The terminal prize is not the developer-tools market but the knowledge-work market measured in trillions — and three-way competition *accelerates* SaaS displacement, because price competition pulls forward the economic crossover point at which agents undercut incumbent software-plus-labor bundles. Reports 4 (*The SaaS Apocalypse Question*) and 8 (*The Functional Anatomy of Enterprise AI Demand*) quantify this displacement thesis market by market and function by function.

**4.2.5 The wrapper squeeze.** As all three vendors ship full stacks — IDE, CLI, desktop, SDK, managed API — the strategic space for intermediaries that resell model access behind a UX (AI-native IDEs, agent wrappers) compresses sharply. Surviving paths: vertical specialization, pivoting to the multi-model routing/governance layer that cascade economics demands, or acquisition. Expect concentrated consolidation in this layer through 2027.

**4.2.6 Multi-homing as default.** With near-symmetric support for MCP, plug-ins, and skills across vendors, switching friction is low and most professional users already run multiple agents. Two consequences: market share becomes volatile on the model-release cycle, and — precisely because everything else is portable — the strategic weight of non-transferable accumulated context (4.2.3) rises further.

## 4.3 2027 Base-Case Scenario

The probability-weighted base case: the model and harness layers commoditize rapidly inside a three-firm oligopoly (benchmark convergence, successive price cuts, compressed margins), while value capture polarizes — downward to compute infrastructure riding token-volume growth, upward to whoever converts deployments into accumulated context and enterprise trust. OpenAI fights a volume war on consumer scale and Codex economics; Google fights a war of attrition on full-stack vertical integration (its in-house Tensor Processing Units → model → harness → Workspace distribution) and price; Anthropic defends the quality-and-trust high ground. Google's balance sheet, distribution, and generative-media lead still make it structurally well-equipped for a long attrition war, but the attrition thesis now carries an execution condition it did not carry in May: Gemini 3.5 Pro missed its announced window and remains unshipped, with coding capability the reported obstacle. Should it arrive at frontier quality near Flash economics, the premium strategy's defensible perimeter shrinks to verified reliability plus accumulated enterprise context. Should the delay extend, the more consequential reading is that frontier agentic quality is *not* a commodity reliably reproducible by any well-capitalized lab — which would strengthen Thesis 3 at the expense of the pure-commoditization case. Anthropic's own Sonnet 5 (June 30) is an early instance of this compression executed pre-emptively against itself — a defensive cannibalization that concedes the price axis to protect the volume. Key risks: for Anthropic, premium compression; for OpenAI, enterprise share loss compounding consumer share erosion; for Google, the persistent gap between platform breadth and agentic product focus.

---

# Part V. Integrated Investment Framework

## 5.1 The Value Migration Map

Across the landscape surveyed in this report, value is migrating in a consistent pattern:

| Layer | Direction | Mechanism |
|---|---|---|
| Raw model capability | **Compressing** | Open weights, distillation, and Chinese price competition cut the half-life of capability advantages to months |
| Harness / agent infrastructure | **Compressing (newly)** | Managed-agent APIs commoditize what was 2025's differentiator |
| Mid-tier model APIs | **Compressing** | Cascade routing caps pricing for undifferentiated workloads |
| Accumulated customer context | **Accumulating** | Memory, skills, and workflow integration compound and do not transfer between vendors |
| Enterprise trust & governance | **Accumulating** | Agents touching corporate data are bought on reliability and accountability, not token price |
| Distribution (OS, search, social) | **Accumulating** | Zero-marginal-cost reach persists independent of model cycles |
| Inference compute | **Accumulating** | Price cuts drive volume (Jevons); multimodal generation will add a second, more compute-intensive demand wave (Reports 10–11) |
| Incumbent SaaS / professional services | **At risk** | Three-way agent price competition pulls forward the substitution crossover; February 3, 2026 was the first repricing event, not the last |

The summary heuristic for the 2026–2027 window: **sell the middle of the barbell, own the ends, and track context lock-in as the new switching cost.**

## 5.2 Bear Cases and Falsification Conditions

Intellectual honesty requires stating what would invalidate each thesis:

- **Against Thesis 1 (task horizon):** if METR-style doubling stalls — e.g., horizons plateau at hours rather than days through 2027 — the addressable-labor expansion thesis weakens materially, and agent revenue growth should decelerate toward conventional SaaS rates.
- **Against Thesis 2 (harness moat → context moat):** if managed-agent APIs plus open standards (MCP and successors) make accumulated context portable across vendors, no durable software-layer moat exists and the industry converges on pure price competition above commodity compute.
- **Against Thesis 3/4 (Anthropic's value-layer lead):** sustained decline in enterprise win rates, or a Gemini 3.5 Pro that delivers frontier-class quality at Flash-class economics, would compress the premium segment faster than context lock-in can mature.
- **Against Thesis 4 (rapid commoditization):** a Gemini 3.5 Pro delay extending materially beyond Q3 2026, or a shipped model that fails to reach agentic parity, would indicate that frontier capability is not replicable by capital and distribution alone — weakening the three-firm-oligopoly-with-commoditized-models premise on which §4.3 rests.
- **Systemic bear case:** agent reliability incidents at enterprise scale (data loss, security breaches via agent permissions) could trigger a regulatory or procurement freeze that resets the adoption curve irrespective of capability.

## 5.3 Consolidated Monitoring Indicators (Quarterly Checklist)

1. Autonomous task-horizon measurements (METR and successors)
2. Convergence speed on remaining high-difficulty benchmarks (SWE-bench Pro and successors)
3. Effective cost per completed task, by vendor (token efficiency × price)
4. Enterprise head-to-head win rates among first-time business AI buyers (currently ~70% Anthropic on Ramp data) and enterprise LLM share
5. Managed-agent API adoption; share of revenue on task/compute-based billing
6. Agent-driven SaaS displacement events (earnings commentary, equity repricings)
7. Western frontier vs. best Chinese open-weight gap (Elo and price), and the share of enterprise workloads on cascade routing
8. Regulatory availability of frontier models: export-control actions, gated previews, and the lag between a model's release and its general availability

*Indicators specific to the multimodal and physical-context front — video-model economics, world-model simulation consistency time, wearable shipments, and robotics commercialization — are maintained in Report 10.*

---

# Coda. The Paradox This Report Cannot Resolve

Everything documented above is a supply-side revolution. Task horizons are doubling every four to seven months; the fastest revenue ramps in the history of commercial software are underway; willingness-to-pay has re-anchored from software budgets to wage bills; public markets have begun repricing the displaced. If capability and monetization were the whole story, the intelligence economy would already be a settled fact.

They are not the whole story. Aggregate productivity statistics show no inflection remotely commensurate with the revenue curves. Outside software engineering — the one domain with built-in verification (Section 2.1.3) — rigorous evidence that agentic systems deliver realized economic utility beyond what chatbot-era tools delivered remains strikingly thin. Two readings are possible, and they lead to opposite conclusions. The first is measurement lag: general-purpose technologies have historically produced a productivity J-curve, with decades separating electrification from its statistical dividend, because output gains require complementary reorganization of the firms that deploy them. The second is that adoption is running ahead of value — that enterprises are buying expenditure, not outcomes, and the revenue curves of 2026 are the signature of a capital cycle rather than a productivity revolution.

Which reading is correct determines whether every growth number in this report is a leading indicator or a warning. This report has established what agents can do and who profits from selling them; it has not established what they are, so far, economically *worth* to those who buy them. That question — the AI productivity paradox — is the subject of Report 2.

---

# Appendix A. Data Sources, Measurement Caveats, and Cross-Verification Notes

Readers should weigh the following limitations, which apply throughout:

1. **Run-rate vs. GAAP.** Most cited revenue figures (Anthropic $14B→$19B→$30B→$47B across Feb–May 2026; OpenAI $25B) are annualized run-rate snapshots, not audited full-year revenue, and differ across outlets by reporting date. Where aggregators conflicted, this report preferred figures attributed to primary disclosures (company announcements, Reuters).
2. **Market-share methodology divergence.** For roughly the same period, ChatGPT's share reads ~68% on Similarweb web-traffic methodology, ~55% on First Page Sage web-traffic, and 46.4% on Sensor Tower's True Audience basis (unique users across mobile app, mobile web, and desktop web). Claude reads 8.2% on the first and 10.3% on the last. These are not conflicting facts but different denominators; shares should always be read with their measurement basis attached, and never compared across providers.
3. **Secondary-source reliability.** Several Chinese-model benchmark claims circulate through promotional secondary sources; individual claims (e.g., a specific model beating a Western flagship on a single benchmark) should be verified against primary leaderboards (SWE-bench, LMArena, Artificial Analysis) before institutional use.
4. **Event attribution.** The February 3, 2026 equity sell-off (~$285B) is Bloomberg's estimate of same-day declines in market value across software, financial-services, and asset-management equities; the sector attribution is Bloomberg's, and secondary outlets variously assign the same aggregate to a two- or four-day window. Attribution to a single product announcement is directionally supported by contemporaneous coverage but inherently approximate.
5. **Benchmark harness dependence.** Coding-benchmark scores are not comparable across vendors unless the scaffolding is held constant. Vendor-run SWE-bench Pro scores routinely exceed standardized-harness scores for the same model by 10–30 points, and Terminal-Bench rankings invert depending on whose CLI is used. All benchmark comparisons in Section 4.1 are drawn from vendor system cards; cross-vendor gaps should accordingly be read as directional evidence carrying wide uncertainty on their magnitudes — the qualified reading Section 4.1 itself applies in flagging harness dependence — rather than as precise rank orderings.
6. **Volatility in model availability.** The frontier model roster changed five times between May 28 and July 9, 2026 (Opus 4.8; Fable 5/Mythos 5 GA; their export-control suspension; Sonnet 5 and the Fable 5 restoration; the GPT-5.6 family). Any capability or market-position ranking in this report is a snapshot at July 22, 2026 — the date of the most recent disclosure incorporated — and has a short half-life. The benchmarks themselves proved unstable over the same window: the coding evaluation on which the largest vendor gap rests was audited and withdrawn from recommendation by one of the labs it ranks.
7. **Survey-series comparability.** The Menlo Ventures figures cited in Section 3 come from two editions with different sample sizes (150+ technical leaders mid-2025; ~500 enterprise decision-makers year-end 2025) and, more importantly, different instruments: the mid-year edition measures production *usage* share, the year-end edition estimates *spend* share. Neither is measured revenue, and the text keeps the two instruments separate rather than chaining them into one series. The Ramp figures in Section 3.3 are a third instrument again — transaction data on corporate cards, covering Ramp's customer base rather than the full market. All readings predate this report by two to twelve months.

# Appendix B. Glossary

- **Agent / Agentic AI:** an AI system that autonomously plans, calls tools, executes, observes results, and retries across multi-step tasks without per-step human review.
- **Harness:** the deterministic software layer (loop, tools, context management, permissions, skills, orchestration) wrapped around a probabilistic model to make agents reliable.
- **Task horizon:** the length of work an agent can complete autonomously at a given reliability threshold; the master capability variable of the agent era.
- **Context lock-in:** switching cost created by an agent's accumulated, non-transferable knowledge of a customer's codebase, procedures, history, and preferences.
- **Cascade routing:** production architecture that routes workloads across multiple models by difficulty, sending bulk traffic to cheap open-weight models and reserving frontier models for hard steps.
- **Distillation:** training a model on the outputs of a stronger model, transferring capability at a fraction of original training cost.
- **MCP (Model Context Protocol):** an open standard for connecting AI systems to external tools and data sources.
- **IDE (Integrated Development Environment):** the visual editor a programmer works in, combining code editing, debugging, and version control.
- **CLI (Command-Line Interface):** the text-based terminal through which a user issues commands directly to the operating system; the universal interface to file systems, processes, and networks.
- **SWE-bench:** a benchmark scoring a model on its ability to resolve real GitHub issues. *Verified* uses 500 human-validated tasks; *Pro* draws on actively maintained repositories and resists memorization (see Appendix A on harness dependence).
- **Elo:** a rating scale, borrowed from chess, that ranks models by head-to-head preference outcomes; used by LMArena.
- **TPU (Tensor Processing Unit):** Google's in-house AI accelerator, an alternative to merchant GPUs.
- **Commoditize the complement:** strategy of giving away or underpricing an adjacent layer (e.g., models) to expand demand for one's core product (e.g., inference hardware).
- **Intelligence economy:** this series' term for the economic system in which cognitive task-completion becomes a purchasable, meterable input, priced against labor rather than software (see Prologue).
- **Run-rate revenue:** an annualized projection formed by multiplying a recent month's billings by twelve; not audited GAAP revenue, and sensitive to prepayments and one-time effects (see Appendix A).
- **Harness dependence:** the sensitivity of an agentic benchmark score to the scaffolding used to run it; the reason vendor-reported coding scores are not comparable across labs (see Appendix A).

# Appendix C. Timeline of Key Events (Nov 2022 – Jul 2026)

- **Nov 2022** — ChatGPT launches; chatbot era begins.
- **2023** — Copilot/RAG wave; first autonomous-agent experiments (AutoGPT) fail on reliability.
- **Late 2024** — Inference-time reasoning models arrive; RL training shifts toward task completion.
- **Jan 2025** — DeepSeek R1 release resets assumptions about Chinese capability and cost.
- **Mid 2025** — Claude Code public launch; CLI emerges as the agent-native interface.
- **Nov 2025** — Claude Code passes $1B run-rate ~6 months post-launch. Gemini 3 generation begins Google's consumer share surge.
- **Dec 2025** — NVIDIA launches Nemotron 3 open-model family.
- **Jan 2026** — Claude Cowork launches in research preview (Jan 12). ChatGPT share at 68% (Similarweb web traffic), down ~19pp YoY; still above half on web-traffic measures, though already below it on U.S. daily-mobile measures.
- **Feb 2026** — Claude Code passes $2.5B run-rate; Anthropic closes $30B Series G at $380B valuation. Cowork professional plug-ins launch; ~$285B single-day software/services equity sell-off (Feb 3).
- **Mar–Apr 2026** — ChatGPT's True Audience share falls below 50% for the first time since launch (Sensor Tower); it settles at 46.4% by end-May, against Gemini's 27.7% and Claude's 10.3%. Codex (GPT-5.4) and Claude Opus 4.7 releases bring agentic coding to benchmark parity. Anthropic reaches ~$30B run-rate (Apr); Amodei cites 80x annualized Q1 growth.
- **May 2026** — Google I/O (May 19): Gemini 3.5 Flash, Antigravity 2.0, and the Managed Agents API — the harness thesis becomes all three players' explicit strategy. Anthropic ships Claude Opus 4.8 (May 28, 69.2% SWE-bench Pro) and closes a $65B Series H at a $965B post-money valuation, disclosing $47B run-rate revenue. ChatGPT becomes the fastest mobile app ever to reach 1 billion monthly active users.
- **Jun 2026** — NVIDIA Nemotron 3 Ultra becomes the strongest US open-weight model; Chinese open models retain the global open-weight lead. Anthropic releases Fable 5 and Mythos 5 (Jun 9) above the Opus tier; the U.S. Commerce Department suspends both on export-control grounds three days later (Jun 12). OpenAI previews GPT-5.6 as a government-gated limited release (Jun 26). Anthropic releases Claude Sonnet 5 (Jun 30) at 63.2% SWE-bench Pro and roughly half of Opus 4.8's price, making near-frontier agentic capability the mid-tier default; Commerce lifts the export-control order the same day.
- **Jul 2026** — Fable 5 is restored to general availability (Jul 1); Mythos 5 remains limited to approved partners. OpenAI publishes an audit finding ~30% of SWE-bench Pro tasks broken and retracts its recommendation of the benchmark (Jul 8), then ships the GPT-5.6 family — Sol, Terra, Luna — to general availability the following day (Jul 9). Google's Gemini 3.5 Pro passes its announced June window without shipping, and no revised date is published.

---

# References

*All sources accessed July–August 2026. Figures are as reported by the listed sources; measurement caveats are set out in Appendix A.*

1. Anthropic — "Anthropic raises $30 billion in Series G funding at $380 billion post-money valuation" — run-rate revenue of $14 billion, February 2026 (Feb 12, 2026). https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
2. Anthropic — "Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute" — run-rate revenue surpassing $30 billion, against approximately $9 billion at end-2025 (Apr 6, 2026). https://www.anthropic.com/news/google-broadcom-partnership-compute
3. Anthropic — "Anthropic raises $65B in Series H funding at $965B post-money valuation" — run-rate revenue crossing $47 billion (May 28, 2026). https://www.anthropic.com/news/series-h
4. VentureBeat — "Anthropic says it hit a $30 billion revenue run rate after 'crazy' 80x growth" — run-rate trajectory from January 2024 to April 2026 (May 8, 2026). https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth
5. TechCrunch — "Anthropic raises $65 billion, nears $1T valuation ahead of IPO" (May 2026). https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/
6. Bloomberg — "Anthropic AI Tool Sparks Selloff From Software to Broader Market" — $285 billion of market value erased in a single session across software, financial services, and asset management (Feb 3, 2026). https://www.bloomberg.com/news/articles/2026-02-03/legal-software-stocks-plunge-as-anthropic-releases-new-ai-tool
7. Bloomberg Law — "Anthropic's Move Into Legal Is Sinking Data-Services Stocks" — same-day market-impact reporting (Feb 2026). https://news.bloomberglaw.com/artificial-intelligence/anthropics-move-into-legal-is-sinking-data-services-stocks-3/
8. ABC News — "Why a new AI tool hammered some software stocks this week" (Feb 2026). https://abcnews.com/Business/new-ai-tool-hammered-software-stocks-week/story?id=129845251
9. Fortune — "Anthropic's Claude triggered a trillion-dollar selloff. A new upgrade could make things worse" (Feb 2026). https://fortune.com/2026/02/06/anthropic-claude-opus-4-6-stock-selloff-new-upgrade/
10. Anthropic — "Introducing Anthropic Labs" — Claude Cowork research-preview launch (Jan 2026). https://www.anthropic.com/news/introducing-anthropic-labs
11. TechCrunch — "Anthropic's new Cowork tool offers Claude Code without the code" (Jan 12, 2026). https://techcrunch.com/2026/01/12/anthropics-new-cowork-tool-offers-claude-code-without-the-code/
12. SemiAnalysis — "Claude Code is the Inflection Point" (Feb 2026). https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point
13. SERPsculpt — "Claude Code Usage Statistics 2026" (May 2026). https://serpsculpt.com/claude-code-usage-statistics/
14. DemandSage — "Claude AI Statistics (2026)" (May 2026). https://www.demandsage.com/claude-ai-statistics/
15. GetPanto — "Claude AI Statistics 2026: Revenue, Users & Market Share" (May 2026). https://www.getpanto.ai/blog/claude-ai-statistics
16. GetPanto — "Anthropic AI Statistics 2026" (Jun 2026). https://www.getpanto.ai/blog/anthropic-ai-statistics
17. Anthropic Support — "Get started with Claude Cowork" (2026). https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
18. Sensor Tower — *State of AI 2026* — True Audience share series, engagement, and monetization data (Jun 16, 2026). https://sensortower.com/report/state-of-ai-2026
19. Sensor Tower — "Sensor Tower State of AI 2026 Report: Global Time Spent on Generative AI Apps Projected to More Than Double Year-Over-Year" — press release accompanying the report (Jun 16, 2026). https://www.prnewswire.com/news-releases/sensor-tower-state-of-ai-2026-report-global-time-spent-on-generative-ai-apps-projected-to-more-than-double-year-over-year-302800975.html
20. TechCrunch — "ChatGPT's market share slips below 50% for first time" — reporting the Sensor Tower series, incl. Dec 2024 and Dec 2025 readings (Jun 2026). https://techcrunch.com/2026/06/16/chatgpts-market-share-slips-below-50-for-first-time/
21. Vertu — "AI Chatbot Market Share 2026: Similarweb Analysis" (Jan 2026). https://vertu.com/lifestyle/ai-chatbot-market-share-2026-chatgpt-drops-to-68-as-google-gemini-surges-to-18-2
22. Big Technology — "New Data: OpenAI's Lead Is Contracting as AI Competition Intensifies" (Apptopia/Similarweb data, Feb 2026). https://www.bigtechnology.com/p/new-data-openais-lead-is-contracting
23. SQ Magazine — "ChatGPT vs Google Gemini Statistics 2026" (May 2026). https://sqmagazine.co.uk/chatgpt-vs-google-gemini-statistics/
24. AI Business Weekly — "AI Market Share 2026: ChatGPT vs Gemini vs Claude" (Apr 2026). https://aibusinessweekly.net/p/ai-market-share-2026
25. ALM Corp — "Google Gemini vs ChatGPT Market Share 2026" (Jan 2026). https://almcorp.com/blog/google-gemini-vs-chatgpt-market-share-2026/
26. Alphabet — "Alphabet earnings call, Q2 2026: Sundar Pichai's remarks" — Gemini app at 950 million monthly active users, daily actives tripling year-over-year, AI Mode past 1 billion monthly active users (Jul 22, 2026). https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/
27. Similarweb — "AI Search Stats in 2026" — worldwide generative-AI traffic panel: platform share and visit-growth series (Jul 29, 2026). https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/
28. Ramp Economics Lab — "Ramp AI Index, March 2026 update" — head-to-head win share among first-time business AI buyers; transaction data from 50,000+ U.S. businesses (Mar 2026). https://ramp.com/data/ai-index-march-2026
29. TechCrunch — "Anthropic now has more business customers than OpenAI, according to Ramp data" (May 13, 2026). https://techcrunch.com/2026/05/13/anthropic-now-has-more-business-customers-than-openai-according-to-ramp-data/
30. Menlo Ventures — "2025 Mid-Year LLM Market Update: Foundation Model Landscape + Economics" — enterprise LLM share, mid-2025 reading; survey of 150+ technical leaders (Jul 2025). https://menlovc.com/perspective/2025-mid-year-llm-market-update/
31. Menlo Ventures — "2025: The State of Generative AI in the Enterprise" — enterprise LLM and coding share, year-end 2025 reading; survey of ~500 U.S. enterprise decision-makers (Dec 2025). https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/
32. Inference Hub — "Chinese Frontier Open-Source AI Models in 2026" (Apr 2026). https://inferencehub.org/blog/chinese-frontier-open-source-ai-models-2026/
33. Remote OpenClaw — "Best Chinese AI Models 2026: DeepSeek, Qwen, GLM, Kimi" (Jun 2026). https://www.remoteopenclaw.com/blog/best-chinese-models-2026
34. TokenMix — "Best Chinese AI Models 2026 (Q2 Update)" (May 2026). https://tokenmix.ai/blog/best-chinese-ai-models-2026-comparison-guide
35. DeathScore Research — "Chinese AI Models in 2026: API, Pricing & Capabilities Comparison" (2026). https://deathscore.ai/research/chinese-ai-models/en
36. Digital Applied — "Chinese AI Models Q2 2026: 10-Provider Landscape Report" (Apr 2026). https://www.digitalapplied.com/blog/chinese-ai-models-q2-2026-market-share-report
37. NVIDIA Newsroom — "NVIDIA Debuts Nemotron 3 Family of Open Models" (Dec 2025). https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models
38. BuildFastWithAI — "NVIDIA Nemotron 3 Ultra Review" (Jun 2026). https://www.buildfastwithai.com/blogs/nvidia-nemotron-3-ultra-review-2026
39. BuildMVPFast — "Nvidia Nemotron Open Source LLM Models 2026" (Apr 2026). https://www.buildmvpfast.com/blog/nvidia-nemotron-open-source-llm-models-2026
40. NVIDIA Blog — "From RTX to Spark: NVIDIA Accelerates Gemma 4 for Local Agentic AI" (Apr 2026). https://blogs.nvidia.com/blog/rtx-ai-garage-open-models-google-gemma-4/
41. Anthropic — "Introducing Claude Opus 4.8" (May 2026). https://www.anthropic.com/news/claude-opus-4-8
42. Vellum — "Claude Opus 4.8 Benchmarks Explained" — system card benchmark tables and harness-dependence discussion (May 2026). https://www.vellum.ai/blog/claude-opus-4-8-benchmarks-explained
43. CoderSera — "Claude Code vs OpenAI Codex (May 2026): The Honest Engineering-Team Comparison" (May 2026). https://codersera.com/blog/claude-code-vs-openai-codex-2026/
44. CatDoes — "Claude Code vs Codex: The 2026 Comparison" (Apr 2026). https://catdoes.com/blog/claude-code-vs-codex
45. Composio — "Claude Code vs Codex: What I Learned After 100+ Hours With Both" (Jun 2026). https://composio.dev/content/claude-code-vs-openai-codex
46. TechCrunch — "With Gemini 3.5 Flash, Google bets its next AI wave on agents, not chatbots" (May 2026). https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/
47. Google Blog — "I/O 2026 developer highlights: Antigravity, Gemini API, AI Studio" (May 2026). https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/
48. Google Antigravity Blog — "Google I/O 2026" (May 2026). https://antigravity.google/blog/google-io-2026
49. MarkTechPost — "Google Introduces Gemini 3.5 Flash at I/O 2026" (May 2026). https://www.marktechpost.com/2026/05/20/google-introduces-gemini-3-5-flash-at-i-o-2026-a-faster-and-cheaper-model-for-ai-agents-and-coding/
50. AIMadeTools — "Google Antigravity 2.0 Complete Guide" (May 2026). https://www.aimadetools.com/blog/antigravity-2-complete-guide/
51. Anthropic — "Introducing Claude Sonnet 5" (Jun 2026). https://www.anthropic.com/news/claude-sonnet-5
52. TechCrunch — "Anthropic launches Claude Sonnet 5 as a cheaper way to run agents" (Jun 2026). https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/
53. Anthropic — "Redeploying Claude Fable 5" — export-control timeline and restoration terms (Jul 1, 2026). https://www.anthropic.com/news/redeploying-fable-5
54. Al Jazeera — "US lifts restrictions on Anthropic's powerful AI models Fable and Mythos" — incl. GPT-5.6 staggered-release reporting (Jul 1, 2026). https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says
55. OpenAI — "GPT-5.6: Frontier intelligence that scales with your ambition" — general-availability release of the Sol/Terra/Luna tiers, with full benchmark tables and per-token pricing (Jul 9, 2026). https://openai.com/index/gpt-5-6/
56. OpenAI — "Separating signal from noise in coding evaluations" — SWE-Bench Pro task-validity audit; ~30% of the 731-task public split assessed as broken; prior recommendation retracted (Jul 8, 2026). https://openai.com/index/separating-signal-from-noise-coding-evaluations/
57. METR — "Summary of METR's predeployment evaluation of GPT-5.6 Sol" — independent pre-deployment assessment, incl. detected evaluation-gaming rates (Jun 26, 2026). https://metr.org/blog/2026-06-26-gpt-5-6-sol/

