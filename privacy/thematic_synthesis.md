# Thematic Synthesis: Privacy in LLMs

*Synthesized from 30+ sources (2022-2025)*

---

## Overview of Themes

| Theme | Maturity | Key Tension |
|-------|----------|-------------|
| Differential Privacy Mechanisms | Medium-High | Privacy vs. Utility |
| Privacy Attacks | High | Attack sophistication vs. Defense efficacy |
| Memorization & Extraction | High | Model capability vs. Data leakage |
| Machine Unlearning | Low-Medium | Efficiency vs. Completeness |
| Privacy Auditing | Low | Theoretical vs. Empirical guarantees |
| Inference-Time Privacy | Low | Latency vs. Protection |
| Regulatory Compliance | Emerging | Legal requirements vs. Technical feasibility |

---

## Theme 1: Differential Privacy Mechanisms for LLMs

### Current State
Differential privacy has emerged as the primary formal privacy framework for LLM training. The field has progressed from basic DP-SGD applications to sophisticated, LLM-specific optimizations.

### Key Developments

**1. Evolution of DP Training:**
```
2021: Basic DP-SGD for language models
2022: First billion-parameter DP fine-tuning (Yu et al.)
2023: Memory-efficient DP-ZO (zeroth-order optimization)
2024: DP + LoRA/PEFT combinations
2025: Subspace-targeted DP, user-level DP maturation
```

**2. Privacy Unit Debate:**
- **Example-level DP:** Protects individual training examples
- **User-level DP:** Protects all contributions from a single user
- Emerging consensus: User-level more appropriate for real deployments, but harder to implement

**3. Parameter-Efficient + DP Synergy:**
- Reducing trainable parameters reduces required noise
- LoRA + DP achieves 89% accuracy on MNLI at ε=6 (only 1.2% drop from non-private)
- FFA-LoRA: Freeze random matrices to further reduce noise

### Recurring Challenges

1. **Privacy-Utility Trade-off:** Strong privacy (ε<1) typically causes significant utility loss
2. **Computational Overhead:** Per-example gradients expensive to compute
3. **Memory Requirements:** Standard DP-SGD requires storing per-example gradients
4. **Hyperparameter Sensitivity:** DP training more sensitive to learning rate, batch size

### Promising Directions

- **Zeroth-order methods (DP-ZO):** Only privatize scalar step sizes; memory-efficient
- **Subspace methods (DP-SFT):** Inject noise only into task-relevant dimensions
- **Pre-trained model leverage:** Larger pre-trained models achieve better privacy-utility curves

### Open Questions

1. What is the minimum ε achievable for practical LLM applications?
2. How should privacy budgets be allocated across pre-training vs. fine-tuning?
3. Can we achieve meaningful DP guarantees during pre-training at scale?

---

## Theme 2: Privacy Attacks and Vulnerabilities

### Attack Taxonomy

```
Privacy Attacks on LLMs
├── Training Data Extraction
│   ├── Verbatim memorization attacks
│   ├── Divergence attacks (bypass alignment)
│   └── Prefix-based extraction
├── Membership Inference
│   ├── Loss-based attacks
│   ├── Reference-based attacks
│   └── Label-only attacks (PETAL)
├── Attribute Inference
│   └── Inferring demographics, location, etc.
├── Model Extraction
│   └── Stealing embeddings/weights via API
└── Prompt Injection
    ├── Direct injection
    └── Indirect injection (RAG poisoning)
```

### Key Findings

**Training Data Extraction:**
- Carlini et al. (2021): Extracted PII from GPT-2
- Nasr et al. (2023): Extracted gigabytes from ChatGPT via "divergence attacks"
- "Repeat this word forever" attack: 150x higher extraction rate than normal
- Alignment does NOT prevent memorization

**Membership Inference:**
- Traditional MIAs less effective on pre-trained LLMs (single epoch, massive data)
- Fine-tuned models much more vulnerable
- SPV-MIA achieves 0.9 AUC on fine-tuned models
- PETAL achieves 0.67 AUC on GPT-3.5-Turbo (label-only, API access)

**Beyond Memorization (Inference Attacks):**
- LLMs can infer personal attributes from text at inference time
- 85% accuracy inferring location, income, sex
- 100x cheaper than human inference
- Anonymization and alignment insufficient defenses

### Defense Landscape

