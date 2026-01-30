# Review Paper Outline: Privacy in Large Language Models

**Working Title:** *Privacy in Large Language Models: From Differential Privacy to Practical Defenses*

**Scope:** Comprehensive review of privacy challenges, formal mechanisms (emphasis on differential privacy), attacks, and emerging solutions for LLMs (2022-2025)

---

## Abstract (Target: 250 words)

- Motivation: LLMs trained on massive datasets containing sensitive information
- Gap: Tension between model capability and privacy protection
- Contribution: Systematize privacy threats, evaluate DP mechanisms, identify research gaps
- Key findings preview

---

## 1. Introduction

### 1.1 Motivation
- LLMs as critical infrastructure (ChatGPT: 100M+ users)
- Training data includes personal, sensitive, proprietary information
- Demonstrated extraction of PII, memorized content

### 1.2 The Privacy Challenge
- Scale: Trillions of tokens from web scrapes
- Capability: Larger models = more memorization
- Deployment: API access enables attacks without model access

### 1.3 Scope and Contributions
- Focus: Differential privacy applications (primary), attacks, defenses
- Exclusions: Federated learning
- Contributions:
  1. Taxonomy of privacy threats
  2. Systematic review of DP mechanisms for LLMs
  3. Analysis of privacy-utility trade-offs
  4. Identification of open problems

### 1.4 Paper Organization
- Section 2: Background
- Section 3: Privacy Threats
- Section 4: Differential Privacy Mechanisms
- Section 5: Other Defenses
- Section 6: Evaluation and Auditing
- Section 7: Open Challenges
- Section 8: Conclusion

---

## 2. Background

### 2.1 Large Language Model Fundamentals
- Transformer architecture (brief)
- Pre-training and fine-tuning paradigm
- Emergence of instruction-tuned and aligned models

### 2.2 Privacy Definitions and Threat Models

#### 2.2.1 What is "Privacy" for LLMs?
- Verbatim memorization
- Semantic leakage
- Inference of attributes
- Membership disclosure

#### 2.2.2 Threat Models
```
Adversary Capabilities:
├── Black-box (API access only)
├── Gray-box (some model info)
└── White-box (full model access)

Adversary Goals:
├── Extract training data
├── Infer membership
├── Infer attributes
└── Reconstruct sensitive records
```

### 2.3 Differential Privacy Primer
- (ε, δ)-Differential Privacy definition
- Key properties: composition, post-processing
- Rényi Differential Privacy (RDP)
- DP-SGD: Clipping and noise addition

---

## 3. Privacy Threats and Attacks

### 3.1 Memorization in LLMs
- Quantifying memorization
- Factors affecting memorization (scale, duplication, position)
- Verbatim vs. approximate memorization

### 3.2 Training Data Extraction

#### 3.2.1 Early Work (2021)
- Carlini et al.: GPT-2 extraction

#### 3.2.2 Scalable Extraction (2023)
- Divergence attacks on ChatGPT
- Production model vulnerabilities

#### 3.2.3 Defense Evasion
- Alignment doesn't prevent extraction
- Style-transfer circumvents verbatim filters

**Table: Extraction Attack Summary**
| Attack | Target | Access | Key Finding |
|--------|--------|--------|-------------|
| Carlini 2021 | GPT-2 | API | PII extractable |
| Nasr 2023 | ChatGPT | API | Gigabytes extracted |

### 3.3 Membership Inference Attacks

#### 3.3.1 Challenges for LLMs
- Single-epoch training limits signal
- Massive datasets blur in/out distinction

#### 3.3.2 Attack Methods
- Loss-based attacks
- Reference-based calibration
- Self-prompt calibration (SPV-MIA)
- Label-only attacks (PETAL)

### 3.4 Inference Attacks Beyond Memorization
- Personal attribute inference
- 85% accuracy on demographics
- Implications: Privacy violation without memorization

