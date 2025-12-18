---
layout: default
title: A Large-Scale Dataset and Citation Intent Classification in Turkish with LLMs
---

# A Large-Scale Dataset and Citation Intent Classification in Turkish with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21907" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21907v1</a>
  <a href="https://arxiv.org/pdf/2509.21907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21907v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21907v1', 'A Large-Scale Dataset and Citation Intent Classification in Turkish with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kemal Sami Karaca, Bahaeddin Eravcı

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

**备注**: Submitted to IEEE UBMK 2025 International Conference on Computer Science and Engineering

**期刊**: In Proceedings of the 10th International Conference on Computer Science and Engineering (UBMK) 1 (2025) 509-514

**DOI**: [10.1109/UBMK67458.2025.11207038](https://doi.org/10.1109/UBMK67458.2025.11207038)

---

## 💡 一句话要点

**提出土耳其语引文意图分类数据集与框架，利用LLM和DSPy实现91.3%的准确率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `土耳其语NLP` `引文意图分类` `大型语言模型` `DSPy框架` `堆叠泛化` `XGBoost` `数据集构建`

## 📋 核心要点

1. 土耳其语引文意图分类任务面临粘着语的独特挑战，现有方法缺乏有效的数据集和可靠的分类框架。
2. 论文提出基于DSPy框架的可编程分类管道，自动优化LLM提示，并采用堆叠泛化集成提高预测的稳定性和准确性。
3. 实验结果表明，该方法在土耳其语引文意图分类任务上取得了91.3%的准确率，达到了最先进水平。

## 📝 摘要（中文）

理解引文的定性意图对于全面评估学术研究至关重要，但对于像土耳其语这样的粘着语来说，这项任务具有独特的挑战。本文介绍了一种系统的方法和一个基础数据集来解决这个问题。首先，我们提出了一个新的、公开可用的土耳其语引文意图数据集，该数据集是使用专门构建的注释工具创建的。然后，我们评估了大型语言模型（LLM）的标准上下文学习（ICL）的性能，结果表明，其有效性受到手动设计的提示导致的不一致结果的限制。为了解决这个核心限制，我们引入了一个基于DSPy框架的可编程分类管道，该管道可以系统地自动优化提示。对于最终分类，我们采用堆叠泛化集成来聚合来自多个优化模型的输出，从而确保稳定和可靠的预测。该集成使用XGBoost元模型，实现了91.3%的最先进的准确率。最终，这项研究为土耳其语NLP社区和更广泛的学术界提供了一个基础数据集和一个强大的分类框架，为未来的定性引文研究铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决土耳其语引文意图分类问题。现有方法在处理土耳其语这种粘着语时面临挑战，缺乏高质量的标注数据集，并且直接使用大型语言模型（LLM）进行上下文学习（ICL）时，由于手动设计的提示不稳定，导致结果不一致。因此，需要一个更系统、更可靠的分类框架。

**核心思路**：论文的核心思路是利用DSPy框架自动优化LLM的提示，并采用堆叠泛化集成方法，将多个优化后的模型进行组合，从而提高分类的准确性和稳定性。通过自动化提示优化，避免了手动设计提示的不确定性，并通过集成学习减少了单个模型的误差。

**技术框架**：整体框架包含以下几个主要阶段：1) 数据集构建：使用专门的标注工具创建土耳其语引文意图数据集。2) 基于DSPy的提示优化：使用DSPy框架自动搜索和优化LLM的提示，以提高分类性能。3) 模型集成：采用堆叠泛化集成方法，将多个优化后的LLM模型进行组合。4) 元模型训练：使用XGBoost作为元模型，学习如何最佳地组合各个LLM模型的输出。

**关键创新**：最重要的技术创新点在于使用DSPy框架进行自动提示优化，以及采用堆叠泛化集成方法。与传统的手动设计提示相比，DSPy可以系统地搜索和优化提示，从而提高LLM的性能。堆叠泛化集成则可以有效地利用多个模型的优势，提高分类的鲁棒性和准确性。

**关键设计**：在DSPy框架中，论文可能使用了特定的优化目标和搜索策略来寻找最佳提示。在堆叠泛化集成中，XGBoost元模型的选择可能基于其在分类任务中的良好表现。具体参数设置和损失函数等细节可能在论文正文中详细描述，但摘要中未提及。

## 📊 实验亮点

该研究通过结合DSPy框架和堆叠泛化集成，在土耳其语引文意图分类任务上取得了91.3%的准确率，显著优于直接使用LLM进行上下文学习的方法。这一结果表明，自动提示优化和模型集成可以有效提高LLM在特定任务上的性能。

## 🎯 应用场景

该研究成果可应用于学术文献分析、引文网络构建、科研成果评估等领域。通过准确识别引文意图，可以更深入地理解学术研究之间的关系，为科研人员提供更有效的文献检索和分析工具，并为学术评价提供更全面的依据。

## 📄 摘要（原文）

> Understanding the qualitative intent of citations is essential for a comprehensive assessment of academic research, a task that poses unique challenges for agglutinative languages like Turkish. This paper introduces a systematic methodology and a foundational dataset to address this problem. We first present a new, publicly available dataset of Turkish citation intents, created with a purpose-built annotation tool. We then evaluate the performance of standard In-Context Learning (ICL) with Large Language Models (LLMs), demonstrating that its effectiveness is limited by inconsistent results caused by manually designed prompts. To address this core limitation, we introduce a programmable classification pipeline built on the DSPy framework, which automates prompt optimization systematically. For final classification, we employ a stacked generalization ensemble to aggregate outputs from multiple optimized models, ensuring stable and reliable predictions. This ensemble, with an XGBoost meta-model, achieves a state-of-the-art accuracy of 91.3\%. Ultimately, this study provides the Turkish NLP community and the broader academic circles with a foundational dataset and a robust classification framework paving the way for future qualitative citation studies.

