---
layout: default
title: Improving LLMs for Machine Translation Using Synthetic Preference Data
---

# Improving LLMs for Machine Translation Using Synthetic Preference Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14951" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14951v1</a>
  <a href="https://arxiv.org/pdf/2508.14951.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14951v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14951v1', 'Improving LLMs for Machine Translation Using Synthetic Preference Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dario Vajda, Domen Vreš, Marko Robnik-Šikonja

**分类**: cs.CL

**发布日期**: 2025-08-20

**备注**: Paper with individual presentation at LUHME workshop at ECAI 2025

---

## 💡 一句话要点

**通过合成偏好数据提升大型语言模型的机器翻译能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器翻译` `直接偏好优化` `合成数据` `自动评估指标`

## 📋 核心要点

1. 现有的大型语言模型在机器翻译中表现良好，但仍存在翻译质量不稳定和错误频发的问题。
2. 本文提出通过直接偏好优化（DPO）训练，利用合成的质量排名数据来提升机器翻译模型的性能。
3. 实验结果表明，微调后的模型在翻译维基百科文章时，COMET得分显著提升，并且减少了语言和格式错误。

## 📝 摘要（中文）

大型语言模型已成为有效的机器翻译系统。本文探讨如何利用相对较少且易于生成的数据资源，改善通用指令调优的大型语言模型在机器翻译中的表现。以斯洛文尼亚语为案例，采用直接偏好优化（DPO）训练对GaMS-9B-Instruct模型进行改进，使用程序化策划和增强的公共数据集子集。DPO需要质量排名实例对，我们通过翻译英文维基百科文章生成训练数据集，并基于启发式方法和自动评估指标（如COMET）对翻译结果进行排名。评估显示，经过微调的模型在翻译维基百科文章时，超越了参与数据集生成的两个模型，COMET得分分别提升约0.04和0.02，并且更一致地避免了语言和格式错误。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在机器翻译中存在的翻译质量不稳定和错误频发的问题。现有方法在生成高质量翻译时，往往依赖于大量人工标注数据，成本高且效率低。

**核心思路**：论文提出利用直接偏好优化（DPO）方法，通过生成合成的质量排名数据来提升模型性能。通过程序化生成数据，降低了对人工标注的依赖，从而提高了数据生成的效率。

**技术框架**：整体流程包括数据生成、质量排名和模型微调三个主要阶段。首先，使用两个大型语言模型（GaMS-9B-Instruct和EuroLLM-9B-Instruct）翻译英文维基百科文章，然后基于启发式方法和自动评估指标对翻译结果进行排名，最后利用DPO对GaMS-9B-Instruct模型进行微调。

**关键创新**：最重要的技术创新在于通过程序化生成的合成偏好数据来进行模型训练，显著减少了对人工标注数据的依赖。这种方法与传统的依赖大量人工标注的训练方式形成鲜明对比。

**关键设计**：在DPO训练中，采用了特定的损失函数来优化模型的翻译质量，并通过COMET等自动评估指标来评估翻译结果的质量。模型的微调过程注重避免语言和格式错误，确保生成的翻译更加自然流畅。

## 📊 实验亮点

实验结果显示，经过微调的模型在翻译维基百科文章时，COMET得分分别提升约0.04和0.02，超越了参与数据集生成的两个基线模型。此外，微调后的模型在语言和格式错误方面表现更为一致，显示出更高的翻译质量。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译系统、跨文化交流平台以及国际化软件开发等。通过提升机器翻译的质量和一致性，可以大幅提高用户体验，促进不同语言用户之间的沟通与理解。未来，该方法有望在更多语言对的翻译任务中得到应用，推动机器翻译技术的进一步发展。

## 📄 摘要（原文）

> Large language models have emerged as effective machine translation systems. In this paper, we explore how a general instruction-tuned large language model can be improved for machine translation using relatively few easily produced data resources. Using Slovene as a use case, we improve the GaMS-9B-Instruct model using Direct Preference Optimization (DPO) training on a programmatically curated and enhanced subset of a public dataset. As DPO requires pairs of quality-ranked instances, we generated its training dataset by translating English Wikipedia articles using two LLMs, GaMS-9B-Instruct and EuroLLM-9B-Instruct. We ranked the resulting translations based on heuristics coupled with automatic evaluation metrics such as COMET. The evaluation shows that our fine-tuned model outperforms both models involved in the dataset generation. In comparison to the baseline models, the fine-tuned model achieved a COMET score gain of around 0.04 and 0.02, respectively, on translating Wikipedia articles. It also more consistently avoids language and formatting errors.

