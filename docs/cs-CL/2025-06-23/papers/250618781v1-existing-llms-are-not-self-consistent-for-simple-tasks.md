---
layout: default
title: Existing LLMs Are Not Self-Consistent For Simple Tasks
---

# Existing LLMs Are Not Self-Consistent For Simple Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18781" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18781v1</a>
  <a href="https://arxiv.org/pdf/2506.18781.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18781v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18781v1', 'Existing LLMs Are Not Self-Consistent For Simple Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenru Lin, Jiawen Tao, Yang Yuan, Andrew Chi-Chih Yao

**分类**: cs.CL

**发布日期**: 2025-06-23

**备注**: 10 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/scorpio-nova/llm-self-consistency)

---

## 💡 一句话要点

**提出不一致性度量与自动化方法以解决LLM自洽性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自洽性` `不一致性度量` `自动化方法` `图结构` `能量优化`

## 📋 核心要点

1. 现有大型语言模型在简单任务上表现出高度的不一致性，影响其决策的透明性和可信度。
2. 论文提出了不一致性度量，并开发了基于图和基于能量的两种自动化方法来缓解这一问题。
3. 实验结果显示，尽管提出的方法在一定程度上改善了模型的一致性，但仍需进一步研究以提高自洽性。

## 📝 摘要（中文）

大型语言模型（LLMs）日益强大，但确保其决策透明和可信需要自洽性，即内部推理无矛盾。我们的研究表明，即使在简单任务上，如比较线段或平面上的点，或推理家谱，所有较小模型都高度不一致，甚至最先进的模型如DeepSeek-R1和GPT-o4-mini也未完全自洽。为量化和缓解这些不一致性，我们引入了不一致性度量，并提出了两种自动化方法——基于图的和基于能量的方法。尽管这些修复提供了部分改进，但也突显了在构建更可靠和可解释的AI时自洽性的重要性和复杂性。代码和数据可在https://github.com/scorpio-nova/llm-self-consistency获取。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在简单任务中表现出的自洽性不足问题。现有方法未能有效处理模型内部推理的矛盾，导致决策不透明。

**核心思路**：论文的核心思路是通过引入不一致性度量来量化模型的不一致性，并提出两种自动化修复方法，以提高模型的自洽性和可靠性。

**技术框架**：整体架构包括不一致性度量的计算模块和两种修复方法的实现。基于图的方法利用图结构来表示模型推理过程，而基于能量的方法则通过优化能量函数来减少不一致性。

**关键创新**：最重要的技术创新点在于提出了量化不一致性的度量标准，并开发了两种不同的自动化修复方法，这在现有文献中尚属首次。

**关键设计**：在设计中，关键参数包括不一致性度量的计算方式、图结构的构建方法以及能量函数的定义。这些设计确保了方法的有效性和可操作性。

## 📊 实验亮点

实验结果表明，尽管提出的修复方法在一定程度上改善了模型的一致性，但仍未达到完全自洽的水平。具体性能数据和对比基线尚未详细披露，未来研究需进一步探索更有效的解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过提高大型语言模型的自洽性，可以增强其在实际应用中的可靠性和用户信任度，推动AI技术的进一步发展与应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have grown increasingly powerful, yet ensuring their decisions remain transparent and trustworthy requires self-consistency -- no contradictions in their internal reasoning. Our study reveals that even on simple tasks, such as comparing points on a line or a plane, or reasoning in a family tree, all smaller models are highly inconsistent, and even state-of-the-art models like DeepSeek-R1 and GPT-o4-mini are not fully self-consistent. To quantify and mitigate these inconsistencies, we introduce inconsistency metrics and propose two automated methods -- a graph-based and an energy-based approach. While these fixes provide partial improvements, they also highlight the complexity and importance of self-consistency in building more reliable and interpretable AI. The code and data are available at https://github.com/scorpio-nova/llm-self-consistency.

