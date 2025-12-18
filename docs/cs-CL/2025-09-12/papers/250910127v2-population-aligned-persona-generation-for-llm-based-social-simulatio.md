---
layout: default
title: Population-Aligned Persona Generation for LLM-based Social Simulation
---

# Population-Aligned Persona Generation for LLM-based Social Simulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10127" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10127v2</a>
  <a href="https://arxiv.org/pdf/2509.10127.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10127v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10127v2', 'Population-Aligned Persona Generation for LLM-based Social Simulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Max Xiong, Yuxuan Lei, Tianfu Wang, Kaize Ding, Ziang Xiao, Nicholas Jing Yuan, Xing Xie

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-12 (更新: 2025-10-04)

---

## 💡 一句话要点

**提出人口对齐的Persona生成框架，提升LLM社会模拟的真实性和准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM` `社会模拟` `Persona生成` `人口对齐` `重要性抽样`

## 📋 核心要点

1. 现有基于LLM的社会模拟研究主要关注Agent框架和模拟环境，忽略了Persona生成和非代表性Persona集合引入的潜在偏差。
2. 论文提出一种人口对齐的Persona生成框架，通过LLM生成、质量评估、重要性抽样对齐和任务特定调整等步骤，构建高质量Persona集合。
3. 实验结果表明，该方法能有效减少人口层面的偏差，实现更准确、灵活的社会模拟，适用于广泛的研究和政策应用。

## 📝 摘要（中文）

本文提出了一种系统性的框架，用于为基于大型语言模型（LLM）的社会模拟合成高质量、人口对齐的Persona集合。该方法首先利用LLM从长期社交媒体数据中生成叙事性Persona，然后进行严格的质量评估以过滤掉低质量的个人资料。接着，应用重要性抽样来实现与参考心理测量分布（如大五人格特质）的全局对齐。为了满足特定模拟环境的需求，进一步引入了一个任务特定的模块，将全局对齐的Persona集合调整到目标子群体。大量实验表明，该方法显著降低了人口层面的偏差，并为广泛的研究和政策应用实现了准确、灵活的社会模拟。

## 🔬 方法详解

**问题定义**：现有基于LLM的社会模拟研究在Persona生成方面存在不足，生成的Persona集合可能无法真实反映现实世界人口的多样性和分布，导致模拟结果产生偏差。现有方法往往忽略了Persona的质量评估和与真实人口统计数据的对齐，使得模拟结果的可靠性受到质疑。

**核心思路**：论文的核心思路是通过一个系统性的框架，生成高质量且与真实人口分布对齐的Persona集合。该框架利用LLM生成Persona，并通过质量评估、重要性抽样和任务特定调整等步骤，确保Persona的真实性、多样性和代表性。通过这种方式，可以减少模拟结果中的偏差，提高社会模拟的准确性和可靠性。

**技术框架**：该框架包含以下几个主要模块：1) **LLM Persona生成**：利用LLM从社交媒体数据中生成叙事性Persona。2) **质量评估**：对生成的Persona进行质量评估，过滤掉低质量的个人资料。3) **全局对齐**：应用重要性抽样，使Persona集合与参考心理测量分布（如大五人格特质）全局对齐。4) **任务特定调整**：根据特定模拟环境的需求，将全局对齐的Persona集合调整到目标子群体。

**关键创新**：该方法最重要的技术创新点在于将LLM的生成能力与统计学方法相结合，实现人口对齐的Persona生成。与现有方法相比，该方法不仅关注Persona的生成，还关注Persona的质量和与真实人口分布的对齐，从而显著降低了模拟结果中的偏差。此外，任务特定调整模块使得该方法能够灵活适应不同的模拟环境。

**关键设计**：在质量评估阶段，使用了多种指标来评估Persona的真实性和一致性。在重要性抽样阶段，使用了大五人格特质等心理测量分布作为参考，通过调整Persona的权重，使其与真实人口分布对齐。在任务特定调整阶段，使用了条件生成模型，根据特定任务的需求，对Persona的属性进行调整。

## 📊 实验亮点

实验结果表明，该方法能够显著降低人口层面的偏差，提高社会模拟的准确性。与现有方法相比，该方法在Persona的真实性、多样性和代表性方面均有显著提升。例如，在模拟特定政策对不同人群的影响时，该方法能够更准确地预测不同人群的反应，从而为政策制定者提供更可靠的依据。

## 🎯 应用场景

该研究成果可广泛应用于计算社会科学、政策模拟、市场营销等领域。例如，可以用于模拟不同政策对社会群体的影响，预测市场趋势，或评估产品对不同人群的吸引力。通过构建更真实、更具代表性的社会模拟环境，可以为决策者提供更可靠的依据，从而制定更有效的政策和策略。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled human-like social simulations at unprecedented scale and fidelity, offering new opportunities for computational social science. A key challenge, however, is the construction of persona sets that authentically represent the diversity and distribution of real-world populations. Most existing LLM-based social simulation studies focus primarily on designing agentic frameworks and simulation environments, often overlooking the complexities of persona generation and the potential biases introduced by unrepresentative persona sets. In this paper, we propose a systematic framework for synthesizing high-quality, population-aligned persona sets for LLM-driven social simulation. Our approach begins by leveraging LLMs to generate narrative personas from long-term social media data, followed by rigorous quality assessment to filter out low-fidelity profiles. We then apply importance sampling to achieve global alignment with reference psychometric distributions, such as the Big Five personality traits. To address the needs of specific simulation contexts, we further introduce a task-specific module that adapts the globally aligned persona set to targeted subpopulations. Extensive experiments demonstrate that our method significantly reduces population-level bias and enables accurate, flexible social simulation for a wide range of research and policy applications.

