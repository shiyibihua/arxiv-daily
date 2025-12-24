---
layout: default
title: Adaptively Robust LLM Inference Optimization under Prediction Uncertainty
---

# Adaptively Robust LLM Inference Optimization under Prediction Uncertainty

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14544" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14544v2</a>
  <a href="https://arxiv.org/pdf/2508.14544.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14544v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14544v2', 'Adaptively Robust LLM Inference Optimization under Prediction Uncertainty')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixi Chen, Yinyu Ye, Zijie Zhou

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-08-20 (更新: 2025-09-01)

---

## 💡 一句话要点

**提出自适应鲁棒LLM推理优化算法以应对预测不确定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理调度` `预测不确定性` `自适应算法` `能效优化` `机器学习` `动态调整`

## 📋 核心要点

1. 核心问题：现有LLM推理调度面临输出长度未知的挑战，导致内存溢出和性能下降。
2. 方法要点：提出了自适应算法$	ext{A}_{	ext{min}}$，动态调整输出长度预测以提高调度效率。
3. 实验或效果：$	ext{A}_{	ext{min}}$在数值模拟中表现接近理想调度器，展现出良好的效率和鲁棒性。

## 📝 摘要（中文）

本文研究了优化大型语言模型（LLM）推理调度以最小化总延迟的问题。LLM推理是一个在线多任务服务过程，且能耗较高。由于输入请求的提示长度已知，但输出长度未知，导致内存使用和处理时间受到影响。为了解决这一不确定性，本文提出了基于机器学习的算法来预测输出长度，并设计了两种调度算法：保守算法$	ext{A}_{	ext{max}}$和自适应算法$	ext{A}_{	ext{min}}$。实验结果表明，$	ext{A}_{	ext{min}}$在实际场景中表现出色，接近于理想调度器的性能，展现了其效率和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型推理调度中的输出长度不确定性问题。现有方法如保守算法$	ext{A}_{	ext{max}}$，在预测不准确时可能导致性能显著下降，尤其是当预测过高时，可能导致内存溢出。

**核心思路**：论文提出的自适应算法$	ext{A}_{	ext{min}}$，初始将预测的下界视为输出长度，并在推理过程中动态调整这一估计，以应对预测的不确定性。这样的设计旨在提高调度的灵活性和效率。

**技术框架**：整体架构包括输入请求的接收、输出长度的预测、调度决策的制定和推理过程的执行。算法通过机器学习模型预测输出长度的区间，并根据下界进行调度。

**关键创新**：最重要的技术创新在于提出了自适应调度算法$	ext{A}_{	ext{min}}$，它能够在不依赖于上界预测的情况下，动态调整输出长度的估计，从而避免了保守算法的性能瓶颈。

**关键设计**：算法设计中，$	ext{A}_{	ext{min}}$依赖于下界预测，避免了对上界的依赖，且在推理过程中通过实时反馈不断优化输出长度的估计。

## 📊 实验亮点

实验结果显示，$	ext{A}_{	ext{min}}$在多次模拟中表现出色，其性能接近理想调度器，且在处理大量请求时，延迟显著低于传统保守算法，展现出良好的鲁棒性和效率。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能客服和实时翻译等场景，能够有效提升大型语言模型在多任务服务中的调度效率和能效，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We study the problem of optimizing Large Language Model (LLM) inference scheduling to minimize total latency. LLM inference is an online and multi-task service process and also heavily energy consuming by which a pre-trained LLM processes input requests and generates output tokens sequentially. Therefore, it is vital to improve its scheduling efficiency and reduce the power consumption while a great amount of prompt requests are arriving. A key challenge in LLM inference scheduling is that while the prompt length is known upon arrival, the output length, which critically impacts memory usage and processing time, is unknown. To address this uncertainty, we propose algorithms that leverage machine learning to predict output lengths, assuming the prediction provides an interval classification (min-max range) for each request.
>   We first design a conservative algorithm, $\mathcal{A}_{\max}$, which schedules requests based on the upper bound of predicted output lengths to prevent memory overflow. However, this approach is overly conservative: as prediction accuracy decreases, performance degrades significantly due to potential overestimation. To overcome this limitation, we propose $\mathcal{A}_{\min}$, an adaptive algorithm that initially treats the predicted lower bound as the output length and dynamically refines this estimate during inferencing. We prove that $\mathcal{A}_{\min}$ achieves a log-scale competitive ratio. Through numerical simulations, we demonstrate that $\mathcal{A}_{\min}$ often performs nearly as well as the hindsight scheduler, highlighting both its efficiency and robustness in practical scenarios. Moreover, $\mathcal{A}_{\min}$ relies solely on the lower bound of the prediction interval--an advantageous design choice since upper bounds on output length are typically more challenging to predict accurately.

