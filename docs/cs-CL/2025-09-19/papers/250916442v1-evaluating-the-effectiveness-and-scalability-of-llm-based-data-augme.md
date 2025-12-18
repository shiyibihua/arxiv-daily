---
layout: default
title: Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval
---

# Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16442" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16442v1</a>
  <a href="https://arxiv.org/pdf/2509.16442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16442v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16442v1', 'Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pranjal A. Chitale, Bishal Santra, Yashoteja Prabhu, Amit Sharma

**分类**: cs.IR, cs.CL

**发布日期**: 2025-09-19

**备注**: EMNLP 2025 (MAIN Conference)

---

## 💡 一句话要点

**研究LLM数据增强在检索中的有效性和可扩展性，揭示最优增强策略。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据增强` `信息检索` `大型语言模型` `双编码器` `分布外泛化`

## 📋 核心要点

1. 紧凑型双编码器检索模型因世界知识有限，性能常不及LLM检索模型，数据增强是潜在的解决方案。
2. 论文系统研究LLM数据增强在检索中的有效性，探索最佳增强规模、模型大小和多样性对性能的影响。
3. 实验表明，增强效果随规模增大而递减，小LLM增强可媲美大LLM，且对预训练不足的模型提升更显著。

## 📝 摘要（中文）

紧凑型双编码器模型因其效率和可扩展性而被广泛用于检索。然而，与基于大型语言模型（LLM）的检索模型相比，此类模型的性能通常较差，这可能是由于其有限的世界知识。虽然基于LLM的数据增强已被提出作为弥合这种性能差距的策略，但对其有效性和可扩展性在实际检索问题中的理解不足。现有的研究没有系统地探索关键因素，例如最佳增强规模、使用大型增强模型的必要性，以及多样化的增强是否能提高泛化能力，尤其是在分布外（OOD）设置中。本研究对LLM增强在检索中的有效性进行了全面研究，包括检索模型、增强模型和增强策略的100多个不同的实验设置。我们发现，虽然增强可以提高检索性能，但其益处会超过一定的增强规模而减小，即使采用多样化的增强策略也是如此。令人惊讶的是，我们观察到使用较小的LLM进行增强可以达到与较大的增强模型相媲美的性能。此外，我们研究了增强效果如何随检索模型预训练的变化而变化，发现增强对未经过良好预训练的模型最有益。我们的见解为更明智和高效的增强策略铺平了道路，从而能够做出明智的决策，并在更具成本效益的同时最大限度地提高检索性能。代码和增强数据集可在https://aka.ms/DAGR公开获取。

## 🔬 方法详解

**问题定义**：论文旨在解决紧凑型双编码器检索模型因缺乏世界知识而性能受限的问题。现有方法依赖大型语言模型进行检索，但计算成本高昂。数据增强是一种潜在的解决方案，但如何有效利用LLM进行数据增强，以及其在实际检索场景中的可扩展性尚不明确。现有研究缺乏对增强规模、模型大小和多样性等关键因素的系统性分析。

**核心思路**：论文的核心思路是通过系统性的实验评估，深入理解LLM数据增强对检索性能的影响。通过控制增强规模、选择不同大小的LLM、采用多样化的增强策略，分析这些因素如何影响检索模型的性能，尤其是在分布外（OOD）场景下的泛化能力。目标是找到一种既能提升检索性能，又能兼顾计算效率的LLM数据增强策略。

**技术框架**：论文的技术框架主要包括以下几个部分：1）选择不同的检索模型，包括预训练程度不同的模型；2）使用不同大小的LLM进行数据增强，生成增强后的数据集；3）采用不同的增强策略，例如多样化的增强；4）在不同的数据集上进行实验，包括分布内和分布外的数据集；5）评估检索模型的性能，并分析不同因素对性能的影响。

**关键创新**：论文的关键创新在于对LLM数据增强在检索中的有效性和可扩展性进行了全面的实验研究。通过大量的实验，揭示了以下几个重要的发现：1）增强效果随规模增大而递减；2）小LLM增强可以达到与大LLM相媲美的性能；3）增强对预训练不足的模型提升更显著。这些发现为更明智和高效的增强策略提供了指导。

**关键设计**：论文的关键设计包括：1）构建了包含100多个不同实验设置的实验框架，涵盖了不同的检索模型、增强模型和增强策略；2）系统地评估了增强规模、模型大小和多样性对检索性能的影响；3）特别关注了分布外（OOD）场景下的泛化能力；4）分析了增强效果与检索模型预训练程度之间的关系。

## 📊 实验亮点

实验结果表明，LLM数据增强可以有效提升检索性能，但存在收益递减效应。令人惊讶的是，使用较小的LLM进行增强可以达到与较大的LLM相媲美的性能。此外，增强对预训练不足的检索模型提升效果更明显。这些发现为优化数据增强策略提供了重要依据。

## 🎯 应用场景

该研究成果可应用于各种信息检索场景，例如搜索引擎、问答系统和推荐系统。通过更有效地利用LLM进行数据增强，可以提升检索模型的性能，尤其是在资源受限的情况下。研究结果有助于降低数据增强的成本，并提高检索系统的效率和准确性，从而改善用户体验。

## 📄 摘要（原文）

> Compact dual-encoder models are widely used for retrieval owing to their efficiency and scalability. However, such models often underperform compared to their Large Language Model (LLM)-based retrieval counterparts, likely due to their limited world knowledge. While LLM-based data augmentation has been proposed as a strategy to bridge this performance gap, there is insufficient understanding of its effectiveness and scalability to real-world retrieval problems. Existing research does not systematically explore key factors such as the optimal augmentation scale, the necessity of using large augmentation models, and whether diverse augmentations improve generalization, particularly in out-of-distribution (OOD) settings. This work presents a comprehensive study of the effectiveness of LLM augmentation for retrieval, comprising over 100 distinct experimental settings of retrieval models, augmentation models and augmentation strategies. We find that, while augmentation enhances retrieval performance, its benefits diminish beyond a certain augmentation scale, even with diverse augmentation strategies. Surprisingly, we observe that augmentation with smaller LLMs can achieve performance competitive with larger augmentation models. Moreover, we examine how augmentation effectiveness varies with retrieval model pre-training, revealing that augmentation provides the most benefit to models which are not well pre-trained. Our insights pave the way for more judicious and efficient augmentation strategies, thus enabling informed decisions and maximizing retrieval performance while being more cost-effective. Code and augmented datasets accompanying this work are publicly available at https://aka.ms/DAGR.

