---
layout: default
title: Long or short CoT? Investigating Instance-level Switch of Large Reasoning Models
---

# Long or short CoT? Investigating Instance-level Switch of Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04182" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04182v1</a>
  <a href="https://arxiv.org/pdf/2506.04182.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04182v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04182v1', 'Long or short CoT? Investigating Instance-level Switch of Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiqi Zhang, Changyi Xiao, Yixin Cao

**分类**: cs.CL

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出SwitchCoT以解决长短CoT策略选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链式思维` `推理模型` `动态选择` `计算效率` `资源约束`

## 📋 核心要点

1. 现有的长CoT策略在复杂任务中表现优异，但其高令牌消耗使得在资源有限的情况下难以应用。
2. 本文提出SwitchCoT框架，能够根据任务需求和资源情况自动选择长短CoT策略，平衡推理准确性与计算效率。
3. 实验结果显示，SwitchCoT在有限令牌预算下的性能与单独使用长或短CoT相当，甚至更优，同时推理成本降低了50%。

## 📝 摘要（中文）

随着大型推理模型的快速发展，长链式思维（CoT）提示在复杂任务中表现出色，但其代价是显著增加的令牌消耗。本文通过全面的实证分析比较了长短CoT策略，发现长CoT在资源充足时能提高性能，但相较于其高令牌消耗，其收益往往是边际的。短CoT在资源紧张时更为有效。为此，本文提出了SwitchCoT，一个自动化框架，根据任务上下文和资源可用性动态选择合适的CoT策略。实验结果表明，SwitchCoT在保持高准确率的同时，能够将推理成本降低多达50%。

## 🔬 方法详解

**问题定义**：本文旨在解决在不同资源约束下，如何有效选择长短CoT策略的问题。现有方法在资源有限时往往无法充分发挥其潜力，导致性能下降。

**核心思路**：SwitchCoT框架的核心思路是动态选择适合的CoT策略，以适应不同的任务上下文和资源限制，从而提高推理效率和准确性。

**技术框架**：SwitchCoT的整体架构包括任务分析模块、策略选择模块和推理执行模块。任务分析模块评估当前任务的复杂性和资源可用性，策略选择模块根据分析结果选择合适的CoT策略，推理执行模块则负责实际的推理过程。

**关键创新**：SwitchCoT的主要创新在于其动态选择机制，能够在长短CoT之间进行智能切换，而不是固定使用某一种策略。这一设计使得模型在不同场景下都能保持高效性。

**关键设计**：在SwitchCoT中，关键参数包括令牌预算的设定和任务复杂度的评估标准。损失函数设计上，考虑了推理准确性与计算成本的平衡，确保在资源有限的情况下仍能取得良好效果。

## 📊 实验亮点

实验结果表明，SwitchCoT在有限令牌预算下的推理性能与单独使用长或短CoT策略相当，甚至在某些情况下超过了这两者。同时，SwitchCoT能够将推理成本降低多达50%，展现出良好的计算效率。

## 🎯 应用场景

SwitchCoT框架具有广泛的应用潜力，适用于需要高效推理的场景，如自然语言处理、智能问答和自动化决策等领域。其动态选择机制能够根据实际资源情况优化推理过程，提升系统的整体性能和用户体验。未来，该方法有望在更多复杂任务中得到应用，推动推理模型的实用化进程。

## 📄 摘要（原文）

> With the rapid advancement of large reasoning models, long Chain-of-Thought (CoT) prompting has demonstrated strong performance on complex tasks. However, this often comes with a significant increase in token usage. In this paper, we conduct a comprehensive empirical analysis comparing long and short CoT strategies. Our findings reveal that while long CoT can lead to performance improvements, its benefits are often marginal relative to its significantly higher token consumption. Specifically, long CoT tends to outperform when ample generation budgets are available, whereas short CoT is more effective under tighter budget constraints. These insights underscore the need for a dynamic approach that selects the proper CoT strategy based on task context and resource availability. To address this, we propose SwitchCoT, an automatic framework that adaptively chooses between long and short CoT strategies to balance reasoning accuracy and computational efficiency. Moreover, SwitchCoT is designed to be budget-aware, making it broadly applicable across scenarios with varying resource constraints. Experimental results demonstrate that SwitchCoT can reduce inference costs by up to 50% while maintaining high accuracy. Notably, under limited token budgets, it achieves performance comparable to, or even exceeding, that of using either long or short CoT alone.

