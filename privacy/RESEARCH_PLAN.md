# Research Plan: Privacy in LLMs

## Project Overview

**Goal**: Create a comprehensive but concise report on the current state of privacy in LLMs, with a strong focus on applications of differential privacy.

**Scope**: Privacy broadly, including:
- Differential privacy (primary focus)
- Privacy attacks (membership inference, data extraction, etc.)
- Machine unlearning
- Memorization and its implications
- Privacy-preserving training/inference techniques

**Out of Scope**: Federated learning (excluded per user request)

**Recency**: Focus on works from 2022 onwards

**Depth**: Wide net approach (~25-30 sources)

---

## Phase 1: Research Sources

### Academic Sources
| Source | Categories/Focus | Search Method |
|--------|-----------------|---------------|
| arXiv | cs.CR, cs.LG, cs.CL | Keyword search + recent submissions |
| Google Scholar | Highly-cited papers | Citation tracking |
| Semantic Scholar | Related work graphs | Paper recommendations |

### Blogs & Technical Writing
| Source | Type |
|--------|------|
| LessWrong / AI Alignment Forum | Community perspectives, alignment-focused privacy |
| OpenAI Blog | Industry practices, GPT privacy measures |
| Google AI Blog | DP research, privacy-preserving ML |
| Anthropic | Constitutional AI, safety perspectives |
| The Gradient | Technical summaries |

### Conferences to Check
- NeurIPS 2022-2024
- ICML 2022-2024
- ICLR 2022-2024
- ACL/EMNLP 2022-2024
- USENIX Security / IEEE S&P (security venues)

---

## Phase 2: Search Terms

### Differential Privacy (Primary Focus)
- "differential privacy LLM"
- "DP-SGD language models"
- "private fine-tuning transformers"
- "epsilon bounds large language models"
- "differential privacy text generation"
- "DP-Adam" / "DP optimizers"
- "privacy budget language models"
- "Renyi differential privacy NLP"

### Privacy Attacks
- "membership inference attack LLM"
- "training data extraction language models"
- "memorization neural networks"
- "prompt injection data leakage"
- "model inversion attacks transformers"
- "attribute inference LLM"

### Machine Unlearning
- "machine unlearning LLM"
- "forget requests language models"
- "GDPR right to be forgotten ML"
- "selective forgetting neural networks"

### General Privacy
- "privacy preserving language models"
- "PII leakage LLM"
- "data privacy generative AI"
- "privacy risks foundation models"

---

## Phase 3: Deliverables

### File Structure
```
privacy/
├── RESEARCH_PLAN.md          # This file
├── research_summaries.md     # Per-resource summaries
├── thematic_synthesis.md     # Findings grouped by theme
├── review_outline.md         # Review paper-style outline
└── bibliography.md           # Full citations (optional)
```

### Summary Format (for research_summaries.md)
For each resource, capture:
1. **Citation**: Authors, title, venue, year
2. **Contributions**: Key novel contributions
3. **Methods**: Technical approach
4. **Limitations**: Acknowledged or apparent limitations
5. **Future Work**: Suggested directions

### Thematic Categories (preliminary)
1. Differential Privacy Mechanisms for LLMs
2. Privacy Attacks and Vulnerabilities
3. Memorization and Extraction
4. Machine Unlearning
5. Privacy Auditing and Measurement
6. Industry Practices and Deployments
7. Theoretical Foundations and Guarantees

---

## Phase 4: Synthesis Approach

1. **First pass**: Collect and summarize individual sources
2. **Second pass**: Identify recurring themes, conflicts, and gaps
3. **Third pass**: Organize into review paper structure with:
   - Problem taxonomy
   - Method comparisons
   - Open challenges
   - Future directions

---

## Visualization Options

To view markdown files with nice formatting:

1. **VS Code**: Open file → Cmd+Shift+V (or Ctrl+Shift+V) for preview
2. **Obsidian**: Free app, excellent for interlinked markdown
3. **Browser Extensions**: "Markdown Viewer" for Chrome/Firefox
4. **Convert to HTML**: `npx marked -i file.md -o file.html` then open in browser
5. **GitHub**: Push to repo, view rendered markdown on github.com
6. **MacDown**: Free macOS markdown editor with live preview

---

## Notes for Future Agents

If picking up this work:
1. Check `research_summaries.md` for completed source reviews
2. The user wants breadth (~25-30 sources) over extreme depth
3. Differential privacy applications are the PRIMARY focus
4. Exclude federated learning entirely
5. Include privacy attacks and machine unlearning as secondary topics
6. Keep final report concise despite comprehensive research
7. All work should be from 2022 or later

---

## Status

- [x] Plan created and approved
- [ ] Research collection (Phase 1-2)
- [ ] Individual summaries (research_summaries.md)
- [ ] Thematic synthesis (thematic_synthesis.md)
- [ ] Review outline (review_outline.md)
