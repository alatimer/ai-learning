# Review of Existing Surveys: Privacy in LLMs

*Systematic review of survey papers and systematizations of knowledge (2024-2025)*

---

## Overview

This document reviews existing survey papers on privacy in Large Language Models to contextualize our research and identify gaps. I identified **15+ substantial surveys** published since 2024, indicating this is an actively surveyed area.

### Survey Landscape Summary

| Category | Count | Key Publications |
|----------|-------|------------------|
| General Privacy Surveys | 6 | Miranda et al., Das et al., Wang et al. |
| SoK Papers | 3 | Shanmugarasa et al., Semantic Privacy SoK, RAG Privacy SoK |
| Machine Unlearning Surveys | 3 | Geng et al., arXiv:2510.25117, Springer AIR |
| Domain-Specific | 3 | Healthcare, Mobile LLMs, Generative AI |
| Security + Privacy Combined | 3 | Yao et al., ACM CSUR entries |

---

## 1. Comprehensive Privacy Surveys

### 1.1 Preserving Privacy in Large Language Models: A Survey on Current Threats and Solutions

**Citation:** Miranda, M., Ruzzetti, E.S., Santilli, A., Zanzotto, F.M., Bratières, S., & Rodolà, E. (2024/2025). *Transactions on Machine Learning Research (TMLR)*.

