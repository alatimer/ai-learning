# Existing Surveys, Funding Databases, and Landscape Analyses for AI Safety Prioritization

*Compiled 2026-03-14. URLs verified where possible; some may have changed since compilation.*

The resources below are organized into three categories: (1) funding databases that reveal where money flows, (2) expert surveys that capture researcher opinion on priorities, and (3) landscape analyses that map the field's structure. Each entry includes a relevance assessment for the task of identifying neglected high-leverage subareas across the three layers of AI defence.

---

## 1. Funding Databases

These allow you to see which AI safety subareas are receiving the most (and least) financial support — a direct measure of neglectedness.

### 1.1 Open Philanthropy Grants Database (now Coefficient Giving)

- **URL:** https://coefficientgiving.org/funds (formerly openphilanthropy.org/grants)
- **Note:** Open Philanthropy has rebranded to Coefficient Giving. The old grants database URL now redirects and the new site does not yet appear to have a publicly searchable grants database. Historical grant data may still be accessible via archived pages or by contacting the organization.
- **Summary:** Open Philanthropy has been the single largest funder of AI safety work, disbursing hundreds of millions of dollars under the "Potential Risks from Advanced AI" focus area. Their database historically allowed filtering by focus area and listed dollar amounts, grantee organizations, dates, and short descriptions for each grant. Grants span technical alignment, interpretability, governance/policy, evaluations, and field-building. The categorization is fairly coarse — you would need to read individual grant descriptions to classify them into fine-grained subareas (e.g., mechanistic interpretability vs. RLHF vs. compute governance).
- **Relevance:** High. This is the single best source for understanding where the majority of philanthropic AI safety funding goes. If the database becomes accessible again, analyzing it by subarea would directly reveal funding gaps.

### 1.2 Long-Term Future Fund (EA Funds)

- **URL:** https://funds.effectivealtruism.org/funds/far-future
- **Verified:** Yes. The page shows payout reports (e.g., 2024 Q2: $5.4M across 141 grantees) and individual grant details.
- **Summary:** The LTFF makes grants to organizations and individuals working on existential risk reduction, with heavy emphasis on AI safety and alignment. It publishes quarterly payout reports listing every grant with dollar amounts and paragraph-length descriptions explaining the fund managers' reasoning. Grant sizes range from a few thousand dollars for individual researchers to six-figure organizational grants. The LTFF is particularly valuable for tracking smaller, earlier-stage, and individual-level funding — the kinds of grants that Open Philanthropy typically does not make.
- **Relevance:** High. Payout report descriptions usually name specific research topics (mechanistic interpretability, agent foundations, governance, etc.), making subarea categorization relatively straightforward. Captures the "long tail" of AI safety funding.

### 1.3 Survival and Flourishing Fund (SFF)

- **URL:** https://survivalandflourishing.fund/
- **Verified:** Yes. Lists ~$152M in total philanthropic gifts and grants from 2019–2025.
- **Summary:** SFF uses a novel "S-process" (simulated donor coordination) to allocate funding, primarily from Jaan Tallinn. It makes large grants ($500K–$5M+) to organizations like MIRI, ARC, Redwood Research, and others. Grant recommendations are published after each funding round as a list of organizations and recommended amounts, but with minimal narrative explanation per grant. SFF's scope extends beyond AI safety to other existential risk areas.
- **Relevance:** Medium. Useful at the organizational level — since SFF funds whole organizations rather than specific projects, you categorize based on what each grantee works on. Less granular than LTFF for subarea analysis.

### 1.4 EA Infrastructure Fund

- **URL:** https://funds.effectivealtruism.org/funds/ea-community
- **Summary:** Not exclusively focused on AI safety, but makes grants supporting the broader AI safety ecosystem — field-building programs, training workshops, career development, and community infrastructure. Publishes payout reports in the same format as the LTFF.
- **Relevance:** Low-medium. Captures "meta" and field-building spending that would be missed by looking only at direct research grants. Useful for a complete picture but not for subarea-level analysis of technical research.

### 1.5 AISafety.com Field Map