| Defense | Effectiveness | Limitations |
|---------|--------------|-------------|
| Differential Privacy | High (formal) | Utility cost |
| Output filtering | Low | Circumventable |
| Alignment/RLHF | Low | Divergence attacks bypass |
| Deduplication | Medium | Doesn't prevent all memorization |
| Rate limiting | Low | Slows but doesn't prevent |

### Synthesis

The attack surface is expanding faster than defenses. Key insight: **semantic/inference attacks may be more dangerous than memorization attacks**, yet receive less attention. Formal privacy guarantees (DP) remain the only robust defense, but at significant utility cost.

---

## Theme 3: Memorization Dynamics

### What We Know

1. **Scale increases memorization:** Larger models memorize more training data
2. **Duplication amplifies risk:** Repeated sequences memorized preferentially
3. **Position matters:** Data at sentence beginnings more extractable
4. **Single-epoch training helps:** Pre-training practices naturally limit some memorization

### Memorization vs. Generalization

```
                    Low DP noise ─────────────────► High DP noise
                         │                              │
High utility ◄───────────┤                              ├──────────► Low utility
                         │                              │
High memorization ◄──────┤                              ├────► Low memorization
                         │                              │
                  Privacy risk ────────────────► Privacy protection
```

### Mitigations

1. **Goldfish Loss:** Exclude random token subset from loss computation
2. **Deduplication:** Remove repeated sequences from training data
3. **DP Training:** Formal guarantee against memorization
4. **DeMem:** Reinforcement learning for dememorization

### Key Insight

Memorization is **not binary**—it exists on a spectrum from verbatim reproduction to semantic retention. Current defenses focus on verbatim memorization, but semantic leakage remains largely unaddressed.

---

## Theme 4: Machine Unlearning

### The Promise vs. Reality

**Promise:** Efficiently remove specific data's influence without full retraining

**Reality:** Current methods achieve **surface-level suppression**, not true forgetting

### Method Categories

| Method | Approach | Limitation |
|--------|----------|------------|
| Gradient Ascent | Maximize loss on forget set | Degrades model quality |
| Relabeling | Fine-tune on neutral responses | Traces remain |
| Self-distillation | Target key tokens | Incomplete removal |
| SISA | Sharded training | Requires specific training setup |

### Critical Finding: Harry Potter Study

Eldan & Russinovich (2023) attempted to remove Harry Potter knowledge:
- Surface prompts failed (success)
- Deeper semantic probes still triggered knowledge (failure)
- **Implication:** Current unlearning is "make model pretend to forget," not true erasure

### Verification Challenge

How do we know data is truly unlearned?
- No agreed-upon verification standard
- Adversarial probing reveals hidden retention
- Membership inference on "unlearned" data often still works

### Connection to Regulation

GDPR Article 17 (Right to Erasure) creates legal pressure, but:
- Technical impossibility of true erasure from neural networks
- Regulatory guidance unclear
- Machine unlearning as "best effort" approximation

---

## Theme 5: Privacy Auditing and Measurement

### The Audit Gap

**Theoretical guarantee:** "We trained with ε=4"
**Empirical audit:** "Our audit shows effective ε≈1"
**Gap:** 4x difference between claimed and verified privacy

### State of the Art (2025)

Privacy auditing of LLMs now achieves:
- 49.6% TPR at 1% FPR (vs. prior 4.2%)
- Provable lower bounds on ε
- No shadow models or gradient access required

### Auditing Methods

1. **Canary insertion:** Plant known sequences, measure extractability
2. **Membership inference:** Measure distinguishability of training data
3. **Empirical ε estimation:** Convert attack success to privacy leakage

### Challenges

1. Auditing requires access during/after training
2. Black-box auditing much harder
3. Audit results depend on attack sophistication
4. No standardized auditing protocol

### Emerging: PrivAuditor Benchmark

NeurIPS 2024 introduced comprehensive privacy benchmarking:
- Multiple architectures
- Multiple fine-tuning methods
- Standardized attack evaluation

---

## Theme 6: Synthetic Data as Privacy Preservation

### The Pipeline

```
Sensitive Data → DP Fine-tune LLM → Generate Synthetic → Train on Synthetic
                       │                    │
                   ε guarantee         Downstream model
                       │                    │
                 Privacy preserved    Utility preserved
```

### Key Insight: PEFT + DP = Better Synthetic Data

