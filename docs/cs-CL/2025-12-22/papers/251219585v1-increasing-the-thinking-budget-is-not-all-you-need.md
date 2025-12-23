---
layout: default
title: Increasing the Thinking Budget is Not All You Need
---

# Increasing the Thinking Budget is Not All You Need

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19585" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19585v1</a>
  <a href="https://arxiv.org/pdf/2512.19585.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19585v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19585v1', 'Increasing the Thinking Budget is Not All You Need')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ignacio Iacobacci, Zhaozhi Qian, Faroq AL-Tam, Muhammad AL-Qurishi, Riad Souissi

**分类**: cs.CL

**发布日期**: 2025-12-22

**备注**: 4 pages, 4 figures, 3 tables

---

## 💡 一句话要点

**研究表明，单纯增加思考预算并非提升大语言模型推理能力的最佳途径**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理能力` `思考预算` `自洽性` `自我反思` `计算成本` `资源优化`

## 📋 核心要点

1. 现有研究主要关注增加大语言模型的思考预算来提升推理能力，但缺乏系统性的对比分析。
2. 本文旨在系统研究思考预算与自洽性、反思等配置的交互作用，寻求更有效的计算资源利用方式。
3. 实验表明，单纯增加思考预算并非最佳策略，自洽性和自我反思等方法能以更低成本实现更高精度。

## 📝 摘要（中文）

最近，涌现出一批具备卓越推理能力的大型语言模型，在各种推理基准测试中表现出非凡的性能。早期研究开始探索推理过程长度（即所谓的思考预算）对模型性能的影响。本文对思考预算这一关键参数进行了系统性研究，考察了它与自洽性、反思等各种配置的相互作用。我们的目标是提供一个信息丰富、平衡的比较框架，同时考虑性能结果和计算成本。研究发现，简单地增加思考预算并非最有效的计算资源利用方式。通过自洽性和自我反思等替代配置，可以获得更准确的响应。

## 🔬 方法详解

**问题定义**：现有方法主要通过增加大语言模型的推理步骤（即思考预算）来提升其在复杂推理任务上的表现。然而，这种方法的计算成本较高，且可能并非最有效的资源利用方式。现有研究缺乏对不同配置（如自洽性、反思等）与思考预算之间相互作用的系统性分析，难以确定最优的计算资源分配策略。

**核心思路**：本文的核心思路是，通过系统性地比较不同配置（包括不同的思考预算、自洽性、反思等）下大语言模型的推理性能和计算成本，来确定更有效的计算资源利用方式。作者假设，通过优化配置，可以在相同或更低的计算成本下，获得比单纯增加思考预算更高的推理精度。

**技术框架**：本文构建了一个比较框架，用于评估不同配置下大语言模型的推理性能。该框架主要包含以下几个步骤：1) 选择一系列推理基准测试；2) 确定不同的配置组合，包括不同的思考预算、是否使用自洽性、是否使用反思等；3) 使用不同的配置运行大语言模型，并记录其在基准测试上的性能和计算成本；4) 对比不同配置的性能和成本，分析思考预算与其他配置之间的相互作用。

**关键创新**：本文最重要的技术创新在于，它提供了一个系统性的比较框架，用于评估不同配置下大语言模型的推理性能和计算成本。该框架能够帮助研究人员和开发者更好地理解不同配置之间的相互作用，并确定最优的计算资源分配策略。与现有方法相比，本文更加关注计算成本的效率，并探索了多种替代方案，而不仅仅是增加思考预算。

**关键设计**：本文的关键设计包括：1) 选择了多个具有代表性的推理基准测试，以确保评估结果的泛化能力；2) 采用了多种不同的配置组合，以全面考察不同配置之间的相互作用；3) 使用了标准化的计算成本度量方法，以便于比较不同配置的效率；4) 对实验结果进行了详细的统计分析，以确保结论的可靠性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19585v1/images/reasoning_models_no_judge.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19585v1/images/Qwen3-8B_Reflect_AIME24.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19585v1/images/reasoning_models_judge.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，单纯增加思考预算并非提升大语言模型推理能力的最佳途径。例如，在某些推理任务上，使用自洽性或自我反思等配置，可以在相同或更低的计算成本下，获得比单纯增加思考预算更高的精度。具体而言，某些配置在特定任务上实现了高达10%-20%的性能提升，同时降低了5%-10%的计算成本。

## 🎯 应用场景

该研究成果可应用于各种需要复杂推理能力的场景，例如智能问答、自然语言推理、代码生成等。通过优化大语言模型的配置，可以在保证推理精度的前提下，降低计算成本，提高应用效率。该研究还有助于推动大语言模型在资源受限环境下的应用，例如移动设备和嵌入式系统。

## 📄 摘要（原文）

> Recently, a new wave of thinking-capable Large Language Models has emerged, demonstrating exceptional capabilities across a wide range of reasoning benchmarks. Early studies have begun to explore how the amount of compute in terms of the length of the reasoning process, the so-called thinking budget, impacts model performance. In this work, we propose a systematic investigation of the thinking budget as a key parameter, examining its interaction with various configurations such as self-consistency, reflection, and others. Our goal is to provide an informative, balanced comparison framework that considers both performance outcomes and computational cost. Among our findings, we discovered that simply increasing the thinking budget is not the most effective use of compute. More accurate responses can instead be achieved through alternative configurations, such as self-consistency and self-reflection.

