---
layout: default
title: Understanding protein function with a multimodal retrieval-augmented foundation model
---

# Understanding protein function with a multimodal retrieval-augmented foundation model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04724" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04724v1</a>
  <a href="https://arxiv.org/pdf/2508.04724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04724v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04724v1', 'Understanding protein function with a multimodal retrieval-augmented foundation model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timothy Fei Truong, Tristan Bepler

**分类**: q-bio.QM, cs.LG

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出PoET-2以解决蛋白质功能预测的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `蛋白质语言模型` `多模态建模` `检索增强` `变体效应预测` `生物信息学` `结构预测` `生成模型`

## 📋 核心要点

1. 现有的蛋白质语言模型在突变理解和功能预测的表示质量上存在不足，限制了其应用效果。
2. 本文提出的PoET-2模型通过多模态和检索增强的方法，结合进化约束和结构信息，提升蛋白质序列的生成能力。
3. PoET-2在零样本变体效应预测中表现出色，尤其在小数据集上，其嵌入效果超越了以往方法。

## 📝 摘要（中文）

蛋白质语言模型（PLMs）通过学习数亿条自然蛋白质序列的概率分布，逐渐具备蛋白质理解和设计能力。尽管现有模型在结构预测上表现良好，但在突变理解和功能预测的表示质量上仍存在不足。为此，本文提出了PoET-2，这是一种多模态、检索增强的蛋白质基础模型，结合了家族特定的进化约束和可选的结构条件，以学习蛋白质序列的生成分布。PoET-2采用了层次化的变换器编码器，能够处理序列上下文顺序的等变性，并具备因果和掩蔽语言建模目标的双解码器架构，支持完全生成和双向表示学习模式。PoET-2在零样本变体效应预测上达到了最先进的性能，尤其在处理多突变和挑战性插入缺失突变时表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有蛋白质语言模型在突变理解和功能预测中的不足，尤其是在小数据集上的表现不佳。

**核心思路**：PoET-2通过结合多模态信息和检索增强技术，利用家族特定的进化约束和结构条件来学习蛋白质序列的生成分布，从而提高模型的预测能力。

**技术框架**：PoET-2的整体架构包括层次化的变换器编码器和双解码器，支持因果和掩蔽语言建模目标，能够在生成和双向表示学习模式下运作。

**关键创新**：PoET-2的主要创新在于其检索增强的多模态建模方法，能够有效结合进化信息与结构信息，显著提升蛋白质功能预测的准确性。

**关键设计**：在网络结构上，PoET-2采用了层次化的变换器编码器，设计了双解码器架构，并使用了特定的损失函数来优化生成和表示学习的效果。具体参数设置和训练策略在实验中进行了详细验证。

## 📊 实验亮点

PoET-2在零样本变体效应预测中达到了最先进的性能，尤其在处理多突变和插入缺失突变时表现优异。与以往方法相比，其在小数据集上的嵌入效果显著提升，展示了检索增强和多模态建模的优势。

## 🎯 应用场景

PoET-2模型在生物信息学、药物设计和基因工程等领域具有广泛的应用潜力。通过提高蛋白质功能预测的准确性，能够加速新药的研发和蛋白质工程的进展，推动生物技术的创新与发展。

## 📄 摘要（原文）

> Protein language models (PLMs) learn probability distributions over natural protein sequences. By learning from hundreds of millions of natural protein sequences, protein understanding and design capabilities emerge. Recent works have shown that scaling these models improves structure prediction, but does not seem to improve mutation understanding and representation quality for protein function prediction. We introduce PoET-2, a multimodal, retrieval-augmented protein foundation model that incorporates in-context learning of family-specific evolutionary constraints with optional structure conditioning to learn generative distributions over protein sequences. PoET-2 uses a hierarchical transformer encoder that is equivariant to sequence context ordering and a dual decoder architecture with both causal and masked language modeling objectives, allowing PoET-2 to operate in both fully generative and bidirectional representation learning modes. PoET-2 achieves state-of-the-art performance on zero-shot variant effect prediction, excelling at scoring variants with multiple mutations and challenging indel mutations. In supervised settings, PoET-2 embeddings outperform previous methods for learning sequence-function relationships, especially with small datasets. This work highlights the benefits of combining retrieval augmentation with multimodal, family-centric modeling for advancing protein foundation models.

