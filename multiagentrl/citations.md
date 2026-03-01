# Citation Appendix: Complete Bibliography with Summaries

Every source identified in this literature review, organized by topic area. Each entry includes the full citation, a brief summary of key conclusions, and open issues identified by the authors.

---

## I. Classic RL Assumption Failures in Multi-Agent Settings

### 1. Bowling, M. and Veloso, M. (2002)
**"Multiagent Learning Using a Variable Learning Rate."** *Artificial Intelligence*, 136(2):215-250.
- **Key conclusions**: Independent Q-learners in matrix games fail to converge due to non-stationarity. WoLF (Win or Learn Fast) varies learning rate based on relative performance, improving convergence in some settings.
- **Open issues**: Limited scalability guarantees; convergence only proven for restricted game classes (two-player, two-action).

### 2. Laurent, G.J., Matignon, L., and Fort-Piat, N.L. (2011)
**"The World of Independent Learners is Not Markovian."** *International Journal of Knowledge-based and Intelligent Engineering Systems*, 15(1):55-64.
- **Key conclusions**: Formal proof that when multiple independent Q-learners operate simultaneously, the environment each agent perceives is non-Markovian and non-stationary. Convergence guarantees of Q-learning do not hold.
- **Open issues**: Proposed mitigations (hysteretic Q-learning) work only in cooperative settings with specific structural assumptions.

### 3. Hernandez-Leal, P., Kaisers, M., Baarslag, T., and de Cote, E.M. (2017)
**"A Survey of Learning in Multiagent Environments: Dealing with Non-Stationarity."** *arXiv:1707.09183*.
- **Key conclusions**: Taxonomy of approaches for non-stationarity: ignoring it, detecting change, modeling opponents, theory-of-mind. No single approach dominates across settings. Problem worsens dramatically with agent count.
- **Open issues**: Most approaches tested with 2-5 agents; scalability to dozens or hundreds unexplored. Interaction with deep RL function approximation poorly understood.

### 4. Papoudakis, G., Christianos, F., Schafer, L., and Albrecht, S.V. (2021)
**"Benchmarking Multi-Agent Deep Reinforcement Learning Algorithms in Cooperative Tasks."** *NeurIPS 2021 (Datasets and Benchmarks Track)*.
- **Key conclusions**: Independent learners can be surprisingly competitive but suffer high variance and instability from non-stationarity. MAPPO generally most robust.
- **Open issues**: Gap between independent and centralized methods varies dramatically across domains; predicting when independent learning will succeed remains open.

### 5. Claus, C. and Boutilier, C. (1998)
**"The Dynamics of Reinforcement Learning in Cooperative Multiagent Systems."** *AAAI 1998*, pp. 746-752.
- **Key conclusions**: Independent learners can converge to suboptimal equilibria. Joint-action learners converge more reliably but scale exponentially with agent count. Fundamental tension: ignoring others causes non-stationarity; modeling them causes combinatorial explosion.
- **Open issues**: Tractable solutions bridging the IL/JAL gap for large numbers of agents.

### 6. Lowe, R., Wu, Y., Tamar, A., Harb, J., Abbeel, P., and Mordatch, I. (2017)
**"Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments."** *NeurIPS 2017*.
- **Key conclusions**: MADDPG uses centralized critics with decentralized actors. Independent DDPG fails catastrophically in competitive settings due to rapid environmental change.
- **Open issues**: CTDE requires cooperative training by a single entity; centralized critics scale poorly with agent count.

### 7. Foerster, J., Chen, R.Y., Al-Shedivat, M., Whiteson, S., Abbeel, P., and Mordatch, I. (2018)
**"Learning with Opponent-Learning Awareness (LOLA)."** *AAMAS 2018*, pp. 122-130.
- **Key conclusions**: LOLA agents model other agents' learning processes and achieve cooperation in IPD where naive learners defect. Addresses the circularity problem directly.
- **Open issues**: Scales poorly beyond two agents; requires knowledge of opponent's learning algorithm; higher-order LOLA leads to infinite regress.

### 8. Lanctot, M., Zambaldi, V., Gruslys, A., et al. (2017)
**"A Unified Game-Theoretic Approach to Multiagent Reinforcement Learning."** *NeurIPS 2017*.
- **Key conclusions**: PSRO (Policy-Space Response Oracles) unifies MARL approaches under empirical game theory. Standard independent RL is a degenerate PSRO case that forgets past strategies, explaining cycling behavior.
- **Open issues**: Maintaining and evaluating growing policy populations creates computational overhead; scaling to many-player games remains active research.

### 9. Bernstein, D.S., Givan, R., Immerman, N., and Zilberstein, S. (2002)
**"The Complexity of Decentralized Control of Markov Decision Processes."** *Mathematics of Operations Research*, 27(4):819-840.
- **Key conclusions**: Dec-POMDPs are NEXP-complete — fundamentally harder than single-agent POMDPs (PSPACE-complete). This is a computational complexity barrier, not merely practical.
- **Open issues**: Exact solutions intractable even for small problems; approximation algorithms have limited guarantees.

### 10. Oliehoek, F.A. and Amato, C. (2016)
**"A Concise Introduction to Decentralized POMDPs."** *Springer Briefs in Intelligent Systems*.
- **Key conclusions**: Comprehensive treatment of Dec-POMDPs. Local observations insufficient to predict future because other agents' hidden states mediate transitions. Necessitates history-dependent policies.
- **Open issues**: Finding compact sufficient statistics for history remains largely unsolved.

### 11. Amodei, D., Olah, C., Steinhardt, J., et al. (2016)
**"Concrete Problems in AI Safety."** *arXiv:1606.06565*.
- **Key conclusions**: Identifies reward hacking as one of five core safety problems. Multi-agent contexts make side effects and reward gaming harder to prevent.
- **Open issues**: Limited concrete solutions for multi-agent reward design robustness.

### 12. Krakovna, V., Uesato, J., Mikulik, V., et al. (2020)
**"Specification Gaming: The Flip Side of AI Ingenuity."** *DeepMind Blog*.
- **Key conclusions**: Cataloged dozens of specification gaming examples. Systematic tendency of powerful optimizers, worsened by agent interaction enabling joint or adversarial exploitation.
- **Open issues**: Specification gaming may be inherent to powerful optimization; formal detection in multi-agent systems underdeveloped.

### 13. Manheim, D. and Garrabrant, S. (2018)
**"Categorizing Variants of Goodhart's Law."** *arXiv:1803.04585*.
- **Key conclusions**: Four Goodhart variants: regressional, extremal, causal, adversarial. Adversarial variant amplified in multi-agent settings where agents game each other's metrics.
- **Open issues**: Quantifying Goodhart severity across multi-agent architectures; interactions between variants poorly understood.

### 14. Skalse, J., Howe, N.H.R., Krasheninnikov, D., and Krueger, D. (2022)
**"Defining and Characterizing Reward Hacking."** *NeurIPS 2022*.
- **Key conclusions**: Formal definitions distinguishing proxy reward exploitation from environment dynamics exploitation. Multi-agent dynamics can amplify proxy-true reward divergence.
- **Open issues**: Formal detection during training, especially in multi-agent settings where "hacking" vs. "legitimate strategy" is ambiguous.

### 15. Leibo, J.Z., Zambaldi, V., Lanctot, M., Marecki, J., and Graepel, T. (2017)
**"Multi-Agent Reinforcement Learning in Sequential Social Dilemmas."** *AAMAS 2017*, pp. 464-473.
- **Key conclusions**: Introduced sequential social dilemmas. Deep RL agents converge to defection under resource scarcity. More capable agents develop more exploitative strategies.
- **Open issues**: Designing environments or algorithms that reliably produce cooperation without explicit incentives.

### 16. Hughes, E., Leibo, J.Z., Phillips, M., et al. (2018)
**"Inequity Aversion Improves Cooperation in Intertemporal Social Dilemmas."** *NeurIPS 2018*.
- **Key conclusions**: Augmenting reward with inequity aversion (fairness preference) improves cooperation. Purely self-interested agents reliably produce socially suboptimal outcomes.
- **Open issues**: Inequity aversion requires modifying objectives; calibration is environment-dependent; prosocial agents can be exploited.

### 17. Eccles, T., Bachrach, Y., Lever, G., Lazaridou, A., and Graepel, T. (2019)
**"Learning Reciprocity in Complex Sequential Social Dilemmas."** *arXiv:1903.08082*.
- **Key conclusions**: Deep RL agents fail to discover reciprocal strategies even when cooperation yields higher long-run rewards. Credit assignment for cooperative behavior spans long time horizons.
- **Open issues**: Achieving reciprocity beyond dyadic interactions in many-agent settings.

### 18. Lerer, A. and Peysakhovich, A. (2017)
**"Maintaining Cooperation in Complex Social Dilemmas Using Deep Reinforcement Learning."** *arXiv:1707.01068*.
- **Key conclusions**: Cooperation becomes harder to maintain as agent count increases. Probability of cascading defection increases with group size.
- **Open issues**: Scalable mechanisms for maintaining cooperation in large agent populations.

### 19. Kirilenko, A., Kyle, A.S., Samadi, M., and Tuzun, T. (2017)
**"The Flash Crash: High-Frequency Trading in an Electronic Market."** *The Journal of Finance*, 72(3):967-998.
- **Key conclusions**: The 2010 Flash Crash resulted from automated trading algorithms creating feedback loops. Emergent dynamics no individual algorithm was designed to produce.
- **Open issues**: Designing algorithmic agents that maintain system stability alongside many other agents; regulation has not kept pace.

### 20. Spooner, T., Fearnley, J., Savani, R., and Koutsoupias, E. (2018)
**"Market Making via Reinforcement Learning."** *AAMAS 2018*, pp. 434-442.
- **Key conclusions**: RL market makers learn correlated strategies reducing liquidity when most needed. Historical training data does not reflect the regime of multiple RL agents present.
- **Open issues**: Training agents robust to distributional shift from other RL agents entering the same market.

