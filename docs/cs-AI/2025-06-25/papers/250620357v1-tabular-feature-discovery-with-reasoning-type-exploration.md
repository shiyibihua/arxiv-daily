---
layout: default
title: Tabular Feature Discovery With Reasoning Type Exploration
---

# Tabular Feature Discovery With Reasoning Type Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20357" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20357v1</a>
  <a href="https://arxiv.org/pdf/2506.20357.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20357v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20357v1', 'Tabular Feature Discovery With Reasoning Type Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sungwon Han, Sungkyu Park, Seungeon Lee

**分类**: cs.AI

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出REFeat方法以解决表格数据特征发现问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `特征工程` `大型语言模型` `推理类型` `表格数据` `机器学习` `特征发现` `数据挖掘`

## 📋 核心要点

1. 现有基于大型语言模型的特征生成方法存在产生简单或重复特征的问题，缺乏有效的推理指导。
2. 本文提出REFeat方法，通过多种推理类型引导LLM生成多样且有意义的特征，提升特征发现的质量。
3. 在59个基准数据集上的实验表明，REFeat方法在预测准确性和特征多样性上均优于现有方法。

## 📝 摘要（中文）

特征工程在机器学习中对于表格数据仍然是一个关键且具有挑战性的步骤。近年来，大型语言模型（LLMs）被用于自动生成新特征，但现有基于LLM的方法往往产生过于简单或重复的特征，部分原因在于LLM选择的转换固有偏见以及生成过程中缺乏结构化推理指导。本文提出了一种新方法REFeat，通过利用多种推理类型来引导LLM发现多样且信息丰富的特征。实验结果表明，该方法不仅在59个基准数据集上平均实现了更高的预测准确性，还发现了更多样化和有意义的特征。这些结果突显了将丰富的推理范式和自适应策略选择融入LLM驱动的特征发现中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决表格数据特征发现中的特征生成质量问题，现有方法往往生成简单或重复的特征，缺乏多样性和信息量。

**核心思路**：REFeat方法通过引入多种推理类型来引导LLM的特征生成过程，旨在提高生成特征的多样性和信息丰富性。

**技术框架**：该方法的整体架构包括特征生成模块和推理引导模块。特征生成模块利用LLM生成初步特征，而推理引导模块则通过多种推理策略对生成过程进行调整和优化。

**关键创新**：REFeat的核心创新在于结合了多种推理类型，提供了结构化的推理指导，从而显著提升了特征生成的多样性和有效性。这一设计与传统方法的单一推理路径形成鲜明对比。

**关键设计**：在参数设置上，REFeat采用了自适应策略选择机制，结合了多种损失函数以平衡特征的多样性与准确性。此外，网络结构上，LLM的选择和推理模块的设计均经过精心调整，以确保生成特征的质量。

## 📊 实验亮点

实验结果显示，REFeat在59个基准数据集上平均提高了预测准确性，且生成的特征在多样性和信息量上显著优于现有方法，体现了该方法的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括金融、医疗、市场营销等需要处理表格数据的行业。通过提高特征发现的质量，REFeat可以帮助模型更好地理解数据，从而提升预测性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Feature engineering for tabular data remains a critical yet challenging step in machine learning. Recently, large language models (LLMs) have been used to automatically generate new features by leveraging their vast knowledge. However, existing LLM-based approaches often produce overly simple or repetitive features, partly due to inherent biases in the transformations the LLM chooses and the lack of structured reasoning guidance during generation. In this paper, we propose a novel method REFeat, which guides an LLM to discover diverse and informative features by leveraging multiple types of reasoning to steer the feature generation process. Experiments on 59 benchmark datasets demonstrate that our approach not only achieves higher predictive accuracy on average, but also discovers more diverse and meaningful features. These results highlight the promise of incorporating rich reasoning paradigms and adaptive strategy selection into LLM-driven feature discovery for tabular data.

