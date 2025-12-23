---
layout: default
title: Layer Importance for Mathematical Reasoning is Forged in Pre-Training and Invariant after Post-Training
---

# Layer Importance for Mathematical Reasoning is Forged in Pre-Training and Invariant after Post-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22638" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22638v2</a>
  <a href="https://arxiv.org/pdf/2506.22638.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22638v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22638v2', 'Layer Importance for Mathematical Reasoning is Forged in Pre-Training and Invariant after Post-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aadim Nepal, Safal Shrestha, Anubhav Shrestha, Minwu Kim, Jalal Naghiyev, Ravid Shwartz-Ziv, Keith Ross

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-27 (更新: 2025-11-05)

---

## 💡 一句话要点

**提出层重要性分析以优化数学推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学推理` `层级消融` `大型语言模型` `预训练` `后训练` `归一化互信息` `模型优化`

## 📋 核心要点

1. 现有方法在数学推理能力提升上存在不确定性，难以判断是结构性变化还是小幅调整导致的。
2. 论文通过层级消融实验，揭示数学推理依赖于少数关键层，这些层在预训练中形成并保持稳定。
3. 实验结果表明，移除关键层会导致数学准确率下降80%，而事实回忆任务的下降幅度较小，显示出层的重要性。

## 📝 摘要（中文）

大型语言模型在经过指令调优、强化学习或知识蒸馏后，数学能力有所提升。本文探讨这些提升是否源于变换器层的重大变化，还是仅仅是保持原有结构的小调整。通过对基础和训练变体的层级消融实验，发现数学推理依赖于少数关键层，这些层在所有后训练方法中保持重要性。移除这些层会导致数学准确率下降多达80%，而事实回忆任务的下降幅度相对较小。这表明，针对数学任务的专用层在预训练期间形成，并在后续保持稳定。通过归一化互信息（NMI）测量，发现接近这些关键层的标记从原始句法簇漂移，朝向与句法关系较弱但对下游任务更有用的表示。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型在数学推理能力提升的机制，现有方法未能明确层级变化与性能提升之间的关系。

**核心思路**：通过层级消融实验，分析不同层对数学推理的贡献，验证关键层在预训练和后训练中的稳定性。

**技术框架**：研究采用层级消融技术，对基础模型和经过训练的变体进行比较，重点关注数学推理相关的关键层。

**关键创新**：发现数学推理依赖于少数关键层，这些层在预训练阶段形成并在后续训练中保持重要性，区别于传统方法对所有层的均匀处理。

**关键设计**：实验中使用归一化互信息（NMI）来测量层级间的关系，分析标记在关键层附近的漂移现象，揭示其对下游任务的影响。

## 📊 实验亮点

实验结果显示，移除关键层导致数学准确率下降多达80%，而在事实回忆任务中，下降幅度相对较小。这一发现强调了特定层在数学推理中的重要性，提供了对模型结构优化的新思路。

## 🎯 应用场景

该研究为大型语言模型在数学推理方面的优化提供了新的视角，具有广泛的应用潜力，尤其是在教育、自动化推理和智能问答系统等领域。未来，基于关键层的设计可以进一步提升模型在复杂推理任务中的表现。

## 📄 摘要（原文）

> Large language models improve at math after instruction tuning, reinforcement learning, or knowledge distillation. We ask whether these gains come from major changes in the transformer layers or from smaller adjustments that keep the original structure. Using layer-wise ablation on base and trained variants, we find that math reasoning depends on a few critical layers, which stay important across all post-training methods. Removing these layers reduces math accuracy by as much as 80%, whereas factual recall tasks only show relatively smaller drops. This suggests that specialized layers for mathematical tasks form during pre-training and remain stable afterward. As measured by Normalized Mutual Information (NMI), we find that near these critical layers, tokens drift from their original syntactic clusters toward representations aligned with tokens less syntactically related but potentially more useful for downstream task.

