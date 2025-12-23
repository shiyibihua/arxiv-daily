---
layout: default
title: Enhancing Decision-Making of Large Language Models via Actor-Critic
---

# Enhancing Decision-Making of Large Language Models via Actor-Critic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06376" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06376v1</a>
  <a href="https://arxiv.org/pdf/2506.06376.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06376v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06376v1', 'Enhancing Decision-Making of Large Language Models via Actor-Critic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heng Dong, Kefei Duan, Chongjie Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-04

**备注**: Forty-second International Conference on Machine Learning (ICML 2025)

---

## 💡 一句话要点

**提出LAC框架以解决大语言模型决策能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `决策优化` `长期推理` `Actor-Critic` `Q值评估` `无梯度策略` `智能决策` `复杂任务`

## 📋 核心要点

1. 现有方法在复杂决策场景中缺乏长期推理能力，导致决策效果不佳。
2. 本文提出LAC框架，通过计算Q值和无梯度策略改进，提升LLM的决策能力。
3. 实验结果显示，LAC在多种环境中表现优于现有最先进方法，尤其在复杂任务中具有竞争力。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理任务中取得了显著进展，但在需要长期推理和高层次目标对齐的复杂决策场景中面临挑战。现有方法依赖短期自回归动作生成或在准确模拟回滚和评估结果方面存在局限，导致决策次优。本文提出了一种新颖的基于LLM的Actor-Critic框架LAC，有效改善LLM策略，通过长期动作评估以原则性和可扩展的方式解决了两个关键挑战：一是通过与正/负结果相关的token logits计算Q值，提取稳健的动作评估，并通过未来轨迹回滚和推理增强；二是通过无梯度机制实现高效的策略改进。实验结果表明，该框架在多种环境中表现优越，尤其在复杂任务中超越了使用GPT-4的基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂决策场景中长期推理不足的问题。现有方法通常依赖短期决策生成，无法有效评估长期结果，导致决策质量下降。

**核心思路**：提出的LAC框架通过计算与正/负结果相关的Q值，结合未来轨迹回滚，增强了动作评估的稳健性，并采用无梯度机制进行策略改进，从而实现了更优的决策能力。

**技术框架**：LAC框架主要包括两个模块：一是动作评估模块，通过token logits计算Q值；二是策略改进模块，利用无梯度方法优化决策策略。整体流程为：输入环境状态，计算Q值，评估动作，优化策略。

**关键创新**：LAC的核心创新在于结合了长期动作评估与无梯度策略改进机制，显著提升了LLM在复杂决策中的表现。这一设计与传统短期决策生成方法形成了本质区别。

**关键设计**：在技术细节上，LAC使用了与正负结果相关的token logits进行Q值计算，并通过未来轨迹回滚增强评估的准确性。无梯度策略改进机制则避免了复杂的梯度计算，提高了效率。实验中使用了7B/8B参数的LLM，确保了模型的可扩展性。

## 📊 实验亮点

实验结果表明，LAC框架在多种环境中表现优越，尤其在高层次决策任务ALFWorld和复杂任务中，使用7B/8B参数的LLM时，性能超过了基线方法，尤其是使用GPT-4的基线，显示出显著的提升幅度。

## 🎯 应用场景

该研究的潜在应用领域包括智能决策系统、自动化机器人、游戏AI等，能够在需要复杂决策和长期规划的场景中发挥重要作用。通过提升LLM的决策能力，未来可能推动更多智能应用的发展，提升人机交互的智能化水平。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable advancements in natural language processing tasks, yet they encounter challenges in complex decision-making scenarios that require long-term reasoning and alignment with high-level objectives. Existing methods either rely on short-term auto-regressive action generation or face limitations in accurately simulating rollouts and assessing outcomes, leading to sub-optimal decisions. This paper introduces a novel LLM-based Actor-Critic framework, termed LAC, that effectively improves LLM policies with long-term action evaluations in a principled and scalable way. Our approach addresses two key challenges: (1) extracting robust action evaluations by computing Q-values via token logits associated with positive/negative outcomes, enhanced by future trajectory rollouts and reasoning; and (2) enabling efficient policy improvement through a gradient-free mechanism. Experiments across diverse environments -- including high-level decision-making (ALFWorld), low-level action spaces (BabyAI-Text), and large action spaces (WebShop) -- demonstrate the framework's generality and superiority over state-of-the-art methods. Notably, our approach achieves competitive performance using 7B/8B parameter LLMs, even outperforming baseline methods employing GPT-4 in complex tasks. These results underscore the potential of integrating structured policy optimization with LLMs' intrinsic knowledge to advance decision-making capabilities in multi-step environments.

