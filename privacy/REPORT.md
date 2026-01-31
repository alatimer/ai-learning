# Privacy in Large Language Models: From Differential Privacy to Practical Defenses

*A Comprehensive Review (2022-2025)*

---

## Abstract

Large Language Models (LLMs) have become critical infrastructure, with systems like ChatGPT serving over 100 million users. However, their training on massive internet-scraped datasets creates fundamental privacy tensions: the same scale that enables capability also enables memorization and leakage of sensitive information. This report systematizes privacy threats facing LLMs, evaluates defense mechanisms with emphasis on differential privacy (DP), and identifies open research challenges. We find that: (1) privacy attacks are advancing faster than defenses, with semantic inference attacks posing underappreciated risks; (2) differential privacy remains the only formally guaranteed defense, though utility costs persist; (3) parameter-efficient fine-tuning dramatically improves DP trade-offs, with DP-LoRA achieving 89% accuracy at ε=6; (4) current machine unlearning achieves surface-level suppression but not true forgetting; and (5) regulatory requirements like GDPR's right to erasure remain technically unachievable for neural networks. We conclude with research priorities including semantic privacy formalization, efficient DP at pre-training scale, and verifiable unlearning.

---

## 1. Introduction

### 1.1 The Privacy Challenge

LLMs are trained on trillions of tokens scraped from the internet, inevitably including personal information, private communications, and proprietary content. This creates a fundamental tension: the memorization that enables impressive capabilities also enables privacy violations.

The scale of the problem is significant:
- **Training data**: GPT-4 class models train on datasets exceeding 1 trillion tokens
- **User exposure**: ChatGPT alone has 100M+ weekly active users sharing prompts
- **Attack surface**: API access enables extraction attacks without model access

Research has demonstrated concrete privacy failures. Carlini et al. (2021) extracted verbatim training data from GPT-2, including names, phone numbers, and email addresses. Nasr et al. (2023) scaled this to production systems, extracting gigabytes of training data from ChatGPT using "divergence attacks" that cause aligned models to emit memorized content at 150x the normal rate.

### 1.2 Scope and Contributions

This report provides:
1. **Taxonomy of privacy threats** across the LLM lifecycle
2. **Systematic review of DP mechanisms** with quantitative comparisons
3. **Analysis of privacy-utility trade-offs** with specific ε values and accuracy impacts
4. **Identification of open problems** and research priorities

We focus on differential privacy applications as the primary formal defense, while covering attacks, machine unlearning, and privacy-preserving inference. We exclude federated learning per scope constraints.

---

## 2. Background

### 2.1 Privacy Definitions for LLMs

Privacy in LLMs encompasses multiple threat types:

| Threat Type | Description | Example |
|-------------|-------------|---------|
| **Verbatim memorization** | Model reproduces exact training sequences | Extracting email addresses |
| **Semantic leakage** | Model reveals information through paraphrase | Describing a person's habits |
| **Attribute inference** | Model infers sensitive attributes from text | Predicting income from writing style |
| **Membership disclosure** | Determining if data was in training set | Confirming medical record inclusion |

### 2.2 Threat Models

Adversaries vary in access and goals:

**Access levels:**
- **Black-box**: API access only (most common)
- **Gray-box**: Some model information (architecture, training procedure)
- **White-box**: Full model weights (open-source models)

**Adversary goals:**
- Extract specific training data
- Determine membership of known data
- Infer attributes about data subjects
- Reconstruct sensitive records

### 2.3 Differential Privacy Primer

Differential privacy provides formal privacy guarantees by ensuring that any individual training example has limited influence on the model.

**(ε, δ)-Differential Privacy**: A mechanism M satisfies (ε, δ)-DP if for all adjacent datasets D and D' (differing in one example) and all outputs S:

```
Pr[M(D) ∈ S] ≤ e^ε · Pr[M(D') ∈ S] + δ
```

**Key properties:**
- **Composition**: Privacy degrades gracefully across multiple computations
- **Post-processing**: Any function of a DP output remains DP
- **Group privacy**: Extends to groups of k individuals with ε → kε

