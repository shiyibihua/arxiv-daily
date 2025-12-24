---
layout: default
title: Cross-Domain Web Information Extraction at Pinterest
---

# Cross-Domain Web Information Extraction at Pinterest

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01096" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01096v1</a>
  <a href="https://arxiv.org/pdf/2508.01096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01096v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01096v1', 'Cross-Domain Web Information Extraction at Pinterest')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael Farag, Patrick Halina, Andrey Zaytsev, Alekhya Munagala, Imtihan Ahmed, Junhao Wang

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-08-01

**DOI**: [10.1145/3711896.3737207](https://doi.org/10.1145/3711896.3737207)

---

## 💡 一句话要点

**提出一种高效的跨域网页信息提取系统以解决电商数据结构化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网页信息提取` `电商数据结构化` `多模态学习` `极端梯度提升` `成本效益优化` `用户体验提升`

## 📋 核心要点

1. 现有方法在从电商网站提取结构化数据时面临准确性和成本的双重挑战。
2. 论文提出了一种新颖的网页表示方法，将结构、视觉和文本信息整合，优化了小模型的学习能力。
3. 实验结果显示，该系统每秒处理超过1000个URL，且在成本效益上显著优于大型语言模型。

## 📝 摘要（中文）

互联网提供了大量非结构化信息，但将其转化为结构化格式是一项重大挑战。在Pinterest，准确提取电商网站的结构化产品数据对于提升用户体验和内容分发至关重要。本文介绍了Pinterest的属性提取系统，该系统在可控成本下实现了显著的准确性和可扩展性。我们的方法利用了一种新颖的网页表示形式，将结构、视觉和文本模态结合成紧凑的形式，优化了小模型学习。该表示捕捉了每个可见HTML节点的文本、样式和布局信息。我们展示了这种方法使得简单模型（如极端梯度提升XGBoost）在属性提取上比复杂的大型语言模型（如GPT）更为准确。我们的结果表明，该系统具有高度可扩展性，每秒处理超过1000个URL，同时成本比最便宜的GPT替代方案低1000倍。

## 🔬 方法详解

**问题定义**：本文旨在解决从电商网站提取结构化产品数据的准确性和成本问题。现有方法通常依赖复杂的模型，导致成本高且处理速度慢。

**核心思路**：论文提出了一种新颖的网页表示形式，结合了结构、视觉和文本信息，旨在提高小模型的学习效率和准确性。通过这种方式，简单模型能够在属性提取上超越复杂模型的表现。

**技术框架**：系统的整体架构包括数据采集、网页表示生成、特征提取和属性预测四个主要模块。首先从电商网站抓取数据，然后生成网页的多模态表示，接着提取特征，最后通过模型进行属性预测。

**关键创新**：最重要的创新在于提出了一种紧凑的网页表示形式，能够有效整合多种信息模态，使得简单模型（如XGBoost）在性能上超越复杂的语言模型。这一方法显著降低了成本并提高了处理速度。

**关键设计**：在模型设计中，采用了XGBoost作为基础模型，并通过优化特征选择和损失函数来提升性能。此外，网页节点的文本、样式和布局信息的整合是关键设计之一，确保了模型能够准确捕捉到重要的属性信息。

## 📊 实验亮点

实验结果表明，该系统每秒能够处理超过1000个URL，且在成本效益上比最便宜的GPT替代方案低1000倍。此外，简单模型XGBoost在属性提取的准确性上超越了复杂的GPT模型，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括电商平台、内容推荐系统和信息检索等。通过高效提取结构化数据，能够显著提升用户体验，优化内容分发策略，并为后续的数据分析和决策提供支持。未来，该技术可能在更多行业中得到应用，推动信息处理的智能化进程。

## 📄 摘要（原文）

> The internet offers a massive repository of unstructured information, but it's a significant challenge to convert this into a structured format. At Pinterest, the ability to accurately extract structured product data from e-commerce websites is essential to enhance user experiences and improve content distribution. In this paper, we present Pinterest's system for attribute extraction, which achieves remarkable accuracy and scalability at a manageable cost. Our approach leverages a novel webpage representation that combines structural, visual, and text modalities into a compact form, optimizing it for small model learning. This representation captures each visible HTML node with its text, style and layout information. We show how this allows simple models such as eXtreme Gradient Boosting (XGBoost) to extract attributes more accurately than much more complex Large Language Models (LLMs) such as Generative Pre-trained Transformer (GPT). Our results demonstrate a system that is highly scalable, processing over 1,000 URLs per second, while being 1000 times more cost-effective than the cheapest GPT alternatives.

