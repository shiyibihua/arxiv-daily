---
layout: default
title: Hierarchical Text Classification Using Black Box Large Language Models
---

# Hierarchical Text Classification Using Black Box Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04219" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04219v1</a>
  <a href="https://arxiv.org/pdf/2508.04219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04219v1', 'Hierarchical Text Classification Using Black Box Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kosuke Yoshimura, Hisashi Kashima

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-06

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**利用黑箱大语言模型进行层次文本分类以应对数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `层次文本分类` `黑箱模型` `大语言模型` `提示策略` `少样本学习` `数据稀缺` `机器学习`

## 📋 核心要点

1. 层次文本分类面临数据稀缺和模型复杂性等挑战，传统方法依赖大量标注数据。
2. 本研究提出利用黑箱大语言模型，通过API实现层次文本分类，探索不同提示策略的有效性。
3. 实验结果显示，少样本设置显著提高分类准确性，LLMs在深层次标签层次上优于传统模型。

## 📝 摘要（中文）

层次文本分类（HTC）旨在将文本分配到结构化标签层次中，但由于数据稀缺和模型复杂性面临挑战。本研究探索通过API访问黑箱大语言模型（LLMs）在HTC中的可行性，作为传统机器学习方法的替代方案。我们评估了三种提示策略——直接叶标签预测（DL）、直接层次标签预测（DH）和自上而下多步层次标签预测（TMH），在零样本和少样本设置下比较这些策略的准确性和成本效益。实验表明，少样本设置在分类准确性上始终优于零样本设置。尽管传统机器学习模型在浅层次数据集上表现良好，但LLMs，尤其是DH策略，在深层次数据集上往往超越机器学习模型。API成本因深层标签层次所需的更高输入标记而显著增加。这些结果强调了准确性提升与提示策略计算成本之间的权衡。

## 🔬 方法详解

**问题定义**：本论文旨在解决层次文本分类中的数据稀缺和模型复杂性问题。传统机器学习方法需要大量标注数据，难以适应深层次标签层次的需求。

**核心思路**：本研究提出利用黑箱大语言模型，通过API进行层次文本分类，探索不同的提示策略以提高分类准确性和降低成本。

**技术框架**：整体架构包括数据输入、提示策略选择、模型调用和结果输出。主要模块包括直接叶标签预测（DL）、直接层次标签预测（DH）和自上而下多步层次标签预测（TMH）。

**关键创新**：本研究的创新点在于将黑箱LLMs应用于层次文本分类，尤其是DH策略在深层次标签层次上超越传统机器学习模型，展示了新的应用潜力。

**关键设计**：在提示策略中，DL、DH和TMH的设计考虑了输入标记的数量和层次结构的复杂性，尤其是DH策略在深层次标签层次上的表现，需关注API调用的成本。

## 📊 实验亮点

实验结果表明，在少样本设置下，分类准确性显著提高，尤其是在深层次标签层次上，DH策略的表现优于传统机器学习模型。具体而言，LLMs在深层次数据集上的准确性提升幅度明显，尽管API成本也随之增加。

## 🎯 应用场景

该研究的潜在应用领域包括文本分类、信息检索和内容推荐等。通过利用黑箱大语言模型，能够在数据稀缺的情况下实现高效的层次文本分类，具有实际价值。未来，随着模型和计算资源的进步，该方法可能在更多领域得到广泛应用。

## 📄 摘要（原文）

> Hierarchical Text Classification (HTC) aims to assign texts to structured label hierarchies; however, it faces challenges due to data scarcity and model complexity. This study explores the feasibility of using black box Large Language Models (LLMs) accessed via APIs for HTC, as an alternative to traditional machine learning methods that require extensive labeled data and computational resources. We evaluate three prompting strategies -- Direct Leaf Label Prediction (DL), Direct Hierarchical Label Prediction (DH), and Top-down Multi-step Hierarchical Label Prediction (TMH) -- in both zero-shot and few-shot settings, comparing the accuracy and cost-effectiveness of these strategies. Experiments on two datasets show that a few-shot setting consistently improves classification accuracy compared to a zero-shot setting. While a traditional machine learning model achieves high accuracy on a dataset with a shallow hierarchy, LLMs, especially DH strategy, tend to outperform the machine learning model on a dataset with a deeper hierarchy. API costs increase significantly due to the higher input tokens required for deeper label hierarchies on DH strategy. These results emphasize the trade-off between accuracy improvement and the computational cost of prompt strategy. These findings highlight the potential of black box LLMs for HTC while underscoring the need to carefully select a prompt strategy to balance performance and cost.

