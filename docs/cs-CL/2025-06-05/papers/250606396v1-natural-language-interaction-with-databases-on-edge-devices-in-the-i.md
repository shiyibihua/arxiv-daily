---
layout: default
title: Natural Language Interaction with Databases on Edge Devices in the Internet of Battlefield Things
---

# Natural Language Interaction with Databases on Edge Devices in the Internet of Battlefield Things

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06396" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06396v1</a>
  <a href="https://arxiv.org/pdf/2506.06396.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06396v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06396v1', 'Natural Language Interaction with Databases on Edge Devices in the Internet of Battlefield Things')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christopher D. Molek, Roberto Fronteddu, K. Brent Venable, Niranjan Suri

**分类**: cs.CL, cs.AI, cs.DB

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出自然语言交互框架以解决战场物联网中的数据处理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `大型语言模型` `边缘计算` `战场物联网` `数据库查询` `信息提取` `决策支持`

## 📋 核心要点

1. 现有方法在战场物联网中处理数据时，缺乏有效的自然语言交互能力，导致信息获取效率低下。
2. 本文提出了一种基于大型语言模型的工作流程，能够将自然语言问题映射到数据库查询，并以自然语言返回结果。
3. 实验结果表明，Llama 3.1模型在准确性上较其他模型提升了19.4%，有效解决了现有方法的不足。

## 📝 摘要（中文）

随着物联网在战场上的扩展，战场物联网（IoBT）为增强态势感知提供了新机遇。为了提高IoBT在关键决策中的潜力，必须将这些设备的数据处理成可供消费者使用的信息对象，并按需提供。为此，本文提出了一种利用自然语言处理（NLP）查询数据库并以自然语言返回响应的工作流程。我们的解决方案采用适合边缘设备的大型语言模型（LLMs）进行NLP，并使用适合动态连接网络的图形数据库。通过评估多种中型LLMs，我们发现Llama 3.1在所有指标上表现优于其他模型，并且我们的两步法显著提升了19.4%的准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决战场物联网中数据处理的效率问题，现有方法在自然语言交互方面存在局限，导致信息获取不够灵活和高效。

**核心思路**：通过引入大型语言模型（LLMs），将用户的自然语言查询转换为数据库查询，并将结果以自然语言反馈给用户，从而实现高效的信息交互。

**技术框架**：整体架构包括两个主要模块：第一步是将自然语言问题映射为Cypher数据库查询，第二步是将数据库输出总结为自然语言响应。这一流程适用于边缘设备，确保快速响应。

**关键创新**：与现有方法相比，本文的两步法放宽了对Cypher查询与真实代码的精确匹配要求，从而提高了查询的准确性，达到了19.4%的提升。

**关键设计**：在模型选择上，评估了多种中型LLMs，最终选择Llama 3.1（80亿参数）作为最佳模型，确保其在边缘设备上的高效运行。

## 📊 实验亮点

实验结果显示，Llama 3.1模型在所有评估指标上均优于其他中型LLMs，尤其在准确性上提升了19.4%。这一显著提升表明，本文提出的两步法有效解决了现有方法的局限性，具有重要的应用前景。

## 🎯 应用场景

该研究的潜在应用领域包括军事指挥与控制、战场监测和情报分析等。通过实现自然语言与数据库的交互，决策者能够更快速地获取关键信息，从而提升战场态势感知和决策效率。未来，该框架还可扩展至其他领域，如智能城市和工业物联网，具有广泛的实际价值。

## 📄 摘要（原文）

> The expansion of the Internet of Things (IoT) in the battlefield, Internet of Battlefield Things (IoBT), gives rise to new opportunities for enhancing situational awareness. To increase the potential of IoBT for situational awareness in critical decision making, the data from these devices must be processed into consumer-ready information objects, and made available to consumers on demand. To address this challenge we propose a workflow that makes use of natural language processing (NLP) to query a database technology and return a response in natural language. Our solution utilizes Large Language Models (LLMs) that are sized for edge devices to perform NLP as well as graphical databases which are well suited for dynamic connected networks which are pervasive in the IoBT. Our architecture employs LLMs for both mapping questions in natural language to Cypher database queries as well as to summarize the database output back to the user in natural language. We evaluate several medium sized LLMs for both of these tasks on a database representing publicly available data from the US Army's Multipurpose Sensing Area (MSA) at the Jornada Range in Las Cruces, NM. We observe that Llama 3.1 (8 billion parameters) outperforms the other models across all the considered metrics. Most importantly, we note that, unlike current methods, our two step approach allows the relaxation of the Exact Match (EM) requirement of the produced Cypher queries with ground truth code and, in this way, it achieves a 19.4% increase in accuracy. Our workflow lays the ground work for deploying LLMs on edge devices to enable natural language interactions with databases containing information objects for critical decision making.

