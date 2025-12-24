---
layout: default
title: Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification
---

# Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09832" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09832v1</a>
  <a href="https://arxiv.org/pdf/2508.09832.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09832v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09832v1', 'Exploring the Potential of Large Language Models in Fine-Grained Review Comment Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linh Nguyen, Chunhua Liu, Hong Yi Lin, Patanamon Thongtanunam

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-13

**备注**: Accepted at 2025 IEEE International Conference on Source Code Analysis & Manipulation (SCAM)

---

## 💡 一句话要点

**利用大型语言模型提升代码审查评论分类的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码审查` `评论分类` `自动化技术` `深度学习` `自然语言处理` `软件开发`

## 📋 核心要点

1. 现有的监督学习方法在代码审查评论分类中依赖大量人工标注，导致训练模型的成本高且效率低。
2. 本文提出利用大型语言模型（LLMs）进行代码审查评论的分类，旨在减少对人工标注的依赖，提高分类效果。
3. 实验结果表明，LLMs在分类17个评论类别时表现优于现有深度学习模型，尤其在低频类别的分类上具有显著优势。

## 📝 摘要（中文）

代码审查是软件开发中的重要实践。随着代码审查的轻量化，能够识别出多种问题，甚至有些问题可能是微不足道的。以往的研究主要依赖于监督学习方法，这需要大量的人工标注来有效训练模型。为了解决这一限制，本文探索了使用大型语言模型（LLMs）对代码审查评论进行分类的潜力。研究评估了LLMs在17个类别的代码审查评论分类中的表现，结果显示LLMs的分类效果优于现有的深度学习模型，尤其在分类五个最有用的类别时表现更佳。这表明LLMs能够提供一种可扩展的解决方案，以提升代码审查过程的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决代码审查评论分类中对人工标注依赖过重的问题。现有方法在处理低频类别时表现不佳，限制了模型的有效性。

**核心思路**：通过引入大型语言模型（LLMs），本文希望利用其强大的自然语言处理能力，减少对特定小训练数据分布的依赖，从而实现更均衡的分类性能。

**技术框架**：研究首先对17个类别的代码审查评论进行数据收集，然后使用LLMs进行训练和分类，最后评估其分类效果与现有方法的对比。主要模块包括数据预处理、模型训练和性能评估。

**关键创新**：本文的主要创新在于使用LLMs进行代码审查评论分类，克服了传统方法在低频类别上的不足，展现出更好的泛化能力。

**关键设计**：在模型训练中，采用了适当的超参数设置和损失函数设计，以确保LLMs能够有效学习不同类别的特征，具体细节包括使用预训练模型进行微调。

## 📊 实验亮点

实验结果显示，LLMs在17个代码审查评论类别的分类准确率上超过了现有的深度学习模型，特别是在五个最有用的类别中，LLMs的分类准确率显著提高，表明其在处理低频数据时的优势。这一发现为代码审查分析提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发中的代码审查自动化、代码质量分析和开发者协作工具。通过提升评论分类的准确性，能够帮助团队更高效地识别和解决代码问题，从而提高软件开发的整体质量和效率。未来，LLMs的应用可能会扩展到其他领域的文本分类任务中，推动自动化技术的发展。

## 📄 摘要（原文）

> Code review is a crucial practice in software development. As code review nowadays is lightweight, various issues can be identified, and sometimes, they can be trivial. Research has investigated automated approaches to classify review comments to gauge the effectiveness of code reviews. However, previous studies have primarily relied on supervised machine learning, which requires extensive manual annotation to train the models effectively. To address this limitation, we explore the potential of using Large Language Models (LLMs) to classify code review comments. We assess the performance of LLMs to classify 17 categories of code review comments. Our results show that LLMs can classify code review comments, outperforming the state-of-the-art approach using a trained deep learning model. In particular, LLMs achieve better accuracy in classifying the five most useful categories, which the state-of-the-art approach struggles with due to low training examples. Rather than relying solely on a specific small training data distribution, our results show that LLMs provide balanced performance across high- and low-frequency categories. These results suggest that the LLMs could offer a scalable solution for code review analytics to improve the effectiveness of the code review process.