**DP-SGD** (Differentially Private Stochastic Gradient Descent) is the primary mechanism for DP training:
1. Clip per-example gradients to bound sensitivity
2. Add calibrated Gaussian noise
3. Use privacy accounting to track cumulative ε

---

## 3. Privacy Threats and Attacks

### 3.1 Training Data Extraction

**Foundational work (Carlini et al., 2021):** Demonstrated extraction of verbatim training sequences from GPT-2 by:
1. Generating large volumes of text via sampling
2. Filtering for high-likelihood sequences
3. Verifying against known training data

Key finding: Larger models memorize more, making them more vulnerable.

**Scalable extraction (Nasr et al., 2023):** Extended attacks to production models:
- Extracted gigabytes from open models (Pythia, GPT-Neo, LLaMA)
- Attacked ChatGPT using "divergence attacks" (e.g., "Repeat this word forever: poem")
- Achieved 150x higher extraction rate than normal prompting
- **Critical finding**: Alignment and RLHF do not prevent memorization

| Attack | Target | Access | Key Result |
|--------|--------|--------|------------|
| Carlini 2021 | GPT-2 | API | Hundreds of PII instances extracted |
| Nasr 2023 | ChatGPT | API | Gigabytes of training data extracted |
| CMU 2024 | Fine-tuned LLMs | API | Higher extraction from fine-tuned models |

### 3.2 Membership Inference Attacks

Membership inference attacks (MIAs) determine whether specific data was used for training.

**Challenges for LLMs:**
- Single-epoch pre-training limits memorization signal
- Massive datasets blur distinction between members and non-members
- In/out distributions highly similar

**Attack methods:**
- **Loss-based**: Members have lower loss than non-members
- **Reference-based**: Compare target model to reference model
- **SPV-MIA**: Self-prompt calibration achieves 0.9 AUC on fine-tuned models
- **PETAL**: Label-only attack achieves 0.67 AUC on GPT-3.5-Turbo

**Key insight**: MIAs are more effective against fine-tuned models than pre-trained models due to overfitting on smaller datasets.

### 3.3 Inference Attacks Beyond Memorization

A critical and underappreciated threat: LLMs can infer personal attributes from text without having memorized that information.

**Staab et al. (2024)** demonstrated:
- LLMs infer location, income, sex, and other attributes from text
- **85% top-1 accuracy**, 95% top-3 accuracy
- 100x cheaper and 240x faster than human inference
- Existing mitigations (anonymization, alignment) are insufficient

This represents a fundamental shift: **privacy violations can occur without any memorization**, purely through the model's inference capabilities applied to user-provided text.

### 3.4 Prompt Injection and Data Exfiltration

LLM agents with tool access create new attack surfaces:

**Indirect prompt injection:** Malicious instructions hidden in external content (websites, documents) manipulate model behavior.

**Data exfiltration methods:**
- HTML/Markdown images with attacker-controlled URLs
- Tool calls to external services
- RAG poisoning (PoisonedRAG: 90% success with just 5 malicious documents)

**Real incidents (2024):**
- ChatGPT memory exploit: Persistent injection across sessions
- Slack AI vulnerability: RAG poisoning + social engineering
- Copy-paste injection: Hidden prompts in copied text

---

## 4. Differential Privacy for LLMs

### 4.1 DP-SGD for Language Models

DP-SGD adapts standard training with two modifications:
1. **Gradient clipping**: Bound each example's gradient norm to C
2. **Noise addition**: Add Gaussian noise calibrated to C and target ε

**Challenges for LLMs:**
- **Memory**: Per-example gradients require O(batch_size × model_size) memory
- **Computation**: Clipping each gradient individually is expensive
- **Sensitivity**: DP training more sensitive to hyperparameters

### 4.2 Privacy Unit Selection

**Example-level DP** protects individual training examples—the standard formulation.

**User-level DP** protects all contributions from a single user, more appropriate for real deployments where users contribute multiple examples.

Levy et al. (2024) compared approaches:
- Example-level sampling (ELS) with per-example clipping
- User-level sampling (ULS) with per-user clipping
- Finding: ULS generally better when users have diverse examples