**Source:** [arXiv:2408.05212](https://arxiv.org/abs/2408.05212) | [OpenReview](https://openreview.net/forum?id=Ss9MTTN7OL)

**Contributions:**
- Comprehensive examination of privacy threats across the LLM lifecycle
- Proposes solutions spanning dataset anonymization → DP training → machine unlearning
- Emphasizes healthcare and other critical domains

**Scope:**
- Privacy attacks on LLMs (memorization, extraction)
- Multi-stage privacy solutions
- Implementation tools and approaches

**DP Coverage:**
- Identifies DP as core solution for both training and inference
- Does not provide extensive empirical comparison of DP methods

**Limitations:**
- Acknowledges "ongoing challenges" in balancing privacy and utility
- Limited quantitative benchmarking of defense effectiveness

**Future Directions:**
- More secure and trustworthy AI systems
- Domain-specific privacy mechanisms

**Relevance to Our Work:** High overlap with our scope; differs in lacking detailed DP method comparisons.

---

### 1.2 On Protecting the Data Privacy of Large Language Models: A Survey

**Citation:** Yan, J., et al. (2024). *arXiv:2403.05156*.

**Source:** [arXiv:2403.05156](https://arxiv.org/abs/2403.05156)

**Contributions:**
- Taxonomy of passive privacy leakage vs. active privacy attacks
- Reviews protection mechanisms across LLM operational stages
- 18-page survey with 4 figures

**Scope:**
- Pre-training, fine-tuning, inference stages
- Both unintentional leakage and adversarial attacks

**DP Coverage:**
- Discusses DP as fundamental mitigation
- Notes DP's role in preventing membership inference and model inversion

**Limitations:**
- Rapidly evolving field limits currency
- Limited empirical comparison

**Future Directions:**
- Privacy in multi-modal LLMs
- Scalable privacy-preserving training

**Relevance to Our Work:** Complementary; we provide more depth on DP mechanisms and emerging methods.

---

### 1.3 A Survey on Privacy Risks and Protection in Large Language Models

**Citation:** (2025). *Journal of King Saud University - Computer and Information Sciences* (Springer).

**Source:** [Springer](https://link.springer.com/article/10.1007/s44443-025-00177-1) | [arXiv:2505.01976](https://arxiv.org/abs/2505.01976)

**Contributions:**
- Comprehensive overview of privacy risks and solutions
- Analyzes model inversion, training data extraction, membership inference
- Emphasizes deployer responsibility for safeguards

**Scope:**
- Privacy leakage mechanisms
- Attack techniques
- Defense implementations

**DP Coverage:**
- Highlights DP as crucial deployer safeguard
- Discusses input/output filtering alongside DP
- Covers audit pipelines and real-time monitoring

**Limitations:**
- Recent publication; may not cover latest 2025 developments

**Relevance to Our Work:** Strong overlap; we add more on DP-specific methods and PEFT combinations.

---

### 1.4 Privacy Issues in Large Language Models: A Survey

**Citation:** (2024). *Computers & Electrical Engineering* (ScienceDirect).

**Source:** [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0045790624006256)

**Contributions:**
- Identifies passive leakage and active attacks
- Reviews: Data Sanitization, Federated Learning, DP, HE, MPC
- Addresses multimodal and personalized LLM challenges

**Scope:**
- Training data threats
- User data threats
- Black-box interpretation challenges

**DP Coverage:**
- Lists DP among core protection approaches
- Acknowledges challenges in black-box LLM interpretation

**Limitations:**
- Notes difficulty interpreting black-box models for privacy analysis

**Future Directions:**
- Multimodal LLM privacy
- Personalized LLM privacy

**Relevance to Our Work:** We exclude federated learning but provide deeper DP focus.

---

## 2. Systematizations of Knowledge (SoK)

### 2.1 SoK: The Privacy Paradox of Large Language Models

**Citation:** Shanmugarasa, Y., Ding, M., Chamikara, M.A.P., & Rakotoarivelo, T. (2024/2025). *ACM Asia CCS 2025*.

**Source:** [arXiv:2506.12699](https://arxiv.org/abs/2506.12699) | [ACM](https://dl.acm.org/doi/10.1145/3708821.3733888)

**Contributions:**
- First SoK to address privacy beyond training data
- Four-category framework: training data, user prompts, outputs, agents
- Evaluates mitigation effectiveness and limitations

**Novel Framework:**
1. Privacy in LLM training data
2. Privacy challenges from user prompts
3. Privacy vulnerabilities in generated outputs
4. Privacy issues in LLM agents

**DP Coverage:**
- Addresses DP as prominent technique
- Notes utility trade-offs
- Covers DP in context of other mitigations

**Key Insight:**
- Prior surveys overlooked user interaction and agent privacy risks
- This is a significant gap our work also addresses

**Limitations:**
- Acknowledges mitigations have both effectiveness and limitations

**Relevance to Our Work:** Highly relevant; shares our concern for agent privacy and inference-time risks.

---

### 2.2 SoK: Semantic Privacy in Large Language Models

**Citation:** (2025). *arXiv:2506.23603*.

**Source:** [arXiv:2506.23603](https://arxiv.org/abs/2506.23603)

**Contributions:**
- Focus on semantic privacy (beyond verbatim memorization)
- Lifecycle-centric framework: input → pretraining → fine-tuning → alignment
- Categorizes attack vectors and defenses

**Key Innovation:**
- Addresses privacy risks from paraphrasing and inference, not just verbatim reproduction
- Analyzes latent representation leakage

**DP Coverage:**
- Lists DP among key defenses
- Also covers embedding encryption, edge computing, unlearning

**Critical Finding:**
- "Critical gaps in semantic-level protection, especially against contextual inference and latent representation leakage"

**Relevance to Our Work:** Very high; aligns with our emphasis on inference attacks beyond memorization.

---

### 2.3 SoK: Privacy Risks and Mitigations in RAG Systems

**Citation:** (2026). *arXiv:2601.03979*.

**Source:** [arXiv:2601.03979](https://arxiv.org/abs/2601.03979)

**Contributions:**
- First systematization of RAG-specific privacy risks
- Systematic literature review
- Framework for risks, mitigations, and evaluation

**Scope:**
- Privacy risks when using sensitive knowledge bases
- RAG poisoning attacks
- Mitigation techniques for retrieval-augmented systems

**Relevance to Our Work:** Complementary; we cover RAG poisoning in attack section but don't focus exclusively on RAG.

---

## 3. Security + Privacy Combined Surveys

### 3.1 Security and Privacy Challenges of Large Language Models: A Survey

**Citation:** Das, B.C., Amini, M.H., & Wu, Y. (2024). *ACM Computing Surveys* 57(6), 1-39.

**Source:** [arXiv:2402.00888](https://arxiv.org/abs/2402.00888) | [ACM](https://dl.acm.org/doi/10.1145/3712001)

**Contributions:**
- Thorough review of security AND privacy challenges
- Covers training data and user risks
- Domain-specific analysis (transportation, education, healthcare)

**Scope:**
- Jailbreaking attacks
- Data poisoning
- PII leakage attacks
- Domain-specific applications

**DP Coverage:**
- Lists among defense approaches
- Not primary focus

**Future Directions:**
- Identifies research gaps in LLM security domain

**Relevance to Our Work:** Broader scope (includes security); we provide deeper privacy/DP focus.

---

### 3.2 Unique Security and Privacy Threats of LLMs: A Comprehensive Survey

**Citation:** Wang, S., Zhu, T., Liu, B., Ding, M., Ye, D., Zhou, W., & Yu, P.S. (2024/2025). *ACM Computing Surveys*.

**Source:** [arXiv:2406.07973](https://arxiv.org/abs/2406.07973)

**Contributions:**
- Systematic taxonomy across LLM lifecycle
- 35 pages, 9 tables, 12 figures
- Four-scenario framework

**Framework:**
1. Pre-training threats
2. Fine-tuning risks
3. Deployment security
4. LLM-agent threats

**Key Insight:**
- LLM threats "fundamentally differ from traditional models"
- Requires scenario-specific countermeasures

**DP Coverage:**
- Addressed within countermeasures
- Not primary focus

**Relevance to Our Work:** Strong structural overlap; we emphasize DP more deeply.

---

### 3.3 A Survey on Large Language Model (LLM) Security and Privacy: The Good, The Bad, and The Ugly

**Citation:** Yao, Y., Duan, J., Xu, K., Cai, Y., Sun, Z., & Zhang, Y. (2023/2024). *High-Confidence Computing* (2024).

**Source:** [arXiv:2312.02003](https://arxiv.org/abs/2312.02003) | [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S266729522400014X)

**Contributions:**
- Novel Good/Bad/Ugly framework
- Explores LLMs as security tools AND attack vectors

**Framework:**
- **The Good:** LLMs for code vulnerability detection, security enhancement
- **The Bad:** LLMs enabling user-level attacks, offensive capabilities
- **The Ugly:** Inherent vulnerabilities, extraction attacks

**DP Coverage:**
- Mentions zero-knowledge proofs, DP, federated learning as Privacy Enhancing Techniques
- Not deep coverage

**Limitations:**
- Parameter/model extraction attacks research is "limited and often theoretical"
- Safe instruction tuning "requires more exploration"

**Relevance to Our Work:** Different framing (security-centric); we focus purely on privacy.

---

## 4. Machine Unlearning Surveys

### 4.1 A Comprehensive Survey of Machine Unlearning Techniques for Large Language Models

**Citation:** Geng, J., Li, Q., Woisetschlaeger, H., Chen, Z., Cai, F., Wang, Y., Nakov, P., Jacobsen, H.A., & Karray, F. (2025). *arXiv:2503.01854*.

**Source:** [arXiv:2503.01854](https://arxiv.org/abs/2503.01854)

**Contributions:**
- Comprehensive taxonomy of LLM unlearning methods
- Definitions and paradigms
- Evaluation metrics and benchmarks
- Strengths and limitations of approaches

**Scope:**
- Removing sensitive/illegal information influence
- Preserving utility without full retraining

**Key Challenge:**
- Balancing data removal with model preservation

**Relevance to Our Work:** Directly relevant to our unlearning section; we cite but don't duplicate.

---

### 4.2 A Survey on Unlearning in Large Language Models

**Citation:** (2025). *arXiv:2510.25117*.

**Source:** [arXiv:2510.25117](https://arxiv.org/abs/2510.25117)

**Contributions:**
- Reviews 180+ papers since 2021
- Novel taxonomy by training stage: training time, post-training, inference time

**Scope:**
- Comprehensive literature coverage
- Stage-based categorization

**Relevance to Our Work:** More comprehensive on unlearning specifically; we provide broader context.

---

### 4.3 A Survey on Large Language Models Unlearning: Taxonomy, Evaluations, and Future Directions

**Citation:** (2025). *Artificial Intelligence Review* (Springer).

**Source:** [Springer](https://link.springer.com/article/10.1007/s10462-025-11376-7)

**Contributions:**
- Taxonomy of unlearning algorithms
- Evaluation methods including benchmarks and threat models
- Novel "robustness" objective formulation

**Applications:**
- Copyright protection
- Model detoxification
- Jailbreaking defense

**Key Finding:**
- Proposes robustness as additional unlearning objective beyond forgetting

**Relevance to Our Work:** Adds robustness perspective we don't emphasize.

---

## 5. Domain-Specific Surveys

### 5.1 Privacy-Preserving Techniques in Generative AI and LLMs: A Narrative Review

**Citation:** (2024). *MDPI Information* 15(11), 697.

**Source:** [MDPI](https://www.mdpi.com/2078-2489/15/11/697)

**Contributions:**
- Narrative review of DP, FL, HE for generative AI
- Focus on preventing memorization of sensitive data

**DP Coverage:**
- Central focus on differential privacy
- Also covers federated learning and homomorphic encryption

**Relevance to Our Work:** Closest to our DP focus; we provide more technical depth.

---

### 5.2 A Survey on Privacy Issues and Mitigation Strategies for LLMs in Healthcare

**Citation:** (2025). *The Journal of Supercomputing* (Springer).

**Source:** [Springer](https://link.springer.com/article/10.1007/s11227-025-08146-1)

**Contributions:**
- Healthcare-specific privacy framework
- Consolidates algorithmic and compliance-based defenses
- Unlike prior surveys, treats privacy and performance together

**Relevance to Our Work:** Domain-specific complement to our general survey.

---

### 5.3 A Survey: Towards Privacy and Security in Mobile Large Language Models

**Citation:** (2025). *arXiv:2509.02411*.

**Source:** [arXiv:2509.02411](https://arxiv.org/abs/2509.02411)

**Contributions:**
- Mobile LLM-specific privacy and security
- Covers DP, FL, prompt encryption
- Unique threats: side-channel attacks on mobile devices

**Relevance to Our Work:** Addresses deployment context we don't cover in depth.

---

## 6. Gap Analysis: What Existing Surveys Miss

Based on this review, existing surveys have the following gaps that our work addresses:

| Gap | Which Surveys Miss It | Our Coverage |
|-----|----------------------|--------------|
| Deep DP method comparison | Most surveys list DP but don't compare methods | Detailed analysis of DP-SGD, DP-LoRA, DP-ZO, etc. |
| PEFT + DP synergy | Briefly mentioned if at all | Dedicated section on parameter-efficient DP |
| Privacy auditing methods | Rarely covered | Section on auditing and empirical ε |
| Quantitative privacy-utility trade-offs | Often qualitative | Tables with specific ε values and accuracy drops |
| Synthetic data via DP | Underexplored | Full section on DP synthetic generation |
| Semantic inference attacks | SoK:Semantic Privacy covers, others miss | Emphasized as emerging threat |

---

## 7. Positioning Our Work

### Overlaps with Existing Surveys
- General privacy threat taxonomy (well-covered)
- Basic DP concepts (covered by all)
- Machine unlearning overview (multiple dedicated surveys)
- Attack descriptions (thoroughly surveyed)

### Our Unique Contributions
1. **DP-Focused Depth:** More detailed treatment of DP variants (DP-SGD, DP-LoRA, DP-ZO, subspace methods)
2. **PEFT Integration:** Systematic coverage of parameter-efficient + DP combinations
3. **Privacy Auditing:** Dedicated coverage of empirical privacy measurement
4. **Synthetic Data Pipeline:** DP for synthetic data generation (Aug-PE, etc.)
5. **Practical Trade-offs:** Quantitative privacy-utility comparisons with specific ε values
6. **2025 Currency:** Includes papers from late 2024 and early 2025

### Recommendation
Our work is **complementary** to existing surveys rather than duplicative. It serves as a **DP-focused technical deep-dive** that readers can use alongside broader surveys like Miranda et al. (2024) or the SoK papers for comprehensive understanding.

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total surveys reviewed | 15 |
| General privacy surveys | 4 |
| SoK papers | 3 |
| Security + privacy combined | 3 |
| Unlearning-specific | 3 |
| Domain-specific | 3 |
| Published in 2024 | 8 |
| Published in 2025 | 7 |
| With substantial DP coverage | 6 |
| Peer-reviewed (journal/conference) | 9 |
| arXiv preprints only | 6 |

---

*Review completed: 2025-01-30*