### 3.5 Prompt Injection and Data Exfiltration
- Indirect prompt injection
- RAG poisoning
- Tool-based exfiltration

---

## 4. Differential Privacy for LLMs

### 4.1 DP-SGD for Language Models

#### 4.1.1 Mechanism Overview
- Per-example gradient clipping
- Gaussian noise addition
- Privacy accounting

#### 4.1.2 Challenges for LLMs
- Memory overhead
- Computational cost
- Hyperparameter sensitivity

### 4.2 Privacy Unit Selection

#### 4.2.1 Example-Level DP
- Standard formulation
- Protects individual training examples

#### 4.2.2 User-Level DP
- Protects all contributions from one user
- More appropriate for real deployments
- Novel accountants for tight bounds

### 4.3 Parameter-Efficient DP Training

#### 4.3.1 Why PEFT Helps DP
- Fewer parameters = lower noise requirement
- Gradient norms reduced
- Pre-trained knowledge preserved

#### 4.3.2 DP-LoRA
- Low-rank adaptation with DP
- Results: 89% accuracy at ε=6 (MNLI)

#### 4.3.3 Variants
- FFA-LoRA: Freeze random matrices
- DP-SFT: Subspace-targeted noise

### 4.4 Memory-Efficient DP Methods

#### 4.4.1 DP-ZO (Zeroth-Order)
- Only privatize scalar step size
- No gradient storage required
- <16GB memory for long sequences

#### 4.4.2 FlashDP
- Optimized DP-SGD implementation
- Scalability improvements

### 4.5 DP at Inference Time

#### 4.5.1 PMixED
- Mix predictions with DP noise
- No training-time DP required

#### 4.5.2 Output Perturbation
- Add noise to generated outputs
- Local DP formulations

### 4.6 Privacy-Utility Trade-offs

**Figure: Privacy-Utility Frontier**
```
Utility
  ↑
  │     ╭─── Non-private baseline
  │    ╱
  │   ╱  DP-LoRA (ε=6)
  │  ╱
  │ ╱   Full DP-SGD (ε=1)
  │╱
  └──────────────────────► Privacy (1/ε)
```

**Table: Representative Results**
| Method | Task | ε | Δ Accuracy |
|--------|------|---|------------|
| DP-SGD | Classification | 8 | -5% |
| DP-LoRA | MNLI | 6 | -1.2% |
| DP-ZO | Generation | 4 | -10% |

---

## 5. Other Privacy Defenses

### 5.1 Machine Unlearning

#### 5.1.1 Methods
- Gradient ascent on forget set
- Relabeling-based fine-tuning
- Self-distillation

#### 5.1.2 Limitations
- Surface-level suppression only
- Semantic traces remain
- Verification challenges

#### 5.1.3 TOFU Benchmark
- Standardized evaluation

### 5.2 Training Data Curation

#### 5.2.1 Deduplication
- Reduce memorization of repeated content

#### 5.2.2 PII Scrubbing
- Pre-training data filtering
- Limitations: Incomplete coverage

### 5.3 Output Filtering
- Post-generation PII detection
- Easily circumvented

### 5.4 Alignment and Safety Training
- RLHF doesn't prevent memorization
- Divergence attacks bypass alignment

### 5.5 Privacy-Preserving Inference

#### 5.5.1 Cryptographic Methods
- MPC: SIGMA, CipherGPT, PUMA
- Current overhead: 100-1000x

#### 5.5.2 Split Learning
- Client-side computation
- PrivacyRestore: Remove and restore

---

## 6. Evaluation and Auditing

### 6.1 Privacy Auditing Methods

#### 6.1.1 Canary-Based Auditing
- Insert known sequences
- Measure extraction success

#### 6.1.2 Membership Inference Auditing
- Convert attack success to ε lower bound

#### 6.1.3 State of the Art
- 49.6% TPR at 1% FPR (2025)
- First nontrivial audit without shadow models

### 6.2 The Audit Gap
- Theoretical ε vs. empirical ε
- Typical gap: 2-4x