### 4.3 Parameter-Efficient DP Training

A key insight: **reducing trainable parameters reduces required noise**.

**Why PEFT helps DP:**
- Fewer parameters → lower gradient dimensionality → lower noise magnitude
- Pre-trained knowledge preserved (not perturbed by noise)
- Faster convergence reduces privacy budget consumption

**DP-LoRA** combines Low-Rank Adaptation with differential privacy:
- Only train low-rank matrices A and B
- Apply DP-SGD to adapter parameters only
- **Result**: 89% accuracy on MNLI at ε=6 (only 1.2% drop from non-private)

**Variants:**
- **FFA-LoRA**: Freeze randomly initialized A matrix, train only B → halves communication and noise
- **DP-SFT**: Identify task-specific subspace, inject noise only there

### 4.4 Memory-Efficient Methods

**DP-ZO (Zeroth-Order Optimization):**
- Estimates gradients via finite differences (no backpropagation)
- Only the scalar step size needs privatization
- Memory: <16GB even with sequence length 2048
- Trade-off: More forward passes required

**FlashDP:**
- Optimized DP-SGD implementation
- Efficient per-example gradient computation
- Enables DP training at foundation model scale

### 4.5 DP at Inference Time

**PMixED:** Provides DP for a private corpus during inference by mixing predictions from multiple models with DP aggregation. No training-time DP required.

**Output perturbation:** Add calibrated noise to generated outputs. Simpler but provides weaker guarantees.

### 4.6 Privacy-Utility Trade-offs

The fundamental challenge: stronger privacy (lower ε) degrades utility.

| Method | Task | ε | δ | Accuracy | Δ vs Non-Private |
|--------|------|---|---|----------|------------------|
| DP-SGD (full) | SST-2 | 8 | 10⁻⁵ | 91% | -5% |
| DP-LoRA | MNLI | 6 | 10⁻⁵ | 89% | -1.2% |
| DP-ZO | Generation | 4 | 10⁻⁵ | — | -10% (perplexity) |
| Gretel GPT | Synthetic text | 8 | 10⁻⁵ | — | -1% (downstream) |

**Key observations:**
- ε < 1 typically causes significant utility loss (>10%)
- PEFT methods (LoRA) dramatically improve trade-offs
- Larger pre-trained models achieve better privacy-utility curves
- ε ∈ [3, 8] represents a practical operating range

### 4.7 DP Safety Benefits Beyond Privacy

An emerging research area reveals that differential privacy provides **safety benefits beyond its original privacy purpose**.

#### 4.7.1 Preventing Harmful Memorization

DP's core mechanism—limiting any single sample's influence—prevents memorization of all training content, not just private data. This has safety implications:

**VaultGemma (Google, 2025):**
- 1B parameter model trained from scratch with DP (ε ≤ 2.0)
- Shows **no detectable memorization** when prompted with 50-token training prefixes
- Demonstrates that DP-trained models cannot reproduce harmful training content
- Performance comparable to GPT-2, quantifying the privacy/safety cost

#### 4.7.2 Defense Against Backdoor and Poisoning Attacks

DP-SGD limits the influence of any single training sample, which naturally bounds the impact of poisoned samples:

| Defense | Mechanism | Effectiveness |
|---------|-----------|---------------|
| DP-SGD | Gradient clipping + noise | Reduces backdoor success (hyperparameter-dependent) |
| PATE | Bagging of teacher models | Effective due to ensemble structure |
| Label-DP | Noise on labels only | Faster, but weaker guarantees |

**Key finding:** DP can prevent backdoor attacks in practice, but effectiveness depends critically on hyperparameter tuning. It is not automatic protection.

#### 4.7.3 Robustness and Generalization

DP noise provides regularization benefits:
- Prevents overfitting to individual training examples
- Improves generalization to unseen data
- Clear dependence: membership attack success correlates with generalization error

#### 4.7.4 Why Large Epsilon Still Provides Protection

A practical finding: even ε ≥ 7 (theoretically weak privacy) defends against real membership inference attacks.

