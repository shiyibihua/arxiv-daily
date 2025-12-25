---
layout: default
title: Can Agentic AI Match the Performance of Human Data Scientists?
---

# Can Agentic AI Match the Performance of Human Data Scientists?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20959" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20959v1</a>
  <a href="https://arxiv.org/pdf/2512.20959.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20959v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20959v1', 'Can Agentic AI Match the Performance of Human Data Scientists?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: An Luo, Jin Du, Fangqiao Tian, Xun Xian, Robert Specht, Ganghua Wang, Xuan Bi, Charles Fleming, Jayanth Srinivasa, Ashish Kundu, Mingyi Hong, Jie Ding

**分类**: cs.LG, cs.AI, stat.ME

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**Agentic AI在数据科学中能否匹敌人类专家？领域知识至关重要**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agentic AI` `数据科学` `领域知识` `大型语言模型` `图像数据` `预测任务` `人机协作`

## 📋 核心要点

1. 现有agentic AI在数据科学任务中，尤其是在需要领域知识的任务中，性能与人类专家存在差距。
2. 论文设计了一个预测任务，其中关键信息隐藏在图像数据中，以此来模拟需要领域知识才能解决的问题。
3. 实验表明，依赖通用分析流程的agentic AI在处理此类任务时表现不佳，突显了领域知识的重要性。

## 📝 摘要（中文）

数据科学在将复杂数据转化为可执行的洞察方面发挥着关键作用。大型语言模型（LLMs）的最新发展已显著自动化了数据科学工作流程，但一个根本问题仍然存在：这些agentic AI系统能否真正匹敌那些经常利用领域特定知识的人类数据科学家？我们通过设计一个预测任务来探索这个问题，其中一个关键的潜在变量隐藏在相关的图像数据中，而不是表格特征中。因此，为建模表格数据生成通用代码的agentic AI无法表现良好，而人类专家可以使用领域知识识别重要的隐藏变量。我们用财产保险的合成数据集证明了这一想法。我们的实验表明，依赖于通用分析工作流程的agentic AI不如使用领域特定见解的方法。这突出了当前用于数据科学的agentic AI的一个关键局限性，并强调了未来研究开发能够更好识别和整合领域知识的agentic AI系统的必要性。

## 🔬 方法详解

**问题定义**：论文旨在研究当前agentic AI在数据科学任务中，尤其是在需要领域知识的任务中，是否能够达到人类专家的水平。现有agentic AI主要依赖于通用代码和表格数据分析，缺乏对领域知识的有效利用，导致在某些任务中表现不佳。

**核心思路**：论文的核心思路是通过设计一个特殊的预测任务，该任务的关键信息隐藏在图像数据中，而非传统的表格特征中。这样，只有具备相关领域知识的人类专家才能识别出这些隐藏信息，从而做出准确的预测。而缺乏领域知识的agentic AI则难以有效解决该问题。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 构建一个合成数据集，模拟财产保险领域的预测任务；2) 将关键的潜在变量隐藏在图像数据中；3) 使用agentic AI和人类专家分别对该数据集进行建模和预测；4) 比较agentic AI和人类专家的预测性能。

**关键创新**：论文最重要的技术创新点在于其任务设计，即巧妙地将关键信息隐藏在图像数据中，从而模拟了需要领域知识才能解决的实际问题。这种设计能够有效地评估agentic AI在利用领域知识方面的能力，并揭示其与人类专家之间的差距。

**关键设计**：在数据集构建方面，论文使用了合成数据，并控制了数据中的噪声和相关性，以确保实验结果的可靠性。在模型选择方面，论文选择了具有代表性的agentic AI系统，并对其进行了适当的配置和优化。在性能评估方面，论文使用了多种指标，如准确率、召回率和F1值，以全面评估agentic AI和人类专家的预测性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20959v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20959v1/roof_good.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20959v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在关键信息隐藏在图像数据中的预测任务中，依赖通用分析流程的agentic AI的性能明显低于人类专家。这表明，当前agentic AI在利用领域知识方面存在不足，无法有效解决需要领域知识的任务。该研究结果为改进agentic AI系统提供了重要的指导。

## 🎯 应用场景

该研究成果可应用于评估和改进现有agentic AI系统在数据科学领域的应用能力，尤其是在需要领域知识的任务中。通过揭示agentic AI的局限性，可以指导未来的研究方向，例如开发能够更好整合领域知识的agentic AI系统，从而提高其在实际应用中的性能和可靠性。此外，该研究还可以促进人机协作，让人类专家和agentic AI能够更好地协同工作，共同解决复杂的数据科学问题。

## 📄 摘要（原文）

> Data science plays a critical role in transforming complex data into actionable insights across numerous domains. Recent developments in large language models (LLMs) have significantly automated data science workflows, but a fundamental question persists: Can these agentic AI systems truly match the performance of human data scientists who routinely leverage domain-specific knowledge? We explore this question by designing a prediction task where a crucial latent variable is hidden in relevant image data instead of tabular features. As a result, agentic AI that generates generic codes for modeling tabular data cannot perform well, while human experts could identify the important hidden variable using domain knowledge. We demonstrate this idea with a synthetic dataset for property insurance. Our experiments show that agentic AI that relies on generic analytics workflow falls short of methods that use domain-specific insights. This highlights a key limitation of the current agentic AI for data science and underscores the need for future research to develop agentic AI systems that can better recognize and incorporate domain knowledge.

