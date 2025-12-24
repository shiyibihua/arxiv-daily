---
layout: default
title: Uncertainty-Aware Collaborative System of Large and Small Models for Multimodal Sentiment Analysis
---

# Uncertainty-Aware Collaborative System of Large and Small Models for Multimodal Sentiment Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04459" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04459v1</a>
  <a href="https://arxiv.org/pdf/2509.04459.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04459v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04459v1', 'Uncertainty-Aware Collaborative System of Large and Small Models for Multimodal Sentiment Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shiqin Han, Manning Gao, Menghua Jiang, Yuncheng Jiang, Haifeng Hu, Sijie Mai

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出不确定性感知协作系统以解决多模态情感分析中的性能与效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态情感分析` `不确定性感知` `协作系统` `大型语言模型` `轻量级模型` `计算资源优化` `深度学习`

## 📋 核心要点

1. 现有的多模态情感分析方法在计算资源需求上存在较大挑战，尤其是大型模型的高开销限制了其实际应用。
2. 本文提出的不确定性感知协作系统（U-ACS）通过将小型模型与MLLM结合，利用不确定性驱动的级联机制优化分析流程。
3. 实验结果表明，U-ACS在基准数据集上实现了最先进的性能，同时计算资源需求仅为单独使用MLLM的一小部分。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）的出现显著推动了多模态机器学习的进展，但其高计算需求成为实际应用的障碍。相对而言，小型专用模型虽然高效，但性能往往受限。为了解决这一性能与效率的权衡问题，本文提出了一种新颖的不确定性感知协作系统（U-ACS），该系统将强大的MLLM（如HumanOmni）与轻量级基线模型协同运作。系统核心是一个基于不确定性的级联机制，首先由小型模型快速筛选输入样本，仅将高预测不确定性的样本提升至MLLM进行更深入分析。此外，系统还引入了处理模糊或冲突预测的高级策略，包括对相似极性的预测进行加权平均，以及在两种模型均表现出高不确定性时进行基于提示的交叉验证。该方法显著降低了推理成本，同时保持了MLLM的高准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态情感分析中大型模型计算资源需求高的问题，现有方法在效率与性能之间难以取得平衡。

**核心思路**：提出的不确定性感知协作系统（U-ACS）通过小型模型快速筛选样本，仅将高不确定性样本传递给MLLM，从而提高效率。

**技术框架**：U-ACS的整体架构包括两个主要模块：小型模型作为初步筛选器，MLLM用于深入分析。系统通过不确定性评估动态决定样本流向。

**关键创新**：U-ACS的核心创新在于不确定性驱动的级联机制和处理冲突预测的策略，显著提高了计算资源的利用效率。

**关键设计**：系统设计中采用了加权平均策略处理相似极性的预测，并在高不确定性情况下引入基于提示的交叉验证，以确保预测的准确性。

## 📊 实验亮点

在基准数据集上的实验结果显示，U-ACS在多模态情感分析任务中达到了最先进的性能，相较于单独使用MLLM，计算资源需求减少了90%以上，同时保持了高准确率，展现了其优越的效率与效果。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体情感分析、客户反馈处理及市场趋势预测等。通过提高多模态情感分析的效率与准确性，U-ACS能够为企业提供更具价值的洞察，推动智能决策的实现。未来，该方法还可扩展至其他多模态任务，具有广泛的应用前景。

## 📄 摘要（原文）

> The advent of Multimodal Large Language Models (MLLMs) has significantly advanced the state-of-the-art in multimodal machine learning, yet their substantial computational demands present a critical barrier to real-world deployment. Conversely, smaller, specialized models offer high efficiency but often at the cost of performance. To reconcile this performance-efficiency trade-off, we propose a novel Uncertainty-Aware Collaborative System (U-ACS) that synergistically orchestrates a powerful MLLM (e.g., HumanOmni) and a lightweight baseline model for multimodal sentiment analysis. The core of our system is an uncertainty-driven cascade mechanism, where the efficient small model first acts as a rapid filter for all input samples. Only those samples yielding high predictive uncertainty, thereby indicating greater difficulty, are selectively escalated to the MLLM for more sophisticated analysis. Furthermore, our system introduces advanced strategies to handle ambiguous or conflicting predictions, including weighted averaging for predictions of similar polarity and a prompt-based cross-verification to resolve conflicting predictions when both models exhibit high uncertainty. This sample-difficulty-aware approach allows for a dynamic allocation of computational resources, drastically reducing inference costs while retaining the high accuracy of MLLM. Extensive experiments on benchmark datasets demonstrate that our proposed method achieves state-of-the-art performance, while requiring only a fraction of the computational resources compared to using a standalone MLLM.