**Explanation (Practical Membership Privacy framework):**
- Theoretical DP assumes worst-case attackers with complete dataset knowledge
- Real attackers lack this knowledge
- Large ε translates to much smaller "practical" privacy leakage
- Industrial deployments with ε ∈ [7, 10] still provide meaningful protection

#### 4.7.5 The Fairness Cost

DP has a critical downside: it can **amplify bias** against underrepresented groups.

**The "Poor Get Poorer" Effect:**
- Underrepresented groups suffer worse privacy/utility trade-offs
- DP amplifies gender, racial, and religious bias in LLM fine-tuning
- Cause: disparity in gradient convergence across sub-groups

**Mitigations:**
- Counterfactual Data Augmentation (CDA) during fine-tuning
- FairDP algorithms with group-aware noise calibration
- Post-processing repair algorithms
- Careful hyperparameter selection per subgroup

| Safety Goal | DP Helps? | Notes |
|-------------|-----------|-------|
| Prevent harmful memorization | Yes | Core mechanism applies |
| Defend against poisoning | Partially | Requires proper tuning |
| Improve model robustness | Yes | Regularization effect |
| Ensure fairness | Mixed | Can help or hurt |

---

## 5. Other Privacy Defenses

### 5.1 Machine Unlearning

Machine unlearning aims to remove specific data's influence without full retraining.

**Methods:**
- **Gradient ascent**: Maximize loss on forget set (degrades model quality)
- **Relabeling**: Fine-tune on neutral substitutes for sensitive content
- **Self-distillation**: Identify and target key tokens (named entities, nouns)

**Critical limitation**: Current methods achieve surface-level suppression, not true forgetting.

The **Harry Potter study** (Eldan & Russinovich, 2023) illustrates this:
- Attempted to remove Harry Potter knowledge from an LLM
- Surface prompts about Harry Potter failed (apparent success)
- Deeper semantic probes still triggered the knowledge (actual failure)
- **Implication**: Unlearning makes models "pretend to forget"

**TOFU Benchmark** provides standardized evaluation using synthetic author profiles.

### 5.2 Training Data Curation

**Deduplication** reduces memorization of repeated content but doesn't prevent it entirely.

**PII scrubbing** filters sensitive data before training but suffers from incomplete coverage—novel PII patterns evade detection.

### 5.3 Output Filtering

Post-generation PII detection can block some leakage but is easily circumvented via:
- Paraphrasing requests
- Encoding schemes
- Multi-turn extraction

### 5.4 Alignment Limitations

RLHF and instruction tuning do **not** prevent memorization:
- Models still store training data in weights
- Alignment merely discourages reproduction in normal operation
- Divergence attacks bypass alignment entirely

### 5.5 Privacy-Preserving Inference

**Cryptographic methods** (MPC, HE) enable computation on encrypted data:

| System | Model | Latency | Overhead vs Plaintext |
|--------|-------|---------|----------------------|
| SIGMA | GPT-2 | 1.5 sec | ~100x |
| SIGMA | LLaMA2-13B | 38 sec | ~500x |
| PUMA | LLaMA-7B | 5 min | ~1000x |

Current overhead makes cryptographic inference impractical for most applications.

**Split learning** alternatives:
- Client computes first layers locally
- Only intermediate representations sent to server
- PrivacyRestore: Remove PII before sending, restore after

---

## 6. Evaluation and Auditing

### 6.1 Privacy Auditing Methods

**Canary-based auditing:**
1. Insert known "canary" sequences into training data
2. Train model
3. Measure extraction success for canaries
4. Convert to empirical privacy estimate

**Membership inference auditing:**
- Use MIA success rate to lower-bound privacy leakage
- Convert TPR/FPR to empirical ε

**State of the art (2025):**
- 49.6% TPR at 1% FPR (vs. prior 4.2%)
- First nontrivial audit without shadow models or gradient access
- Achieves audit of ε ≈ 1 for model trained with theoretical ε = 4

### 6.2 The Audit Gap

A persistent finding: **empirical privacy is better than theoretical guarantees suggest**.

