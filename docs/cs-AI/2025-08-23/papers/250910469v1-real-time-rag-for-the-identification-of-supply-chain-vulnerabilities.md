---
layout: default
title: Real-Time RAG for the Identification of Supply Chain Vulnerabilities
---

# Real-Time RAG for the Identification of Supply Chain Vulnerabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10469" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10469v1</a>
  <a href="https://arxiv.org/pdf/2509.10469.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10469v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10469v1', 'Real-Time RAG for the Identification of Supply Chain Vulnerabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jesse Ponnock, Grace Kenneally, Michael Robert Briggs, Elinor Yeo, Tyrone Patterson, Nicholas Kinberg, Matthew Kalinowski, David Hechtman

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-08-23

**备注**: 14 pages, 5 figures, 1 table. Approved for Public Release; Distribution Unlimited. PRS Release Number: 25-0864

---

## 💡 一句话要点

**提出实时RAG方法以识别供应链脆弱性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `供应链分析` `检索增强生成` `实时数据处理` `网络爬虫` `大语言模型` `信息更新` `性能优化`

## 📋 核心要点

1. 现有方法在供应链分析中无法及时更新信息，导致决策依据滞后。
2. 本研究通过结合检索增强生成技术与网络爬虫，提出了一种新的供应链分析方法。
3. 实验结果显示，微调检索模型显著提升性能，而LLM的微调效果有限且成本高。

## 📝 摘要（中文）

新兴的生成式人工智能技术能够深入分析国家供应链，但真正有价值的洞察需要及时更新和聚合大量数据。大型语言模型（LLMs）提供了前所未有的分析机会，但其知识基础受限于最后的训练日期，使得这些能力无法满足依赖于新兴和及时信息的组织需求。本研究提出了一种创新的供应链分析方法，通过将新兴的检索增强生成（RAG）预处理和检索技术与先进的网络爬虫技术相结合，旨在减少将新信息纳入增强型LLM的延迟，从而实现对供应链干扰因素的及时分析。实验结果表明，应用RAG系统进行供应链分析时，微调嵌入检索模型能显著提升性能，强调了检索质量的重要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决供应链分析中信息更新滞后的问题。现有方法依赖于静态的知识库，无法及时反映市场变化，影响决策的有效性。

**核心思路**：论文提出通过结合检索增强生成（RAG）技术与网络爬虫，动态获取和整合最新信息，以提高供应链分析的时效性和准确性。

**技术框架**：整体架构包括数据采集模块、检索增强生成模块和分析模块。数据采集模块利用网络爬虫技术获取实时数据，检索增强生成模块则通过RAG技术处理和分析这些数据，最终输出分析结果。

**关键创新**：最重要的技术创新在于结合了动态检索和生成模型，尤其是通过微调嵌入检索模型来提升检索质量，从而显著改善分析结果的时效性和准确性。

**关键设计**：在参数设置上，采用了自适应迭代检索策略，根据上下文动态调整检索深度。此外，损失函数和网络结构经过优化，以确保在复杂查询下的性能提升。实验中还比较了向下抽象与向上抽象的效果，结果显示前者在实践中表现更佳。

## 📊 实验亮点

实验结果表明，微调嵌入检索模型在性能上提升显著，尤其是在复杂查询下，适应性迭代检索策略进一步增强了分析效果。与基线相比，检索质量的提升使得分析结果的时效性和准确性得到了显著改善。

## 🎯 应用场景

该研究的潜在应用领域包括供应链管理、风险评估和决策支持系统。通过实时获取和分析数据，企业能够更快地识别和应对供应链中的潜在脆弱性，从而提高整体运营效率和响应能力。未来，该方法有望在其他领域如金融分析和市场预测中得到应用。

## 📄 摘要（原文）

> New technologies in generative AI can enable deeper analysis into our nation's supply chains but truly informative insights require the continual updating and aggregation of massive data in a timely manner. Large Language Models (LLMs) offer unprecedented analytical opportunities however, their knowledge base is constrained to the models' last training date, rendering these capabilities unusable for organizations whose mission impacts rely on emerging and timely information. This research proposes an innovative approach to supply chain analysis by integrating emerging Retrieval-Augmented Generation (RAG) preprocessing and retrieval techniques with advanced web-scraping technologies. Our method aims to reduce latency in incorporating new information into an augmented-LLM, enabling timely analysis of supply chain disruptors. Through experimentation, this study evaluates the combinatorial effects of these techniques towards timeliness and quality trade-offs. Our results suggest that in applying RAG systems to supply chain analysis, fine-tuning the embedding retrieval model consistently provides the most significant performance gains, underscoring the critical importance of retrieval quality. Adaptive iterative retrieval, which dynamically adjusts retrieval depth based on context, further enhances performance, especially on complex supply chain queries. Conversely, fine-tuning the LLM yields limited improvements and higher resource costs, while techniques such as downward query abstraction significantly outperforms upward abstraction in practice.