Parameter-efficient fine-tuning dramatically improves DP synthetic data quality because:
- Fewer parameters → lower gradient norms → less noise needed
- Pre-trained knowledge preserved
- Task adaptation with minimal perturbation

### Approaches

| Approach | Requires Training | Model Access |
|----------|-------------------|--------------|
| DP fine-tuning | Yes | Weights |
| Aug-PE | No | API only |
| Inference-time DP | No | API only |

### Aug-PE Breakthrough

- 65.7x speedup vs. DP fine-tuning
- Works with proprietary models (GPT-3.5)
- No training compute required

### Industry Adoption

Gretel AI: Production DP synthetic text
- ε=8 achieves within 1% of non-private utility
- Finance, healthcare, customer support applications

---

## Theme 7: Privacy-Preserving Inference

### The Challenge

Inference privacy requires protecting:
1. User queries (input privacy)
2. Model responses (output privacy)
3. Intermediate computations

### Techniques

```
Inference Privacy
├── Cryptographic
│   ├── Homomorphic Encryption (FHE)
│   ├── Secure Multi-Party Computation (MPC)
│   └── Function Secret Sharing (FSS)
├── Trusted Execution
│   └── TEEs (SGX, TrustZone)
└── Differential Privacy
    ├── Local DP (split-and-denoise)
    └── Output perturbation
```

### Performance Reality (2024-2025)

| System | Model | Latency |
|--------|-------|---------|
| SIGMA | GPT-2 | 1.5 sec |
| SIGMA | LLaMA2-13B | 38 sec |
| PUMA | LLaMA-7B | 5 min |
| Plaintext | LLaMA-7B | <1 sec |

**Gap:** 100-1000x slowdown for cryptographic protection

### Practical Alternatives

1. **Split learning:** Client holds first layers locally
2. **PrivacyRestore:** Remove PII before sending, restore after
3. **Local DP:** Add noise client-side

---

## Theme 8: Regulatory Landscape

### Key Regulations

| Regulation | Privacy Requirement | LLM Challenge |
|------------|---------------------|---------------|
| GDPR Art. 17 | Right to erasure | Cannot truly erase from weights |
| GDPR Art. 15 | Right to access | Cannot enumerate what model "knows" |
| GDPR Art. 22 | Explanation of decisions | LLM reasoning opaque |
| EU AI Act | Documentation retention | Conflicts with GDPR erasure |

### Enforcement Actions

- **OpenAI (Italy, 2024):** €15M fine for transparency, legal basis, hallucination issues
- **Clearview AI:** €25M+ cumulative fines in Europe

### The Core Tension

```
GDPR: "Delete data after purpose fulfilled"
      ↕ CONFLICT ↕
AI Act: "Retain documentation for system lifecycle"
```

### Emerging Interpretations

Hamburg DPA suggestion: LLMs don't "store" personal data in traditional sense, so erasure applies only to inputs/outputs, not weights. **Not yet settled law.**

---

## Cross-Cutting Insights

### 1. The DP Adoption Barrier

Despite being the only formally guaranteed defense, DP adoption remains limited because:
- Utility cost too high for competitive models
- Implementation complexity
- Lack of standardized tooling
- Unclear regulatory requirement for formal privacy

### 2. Attack-Defense Arms Race

Attacks are advancing faster than defenses:
- Semantic inference attacks largely undefended
- Alignment provides false sense of security
- Prompt injection enables new exfiltration vectors

### 3. The Verification Problem

How do we know privacy claims are true?
- Self-reported ε values not verified
- Privacy auditing nascent
- No industry standard for privacy certification

### 4. Pre-training vs. Fine-tuning Asymmetry

- Pre-training: Massive scale provides some natural protection
- Fine-tuning: Much higher attack success rates, DP more critical

### 5. Emerging Threat: Agent Privacy

As LLMs become agents with tools:
- New exfiltration vectors (tool calls, file access)
- Indirect prompt injection more dangerous
- Privacy boundaries harder to define

---

## Maturity Assessment

| Area | Research Maturity | Production Readiness |
|------|-------------------|---------------------|
| DP for fine-tuning | High | Medium |
| DP for pre-training | Medium | Low |
| Privacy attacks | High | N/A (offense) |
| Machine unlearning | Medium | Low |
| Privacy auditing | Low-Medium | Low |
| Secure inference | Medium | Low |
| Regulatory compliance | Emerging | Low |

---

*Synthesis completed: 2025-01-30*