| Theoretical ε | Empirical ε (audited) | Gap |
|---------------|----------------------|-----|
| 8 | ~3 | 2.7x |
| 4 | ~1 | 4x |
| 1 | <0.5 | 2x |

This gap arises because:
- DP analysis is worst-case
- Actual data distributions are more benign
- Attack efficiency below theoretical maximum

### 6.3 Benchmarks

**PrivAuditor** (NeurIPS 2024): Comprehensive benchmark across architectures and fine-tuning methods.

**PII-Scope**: First comprehensive PII extraction benchmark, included in TrustLLM and DecodingTrust.

**TOFU**: Unlearning evaluation using synthetic author profiles.

---

## 7. DP Synthetic Data Generation

### 7.1 The Pipeline

```
Sensitive Data → DP Fine-tune LLM → Generate Synthetic → Use Synthetic Downstream
                      │                    │
                  ε guarantee         Provably private
```

**Key finding** (Google Research): PEFT + DP dramatically improves synthetic data quality because fewer parameters means less noise.

### 7.2 API-Based Methods

**Aug-PE** (ICLR 2024) enables DP synthetic generation via API access:
- Prompt LLM with sensitive examples
- Aggregate predictions with DP noise
- **No training required**
- 65.7x speedup vs. DP fine-tuning
- Works with proprietary models (GPT-3.5, Claude)

### 7.3 Industrial Applications

**Gretel AI** offers production DP synthetic text:
- ε = 8 achieves within 1% of non-private downstream accuracy
- Applications in healthcare, finance, customer support
- Uses DP-SGD + QLoRA for efficient training

---

## 8. Regulatory Landscape

### 8.1 GDPR Implications

**Article 17 (Right to Erasure)** creates fundamental tensions:
- Requires deletion of personal data upon request
- **Technical impossibility**: Cannot truly erase from neural network weights
- Machine unlearning positioned as "best effort" approximation

**Hamburg DPA suggestion**: LLMs don't "store" personal data traditionally; erasure applies to inputs/outputs, not weights. **Not settled law.**

### 8.2 EU AI Act Tensions

The AI Act requires documentation retention for system lifecycle, conflicting with GDPR erasure:
- GDPR: Delete when purpose fulfilled
- AI Act: Retain for accountability
- No clear reconciliation mechanism

### 8.3 Enforcement

| Entity | Fine | Violation |
|--------|------|-----------|
| OpenAI (Italy, 2024) | €15M | Transparency, legal basis, hallucination |
| Clearview AI (France) | €25M+ | Biometric data without consent |

---

## 9. Open Challenges and Future Directions

### 9.1 Fundamental Challenges

**Privacy-Utility Frontier:**
- Can we achieve ε < 1 with acceptable utility?
- What are fundamental limits for LLM privacy?
- How should privacy budgets be allocated across training stages?

**Pre-training Privacy:**
- DP for trillion-token training remains unsolved
- Current methods focus on fine-tuning only
- Need distributed DP across data sources

**Semantic Privacy:**
- Formalizing inference-based threats
- Defenses against attribute inference (not just memorization)
- Currently no formal framework exists

### 9.2 Technical Gaps

**Efficient DP at Scale:**
- Memory-efficient per-example gradients
- Hardware acceleration for DP operations
- Better privacy accounting (tighter bounds)

**Verifiable Unlearning:**
- Certification that data is truly forgotten
- Adversarial robustness of unlearning
- Formal guarantees beyond empirical testing

**Real-Time Auditing:**
- Continuous monitoring during training
- Early warning for memorization
- Automated privacy budget tracking

### 9.3 Emerging Threats

**Agent Privacy:**
- LLM agents with tool access create new exfiltration vectors
- Multi-step attack chains harder to defend
- Privacy boundaries harder to define

**Multimodal Privacy:**
- Image + text enables new inference attacks
- Cross-modal leakage (visual revealing textual)
- Underexplored attack surface

---

## 10. Conclusion

### Key Takeaways

1. **Privacy threats are diverse and evolving.** Beyond memorization, inference attacks pose underappreciated risks—LLMs can violate privacy without having memorized any sensitive data.

