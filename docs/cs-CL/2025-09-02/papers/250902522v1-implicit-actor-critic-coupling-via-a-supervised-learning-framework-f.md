---
layout: default
title: Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR
---

# Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02522" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02522v1</a>
  <a href="https://arxiv.org/pdf/2509.02522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02522v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02522v1', 'Implicit Actor Critic Coupling via a Supervised Learning Framework for RLVR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaming Li, Longze Chen, Ze Gong, Yukun Chen, Lu Wang, Wanwei He, Run Luo, Min Yang

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-02

**🔗 代码/项目**: [GITHUB](https://github.com/ritzz-ai/PACS)

---

## 💡 一句话要点

**提出PACS框架，通过监督学习隐式耦合Actor-Critic，提升RLVR中LLM的推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `可验证奖励` `大型语言模型` `监督学习` `策略梯度` `Actor-Critic` `数学推理`

## 📋 核心要点

1. 现有RLVR方法在奖励稀疏和策略梯度更新不稳定方面存在挑战，尤其是在基于强化学习的方法中。
2. PACS框架将RLVR问题转化为监督学习任务，通过预测奖励标签隐式耦合Actor和Critic，实现更稳定的训练。
3. 实验表明，PACS在数学推理任务上优于PPO和GRPO等基线，显著提升了LLM的推理性能。

## 📝 摘要（中文）

本文提出了一种名为PACS的新型RLVR框架，旨在解决现有RLVR方法中奖励稀疏和策略梯度更新不稳定等问题。PACS通过将结果奖励视为可预测的标签，将RLVR问题转化为一个监督学习任务，该任务基于由策略模型参数化的评分函数，并使用交叉熵损失进行优化。详细的梯度分析表明，这种监督学习形式在本质上恢复了经典的策略梯度更新，同时隐式地耦合了actor和critic的角色，从而实现了更稳定和高效的训练。在具有挑战性的数学推理任务上的基准测试表明，PACS优于强大的RLVR基线方法，例如PPO和GRPO，实现了卓越的推理性能。例如，PACS在AIME 2025上实现了59.78%的pass@256，比PPO和GRPO分别提高了13.32和14.36个百分点。这种简单而强大的框架为LLM基于可验证奖励的后训练提供了一个有希望的途径。

## 🔬 方法详解

**问题定义**：论文旨在解决RLVR（Reinforcement Learning with Verifiable Rewards）框架下，大型语言模型（LLMs）在处理复杂推理任务时，由于奖励信号稀疏和策略梯度更新不稳定而导致的训练困难问题。现有方法，如基于强化学习的PPO和GRPO，难以有效利用可验证的奖励来指导策略优化，限制了LLMs在数学和编程等领域的应用。

**核心思路**：PACS的核心思路是将RLVR问题重新表述为一个监督学习问题。具体来说，它将可验证的结果奖励视为一个可预测的标签，然后训练一个评分函数（由策略模型参数化）来预测这个标签。通过这种方式，PACS将强化学习中的策略优化问题转化为一个监督学习中的分类问题，从而可以利用交叉熵损失等成熟的监督学习技术进行训练。

**技术框架**：PACS的整体框架包括以下几个主要步骤：1) 给定一个输入问题，LLM生成一个候选答案。2) 使用可验证的奖励函数评估该答案，得到一个奖励值。3) 将该奖励值视为一个监督学习的标签。4) 使用策略模型参数化的评分函数预测该标签。5) 使用交叉熵损失函数优化评分函数，从而隐式地更新策略模型。这个过程迭代进行，直到策略模型收敛。

**关键创新**：PACS最重要的技术创新在于它通过监督学习框架实现了Actor-Critic的隐式耦合。传统的Actor-Critic方法需要分别训练Actor（策略模型）和Critic（价值函数），而PACS通过将奖励预测问题转化为监督学习问题，使得Actor和Critic的角色在训练过程中自然地协同工作。这种隐式耦合避免了传统Actor-Critic方法中可能出现的训练不稳定问题。

**关键设计**：PACS的关键设计包括：1) 使用策略模型直接作为评分函数，避免了引入额外的网络结构。2) 使用交叉熵损失函数作为优化目标，简化了训练过程。3) 通过梯度分析证明了该方法在本质上等价于传统的策略梯度更新，保证了算法的收敛性。具体参数设置和网络结构的选择取决于具体的LLM和任务。

## 📊 实验亮点

PACS在AIME 2025数学推理任务上取得了显著的性能提升，pass@256指标达到59.78%，相比于PPO和GRPO基线分别提高了13.32和14.36个百分点。实验结果表明，PACS框架能够更有效地利用可验证的奖励信号，提升LLMs的推理能力，并在复杂任务中表现出更强的鲁棒性和泛化能力。

## 🎯 应用场景

PACS框架具有广泛的应用前景，可用于提升LLMs在需要可验证奖励的复杂推理任务中的表现，例如数学问题求解、代码生成、逻辑推理等。该方法能够有效利用外部反馈来指导LLMs的训练，提高其输出结果的可靠性和准确性，从而在教育、科研、软件开发等领域发挥重要作用。

## 📄 摘要（原文）

> Recent advances in Reinforcement Learning with Verifiable Rewards (RLVR) have empowered large language models (LLMs) to tackle challenging reasoning tasks such as mathematics and programming. RLVR leverages verifiable outcome rewards to guide policy optimization, enabling LLMs to progressively improve output quality in a grounded and reliable manner. Despite its promise, the RLVR paradigm poses significant challenges, as existing methods often suffer from sparse reward signals and unstable policy gradient updates, particularly in RL-based approaches. To address the challenges, we propose $\textbf{PACS}$, a novel RLVR framework that achieves im$\textbf{P}$licit $\textbf{A}$ctor $\textbf{C}$ritic coupling via a $\textbf{S}$upervised learning framework. By treating the outcome reward as a predictable label, we reformulate the RLVR problem into a supervised learning task over a score function parameterized by the policy model and optimized using cross-entropy loss. A detailed gradient analysis shows that this supervised formulation inherently recovers the classical policy gradient update while implicitly coupling actor and critic roles, yielding more stable and efficient training. Benchmarking on challenging mathematical reasoning tasks, PACS outperforms strong RLVR baselines, such as PPO and GRPO, achieving superior reasoning performance. For instance, PACS achieves 59.78\% at pass@256 on AIME 2025, representing improvements of 13.32 and 14.36 points over PPO and GRPO. This simple yet powerful framework offers a promising avenue for LLMs post-training with verifiable rewards. Our code and data are available as open source at https://github.com/ritzz-ai/PACS.

