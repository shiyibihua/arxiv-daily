---
layout: default
title: How Quantization Shapes Bias in Large Language Models
---

# How Quantization Shapes Bias in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18088" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18088v1</a>
  <a href="https://arxiv.org/pdf/2508.18088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18088v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18088v1', 'How Quantization Shapes Bias in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Federico Marcuzzi, Xuefei Ning, Roy Schwartz, Iryna Gurevych

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**评估量化对大语言模型偏见的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `模型偏见` `大语言模型` `自然语言处理` `伦理考量`

## 📋 核心要点

1. 现有方法在量化过程中未能充分考虑对模型偏见的影响，尤其是对不同人口子群体的影响。
2. 本研究提出了一种综合评估量化对模型偏见影响的方法，重点分析权重和激活量化策略。
3. 实验结果表明，量化可以降低模型毒性，但在生成任务中可能增加刻板印象和不公平性，尤其是在激进压缩下。

## 📝 摘要（中文）

本研究全面评估了量化如何影响模型偏见，特别关注其对个体人口子群体的影响。我们聚焦于权重和激活量化策略，考察其在多种偏见类型（包括刻板印象、毒性、情感和公平性）上的效果。通过在九个基准上使用概率和生成文本指标，我们评估了不同架构和推理能力的模型。研究发现，量化对偏见的影响复杂：虽然它可以减少模型的毒性且对情感影响不大，但在生成任务中，尤其是在激进压缩下，往往会略微增加刻板印象和不公平性。这些趋势在不同人口类别和模型类型中普遍一致，尽管其幅度依赖于具体设置。总体而言，结果强调了在实际应用中平衡效率与伦理考量的重要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决量化对大语言模型偏见影响的评估问题。现有方法往往忽视了量化对不同人口子群体的潜在影响，导致模型在实际应用中可能产生不公平结果。

**核心思路**：论文的核心思路是通过系统评估量化策略对模型偏见的影响，特别是权重和激活量化，分析其在不同偏见类型上的表现，以便为模型优化提供指导。

**技术框架**：研究采用了多种评估指标，包括概率和生成文本指标，涵盖九个基准测试。模型的架构和推理能力也被纳入考量，以全面评估量化的效果。

**关键创新**：本研究的创新点在于系统性地分析了量化对模型偏见的复杂影响，揭示了量化在降低毒性与增加刻板印象之间的权衡，填补了现有文献的空白。

**关键设计**：在实验中，采用了不同的量化策略，并对模型的架构和推理能力进行了分类。通过对比不同设置下的模型表现，研究揭示了量化对偏见的影响幅度和方向。

## 📊 实验亮点

实验结果显示，量化能够显著降低模型的毒性，但在生成任务中，尤其是在激进压缩下，刻板印象和不公平性略有上升。不同模型架构和推理能力的比较表明，这些趋势在各人口类别中普遍存在，强调了量化策略选择的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、社交媒体内容审核和人工智能伦理等。通过理解量化对模型偏见的影响，研究可以帮助开发更公平和高效的语言模型，促进技术在社会中的负责任使用。未来，随着量化技术的广泛应用，该研究的发现将对模型设计和评估标准产生深远影响。

## 📄 摘要（原文）

> This work presents a comprehensive evaluation of how quantization affects model bias, with particular attention to its impact on individual demographic subgroups. We focus on weight and activation quantization strategies and examine their effects across a broad range of bias types, including stereotypes, toxicity, sentiment, and fairness. We employ both probabilistic and generated text-based metrics across nine benchmarks and evaluate models varying in architecture family and reasoning ability. Our findings show that quantization has a nuanced impact on bias: while it can reduce model toxicity and does not significantly impact sentiment, it tends to slightly increase stereotypes and unfairness in generative tasks, especially under aggressive compression. These trends are generally consistent across demographic categories and model types, although their magnitude depends on the specific setting. Overall, our results highlight the importance of carefully balancing efficiency and ethical considerations when applying quantization in practice.

