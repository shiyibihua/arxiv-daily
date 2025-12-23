---
layout: default
title: Reinforcement learning fine-tuning of language model for instruction following and math reasoning
---

# Reinforcement learning fine-tuning of language model for instruction following and math reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21560" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21560v2</a>
  <a href="https://arxiv.org/pdf/2506.21560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21560v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21560v2', 'Reinforcement learning fine-tuning of language model for instruction following and math reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifu Han, Geo Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-07-27)

---

## 💡 一句话要点

**通过强化学习微调语言模型以提升指令跟随和数学推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `语言模型` `指令跟随` `数学推理` `微调技术` `数据增强` `奖励模型`

## 📋 核心要点

1. 现有方法在指令跟随和数学推理任务上面临挑战，尤其是在模型的对齐性和准确性方面。
2. 论文提出通过强化学习微调技术，结合不同的优化策略来提升小型语言模型的性能。
3. 实验结果显示，RLOO方法在对齐性上表现最佳，而DPO在多个任务上提供了稳定的性能提升。

## 📝 摘要（中文）

本研究探讨了强化学习（RL）微调技术在紧凑型语言模型（Qwen2.5-0.5B Base）上的有效性，针对指令跟随和数学推理这两项挑战性任务进行比较。我们比较了监督微调（SFT）、使用偏好标注数据的直接偏好优化（DPO）和带有奖励模型的强化留一法（RLOO）。实验结果表明，使用DeBERTa奖励建模的RLOO在对齐性上表现最佳，而DPO则提供了强大且一致的结果。在数学推理任务中，合成数据增强和外部验证器的最佳N采样显著提高了准确性，展示了微调与推理时工具结合的潜力。该研究强调了训练轻量级、任务对齐的小规模语言模型的关键权衡和实用策略。

## 🔬 方法详解

**问题定义**：本研究旨在解决小型语言模型在指令跟随和数学推理任务中的性能不足，现有方法在对齐性和准确性上存在明显短板。

**核心思路**：通过强化学习微调技术，结合监督微调和偏好优化策略，提升模型在特定任务上的表现，尤其是通过奖励模型来优化学习过程。

**技术框架**：整体架构包括数据准备、模型训练和评估三个主要阶段。数据准备阶段涉及偏好标注数据的收集，模型训练阶段则应用不同的微调策略，最后通过评估阶段验证模型的性能。

**关键创新**：最重要的技术创新在于引入了RLOO方法与DeBERTa奖励模型的结合，这种方法在对齐性上显著优于传统的微调方法。

**关键设计**：在参数设置上，采用了合成数据增强和最佳N采样策略，结合外部验证器以提高数学推理任务的准确性。损失函数设计上，重点考虑了奖励信号的有效性。

## 📊 实验亮点

实验结果显示，使用DeBERTa奖励模型的RLOO方法在对齐性上达到了最佳效果，而DPO方法在多个任务上表现出强大且一致的性能提升。数学推理任务的准确性通过合成数据增强和最佳N采样策略显著提高，展示了微调与推理工具结合的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能助手和自动化决策系统等。通过提升语言模型在指令跟随和数学推理方面的能力，可以为用户提供更为精准和智能的交互体验，未来可能在多种实际场景中发挥重要作用。

## 📄 摘要（原文）

> This study investigates the effectiveness of reinforcement learning (RL) fine-tuning techniques on a compact language model (Qwen2.5-0.5B Base) for two challenging tasks: instruction following and mathematical reasoning. We compare supervised fine-tuning (SFT), Direct Preference Optimization (DPO) using preference-labeled data, and Reinforce Leave-One-Out (RLOO) with reward models. Our experiments show that RLOO with DeBERTa reward modeling achieves the best alignment, while DPO provides strong and consistent results. For math reasoing tasks, synthetic data augmentation and best-of-N sampling with an external verifier significantly improve accuracy, showing the potential of combining fine-tuning with inference-time tools. This study highlights key trade-offs and practical strategies for training lightweight, task-aligned small-scale language models.

