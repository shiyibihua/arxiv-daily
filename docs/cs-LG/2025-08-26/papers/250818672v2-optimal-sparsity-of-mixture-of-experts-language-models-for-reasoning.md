---
layout: default
title: Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks
---

# Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18672" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18672v2</a>
  <a href="https://arxiv.org/pdf/2508.18672.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18672v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18672v2', 'Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taishi Nakamura, Satoki Ishikawa, Masaki Kawamura, Takumi Okamoto, Daisuke Nohara, Jun Suzuki, Rio Yokota

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-26 (更新: 2025-09-25)

**备注**: Presented at the Second AI for Math Workshop at ICML

**🔗 代码/项目**: [GITHUB](https://github.com/rioyokotalab/optimal-sparsity)

---

## 💡 一句话要点

**提出混合专家模型的最优稀疏性以提升推理任务性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家模型` `稀疏性` `推理任务` `记忆能力` `大规模语言模型` `活跃计算量` `每参数总令牌数`

## 📋 核心要点

1. 现有的稠密模型在处理大规模语言模型时忽视了稀疏性对推理能力的影响。
2. 论文提出通过训练不同配置的MoE模型，探讨活跃计算量和TPP对推理和记忆任务的影响。
3. 实验结果显示，活跃计算量和TPP的优化共同决定了MoE模型的性能，推翻了传统计算最优缩放的观点。

## 📝 摘要（中文）

随着大规模语言模型（LLMs）的发展，混合专家（MoE）模型引入了一种新的稀疏性维度。本文研究了MoE稀疏性对记忆和推理能力的影响，通过训练不同参数配置的MoE模型，揭示了活跃计算量和每参数总令牌数（TPP）对推理任务的重要性。研究结果表明，具有相同训练损失但更高活跃计算的模型在推理准确性上表现更佳，而记忆任务则随着参数增加而改善，推理任务则需优化TPP，表明推理任务对数据的需求较高。本文的模型检查点、代码和日志已开源。

## 🔬 方法详解

**问题定义**：本文旨在解决混合专家模型在推理任务中的稀疏性如何影响模型性能的问题。现有方法未能充分考虑稀疏性对推理能力的影响，导致模型性能不理想。

**核心思路**：通过训练不同参数配置的MoE模型，分析活跃计算量和每参数总令牌数（TPP）对推理和记忆任务的影响，从而优化模型的稀疏性设计。

**技术框架**：研究采用了多种MoE模型配置，分别调整总参数、活跃参数和top-k路由，保持固定的计算预算。通过对比训练损失和下游准确性，揭示了稀疏性对模型性能的影响。

**关键创新**：提出了活跃计算量和TPP共同决定MoE模型性能的理论，挑战了传统的计算最优缩放观念，强调了推理任务对数据的需求。

**关键设计**：在实验中，模型的训练损失保持一致，但通过调整活跃计算量，观察到推理准确性显著提升。同时，记忆任务随着参数增加而改善，推理任务则需优化TPP以达到最佳效果。

## 📊 实验亮点

实验结果表明，具有相同训练损失的模型，活跃计算量更高的情况下推理准确性显著提升。此外，记忆任务随着参数增加而改善，而推理任务则需优化TPP，表明推理任务对数据的需求较高。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过优化MoE模型的稀疏性，可以在保持高效计算的同时，提升模型在推理任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Empirical scaling laws have driven the evolution of large language models (LLMs), yet their coefficients shift whenever the model architecture or data pipeline changes. Mixture-of-Experts (MoE) models, now standard in state-of-the-art systems, introduce a new sparsity dimension that current dense-model frontiers overlook. We investigate how MoE sparsity influences two distinct capability regimes: memorization skills and reasoning skills. By training MoE families that vary total parameters, active parameters, and top-$k$ routing under fixed compute budgets, we disentangle pre-training loss from downstream accuracy. Our results reveal two principles. First, Active FLOPs: models with identical training loss but greater active compute achieve higher reasoning accuracy. Second, Total tokens per parameter (TPP): memorization tasks improve with more parameters, while reasoning tasks benefit from optimal TPP, indicating that reasoning is data-hungry. Neither reinforcement learning post-training (GRPO) nor increased test-time compute alters these trends. We therefore argue that optimal MoE sparsity must be determined jointly by active FLOPs and TPP, revising the classical picture of compute-optimal scaling. Our model checkpoints, code and logs are open-source at https://github.com/rioyokotalab/optimal-sparsity.

