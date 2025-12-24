---
layout: default
title: Constrained Black-Box Attacks Against Multi-Agent Reinforcement Learning
---

# Constrained Black-Box Attacks Against Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09275" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09275v1</a>
  <a href="https://arxiv.org/pdf/2508.09275.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09275v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09275v1', 'Constrained Black-Box Attacks Against Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amine Andam, Jamal Bentahar, Mustapha Hedabou

**分类**: cs.LG, cs.MA

**发布日期**: 2025-08-12

**备注**: Under review in TNNLS

---

## 💡 一句话要点

**提出约束黑箱攻击方法以解决多智能体强化学习的脆弱性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `对抗攻击` `样本效率` `环境感知` `安全性研究`

## 📋 核心要点

1. 现有方法主要关注训练阶段的攻击或不切实际的假设，缺乏对多智能体强化学习在真实环境中的脆弱性研究。
2. 本文提出了一种新的对抗攻击方法，假设对手只能收集和扰动智能体的观察数据，从而在更现实的条件下进行攻击。
3. 实验结果表明，该方法在22个环境中表现出色，样本效率高，仅需1,000个样本，相较于传统方法显著提升。

## 📝 摘要（中文）

协作多智能体强化学习（c-MARL）迅速发展，为现实应用提供了最先进的算法，但其在对抗攻击下的脆弱性尚未得到充分研究。现有研究主要集中在训练阶段攻击或不切实际的场景，如访问策略权重或训练替代策略。本文在更现实和受限的条件下探讨新的脆弱性，假设对手只能收集和扰动已部署智能体的观察数据。我们提出了简单而高效的算法，用于生成对抗性扰动，旨在误导受害者智能体对环境的感知。通过在三个基准和22个环境中的实证验证，展示了该方法在多种算法和环境中的有效性，并且样本效率高，仅需1,000个样本，相较于以往方法所需的数百万样本显著降低。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体强化学习（c-MARL）在对抗攻击下的脆弱性问题。现有方法多集中于训练阶段的攻击，缺乏对实际部署环境中攻击的研究，导致对手在攻击时的能力受到限制。

**核心思路**：我们提出了一种新的攻击方法，假设对手只能收集和扰动智能体的观察数据。通过设计简单而有效的算法，生成对抗性扰动，误导智能体对环境的感知，从而实现攻击目的。

**技术框架**：我们的框架包括数据收集、扰动生成和攻击实施三个主要模块。首先，收集智能体的观察数据；其次，基于这些数据生成对抗性扰动；最后，将扰动应用于智能体的输入，观察其行为变化。

**关键创新**：本研究的主要创新在于在受限条件下进行对抗攻击，突破了以往方法对训练阶段的依赖。通过仅依赖观察数据，我们的算法能够在实际应用中更具可行性。

**关键设计**：我们在算法设计中关注样本效率，采用了简单的扰动生成策略，确保在仅需1,000个样本的情况下，仍能有效实施攻击。

## 📊 实验亮点

实验结果显示，提出的攻击方法在22个不同环境中均表现出色，样本效率高，仅需1,000个样本，相较于传统方法所需的数百万样本，显著降低了攻击成本，提升了实际应用的可行性。

## 🎯 应用场景

该研究的潜在应用领域包括安全敏感的多智能体系统，如自动驾驶、金融交易和智能制造等。通过识别和缓解对抗攻击的脆弱性，可以提高这些系统的安全性和可靠性，推动其在实际应用中的广泛采用。

## 📄 摘要（原文）

> Collaborative multi-agent reinforcement learning (c-MARL) has rapidly evolved, offering state-of-the-art algorithms for real-world applications, including sensitive domains. However, a key challenge to its widespread adoption is the lack of a thorough investigation into its vulnerabilities to adversarial attacks. Existing work predominantly focuses on training-time attacks or unrealistic scenarios, such as access to policy weights or the ability to train surrogate policies. In this paper, we investigate new vulnerabilities under more realistic and constrained conditions, assuming an adversary can only collect and perturb the observations of deployed agents. We also consider scenarios where the adversary has no access at all. We propose simple yet highly effective algorithms for generating adversarial perturbations designed to misalign how victim agents perceive their environment. Our approach is empirically validated on three benchmarks and 22 environments, demonstrating its effectiveness across diverse algorithms and environments. Furthermore, we show that our algorithm is sample-efficient, requiring only 1,000 samples compared to the millions needed by previous methods.