### 6.3 Benchmarks

#### 6.3.1 PrivAuditor
- Comprehensive adaptation scenarios

#### 6.3.2 PII-Scope
- PII extraction benchmark

#### 6.3.3 TOFU
- Unlearning evaluation

---

## 7. DP Synthetic Data Generation

### 7.1 DP Fine-tuning for Synthesis
- Train with DP-SGD, sample from model
- PEFT significantly improves quality

### 7.2 API-Based Methods (Aug-PE)
- No training required
- 65.7x speedup
- Works with proprietary models

### 7.3 Industrial Applications
- Gretel: ε=8, within 1% utility
- Healthcare, finance use cases

---

## 8. Regulatory and Compliance

### 8.1 GDPR Implications
- Right to erasure (Art. 17)
- Technical impossibility for neural networks
- Machine unlearning as approximation

### 8.2 EU AI Act
- Documentation requirements
- Tension with GDPR erasure

### 8.3 Enforcement Landscape
- OpenAI €15M fine (Italy, 2024)
- Evolving regulatory interpretation

---

## 9. Open Challenges and Future Directions

### 9.1 Fundamental Challenges

1. **Privacy-Utility Frontier**
   - Can we achieve ε<1 with acceptable utility?
   - What is the fundamental limit?

2. **Pre-training Privacy**
   - DP for trillion-token training
   - Distributed DP across data sources

3. **Semantic Privacy**
   - Formalizing inference-based threats
   - Defenses against attribute inference

### 9.2 Technical Gaps

1. **Efficient DP at Scale**
   - Memory-efficient per-example gradients
   - Hardware acceleration

2. **Verifiable Unlearning**
   - Certification that data is truly forgotten
   - Adversarial robustness

3. **Real-Time Privacy Auditing**
   - Continuous monitoring during training
   - Early warning systems

### 9.3 Deployment Challenges

1. **Standardization**
   - Agreed-upon privacy metrics
   - Certification frameworks

2. **Regulatory Clarity**
   - What constitutes compliance?
   - Technical safe harbors

### 9.4 Emerging Threats

1. **Agent Privacy**
   - Tool-enabled exfiltration
   - Multi-step attack chains

2. **Multimodal Privacy**
   - Image + text inference attacks
   - Cross-modal leakage

---

## 10. Conclusion

### Key Takeaways
1. Privacy threats are diverse and evolving
2. DP remains only formally guaranteed defense
3. PEFT + DP significantly improves trade-offs
4. Current unlearning is incomplete
5. Regulation outpacing technical solutions

### Call to Action
- More research on semantic privacy
- Standardized auditing protocols
- Industry adoption of DP practices
- Regulatory guidance for neural networks

---

## References

*(Organize by section, ~100 references for full paper)*

### Key Citations by Theme

**Surveys:**
- Yan et al. (2024) - LLM privacy survey
- Yao et al. (2023) - Attacks and defenses

**Differential Privacy:**
- Yu et al. (2022) - DP fine-tuning
- Levy et al. (2024) - User-level DP
- Malladi et al. (2024) - DP-ZO

**Attacks:**
- Carlini et al. (2021) - Training data extraction
- Nasr et al. (2023) - Scalable extraction
- Staab et al. (2024) - Inference attacks

**Unlearning:**
- Eldan & Russinovich (2023) - Harry Potter
- TOFU benchmark (2024)

**Auditing:**
- Privacy auditing of LLMs (2025)
- PrivAuditor (NeurIPS 2024)

---

## Appendices

### A. Differential Privacy Definitions
- (ε, δ)-DP formal definition
- RDP definition and conversion
- Composition theorems

### B. Attack Success Metrics
- TPR at fixed FPR
- AUC-ROC
- Extraction rate

### C. Benchmark Details
- Dataset specifications
- Evaluation protocols

---

*Outline version: 1.0 | Last updated: 2025-01-30*