### 21. Balduzzi, D., Racaniere, S., Martens, J., et al. (2018)
**"The Mechanics of n-Player Differentiable Games."** *ICML 2018*, pp. 363-372.
- **Key conclusions**: Simultaneous gradient descent in multi-player games exhibits rotational/oscillatory dynamics rather than convergence. Proposed Symplectic Gradient Adjustment (SGA).
- **Open issues**: SGA requires second-order derivatives across agents and information sharing; extending to non-cooperative settings remains open.

### 22. Zhang, K., Yang, Z., and Basar, T. (2021)
**"Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms."** *Handbook of Reinforcement Learning and Control*, pp. 321-384.
- **Key conclusions**: Convergence guaranteed only in restricted game classes. General-sum games with many agents lack convergence guarantees entirely.
- **Open issues**: Bridging theoretical game classes with convergence understanding and complex real-world deployments.

### 23. Busoniu, L., Babuska, R., and De Schutter, B. (2008)
**"A Comprehensive Survey of Multiagent Reinforcement Learning."** *IEEE Transactions on Systems, Man, and Cybernetics, Part C*, 38(2):156-172.
- **Key conclusions**: Identifies convergence vs. rational behavior dilemma: convergent algorithms may converge to poor equilibria; algorithms targeting good equilibria may not converge. Dilemma worsens with agents.
- **Open issues**: Unified framework handling all assumption breakdowns simultaneously.

### 24. Shoham, Y., Powers, R., and Grenager, T. (2007)
**"If Multi-Agent Learning is the Answer, What is the Question?"** *Artificial Intelligence*, 171(7):365-377.
- **Key conclusions**: MARL community often lacks clear problem definitions. No single "optimal" policy exists since best policy depends on what others do.
- **Open issues**: Establishing clear, agreed-upon evaluation criteria for MARL algorithms.

---

## II. Multi-Agent RL Solutions and Cooperative Frameworks

### 25. Sunehag, P., Lever, G., Gruslys, A., et al. (2018)
**"Value-Decomposition Networks For Cooperative Multi-Agent Learning."** *AAMAS 2018*, pp. 2085-2087.
- **Key conclusions**: VDN decomposes joint value function into additive individual utilities. Without decomposition, independent learners converge to "lazy" strategies. Additive assumption is restrictive.
- **Open issues**: Cannot represent non-linear interactions between agents.

### 26. Rashid, T., Samvelyan, M., de Witt, C.S., et al. (2018)
**"QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning."** *ICML 2018*, pp. 4295-4304.
- **Key conclusions**: Relaxes VDN's additivity to monotonicity constraint via hypernetwork. De facto cooperative MARL baseline. Ensures decentralized execution by preserving IGM property.
- **Open issues**: Monotonicity limits expressiveness; cannot represent strategies requiring non-monotonic agent interactions.

### 27. Son, K., Kim, D., Kang, W.J., et al. (2019)
**"QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning."** *ICML 2019*.
- **Key conclusions**: Removes QMIX's monotonicity constraint. Theoretically more expressive but often underperforms QMIX in practice.
- **Open issues**: Gap between theoretical expressiveness and practical performance.

### 28. Rashid, T., Farquhar, G., Peng, B., and Whiteson, S. (2020)
**"Weighted QMIX: Expanding Monotonic Value Function Factorisation."** *NeurIPS 2020*.
- **Key conclusions**: Addresses QMIX limitations through intelligent weighting of joint actions during training. Can recover optimal policies beyond monotonic class.
- **Open issues**: Weighting schemes require estimated joint Q-values, which may be inaccurate.

### 29. Yu, C., Velu, A., Vinitsky, E., et al. (2022)
**"The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games."** *NeurIPS 2022*.
- **Key conclusions**: MAPPO (straightforward PPO with centralized value function) matches or beats specialized MARL algorithms. Input representation matters more than algorithmic novelty.
- **Open issues**: Raises questions about whether cooperative MARL benchmarks are too easy.

### 30. Foerster, J., Farquhar, G., Afouras, T., Nardelli, N., and Whiteson, S. (2018)
**"Counterfactual Multi-Agent Policy Gradients."** *AAAI 2018*.
- **Key conclusions**: COMA uses counterfactual baselines for multi-agent credit assignment by computing marginal contribution of each agent's action.
- **Open issues**: Requires centralized computation; scales poorly with agent count.

### 31. Sukhbaatar, S., Szlam, A., and Fergus, R. (2016)
**"Learning Multiagent Communication with Backpropagation."** *NeurIPS 2016*.
- **Key conclusions**: CommNet allows learned communication via hidden state averaging. Significantly improves coordination on traffic junction and predator-prey tasks.
- **Open issues**: Mean-pooling limits expressiveness; all agents receive same aggregated message.

### 32. Foerster, J., Assael, Y.M., de Freitas, N., and Whiteson, S. (2016)
**"Learning to Communicate with Deep Multi-Agent Reinforcement Learning."** *NeurIPS 2016*.
- **Key conclusions**: DIAL passes continuous messages during training, discretizes for execution. Agents develop task-specific communication protocols.
- **Open issues**: Train-test gap from discretization; scaling requires deciding communication topology.

### 33. Das, A., Gerber, T., Levine, S., and Icarte, R.T. (2019)
**"TarMAC: Targeted Multi-Agent Communication."** *ICML 2019*.
- **Key conclusions**: Attention-based targeted communication more efficient than broadcast. Agents selectively send messages to specific recipients.
- **Open issues**: Pairwise attention infeasible for very large agent populations.

### 34. Lazaridou, A., Peysakhovich, A., and Baroni, M. (2017)
**"Multi-Agent Cooperation and the Emergence of (Natural) Language."** *ICLR 2017*.
- **Key conclusions**: Agents in referential games develop discrete symbolic communication with some natural language properties including compositionality.
- **Open issues**: Emergent languages tend to be degenerate without careful environmental pressure.

### 35. Mordatch, I. and Abbeel, P. (2018)
**"Emergence of Grounded Compositional Language in Multi-Agent Populations."** *AAAI 2018*.
- **Key conclusions**: Compositional, grounded language emerges when agents coordinate in physical environments.
- **Open issues**: Gap between emergent protocols and natural language.

### 36. Rabinowitz, N.C., Perbet, F., Song, H.F., et al. (2018)
**"Machine Theory of Mind."** *ICML 2018*.
- **Key conclusions**: ToMNet learns to model other agents' mental states (beliefs, goals, characters) via meta-learning. Generalizes to new agents from few trajectories.
- **Open issues**: Requires full trajectory access; integration into agent's own decision-making loop remains challenging.

### 37. Wang, R., Wu, X., Chen, J., and Wang, Y. (2022)
**"ToM2C: Target-oriented Multi-agent Communication and Cooperation with Theory of Mind."** *ICLR 2022*.
- **Key conclusions**: Integrates theory of mind into communication, allowing selective messaging only when predicted to change receiver's behavior beneficially.
- **Open issues**: ToM module adds computational overhead; accuracy degrades under high partial observability.

### 38. Jaques, N., Lazaridou, A., Hughes, E., et al. (2019)
**"Social Influence as Intrinsic Motivation for Multi-Agent Deep Reinforcement Learning."** *ICML 2019*.
- **Key conclusions**: Intrinsic reward for causal influence on others' actions improves coordination and emergent communication in social dilemmas.
- **Open issues**: May encourage manipulation in adversarial settings; counterfactual reasoning is expensive.

### 39. Yang, J., Nakhaei, A., Rafiee, A., and Wen, Z. (2020)
**"Learning to Incentivize Other Learning Agents."** *NeurIPS 2020*.
- **Key conclusions**: Agents learn to redistribute rewards to create emergent cooperation among self-interested agents.
- **Open issues**: Bilevel optimization is computationally demanding and unstable.

### 40. Wolpert, D.H. and Tumer, K. (2001)
**"Optimal Payoff Functions for Members of Collectives."** *Advances in Complex Systems*.
- **Key conclusions**: Difference rewards (crediting each agent for its marginal contribution) address credit assignment and improve cooperation in large collectives.
- **Open issues**: Computing difference rewards requires counterfactual evaluation.

### 41. Yang, Y., Luo, R., Li, M., et al. (2018)
**"Mean Field Multi-Agent Reinforcement Learning."** *ICML 2018*, pp. 5571-5580.
- **Key conclusions**: Mean field approximation reduces exponential complexity to linear. Accurate when agents are homogeneous with pairwise interactions.
- **Open issues**: Breaks down with agent heterogeneity or when small groups have disproportionate influence.

### 42. Lasry, J.-M. and Lions, P.-L. (2007)
**"Mean Field Games."** *Japanese Journal of Mathematics*, 2(1):229-260.
- **Key conclusions**: Mathematical foundation for strategic interactions among very large populations. Each agent's strategy depends on population distribution; equilibrium requires self-consistency.
- **Open issues**: Extension from rational agents to bounded-rationality RL agents.

### 43. Huang, M., Caines, P.E., and Malhame, R.P. (2007)
**"Large-Population Cost-Coupled LQG Problems."** *IEEE Transactions on Automatic Control*.
- **Key conclusions**: Independent co-development of mean field game theory for large-population settings with decentralized epsilon-Nash equilibria.
- **Open issues**: Extension beyond LQG settings.

### 44. Carmona, R., Lauriere, M., and Tan, Z. (2019)
**"Model-Free Mean-Field Reinforcement Learning."** *arXiv:1907.05854*.
- **Key conclusions**: Model-free RL algorithms for mean field MDPs and mean field games. Learn by sampling from population distribution.
- **Open issues**: Convergence requires smoothness assumptions; sample efficiency in high dimensions.

