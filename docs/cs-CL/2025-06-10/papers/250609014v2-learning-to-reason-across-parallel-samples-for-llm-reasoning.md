---
layout: default
title: Learning to Reason Across Parallel Samples for LLM Reasoning
---

# Learning to Reason Across Parallel Samples for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09014" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09014v2</a>
  <a href="https://arxiv.org/pdf/2506.09014.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09014v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09014v2', 'Learning to Reason Across Parallel Samples for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianing Qi, Xi Ye, Hao Tang, Zhigang Zhu, Eunsol Choi

**分类**: cs.CL

**发布日期**: 2025-06-10 (更新: 2025-10-10)

---

## 💡 一句话要点

**提出样本集聚合器以提升大语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理能力` `样本聚合` `强化学习` `数学推理` `模型优化` `数据集实验`

## 📋 核心要点

1. 现有方法在处理多个答案时，往往依赖简单的聚合策略，如多数投票，导致性能提升有限。
2. 本文提出的样本集聚合器（SSA）通过强化学习优化多个样本的聚合过程，旨在提高答案的准确性。
3. 实验结果显示，SSA在多个推理数据集上表现优异，尤其在MATH数据集上比传统方法提升了8%的通过率。

## 📝 摘要（中文）

随着测试时计算能力的提升，大语言模型（LLMs）的性能显著提高。通过对多个答案进行采样并进行启发式聚合（如多数投票或使用验证器对答案进行排序），可以在数学领域实现一致的性能提升。本文提出了一种新的利用多样本集的方法，训练了一个紧凑型的LLM，称为样本集聚合器（SSA），该模型接收多个样本的串联序列并输出最终答案，利用强化学习优化答案的准确性。在五个推理数据集上的实验表明SSA在有效性和效率上的优势，尤其是在MATH数据集上，SSA相较于简单的多数投票提高了8%的通过率。此外，我们的3B SSA在处理奖励模型时超越了更大规模的72B模型。分析结果显示SSA在样本集大小、基础模型家族和任务上的良好泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理任务中对多个答案的聚合效率和准确性不足的问题。现有方法如多数投票在复杂任务中表现不佳，难以充分利用多样本信息。

**核心思路**：论文提出的样本集聚合器（SSA）通过将多个样本的答案串联输入，并利用强化学习优化最终答案的选择，旨在提升聚合结果的准确性和一致性。

**技术框架**：SSA的整体架构包括样本生成模块和聚合模块。样本生成模块负责从基础LLM中生成多个答案，而聚合模块则对这些答案进行分析和优化，最终输出最佳答案。

**关键创新**：SSA的主要创新在于将答案生成与答案聚合分开处理，允许与其他黑箱模型的输出高效结合，显著提升了聚合的灵活性和准确性。

**关键设计**：在设计上，SSA采用了强化学习策略来优化聚合过程，关键参数包括样本数量、奖励函数的设计等，确保模型在多样本环境中能够有效学习并做出准确判断。

## 📊 实验亮点

实验结果显示，SSA在MATH数据集上相较于传统的多数投票方法提高了8%的通过率。此外，3B SSA在处理奖励模型时超越了更大规模的72B模型，展示了其在效率和准确性上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学研究等需要高精度推理的场景。通过提升大语言模型在复杂推理任务中的表现，SSA可以为自动化决策和智能助手提供更可靠的支持，未来可能在多种实际应用中发挥重要作用。

## 📄 摘要（原文）

> Scaling test-time compute brings substantial performance gains for large language models (LLMs). By sampling multiple answers and heuristically aggregate their answers (e.g., either through majority voting or using verifiers to rank the answers), one can achieve consistent performance gains in math domains. In this paper, we propose a new way to leverage such multiple sample set. We train a compact LLM, called Sample Set Aggregator (SSA), that takes a concatenated sequence of multiple samples and output the final answer, optimizing it for the answer accuracy with reinforcement learning. Experiments on five reasoning datasets demonstrate both the efficacy and efficiency of SSA. Notably, SSA improves over naive majority voting by 8% pass@5 on MATH. Furthermore, our 3B SSA surpasses model-based re-ranking with a much larger 72B process reward model. Our analysis also shows promising generalization ability of SSA, across sample set sizes, base model families and scales, and tasks. By separating LLMs to generate answers and LLMs to analyze and aggregate sampled answers, our approach can work with the outputs from premier black box models easily and efficiently.