2. **Differential privacy remains the only formally guaranteed defense.** Despite utility costs, DP provides mathematical bounds on information leakage that no other approach matches.

3. **PEFT + DP is a breakthrough combination.** Parameter-efficient fine-tuning reduces noise requirements, making practical privacy achievable: DP-LoRA achieves 89% accuracy at ε=6.

4. **DP provides safety benefits beyond privacy.** The same mechanisms that prevent privacy leakage also prevent memorization of harmful content, defend against poisoning attacks, and improve model robustness. VaultGemma demonstrates that DP-trained models show no detectable memorization of any training content.

5. **Current unlearning is incomplete.** Methods suppress surface behavior but leave semantic traces. Verification remains an open problem.

6. **DP can harm fairness.** The "poor get poorer" effect means underrepresented groups suffer worse privacy/utility trade-offs. Mitigations like Counterfactual Data Augmentation are essential.

7. **Regulation is outpacing technical solutions.** GDPR's right to erasure is technically unachievable; enforcement actions are increasing without clear technical compliance paths.

### Research Priorities

1. **Semantic privacy formalization**: Extend DP-style guarantees to inference-based threats
2. **Efficient DP at scale**: Enable privacy-preserving pre-training, not just fine-tuning
3. **Verifiable unlearning**: Develop certification mechanisms for data removal
4. **Standardized auditing**: Establish industry protocols for privacy verification
5. **DP-fairness co-optimization**: Develop methods that provide privacy without amplifying bias
6. **DP for safety**: Explore whether DP can be tuned to specifically prevent harmful capabilities while preserving useful ones

### Final Observation

The privacy landscape for LLMs is characterized by a fundamental asymmetry: attacks require only API access and modest compute, while defenses require architectural changes, training modifications, and significant utility trade-offs. Closing this gap—through better DP mechanisms, verified unlearning, and formal semantic privacy—represents one of the defining challenges for trustworthy AI deployment.

---

## References

### Surveys
- Miranda et al. (2025). Preserving Privacy in Large Language Models. *TMLR*.
- Yan et al. (2024). On Protecting the Data Privacy of LLMs. *arXiv:2403.05156*.
- Shanmugarasa et al. (2025). SoK: The Privacy Paradox of LLMs. *ACM AsiaCCS*.

### Differential Privacy
- Yu et al. (2022). Privately Fine-Tuning LLMs with DP. *arXiv:2210.15042*.
- Levy et al. (2024). User-Level DP for LLM Fine-Tuning. *arXiv:2407.07737*.
- Malladi et al. (2024). Private Fine-tuning with Zeroth-order Optimization. *arXiv:2401.04343*.

### Attacks
- Carlini et al. (2021). Extracting Training Data from LLMs. *USENIX Security*.
- Nasr et al. (2023). Scalable Extraction from Production LLMs. *arXiv:2311.17035*.
- Staab et al. (2024). Beyond Memorization: Privacy via Inference. *ICLR*.

### Unlearning
- Geng et al. (2025). Machine Unlearning Techniques for LLMs. *arXiv:2503.01854*.
- Eldan & Russinovich (2023). Who's Harry Potter? *arXiv*.

### Auditing
- Privacy Auditing of LLMs (2025). *arXiv:2503.06808*.
- PrivAuditor (2024). *NeurIPS*.

### Synthetic Data
- Tang et al. (2024). DP Synthetic Data via Foundation Model APIs. *ICLR*.
- Google Research (2024). Protecting Users with DP Synthetic Data. *Blog*.

### DP Safety Benefits
- Google Research (2025). VaultGemma: The World's Most Capable Differentially Private LLM. *Blog*.
- Does Differential Privacy Prevent Backdoor Attacks in Practice? (2023). *arXiv:2311.06227*.
- Why Does Large Epsilon DP Defend Against Practical MIAs? (2024). *arXiv:2402.09540*.
- De-amplifying Bias from DP in LLM Fine-tuning (2024). *arXiv:2402.04489*.
- Defending Against Attacks in Deep Learning with DP: A Survey (2025). *Artificial Intelligence Review*.

---

*Report completed: 2025-01-31*
