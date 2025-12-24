---
layout: default
title: Comparing energy consumption and accuracy in text classification inference
---

# Comparing energy consumption and accuracy in text classification inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14170" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14170v1</a>
  <a href="https://arxiv.org/pdf/2508.14170.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14170v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14170v1', 'Comparing energy consumption and accuracy in text classification inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Johannes Zschache, Tilman Hartwig

**分类**: cs.CL, cs.CY

**发布日期**: 2025-08-19

**备注**: Key results in Figure 1, submitted to Nature Communications, 25 pages

---

## 💡 一句话要点

**评估文本分类推理中的能耗与准确性权衡**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `能效评估` `文本分类` `大型语言模型` `推理阶段` `可持续AI` `模型架构` `能耗与准确性`

## 📋 核心要点

1. 现有研究主要关注模型训练阶段的能耗，推理阶段的能效问题被忽视，导致可持续性挑战。
2. 本研究通过系统评估不同模型架构和硬件配置下的文本分类推理，提出了能耗与准确性之间的权衡分析。
3. 实验结果显示，最佳准确性模型也可实现能效，且推理能耗与模型运行时间高度相关，提供了实用的能耗估计方法。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在自然语言处理（NLP）任务中的广泛应用，能效和可持续性问题日益受到关注。尽管以往研究主要集中在模型训练阶段的能耗，推理阶段的研究相对较少。本研究系统评估了不同模型架构和硬件配置下文本分类推理的模型准确性与能耗之间的权衡。实证分析表明，准确性最佳的模型也可以实现能效，而较大的LLMs往往消耗更多能量且分类准确性较低。推理能耗的显著变异性受到模型类型、规模和硬件规格的影响。此外，我们发现推理能耗与模型运行时间之间存在强相关性，这表明在无法直接测量的情况下，执行时间可以作为能耗的实用代理。这些发现为可持续AI发展提供了可行的见解，帮助研究人员、行业从业者和政策制定者在NLP应用中平衡性能与资源效率。

## 🔬 方法详解

**问题定义**：本研究旨在解决文本分类推理阶段的能耗与准确性之间的权衡问题。现有方法多集中于训练阶段，忽视了推理阶段的能效评估，导致在实际应用中面临可持续性挑战。

**核心思路**：论文通过系统评估不同模型架构和硬件配置下的推理能耗与准确性，提出了一种新的分析框架，以便在保证模型性能的同时提高能效。

**技术框架**：研究采用实证分析方法，比较了多种模型架构（如小型与大型LLMs）在不同硬件上的推理表现，分析了能耗与准确性之间的关系。

**关键创新**：本研究的创新点在于首次系统性地将推理能耗与模型运行时间关联起来，提出运行时间作为能耗的代理指标，填补了推理阶段能效研究的空白。

**关键设计**：研究中使用了多种模型架构和硬件配置，关注模型类型、规模及其对能耗的影响，采用了标准化的评估流程以确保结果的可比性。实验中还考虑了不同的运行时间测量方法，以验证其与能耗的相关性。

## 📊 实验亮点

实验结果表明，最佳准确性模型在能耗方面也表现出色，推理能耗范围从小于毫瓦到超过千瓦时，显示出显著的变异性。此外，推理能耗与模型运行时间之间的强相关性为能耗估算提供了新的视角，具有实际应用价值。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本分类、情感分析和信息检索等任务。通过优化模型的能耗与准确性平衡，研究为AI系统的可持续发展提供了重要指导，能够帮助企业和研究机构在资源有限的情况下实现高效的模型部署。

## 📄 摘要（原文）

> The increasing deployment of large language models (LLMs) in natural language processing (NLP) tasks raises concerns about energy efficiency and sustainability. While prior research has largely focused on energy consumption during model training, the inference phase has received comparatively less attention. This study systematically evaluates the trade-offs between model accuracy and energy consumption in text classification inference across various model architectures and hardware configurations. Our empirical analysis shows that the best-performing model in terms of accuracy can also be energy-efficient, while larger LLMs tend to consume significantly more energy with lower classification accuracy. We observe substantial variability in inference energy consumption ($<$mWh to $>$kWh), influenced by model type, model size, and hardware specifications. Additionally, we find a strong correlation between inference energy consumption and model runtime, indicating that execution time can serve as a practical proxy for energy usage in settings where direct measurement is not feasible. These findings have implications for sustainable AI development, providing actionable insights for researchers, industry practitioners, and policymakers seeking to balance performance and resource efficiency in NLP applications.

