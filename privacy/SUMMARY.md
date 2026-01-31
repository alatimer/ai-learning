# Summary: Privacy in LLMs Research

*Comprehensive review with focus on differential privacy applications (2022-2025)*

---

## Deliverables

| File | Description |
|------|-------------|
| `research_summaries.md` | 50+ papers summarized with contributions, methods, limitations, future work |
| `thematic_synthesis.md` | 9 cross-cutting themes with maturity assessments |
| `review_outline.md` | Full 10-section review paper outline |
| `bibliography.md` | 88 organized references with URLs |
| `existing_surveys_review.md` | Review of 15 existing surveys (2024-2025) |
| `REPORT.md` | Full synthesized report |
| `RESEARCH_PLAN.md` | Research plan and completion status |

---

## Key Findings

### 1. Differential Privacy is the Only Formal Defense
- DP-SGD remains the gold standard for privacy guarantees
- However, utility cost is significant: ε<1 typically degrades performance substantially
- Pre-training with DP at scale remains largely unsolved

### 2. PEFT + DP Synergy
- Parameter-efficient fine-tuning (LoRA, adapters) dramatically reduces noise requirements
- DP-LoRA achieves 89% accuracy on MNLI at ε=6 (only 1.2% drop from non-private)
- Key insight: fewer trainable parameters = lower gradient norms = less noise needed

### 3. Attacks Outpacing Defenses
- Training data extraction: Carlini et al. extracted gigabytes from ChatGPT via "divergence attacks"
- Semantic inference attacks achieve 85% accuracy inferring demographics from text
- Alignment/RLHF does NOT prevent memorization or extraction
- Prompt injection enables new exfiltration vectors (RAG poisoning, tool calls)

### 4. Machine Unlearning is Incomplete
- Current methods achieve surface-level suppression, not true forgetting
- Harry Potter study: semantic traces remain after "unlearning"
- Verification of unlearning remains an open problem
- TOFU benchmark provides first standardized evaluation

### 5. Privacy Auditing is Nascent
- Gap between theoretical ε and empirical ε can be 2-4x
- 2025 work achieves first nontrivial audit without shadow models (49.6% TPR at 1% FPR)
- No industry standard for privacy certification exists

### 6. Regulatory Uncertainty
- GDPR Article 17 (right to erasure) technically impossible for neural networks
- EU AI Act documentation requirements conflict with GDPR erasure
- OpenAI fined €15M in Italy (2024) for GDPR violations
- Machine unlearning positioned as "best effort" approximation

### 7. DP Has Safety Benefits Beyond Privacy
- **Prevents harmful memorization**: VaultGemma (Google, 2025) shows no detectable memorization at ε≤2.0
- **Defends against poisoning**: DP limits influence of any single sample, including poison samples
- **Improves robustness**: DP noise acts as regularization, reducing overfitting
- **Large ε still works**: Even ε≥7 defends against practical membership inference attacks
- **Fairness concern**: DP can amplify bias against underrepresented groups ("poor get poorer")
- **Mitigation**: Counterfactual Data Augmentation (CDA) can reduce DP-induced bias

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
| DP for safety/anti-memorization | Medium | Low |
| DP-fairness co-optimization | Low | Very Low |

---

## Open Challenges

1. **Privacy-Utility Frontier**: Can we achieve ε<1 with acceptable utility?
2. **Pre-training Privacy**: DP for trillion-token training remains unsolved
3. **Semantic Privacy**: Formalizing and defending against inference attacks
4. **Verifiable Unlearning**: Certification that data is truly forgotten
5. **Agent Privacy**: Tool-enabled exfiltration in LLM agents
6. **DP-Fairness Balance**: Achieving privacy without amplifying bias
7. **DP for Targeted Safety**: Can DP prevent harmful capabilities while preserving useful ones?

---

## How to View These Files

**Easiest options:**

1. **VS Code**: Open any `.md` file, press `Cmd+Shift+V` for rendered preview

2. **Browser** (no install needed):
   ```bash
   npx marked research_summaries.md -o research_summaries.html && open research_summaries.html
   ```

3. **GitHub**: Push to a repo and view rendered markdown at github.com

4. **Obsidian** (free app): Open the `privacy/` folder as a vault for interlinked viewing

5. **MacDown** (free macOS app): Double-click any `.md` file for side-by-side editing/preview

---

*Research completed: 2025-01-31*
