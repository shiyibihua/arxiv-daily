---
layout: default
title: Flow-Based Single-Step Completion for Efficient and Expressive Policy Learning
---

# Flow-Based Single-Step Completion for Efficient and Expressive Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21427" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21427v2</a>
  <a href="https://arxiv.org/pdf/2506.21427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21427v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21427v2', 'Flow-Based Single-Step Completion for Efficient and Expressive Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prajwal Koirala, Cody Fleming

**分类**: cs.LG, cs.RO

**发布日期**: 2025-06-26 (更新: 2025-07-23)

---

## 💡 一句话要点

**提出单步完成策略以提高离线强化学习效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `离线强化学习` `生成模型` `流匹配` `单步完成策略` `目标条件强化学习` `演员-评论家` `高效决策` `多模态动作生成`

## 📋 核心要点

1. 现有生成模型在离线强化学习中存在高推理成本和训练不稳定性的问题，影响了其应用效果。
2. 本文提出的单步完成策略（SSCP）通过增强流匹配目标，直接生成动作，提升了生成效率。
3. SSCP在多个标准基准测试中表现优异，相较于扩散基线显著提高了速度和适应性。

## 📝 摘要（中文）

生成模型如扩散和流匹配在离线强化学习中提供了丰富的多模态动作分布，但其迭代采样导致高推理成本和训练不稳定。本文提出了单步完成策略（SSCP），通过增强的流匹配目标直接预测完成向量，实现准确的一次性动作生成。SSCP结合了生成模型的表现力与单模态策略的训练和推理效率，避免了长时间的反向传播链。该方法在离线、离线到在线及在线强化学习设置中有效扩展，显著提升了速度和适应性。SSCP还扩展到目标条件强化学习，使平面策略能够利用子目标结构而无需显式的层次推理。该方法在标准的离线强化学习和行为克隆基准测试中表现出色，成为深度强化学习和序列决策的多功能、高效框架。

## 🔬 方法详解

**问题定义**：本文旨在解决现有生成模型在离线强化学习中由于迭代采样导致的高推理成本和训练不稳定性的问题。现有方法需要长时间的反向传播，影响了训练效率。

**核心思路**：单步完成策略（SSCP）通过增强的流匹配目标，直接从中间流样本预测完成向量，实现一次性动作生成，避免了长时间的反向传播链。

**技术框架**：SSCP在离线演员-评论家框架中运作，结合了生成模型的表现力与单模态策略的高效性。该方法包括生成模型训练、动作生成和策略优化等主要模块。

**关键创新**：SSCP的核心创新在于其一次性动作生成能力，显著提高了生成效率，并且在目标条件强化学习中能够利用子目标结构，避免了显式层次推理。

**关键设计**：在设计上，SSCP采用了增强的流匹配目标作为损失函数，网络结构上则结合了生成模型与演员-评论家架构，确保了高效的训练和推理过程。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在标准的离线强化学习和行为克隆基准测试中，SSCP相较于扩散基线在速度和适应性上实现了显著提升，具体性能数据表明其在多个任务中均表现优异，验证了其作为高效框架的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏AI等，能够在复杂环境中实现高效的决策制定。通过提高离线强化学习的效率，SSCP有望推动智能体在真实世界中的应用，提升其适应性和灵活性。

## 📄 摘要（原文）

> Generative models such as diffusion and flow-matching offer expressive policies for offline reinforcement learning (RL) by capturing rich, multimodal action distributions, but their iterative sampling introduces high inference costs and training instability due to gradient propagation across sampling steps. We propose the \textit{Single-Step Completion Policy} (SSCP), a generative policy trained with an augmented flow-matching objective to predict direct completion vectors from intermediate flow samples, enabling accurate, one-shot action generation. In an off-policy actor-critic framework, SSCP combines the expressiveness of generative models with the training and inference efficiency of unimodal policies, without requiring long backpropagation chains. Our method scales effectively to offline, offline-to-online, and online RL settings, offering substantial gains in speed and adaptability over diffusion-based baselines. We further extend SSCP to goal-conditioned RL, enabling flat policies to exploit subgoal structures without explicit hierarchical inference. SSCP achieves strong results across standard offline RL and behavior cloning benchmarks, positioning it as a versatile, expressive, and efficient framework for deep RL and sequential decision-making.

