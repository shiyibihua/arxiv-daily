---
layout: default
title: Parallel Continuous Chain-of-Thought with Jacobi Iteration
---

# Parallel Continuous Chain-of-Thought with Jacobi Iteration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18582" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18582v1</a>
  <a href="https://arxiv.org/pdf/2506.18582.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18582v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18582v1', 'Parallel Continuous Chain-of-Thought with Jacobi Iteration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyi Wu, Zhihao Teng, Kewei Tu

**分类**: cs.CL

**发布日期**: 2025-06-23

**备注**: under review

**🔗 代码/项目**: [GITHUB](https://github.com/whyNLP/PCCoT)

---

## 💡 一句话要点

**提出并行连续思维链方法以提升推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `并行计算` `连续思维链` `雅可比迭代` `推理效率` `自然语言处理` `模型训练` `智能系统`

## 📋 核心要点

1. 现有的连续思维链方法由于潜在思维令牌的顺序依赖性，导致训练效率低下，训练时间较长。
2. 本文提出的PCCoT通过雅可比迭代实现潜在思维令牌的并行更新，克服了顺序依赖性的问题。
3. 实验结果显示，PCCoT在节省近50%训练和推理时间的同时，性能可比甚至优于传统方法，且训练过程更稳定。

## 📝 摘要（中文）

连续思维链（CoT）在大型语言模型中已被证明能够有效节省推理令牌。然而，潜在思维令牌之间的顺序依赖性影响了并行训练，导致训练时间较长。本文提出了并行连续思维链（PCCoT），通过对潜在思维令牌进行雅可比迭代，实现并行更新，从而提高了连续CoT的训练和推理效率。实验表明，通过选择适当的迭代次数，PCCoT能够在节省近50%训练和推理时间的同时，达到可比甚至更好的性能。此外，PCCoT在训练过程中表现出更好的稳定性和鲁棒性。代码可在https://github.com/whyNLP/PCCoT获取。

## 🔬 方法详解

**问题定义**：本文旨在解决现有连续思维链方法在训练过程中由于潜在思维令牌的顺序依赖性而导致的低效率问题。现有方法在推理时需要依赖于前一个令牌的输出，限制了并行处理的能力，导致训练时间过长。

**核心思路**：PCCoT的核心思路是通过雅可比迭代对潜在思维令牌进行并行更新，而非顺序更新。这种设计允许多个令牌同时进行计算，从而显著提高训练和推理的效率。

**技术框架**：PCCoT的整体架构包括潜在思维令牌的初始化、雅可比迭代更新过程以及最终的推理阶段。每个潜在思维令牌在每次迭代中都能并行更新，减少了计算时间。

**关键创新**：PCCoT的主要创新在于引入了雅可比迭代方法，使得潜在思维令牌的更新过程可以并行进行。这一方法与传统的顺序更新方式本质上不同，极大地提升了计算效率。

**关键设计**：在设计中，PCCoT需要设置适当的迭代次数，以确保在节省时间的同时不损失性能。此外，损失函数的选择和网络结构的设计也对最终效果有重要影响。

## 📊 实验亮点

实验结果显示，PCCoT在选择合适的迭代次数后，能够在节省近50%的训练和推理时间的同时，达到与传统方法相当甚至更优的性能。这一成果表明，PCCoT在稳定性和鲁棒性方面也有显著提升，进一步验证了其有效性。

## 🎯 应用场景

PCCoT的研究成果在自然语言处理、对话系统和智能问答等领域具有广泛的应用潜力。通过提高推理效率，该方法能够支持更大规模的模型训练和实时推理，推动智能系统的快速响应和高效运行。未来，PCCoT可能会在多模态学习和复杂推理任务中发挥更大作用。

## 📄 摘要（原文）

> Continuous chain-of-thought has been shown to be effective in saving reasoning tokens for large language models. By reasoning with continuous latent thought tokens, continuous CoT is able to perform implicit reasoning in a compact manner. However, the sequential dependencies between latent thought tokens spoil parallel training, leading to long training time. In this paper, we propose Parallel Continuous Chain-of-Thought (PCCoT), which performs Jacobi iteration on the latent thought tokens, updating them iteratively in parallel instead of sequentially and thus improving both training and inference efficiency of continuous CoT. Experiments demonstrate that by choosing the proper number of iterations, we are able to achieve comparable or even better performance while saving nearly 50% of the training and inference time. Moreover, PCCoT shows better stability and robustness in the training process. Our code is available at https://github.com/whyNLP/PCCoT.

