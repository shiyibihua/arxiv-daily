---
layout: default
title: Scaling Algorithm Distillation for Continuous Control with Mamba
---

# Scaling Algorithm Distillation for Continuous Control with Mamba

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13892" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13892v1</a>
  <a href="https://arxiv.org/pdf/2506.13892.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13892v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13892v1', 'Scaling Algorithm Distillation for Continuous Control with Mamba')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samuel Beaussant, Mehdi Mounsif

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出Mamba以解决算法蒸馏在连续控制中的效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `算法蒸馏` `连续控制` `选择性结构` `长序列建模` `元强化学习` `自回归模型` `变换器模型`

## 📋 核心要点

1. 现有的算法蒸馏方法在处理长时间序列时受到变换器模型的平方复杂度限制，导致性能瓶颈。
2. 本文提出Mamba模型，利用选择性结构状态空间序列（S6）模型，能够在长序列建模中实现线性扩展，提升算法蒸馏效率。
3. 实验结果表明，Mamba在四个复杂的连续元强化学习环境中表现优越，且在长上下文下的ICRL性能显著提升。

## 📝 摘要（中文）

算法蒸馏（AD）最近被提出作为一种通过因果变换器模型自回归地建模跨情节训练历史的新方法。然而，由于注意力机制引发的实际限制，实验受到变换器的平方复杂度的瓶颈，限制在简单的离散环境和短时间范围内。本文提出利用最近提出的选择性结构状态空间序列（S6）模型，该模型在长序列建模上实现了最先进的性能，同时在序列长度上线性扩展。通过四个复杂的连续元强化学习环境，我们展示了基于S6层构建的Mamba模型在AD任务上相较于变换器模型的整体优越性。此外，我们还表明，将AD扩展到非常长的上下文可以提高ICRL性能，使其在与最先进的在线元RL基线竞争时更具竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有算法蒸馏（AD）方法在长时间序列建模中的效率问题，尤其是变换器模型的平方复杂度限制导致的性能瓶颈。

**核心思路**：论文提出Mamba模型，基于选择性结构状态空间序列（S6）模型，能够在长序列建模中实现线性扩展，从而提高算法蒸馏的效率和效果。

**技术框架**：Mamba模型的整体架构包括多个S6层，能够有效处理长时间序列数据。模型通过自回归方式建模跨情节的训练历史，优化了信息的传递和利用。

**关键创新**：Mamba模型的核心创新在于引入S6模型，突破了传统变换器模型的复杂度限制，使得在长上下文下的算法蒸馏成为可能，显著提升了性能。

**关键设计**：在模型设计中，S6层的选择性结构允许模型在处理长序列时保持线性复杂度，此外，损失函数和训练策略经过优化，以适应连续控制任务的需求。

## 📊 实验亮点

实验结果显示，Mamba模型在四个复杂的连续元强化学习环境中表现优越，相较于传统变换器模型，性能提升显著，尤其是在长上下文的ICRL任务中，Mamba的表现与最先进的在线元RL基线相竞争，展示了其强大的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏AI等需要处理复杂决策和长时间序列的场景。通过提高算法蒸馏的效率，Mamba模型能够在实际应用中实现更高效的学习和决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Algorithm Distillation (AD) was recently proposed as a new approach to perform In-Context Reinforcement Learning (ICRL) by modeling across-episodic training histories autoregressively with a causal transformer model. However, due to practical limitations induced by the attention mechanism, experiments were bottlenecked by the transformer's quadratic complexity and limited to simple discrete environments with short time horizons. In this work, we propose leveraging the recently proposed Selective Structured State Space Sequence (S6) models, which achieved state-of-the-art (SOTA) performance on long-range sequence modeling while scaling linearly in sequence length. Through four complex and continuous Meta Reinforcement Learning environments, we demonstrate the overall superiority of Mamba, a model built with S6 layers, over a transformer model for AD. Additionally, we show that scaling AD to very long contexts can improve ICRL performance and make it competitive even with a SOTA online meta RL baseline.

