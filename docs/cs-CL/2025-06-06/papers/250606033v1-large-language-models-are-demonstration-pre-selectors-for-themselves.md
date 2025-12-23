---
layout: default
title: Large Language Models are Demonstration Pre-Selectors for Themselves
---

# Large Language Models are Demonstration Pre-Selectors for Themselves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06033" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06033v1</a>
  <a href="https://arxiv.org/pdf/2506.06033.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06033v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06033v1', 'Large Language Models are Demonstration Pre-Selectors for Themselves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiarui Jin, Yuwei Wu, Haoxuan Li, Xiaoting He, Weinan Zhang, Yiming Yang, Yong Yu, Jun Wang, Mengyue Yang

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: ICML 2025

---

## 💡 一句话要点

**提出FEEDER框架以提高大语言模型的示例选择效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `上下文学习` `示例选择` `预选择框架` `训练效率` `双层优化` `树形算法`

## 📋 核心要点

1. 现有的ICL方法在选择示例时计算成本高，需重复从大规模数据集中检索，效率低下。
2. 本文提出FEEDER框架，通过预选择代表性示例子集，降低计算成本并提高效率。
3. 实验表明，FEEDER能将训练数据大小减少超过20%，同时保持与完整数据集相当的性能。

## 📝 摘要（中文）

在上下文学习（ICL）中，大语言模型（LLMs）通过从整个训练数据中选择少量示例来实现强大的少样本性能。然而，现有的ICL方法依赖于相似性或多样性评分来选择示例，这导致在每个查询中都需从大规模数据集中重复检索，造成高计算成本。为此，本文提出了FEEDER（少量但必要的示例预选择器），一个新颖的预选择框架，旨在识别包含训练数据中最具代表性的示例的子集。通过引入“充分性”和“必要性”指标，并设计基于树的算法来高效识别代表性示例，FEEDER能够有效替代完整训练数据，提高效率，同时在ICL中保持可比性能。此外，该预选择子集还可用于微调LLMs，采用双层优化方法提升训练效率而不牺牲性能。实验结果表明，FEEDER能够将训练数据大小减少超过20%，同时保持性能，并与多种下游示例选择策略无缝集成。

## 🔬 方法详解

**问题定义**：本文旨在解决现有ICL方法在示例选择中计算成本高的问题。现有方法依赖于相似性或多样性评分，导致在每次查询时都需重复检索大规模数据集，效率低下。

**核心思路**：FEEDER框架的核心思路是通过预选择一个包含最具代表性示例的子集，来替代完整的训练数据集，从而提高示例选择的效率。通过引入“充分性”和“必要性”指标，FEEDER能够高效识别出最具代表性的示例。

**技术框架**：FEEDER的整体架构包括预选择阶段和后续的示例选择阶段。预选择阶段使用树形算法来识别代表性示例，而后续阶段则利用这些示例进行上下文学习。

**关键创新**：FEEDER的主要创新在于引入了“充分性”和“必要性”指标，并设计了高效的树形算法来进行示例的预选择。这一方法与现有依赖相似性评分的选择方法本质上不同，显著提高了效率。

**关键设计**：在设计中，FEEDER采用了双层优化方法以提升训练效率，确保在微调过程中不牺牲性能。具体的参数设置和损失函数设计尚未详细说明，可能为未知。

## 📊 实验亮点

实验结果显示，FEEDER能够将训练数据大小减少超过20%，同时在不同参数规模的LLMs（从300M到8B参数）上保持性能，展现出良好的适应性。此外，FEEDER与多种下游示例选择策略的无缝集成，进一步增强了其实用性。

## 🎯 应用场景

FEEDER框架具有广泛的应用潜力，尤其在需要高效示例选择的自然语言处理任务中，如文本生成、问答系统和对话系统等。通过提高示例选择的效率，FEEDER能够加速模型训练过程，降低计算资源消耗，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In-context learning (ICL) with large language models (LLMs) delivers strong few-shot performance by choosing few-shot demonstrations from the entire training data. However, existing ICL methods, which rely on similarity or diversity scores to choose demonstrations, incur high computational costs due to repeatedly retrieval from large-scale datasets for each query. To this end, we propose FEEDER (FEw yet Essential Demonstration prE-selectoR), a novel pre-selection framework that identifies a representative subset of demonstrations containing the most representative examples in the training data, tailored to specific LLMs. To construct this subset, we introduce the "sufficiency" and "necessity" metrics in the pre-selection stage and design a tree-based algorithm to identify representative examples efficiently. Once pre-selected, this representative subset can effectively replace the full training data, improving efficiency while maintaining comparable performance in ICL. Additionally, our pre-selected subset also benefits fine-tuning LLMs, where we introduce a bi-level optimization method that enhances training efficiency without sacrificing performance. Experiments with LLMs ranging from 300M to 8B parameters show that FEEDER can reduce training data size by over 20% while maintaining performance and seamlessly integrating with various downstream demonstration selection strategies in ICL.

