---
layout: default
title: "FinMMDocR: Benchmarking Financial Multimodal Reasoning with Scenario Awareness, Document Understanding, and Multi-Step Computation"
---

# FinMMDocR: Benchmarking Financial Multimodal Reasoning with Scenario Awareness, Document Understanding, and Multi-Step Computation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24903" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24903v1</a>
  <a href="https://arxiv.org/pdf/2512.24903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24903v1', 'FinMMDocR: Benchmarking Financial Multimodal Reasoning with Scenario Awareness, Document Understanding, and Multi-Step Computation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zichen Tang, Haihong E, Rongjin Li, Jiacheng Liu, Linwei Jia, Zhuodi Hao, Zhongjun Yang, Yuanze Li, Haolin Tian, Xinyi Hu, Peizhi Zhao, Yuan Liu, Zhengyu Wang, Xianghe Wang, Yiling Huang, Xueyuan Lin, Ruofei Bai, Zijian Xie, Qian Huang, Ruining Cao, Haocheng Gao

**分类**: cs.CV, cs.CE

**发布日期**: 2025-12-31

**备注**: Accepted by AAAI-26 Main Track

---

## 💡 一句话要点

**FinMMDocR：提出金融多模态推理基准，关注场景感知、文档理解和多步计算。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融多模态推理` `大型语言模型` `基准测试` `场景感知` `文档理解` `多步计算` `检索增强生成`

## 📋 核心要点

1. 现有基准在金融领域的多模态推理方面存在不足，缺乏对复杂场景、深度文档理解和多步计算的有效评估。
2. FinMMDocR通过引入场景感知、深度金融文档和多步计算，构建更贴近真实金融场景的多模态推理基准。
3. 实验表明，现有最佳MLLM在FinMMDocR上表现仍有提升空间，且RAG方法性能差异显著，突显了该基准的挑战性。

## 📝 摘要（中文）

本文提出了FinMMDocR，这是一个新的双语多模态基准，用于评估多模态大型语言模型（MLLM）在真实金融数值推理方面的能力。与现有基准相比，FinMMDocR有三个主要进展：(1) 场景感知：1200个专家标注的问题中，57.9%的问题融入了12种隐式金融场景（例如，投资组合管理），挑战模型基于假设执行专家级推理；(2) 文档理解：837篇中文/英文文档涵盖9种类型（例如，公司研究），平均50.8页，包含丰富的视觉元素，在金融文档的广度和深度上显著超越现有基准；(3) 多步计算：问题平均需要11步推理（5.3步提取+5.7步计算），其中65.0%需要跨页证据（平均2.4页）。性能最佳的MLLM仅达到58.0%的准确率，并且不同的检索增强生成（RAG）方法在该任务上表现出显著的性能差异。我们期望FinMMDocR能够推动MLLM和推理增强方法在真实场景中复杂多模态推理任务上的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）在真实金融场景下进行数值推理时面临的挑战。现有方法在场景感知、文档理解深度和多步计算能力方面存在不足，难以有效处理复杂的金融文档和推理任务。

**核心思路**：论文的核心思路是构建一个更具挑战性和真实性的金融多模态推理基准，即FinMMDocR。该基准通过引入隐式金融场景、深度金融文档和多步计算，迫使模型进行更深入的理解和推理，从而更好地评估和提升MLLM在金融领域的应用能力。

**技术框架**：FinMMDocR基准包含以下几个关键组成部分：1) 大量的金融文档，涵盖多种类型和格式；2) 专家标注的问题，包含隐式金融场景和多步计算要求；3) 评估指标，用于衡量模型在场景感知、文档理解和多步计算方面的性能。整体流程是：给定金融文档和问题，模型需要提取相关信息、进行计算和推理，最终给出答案。

**关键创新**：FinMMDocR的关键创新在于其对真实金融场景的模拟和对模型推理能力的深度评估。具体体现在：1) 引入了隐式金融场景，要求模型具备专家级的推理能力；2) 采用了深度金融文档，挑战模型的文档理解能力；3) 设计了多步计算问题，考察模型的推理和计算能力。

**关键设计**：FinMMDocR基准包含1200个专家标注的问题，其中57.9%的问题包含12种隐式金融场景。文档方面，包含837篇中文/英文文档，涵盖9种类型，平均50.8页。问题平均需要11步推理（5.3步提取+5.7步计算），其中65.0%需要跨页证据（平均2.4页）。评估指标包括准确率等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24903v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24903v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24903v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，现有最佳MLLM在FinMMDocR上的准确率仅为58.0%，表明该基准具有很高的挑战性。此外，不同的RAG方法在该任务上表现出显著的性能差异，突显了检索和推理策略的重要性。这些结果为未来研究提供了明确的方向，即需要进一步提升MLLM在场景感知、文档理解和多步计算方面的能力。

## 🎯 应用场景

FinMMDocR的研究成果可应用于金融领域的智能投顾、风险评估、财务分析等场景。通过提升MLLM在金融多模态推理方面的能力，可以帮助金融从业者更高效地处理海量金融数据，做出更明智的决策，并为投资者提供更优质的服务。未来，该基准可以促进金融领域AI应用的进一步发展。

## 📄 摘要（原文）

> We introduce FinMMDocR, a novel bilingual multimodal benchmark for evaluating multimodal large language models (MLLMs) on real-world financial numerical reasoning. Compared to existing benchmarks, our work delivers three major advancements. (1) Scenario Awareness: 57.9% of 1,200 expert-annotated problems incorporate 12 types of implicit financial scenarios (e.g., Portfolio Management), challenging models to perform expert-level reasoning based on assumptions; (2) Document Understanding: 837 Chinese/English documents spanning 9 types (e.g., Company Research) average 50.8 pages with rich visual elements, significantly surpassing existing benchmarks in both breadth and depth of financial documents; (3) Multi-Step Computation: Problems demand 11-step reasoning on average (5.3 extraction + 5.7 calculation steps), with 65.0% requiring cross-page evidence (2.4 pages average). The best-performing MLLM achieves only 58.0% accuracy, and different retrieval-augmented generation (RAG) methods show significant performance variations on this task. We expect FinMMDocR to drive improvements in MLLMs and reasoning-enhanced methods on complex multimodal reasoning tasks in real-world scenarios.