- **URL:** https://www.aisafety.com/landscape-map
- **Verified:** Yes. An interactive map and directory of AI safety organizations, categorized by type (research, advocacy, funding, governance, training, etc.).
- **Summary:** A community-maintained directory cataloging AI safety organizations, researchers, and projects. Includes an interactive D3.js visualization showing organizations geographically, with categories like "Conceptual Cliffs," "Funding Forest," and "Research Range." While not a funding tracker per se, it provides a comprehensive map of the AI safety organizational landscape.
- **Relevance:** Medium. Useful for identifying the full universe of AI safety organizations to cross-reference with funding data and identify gaps — particularly organizations that may be underfunded or working in neglected areas.

### 1.6 Georgetown CSET Data Tools

- **URL:** https://cset.georgetown.edu/
- **Summary:** Georgetown's Center for Security and Emerging Technology tracks government R&D spending on AI (NSF, DARPA, etc.), complementing the philanthropic databases above. Their data tools and reports map AI governance and safety funding flows from government sources.
- **Relevance:** Medium. Important for capturing the government funding side, which is significant but harder to disaggregate into safety-specific subareas.

---

## 2. Expert Surveys

These capture researcher opinions on which AI safety problems are most important, most neglected, and most tractable.

### 2.1 AI Impacts: "Thousands of AI Authors on the Future of AI" (2024)

- **URL:** https://arxiv.org/abs/2401.02843
- **Verified:** Yes. Authors: Katja Grace, Harlan Stewart, Julia Fabienne Sandkühler, Stephen Thomas, Ben Weinstein-Raun, Jan Brauner, Richard C. Korzekwa. Revised October 2025.
- **Summary:** The largest and most comprehensive survey of AI researchers on timelines, risk, and safety. Surveyed 2,778 researchers who had published at top AI venues (NeurIPS, ICML, ICLR, AAAI, IJCAI, JMLR). Key findings: median 50% chance of HLMI by ~2047 (down from ~2060 in 2022 wave), roughly 5–10% median probability assigned to "extremely bad" outcomes (human extinction or similar), and strong majority support for prioritizing AI safety research. The survey asks about which concerns researchers weight most heavily (misuse, loss of control, inequality, etc.).
- **Relevance:** High. Directly shows which AI risk categories the broad research community considers most serious. The longitudinal data (2016 → 2022 → 2023 waves) shows how priorities are shifting. However, the survey asks about risk categories rather than specific technical subareas, so it's better for high-level prioritization than for comparing e.g. interpretability vs. RLHF.

### 2.2 AI Impacts: Earlier Survey Waves (2016, 2022)

- **URL (2016):** https://arxiv.org/abs/1705.08807
- **URL (2022):** https://aiimpacts.org/2022-expert-survey-on-progress-in-ai/
- **Summary:** The 2016 wave surveyed 352 AI researchers (NeurIPS, ICML) and found median HLMI estimates around 2061–2086 depending on respondent region. The 2022 wave repeated and expanded the survey with accelerated timeline estimates. These earlier waves provide a longitudinal baseline showing experts becoming more compressed in their timeline estimates and more concerned about risk.
- **Relevance:** Medium. Valuable for contextualizing urgency but not for subarea-level prioritization.

### 2.3 Existential Risk Persuasion Tournament (XPT)

- **URL:** https://forecastingresearch.org/xpt
- **Verified:** Yes. Run by the Forecasting Research Institute with 169 participants.
- **Summary:** Brought together superforecasters and domain experts to estimate probabilities of various existential catastrophes by 2100, including AI-caused extinction. Used structured adversarial collaboration — participants wrote arguments for and against different risk levels and updated estimates. Key finding: superforecasters gave relatively low AI extinction probabilities (~0.38% median) while domain experts gave somewhat higher estimates. Also covers nuclear war, biorisks, climate for comparison.
- **Relevance:** Medium-high. Provides unusually well-calibrated risk estimates and allows comparing AI risk to other existential risks. The superforecaster/expert gap is itself informative. However, it assesses risk magnitude rather than which safety subareas are most neglected.

### 2.4 80,000 Hours: "Preventing an AI-Related Catastrophe" Problem Profile

- **URL:** https://80000hours.org/problem-profiles/artificial-intelligence/
- **Verified:** Yes.
- **Summary:** 80,000 Hours ranks global problems using the Importance, Neglectedness, Tractability (INT) framework. Their AI problem profile rates preventing AI catastrophe as their top-priority problem area. It breaks down AI risk into categories (misalignment/loss of control, power concentration, arms races, misuse), discusses specific career paths, and estimates the number of researchers working in each area. Notes that "only a few thousand people" are focused on the most important AI challenges.
- **Relevance:** High. One of the most accessible analyses explicitly designed to identify neglected areas. The INT framework maps directly onto the question of "where should additional effort go?" Covers both technical safety and governance.

