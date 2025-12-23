---
layout: default
title: Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning
---

# Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11672" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11672v1</a>
  <a href="https://arxiv.org/pdf/2506.11672.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11672v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11672v1', 'Dynamic Mixture of Curriculum LoRA Experts for Continual Multimodal Instruction Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chendi Ge, Xin Wang, Zeyang Zhang, Hong Chen, Jiapei Fan, Longtao Huang, Hui Xue, Wenwu Zhu

**分类**: cs.CV

**发布日期**: 2025-06-13

**备注**: Accepted by ICML 2025

---

## 💡 一句话要点

**提出动态混合课程LoRA专家以解决持续多模态指令调优问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态指令调优` `持续学习` `动态架构` `LoRA专家` `模态不平衡` `任务适应性` `深度学习`

## 📋 核心要点

1. 现有方法采用固定架构，难以适应新任务，面临任务架构冲突和模态不平衡的挑战。
2. 提出动态混合课程LoRA专家（D-MoLE）方法，通过动态分配LoRA专家和调整更新比例来解决上述问题。
3. D-MoLE在多项实验中表现优异，平均提升15%，是首次从架构角度研究多模态大语言模型的持续学习。

## 📝 摘要（中文）

持续的多模态指令调优对于适应不断变化的任务至关重要。然而，现有方法通常采用固定架构，难以适应新任务。本文提出了一种在参数预算下动态演化架构的方法，解决了任务架构冲突和模态不平衡两个挑战。我们提出的动态混合课程LoRA专家（D-MoLE）方法，能够自动演化多模态大语言模型的架构，以持续适应新任务，同时保留已学知识。实验结果表明，D-MoLE在性能上显著优于现有基线，平均提升15%。

## 🔬 方法详解

**问题定义**：本文旨在解决持续多模态指令调优中的架构适应性问题。现有方法由于固定架构，无法有效应对不同任务的需求，导致任务架构冲突和模态不平衡。

**核心思路**：提出动态混合课程LoRA专家（D-MoLE）方法，通过动态分配LoRA专家和调整更新比例，灵活适应新任务，同时保留已有知识。

**技术框架**：D-MoLE的整体架构包括动态层级专家分配器和基于梯度的跨模态持续课程。动态层级专家分配器负责在不同层之间分配LoRA专家，而跨模态持续课程则根据模态难度调整各模块的更新比例。

**关键创新**：D-MoLE的主要创新在于其动态架构演化能力，能够在参数预算内自动适应新任务，解决了传统方法的静态限制。

**关键设计**：在设计中，采用了动态层级专家分配机制和基于任务难度的更新比例调整，确保了在不同模态间的知识共享和更新平衡。

## 📊 实验亮点

D-MoLE在多项实验中表现出色，平均提升15%相较于最佳基线，显示出其在持续学习和多模态指令调优中的显著优势。这一结果表明，D-MoLE在解决任务架构冲突和模态不平衡方面的有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在需要快速适应新任务的多模态系统中，如智能助手、自动驾驶和人机交互等领域。D-MoLE的动态架构演化能力将推动多模态大语言模型在实际应用中的灵活性和效率，提升用户体验。

## 📄 摘要（原文）

> Continual multimodal instruction tuning is crucial for adapting Multimodal Large Language Models (MLLMs) to evolving tasks. However, most existing methods adopt a fixed architecture, struggling with adapting to new tasks due to static model capacity. We propose to evolve the architecture under parameter budgets for dynamic task adaptation, which remains unexplored and imposes two challenges: 1) task architecture conflict, where different tasks require varying layer-wise adaptations, and 2) modality imbalance, where different tasks rely unevenly on modalities, leading to unbalanced updates. To address these challenges, we propose a novel Dynamic Mixture of Curriculum LoRA Experts (D-MoLE) method, which automatically evolves MLLM's architecture with controlled parameter budgets to continually adapt to new tasks while retaining previously learned knowledge. Specifically, we propose a dynamic layer-wise expert allocator, which automatically allocates LoRA experts across layers to resolve architecture conflicts, and routes instructions layer-wisely to facilitate knowledge sharing among experts. Then, we propose a gradient-based inter-modal continual curriculum, which adjusts the update ratio of each module in MLLM based on the difficulty of each modality within the task to alleviate the modality imbalance problem. Extensive experiments show that D-MoLE significantly outperforms state-of-the-art baselines, achieving a 15% average improvement over the best baseline. To the best of our knowledge, this is the first study of continual learning for MLLMs from an architectural perspective.