### 45. Lauriere, M., Perrin, S., Geist, M., and Pietquin, O. (2022)
**"Learning Mean Field Games: A Survey."** *arXiv:2205.12944*.
- **Key conclusions**: Survey of MFG-ML intersection. Applications in crowd modeling, autonomous driving, economics.
- **Open issues**: Existence/uniqueness of equilibria; finite-population approximation errors.

### 46. He, H., Boyd-Graber, J., Kwok, K., and Daume III, H. (2016)
**"Opponent Modeling in Deep Reinforcement Learning."** *ICML 2016*.
- **Key conclusions**: DRON augments DQN with opponent modeling module. Outperforms standard DQN in competitive games.
- **Open issues**: Cold-start problem; assumes relatively stable opponent policy.

### 47. Wen, Y., Yang, Y., Luo, R., Wang, J., and Pan, W. (2019)
**"Probabilistic Recursive Reasoning for Multi-Agent Reinforcement Learning."** *ICLR 2019*.
- **Key conclusions**: PR2 uses cognitive hierarchy for recursive belief reasoning. Level-1 or level-2 captures most benefit.
- **Open issues**: Computational cost grows exponentially with recursion depth.

### 48. Vinitsky, E., Jaques, N., Leibo, J., et al. (2019)
**"The Problem of Autonomous Sanctioning."** *AAMAS Workshop 2019*.
- **Key conclusions**: Agents can learn to punish defectors, sustaining cooperation. But punishment creates second-order dilemmas.
- **Open issues**: Antisocial punishment emergence; robust punishment mechanism design.

### 49. Perolat, J., Leibo, J.Z., Zambaldi, V., et al. (2017)
**"A Multi-Agent Reinforcement Learning Model of Common-Pool Resource Appropriation."** *NeurIPS 2017*.
- **Key conclusions**: RL agents in common-pool resource settings converge to over-exploitation without cooperation mechanisms.
- **Open issues**: Mechanism design for cooperative resource management.

### 50. Anastassacos, N., Hailes, S., and Musolesi, M. (2021)
**"Partner Selection for the Emergence of Cooperation in Multi-Agent Systems Using Reinforcement Learning."** *AAAI 2021*.
- **Key conclusions**: Partner selection based on reputation creates selection pressure favoring cooperators.
- **Open issues**: Reputation systems can be gamed; scaling to large populations is expensive.

### 51. Christoffersen, P., Haupt, A., and Hadfield-Menell, D. (2023)
**"Get It in Writing: Formal Contracts Mitigate Social Dilemmas in Multi-Agent RL."** *AAMAS 2023*.
- **Key conclusions**: Binding contracts enable mutual cooperation by making commitment credible. Transforms social dilemma structure.
- **Open issues**: Contract design, negotiation, and enforcement in complex settings.

### 52. Zheng, S., Trott, A., Srinivasa, S., Parkes, D.C., and Socher, R. (2022)
**"The AI Economist: Taxation Policy Design via Two-Level Deep RL."** *Science Advances*.
- **Key conclusions**: Two-level RL discovers tax policies with better equality-productivity trade-offs than baselines. Demonstrates mechanism design via RL.
- **Open issues**: Sim-to-real transfer for economic policy; robustness to strategic manipulation.

### 53. Koster, R., Balaguer, J., Tacchetti, A., et al. (2022)
**"Human-Centred Mechanism Design with Democratic AI."** *Nature Human Behaviour*.
- **Key conclusions**: RL mechanism trained on human preferences achieves redistribution rated fairer than human-designed alternatives.
- **Open issues**: Tyranny of majority; scalability to complex decisions.

### 54. Lu, S., Balis, K., and Zhang, K. (2021)
**"Decentralized Policy Gradient for Nash Equilibria in Multi-Agent Constrained MDPs."** *arXiv:2106.07160*.
- **Key conclusions**: Lagrangian methods adapted for multi-agent constrained optimization.
- **Open issues**: Constraint satisfaction during training (not just at convergence); decentralized enforcement is challenging.

### 55. Gu, S., Kuba, J.G., Chen, Y., et al. (2023)
**"Safe Multi-Agent Reinforcement Learning for Multi-Robot Control."** *Artificial Intelligence*.
- **Key conclusions**: Constrained MARL achieves coordination while maintaining safety guarantees.
- **Open issues**: Non-stationarity means constraints satisfied at one point may be violated later.

### 56. Elsayed-Aly, I., Bharadwaj, S., Amato, C., et al. (2021)
**"Safe Multi-Agent Reinforcement Learning via Shielding."** *AAMAS 2021*.
- **Key conclusions**: Factored shields decompose joint safety specifications into per-agent shields for scalability.
- **Open issues**: Computing shields for large systems is expensive; shields may be overly conservative.

### 57. Phan, T., Belzner, L., Gabor, T., et al. (2021)
**"Resilient Multi-Agent Reinforcement Learning with Adversarial Value Decomposition."** *AAAI 2021*.
- **Key conclusions**: Training with adversarial partner replacements improves robustness to miscoordination.
- **Open issues**: Trade-off between robustness and optimality with cooperative partners.

### 58. Gronauer, S. and Diepold, K. (2022)
**"Multi-Agent Deep Reinforcement Learning: A Survey."** *Artificial Intelligence Review*, 55:895-943.
- **Key conclusions**: Comprehensive survey of cooperative, competitive, and mixed MARL. Key challenges: non-stationarity, partial observability, credit assignment, scalability.
- **Open issues**: Transfer learning in MARL under-explored; real-world deployment rare; theoretical understanding limited.

### 59. Oroojlooy, A. and Hajinezhad, D. (2023)
**"A Review of Cooperative Multi-Agent Deep Reinforcement Learning."** *Applied Intelligence*, 53:13677-13722.
- **Key conclusions**: Credit assignment is the central cooperative MARL challenge. Detailed comparison of value decomposition, policy gradient, and communication approaches.
- **Open issues**: Scalability; heterogeneous agents; sim-to-real gap.

### 60. Lazaridou, A. and Baroni, M. (2020)
**"Emergent Multi-Agent Communication in the Deep Learning Era."** *arXiv:2006.02419*.
- **Key conclusions**: Survey of emergent communication. Compositional communication requires specific environmental pressures.
- **Open issues**: Bridging emergent-natural language gap; evaluation metrics.

### 61. Guo, S., Zhang, Y., Gao, J., and An, B. (2024)
**"A Survey on Large Language Model-Based Multi-Agent Systems."** *arXiv*.
- **Key conclusions**: LLM-based agents communicate in natural language, reason about mental states, and coordinate on complex tasks. Paradigm shift from traditional MARL.
- **Open issues**: Cost limits scale; grounding LLM reasoning in environment dynamics; evaluation methodology.

---

## III. Game Theory and Multi-Agent Systems

### 62. Daskalakis, C., Goldberg, P.W., and Papadimitriou, C.H. (2009)
**"The Complexity of Computing a Nash Equilibrium."** *SIAM Journal on Computing*, 39(1):195-259.
- **Key conclusions**: Computing Nash equilibrium in two-player games is PPAD-complete.
- **Open issues**: Tractability in structured/typical games; efficient approximation.

### 63. Chen, X. and Deng, X. (2006)
**"Settling the Complexity of Two-Player Nash Equilibrium."** *FOCS 2006*, pp. 261-272.
- **Key conclusions**: Independent proof of PPAD-completeness for two-player Nash equilibrium.
- **Open issues**: Gap between worst-case hardness and practical tractability.

### 64. Rubinstein, A. (2018)
**"Inapproximability of Nash Equilibrium."** *SIAM Journal on Computing*, 47(3):917-959.
- **Key conclusions**: Even approximate Nash equilibria require quasi-polynomial time under ETH for PPAD.
- **Open issues**: Exact tractability threshold for approximation.

### 65. Piliouras, G. and Shamma, J.S. (2018)
**"Optimization Despite Chaos."** *ICML 2018*.
- **Key conclusions**: Gradient-based learning can exhibit chaos while still providing some optimization guarantees.
- **Open issues**: Characterizing which game structures lead to chaos vs. convergence.

### 66. Cheung, Y.K. and Piliouras, G. (2019)
**"Vortices Instead of Equilibria in MinMax Optimization."** *COLT 2019*.
- **Key conclusions**: Multiplicative weights in zero-sum games produce vortices, not convergence. Time-average converges but day-to-day behavior is cyclical.
- **Open issues**: Modified dynamics for last-iterate convergence in broader game classes.

### 67. Mertikopoulos, P., Papadimitriou, C., and Piliouras, G. (2018)
**"Cycles in Adversarial Regularized Learning."** *SODA 2018*.
- **Key conclusions**: Regularized learning generically follows limit cycles rather than converging to Nash equilibria.
- **Open issues**: Whether cycling produces better or worse average welfare than equilibrium play.

### 68. Bailey, J.P. and Piliouras, G. (2018)
**"Multiplicative Weights Update in Zero-Sum Games."** *ACM EC 2018*.
- **Key conclusions**: Time-average converges to Nash but day-to-day behavior diverges from equilibrium.
- **Open issues**: Algorithms achieving genuine last-iterate convergence.

### 69. Daskalakis, C. and Panageas, I. (2019)
**"Last-Iterate Convergence: Zero-Sum Games and Constrained Min-Max Optimization."** *ITCS 2019*.
- **Key conclusions**: Optimistic MWU achieves last-iterate convergence to Nash in zero-sum games. Breakthrough showing minor algorithmic modifications qualitatively change convergence.
- **Open issues**: Extension to general-sum and multi-player settings.