### 2.5 GovAI Surveys and Research Reports

- **URL:** https://www.governance.ai/research
- **Verified:** Yes. Active research hub with publications through 2026.
- **Summary:** GovAI has conducted multiple surveys on AI governance priorities, including surveys of the general public, policymakers, and AI experts. Their research covers which governance interventions experts consider most important (compute governance, international treaties, licensing regimes, safety standards). Recent publications (2025–2026) cover topics like frontier AI auditing, dual-use AI capabilities, data center policy, and AI labor displacement. Allan Dafoe and collaborators have published "AI Governance: A Research Agenda" mapping priority areas.
- **Relevance:** High for Layer 1 and Layer 3 subareas (governance, international coordination, societal resilience). GovAI is the best source for understanding which governance subareas experts consider most important and neglected.

### 2.6 EA Survey (Rethink Priorities)

- **URL:** https://rethinkpriorities.org/research (search for "EA Survey")
- **Summary:** The annual EA Survey asks effective altruists about cause area priorities. AI safety / "long-term future and AI" has grown to become the top or near-top cause area among respondents. While respondents are not all AI experts, the EA community contains a high concentration of people who have thought carefully about cause prioritization using the INT framework.
- **Relevance:** Low-medium. Shows macro-level trends in how AI safety is prioritized relative to other causes (global poverty, animal welfare, biosecurity), but does not disaggregate into AI safety subareas.

### 2.7 MIT AI Risk Repository

- **URL:** https://airisk.mit.edu/
- **Verified:** Yes. Contains 1,700+ AI risks extracted from 74 frameworks.
- **Summary:** A comprehensive database of AI risks organized via two taxonomies: a causal taxonomy (by entity, intent, timing) and a domain taxonomy (seven domains: discrimination, privacy, misinformation, malicious actors, human-computer interaction, socioeconomic impacts, AI system safety). Freely accessible via Google Sheets or OneDrive. Not a survey of opinion, but a systematic cataloguing of which risk categories have received the most academic attention (measured by publication volume).
- **Relevance:** High. Comparing the density of literature across the 1,700+ risk categories provides a direct proxy for research attention allocation. Categories with fewer associated papers may indicate neglected areas.

### 2.8 CAIS Statement on AI Risk (2023)

- **URL:** https://www.safe.ai/work/statement-on-ai-risk
- **Summary:** A one-sentence statement — "Mitigating the risk of extinction from AI should be a global priority alongside other societal-scale risks such as pandemics and nuclear war" — signed by hundreds of AI researchers and executives including Geoffrey Hinton, Yoshua Bengio, Demis Hassabis, Sam Altman, and Dario Amodei.
- **Relevance:** Low. Useful as a data point about breadth of expert concern but provides no subarea-level information.

### 2.9 FLI "Pause Giant AI Experiments" Open Letter (2023)

- **URL:** https://futureoflife.org/open-letter/pause-giant-ai-experiments/
- **Summary:** Called for a 6-month pause on training AI systems more powerful than GPT-4. Garnered thousands of signatures from AI researchers and public figures. Reflects widespread expert concern about pace of development outstripping safety work.
- **Relevance:** Low. Demonstrates breadth of concern but not useful for subarea prioritization. Subject to selection bias.

### 2.10 Stanford HAI AI Index Report (Annual)

- **URL:** https://hai.stanford.edu/ai-index
- **Verified:** Yes (redirects from aiindex.stanford.edu).
- **Summary:** Annual data compilation covering AI research trends, policy activity, public opinion, corporate safety commitments, and expert views. Includes data on government AI policy activity and academic research trends. Aggregates from multiple surveys and sources rather than conducting original surveys.
- **Relevance:** Medium. Good for macro-level trends in AI safety attention (publication volumes, policy actions) but not disaggregated by safety subarea.

---

## 3. Landscape Analyses and Taxonomies

These map the structure of the AI safety field and identify where effort is concentrated versus where gaps exist.

### 3.1 Larks' Annual AI Alignment Literature Review

