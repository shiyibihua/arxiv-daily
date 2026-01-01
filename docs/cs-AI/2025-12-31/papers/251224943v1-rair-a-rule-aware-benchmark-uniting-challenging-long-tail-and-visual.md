---
layout: default
title: "RAIR: A Rule-Aware Benchmark Uniting Challenging Long-Tail and Visual Salience Subset for E-commerce Relevance Assessment"
---

# RAIR: A Rule-Aware Benchmark Uniting Challenging Long-Tail and Visual Salience Subset for E-commerce Relevance Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24943" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24943v1</a>
  <a href="https://arxiv.org/pdf/2512.24943.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24943v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24943v1', 'RAIR: A Rule-Aware Benchmark Uniting Challenging Long-Tail and Visual Salience Subset for E-commerce Relevance Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenji Lu, Zhuo Chen, Hui Zhao, Zhenyi Wang, Pengjie Wang, Jian Xu, Bo Zheng

**分类**: cs.IR, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-12-31

---

## 💡 一句话要点

**提出RAIR：一个面向电商相关性评估的规则感知、长尾和视觉显著性基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电商搜索` `相关性评估` `长尾数据` `视觉显著性` `多模态理解` `大型语言模型` `评估基准`

## 📋 核心要点

1. 现有电商搜索相关性评估基准缺乏足够的复杂性，难以全面评估模型，行业内缺少标准化的评估指标。
2. RAIR通过构建包含通用、长尾和视觉显著性三个子集的数据集，并制定通用规则，建立标准化的评估框架。
3. 实验结果表明，即使是GPT-5在RAIR上也面临挑战，证明了RAIR的难度和有效性，为LLM和VLM评估提供新视角。

## 📝 摘要（中文）

本文提出了一个名为RAIR（Rule-Aware benchmark with Image for Relevance assessment）的中文数据集，用于电商搜索相关性评估。现有基准在模型评估的复杂性方面存在不足，导致行业内缺乏标准化的相关性评估指标。RAIR源于真实场景，建立了一个标准化的相关性评估框架，并提供了一套通用的规则，为标准化评估奠定了基础。RAIR分析了当前相关性模型所需的基本能力，并引入了一个包含三个子集的数据集：一个具有行业平衡抽样的通用子集，用于评估基本模型能力；一个侧重于挑战性案例的长尾硬子集，用于评估性能极限；一个用于评估多模态理解能力的视觉显著性子集。使用14个开源和闭源模型在RAIR上进行了实验，结果表明即使是性能最佳的GPT-5，RAIR也提出了足够的挑战。RAIR数据现已开放，可作为相关性评估的行业基准，并为通用LLM和视觉语言模型（VLM）评估提供新的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决电商搜索相关性评估中，现有基准数据集复杂度不足，无法充分评估大型语言模型（LLM）和视觉语言模型（VLM）的问题。现有方法无法有效评估模型在长尾数据和多模态理解方面的能力，导致行业内缺乏统一且具有挑战性的评估标准。

**核心思路**：论文的核心思路是构建一个更具挑战性和代表性的数据集RAIR，该数据集包含通用子集、长尾硬子集和视觉显著性子集，并制定一套通用的评估规则。通过这种方式，RAIR能够更全面地评估模型在不同场景下的相关性判断能力，并为行业提供一个标准化的评估基准。

**技术框架**：RAIR的构建主要包含以下几个阶段：1) 数据收集：从真实电商场景中收集数据，保证数据的真实性和多样性。2) 子集划分：将数据划分为通用子集、长尾硬子集和视觉显著性子集，分别评估模型在不同方面的能力。3) 规则制定：制定一套通用的评估规则，用于指导相关性判断，保证评估的公平性和一致性。4) 模型评估：使用多个开源和闭源模型在RAIR上进行评估，验证RAIR的有效性和挑战性。

**关键创新**：RAIR的关键创新在于其数据集的构建方式和评估规则的制定。RAIR不仅考虑了数据的通用性，还特别关注了长尾数据和视觉信息，这使得RAIR能够更全面地评估模型的相关性判断能力。此外，RAIR制定的通用评估规则也为行业提供了一个标准化的评估框架。

**关键设计**：RAIR的关键设计包括：1) 长尾硬子集的构建：通过选择具有挑战性的长尾查询和商品，评估模型在罕见情况下的表现。2) 视觉显著性子集的构建：通过引入商品图片，评估模型的多模态理解能力。3) 通用评估规则的制定：制定清晰明确的规则，指导相关性判断，减少主观性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24943v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24943v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24943v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，即使是性能领先的GPT-5模型在RAIR上也面临挑战，这证明了RAIR数据集的难度和有效性。不同模型在RAIR的不同子集上表现差异明显，表明RAIR能够有效区分模型在通用性、长尾处理和多模态理解方面的能力。RAIR的发布为电商相关性评估提供了一个新的行业基准。

## 🎯 应用场景

RAIR可应用于电商搜索、推荐系统、广告排序等领域，帮助提升用户搜索体验和商品点击率。通过更准确地评估模型的相关性判断能力，RAIR可以指导模型优化，提升电商平台的整体效率和用户满意度。未来，RAIR可以扩展到其他领域，如新闻推荐、知识问答等，为更广泛的应用场景提供支持。

## 📄 摘要（原文）

> Search relevance plays a central role in web e-commerce. While large language models (LLMs) have shown significant results on relevance task, existing benchmarks lack sufficient complexity for comprehensive model assessment, resulting in an absence of standardized relevance evaluation metrics across the industry. To address this limitation, we propose Rule-Aware benchmark with Image for Relevance assessment(RAIR), a Chinese dataset derived from real-world scenarios. RAIR established a standardized framework for relevance assessment and provides a set of universal rules, which forms the foundation for standardized evaluation. Additionally, RAIR analyzes essential capabilities required for current relevance models and introduces a comprehensive dataset consists of three subset: (1) a general subset with industry-balanced sampling to evaluate fundamental model competencies; (2) a long-tail hard subset focus on challenging cases to assess performance limits; (3) a visual salience subset for evaluating multimodal understanding capabilities. We conducted experiments on RAIR using 14 open and closed-source models. The results demonstrate that RAIR presents sufficient challenges even for GPT-5, which achieved the best performance. RAIR data are now available, serving as an industry benchmark for relevance assessment while providing new insights into general LLM and Visual Language Model(VLM) evaluation.

