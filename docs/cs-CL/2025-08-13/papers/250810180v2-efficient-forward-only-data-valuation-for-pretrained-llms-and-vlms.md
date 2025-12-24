---
layout: default
title: Efficient Forward-Only Data Valuation for Pretrained LLMs and VLMs
---

# Efficient Forward-Only Data Valuation for Pretrained LLMs and VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10180" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10180v2</a>
  <a href="https://arxiv.org/pdf/2508.10180.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10180v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10180v2', 'Efficient Forward-Only Data Valuation for Pretrained LLMs and VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenlong Deng, Jiaming Zhang, Qi Zeng, Christos Thrampoulidis, Boying Gong, Xiaoxiao Li

**分类**: cs.CL

**发布日期**: 2025-08-13 (更新: 2025-08-18)

---

## 💡 一句话要点

**提出For-Value框架以高效评估大模型数据影响力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据估值` `大模型` `前向计算` `影响力评估` `自然语言处理` `计算机视觉` `模型透明度` `样本选择`

## 📋 核心要点

1. 现有数据估值方法依赖于Hessian信息或模型重训练，计算成本高，难以应用于亿参数模型。
2. 提出For-Value框架，通过一次前向传递计算影响力分数，避免了梯度计算的高昂开销。
3. 实验结果显示，For-Value在识别重要样本和检测错误标记数据方面，性能与基于梯度的方法相当或更优。

## 📝 摘要（中文）

量化单个训练样本的影响力对于提升大型语言模型（LLMs）和视觉语言模型（VLMs）的透明度和问责制至关重要。然而，现有的数据估值方法通常依赖于Hessian信息或模型重训练，这使得其在亿参数模型上计算成本高昂。本文提出了For-Value，一个前向数据估值框架，能够为LLMs和VLMs提供可扩展且高效的影响力估计。通过利用现代基础模型的丰富表示，For-Value仅通过一次前向传递计算影响力分数，从而消除了昂贵的梯度计算需求。理论分析表明，For-Value通过捕捉训练样本与验证样本之间的隐藏表示和预测误差的对齐，准确估计每个样本的影响力。大量实验表明，For-Value在识别重要的微调示例和有效检测错误标记数据方面，与基于梯度的方法相比表现相当或更优。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数据估值方法在大规模模型中计算成本高的问题。传统方法依赖于Hessian信息或重训练，导致在亿参数模型上难以实施。

**核心思路**：For-Value框架通过一次前向传递计算影响力分数，利用现代基础模型的表示能力，避免了复杂的梯度计算，从而实现高效的数据估值。

**技术框架**：For-Value的整体架构包括数据输入、前向传递计算、影响力分数生成和结果输出四个主要模块。通过前向传递，模型能够快速评估每个训练样本的影响力。

**关键创新**：For-Value的核心创新在于其前向计算方法，能够在不依赖梯度信息的情况下，准确评估样本影响力。这一设计显著降低了计算复杂度，与传统方法形成鲜明对比。

**关键设计**：在实现中，For-Value采用简单的闭式表达式来计算影响力分数，确保了计算的高效性和准确性。模型的参数设置和损失函数设计经过精心调整，以适应不同的任务需求。

## 📊 实验亮点

实验结果表明，For-Value在识别重要微调样本方面与基于梯度的方法相比，性能相当或更优，且在检测错误标记数据时表现出色，展示了其在数据估值中的有效性和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉及其交叉领域，能够提升模型的透明度和问责制。For-Value框架可用于数据清洗、样本选择和模型优化等任务，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Quantifying the influence of individual training samples is essential for enhancing the transparency and accountability of large language models (LLMs) and vision-language models (VLMs). However, existing data valuation methods often rely on Hessian information or model retraining, making them computationally prohibitive for billion-parameter models. In this work, we introduce For-Value, a forward-only data valuation framework that enables scalable and efficient influence estimation for both LLMs and VLMs. By leveraging the rich representations of modern foundation models, For-Value computes influence scores using a simple closed-form expression based solely on a single forward pass, thereby eliminating the need for costly gradient computations. Our theoretical analysis demonstrates that For-Value accurately estimates per-sample influence by capturing alignment in hidden representations and prediction errors between training and validation samples. Extensive experiments show that For-Value matches or outperforms gradient-based baselines in identifying impactful fine-tuning examples and effectively detecting mislabeled data.