- **URL:** https://www.alignmentforum.org/ (search for "Larks annual review"; published each December/January)
- **Summary:** An annual review series on the Alignment Forum that surveys essentially all published alignment research for a given year, organized by research group and topic. Covers academic labs, independent researchers, and organizations. Provides a near-exhaustive catalog of who is working on what, allowing longitudinal comparison year over year.
- **Relevance:** Very high. Arguably the single most useful resource for this project. It tracks actual research output by subarea and institution, making it possible to see where effort is concentrated and where it's thin. The annual format allows tracking trends over time.

### 3.2 CAIS: "An Overview of Catastrophic AI Risks" (Hendrycks et al., 2023)

- **URL:** https://arxiv.org/abs/2306.12001
- **Verified:** Yes. Authors: Dan Hendrycks, Mantas Mazeika, Thomas Woodside.
- **Summary:** Comprehensive taxonomy of catastrophic AI risks organized into four categories: malicious use, AI race dynamics, organizational risks, and rogue AI. While not strictly a "landscape of research" document, it functions as a taxonomy of problem areas and implicitly maps where work is and is not being done.
- **Relevance:** High. Provides a structured framework for categorizing safety subareas across all three defence layers. The four-category structure maps well onto Layer 1 (race dynamics), Layer 2 (rogue AI, organizational risks), and Layer 3 (malicious use).

### 3.3 CAIS: "Unsolved Problems in ML Safety" (Hendrycks et al., 2021)

- **URL:** https://arxiv.org/abs/2109.13916
- **Verified:** Yes. Authors: Dan Hendrycks, Nicholas Carlini, John Schulman, Jacob Steinhardt.
- **Summary:** Research agenda organized around four pillars: robustness, monitoring, alignment, and systemic safety. Each pillar is broken into specific open problems with concrete research questions. Identifies which areas have well-defined tractable problems versus which are more nebulous.
- **Relevance:** High. Directly relevant for Layer 2 (constraining AI capabilities). The four-pillar structure provides a ready-made taxonomy of technical safety subareas with identified open problems — useful for assessing which problems have attracted substantial work since 2021 and which remain under-explored.

### 3.4 "Concrete Problems in AI Safety" (Amodei et al., 2016)

- **URL:** https://arxiv.org/abs/1606.06565
- **Summary:** Foundational paper defining five concrete research problems: safe exploration, robustness to distributional shift, avoiding negative side effects, avoiding reward hacking, and scalable oversight. Authored by Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, Dan Mané. Heavily influenced how the field is organized.
- **Relevance:** Medium. Now somewhat dated, but serves as a baseline taxonomy. Comparing the 2016 problem set against current research activity shows which problems attracted substantial follow-up work and which did not.

### 3.5 Anthropic: "Core Views on AI Safety"

- **URL:** https://www.anthropic.com/news/core-views-on-ai-safety
- **Summary:** Anthropic's published perspective on safety priorities, timelines, and research approach. Covers constitutional AI, interpretability, evaluations, and their overall strategy for why safety is important and what the key technical challenges are.
- **Relevance:** Medium. Reveals how one of the major frontier AI labs prioritizes safety subareas. Not a neutral analysis, but useful for understanding where industry investment is directed (which areas are therefore less neglected).

### 3.6 Anthropic: Transformer Circuits (Mechanistic Interpretability)

- **URL:** https://transformer-circuits.pub/
- **Summary:** Anthropic's dedicated publication thread for mechanistic interpretability research. Represents a major, well-documented research agenda in one specific safety subarea with detailed open problems and progress tracking.
- **Relevance:** Low-medium. Useful for understanding the depth of effort in one specific subarea (interpretability) but not a landscape analysis.

### 3.7 MIRI Technical Research Agenda

- **URL:** https://intelligence.org/files/TechnicalAgenda.pdf
- **Summary:** MIRI's foundational 2014–2015 research agenda covering agent foundations: decision theory, logical uncertainty, Vingean reflection, and value alignment theory. Defined the "agent foundations" branch of alignment research. MIRI later shifted toward less publicly shared research directions (~2020–2021).
- **Relevance:** Low. Historically important for understanding how the field was conceptualized but now dated. The shift toward opacity makes MIRI's current priorities hard to assess.

### 3.8 ARC (Alignment Research Center) / ELK Report

