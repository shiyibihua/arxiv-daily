---
layout: default
title: Masked Language Models are Good Heterogeneous Graph Generalizers
---

# Masked Language Models are Good Heterogeneous Graph Generalizers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06157" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06157v2</a>
  <a href="https://arxiv.org/pdf/2506.06157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06157v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06157v2', 'Masked Language Models are Good Heterogeneous Graph Generalizers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinyu Yang, Cheng Yang, Shanyuan Cui, Zeyuan Guo, Liangwei Yang, Muhan Zhang, Zhiqiang Zhang, Chuan Shi

**分类**: cs.SI, cs.CL

**发布日期**: 2025-06-06 (更新: 2025-07-30)

**🔗 代码/项目**: [GITHUB](https://github.com/BUPT-GAMMA/MLM4HG)

---

## 💡 一句话要点

**提出MLM4HG以解决异构图泛化能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `异构图神经网络` `掩码语言建模` `跨领域学习` `多任务学习` `图表示学习`

## 📋 核心要点

1. 现有的HGNNs在跨领域和任务的泛化能力上存在显著不足，影响了其在实际应用中的效果。
2. 本文提出的MLM4HG方法通过使用基于元路径的文本序列替代HG标记，旨在提升模型的泛化能力。
3. 在四个真实数据集上的跨领域和多任务实验中，MLM4HG在少样本和零样本场景下均优于现有最先进的方法。

## 📝 摘要（中文）

异构图神经网络（HGNNs）在捕捉异构图（HGs）的结构和语义信息方面表现出色，但在跨领域和任务的泛化能力上存在不足。随着大型语言模型（LLMs）的快速发展，近期研究探索了HGNNs与LLMs的结合以实现可泛化的异构图学习。然而，现有方法通常将结构信息编码为HG标记，导致HGNNs与LLMs之间的嵌入空间差异影响LLMs对HGs的理解。为此，本文提出了一种简单而有效的基于掩码语言建模的方法MLM4HG，通过引入基于元路径的文本序列来提取HGs中的结构和语义信息，并设计定制的文本模板，将不同图任务统一为连贯的填空式“掩码”标记预测范式。实验结果表明，MLM4HG在多个真实数据集上表现出优越的泛化性能。

## 🔬 方法详解

**问题定义**：本文旨在解决异构图神经网络在跨领域和任务泛化能力不足的问题。现有方法通常依赖于HG标记，导致HGNNs与LLMs之间的嵌入空间差异，影响了模型的理解能力。

**核心思路**：论文提出的MLM4HG方法通过引入基于元路径的文本序列，替代传统的HG标记，从而提取HGs中的结构和语义信息，并设计统一的文本模板，以实现不同图任务的连贯性。

**技术框架**：MLM4HG的整体架构包括三个主要阶段：首先，将来自不同领域的HGs转换为基于元路径的文本；其次，将这些文本与统一的任务文本结合，形成HG基础语料库；最后，将该语料库输入预训练语言模型进行微调。

**关键创新**：MLM4HG的核心创新在于使用基于元路径的文本序列替代HG标记，这一设计有效解决了HGNNs与LLMs之间的嵌入空间差异问题，提升了模型的泛化能力。

**关键设计**：在模型设计中，MLM4HG采用了定制的文本模板和约束目标词汇，以确保模型在微调过程中能够有效学习到HGs的结构和语义信息。

## 📊 实验亮点

在四个真实数据集上的实验结果显示，MLM4HG在少样本和零样本场景下的泛化性能显著优于现有最先进的方法，具体提升幅度达到了XX%（具体数据待补充），验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、推荐系统、知识图谱构建等。通过提升异构图的泛化能力，MLM4HG能够在多种实际场景中提供更准确的分析和预测，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Heterogeneous graph neural networks (HGNNs) excel at capturing structural and semantic information in heterogeneous graphs (HGs), while struggling to generalize across domains and tasks. With the rapid advancement of large language models (LLMs), a recent study explored the integration of HGNNs with LLMs for generalizable heterogeneous graph learning. However, this approach typically encodes structural information as HG tokens using HGNNs, and disparities in embedding spaces between HGNNs and LLMs have been shown to bias the LLM's comprehension of HGs. Moreover, since these HG tokens are often derived from node-level tasks, the model's ability to generalize across tasks remains limited. To this end, we propose a simple yet effective Masked Language Modeling-based method, called MLM4HG. MLM4HG introduces metapath-based textual sequences instead of HG tokens to extract structural and semantic information inherent in HGs, and designs customized textual templates to unify different graph tasks into a coherent cloze-style 'mask' token prediction paradigm. Specifically,MLM4HG first converts HGs from various domains to texts based on metapaths, and subsequently combines them with the unified task texts to form a HG-based corpus. Moreover, the corpus is fed into a pretrained LM for fine-tuning with a constrained target vocabulary, enabling the fine-tuned LM to generalize to unseen target HGs. Extensive cross-domain and multi-task experiments on four real-world datasets demonstrate the superior generalization performance of MLM4HG over state-of-the-art methods in both few-shot and zero-shot scenarios. Our code is available at https://github.com/BUPT-GAMMA/MLM4HG.

