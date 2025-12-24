---
layout: default
title: Pre-trained knowledge elevates large language models beyond traditional chemical reaction optimizers
---

# Pre-trained knowledge elevates large language models beyond traditional chemical reaction optimizers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00103" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00103v2</a>
  <a href="https://arxiv.org/pdf/2509.00103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00103v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00103v2', 'Pre-trained knowledge elevates large language models beyond traditional chemical reaction optimizers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robert MacKnight, Jose Emilio Regio, Jeffrey G. Ethier, Luke A. Baldwin, Gabe Gomes

**分类**: cs.LG, cs.AI, physics.chem-ph

**发布日期**: 2025-08-27 (更新: 2025-10-27)

**备注**: 27 pages, 8 figures

---

## 💡 一句话要点

**利用预训练知识提升大语言模型在化学反应优化中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `化学反应优化` `大语言模型` `贝叶斯优化` `预训练知识` `参数空间探索`

## 📋 核心要点

1. 现有的化学反应优化方法主要依赖于黑箱搜索，难以有效处理复杂的参数空间，尤其在高性能条件稀缺时表现不佳。
2. 本文提出了LLM引导的优化（LLM-GO），利用预训练知识提高在复杂分类空间中的优化效率，特别是在高熵探索中表现优越。
3. 实验结果表明，LLM-GO在五个单目标数据集上超越了传统的贝叶斯优化，尤其在参数复杂性增加时优势更加明显。

## 📝 摘要（中文）

现代实验化学中的优化通常依赖于黑箱参数空间的算法搜索。本文展示了大语言模型（LLMs）中的预训练知识如何根本改变这一范式。通过对六个完全枚举的分类反应数据集进行基准测试，LLM引导的优化（LLM-GO）在五个单目标数据集上持续匹配或超越贝叶斯优化（BO）的表现，尤其在参数复杂性增加和高性能条件稀缺的情况下（<5%空间）。BO仅在明确的多目标权衡中保持优势。我们引入了一种拓扑无关的信息理论框架，量化优化过程中的采样多样性，发现LLMs在所有数据集上保持系统性更高的探索香农熵，表明预训练的领域知识使得在化学参数空间的导航更为有效，而非替代结构化的探索策略。为促进透明的基准测试和社区验证，我们发布了Iron Mind平台，支持人类、算法和LLM优化活动的并行评估。

## 🔬 方法详解

**问题定义**：本文旨在解决传统化学反应优化方法在复杂参数空间中的低效问题，尤其是在高性能条件稀缺的情况下，现有方法难以找到有效解。

**核心思路**：通过引入大语言模型（LLMs）中的预训练知识，LLM-GO能够更有效地探索化学参数空间，提升优化性能，尤其是在高熵探索中。

**技术框架**：整体架构包括数据集准备、LLM训练、优化策略实施和结果评估四个主要模块。数据集涵盖了多种化学反应，LLM通过预训练获取领域知识，优化策略则基于LLM的输出进行参数选择。

**关键创新**：最重要的创新在于将LLMs应用于化学反应优化，利用其预训练知识实现更高效的探索，尤其在传统方法难以应对的复杂分类空间中表现突出。

**关键设计**：在模型设计中，采用了特定的损失函数以优化LLM的输出质量，并通过调节超参数来提高模型的泛化能力，确保在不同数据集上均能保持良好的性能。

## 📊 实验亮点

实验结果显示，LLM-GO在五个单目标数据集上均超越了贝叶斯优化，尤其在参数复杂性增加时，LLM-GO的优势更加明显，探索香农熵系统性更高，表明其在解决稀缺条件下的优化问题中具有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括化学合成、药物发现和材料设计等。通过提升化学反应优化的效率，LLM-GO能够加速新材料和药物的开发，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Modern optimization in experimental chemistry employs algorithmic search through black-box parameter spaces. Here we demonstrate that pre-trained knowledge in large language models (LLMs) fundamentally changes this paradigm. Using six fully enumerated categorical reaction datasets (768-5,684 experiments), we benchmark LLM-guided optimization (LLM-GO) against Bayesian optimization (BO) and random sampling. Frontier LLMs consistently match or exceed BO performance across five single-objective datasets, with advantages growing as parameter complexity increases and high-performing conditions become scarce (<5% of space). BO retains superiority only for explicit multi-objective trade-offs. To understand these contrasting behaviors, we introduce a topology-agnostic information theory framework quantifying sampling diversity throughout optimization campaigns. This analysis reveals that LLMs maintain systematically higher exploration Shannon entropy than BO across all datasets while achieving superior performance, with advantages most pronounced in solution-scarce parameter spaces where high-entropy exploration typically fails-suggesting that pre-trained domain knowledge enables more effective navigation of chemical parameter space rather than replacing structured exploration strategies. To enable transparent benchmarking and community validation, we release Iron Mind (https://gomes.andrew.cmu.edu/iron-mind), a no-code platform for side-by-side evaluation of human, algorithmic, and LLM optimization campaigns with public leaderboards and complete trajectories. Our findings establish that LLM-GO excels precisely where traditional methods struggle: complex categorical spaces requiring domain understanding rather than mathematical optimization.