- **URL:** https://alignment.org/ (approximate)
- **Summary:** ARC, founded by Paul Christiano, published research agendas focused on Eliciting Latent Knowledge (ELK) and related alignment problems. The ELK report became a significant reference document defining a specific cluster of alignment research problems.
- **Relevance:** Low-medium. Important for understanding one influential research direction but not a broad landscape analysis.

### 3.9 GovAI Research Agenda

- **URL:** https://www.governance.ai/research
- **Verified:** Yes (see Section 2.5).
- **Summary:** GovAI's research agendas outline their view of the AI governance landscape: compute governance, international AI governance, AI labor impacts, standards/regulation, and strategic dynamics. Recent work (2025–2026) covers frontier AI auditing, dual-use capabilities, and data center policy.
- **Relevance:** High for governance subareas (Layer 1 and Layer 3). The best source for a structured map of AI governance research priorities.

### 3.10 80,000 Hours Problem Profiles

- **URL:** https://80000hours.org/problem-profiles/artificial-intelligence/
- **Verified:** Yes (see Section 2.4).
- **Summary:** Categorizes AI safety into technical safety, governance/policy, and strategy, with further subdivision into specific research areas. Includes estimates of researcher headcount per area and assessments of neglectedness.
- **Relevance:** High. One of the most regularly updated landscape mappings, explicitly designed to help identify neglected areas.

### 3.11 DeepMind Safety Research

- **URL:** https://deepmindsafetyresearch.medium.com/ (approximate)
- **Summary:** DeepMind has published research agendas covering reward modeling, specification gaming, goal misgeneralization, and scalable oversight. Their specification gaming repository is a taxonomy of one specific failure mode.
- **Relevance:** Medium. Like Anthropic's publications, useful for understanding where a major lab directs safety effort but not a neutral landscape analysis.

### 3.12 Frontier Lab Safety Publications (Anthropic, DeepMind, OpenAI)

- **URLs:**
  - https://www.anthropic.com/news/core-views-on-ai-safety
  - https://deepmind.google/about/safety/
  - https://openai.com/safety
- **Summary:** All three leading frontier labs have published their safety priorities. Anthropic emphasizes interpretability, Constitutional AI, and evals. DeepMind focuses on scalable alignment and reward modeling. OpenAI has discussed superalignment, red-teaming, and preparedness frameworks. Comparing their stated priorities reveals areas of consensus (e.g., evaluations, interpretability) and divergence.
- **Relevance:** Medium. These are revealed priorities of the best-resourced actors, so areas they agree on are likely least neglected. Areas none of them emphasize may represent gaps.

### 3.13 OECD AI Policy Observatory

- **URL:** https://oecd.ai/
- **Summary:** Tracks AI governance and policy developments globally, including safety-related governance efforts across countries and international bodies. Focused more on policy/governance than technical research.
- **Relevance:** Medium for Layer 1 (international agreements, export controls) and Layer 3 (societal preparedness). Provides the governmental/institutional perspective that philanthropic databases miss.

---

## Summary: Most Useful Resources by Purpose

### For quantifying research attention by subarea:
1. **Larks' Annual Reviews** — near-exhaustive catalog of alignment research output, year by year
2. **MIT AI Risk Repository** — 1,700+ risks categorized; publication density per category is a direct proxy for attention
3. **Semantic Scholar / OpenAlex API** — not listed above but can be queried programmatically to count papers by subarea keyword

### For quantifying funding by subarea:
1. **Open Philanthropy / Coefficient Giving grants** — largest single funder (if database becomes accessible again)
2. **LTFF payout reports** — detailed, subarea-tagged grants
3. **SFF grant rounds** — large organizational grants

### For expert assessments of neglectedness:
1. **80,000 Hours problem profiles** — explicit INT ratings
2. **AI Impacts 2024 survey** — largest survey of AI researchers on risk priorities
3. **GovAI research and surveys** — best for governance subarea prioritization
4. **XPT** — calibrated risk magnitude estimates with expert-superforecaster comparison

### For structured taxonomies to organize subareas:
1. **CAIS "Unsolved Problems in ML Safety"** — four-pillar technical taxonomy
2. **CAIS "Overview of Catastrophic AI Risks"** — four-category risk taxonomy
3. **"Concrete Problems in AI Safety"** — foundational five-problem taxonomy
4. **GovAI Research Agenda** — governance-specific taxonomy