### 70. Daskalakis, C., Fishelson, M., and Golowich, N. (2021)
**"Near-Optimal No-Regret Learning in General Games."** *NeurIPS 2021*.
- **Key conclusions**: Near-optimal O(sqrt(T)) regret bounds in bandit feedback for general multi-player games.
- **Open issues**: Translating regret bounds into welfare guarantees.

### 71. Koutsoupias, E. and Papadimitriou, C. (1999)
**"Worst-Case Equilibria."** *STACS 1999*, pp. 404-413.
- **Key conclusions**: Introduced price of anarchy framework measuring worst equilibrium vs. social optimum.
- **Open issues**: Generalization to broader game classes.

### 72. Roughgarden, T. and Tardos, E. (2002)
**"How Bad Is Selfish Routing?"** *Journal of the ACM*, 49(2):236-259.
- **Key conclusions**: Price of anarchy in nonatomic selfish routing with linear latencies is exactly 4/3.
- **Open issues**: Tighter bounds for atomic routing; dynamic settings.

### 73. Roughgarden, T. (2015)
**"Intrinsic Robustness of the Price of Anarchy."** *Journal of the ACM*, 62(5):32.
- **Key conclusions**: Smoothness-based PoA bounds extend to correlated equilibria, coarse correlated equilibria, and no-regret learning outcomes.
- **Open issues**: Games that are not smooth or where smoothness gives loose bounds.

### 74. Braess, D. (1968)
**"Uber ein Paradoxon aus der Verkehrsplanung."** *Unternehmensforschung*, 12:258-268.
- **Key conclusions**: Adding a new road can increase all travelers' costs at equilibrium.
- **Open issues**: Identifying structures immune to Braess's paradox.

### 75. Rosenthal, R.W. (1973)
**"A Class of Games Possessing Pure-Strategy Nash Equilibria."** *International Journal of Game Theory*, 2(1):65-67.
- **Key conclusions**: Congestion games always have pure-strategy Nash equilibria via potential function.
- **Open issues**: Computational complexity of finding best/worst Nash equilibria.

### 76. Marden, J.R. and Wierman, A. (2013)
**"Distributed Welfare Games."** *Operations Research*, 61(1):155-168.
- **Key conclusions**: Designing local utility functions (Shapley-value, marginal-contribution) achieves optimal or near-optimal price of anarchy bounds.
- **Open issues**: Application to complex AI systems where global welfare is hard to define.

### 77. Vickrey, W. (1961)
**"Counterspeculation, Auctions, and Competitive Sealed Tenders."** *Journal of Finance*, 16(1):8-37.
- **Key conclusions**: Second-price auction makes truthful bidding dominant strategy.
- **Open issues**: Extension to multi-item settings; susceptibility to collusion.

### 78. Clarke, E.H. (1971) / Groves, T. (1973)
**"Multipart Pricing of Public Goods" / "Incentives in Teams."** *Public Choice* / *Econometrica*.
- **Key conclusions**: VCG mechanism achieves efficient outcomes with truthful reporting as dominant strategy. Payments equal externalities imposed on others.
- **Open issues**: Not budget-balanced; susceptible to collusion; combinatorial complexity.

### 79. Myerson, R. (1981)
**"Optimal Auction Design."** *Mathematics of Operations Research*, 6(1):58-73.
- **Key conclusions**: Revenue-maximizing single-item auction characterized via virtual valuations.
- **Open issues**: Multi-item optimal auction design largely unsolved.

### 80. Nisan, N. and Ronen, A. (2001)
**"Algorithmic Mechanism Design."** *Games and Economic Behavior*, 35(1-2):166-196.
- **Key conclusions**: Founded algorithmic mechanism design by combining computational and incentive constraints. Truthfulness can fundamentally change the computational landscape.
- **Open issues**: Characterizing the "price of truthfulness."

### 81. Nisan, N., Roughgarden, T., Tardos, E., and Vazirani, V.V. (Eds.) (2007)
**"Algorithmic Game Theory."** *Cambridge University Press*.
- **Key conclusions**: Definitive reference covering equilibrium computation, mechanism design, price of anarchy, combinatorial auctions.
- **Open issues**: Each chapter identifies specific open problems.

### 82. Parkes, D.C. and Wellman, M.P. (2015)
**"Economic Reasoning and Artificial Intelligence."** *Science*, 349(6245):267-272.
- **Key conclusions**: Economic reasoning and mechanism design essential for AI agent governance. Challenge: AI with potentially superhuman strategic capabilities may require new approaches.
- **Open issues**: Mechanism design when agents have superhuman strategic capability.

### 83. Conitzer, V. and Sandholm, T. (2002)
**"Complexity of Mechanism Design."** *UAI 2002*, pp. 103-110.
- **Key conclusions**: Even simple mechanism design problems can be NP-hard. Implications for automated mechanism design.
- **Open issues**: Tractable subclasses; ML approaches to mechanism design.

### 84. Duetting, P., Feng, Z., Narasimhan, H., Parkes, D.C., and Ravindranath, S.S. (2019)
**"Optimal Auctions through Deep Learning."** *ICML 2019*, pp. 1706-1715.
- **Key conclusions**: Deep learning can discover approximately optimal, incentive-compatible auction mechanisms.
- **Open issues**: Theoretical guarantees on learned mechanisms; generalization.

### 85. Maynard Smith, J. and Price, G.R. (1973)
**"The Logic of Animal Conflict."** *Nature*, 246(5427):15-18.
- **Key conclusions**: Introduced Evolutionarily Stable Strategy (ESS). A strategy an ESS if no rare mutant can invade.
- **Open issues**: ESS existence not guaranteed in all games.

### 86. Taylor, P.D. and Jonker, L.B. (1978)
**"Evolutionary Stable Strategies and Game Dynamics."** *Mathematical Biosciences*, 40(1-2):145-156.
- **Key conclusions**: Formalized replicator dynamics. Rest points correspond to Nash equilibria.
- **Open issues**: Behavior in complex games with many strategies.

### 87. Borgers, T. and Sarin, R. (1997)
**"Learning Through Reinforcement and Replicator Dynamics."** *Journal of Economic Theory*, 77(1):1-14.
- **Key conclusions**: Formal connection: reinforcement learning converges to replicator dynamics as learning rate goes to zero.
- **Open issues**: Whether connection holds for more sophisticated algorithms.

### 88. Bloembergen, D., Tuyls, K., Hennes, D., and Kaisers, M. (2015)
**"Evolutionary Dynamics of Multi-Agent Learning: A Survey."** *JAIR*, 53:659-697.
- **Key conclusions**: Many MARL algorithms have evolutionary dynamics counterparts. Evolutionary game theory provides valuable analytical tools.
- **Open issues**: Scaling beyond normal-form games; incorporating deep learning.

### 89. Tuyls, K., Verbeeck, K., and Lenaerts, T. (2003)
**"A Selection-Mutation Model for Q-learning in Multi-Agent Systems."** *AAMAS 2003*, pp. 693-700.
- **Key conclusions**: Multi-agent Q-learning modeled by replicator-mutator dynamics.
- **Open issues**: Extension to larger state spaces.

### 90. Boyd, R. and Richerson, P.J. (1985)
**"Culture and the Evolutionary Process."** *University of Chicago Press*.
- **Key conclusions**: Mathematical models of cultural evolution. Social learning rules (imitation, conformism) shape cultural dynamics. Cultural evolution enables cooperation beyond biological evolution.
- **Open issues**: Application to artificial agent populations.

### 91. Friedman, J.W. (1971)
**"A Non-Cooperative Equilibrium for Supergames."** *Review of Economic Studies*, 38(1):1-12.
- **Key conclusions**: In infinitely repeated games with patient players, any feasible individually rational payoff is sustainable via trigger strategies.
- **Open issues**: Robustness to trembles and mistakes.

### 92. Fudenberg, D. and Maskin, E. (1986)
**"The Folk Theorem in Repeated Games."** *Econometrica*, 54(3):533-554.
- **Key conclusions**: Any feasible individually rational payoff achievable as subgame perfect equilibrium with sufficient patience. Multiplicity of equilibria is itself a problem.
- **Open issues**: Equilibrium selection.

### 93. Axelrod, R. (1984)
**"The Evolution of Cooperation."** *Basic Books*.
- **Key conclusions**: Tit-for-Tat outperforms complex strategies in IPD tournaments. Successful cooperation requires being nice, retaliatory, forgiving, and clear.
- **Open issues**: Tit-for-Tat vulnerable to noise; n-player extensions.

### 94. Nowak, M.A. (2006)
**"Five Rules for the Evolution of Cooperation."** *Science*, 314(5805):1560-1563.
- **Key conclusions**: Five mechanisms promote cooperation: kin selection, direct reciprocity, indirect reciprocity, network reciprocity, group selection.
- **Open issues**: Interactions among mechanisms; application to artificial agents.

### 95. Press, W.H. and Dyson, F.J. (2012)
**"Iterated Prisoner's Dilemma Contains Strategies That Dominate Any Evolutionary Opponent."** *PNAS*, 109(26):10409-10413.
- **Key conclusions**: Zero-determinant strategies can unilaterally set opponent's payoff or enforce linear payoff relationships.
- **Open issues**: Robustness in finite populations; evolutionary stability.

### 96. Freund, Y. and Schapire, R.E. (1997)
**"A Decision-Theoretic Generalization of On-Line Learning."** *JCSS*, 55(1):119-139.
- **Key conclusions**: Hedge algorithm achieves O(sqrt(T log N)) regret. All players using no-regret converge to coarse correlated equilibria.
- **Open issues**: Last-iterate vs. time-average convergence.

### 97. Arora, S., Hazan, E., and Kale, S. (2012)
**"The Multiplicative Weights Update Method: A Meta-Algorithm and Applications."** *Theory of Computing*, 8(6):121-164.
- **Key conclusions**: Unified presentation of multiplicative weights across fields.
- **Open issues**: Extension to continuous strategy spaces.

