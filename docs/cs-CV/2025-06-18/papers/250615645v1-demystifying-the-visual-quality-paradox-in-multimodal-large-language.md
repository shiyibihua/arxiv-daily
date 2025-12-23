---
layout: default
title: Demystifying the Visual Quality Paradox in Multimodal Large Language Models
---

# Demystifying the Visual Quality Paradox in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15645" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15645v1</a>
  <a href="https://arxiv.org/pdf/2506.15645.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15645v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15645v1', 'Demystifying the Visual Quality Paradox in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuo Xing, Lanqing Guo, Hongyuan Hua, Seoyoung Lee, Peiran Li, Yufei Wang, Zhangyang Wang, Zhengzhong Tu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-18

**备注**: 18 pages

---

## 💡 一句话要点

**提出VQ-TTT以解决多模态大语言模型的视觉质量悖论问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉质量` `测试时调优` `图像处理` `模型适应性` `深度学习`

## 📋 核心要点

1. 现有的多模态大语言模型在视觉质量与模型理解之间的关系尚不明确，导致对输入图像质量的理解不足。
2. 论文提出视觉质量测试时调优（VQ-TTT），通过动态调整输入图像以适应任务特定的模型偏好，提升模型性能。
3. 实验结果表明，VQ-TTT显著提高了多模态大语言模型的平均准确率，且无需依赖外部模型或额外数据。

## 📝 摘要（中文）

近期的多模态大语言模型（MLLMs）在视觉-语言基准任务上表现优异，但关于输入视觉质量如何影响其响应仍知之甚少。我们进行了一项系统研究，发现视觉质量悖论：当图像偏离人类感知的真实度时，模型和任务的表现反而可能提高。为此，我们提出了视觉质量测试时调优（VQ-TTT），该模块通过在冻结的视觉编码器前插入可学习的低秩核，调节频率内容，并通过LoRA微调浅层视觉编码器。VQ-TTT在单次前向传播中动态调整每个输入图像，显著提升了评估的MLLMs在所有数据集上的平均准确率，无需外部模型或额外训练数据。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态大语言模型在视觉输入质量与模型响应之间的悖论，现有方法未能有效利用图像质量的变化来提升模型性能。

**核心思路**：提出视觉质量测试时调优（VQ-TTT），通过在视觉编码器前插入可学习的低秩核，调整输入图像的频率内容，以适应不同任务的需求。

**技术框架**：VQ-TTT模块包括两个主要部分：首先，在冻结的视觉编码器前插入低秩核；其次，通过LoRA技术微调视觉编码器的浅层层次，以实现对输入图像的动态调整。

**关键创新**：VQ-TTT的创新之处在于其能够在不依赖外部模型或额外训练数据的情况下，动态优化输入图像，从而提升模型的任务适应性和准确性。

**关键设计**：VQ-TTT的设计包括可学习的低秩核的参数设置，以及通过LoRA微调的具体层次选择，确保在保持模型稳定性的同时，提升其对视觉输入的适应能力。

## 📊 实验亮点

实验结果显示，VQ-TTT在所有评估的多模态大语言模型上显著提高了平均准确率，具体提升幅度达到X%（具体数据待补充），且在不同数据集上均表现出色，验证了其有效性和普适性。

## 🎯 应用场景

该研究的潜在应用领域包括图像识别、自然语言处理和人机交互等多个领域。通过优化多模态大语言模型的输入质量，可以显著提升模型在实际应用中的表现，推动智能助手、自动翻译和内容生成等技术的发展。

## 📄 摘要（原文）

> Recent Multimodal Large Language Models (MLLMs) excel on benchmark vision-language tasks, yet little is known about how input visual quality shapes their responses. Does higher perceptual quality of images already translate to better MLLM understanding? We conduct the first systematic study spanning leading MLLMs and a suite of vision-language benchmarks, applying controlled degradations and stylistic shifts to each image. Surprisingly, we uncover a visual-quality paradox: model, task, and even individual-instance performance can improve when images deviate from human-perceived fidelity. Off-the-shelf restoration pipelines fail to reconcile these idiosyncratic preferences. To close the gap, we introduce Visual-Quality Test-Time Tuning (VQ-TTT)-a lightweight adaptation module that: (1) inserts a learnable, low-rank kernel before the frozen vision encoder to modulate frequency content; and (2) fine-tunes only shallow vision-encoder layers via LoRA. VQ-TTT dynamically adjusts each input image in a single forward pass, aligning it with task-specific model preferences. Across the evaluated MLLMs and all datasets, VQ-TTT lifts significant average accuracy, with no external models, cached features, or extra training data. These findings redefine ``better'' visual inputs for MLLMs and highlight the need for adaptive, rather than universally ``clean'', imagery, in the new era of AI being the main data customer.

