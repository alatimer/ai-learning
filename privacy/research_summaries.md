# Research Summaries: Privacy in LLMs

*Focus: Differential Privacy Applications | Scope: 2022-2025*

This document provides narrative summaries of the key papers in LLM privacy research, organized thematically. For each paper, I include my assessment of its significance and novelty.

---

## 1. Surveys and Overviews

### On Protecting the Data Privacy of Large Language Models: A Survey

Yan et al. (2024)
[https://arxiv.org/abs/2403.05156](https://arxiv.org/abs/2403.05156)

This survey provides a comprehensive taxonomy of data privacy threats in LLMs, distinguishing between passive privacy leakage (where information escapes unintentionally during normal operation) and active privacy attacks (where adversaries deliberately attempt extraction). The authors organize their analysis around the LLM lifecycle, examining threats at pre-training, fine-tuning, and inference stages separately. They review protection mechanisms available at each stage and identify gaps where defenses remain inadequate.

The main limitation is one shared by all surveys in fast-moving fields: by the time of publication, new developments have already emerged. The authors also acknowledge that they provide limited empirical comparison of defense effectiveness, instead relying on the original papers' reported results. They point toward multi-modal LLMs and scalable privacy-preserving training as important future directions.

**My take:** This is a solid entry point for researchers new to the field. The lifecycle-based organization is intuitive and practical. However, the survey doesn't offer particularly novel insights beyond what you'd get from reading the primary literature carefully. I'd rate it as useful but not essential.

---

### Privacy in Large Language Models: Attacks, Defenses and Future Directions

Yao et al. (2023)
[https://arxiv.org/abs/2310.10383](https://arxiv.org/abs/2310.10383)

This survey takes a threat-model-centric approach, categorizing privacy attacks according to the adversary's assumed capabilities rather than the stage of the LLM lifecycle. The authors provide a comprehensive overview of defense strategies and identify emerging privacy concerns as LLMs continue to evolve. Their framework distinguishes between black-box attacks (API access only), gray-box attacks (some model information available), and white-box attacks (full model access).

The focus is primarily on text modality, which limits applicability to increasingly common multi-modal systems. Some of the defenses reviewed lack rigorous privacy guarantees, which the authors acknowledge. Future directions include multi-modal privacy research and privacy in LLM agents that can use tools.

**My take:** The adversary-centric organization is genuinely useful for practitioners trying to understand what they're defending against. This is more actionable than the lifecycle-based surveys for someone building defenses. The recent update covering multi-modality makes it more current than many alternatives.

---

### SoK: Semantic Privacy in Large Language Models

arXiv:2506.23603 (2025)
[https://arxiv.org/abs/2506.23603](https://arxiv.org/abs/2506.23603)

This systematization of knowledge addresses a critical gap: most privacy research focuses on verbatim memorization (can the model reproduce exact training sequences?), but this paper examines semantic privacy—whether models can reveal information through paraphrase or inference without reproducing anything verbatim. The authors develop a framework for understanding inference-based privacy violations and analyze existing mitigation approaches through this lens.

The main challenge they identify is definitional: semantic privacy is inherently harder to define and measure than syntactic privacy. When does inference cross the line from "the model is smart" to "the model is violating privacy"? This remains philosophically murky.

**My take:** This is one of the most intellectually interesting papers in the collection. The insight that current defenses target the wrong threat model (verbatim reproduction when semantic leakage is the real risk) is important and underappreciated. I think this direction will become increasingly central as models become more capable.

---

### Privacy Issues in Large Language Models: A Survey (Technical Report)

Neel et al. (2023)

Seth Neel's technical report takes a more practical and industry-focused perspective on privacy risks. Rather than organizing around academic threat taxonomies, it discusses regulatory implications directly and considers what privacy risks actually matter for deployed systems.

**My take:** This is a good complement to the more academic surveys. If you're building a product and need to understand privacy risks, this is more directly applicable than the arxiv surveys.

---

## 2. Differential Privacy for LLM Training and Fine-tuning

### Privately Fine-Tuning Large Language Models with Differential Privacy

Yu et al. (2022)
[https://arxiv.org/abs/2210.15042](https://arxiv.org/abs/2210.15042)

This paper represents the first systematic study of differentially private fine-tuning for billion-parameter language models. The key finding is counterintuitive: larger pre-trained models actually achieve better privacy-utility trade-offs than smaller ones. This happens because larger models start with more knowledge already embedded, so they need less adaptation (and thus less noisy gradient updates) to achieve good performance on downstream tasks.

The authors use DP-SGD with gradient clipping and Gaussian noise addition, evaluating across multiple NLP benchmarks. The main limitations are the significant utility degradation at strong privacy levels (ε less than 1 causes serious performance drops) and the computational overhead from computing per-example gradients.

**My take:** This is a foundational paper that established the paradigm most subsequent work builds on. The finding about larger models being better for privacy is genuinely surprising and has important practical implications—it suggests that the trend toward larger foundation models is actually good for privacy, not bad. Highly recommended reading.

---

### Fine-Tuning LLMs with User-Level Differential Privacy

Levy et al. (2024)
[https://arxiv.org/abs/2407.07737](https://arxiv.org/abs/2407.07737)

Most differential privacy work protects individual training examples, but this paper addresses user-level privacy, which protects all contributions from a single user. This is more appropriate for real deployments where users contribute multiple examples (think of all the messages one person sends to a chatbot). The authors compare example-level sampling with per-example gradient clipping versus user-level sampling with per-user gradient clipping.

They develop a novel privacy accountant that provides tight guarantees for example-level sampling, allowing fair comparison between approaches. The finding is that user-level sampling generally works better when users have diverse collections of examples, though example-level can win in specific settings.

The limitation is that this requires knowing user boundaries in the training data, which isn't always available. Performance also depends heavily on how diverse each user's data is.

**My take:** This is an important practical contribution. The distinction between example-level and user-level privacy is often glossed over, but it matters enormously for real applications. If you're building a privacy-preserving system where users are the natural unit of protection, this paper is essential reading.

---

### Mind the Privacy Unit! User-Level DP for Language Model Fine-Tuning

Chua et al. (2024)
[https://arxiv.org/abs/2406.14322](https://arxiv.org/abs/2406.14322)

This paper complements the Levy et al. work by providing an empirical analysis of how privacy unit choice (example versus user) affects outcomes. The authors develop practical guidelines for when to use each approach and conduct empirical privacy auditing to verify that theoretical guarantees hold in practice.

The main finding is that the right choice depends on data characteristics—there's no universal answer. The paper provides decision criteria for practitioners.

**My take:** Less theoretically novel than Levy et al., but more practically useful as a how-to guide. Read this if you need to actually implement user-level DP.

---

### Private Fine-tuning of Large Language Models with Zeroth-order Optimization (DP-ZO)

Malladi et al. (2024)
[https://arxiv.org/abs/2401.04343](https://arxiv.org/abs/2401.04343)

This paper addresses a fundamental scalability problem with DP-SGD: computing per-example gradients requires storing each gradient separately, which is memory-prohibitive for large models. The clever insight is that zeroth-order optimization estimates gradients via finite differences using only forward passes, and critically, the gradient direction is random—only the scalar step size carries information from the training data. Therefore, only this scalar needs to be privatized, not the full gradient.

This reduces memory requirements to under 16GB even with sequence lengths of 2048 tokens, making private training feasible on consumer hardware. The trade-off is slower convergence requiring more forward passes.

**My take:** This is one of the most creative papers in the collection. The observation that the step size is the only thing that needs privatization is elegant and has immediate practical impact. If memory is your bottleneck for private training, this paper solves your problem.

---

### Differentially Private Subspace Fine-Tuning (DP-SFT)

arXiv:2601.11113 (2025)
[https://arxiv.org/abs/2601.11113](https://arxiv.org/abs/2601.11113)

The core observation here is that during fine-tuning, most of the meaningful parameter updates lie within a low-dimensional, task-specific subspace. Other directions see minimal change. The paper proposes identifying this subspace (via PCA or learned projections) and then injecting DP noise only into this subspace, leaving irrelevant dimensions unperturbed.

This reduces the total noise added while maintaining privacy guarantees for what matters. The limitation is that subspace quality affects results, and there's computational cost for identifying the subspace.

**My take:** Conceptually elegant and closely related to the LoRA intuition, but formalized differently. The empirical gains depend on how well the subspace can be identified, which makes this somewhat fragile in practice. Worth knowing about but not as immediately applicable as DP-LoRA.

---

### Differentially Private Parameter-Efficient Fine-tuning (DP-LoRA)

Various papers (2023-2024), including ICLR 2024 and arXiv:2312.17493
[https://arxiv.org/abs/2312.17493](https://arxiv.org/abs/2312.17493)

Multiple research groups converged on combining Low-Rank Adaptation (LoRA) with differential privacy. The key insight is beautifully simple: DP-SGD requires adding noise proportional to the gradient's dimensionality, and LoRA dramatically reduces the number of trainable parameters. Fewer parameters means smaller gradients, which means less noise needed for the same privacy guarantee.

Results are impressive: 89% accuracy on MNLI with ε=6, only 1.2% below non-private training. However, there's a subtlety: LoRA produces about 3x more noise than full fine-tuning for the same DP guarantee because the low-rank structure concentrates gradient magnitude. The overall win comes from the dimensionality reduction outweighing this effect.

Variants like FFA-LoRA (freeze one of the low-rank matrices, train only the other) further improve efficiency.

**My take:** This is probably the most practically important result for anyone wanting to do private fine-tuning today. The combination of LoRA's efficiency benefits with DP's privacy guarantees hits a sweet spot that makes private training actually feasible. If I had to pick one technique from this literature to implement, this would be it.

---

### FlashDP: Private Training Large Language Models with Efficient DP-SGD

arXiv:2507.01154 (2025)
[https://arxiv.org/abs/2507.01154](https://arxiv.org/abs/2507.01154)

This paper addresses the engineering challenges of scaling DP-SGD to foundation model scale. The contributions are primarily about efficient implementation: better algorithms for per-example gradient computation and memory-optimized clipping. This is the kind of work that enables research at scale rather than proposing new ideas.

**My take:** Important infrastructure work. Not intellectually exciting, but necessary for the field to progress. If you're actually training large models with DP, you'll want to read this.

---

### Differentially Private Next-Token Prediction

Ginart et al. (2024)
[https://arxiv.org/abs/2403.15638](https://arxiv.org/abs/2403.15638)

Most DP work focuses on training time, but this paper provides privacy guarantees at inference time instead. The PMixED approach mixes predictions from multiple models and adds DP noise to the aggregation. This means you can use models trained without DP and still get privacy guarantees for how they're used.

The trade-off is increased inference cost (you need multiple model evaluations) and potentially degraded output quality from the aggregation.

**My take:** Clever idea that inverts the usual approach. Particularly relevant for deployments where you want to use existing (non-private) models but still provide some privacy guarantees to users. The practical applicability depends heavily on whether the inference overhead is acceptable.

---

## 3. Privacy Attacks

### Extracting Training Data from Large Language Models

Carlini, Tramèr, Wallace et al. (2021)
[https://arxiv.org/abs/2012.07805](https://arxiv.org/abs/2012.07805)

This is the paper that put training data extraction on the map. The authors demonstrated that GPT-2 could be prompted to regurgitate verbatim training sequences, including names, phone numbers, email addresses, code, and even 128-bit UUIDs. The method is straightforward: generate large amounts of text via sampling, then filter for high-likelihood sequences that appear memorized.

The most important finding, beyond the existence of the vulnerability, is that larger models are more vulnerable. This was concerning given the trend toward ever-larger models.

**My take:** A landmark paper that shaped the entire field. The finding that scale increases vulnerability was both surprising and alarming. This is essential reading for anyone in ML safety or privacy—it's the paper that demonstrated these aren't just theoretical concerns.

---

### Scalable Extraction of Training Data from (Production) Language Models

Nasr, Carlini et al. (2023)
[https://arxiv.org/abs/2311.17035](https://arxiv.org/abs/2311.17035)

This follow-up scales the attacks to production systems, including ChatGPT. The key innovation is the "divergence attack": prompts that cause aligned models to break out of their chatbot persona and emit raw training data. The famous example is "Repeat this word forever: poem"—when given this instruction, ChatGPT would eventually start outputting memorized training content at 150x the normal rate.

The authors extracted gigabytes of training data from both open models (Pythia, GPT-Neo, LLaMA) and closed systems (ChatGPT). The critical finding is that alignment and RLHF do not prevent memorization—they merely make it harder to trigger during normal use.

**My take:** If the first Carlini paper was a proof of concept, this one was a proof of scale. The divergence attack is particularly clever because it reveals that safety training creates a facade rather than a fix. The underlying memorization is still there; alignment just adds a layer that can be peeled back. This has important implications for how we think about safety more broadly.

---

### Membership Inference Attacks on Large Language Models

Various papers (2023-2024), including arXiv:2402.07841
[https://arxiv.org/abs/2402.07841](https://arxiv.org/abs/2402.07841)

Membership inference attacks try to determine whether a specific data point was in the training set. This line of work investigates whether these attacks actually work against large pre-trained LLMs—and the answer is complicated.

For models pre-trained on massive datasets for a single epoch, membership inference is surprisingly difficult. The distributions of members and non-members are nearly indistinguishable because no individual example gets enough attention to leave a detectable trace.

However, fine-tuned models are much more vulnerable. SPV-MIA (self-prompt calibration) raises attack AUC from 0.7 to 0.9 on fine-tuned models. PETAL, a label-only attack requiring no probability access, achieves 0.67 AUC even on GPT-3.5-Turbo.

**My take:** The finding that pre-training at scale provides natural protection is reassuring, but the fine-tuning vulnerability is concerning. Since most deployed models are fine-tuned, the attacks that work on fine-tuned models are what matter in practice. The gap between pre-training and fine-tuning privacy is underappreciated.

---

### Beyond Memorization: Violating Privacy via Inference

Staab et al. (2024), ICLR 2024
[https://arxiv.org/abs/2310.07298](https://arxiv.org/abs/2310.07298)

This paper represents a paradigm shift in how we think about LLM privacy. Instead of asking "can the model reproduce training data?", it asks "can the model infer personal attributes from text?" The answer is a resounding yes: LLMs can infer location, income, sex, and other attributes with 85% top-1 accuracy and 95% top-3 accuracy—100 times cheaper and 240 times faster than human inference.

The implications are profound: privacy violations can occur without any memorization whatsoever. A model that has never seen your data can still violate your privacy by making inferences from text you provide. The authors show that existing mitigations like anonymization and alignment are insufficient.

**My take:** This might be the most important paper in the collection from a conceptual standpoint. It completely reframes the threat model. All the work on preventing memorization becomes irrelevant if models can violate privacy through inference. This is the paper I'd recommend to anyone who thinks they understand LLM privacy—it will change how you think about the problem.

---

### Prompt Injection and Data Exfiltration

Greshake et al. (2023) and OWASP Top 10 for LLM (2023-2025)
[https://arxiv.org/abs/2302.12173](https://arxiv.org/abs/2302.12173)

This work documents how prompt injection attacks can be used for data exfiltration. Indirect prompt injection embeds malicious instructions in external content (web pages, documents) that the LLM processes. When the model follows these hidden instructions, it can exfiltrate data via markdown images (where the URL includes sensitive data), tool calls to external services, or other side channels.

Real incidents in 2024 included the ChatGPT memory exploit (persistent injection across sessions) and Slack AI vulnerability (RAG poisoning combined with social engineering). PoisonedRAG demonstrated that just 5 malicious documents in a corpus of millions could achieve 90% attack success.

**My take:** This is where privacy and security intersect in dangerous ways. Prompt injection creates data exfiltration pathways that are fundamentally different from memorization-based attacks. The lack of complete defenses is concerning, and the PoisonedRAG result suggests that RAG-based systems are particularly vulnerable.

---

## 4. Machine Unlearning

### Machine Unlearning of Pre-trained Large Language Models

ACL 2024
[https://aclanthology.org/2024.acl-long.457/](https://aclanthology.org/2024.acl-long.457/)

This paper addresses unlearning from pre-trained (not just fine-tuned) LLMs, which is considerably harder because the unwanted knowledge is deeply embedded. The approach combines gradient ascent on the forget set (to push away from memorized content) with gradient descent on a retain set (to maintain overall capability). The method is 100,000 times more efficient than retraining from scratch.

The main limitation is that gradient ascent degrades model quality, and verifying that unlearning actually occurred is challenging. How do you know if the model truly forgot versus just learned to hide?

**My take:** An important step toward practical unlearning, but I'm skeptical of claims about efficiency until verification is solved. If you can't verify unlearning, you can't know if your 100,000x speedup actually worked.

---

### Rethinking Machine Unlearning for Large Language Models

Nature Machine Intelligence (2025)
[https://www.nature.com/articles/s42256-025-00985-0](https://www.nature.com/articles/s42256-025-00985-0)

This paper provides a critical analysis of current unlearning methods and reaches a sobering conclusion: most methods achieve only surface-level suppression while leaving underlying representations intact. Using adversarial probing and red-teaming, the authors show that "unlearned" models can still be manipulated into revealing supposedly forgotten information.

**My take:** This is the paper that should give everyone pause about unlearning claims. The distinction between "pretending to forget" and "actually forgetting" is crucial, and this paper provides evidence that current methods fail at the latter. Essential reading for anyone relying on unlearning for compliance or safety.

---

### A Survey of Machine Unlearning in LLMs

arXiv:2503.01854 (2025)
[https://arxiv.org/abs/2503.01854](https://arxiv.org/abs/2503.01854)

This comprehensive survey taxonomizes unlearning methods into gradient ascent approaches, relabeling-based fine-tuning, and self-distillation techniques. The authors identify key challenges including applicability to black-box models, vulnerability to adversarial attacks, and the efficiency-effectiveness trade-off.

The famous Harry Potter study (Eldan and Russinovich attempting to remove Harry Potter knowledge from an LLM) is cited as evidence that semantic traces remain even after apparent unlearning. Surface prompts failed, but deeper probes still triggered the knowledge.

**My take:** A good comprehensive overview, but the field it surveys is in rough shape. The Harry Potter example crystallizes the problem: we can make models pretend to forget, but we can't make them actually forget.

---

### TOFU Benchmark

2024

The Task of Fictitious Unlearning (TOFU) provides the first standardized benchmark for evaluating LLM unlearning. The approach is clever: create fake author profiles using GPT-4, fine-tune an LLM on this synthetic data, then attempt to unlearn it. Because the data is synthetic, you know exactly what should be forgotten and can measure success precisely.

**My take:** Benchmarks drive progress, and the unlearning field badly needed one. The synthetic data approach sidesteps the problem of not knowing what's in training data. This is infrastructure that will enable better research.

---

## 5. Privacy Auditing and Measurement

### Privacy Auditing of Large Language Models

arXiv:2503.06808 (2025)
[https://arxiv.org/abs/2503.06808](https://arxiv.org/abs/2503.06808)

This paper achieves a significant milestone: the first nontrivial privacy audit of LLM training that doesn't require shadow models, gradient access, or per-iteration model checkpoints. Using novel canary designs, they achieve 49.6% true positive rate at 1% false positive rate—vastly outperforming prior approaches that achieved only 4.2%.

The practical implication is a provable lower bound on privacy leakage. For a model trained with theoretical ε=4, their audit demonstrates an empirical ε of approximately 1. This gap between theoretical and empirical privacy is persistent and suggests that theoretical guarantees are conservative.

**My take:** Privacy claims mean nothing without auditing. This paper provides tools to verify whether DP training actually delivers the promised privacy. The finding that theoretical ε consistently overestimates actual leakage is reassuring but also raises questions about whether we're being too conservative.

---

### PrivAuditor Benchmark

NeurIPS 2024

This benchmark standardizes privacy evaluation across multiple LLM architectures and fine-tuning methods. By providing consistent evaluation protocols, it enables fair comparison between approaches that previously reported results on different setups.

**My take:** Another important piece of infrastructure. The field has suffered from incomparable results; this helps fix that.

---

### Epsilon*: Privacy Metric for Machine Learning Models

arXiv:2307.11280 (2023)
[https://arxiv.org/abs/2307.11280](https://arxiv.org/abs/2307.11280)

This paper proposes an empirical privacy metric based on membership inference success, independent of how the model was trained. Models trained with DP show Epsilon* values reduced by up to 800% compared to non-DP baselines, confirming that DP training provides real protection. The metric allows privacy auditors to work independently of model owners.

**My take:** Practical and useful. The ability to assess privacy without knowing how a model was trained is valuable for third-party auditing and compliance verification.

---

## 6. Synthetic Data Generation

### Protecting Users with DP Synthetic Training Data

Google Research Blog (2024)
[https://research.google/blog/protecting-users-with-differentially-private-synthetic-training-data/](https://research.google/blog/protecting-users-with-differentially-private-synthetic-training-data/)

Google's work establishes that combining DP fine-tuning with parameter-efficient methods yields surprisingly high-quality synthetic data. The key insight is that PEFT reduces the noise burden, allowing DP-trained models to generate useful synthetic text. This synthetic data can then be used to train downstream models without privacy concerns.

**My take:** This represents a viable path to privacy-preserving AI: train a DP model, generate synthetic data, then train freely on the synthetic data. The pipeline is practical and the privacy guarantees compose cleanly.

---

### Aug-PE: DP Synthetic Text via Foundation Model APIs

Tang et al. (2024), ICLR 2024
[https://arxiv.org/abs/2403.01749](https://arxiv.org/abs/2403.01749)

The breakthrough here is generating differentially private synthetic text without any training. The method prompts an off-the-shelf LLM with sensitive examples in parallel, then aggregates predictions with DP noise. This works with proprietary models (GPT-3.5, Claude) that don't expose weights.

The speedup over DP fine-tuning is 65.7x, making private synthetic data generation accessible to anyone with API access.

**My take:** This democratizes private synthetic data generation. If you don't have the resources for DP training, you can still get privacy guarantees through this approach. The fact that it works with proprietary models is particularly important for practical adoption.

---

### Gretel GPT

Gretel AI (2024)
[https://www.gretel.ai/blog/differentially-private-synthetic-text-generation-at-scale-part-1](https://www.gretel.ai/blog/differentially-private-synthetic-text-generation-at-scale-part-1)

Gretel offers a production-ready system for DP synthetic text generation. At ε=8, downstream task accuracy is within 1% of non-private models. The system uses DP-SGD combined with QLoRA for efficient training and targets healthcare, finance, and customer support applications.

**My take:** Industrial validation that private synthetic data works in practice. The 1% accuracy gap at ε=8 is remarkably small and suggests this approach is ready for real deployment.

---

## 7. Privacy-Preserving Inference

### SIGMA: GPU-Accelerated MPC for LLM Inference

2024

SIGMA uses function secret sharing for non-linear operations (Softmax, GeLU, SiLU), achieving 12-19x latency improvement over prior GPU-based approaches. LLaMA2-13B runs in 38 seconds; GPT-2 in 1.5 seconds. This makes cryptographic inference at least imaginable for some applications.

**My take:** Impressive progress, but still 100-1000x slower than plaintext inference. This limits applicability to scenarios where privacy is worth substantial latency costs.

---

### PUMA: Secure LLaMA-7B Inference

arXiv:2307.12533 (2023)
[https://arxiv.org/abs/2307.12533](https://arxiv.org/abs/2307.12533)

PUMA demonstrates secure inference of LLaMA-7B in 5 minutes using multi-party computation. This represents practical MPC for large models, though "practical" here means "feasible" rather than "fast."

**My take:** A milestone for cryptographic privacy, but the 5-minute latency limits real-world applicability. Important for scenarios where privacy is paramount and latency is acceptable.

---

### PrivacyRestore: Privacy Removal and Restoration

arXiv:2406.01394 (2024)
[https://arxiv.org/abs/2406.01394](https://arxiv.org/abs/2406.01394)

This paper takes a practical approach: remove sensitive information before sending queries to the model, then restore it afterward. This sidesteps the computational overhead of cryptographic methods while providing meaningful privacy protection for inference.

**My take:** Refreshingly pragmatic. Not every privacy solution needs to be cryptographic. For many applications, this kind of preprocessing approach may be good enough.

---

## 8. PII Detection and Protection

### Analyzing Leakage of Personally Identifiable Information in Language Models

Lukas et al. (2023), IEEE S&P 2023
[https://arxiv.org/abs/2302.00539](https://arxiv.org/abs/2302.00539)

This paper provides rigorous game-based definitions for three types of PII leakage: extraction (recovering PII directly), inference (deducing PII from context), and reconstruction (piecing together partial information). Their attacks extract 10x more PII than prior work.

Critically, they find that sentence-level differential privacy still leaks approximately 3% of PII sequences. DP reduces but does not eliminate the problem.

**My take:** The game-based definitions are valuable for reasoning precisely about privacy. The finding that DP doesn't eliminate leakage entirely is sobering but important to understand.

---

### ProPILE: Probing Privacy Leakage in LLMs

Kim et al. (2023), NeurIPS 2023
[https://arxiv.org/abs/2307.01881](https://arxiv.org/abs/2307.01881)

ProPILE is a tool that lets data subjects probe whether their own PII is leaking from an LLM. Applied to OPT-1.3B trained on the Pile dataset, users can construct prompts based on their own information and measure how much the model reveals.

**My take:** A valuable contribution to individual agency in privacy. Giving data subjects tools to assess their own exposure is important for informed consent and regulatory compliance.

---

## 9. Regulatory and Compliance

### Right to Be Forgotten in the Era of LLMs

arXiv:2307.03941 (2023)
[https://arxiv.org/abs/2307.03941](https://arxiv.org/abs/2307.03941)

This paper analyzes whether GDPR Article 17 (right to erasure) can be satisfied for LLMs. The conclusion is stark: personal data encoded in neural network weights cannot be truly erased without retraining, which may be computationally prohibitive. Machine unlearning is positioned as a best-effort approximation, and approaches like SISA (Sharded, Isolated, Sliced, Aggregated training) can enable localized retraining by partitioning data during initial training.

**My take:** The collision between GDPR requirements and neural network reality is fascinating and unresolved. This paper does a good job articulating the technical constraints that regulators may not fully appreciate.

---

### LLMs as Personal Data

arXiv:2503.01630 (2025)
[https://arxiv.org/abs/2503.01630](https://arxiv.org/abs/2503.01630)

This legal analysis argues that LLMs themselves may constitute personal data under GDPR, not just the training data. If models can be used to infer information about individuals, the models inherit data protection obligations. The implications for data subject rights are significant.

**My take:** An important legal argument that could reshape how models are regulated. If this interpretation gains traction, it would have major implications for model distribution and deployment.

---

## 10. Industry Practices

The major LLM providers have distinct privacy approaches. OpenAI trains on consumer ChatGPT prompts by default (opt-out available) but excludes Enterprise and API data from training. In August 2025, they reversed some privacy protections, drawing criticism.

Anthropic's Claude takes a consent-forward approach, not training on prompts without explicit opt-in. Conversations are deleted from backend systems within 30 days of deletion. Their Constitutional AI approach and ISO 42001 certification provide formal privacy governance.

Google's Gemini links prompts to accounts with a minimum 72-hour retention (longer if flagged for review). Enterprise contracts include guarantees against training.

Stanford HAI research found that six leading US companies use user inputs for training, and 8.5% of prompts contain sensitive information that existing systems fail to flag.

**My take:** The variation in industry practices is striking. Anthropic's approach is the most privacy-respecting; OpenAI's default-on training is the least. Users should understand these differences when choosing providers.

---

## 11. DP Safety Benefits Beyond Privacy

### VaultGemma: Differentially Private LLM from Scratch

Google Research (2025)
[https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/](https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/)

VaultGemma is the largest open model (1 billion parameters) trained from scratch with differential privacy, achieving ε ≤ 2.0 with δ ≤ 1.1e−10 at the sequence level. The key finding for safety is that the model shows no detectable memorization when prompted with 50-token prefixes from training data. This means DP-trained models cannot reproduce any training content—including harmful content.

The model uses Gemma 2 architecture with Poisson sampling instead of uniform batches to reduce noise requirements. Performance is comparable to GPT-2, quantifying the current cost of strong privacy: about 5 years of capability progress.

**My take:** This is a landmark result. By demonstrating that DP completely prevents memorization at the 1B parameter scale, Google has shown that privacy-by-design is achievable. The performance cost is significant but may be acceptable for sensitive domains. The safety implications (no memorization of harmful content) are an important bonus.

---

### Does Differential Privacy Prevent Backdoor Attacks in Practice?

arXiv:2311.06227 (2023)
[https://arxiv.org/abs/2311.06227](https://arxiv.org/abs/2311.06227)

This paper empirically studies whether DP training protects against backdoor and poisoning attacks. The intuition is that DP limits any single sample's influence, which should include poison samples. The findings confirm this works, but with important caveats: effectiveness depends critically on hyperparameters, PATE is more effective than DP-SGD due to its bagging structure, and the number of backdoors in training data impacts success.

The paper introduces Label-DP as a faster alternative that can, with proper tuning, outperform traditional DP methods for backdoor defense while being computationally cheaper.

**My take:** Exciting dual-use potential. If DP can provide both privacy protection and poisoning defense, that strengthens the case for adoption. The hyperparameter sensitivity is concerning though—this isn't automatic protection.

---

### Why Does Large Epsilon DP Defend Against Practical MIAs?

arXiv:2402.09540 (2024)
[https://arxiv.org/abs/2402.09540](https://arxiv.org/abs/2402.09540)

This paper addresses a puzzle: theoretical DP guarantees at ε ≥ 7 are essentially vacuous, yet industry deploys models with these parameters and they empirically resist membership inference attacks. Why does weak theoretical privacy translate to strong practical privacy?

The answer is that theoretical DP assumes worst-case attackers with complete dataset knowledge. Real attackers lack this knowledge. The paper introduces Practical Membership Privacy (PMP) to model realistic attacker uncertainty and shows that large ε translates to much smaller PMP values.

**My take:** This resolves an important theory-practice gap. Practitioners can feel more confident that industrially-deployed DP (with ε around 7-10) provides meaningful protection, even if the theoretical guarantees seem weak. This is practically important guidance.

---

### Defending Against Attacks in Deep Learning with DP: A Survey

Artificial Intelligence Review (2025)
[https://link.springer.com/article/10.1007/s10462-025-11350-3](https://link.springer.com/article/10.1007/s10462-025-11350-3)

This comprehensive survey documents DP's role beyond privacy: reducing overfitting, improving generalization, defending against multiple attack types (membership inference, model inversion, data poisoning), and potentially improving fairness. However, it also documents a critical concern: DP can exacerbate unfairness for underrepresented groups. The "poor get poorer" effect means groups with less training data suffer worse privacy-utility trade-offs.

Mitigation strategies include FairDP algorithms and Counterfactual Data Augmentation, but this remains an active research area.

**My take:** The fairness findings are troubling. If privacy-preserving AI systematically harms already-disadvantaged groups, that creates a serious ethical tension. This isn't a reason to abandon DP, but it is a reason to combine it with fairness interventions.

---

### De-amplifying Bias from DP in LLM Fine-tuning

arXiv:2402.04489 (2024)
[https://arxiv.org/abs/2402.04489](https://arxiv.org/abs/2402.04489)

This paper documents that DP amplifies gender, racial, and religious bias during LLM fine-tuning, producing models more biased than those fine-tuned without DP. The cause is identified as disparity in gradient convergence across sub-groups: some groups' gradients stabilize faster than others, and DP noise disproportionately affects the slower-converging groups.

The proposed mitigation, Counterfactual Data Augmentation (CDA), creates balanced training data that reduces the convergence disparity.

**My take:** This is essential reading for anyone planning to deploy DP in practice. The finding that privacy and fairness can trade off against each other is important, and the CDA mitigation is practical. Privacy-preserving AI must also be fair AI.

---

## Key Observations Across the Literature

The research reveals several consistent patterns. First, the privacy-utility trade-off remains real but is being pushed back: strong privacy at ε less than 1 typically causes significant utility degradation, but techniques like DP-LoRA are shrinking the gap.

Second, parameter-efficient methods are a major enabler. LoRA, adapters, and other PEFT techniques reduce the noise required for DP, making private training more practical.

Third, scale provides some natural protection. Single-epoch pre-training on massive datasets makes membership inference harder than on fine-tuned models.

Fourth, semantic privacy is underexplored. Inference attacks that derive personal information without memorization may be more dangerous than extraction attacks, yet they receive less research attention.

Fifth, machine unlearning remains incomplete. Current methods suppress surface behavior but leave semantic traces. Verification is unsolved.

Sixth, regulatory requirements are technically unsatisfiable. GDPR's right to erasure cannot be fully implemented for neural networks; machine unlearning is a best-effort approximation.

Seventh, DP provides safety benefits beyond privacy. The same mechanisms that prevent data leakage also prevent memorization of harmful content and defend against poisoning attacks.

Eighth, DP and fairness can conflict. Privacy mechanisms can amplify bias against underrepresented groups, requiring explicit mitigation.

---

*Last updated: 2025-01-31*