### 98. Hart, S. and Mas-Colell, A. (2000)
**"A Simple Adaptive Procedure Leading to Correlated Equilibrium."** *Econometrica*, 68(5):1127-1150.
- **Key conclusions**: Regret matching converges to correlated equilibria. Simple, decentralized procedure.
- **Open issues**: Convergence rate; behavior with many players and actions.

### 99. Zinkevich, M., Johanson, M., Bowling, M., and Piccione, C. (2008)
**"Regret Minimization in Games with Incomplete Information."** *NeurIPS 2008*, pp. 1729-1736.
- **Key conclusions**: Counterfactual Regret Minimization (CFR) for extensive-form games. Foundation for solving large poker games.
- **Open issues**: Scalability with very large state spaces; function approximation.

### 100. Brown, N. and Sandholm, T. (2018)
**"Superhuman AI for Heads-Up No-Limit Poker: Libratus."** *Science*, 359(6374):418-424.
- **Key conclusions**: CFR-based computation achieves superhuman poker play.
- **Open issues**: Extension to multi-player games; generalization.

### 101. Brown, N. and Sandholm, T. (2019)
**"Superhuman AI for Multiplayer Poker."** *Science*, 365(6456):885-890.
- **Key conclusions**: Pluribus achieves superhuman six-player poker. Near-equilibrium play effective even without two-player zero-sum guarantees.
- **Open issues**: Theoretical foundations for multi-player equilibrium computation.

