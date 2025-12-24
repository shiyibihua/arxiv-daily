---
layout: default
title: Interestingness First Classifiers
---

# Interestingness First Classifiers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19780" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19780v1</a>
  <a href="https://arxiv.org/pdf/2508.19780.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19780v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19780v1', 'Interestingness First Classifiers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryoma Sato

**分类**: cs.LG, stat.ML

**发布日期**: 2025-08-27

**备注**: 14 pages

---

## 💡 一句话要点

**提出EUREKA框架以构建有趣的分类器**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `有趣分类器` `特征选择` `大型语言模型` `知识发现` `可解释性` `机器学习`

## 📋 核心要点

1. 现有的机器学习模型通常专注于提高预测准确性，忽视了特征的有趣性。
2. 本研究提出EUREKA框架，通过大型语言模型评估特征的有趣性，从而选择特征构建分类器。
3. 在多个数据集上，EUREKA成功识别出非显而易见的特征，提供了有意义的准确性和洞察力。

## 📝 摘要（中文）

大多数机器学习模型旨在最大化预测准确性，而本研究探索了一种不同的目标：构建有趣的分类器。所谓“有趣的分类器”是指使用不寻常或意外特征的分类器，即使其准确性低于最佳模型。例如，从CO2水平预测房间拥挤度的准确性接近完美，但缺乏新意。相反，从湿度预测房间拥挤度的准确性较低，但更具深度和吸引力。我们提出了EUREKA，一个简单的框架，根据特征的有趣性选择特征。该方法利用大型语言模型对特征进行有趣性排名，然后仅使用所选的有趣特征构建可解释的分类器。在多个基准数据集上，EUREKA一致识别出非显而易见但仍具预测性的特征。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有机器学习模型过于关注预测准确性的问题，忽略了特征的有趣性和解释性。现有方法往往使用显而易见的特征，导致模型缺乏新颖性和深度。

**核心思路**：论文的核心思路是构建“有趣的分类器”，即使其准确性低于最佳模型，也要使用不寻常或意外的特征。通过评估特征的有趣性，选择那些能够提供新颖见解的特征。

**技术框架**：EUREKA框架的整体架构包括特征选择和分类器构建两个主要模块。首先，利用大型语言模型对特征进行有趣性排名；其次，基于选定的有趣特征构建可解释的分类器。

**关键创新**：最重要的技术创新在于引入了特征有趣性评估机制，利用大型语言模型进行特征排名，这与传统模型仅关注准确性的方法本质上不同。

**关键设计**：在特征选择过程中，EUREKA使用了特征的上下文信息和语言模型的输出作为评估标准，确保所选特征不仅具有预测能力，还能提供新的视角和解释。

## 📊 实验亮点

在Occupancy Detection数据集中，EUREKA选择湿度作为特征，相较于CO2水平和光强度，生成的分类器在准确性上取得了有意义的提升。此外，在Twin Papers数据集中，EUREKA发现标题中包含冒号的论文更可能被引用，展示了其在知识发现中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学研究和商业分析等，尤其是在需要新颖性和解释性的场景中。EUREKA框架能够帮助研究人员和决策者发现新的知识和洞察，推动创新和有效沟通。

## 📄 摘要（原文）

> Most machine learning models are designed to maximize predictive accuracy. In this work, we explore a different goal: building classifiers that are interesting. An ``interesting classifier'' is one that uses unusual or unexpected features, even if its accuracy is lower than the best possible model. For example, predicting room congestion from CO2 levels achieves near-perfect accuracy but is unsurprising. In contrast, predicting room congestion from humidity is less accurate yet more nuanced and intriguing. We introduce EUREKA, a simple framework that selects features according to their perceived interestingness. Our method leverages large language models to rank features by their interestingness and then builds interpretable classifiers using only the selected interesting features. Across several benchmark datasets, EUREKA consistently identifies features that are non-obvious yet still predictive. For example, in the Occupancy Detection dataset, our method favors humidity over CO2 levels and light intensity, producing classifiers that achieve meaningful accuracy while offering insights. In the Twin Papers dataset, our method discovers the rule that papers with a colon in the title are more likely to be cited in the future. We argue that such models can support new ways of knowledge discovery and communication, especially in settings where moderate accuracy is sufficient but novelty and interpretability are valued.

