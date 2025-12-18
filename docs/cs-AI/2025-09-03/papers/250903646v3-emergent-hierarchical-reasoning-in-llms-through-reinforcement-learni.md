---
layout: default
title: Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning
---

# Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03646" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03646v3</a>
  <a href="https://arxiv.org/pdf/2509.03646.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03646v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03646v3', 'Emergent Hierarchical Reasoning in LLMs through Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haozhe Wang, Qixin Xu, Che Liu, Junhong Wu, Fangzhen Lin, Wenhu Chen

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-03 (更新: 2025-09-27)

**备注**: Preprint

---

## 💡 一句话要点

**提出HICRA算法，通过强化学习提升LLM的层级推理能力，优化策略规划。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `层级推理` `信用分配` `战略规划` `涌现能力` `HICRA算法`

## 📋 核心要点

1. 现有强化学习方法在提升LLM推理能力时，优化压力分配不均，导致学习信号被稀释。
2. 论文提出层级感知信用分配（HICRA）算法，专注于优化高影响力的规划token，提升学习效率。
3. 实验结果表明，HICRA算法显著优于现有基线方法，并提供了关于战略探索如何提升推理能力的深刻见解。

## 📝 摘要（中文）

本文研究表明，强化学习能有效提升大型语言模型（LLM）的复杂推理能力，并揭示了其背后的机制。研究发现，“顿悟时刻”、“长度缩放”和熵动力学等现象并非孤立存在，而是涌现推理层级的标志，类似于人类认知中高层战略规划与低层程序执行的分离。模型学习呈现出两阶段动态：初始阶段受限于程序正确性，必须提升低层技能；随后，学习瓶颈转移到高层战略规划的探索和掌握。针对现有强化学习算法（如GRPO）优化压力分配不均的问题，本文提出层级感知信用分配（HICRA）算法，将优化重点放在高影响力的规划token上。实验验证了HICRA算法的有效性，并深入分析了战略探索视角下的推理能力提升。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在强化学习训练中，由于优化压力分配不均导致的推理能力提升瓶颈问题。现有方法，如GRPO，对所有token施加相同的优化压力，忽略了不同token在推理过程中的重要性差异，导致学习信号被稀释，训练效率低下。

**核心思路**：论文的核心思路是识别并专注于优化对推理结果影响最大的“规划token”。通过将优化重点放在这些高影响力的token上，可以更有效地提升LLM的战略规划能力，从而提高整体的推理性能。这种方法模拟了人类认知中高层战略规划与低层程序执行的分离，旨在更有效地利用强化学习信号。

**技术框架**：HICRA算法的技术框架主要包含以下几个阶段：1) 使用强化学习训练LLM；2) 分析模型在推理过程中的行为，识别对最终结果影响最大的token（即“规划token”）；3) 设计一种信用分配机制，将更多的优化压力分配给这些规划token；4) 使用调整后的优化策略更新模型参数。整体流程旨在引导模型更多地关注战略规划，而非仅仅是程序执行。

**关键创新**：HICRA算法的最重要的技术创新点在于其层级感知的信用分配机制。与现有方法对所有token一视同仁不同，HICRA能够根据token对推理结果的影响程度，动态地调整优化压力。这种差异化的优化策略能够更有效地利用强化学习信号，加速模型的学习过程，并提升其战略规划能力。

**关键设计**：HICRA算法的关键设计包括：1) 如何识别“规划token”：论文可能采用注意力机制或其他方法来评估token的重要性；2) 信用分配策略：如何根据token的重要性来调整优化压力，例如，可以采用加权损失函数或梯度裁剪等技术；3) 损失函数的设计：可能需要设计一种新的损失函数，以鼓励模型更多地关注战略规划，而非仅仅是程序执行。具体的参数设置和网络结构细节需要在论文中查找。

## 📊 实验亮点

实验结果表明，HICRA算法在提升LLM的推理能力方面显著优于现有基线方法。具体的性能数据（例如，在特定推理任务上的准确率提升）需要在论文中查找。通过专注于优化高影响力的规划token，HICRA能够更有效地利用强化学习信号，加速模型的学习过程，并提升其战略规划能力。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如智能问答、游戏AI、自动驾驶决策等。通过提升LLM的战略规划能力，可以使其在复杂环境中做出更明智的决策，提高任务完成的效率和质量。未来，该方法有望推动通用人工智能的发展，使其在更广泛的领域发挥作用。

## 📄 摘要（原文）

> Reinforcement Learning (RL) has proven highly effective at enhancing the complex reasoning abilities of Large Language Models (LLMs), yet underlying mechanisms driving this success remain largely opaque. Our analysis reveals that puzzling phenomena like ``aha moments", ``length-scaling'' and entropy dynamics are not disparate occurrences but hallmarks of an emergent reasoning hierarchy, akin to the separation of high-level strategic planning from low-level procedural execution in human cognition. We uncover a compelling two-phase dynamic: initially, a model is constrained by procedural correctness and must improve its low-level skills. The learning bottleneck then decisively shifts, with performance gains being driven by the exploration and mastery of high-level strategic planning. This insight exposes a core inefficiency in prevailing RL algorithms like GRPO, which apply optimization pressure agnostically and dilute the learning signal across all tokens. To address this, we propose Hierarchy-Aware Credit Assignment (HICRA), an algorithm that concentrates optimization efforts on high-impact planning tokens. Our extensive experiments validate that HICRA significantly outperforms strong baselines, and offer deep insights into how reasoning advances through the lens of strategic exploration.

