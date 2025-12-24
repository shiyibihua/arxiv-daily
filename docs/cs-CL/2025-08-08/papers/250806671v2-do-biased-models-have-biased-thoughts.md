---
layout: default
title: Do Biased Models Have Biased Thoughts?
---

# Do Biased Models Have Biased Thoughts?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06671" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06671v2</a>
  <a href="https://arxiv.org/pdf/2508.06671.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06671v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06671v2', 'Do Biased Models Have Biased Thoughts?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Swati Rajwal, Shivank Garg, Reem Abdel-Salam, Abdelrahman Zayed

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-08 (更新: 2025-08-12)

**备注**: Accepted at main track of the Second Conference on Language Modeling (COLM 2025)

---

## 💡 一句话要点

**研究链式思维提示对语言模型偏见的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `偏见研究` `链式思维提示` `公平性评估` `自然语言处理` `模型思维` `实验分析`

## 📋 核心要点

1. 现有语言模型在处理偏见问题时面临挑战，尤其是在性别、种族等方面的偏见影响其输出结果。
2. 本文提出通过链式思维提示的方法，研究模型在生成响应前的思维过程，以评估其公平性。
3. 实验结果显示，模型思维中的偏见与其输出偏见之间的相关性较低，表明模型的决策过程与人类思维存在显著差异。

## 📝 摘要（中文）

语言模型的卓越性能毋庸置疑，但基于性别、种族、社会经济地位、外貌和性取向的偏见使得其部署面临挑战。本文研究了链式思维提示对公平性的影响，探讨了偏见模型是否具有偏见思维。通过对五个流行的大型语言模型进行实验，使用公平性指标量化模型思维和输出中的11种不同偏见。结果表明，思维步骤中的偏见与输出偏见之间的相关性不高（大多数情况下相关性低于0.6，p值小于0.001）。换句话说，与人类不同，测试的偏见决策模型并不总是具有偏见思维。

## 🔬 方法详解

**问题定义**：本文旨在探讨偏见模型是否具有偏见思维，现有方法未能充分揭示模型思维过程与输出之间的关系。

**核心思路**：通过链式思维提示，分析模型在生成响应前的思维步骤，评估其对公平性的影响。此方法能够揭示模型内部的思维过程，提供更深入的理解。

**技术框架**：研究包括数据收集、模型选择、链式思维提示实施、偏见量化和结果分析等主要模块。首先选择五个流行的大型语言模型，然后应用链式思维提示，最后使用公平性指标量化偏见。

**关键创新**：本研究的创新点在于通过链式思维提示揭示模型思维过程与输出之间的关系，挑战了传统对模型偏见的理解，表明模型的思维与输出不一定一致。

**关键设计**：在实验中，采用了11种不同的偏见量化指标，设置了严格的统计分析标准，确保结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，模型思维步骤中的偏见与输出偏见的相关性低于0.6，且大多数情况下p值小于0.001。这一发现表明，偏见决策模型的思维过程与输出结果之间存在显著差异，挑战了传统观点。

## 🎯 应用场景

该研究对自然语言处理领域具有重要的应用价值，尤其是在开发公平性更高的语言模型时。通过理解模型的思维过程，可以更好地设计和优化模型，减少其在实际应用中的偏见，从而提升用户体验和社会责任感。

## 📄 摘要（原文）

> The impressive performance of language models is undeniable. However, the presence of biases based on gender, race, socio-economic status, physical appearance, and sexual orientation makes the deployment of language models challenging. This paper studies the effect of chain-of-thought prompting, a recent approach that studies the steps followed by the model before it responds, on fairness. More specifically, we ask the following question: $\textit{Do biased models have biased thoughts}$? To answer our question, we conduct experiments on $5$ popular large language models using fairness metrics to quantify $11$ different biases in the model's thoughts and output. Our results show that the bias in the thinking steps is not highly correlated with the output bias (less than $0.6$ correlation with a $p$-value smaller than $0.001$ in most cases). In other words, unlike human beings, the tested models with biased decisions do not always possess biased thoughts.

