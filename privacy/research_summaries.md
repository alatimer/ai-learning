# Research Summaries: Privacy in LLMs

*Focus: Differential Privacy Applications | Scope: 2022-2025*

---

## Table of Contents
1. [Surveys and Overviews](#1-surveys-and-overviews)
2. [Differential Privacy for LLM Training/Fine-tuning](#2-differential-privacy-for-llm-trainingfine-tuning)
3. [Privacy Attacks](#3-privacy-attacks)
4. [Machine Unlearning](#4-machine-unlearning)
5. [Privacy Auditing and Measurement](#5-privacy-auditing-and-measurement)
6. [Synthetic Data Generation](#6-synthetic-data-generation)
7. [Privacy-Preserving Inference](#7-privacy-preserving-inference)
8. [PII Detection and Protection](#8-pii-detection-and-protection)
9. [Regulatory and Compliance](#9-regulatory-and-compliance)
10. [Industry Practices](#10-industry-practices)
11. [DP Safety Benefits Beyond Privacy](#11-dp-safety-benefits-beyond-privacy)

---

## 1. Surveys and Overviews

### 1.1 On Protecting the Data Privacy of Large Language Models: A Survey
**Citation:** Yan et al. (2024). arXiv:2403.05156

**Contributions:**
- Comprehensive taxonomy of data privacy threats in LLMs
- Categorizes threats into passive privacy leakage vs. active privacy attacks
- Reviews protection mechanisms across different LLM operational stages

**Methods:**
- Systematic literature review
- Threat modeling across LLM lifecycle (pre-training, fine-tuning, inference)

**Limitations:**
- Rapidly evolving field means survey may miss recent developments
- Limited empirical comparison of defense effectiveness

**Future Work:**
- Privacy in multi-modal LLMs
- Scalable privacy-preserving training methods

---

### 1.2 Privacy in Large Language Models: Attacks, Defenses and Future Directions
**Citation:** Yao et al. (2023). arXiv:2310.10383

**Contributions:**
- Categorizes privacy attacks by adversary capabilities
- Comprehensive overview of defense strategies
- Identifies emerging privacy concerns as LLMs evolve

**Methods:**
- Attack taxonomy based on threat model
- Defense evaluation framework

**Limitations:**
- Focus primarily on text modality
- Some defenses lack rigorous privacy guarantees

**Future Work:**
- Multi-modal privacy research
- Privacy in LLM agents and tool use

---

### 1.3 SoK: Semantic Privacy in Large Language Models
**Citation:** arXiv:2506.23603 (2025)

**Contributions:**
- Systematization of knowledge on semantic privacy (beyond verbatim memorization)
- Framework for understanding inference-based privacy violations

**Methods:**
- Taxonomy of semantic privacy threats
- Analysis of mitigation approaches

**Limitations:**
- Semantic privacy harder to define and measure than syntactic privacy

**Future Work:**
- Formal definitions of semantic privacy
- Defenses against inference attacks

---

### 1.4 Privacy Issues in Large Language Models: A Survey (Technical Report)
**Citation:** Neel et al. (2023). Seth Neel's technical report

**Contributions:**
- Practical overview of privacy risks
- Discussion of regulatory implications

**Methods:**
- Literature synthesis with industry focus

---

## 2. Differential Privacy for LLM Training/Fine-tuning

### 2.1 Privately Fine-Tuning Large Language Models with Differential Privacy
**Citation:** Yu et al. (2022). arXiv:2210.15042

**Contributions:**
- First systematic study of DP fine-tuning for billion-parameter LLMs
- Shows larger pre-trained models achieve better privacy-utility trade-offs

**Methods:**
- DP-SGD with gradient clipping and noise addition
- Evaluation across multiple NLP benchmarks

**Limitations:**
- Significant utility degradation at strong privacy levels (ε < 1)
- Computational overhead from per-example gradient computation

**Future Work:**
- More efficient DP training algorithms
- Better privacy accounting for fine-tuning

---

### 2.2 Fine-Tuning LLMs with User-Level Differential Privacy
**Citation:** Levy et al. (2024). arXiv:2407.07737

**Contributions:**
- Addresses user-level DP (protecting all contributions from a single user)
- Compares example-level sampling (ELS) vs. user-level sampling (ULS)
- Novel privacy accountant for tight guarantees

**Methods:**
- User-level DP-SGD variants
- Per-user gradient clipping

**Limitations:**
- Requires knowing user boundaries in training data
- Performance depends on user data diversity

**Future Work:**
- Adaptive user-level clipping strategies
- Combining with other PEFT methods

---

### 2.3 Mind the Privacy Unit! User-Level DP for Language Model Fine-Tuning
**Citation:** Chua et al. (2024). arXiv:2406.14322

**Contributions:**
- Analysis of privacy unit choice (example vs. user)
- Practical guidelines for user-level DP

**Methods:**
- Comparative evaluation of privacy units
- Empirical privacy auditing

**Limitations:**
- Trade-offs depend on data characteristics

---

### 2.4 Private Fine-tuning of Large Language Models with Zeroth-order Optimization (DP-ZO)
**Citation:** Malladi et al. (2024). arXiv:2401.04343

**Contributions:**
- Memory-efficient DP fine-tuning using zeroth-order optimization
- Only privatizes scalar step size (not full gradients)
- Reduces memory to <16GB even with sequence length 2048

**Methods:**
- Zeroth-order gradient estimation
- Noise addition only to scalar values

**Limitations:**
- May converge slower than first-order methods
- Requires more forward passes

**Future Work:**
- Hybrid zeroth/first-order approaches
- Application to larger models

---

### 2.5 Differentially Private Subspace Fine-Tuning (DP-SFT)
**Citation:** arXiv:2601.11113 (2025)

**Contributions:**
- Identifies low-dimensional task-specific subspace for updates
- Injects DP noise only into this subspace

**Methods:**
- Subspace identification via PCA or learned projections
- Targeted noise injection

**Limitations:**
- Subspace quality affects results
- Additional computational cost for subspace identification

---

### 2.6 Differentially Private Parameter-Efficient Fine-tuning (DP-LoRA)
**Citation:** Various (2023-2024). ICLR 2024, arXiv:2312.17493

**Contributions:**
- Combines LoRA with differential privacy
- Reduces total noise by reducing trainable parameters
- 89% accuracy on MNLI with ε=6

**Methods:**
- Low-rank adaptation with DP-SGD
- Per-adapter gradient clipping

**Limitations:**
- LoRA produces ~3x more noise than full fine-tuning for same DP guarantee
- Sensitive to hyperparameters under DP

**Future Work:**
- FFA-LoRA (freeze random matrices) for further improvement
- Better understanding of LoRA + DP dynamics

---

### 2.7 FlashDP: Private Training Large Language Models with Efficient DP-SGD
**Citation:** arXiv:2507.01154 (2025)

**Contributions:**
- Addresses scalability of DP-SGD to foundation model era
- Optimized implementation for large-scale training

**Methods:**
- Efficient per-example gradient computation
- Memory-optimized clipping

---

### 2.8 Differentially Private Next-Token Prediction
**Citation:** Ginart et al. (2024). arXiv:2403.15638

**Contributions:**
- DP guarantees for the prediction task itself (not just training)
- PMixED approach: DP at inference via prediction mixing

**Methods:**
- Mix predictions from multiple models
- Aggregation with DP noise

**Limitations:**
- Increased inference cost
- Requires multiple model evaluations

---

## 3. Privacy Attacks

### 3.1 Extracting Training Data from Large Language Models
**Citation:** Carlini, Tramèr, Wallace et al. (2021). USENIX Security

**Contributions:**
- First demonstration of training data extraction from GPT-2
- Extracted PII (names, phone numbers, emails), code, UUIDs
- Showed larger models are more vulnerable

**Methods:**
- Generate text via sampling
- Filter for memorized sequences using likelihood ratio

**Limitations:**
- Focused on autoregressive models
- Extraction rate depends on memorization

---

### 3.2 Scalable Extraction of Training Data from (Production) Language Models
**Citation:** Nasr, Carlini et al. (2023). arXiv:2311.17035

**Contributions:**
- Demonstrated extraction from production models (ChatGPT)
- "Divergence attack" causes aligned models to emit training data
- 150x higher extraction rate than normal prompting
- Extracted gigabytes of data from open/closed models

**Methods:**
- Prompts that cause model to diverge from alignment
- "Repeat this word forever" attack on ChatGPT

**Limitations:**
- Some attacks patched after disclosure
- Extraction efficiency varies by model

**Future Work:**
- Defenses against divergence attacks
- Understanding alignment's role in memorization

---

### 3.3 Membership Inference Attacks on Large Language Models
**Citation:** Various (2023-2024). arXiv:2402.07841, NeurIPS 2024

**Contributions:**
- Question whether MIAs work on pre-trained LLMs
- SPV-MIA: Self-prompt calibration raises AUC from 0.7 to 0.9
- PETAL: Label-only attack achieves 0.67 AUC on GPT-3.5-Turbo

**Methods:**
- Reference-free vs. reference-based attacks
- Loss-based membership scoring
- Self-prompt calibration for fine-tuned models

**Limitations:**
- Pre-training at scale (single epoch, huge datasets) reduces MIA efficacy
- In/out member distributions very similar

**Future Work:**
- Attacks on fine-tuned models (higher success rate)
- Combining MIA with extraction attacks

---

### 3.4 Beyond Memorization: Violating Privacy via Inference
**Citation:** Staab et al. (2024). ICLR 2024. arXiv:2310.07298

**Contributions:**
- Shows LLMs can infer personal attributes (location, income, sex)
- 85% top-1 accuracy, 95% top-3 accuracy
- 100x cheaper and 240x faster than human inference

**Methods:**
- Prompt LLMs with text samples
- Measure inference accuracy across attribute types

**Limitations:**
- Existing mitigations (anonymization, alignment) insufficient

**Future Work:**
- Defenses against inference attacks
- Understanding what enables inference capability

---

### 3.5 Prompt Injection and Data Exfiltration
**Citation:** OWASP Top 10 for LLM (2023-2025), Greshake et al. (2023). arXiv:2302.12173

**Contributions:**
- Taxonomy of indirect prompt injection attacks
- Data exfiltration via HTML images, tool calls
- Real incidents: ChatGPT memory exploit (2024), Slack AI attack (2024)

**Methods:**
- Hidden prompts in external content
- Markdown image exfiltration
- RAG poisoning (PoisonedRAG: 90% success with 5 malicious docs)

**Limitations:**
- No complete defense exists
- RAG and fine-tuning don't mitigate

---

## 4. Machine Unlearning

### 4.1 Machine Unlearning of Pre-trained Large Language Models
**Citation:** ACL 2024. aclanthology.org/2024.acl-long.457

**Contributions:**
- Methods for unlearning from pre-trained (not just fine-tuned) LLMs
- 10^5x more efficient than retraining

**Methods:**
- Gradient ascent on forget set
- Integration with gradient descent on retain set

**Limitations:**
- Gradient ascent degrades model quality
- Unlearning verification is challenging

---

### 4.2 Rethinking Machine Unlearning for Large Language Models
**Citation:** Nature Machine Intelligence (2025)

**Contributions:**
- Critical analysis of current unlearning methods
- Shows surface-level suppression leaves underlying representations intact

**Methods:**
- Adversarial probing of "unlearned" models
- Red-teaming evaluations

**Limitations:**
- Current methods don't achieve true unlearning
- Vulnerable to adversarial attacks

---

### 4.3 A Survey of Machine Unlearning in LLMs
**Citation:** arXiv:2503.01854 (2025), Springer (2025)

**Contributions:**
- Comprehensive taxonomy of unlearning methods
- Identifies key challenges: black-box models, adversarial vulnerability, efficiency

**Methods:**
- Gradient ascent
- Relabeling-based fine-tuning
- Self-distillation (key token identification)

**Limitations:**
- Most methods merely suppress surface expression
- Harry Potter study showed semantic traces remain

**Future Work:**
- Verifiable unlearning
- Unlearning for black-box models

---

### 4.4 TOFU Benchmark
**Citation:** 2024

**Contributions:**
- First benchmark for LLM unlearning evaluation
- Fake author profiles for controlled experiments

**Methods:**
- Fine-tune on synthetic data, then unlearn
- Measure retention vs. forgetting

---

### 4.5 Towards Safer LLMs through Machine Unlearning
**Citation:** ACL Findings 2024

**Contributions:**
- Unlearning for safety (removing harmful capabilities)
- Connection to alignment

---

## 5. Privacy Auditing and Measurement

### 5.1 Privacy Auditing of Large Language Models
**Citation:** arXiv:2503.06808 (2025)

**Contributions:**
- First nontrivial privacy audit without shadow models
- Achieves 49.6% TPR at 1% FPR (vs. prior 4.2%)
- Provides provable lower bound on ε (audit of ε≈1 for theoretical ε=4)

**Methods:**
- Novel canary design for LLM training
- Improved membership inference for auditing

**Limitations:**
- Gap between theoretical and empirical ε remains

**Future Work:**
- Tighter auditing methods
- Real-time auditing during training

---

### 5.2 PrivAuditor Benchmark
**Citation:** NeurIPS 2024

**Contributions:**
- Comprehensive benchmark for privacy in LLM adaptation
- Covers multiple architectures and fine-tuning methods

**Methods:**
- Standardized evaluation across attack types
- Multiple adaptation scenarios

---

### 5.3 Epsilon*: Privacy Metric for Machine Learning Models
**Citation:** arXiv:2307.11280 (2023)

**Contributions:**
- Empirical privacy metric independent of training
- DP training reduces Epsilon* by up to 800%

**Methods:**
- Membership inference-based measurement
- Privacy-utility visualization

**Limitations:**
- Empirical metric, not formal guarantee

---

## 6. Synthetic Data Generation

### 6.1 Protecting Users with DP Synthetic Training Data (Google)
**Citation:** Google Research Blog (2024)

**Contributions:**
- DP fine-tuning + parameter-efficient methods = high-quality synthetic data
- Key finding: PEFT significantly improves DP synthetic data quality

**Methods:**
- DP-SGD fine-tuning
- Sample from fine-tuned model

**Limitations:**
- Requires access to model weights

---

### 6.2 Aug-PE: DP Synthetic Text via Foundation Model APIs
**Citation:** Tang et al. (2024). arXiv:2403.01749, ICLR 2024

**Contributions:**
- API-only approach (no training needed)
- Works with GPT-3.5, LLaMA, Mixtral
- 65.7x speedup vs. DP fine-tuning

**Methods:**
- Prompt with sensitive examples
- Aggregate predictions with DP noise

**Limitations:**
- Depends on API model quality
- Privacy accounting for API access

---

### 6.3 SafeSynthDP
**Citation:** arXiv:2412.20641 (2024)

**Contributions:**
- Framework for DP synthetic data via LLMs
- Compares Laplace vs. Gaussian noise mechanisms

**Methods:**
- DP-based noise injection during generation

---

### 6.4 DP-LLMTGen: DP Tabular Data Synthesis
**Citation:** arXiv:2406.01457 (2024)

**Contributions:**
- Two-stage fine-tuning for tabular data
- Novel loss function for structure preservation

---

### 6.5 Gretel GPT
**Citation:** Gretel AI (2024)

**Contributions:**
- Industrial DP synthetic text system
- Downstream accuracy within 1% of non-private models at ε=8

**Methods:**
- DP-SGD + QLoRA
- Accelerated training techniques

---

## 7. Privacy-Preserving Inference

### 7.1 SIGMA: GPU-Accelerated MPC for LLM Inference
**Citation:** 2024

**Contributions:**
- Function secret sharing for non-linearities
- 12-19x latency improvement
- LLaMA2-13B in 38 seconds, GPT-2 in 1.5 seconds

**Methods:**
- FSS for Softmax, GeLU, SiLU
- GPU acceleration

**Limitations:**
- Still significant overhead vs. plaintext inference

---

### 7.2 CipherGPT: Secure Two-Party GPT Inference
**Citation:** 2024

**Contributions:**
- 6.2x speedup in secure matrix multiplication
- 4.1x bandwidth savings

**Methods:**
- Novel secure multiplication protocol
- Optimized for Transformer architecture

---

### 7.3 PUMA: Secure LLaMA-7B Inference
**Citation:** arXiv:2307.12533 (2023)

**Contributions:**
- LLaMA-7B inference in 5 minutes
- Practical MPC for large models

---

### 7.4 Split-and-Denoise: Local DP for LLM Inference
**Citation:** ICML 2024

**Contributions:**
- Split learning with local DP
- No need for trusted server

**Methods:**
- Add noise at client before sending to server
- Denoise at inference

---

### 7.5 PrivacyRestore: Privacy Removal and Restoration
**Citation:** arXiv:2406.01394 (2024)

**Contributions:**
- Remove sensitive info before inference, restore after
- Practical privacy-preserving inference

---

## 8. PII Detection and Protection

### 8.1 Analyzing Leakage of PII in Language Models
**Citation:** Lukas et al. (2023). IEEE S&P 2023

**Contributions:**
- Game-based definitions for PII leakage
- Three attack types: extraction, inference, reconstruction
- Novel attacks extract 10x more PII than prior work
- Sentence-level DP still leaks ~3% of PII

**Methods:**
- Black-box API attacks
- Named entity recognition for PII identification

**Limitations:**
- DP reduces but doesn't eliminate PII leakage

---

### 8.2 ProPILE: Probing Privacy Leakage in LLMs
**Citation:** Kim et al. (2023). NeurIPS 2023

**Contributions:**
- Tool for data subjects to probe their own PII leakage
- Applied to OPT-1.3B on Pile dataset

**Methods:**
- User-generated prompts based on own PII
- Measure response sensitivity

---

### 8.3 PII-Scope: Benchmark for PII Leakage Assessment
**Citation:** arXiv:2410.06704 (2024)

**Contributions:**
- First comprehensive PII extraction benchmark
- Included in TrustLLM and DecodingTrust

**Methods:**
- Standardized PII extraction evaluation
- Multiple attack scenarios

---

### 8.4 DeMem: Dememorization via Unlearning
**Citation:** EMNLP 2023

**Contributions:**
- Uses PPO to unlearn pre-training data
- Negative similarity reward signal

**Methods:**
- RL-based fine-tuning for paraphrasing policy

---

## 9. Regulatory and Compliance

### 9.1 Right to Be Forgotten in the Era of LLMs
**Citation:** arXiv:2307.03941 (2023)

**Contributions:**
- Analysis of GDPR Art. 17 applicability to LLMs
- Technical challenges of erasure from model weights

**Key Issues:**
- Personal data in LLMs can never be truly erased
- Machine unlearning as approximation to erasure
- SISA (Sharded, Isolated, Sliced, Aggregated) enables localized retraining

---

### 9.2 LLMs as Personal Data (Legal Analysis)
**Citation:** arXiv:2503.01630 (2025)

**Contributions:**
- Legal argument that LLMs may constitute personal data
- Implications for data subject rights

---

### 9.3 GDPR vs. EU AI Act Tension
**Citation:** Various (2024-2025)

**Key Issues:**
- GDPR mandates erasure; AI Act requires documentation retention
- Conflicting regulatory requirements
- Need for reconciliation mechanisms

---

### 9.4 Enforcement Actions
- **OpenAI (Italy, Dec 2024):** €15M fine for GDPR breaches
- **Clearview AI (France):** €20M (2022), €5.2M (2023)

---

## 10. Industry Practices

### 10.1 OpenAI Privacy Practices
- Consumer ChatGPT: Training on prompts by default (opt-out available)
- Enterprise/API: No training on customer data
- August 2025: Reversed some privacy protections

---

### 10.2 Anthropic Privacy Practices
- Claude consumer: No training without explicit opt-in
- 30-day deletion after conversation deletion
- Constitutional AI + ISO 42001 certification

---

### 10.3 Google Privacy Practices
- Gemini: Prompts linked to accounts, 72-hour retention minimum
- Flagged content: Up to 3-year retention for review
- Enterprise: Contractual guarantees against training

---

### 10.4 Stanford Research on Chatbot Privacy
**Citation:** Stanford HAI (2025)

**Findings:**
- Six leading US companies use inputs for training
- 8.5% of prompts contain sensitive information
- Existing systems don't flag most exposures

---

## 11. DP Safety Benefits Beyond Privacy

### 11.1 VaultGemma: Differentially Private LLM from Scratch
**Citation:** Google Research (2025). [Blog](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)

**Contributions:**
- Largest open model (1B parameters) trained from scratch with DP
- Achieves (ε ≤ 2.0, δ ≤ 1.1e−10) at sequence level
- **No detectable memorization** when prompted with 50-token training prefixes
- New scaling laws for DP training

**Methods:**
- Gemma 2 architecture with 26 layers, Multi-Query Attention
- Poisson sampling instead of uniform batches (reduces noise requirements)
- Sequence length limited to 1,024 tokens

**Safety Implications:**
- Demonstrates DP prevents memorization of potentially harmful training content
- Privacy-by-design approach applicable to sensitive domains (healthcare, finance)

**Limitations:**
- Performance comparable to GPT-2 (5 years older) — quantifies privacy cost
- High computational requirements

---

### 11.2 Does Differential Privacy Prevent Backdoor Attacks in Practice?
**Citation:** arXiv:2311.06227 (2023)

**Contributions:**
- Empirical study of DP-SGD and PATE against backdoor/poisoning attacks
- PATE effective due to bagging structure of teacher models
- Introduces Label-DP as faster alternative

**Key Findings:**
- DP can prevent backdoor attacks, but **effectiveness depends on hyperparameters**
- Number of backdoors in training data impacts DP success
- Proper tuning can make DP more effective than specialized backdoor defenses

**Safety Implications:**
- DP limits influence of any single sample → limits poison sample influence
- Potential dual-use: privacy protection + poisoning defense

**Limitations:**
- Not a silver bullet; requires careful configuration
- Trade-off between privacy strength and attack resistance

---

### 11.3 Why Does Large Epsilon DP Defend Against Practical MIAs?
**Citation:** arXiv:2402.09540 (2024)

**Contributions:**
- Explains why ε ≥ 7 (theoretically vacuous) still works in practice
- Introduces Practical Membership Privacy (PMP) framework
- Bridges gap between theoretical guarantees and empirical defense

**Key Findings:**
- Real attackers lack worst-case dataset knowledge
- Large ε translates to much smaller PMP parameter
- Provides principled guidance for ε selection

**Safety Implications:**
- Industrial deployments with large ε still provide meaningful protection
- Practical security even without strong theoretical guarantees

---

### 11.4 Defending Against Attacks in Deep Learning with DP: A Survey
**Citation:** Artificial Intelligence Review (2025). [Springer](https://link.springer.com/article/10.1007/s10462-025-11350-3)

**Contributions:**
- Comprehensive survey of DP for security beyond privacy
- Documents DP's role in fairness, robustness, and overfitting prevention

**Key Findings on Safety Benefits:**

1. **Reduces Overfitting:**
   - DP noise prevents models from memorizing individual data points
   - Improves generalization to unseen data
   - Clear dependence of membership advantage on generalization error

2. **Defends Against Multiple Attack Types:**
   - Membership inference attacks
   - Attribute inference attacks
   - Model inversion attacks
   - Data poisoning (with proper configuration)

3. **Fairness Implications (Mixed):**
   - Can reduce bias by preventing outliers from dominating
   - BUT can exacerbate unfairness for underrepresented groups ("poor get poorer")
   - Mitigation: FairDP algorithms, Counterfactual Data Augmentation

**Limitations:**
- DP can amplify bias in LLM fine-tuning
- Underrepresented groups suffer worse privacy/utility trade-offs

---

### 11.5 DP for Backdoor Defense in Federated Learning
**Citation:** Various (2024-2025). CMES, ScienceDirect

**Contributions:**
- DP mechanisms limit single sample influence during updates
- When properly tuned, reduces backdoor success rates

**Methods:**
- DP-SGD with out-of-distribution detection
- Adaptive sample-splitting to isolate poisoned examples

**Limitations:**
- Significant degradation in benign task performance
- Ongoing research to balance defense and utility

---

### 11.6 DP and Machine Unlearning for Safety
**Citation:** Various surveys (2024-2025)

**Contributions:**
- DP methods used to isolate target data during training
- Enables post-hoc privacy and safety improvements
- Applications: model detoxification, jailbreaking defense, copyright protection

**Key Insight:**
- Traditional unlearning categories include DP-based approaches
- DP provides formal framework for limiting data influence

**Limitations:**
- DP alone doesn't achieve true unlearning
- Complements but doesn't replace dedicated unlearning methods

---

### 11.7 De-amplifying Bias from DP in LLM Fine-tuning
**Citation:** arXiv:2402.04489 (2024)

**Contributions:**
- Documents that DP amplifies gender, racial, and religious bias in LLM fine-tuning
- Identifies cause: disparity in gradient convergence across sub-groups
- Proposes Counterfactual Data Augmentation (CDA) as mitigation

**Safety Implications:**
- DP alone may harm fairness — requires additional interventions
- CDA can mitigate bias amplification

---

## Key Observations Across Literature

1. **DP-Utility Trade-off Persists:** Strong privacy (ε<1) typically degrades utility significantly
2. **Parameter-Efficient Methods Help:** LoRA, adapters reduce noise needed for DP
3. **Pre-training Scale Protects:** Single-epoch training on massive data naturally resists some attacks
4. **Semantic Privacy Understudied:** Inference attacks may be more dangerous than memorization
5. **Unlearning is Incomplete:** Current methods suppress surface behavior but leave traces
6. **Regulatory Uncertainty:** GDPR erasure requirements unclear for neural networks
7. **DP Has Safety Benefits Beyond Privacy:** Reduces overfitting, defends against backdoors/poisoning, limits memorization of harmful content
8. **DP-Fairness Tension:** DP can exacerbate bias for underrepresented groups; requires mitigation strategies

---

*Last updated: 2025-01-31*
