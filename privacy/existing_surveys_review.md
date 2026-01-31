# Review of Existing Surveys: Privacy in LLMs

*Systematic review of survey papers and systematizations of knowledge (2024-2025)*

---

## Overview

Before diving into the primary research, I conducted a systematic review of existing survey papers on privacy in Large Language Models. This serves to contextualize our work and identify gaps in the literature that our synthesis might fill. I identified fifteen substantial surveys published since 2024, which indicates this is an actively surveyed area with considerable scholarly attention.

The survey landscape breaks down roughly as follows: six general privacy surveys, three formal Systematizations of Knowledge (SoK papers), three surveys combining security and privacy concerns, three focused specifically on machine unlearning, and three addressing domain-specific applications like healthcare and mobile deployment. What this reveals is that while privacy in LLMs is well-surveyed at a high level, there remains room for deeper technical treatment of specific mechanisms—particularly differential privacy methods and their practical trade-offs.

---

## Part 1: Comprehensive Privacy Surveys

### 1.1 Preserving Privacy in Large Language Models: A Survey on Current Threats and Solutions

Miranda, M., Ruzzetti, E.S., Santilli, A., Zanzotto, F.M., Bratières, S., & Rodolà, E. (2024/2025). *Transactions on Machine Learning Research*.

[https://arxiv.org/abs/2408.05212](https://arxiv.org/abs/2408.05212)

This survey provides a comprehensive examination of privacy threats across the entire LLM lifecycle, proposing solutions that span dataset anonymization, differentially private training, and machine unlearning. The authors place particular emphasis on healthcare and other critical domains where privacy violations carry especially serious consequences. They identify differential privacy as a core solution for both training and inference, though the paper does not provide extensive empirical comparisons between different DP methods. The authors acknowledge the "ongoing challenges" in balancing privacy with utility, but offer limited quantitative benchmarking of defense effectiveness.

**My take:** This is one of the most thorough general surveys available, and it's a good starting point for anyone new to the field. However, it treats DP as one tool among many rather than exploring the nuances of different DP approaches. If you're specifically interested in differential privacy mechanisms, you'll need to look elsewhere for technical depth. The healthcare emphasis is valuable since that's where privacy concerns are most acute, but it means some of the discussion is domain-specific rather than generally applicable.

---

### 1.2 On Protecting the Data Privacy of Large Language Models: A Survey

Yan, J., et al. (2024).

[https://arxiv.org/abs/2403.05156](https://arxiv.org/abs/2403.05156)

This 18-page survey introduces a useful taxonomy distinguishing passive privacy leakage (unintentional) from active privacy attacks (adversarial). The authors review protection mechanisms across the pre-training, fine-tuning, and inference stages. Differential privacy is discussed as a fundamental mitigation, with particular attention to its role in preventing membership inference and model inversion attacks. The paper acknowledges that the rapidly evolving nature of the field limits currency, and like many surveys, it provides limited empirical comparison between approaches. Future directions include privacy in multi-modal LLMs and scalable privacy-preserving training.

**My take:** The passive versus active taxonomy is genuinely useful for thinking about the threat landscape—it forces you to consider both the accidents and the adversaries. This survey is more accessible than some of the more technical papers, making it a good introduction. The coverage of all three stages (pre-training, fine-tuning, inference) is comprehensive without being overwhelming. However, by March 2024 the field was already moving fast, and some of the content feels slightly dated now, particularly around the PEFT+DP combinations that have become so important.

---

### 1.3 A Survey on Privacy Risks and Protection in Large Language Models

(2025). *Journal of King Saud University - Computer and Information Sciences*.

[https://arxiv.org/abs/2505.01976](https://arxiv.org/abs/2505.01976)

This recent survey analyzes model inversion, training data extraction, and membership inference attacks, with particular emphasis on deployer responsibility for implementing safeguards. The authors highlight DP as a crucial deployer safeguard alongside input/output filtering, and they cover audit pipelines and real-time monitoring approaches. Given its 2025 publication date, it may not cover the very latest developments, but it's more current than most available surveys.

**My take:** The emphasis on deployer responsibility is refreshing—much of the privacy literature focuses on what model developers should do during training, but this paper takes seriously the question of what operators can do after deployment. The coverage of audit pipelines is particularly valuable since privacy auditing is an underexplored area. This is a good choice for practitioners who are deploying rather than building LLMs.

---

### 1.4 Privacy Issues in Large Language Models: A Survey

(2024). *Computers & Electrical Engineering*.

[https://www.sciencedirect.com/science/article/abs/pii/S0045790624006256](https://www.sciencedirect.com/science/article/abs/pii/S0045790624006256)

This survey identifies passive leakage and active attacks, reviewing data sanitization, federated learning, differential privacy, homomorphic encryption, and multi-party computation as protection approaches. The authors address emerging challenges with multimodal and personalized LLMs. A notable limitation they acknowledge is the difficulty of interpreting black-box models for privacy analysis—you often can't tell what the model has memorized without attacking it.

**My take:** This is a broader survey that covers the full spectrum of privacy-enhancing technologies rather than focusing specifically on differential privacy. The inclusion of federated learning, homomorphic encryption, and MPC provides useful context for understanding where DP fits in the larger toolkit. However, this breadth comes at the cost of depth—if you want to understand DP specifically, you'll find the treatment somewhat shallow. The discussion of multimodal LLM privacy is forward-looking but necessarily speculative given how new the area is.

---

## Part 2: Systematizations of Knowledge (SoK Papers)

SoK papers aim to organize and synthesize existing knowledge rather than present new research. They're particularly valuable for understanding the state of a field and identifying open problems.

### 2.1 SoK: The Privacy Paradox of Large Language Models

Shanmugarasa, Y., Ding, M., Chamikara, M.A.P., & Rakotoarivelo, T. (2024/2025). *ACM Asia CCS 2025*.

[https://arxiv.org/abs/2506.12699](https://arxiv.org/abs/2506.12699)

This is the first SoK to address privacy concerns beyond training data, introducing a four-category framework covering privacy in training data, user prompts, generated outputs, and LLM agents. The authors evaluate the effectiveness and limitations of various mitigations, noting that prior surveys had overlooked user interaction and agent privacy risks. Differential privacy is addressed as a prominent technique, with acknowledgment of utility trade-offs, but the paper's scope is deliberately broader than any single defense mechanism.

**My take:** This is an excellent paper that deserves more attention. The four-category framework is genuinely novel and forces consideration of privacy dimensions that most surveys ignore. In particular, the attention to agent privacy risks is prescient—as LLMs increasingly use tools and interact with external systems, the attack surface expands dramatically. The observation that prior surveys overlooked user interaction privacy is spot-on. If you read only one SoK in this area, this should be it.

---

### 2.2 SoK: Semantic Privacy in Large Language Models

(2025).

[https://arxiv.org/abs/2506.23603](https://arxiv.org/abs/2506.23603)

This SoK focuses on semantic privacy—privacy risks that go beyond verbatim memorization to include paraphrasing and inference. The authors present a lifecycle-centric framework covering input, pretraining, fine-tuning, and alignment stages, categorizing attack vectors and defenses at each stage. They analyze latent representation leakage, where information can be extracted from intermediate model states even when outputs appear safe. The paper's critical finding is that there are "critical gaps in semantic-level protection, especially against contextual inference and latent representation leakage."

**My take:** This is one of the most intellectually ambitious papers in the survey literature. The distinction between verbatim memorization and semantic inference is crucial and underappreciated. Most privacy research focuses on whether a model can regurgitate training data verbatim, but the more insidious threat may be that models can infer sensitive information that was never explicitly stated. The lifecycle-centric framework is well-structured, and the identification of latent representation leakage as a critical gap is an important contribution. This paper changed how I think about the problem.

---

### 2.3 SoK: Privacy Risks and Mitigations in RAG Systems

(2026).

[https://arxiv.org/abs/2601.03979](https://arxiv.org/abs/2601.03979)

This paper provides the first systematization specifically focused on Retrieval-Augmented Generation (RAG) systems. The authors conducted a systematic literature review to develop a framework for understanding risks, mitigations, and evaluation approaches when LLMs are connected to sensitive knowledge bases. RAG poisoning attacks receive particular attention—these occur when adversaries inject malicious content into retrieval corpora to manipulate model outputs.

**My take:** RAG is increasingly how LLMs are deployed in practice, so this specialized focus is valuable. The privacy risks in RAG are qualitatively different from training-time risks because the retrieval corpus can be modified dynamically, creating an ongoing attack surface. The 2026 publication date means this is the most recent paper in the survey literature, and it benefits from seeing how RAG deployments have evolved. However, the narrow focus on RAG means you'll need other sources for training-time privacy concerns.

---

## Part 3: Security and Privacy Combined Surveys

Several surveys treat security and privacy together, recognizing that the distinction between them is often blurred in practice.

### 3.1 Security and Privacy Challenges of Large Language Models: A Survey

Das, B.C., Amini, M.H., & Wu, Y. (2024). *ACM Computing Surveys* 57(6), 1-39.

[https://arxiv.org/abs/2402.00888](https://arxiv.org/abs/2402.00888)

This thorough review covers both security and privacy challenges, including jailbreaking attacks, data poisoning, and PII leakage attacks. The authors provide domain-specific analysis for transportation, education, and healthcare applications. Differential privacy is listed among defense approaches but is not the primary focus. The paper identifies research gaps in LLM security that point toward future work.

**My take:** The combined security-and-privacy framing is appropriate for practitioners who need to understand the full threat landscape. Jailbreaking and data poisoning are security concerns that can have privacy implications, and treating them together makes sense. The domain-specific sections are useful for understanding how abstract threats manifest in specific applications. However, if your primary interest is privacy and differential privacy specifically, you'll find that DP is one item in a long list rather than a focus.

---

### 3.2 Unique Security and Privacy Threats of LLMs: A Comprehensive Survey

Wang, S., Zhu, T., Liu, B., Ding, M., Ye, D., Zhou, W., & Yu, P.S. (2024/2025). *ACM Computing Surveys*.

[https://arxiv.org/abs/2406.07973](https://arxiv.org/abs/2406.07973)

This is an impressively comprehensive survey at 35 pages with 9 tables and 12 figures. The authors develop a four-scenario framework covering pre-training threats, fine-tuning risks, deployment security, and LLM-agent threats. A key insight is that LLM threats "fundamentally differ from traditional models" and require scenario-specific countermeasures. Differential privacy is addressed within the countermeasures discussion but is not a primary focus.

**My take:** The scale and organization of this survey are impressive—the tables and figures alone are worth consulting as reference material. The argument that LLM threats are fundamentally different from traditional ML threats is important and well-supported. The four-scenario framework provides a useful structure for thinking about where different defenses apply. However, the breadth means that any individual topic receives relatively shallow treatment. This is a good map of the territory but not a detailed guide to any specific region.

---

### 3.3 A Survey on Large Language Model (LLM) Security and Privacy: The Good, The Bad, and The Ugly

Yao, Y., Duan, J., Xu, K., Cai, Y., Sun, Z., & Zhang, Y. (2023/2024). *High-Confidence Computing*.

[https://arxiv.org/abs/2312.02003](https://arxiv.org/abs/2312.02003)

This survey introduces a memorable Good/Bad/Ugly framework. The Good covers how LLMs can be used for security purposes like code vulnerability detection. The Bad addresses how LLMs enable user-level attacks and offensive capabilities. The Ugly covers inherent vulnerabilities and extraction attacks. The authors mention differential privacy, zero-knowledge proofs, and federated learning as Privacy Enhancing Techniques, though without deep coverage. They note that parameter and model extraction attack research is "limited and often theoretical" and that safe instruction tuning "requires more exploration."

**My take:** The Good/Bad/Ugly framing is clever and memorable, making this paper easy to navigate and cite. The recognition that LLMs are both attack targets and attack tools is important—most surveys focus only on one side. However, the privacy coverage is relatively shallow, treating DP as one item in a list. This survey is most useful for understanding the dual-use nature of LLMs rather than for technical depth on any particular defense. The acknowledgment that extraction attack research is limited and theoretical is honest and helpful for calibrating expectations.

---

## Part 4: Machine Unlearning Surveys

Machine unlearning has received dedicated survey attention because it sits at the intersection of privacy law (right to erasure) and technical capability.

### 4.1 A Comprehensive Survey of Machine Unlearning Techniques for Large Language Models

Geng, J., Li, Q., Woisetschlaeger, H., Chen, Z., Cai, F., Wang, Y., Nakov, P., Jacobsen, H.A., & Karray, F. (2025).

[https://arxiv.org/abs/2503.01854](https://arxiv.org/abs/2503.01854)

This survey provides a comprehensive taxonomy of LLM unlearning methods, covering definitions, paradigms, evaluation metrics, and benchmarks. The authors systematically analyze the strengths and limitations of different approaches to removing sensitive or illegal information influence from models without full retraining. They identify the key challenge as balancing data removal with model preservation—you want to forget specific things without degrading general capabilities.

**My take:** This is the best single source for understanding the current state of machine unlearning in LLMs. The taxonomy is well-organized and the coverage is comprehensive. The honest treatment of limitations is particularly valuable—the authors don't oversell current capabilities. If you're trying to understand whether and how to implement unlearning in practice, start here. The benchmark coverage is especially useful for evaluation.

---

### 4.2 A Survey on Unlearning in Large Language Models

(2025).

[https://arxiv.org/abs/2510.25117](https://arxiv.org/abs/2510.25117)

This ambitious survey reviews over 180 papers published since 2021, organizing them by training stage: training-time approaches, post-training approaches, and inference-time approaches. This temporal taxonomy provides a different perspective from method-based taxonomies and helps clarify when different techniques can be applied.

**My take:** The sheer scale of this survey—180+ papers—is impressive and makes it a valuable reference. The training stage taxonomy is useful because it answers the practical question of "when can I apply this technique?" However, the breadth means that individual papers receive less attention. This is more of an annotated bibliography than a critical synthesis. Use it for finding papers rather than understanding them.

---

### 4.3 A Survey on Large Language Models Unlearning: Taxonomy, Evaluations, and Future Directions

(2025). *Artificial Intelligence Review*.

[https://link.springer.com/article/10.1007/s10462-025-11376-7](https://link.springer.com/article/10.1007/s10462-025-11376-7)

This survey proposes robustness as an additional unlearning objective beyond simple forgetting. The authors develop a taxonomy of unlearning algorithms and evaluation methods, including benchmarks and threat models. Applications covered include copyright protection, model detoxification, and jailbreaking defense.

**My take:** The addition of robustness as an objective is an important contribution. Most unlearning work asks "did the model forget?" but this paper also asks "is the forgetting robust to adversarial probing?" This is crucial because surface-level forgetting that can be circumvented by clever prompting isn't really forgetting at all. The connection to jailbreaking defense is novel and suggests interesting future directions.

---

## Part 5: Domain-Specific Surveys

Three surveys focus on specific application domains or deployment contexts.

### 5.1 Privacy-Preserving Techniques in Generative AI and LLMs: A Narrative Review

(2024). *MDPI Information* 15(11), 697.

[https://www.mdpi.com/2078-2489/15/11/697](https://www.mdpi.com/2078-2489/15/11/697)

This narrative review centers on differential privacy, federated learning, and homomorphic encryption for generative AI, with particular focus on preventing memorization of sensitive data. Of the general surveys, this one has the strongest focus on differential privacy specifically.

**My take:** This is the existing survey closest to our own focus on differential privacy. The narrative review format makes it more readable than some of the more taxonomic surveys. However, even here the DP treatment is relatively high-level—you won't find detailed comparisons of DP-SGD variants or PEFT+DP combinations. Still, this is a good starting point if DP is your primary interest.

---

### 5.2 A Survey on Privacy Issues and Mitigation Strategies for LLMs in Healthcare

(2025). *The Journal of Supercomputing*.

[https://link.springer.com/article/10.1007/s11227-025-08146-1](https://link.springer.com/article/10.1007/s11227-025-08146-1)

This survey develops a healthcare-specific privacy framework that consolidates algorithmic and compliance-based defenses. Unlike prior surveys that treat privacy and performance separately, this one explicitly considers them together. The healthcare focus means attention to HIPAA and other regulatory requirements in addition to technical measures.

**My take:** Healthcare is perhaps the single most important domain for LLM privacy, given the sensitivity of medical data and the strict regulatory requirements. This survey does a good job of bridging the technical and compliance perspectives. If you're deploying LLMs in healthcare, this is essential reading. For general audiences, the domain-specific framing may be more detailed than necessary.

---

### 5.3 A Survey: Towards Privacy and Security in Mobile Large Language Models

(2025).

[https://arxiv.org/abs/2509.02411](https://arxiv.org/abs/2509.02411)

This survey addresses the unique privacy and security challenges of running LLMs on mobile devices. Coverage includes differential privacy, federated learning, and prompt encryption, along with threats specific to mobile contexts like side-channel attacks. The on-device computation context creates different trade-offs than cloud deployment.

**My take:** Mobile LLM deployment is an increasingly important context that receives little attention in general surveys. The side-channel attack discussion is particularly relevant—when the model runs on a device you don't control, hardware-level attacks become possible. However, this is a specialized topic, and most readers interested in LLM privacy can safely skip it unless mobile deployment is specifically relevant.

---

## Gap Analysis: What Existing Surveys Miss

Based on this comprehensive review, I identified several gaps in the existing survey literature that our work addresses.

**Deep comparison of DP methods.** Most surveys list differential privacy as one defense among many but do not compare DP-SGD, DP-LoRA, DP-ZO, and subspace methods. Our work provides detailed analysis of these variants and their trade-offs.

**PEFT + DP synergy.** The combination of parameter-efficient fine-tuning with differential privacy is briefly mentioned in some surveys but rarely receives dedicated attention. We cover this synergy in depth because it represents the current state of the art for practical private fine-tuning.

**Privacy auditing methods.** Methods for empirically measuring privacy leakage are rarely covered in existing surveys. We include a section on auditing because the gap between theoretical ε guarantees and empirical privacy is often substantial.

**Quantitative privacy-utility trade-offs.** Many surveys discuss the privacy-utility trade-off qualitatively but don't provide specific numbers. We include tables with specific ε values and corresponding accuracy measurements.

**Synthetic data generation via DP.** Using differentially private LLMs to generate synthetic training data is underexplored in the survey literature. We cover this pipeline in detail.

**Semantic inference attacks.** The SoK on Semantic Privacy covers this, but other surveys largely miss the distinction between verbatim memorization and semantic inference. We emphasize this as an emerging threat.

---

## Positioning Our Work

### Where We Overlap

Several areas are already well-covered in existing surveys. General privacy threat taxonomies appear in nearly every survey we reviewed. Basic differential privacy concepts are covered by all. Machine unlearning has multiple dedicated surveys with comprehensive coverage. Attack descriptions are thoroughly surveyed across multiple papers.

### Our Unique Contributions

First, we provide DP-focused depth with detailed treatment of DP variants including DP-SGD, DP-LoRA, DP-ZO, and subspace methods. Second, we offer systematic coverage of PEFT integration—how parameter-efficient methods combine with differential privacy. Third, we dedicate attention to privacy auditing and empirical privacy measurement. Fourth, we cover the synthetic data pipeline for DP-based synthetic data generation. Fifth, we provide practical trade-offs with quantitative privacy-utility comparisons using specific ε values. Sixth, our 2025 currency includes papers from late 2024 and early 2025 that earlier surveys could not cover.

### Bottom Line

Our work is complementary to existing surveys rather than duplicative. It serves as a DP-focused technical deep-dive that readers can use alongside broader surveys like Miranda et al. (2024) or the SoK papers. If you want a broad overview of LLM privacy, the existing surveys are excellent starting points. If you want to understand differential privacy mechanisms specifically, including practical implementation guidance and quantitative trade-offs, our synthesis provides depth that existing surveys lack.

---

## Summary Statistics

In total, I reviewed fifteen surveys: four general privacy surveys, three SoK papers, three combining security and privacy, three focused specifically on unlearning, and three addressing domain-specific applications. Of these, eight were published in 2024 and seven in 2025, reflecting the rapid growth of interest in this area. Six surveys provide substantial coverage of differential privacy, though none match the depth we provide here. Nine surveys have been peer-reviewed in journals or conferences, while six remain as arXiv preprints.

---

*Review completed: 2025-01-30*