### 102. Armstrong, S., Bostrom, N., and Shulman, C. (2016)
**"Racing to the Precipice."** *AI & Society*, 31(2):201-206.
- **Key conclusions**: Competitive pressure leads to underinvestment in safety (Prisoner's Dilemma). Nash equilibrium involves less safety than social optimum.
- **Open issues**: Implementing effective coordination given competitive pressures and information asymmetry.

### 103. Cave, S. and OhEigeartaigh, S.S. (2018)
**"An AI Race for Strategic Advantage: Rhetoric and Risks."** *AIES 2018*, pp. 36-40.
- **Key conclusions**: "Race" framing creates self-fulfilling competitive pressure undermining safety.
- **Open issues**: Reframing toward cooperative narratives.

### 104. Schelling, T.C. (1960)
**"The Strategy of Conflict."** *Harvard University Press*.
- **Key conclusions**: Focal points, commitment, credible threats, and tacit bargaining enable cooperation without communication.
- **Open issues**: Application to AI agents where cultural focal points may not be shared.

### 105. Jervis, R. (1978)
**"Cooperation Under the Security Dilemma."** *World Politics*, 30(2):167-214.
- **Key conclusions**: When agents cannot distinguish offensive from defensive capabilities, rational defense measures escalate into arms races.
- **Open issues**: Application to AI capabilities where offense-defense distinctions are unclear.

### 106. Arrow, K.J. (1951/1963)
**"Social Choice and Individual Values."** *Wiley*.
- **Key conclusions**: Arrow's Impossibility Theorem: no social welfare function satisfies all four desirable axioms simultaneously.
- **Open issues**: Which axiom to relax; cardinal utility approaches.

### 107. Gibbard, A. (1973) / Satterthwaite, M.A. (1975)
**"Manipulation of Voting Schemes" / "Strategy-Proofness and Arrow's Conditions."**
- **Key conclusions**: Any non-dictatorial voting rule with 3+ alternatives is susceptible to strategic manipulation.
- **Open issues**: Computational complexity as a barrier to manipulation.

### 108. Brandt, F., Conitzer, V., Endriss, U., et al. (Eds.) (2016)
**"Handbook of Computational Social Choice."** *Cambridge University Press*.
- **Key conclusions**: Computational hardness of manipulation as practical barrier to strategic behavior.
- **Open issues**: Whether barriers hold against AI-powered manipulation.

### 109. Noothigattu, R., Shah, S., Gkatzelis, V., et al. (2018)
**"A Voting-Based System for Ethical Decision Making."** *AAAI 2018*, pp. 1587-1594.
- **Key conclusions**: Framework for ethical AI decisions based on voting theory and preference aggregation.
- **Open issues**: Whose preferences; tyranny of majority.

### 110. Roth, A.E. (2002)
**"The Economist as Engineer."** *Econometrica*, 70(4):1341-1378.
- **Key conclusions**: Market design as economic engineering using game-theoretic insights.
- **Open issues**: Robustness of designed markets to sophisticated AI agents.

### 111. Gale, D. and Shapley, L.S. (1962)
**"College Admissions and the Stability of Marriage."** *American Mathematical Monthly*, 69(1):9-15.
- **Key conclusions**: Deferred acceptance for stable matching. Foundation for practical market design.
- **Open issues**: Strategy-proofness only for proposing side.

### 112. Shapley, L.S. (1953)
**"A Value for n-Person Games."** *Contributions to the Theory of Games, Vol. II*.
- **Key conclusions**: Shapley value gives unique fair allocation satisfying efficiency, symmetry, null player, additivity.
- **Open issues**: Exponential computational complexity in general.

### 113. Nash, J.F. (1950)
**"The Bargaining Problem."** *Econometrica*, 18(2):155-162.
- **Key conclusions**: Axiomatized two-player bargaining. Unique solution maximizes product of gains from disagreement.
- **Open issues**: Extension to n-player; sensitivity to disagreement point.

### 114. Vinyals, O., et al. (2019)
**"Grandmaster Level in StarCraft II Using Multi-Agent Reinforcement Learning."** *Nature*, 575(7782):350-354.
- **Key conclusions**: AlphaStar used league-based training combining deep RL with game-theoretic population methods.
- **Open issues**: Computational cost; real-world transfer.

### 115. Perolat, J., De Vylder, B., et al. (2022)
**"Mastering the Game of Stratego."** *Science*, 378(6623):990-996.
- **Key conclusions**: DeepNash achieved expert Stratego using deep RL with regularized Nash dynamics.
- **Open issues**: Extension to multi-player and general-sum settings.

### 116. Tennenholtz, M. (2004)
**"Program Equilibrium."** *Games and Economic Behavior*, 49(2):363-373.
- **Key conclusions**: Agents submitting programs enables conditional cooperation in Prisoner's Dilemma.
- **Open issues**: Verification complexity; application to real AI agents.

### 117. Bertsimas, D., Farias, V.F., and Trichakis, N. (2011)
**"The Price of Fairness."** *Operations Research*, 59(1):17-31.
- **Key conclusions**: Quantified efficiency loss from fairness constraints.
- **Open issues**: Optimal tradeoffs in dynamic multi-agent AI systems.

### 118. Crandall, J.W., Oudah, M., et al. (2018)
**"Cooperating with Machines."** *Nature Communications*, 9:233.
- **Key conclusions**: Cheap talk plus forgiving-but-retaliatory policy achieves high cooperation with humans and machines.
- **Open issues**: Scaling; costly communication.

### 119. Sandholm, T. (2003)
**"Automated Mechanism Design."** *CP 2003*, pp. 19-36.
- **Key conclusions**: Computational methods can find mechanisms satisfying desired properties, sometimes outperforming analytical solutions.
- **Open issues**: Scalability; verification.

### 120. Lundberg, S.M. and Lee, S.-I. (2017)
**"A Unified Approach to Interpreting Model Predictions."** *NeurIPS 2017*, pp. 4765-4774.
- **Key conclusions**: SHAP applies Shapley values to ML model interpretation.
- **Open issues**: Computational cost for large models.

### 121. Balduzzi, D., Racaniere, S., Martens, J., et al. (2019)
**"Open-Ended Learning in Symmetric Zero-Sum Games."** *ICML 2019*.
- **Key conclusions**: Games decompose into transitive and cyclic components. Effective training must navigate both.
- **Open issues**: Scaling geometric decomposition.

### 122. Christodoulou, G. and Koutsoupias, E. (2005)
**"The Price of Anarchy of Finite Congestion Games."** *STOC 2005*, pp. 67-73.
- **Key conclusions**: Tight PoA bound of 5/2 for atomic congestion games with linear delays.
- **Open issues**: Weighted games with player-specific costs.

### 123. Milgrom, P. (2004)
**"Putting Auction Theory to Work."** *Cambridge University Press*.
- **Key conclusions**: Comprehensive treatment of auction theory and practical applications.
- **Open issues**: Optimal combinatorial auction design.

### 124. Chalkiadakis, G., Elkind, E., and Wooldridge, M. (2011)
**"Computational Aspects of Cooperative Game Theory."** *Morgan & Claypool*.
- **Key conclusions**: Surveyed complexity of cooperative solution concepts for multi-agent task allocation and coalition formation.
- **Open issues**: Scalable algorithms for large-scale systems.

### 125. Bartholdi, J., Tovey, C.A., and Trick, M.A. (1989)
**"The Computational Difficulty of Manipulating an Election."** *Social Choice and Welfare*, 6(3):227-241.
- **Key conclusions**: Computing optimal manipulation is NP-hard for certain voting rules.
- **Open issues**: NP-hardness is worst-case; AI may find average-case manipulation easy.

---

## IV. Mimetic Desire and Agent Behavior

### 126. Girard, R. (1961/1965)
**"Deceit, Desire, and the Novel."** *Johns Hopkins University Press*.
- **Key conclusions**: Desire is not autonomous but mediated by a model. Distinguishes external mediation (distant model) from internal mediation (peer/rival).
- **Open issues**: Generalizability beyond literary analysis debated.

### 127. Girard, R. (1972/1977)
**"Violence and the Sacred."** *Johns Hopkins University Press*.
- **Key conclusions**: Mimetic desire produces mimetic crisis (undifferentiated rivalry). Resolved through scapegoat mechanism — unanimous violence against single victim restoring social order.
- **Open issues**: Universality of scapegoat mechanism across cultures contested.

### 128. Girard, R. (1978/1987)
**"Things Hidden Since the Foundation of the World."** *Stanford University Press*.
- **Key conclusions**: Synthesizes mimetic theory with Judeo-Christian scriptures as revealing (not participating in) the scapegoat mechanism.
- **Open issues**: Theological claims debated; relationship to evolutionary accounts unclear.

### 129. Girard, R. (1982/1986)
**"The Scapegoat."** *Johns Hopkins University Press*.
- **Key conclusions**: Systematic method for identifying scapegoat patterns: social crisis, indifferentiation, transgression accusations, victim selection marks.
- **Open issues**: Critics argue interpretive framework is overly deterministic.

### 130. Banerjee, A.V. (1992)
**"A Simple Model of Herd Behavior."** *Quarterly Journal of Economics*, 107(3):797-817.
- **Key conclusions**: Rational agents may rationally ignore private information and follow the herd. Cascades are fragile.
- **Open issues**: How cascades change with boundedly rational or learning agents.

### 131. Bikhchandani, S., Hirshleifer, D., and Welch, I. (1992)
**"A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades."** *Journal of Political Economy*, 100(5):992-1026.
- **Key conclusions**: Even rational agents produce fragile, arbitrary conventions through sequential imitation. Formal version of mimetic convergence.
- **Open issues**: Connection to Girard structural but never made explicit.

### 132. Cont, R. and Bouchaud, J.-P. (2000)
**"Herd Behavior and Aggregate Fluctuations in Financial Markets."** *Macroeconomic Dynamics*, 4(2):170-196.
- **Key conclusions**: Herding in networks produces fat-tailed returns (crashes and bubbles). Mimetic character explicit: agents desire what neighbors desire.
- **Open issues**: Real markets have additional institutional structure.

### 133. Bowles, S. (1998)
**"Endogenous Preferences."** *Journal of Economic Literature*, 36(1):75-111.
- **Key conclusions**: Economic institutions shape preferences rather than merely responding to them. Preferences for cooperation and fairness influenced by institutional environment.
- **Open issues**: Does not engage with Girard but framework is compatible.

### 134. Bisin, A. and Verdier, T. (2001)
**"The Economics of Cultural Transmission and the Dynamics of Preferences."** *Journal of Economic Theory*, 97(2):298-319.
- **Key conclusions**: Formal model of preference transmission through socialization. Preferences endogenous at population level.
- **Open issues**: Continuous preference spaces harder to analyze.

### 135. Postlewaite, A. (2011)
**"Social Norms and Preferences."** *Handbook of Social Economics*.
- **Key conclusions**: Social norms, status, and peer effects shape preferences. Status desire is inherently mimetic.
- **Open issues**: Gap between static and dynamic models.

### 136. Schaal, S. (1999)
**"Is Imitation Learning the Route to Humanoid Robots?"** *Trends in Cognitive Sciences*, 3(6):233-242.
- **Key conclusions**: Agents learn by observing demonstrations — literal mimesis. Foundation for imitation learning in robotics.
- **Open issues**: Motor skill focus; does not address preference/desire formation through imitation.

### 137. Abbeel, P. and Ng, A.Y. (2004)
**"Apprenticeship Learning via Inverse Reinforcement Learning."** *ICML 2004*.
- **Key conclusions**: Agents infer reward function (desire) of expert by observing behavior. Structurally mimetic: agent comes to desire what demonstrator desires.
- **Open issues**: Multiple demonstrators with conflicting preferences create complex dynamics.

### 138. Christiano, P., Leike, J., Brown, T., et al. (2017)
**"Deep Reinforcement Learning from Human Feedback."** *NeurIPS 2017*.
- **Key conclusions**: Agents learn reward models from human preferences. Creates chain of mimetic mediation.
- **Open issues**: When multiple humans provide feedback, whose desires dominate? Aggregation has mimetic implications.

### 139. Shah, R., Garg, S., and Dragan, A. (2019)
**"The Implicit Assumptions of Reward Learning."** *NeurIPS Workshop*.
- **Key conclusions**: Reward learning assumes stable, well-defined human preferences. If preferences are mimetically formed, the learning problem is fundamentally different.
- **Open issues**: No explicit Girard engagement but challenges mirror mimetic theory concerns.

### 140. Bak-Coleman, J.B. et al. (2021)
**"Stewardship of Global Collective Behavior."** *PNAS*, 118(27).
- **Key conclusions**: Digital platforms create "high-throughput" environments for social imitation, potentially destabilizing collective behavior. Technology amplifies mimetic contagion.
- **Open issues**: Calls for "crisis discipline" for collective behavior; no specific models provided.

### 141. Watts, D.J. (2002)
**"A Simple Model of Global Cascades on Random Networks."** *PNAS*, 99(9):5766-5771.
- **Key conclusions**: Cascades depend on interaction of individual thresholds and network structure. Sparse, heterogeneous networks vulnerable to large cascades.
- **Open issues**: Binary adoption; continuous desire dynamics more complex.

### 142. Centola, D. (2010)
**"The Spread of Behavior in an Online Social Network Experiment."** *Science*, 329(5996):1194-1198.
- **Key conclusions**: Complex behaviors requiring social reinforcement spread through clustered networks. Mimetic desire often requires repeated exposure.
- **Open issues**: Whether dynamics apply to desire/preference formation.

### 143. Christakis, N.A. and Fowler, J.H. (2007)
**"The Spread of Obesity in a Large Social Network."** *NEJM*, 357(4):370-379.
- **Key conclusions**: Observational evidence that obesity spreads through social networks via norm/behavior influence — mimetic contagion of desires.
- **Open issues**: Homophily may confound results; causal identification debated.

### 144. Flache, A., Mas, M., Feliciani, T., et al. (2017)
**"Models of Social Influence: Towards the Next Frontiers."** *JASSS*, 20(4):2.
- **Key conclusions**: Comprehensive review of opinion dynamics models. Identifies gap: most models treat influence on opinions, not on desires/preferences.
- **Open issues**: Explicitly calls for models of deeper preference-level influence — the domain of mimetic theory.

### 145. DeGroot, M.H. (1974)
**"Reaching a Consensus."** *Journal of the American Statistical Association*, 69(345):118-121.
- **Key conclusions**: Simplest formal model of mimetic convergence: agents repeatedly average opinions with neighbors, converging to consensus.
- **Open issues**: Linear model; cannot produce rivalry or polarization without modification.

### 146. Epstein, J.M. and Axtell, R. (1996)
**"Growing Artificial Societies."** *Brookings/MIT Press*.
- **Key conclusions**: Sugarscape model shows emergence of inequality, migration, conflict, trade from simple rules. "Generative" approach to social science.
- **Open issues**: Fixed exogenous preferences; mimetic desire not modeled.

### 147. Epstein, J.M. (2002)
**"Modeling Civil Violence."** *PNAS*, 99(suppl 3):7243-7250.
- **Key conclusions**: Models how rebellion emerges from citizen-cop-legitimacy interactions. Sudden outbreaks from grievance-risk dynamics.
- **Open issues**: Does not model mimetic/contagion aspect explicitly.

### 148. Axelrod, R. (1997)
**"The Dissemination of Culture."** *Journal of Conflict Resolution*, 41(2):203-226.
- **Key conclusions**: Cultural influence model produces either homogeneity (mimetic convergence) or stable regions (differentiation).
- **Open issues**: Conditions under which cultural interaction leads to rivalry vs. assimilation.

### 149. Hammond, R.A. and Axelrod, R. (2006)
**"The Evolution of Ethnocentrism."** *Journal of Conflict Resolution*, 50(6):926-936.
- **Key conclusions**: Ethnocentric strategies dominate evolutionarily, producing inter-group conflict from simple categorization.
- **Open issues**: Does not explain how in-group/out-group boundaries form; Girard suggests scapegoat mechanism.

### 150. Gavrilets, S. (2015)
**"Collective Action and the Collaborative Brain."** *Journal of the Royal Society Interface*, 12.
- **Key conclusions**: Coalitionary punishment (collective violence against individuals) stabilizes cooperation. Formal analog of scapegoat mechanism.
- **Open issues**: Does not capture mimetic convergence in target selection.

### 151. Helbing, D., Szolnoki, A., Perc, M., and Szabo, G. (various, 2010s)
**"Punishing Free-riders and Second-Order Free-riders."** *Physical Review E* and related journals.
- **Key conclusions**: Antisocial punishment (punishing cooperators) can emerge and persist in evolutionary settings. Target may be innocent.
- **Open issues**: Literature does not engage with Girardian insight about arbitrary victim selection.

### 152. Whitaker, R.M., Colombo, G.B., and Allen, S.M. (2018)
**"A Network Approach to Modelling Ostracism."** *PLOS ONE*.
- **Key conclusions**: Ostracism emerges from local decisions but cascades system-wide.
- **Open issues**: Does not model mimetic convergence driving scapegoating.

### 153. Hofbauer, J. and Sigmund, K. (1998)
**"Evolutionary Games and Population Dynamics."** *Cambridge University Press*.
- **Key conclusions**: Replicator dynamics: strategies spread by imitation of success. Formal mimetic contagion of strategies.
- **Open issues**: Girard's mimetic desire imitates desire itself, not just successful outcomes.

### 154. Szabo, G. and Fath, G. (2007)
**"Evolutionary Games on Graphs."** *Physics Reports*, 446(4-6):97-216.
- **Key conclusions**: Network structure shapes imitation dynamics and cooperation/conflict emergence.
- **Open issues**: Connection to mimetic theory structural but unexplored.

### 155. Rizzolatti, G. and Craighero, L. (2004)
**"The Mirror-Neuron System."** *Annual Review of Neuroscience*, 27:169-192.
- **Key conclusions**: Mirror neurons fire for both action and observation. Cited as neural basis for mimetic theory.
- **Open issues**: May explain motor imitation but not imitation of desire. See Garrels (2011).

### 156. Thiel, P. (2004/2007)
**"The Straussian Moment."** In *Politics and Apocalypse*, ed. Hamerton-Kelly.
- **Key conclusions**: Liberal modernity has not solved mimetic violence but deferred it. Technology amplifies mimetic dynamics.
- **Open issues**: Philosophical, not formal.

### 157. Thiel, P. (2014)
**"Zero to One."** *Crown Business*.
- **Key conclusions**: "Competition is for losers" — Girardian thesis that mimetic rivalry destroys value. Monopoly (differentiation) escapes the mimetic trap.
- **Open issues**: Ethical implications of monopoly seeking.

### 158. Burgis, L. (2021)
**"Wanting: The Power of Mimetic Desire in Everyday Life."** *St. Martin's Press*.
- **Key conclusions**: Popularization of Girard. Distinguishes "thin desires" (mimetically generated) from "thick desires" (authentic).
- **Open issues**: Popular rather than scholarly; thick/thin distinction is Burgis's addition.

### 159. Palaver, W. (2016)
**"Mimetic Theories and Technology."** *Contagion*, 23:1-20.
- **Key conclusions**: Modern technology amplifies mimetic dynamics. Social media intensifies mimetic comparison.
- **Open issues**: No computational models provided.

### 160. Williams, J. (2018)
**"Stand Out of Our Light."** *Cambridge University Press*.
- **Key conclusions**: Attention economy exploits social comparison and mimetic desire.
- **Open issues**: Theoretical; no formal models.

### 161. Zuboff, S. (2019)
**"The Age of Surveillance Capitalism."** *PublicAffairs*.
- **Key conclusions**: Platforms shape behavior through behavioral modification — compatible with mimetic theory framework.
- **Open issues**: Implicit Girard connection; no formal engagement.

### 162. Baker, B., Kanitscheider, I., Markov, T., et al. (2020)
**"Emergent Tool Use from Multi-Agent Autocurricula."** *ICLR 2020*.
- **Key conclusions**: Hide-and-seek agents develop increasingly sophisticated strategies through competitive co-evolution — concrete mimetic escalation.
- **Open issues**: Desires fixed (hide/seek); strategies co-evolve, not goals.

### 163. Dumouchel, P. and Dupuy, J.-P. (1979)
**"L'enfer des choses: René Girard et la logique de l'économie."** *Seuil*.
- **Key conclusions**: Earliest attempt to formalize mimetic desire in economics. Mimetic desire leads to indeterminacy in standard models.
- **Open issues**: No computational implementation; purely analytical.

### 164. Elsenbroich, C. and Gilbert, N. (2014)
**"Modelling Norms."** *Springer*.
- **Key conclusions**: Agent-based models of norm emergence through social imitation and conformity pressure. Maps onto mimetic dynamics.
- **Open issues**: Does not engage with specifically rivalrous/violent aspects.

---

## V. AI Safety, Governance, and Multi-Agent Alignment

### 165. Dafoe, A., Hughes, E., Lanctot, M., et al. (2020/2021)
**"Open Problems in Cooperative AI."** *arXiv:2012.08630 / Nature Human Behaviour*.
- **Key conclusions**: Cooperative AI requires understanding, communication, commitment, and institutions. AI research has over-indexed on competitive benchmarks.
- **Open issues**: Cooperation without trust or transparency; credible commitment for AI.

### 166. Dafoe, A., Bachrach, Y., Hadfield, G., et al. (2021)
**"Cooperative AI: Machines Must Learn to Find Common Ground."** *Nature*, 593(7857):33-36.
- **Key conclusions**: AI must develop cooperative capabilities analogous to human social evolution.
- **Open issues**: Standard cooperative AI benchmarks lacking; cultural norm differences.

### 167. Conitzer, V., Oesterheld, C., and Dafoe, A. (2023)
**"Foundations of Cooperative AI."** *AAAI*.
- **Key conclusions**: Formal foundations using program equilibria and commitment devices. Transparency between AI could enable novel forms of cooperation.
- **Open issues**: Computational tractability; whether real AI systems can meaningfully inspect each other.

### 168. Gabriel, I. (2020)
**"Artificial Intelligence, Values, and Alignment."** *Minds and Machines*, 30:411-437.
- **Key conclusions**: No single alignment approach (instructions, preferences, moral values) is sufficient. Value pluralism central challenge.
- **Open issues**: Genuine moral disagreement in multi-agent alignment.

### 169. Hadfield-Menell, D., Russell, S., Abbeel, P., and Dragan, A. (2016)
**"Cooperative Inverse Reinforcement Learning."** *NeurIPS 2016*.
- **Key conclusions**: Alignment as cooperative game where AI learns human reward through interaction. Optimal strategy involves active information gathering.
- **Open issues**: Multiple humans with conflicting preferences; computational tractability.

### 170. Critch, A. and Krueger, D. (2020)
**"AI Research Considerations for Human Existential Safety (ARCHES)."** *arXiv:2006.04948*.
- **Key conclusions**: Multi/multi alignment (many AIs, many humans) is least studied and most important. Taxonomy of alignment scenarios.
- **Open issues**: Formal models of multi-principal AI dynamics; governance mechanisms.

### 171. Christiano, P. (2019)
**"What Failure Looks Like."** *Alignment Forum*.
- **Key conclusions**: Two catastrophe scenarios: (1) many AIs pursuing slightly wrong objectives causing gradual value erosion; (2) influence-seeking AI. Scenario 1 especially relevant to multi-agent settings.
- **Open issues**: Detecting gradual value drift; whether markets correct or amplify misalignment.

### 172. Dafoe, A. (2018)
**"AI Governance: A Research Agenda."** *Future of Humanity Institute*.
- **Key conclusions**: Comprehensive agenda: technical governance (standards), institutional governance (regulation), structural governance (power dynamics). Identifies pacing problem.
- **Open issues**: Adaptive governance; international coordination; enforcement.

### 173. Cihon, P., Maas, M.M., and Kemp, L. (2020)
**"Should AI Governance Be Centralised?"** *AIES 2020*.
- **Key conclusions**: Historical precedents suggest polycentric governance (multiple overlapping bodies) following Ostrom's approach.
- **Open issues**: Coherence; cross-jurisdictional enforcement.

### 174. Ostrom, E. (1990)
**"Governing the Commons."** *Cambridge University Press*.
- **Key conclusions**: Communities can self-govern shared resources. Eight design principles for common-pool resource institutions widely applied to digital commons and AI.
- **Open issues**: Whether principles for human communities transfer to AI ecosystems.

### 175. Ostrom, E. (2005)
**"Understanding Institutional Diversity."** *Princeton University Press*.
- **Key conclusions**: IAD framework shows institutions are neither purely designed nor purely emergent. Middle path for AI: design frameworks within which norms emerge.
- **Open issues**: Applying IAD where participants are AI agents.

### 176. Rahwan, I. (2018)
**"Society-in-the-Loop."** *Ethics and Information Technology*, 20:5-14.
- **Key conclusions**: Society-in-the-loop extends human-in-the-loop. Democratic processes should be embedded in AI governance.
- **Open issues**: Operationalizing democratic input at scale; deliberation speed vs. deployment pace.

### 177. Anderljung, M., Barnhart, J., et al. (2023)
**"Frontier AI Regulation."** *arXiv:2307.03718*.
- **Key conclusions**: Mandatory risk assessments, pre-deployment safety evaluations, incident reporting proposed.
- **Open issues**: Defining "frontier"; balancing innovation and safety; international harmonization.

### 178. Shoham, Y. and Tennenholtz, M. (1995)
**"On Social Laws for Artificial Agent Societies."** *Artificial Intelligence*, 73(1-2):231-252.
- **Key conclusions**: Multi-agent systems need explicit norms constraining behavior. Formal frameworks for designing social laws.
- **Open issues**: Robustness to diverse agent types; enforcement mechanisms.

### 179. Boella, G., van der Torre, L., and Verhagen, H. (2006)
**"Introduction to Normative Multiagent Systems."** *Computational & Mathematical Organization Theory*, 12:71-79.
- **Key conclusions**: Survey of norm types, enforcement, emergence, and individual-social goal relationships.
- **Open issues**: Bridging formal specifications and practical systems.

### 180. Esteva, M., Rodriguez-Aguilar, J.A., Sierra, C., et al. (2001)
**"On the Formal Specification of Electronic Institutions."** *LNCS 1991*.
- **Key conclusions**: Electronic institutions structure agent interactions with roles, protocols, and norms. ISLANDER specification language.
- **Open issues**: Flexibility vs. rigidity; institutional adaptation.

### 181. Morris-Martin, A., De Vos, M., and Padget, J. (2019)
**"Norm Emergence in Multiagent Systems."** *Autonomous Agents and Multi-Agent Systems*, 33:706-749.
- **Key conclusions**: Norms emerge from imitation, social learning, evolutionary dynamics. No guarantee emerged norms are beneficial.
- **Open issues**: Timescale of emergence vs. governance needs.

### 182. Hadfield, G.K. and Weingast, B.R. (2014)
**"Microfoundations of the Rule of Law."** *Annual Review of Political Science*, 17:21-42.
- **Key conclusions**: Legal order requires shared behavioral classification and decentralized willingness to punish violators.
- **Open issues**: Whether AI agents can develop "shared understandings" for norm enforcement.

### 183. Hadfield, G.K. (2016)
**"Rules for a Flat World."** *Oxford University Press*.
- **Key conclusions**: Competing private regulators providing different rule sets. Applicable to AI governance with multiple frameworks.
- **Open issues**: Quality assurance; access and equity.

### 184. Hayek, F.A. (1945)
**"The Use of Knowledge in Society."** *American Economic Review*, 35(4):519-530.
- **Key conclusions**: Centralized planning cannot aggregate dispersed knowledge. Price mechanisms efficiently aggregate information.
- **Open issues**: AI agents may have different knowledge distribution than humans.

### 185. Hayek, F.A. (1973)
**"Law, Legislation, and Liberty, Vol. 1."** *University of Chicago Press*.
- **Key conclusions**: Designed order (taxis) vs. spontaneous order (cosmos). Most complex social orders emerged spontaneously.
- **Open issues**: Whether AI agent societies resemble designed organizations or spontaneous orders.

### 186. Askell, A., Brundage, M., and Hadfield, G. (2019)
**"The Role of Cooperation in Responsible AI Development."** *arXiv:1907.04534*.
- **Key conclusions**: Safety standards, shared testing, risk info sharing, coordinated deployment. Game theory analysis of when cooperation is stable.
- **Open issues**: Antitrust concerns; free riders; information sharing vs. competitive advantage.

### 187. Bostrom, N. (2014)
**"Superintelligence."** *Oxford University Press*.
- **Key conclusions**: Strategic dynamics of advanced AI: first-mover advantages, decisive strategic advantage, control problem.
- **Open issues**: Whether singleton or multi-agent scenarios more likely.

### 188. Bostrom, N. (2017)
**"Strategic Implications of Openness in AI Development."** *Global Policy*, 8(2):135-148.
- **Key conclusions**: Full openness accelerates races; full secrecy prevents safety collaboration. "Structured access" as middle ground.
- **Open issues**: Optimal openness level.

### 189. Hendrycks, D., Mazeika, M., and Woodside, T. (2023)
**"An Overview of Catastrophic AI Risks."** *arXiv:2306.12001*.
- **Key conclusions**: Risk categories: malicious use, race dynamics, organizational risks, rogue AI. Emergent multi-agent behaviors particularly unpredictable.
- **Open issues**: Risk prioritization.

### 190. Bengio, Y., Hinton, G., et al. (2024)
**"Managing Extreme AI Risks amid Rapid Progress."** *Science*, 384(6698):842-845.
- **Key conclusions**: Mandatory safety evaluations, international oversight, contingency planning. Multi-agent systems create compounding risks.
- **Open issues**: Implementation; international coordination; red lines.

### 191. Bai, Y., Kadavath, S., et al. (2022)
**"Constitutional AI: Harmlessness from AI Feedback."** *arXiv:2212.08073*.
- **Key conclusions**: AI trained on principles ("constitution") rather than solely human feedback. Self-critique and revision loop.
- **Open issues**: Choosing the right constitution; multi-agent extension (shared vs. different constitutions?).

### 192. Park, J.S., O'Brien, J.C., Cai, C.J., et al. (2023)
**"Generative Agents: Interactive Simulacra of Human Behavior."** *UIST 2023*.
- **Key conclusions**: 25 LLM agents exhibit emergent social behaviors: relationships, information spread, event coordination.
- **Open issues**: Fidelity to real behavior; scalability; training data artifacts.

### 193. Horton, J.J. (2023)
**"Large Language Models as Simulated Economic Agents."** *NBER Working Paper 31122*.
- **Key conclusions**: LLMs reproduce human behavioral patterns in experimental economics. "Homo silicus" as modeling complement.
- **Open issues**: LLM biases; calibration to specific populations.

### 194. Hadfield-Menell, D. and Hadfield, G.K. (2019)
**"Incomplete Contracting and AI Alignment."** *AIES 2019*.
- **Key conclusions**: Human-AI relationships are like incomplete contracts. AI should defer to human judgment in ambiguous cases.
- **Open issues**: When deference vs. autonomy is appropriate.

### 195. Russell, S. (2019)
**"Human Compatible."** *Viking*.
- **Key conclusions**: Three principles: AI objective is human preference realization; AI initially uncertain about preferences; AI learns from behavior.
- **Open issues**: Multiple principals with conflicting preferences; computational tractability.

### 196. Cotra, A. (2022)
**"Without Specific Countermeasures, the Easiest Path to Transformative AI Likely Leads to AI Takeover."** *Open Philanthropy*.
- **Key conclusions**: Default training creates principal-agent problem: AI satisfies evaluators rather than pursuing intended objectives.
- **Open issues**: Countermeasures ensuring genuine vs. metric alignment.

### 197. Zwetsloot, R. and Dafoe, A. (2019)
**"Thinking About Risks from AI: Accidents, Misuse, and Structure."**
- **Key conclusions**: Structural risks (from how AI is developed/deployed) are underappreciated. Race dynamics are key structural risk.
- **Open issues**: Addressing structural risks from many-actor interaction.

### 198. Meta FAIR (2022)
**"Human-Level Play in the Game of Diplomacy by Combining Language Models with Strategic Reasoning."** *Science*.
- **Key conclusions**: Cicero achieves human-level Diplomacy requiring natural language negotiation and cooperation.
- **Open issues**: Whether cooperative communication transfers beyond games; manipulation risk.

### 199. Axelrod, R. (1997)
**"The Complexity of Cooperation."** *Princeton University Press*.
- **Key conclusions**: Cooperation sustained through reciprocity, reputation, and spatial structure. Alliances form from simple interaction rules.
- **Open issues**: Transferability to AI agents that can be redesigned.

### 200. Argyle, L.P., et al. (2023)
**"Out of One, Many: Using Language Models to Simulate Human Samples."** *Political Analysis*, 31(3):337-351.
- **Key conclusions**: LLMs prompted with demographics reproduce survey patterns. Potential for simulating public opinion.
- **Open issues**: Representativeness; ethics of simulating specific groups.

### 201. Mguni, D., Jennings, J., and de Cote, E.M. (2018)
**"Decentralised Learning in Systems with Many Strategic Agents."** *AAAI 2018*.
- **Key conclusions**: Principal agent can learn reward transfers incentivizing socially optimal convergence. Must account for agents' learning dynamics.
- **Open issues**: Bilevel optimization is computationally challenging; tension between optimality and robustness.

### 202. Phelps, S. and Wooldridge, M. (2013)
**"Game Theory and Evolution."** *IEEE Intelligent Systems*, 28(4):76-81.
- **Key conclusions**: Multi-agent learning dynamics understood through evolutionary game theory lens. Gradient learning can cycle, producing Pareto-dominated outcomes ("races to the bottom").
- **Open issues**: Connecting evolutionary dynamics theory to practical deep MARL.

### 203. Devlin, S. and Kudenko, D. (2012)
**"Dynamic Potential-Based Reward Shaping."** *AAMAS 2012*.
- **Key conclusions**: Potential-based reward shaping can guide agents toward cooperation without changing optimal policy (under conditions).
- **Open issues**: Requires domain knowledge; guarantees can break in non-stationary settings.

### 204. Artikis, A., Sergot, M., and Pitt, J. (2009)
**"Specifying Norm-Governed Computational Societies."** *ACM Transactions on Computational Logic*, 10(1).
- **Key conclusions**: Formal languages for norms in MAS using event calculus. Specification, monitoring, enforcement demonstrated.
- **Open issues**: Scalability of formal norm specification; norm conflicts.

### 205. Nisioti, E., Briscoe, G., and Prieto-Curiel, R. (2021-2023)
**"Multi-Agent Reinforcement Learning for Climate Cooperation."** *Various workshops*.
- **Key conclusions**: Independently-optimizing RL agents representing nations fail to achieve cooperative climate agreements, converging to tragedy-of-the-commons.
- **Open issues**: Mechanism design for inducing cooperation in shared-resource settings.

### 206. Ouyang, L., Wu, J., et al. (2022)
**"Training Language Models to Follow Instructions with Human Feedback."** *NeurIPS 2022*.
- **Key conclusions**: InstructGPT: RLHF fine-tuning makes models more helpful, honest, harmless.
- **Open issues**: Reward model gaming; optimizing for approval vs. truth.

### 207. Perez, E., et al. (2022)
**"Discovering Language Model Behaviors with Model-Written Evaluations."** *arXiv:2212.09251*.
- **Key conclusions**: LLMs generate evaluations revealing concerning behaviors (sycophancy, power-seeking).
- **Open issues**: Coverage of failure modes; self-referential evaluation.

### 208. Girard, R. (2001)
**"I See Satan Fall Like Lightning."** *Orbis Books*.
- **Key conclusions**: Modern desacralization makes scapegoating harder to sustain but mimetic rivalry intensifies without ritual containment.
- **Open issues**: How modern institutions/technologies interact with mimetic dynamics.

### 209. Palaver, W. (2013)
**"René Girard's Mimetic Theory."** *Michigan State University Press*.
- **Key conclusions**: Comprehensive scholarly introduction to full arc of Girard's thought.

### 210. Dupuy, J.-P. (2014)
**"Economy and the Future: A Crisis of Faith."** *Michigan State University Press*.
- **Key conclusions**: Connects mimetic theory to economics and catastrophe theory.

### 211. Cederman, L.-E. (1997)
**"Emergent Actors in World Politics."** *Princeton University Press*.
- **Key conclusions**: Agent-based models of state formation and war. Conflict emerges from interaction of expanding polities.
- **Open issues**: Micro-level mimetic dynamics not modeled.

### 212. Girard, R. (1990)
**"Innovation and Repetition."** *SubStance*, 19(2/3):7-20.
- **Key conclusions**: Modern culture oscillates between innovation demand and imitation pull. Relevant to AI content generation.
- **Open issues**: Pre-internet era analysis needs updating.

---

*Note: All citations are drawn from established academic literature. Exact page numbers, volume numbers, and publication details should be verified against primary sources before use in formal publications. The literature is rapidly evolving, and works published after early 2025 are not included.*
