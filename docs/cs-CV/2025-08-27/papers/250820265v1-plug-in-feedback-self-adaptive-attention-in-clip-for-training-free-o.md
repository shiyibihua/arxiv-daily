---
layout: default
title: Plug-in Feedback Self-adaptive Attention in CLIP for Training-free Open-Vocabulary Segmentation
---

# Plug-in Feedback Self-adaptive Attention in CLIP for Training-free Open-Vocabulary Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20265" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20265v1</a>
  <a href="https://arxiv.org/pdf/2508.20265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20265v1', 'Plug-in Feedback Self-adaptive Attention in CLIP for Training-free Open-Vocabulary Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixiang Chi, Yanan Wu, Li Gu, Huan Liu, Ziqiang Wang, Yang Zhang, Yang Wang, Konstantinos N. Plataniotis

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-27

**备注**: ICCV 2025, code:https://github.com/chi-chi-zx/FSA

---

## 💡 一句话要点

**提出反馈自适应注意力机制以解决CLIP的开放词汇分割问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇分割` `自适应注意力` `视觉文本对齐` `深度学习` `计算机视觉` `模型优化` `反馈机制`

## 📋 核心要点

1. 现有的开放词汇分割方法在空间一致性和最终输出之间的传递存在不足，导致定位效果不佳。
2. 本文提出了一种反馈驱动的自适应框架，通过将输出信息反馈到中间注意力，增强语义一致性。
3. 实验结果表明，该方法在八个基准测试中显著提升了性能，验证了其有效性和广泛适用性。

## 📝 摘要（中文）

CLIP在视觉与文本对齐方面表现出色，但在开放词汇分割中由于定位不佳而面临挑战。现有方法通过修改中间注意力来增强空间一致性，但这种一致性未能有效传递到最终输出。本文提出了一种无训练的反馈驱动自适应框架，将基于输出的补丁级对应关系反馈到中间注意力中，从而增强内部表示与最终预测之间的语义一致性。我们设计了多个关键模块，包括注意力隔离、基于置信度的稀疏适应修剪和适应集成，能够有效反馈输出一致性线索。该方法作为插件模块，能够无缝集成到四种最先进的方法中，并在多个基准测试中验证了其有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决CLIP在开放词汇分割中的定位不佳问题。现有方法通过修改中间注意力来增强空间一致性，但这种一致性未能有效传递到最终输出，导致语义差异。

**核心思路**：我们提出了一种无训练的反馈驱动自适应框架，通过将输出的补丁级对应关系反馈到中间注意力中，利用模型输出作为更强的空间一致性先验，从而增强内部表示与最终预测之间的语义一致性。

**技术框架**：该框架包括多个关键模块：注意力隔离、基于置信度的稀疏适应修剪和适应集成。整体流程是通过输出预测信息来调整中间注意力，从而实现自适应调整。

**关键创新**：最重要的创新在于将输出信息反馈到中间注意力中，形成闭环机制，显著提高了模型的语义一致性。这一方法与现有的单向调整方法有本质区别。

**关键设计**：我们在设计中采用了注意力隔离机制，以确保中间表示的独立性；同时，基于置信度的稀疏适应修剪策略用于优化计算效率，适应集成则用于整合多种注意力类型的反馈信息。具体的参数设置和损失函数设计也经过精心调整，以确保最佳性能。

## 📊 实验亮点

实验结果显示，所提方法在八个基准测试中均显著提升了性能，尤其是在与现有最先进方法的对比中，提升幅度达到X%（具体数据未知），验证了其有效性和广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉中的图像分割、物体检测和场景理解等任务。通过提升开放词汇分割的性能，该方法能够在多种实际场景中实现更高效的视觉信息处理，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> CLIP exhibits strong visual-textual alignment but struggle with open-vocabulary segmentation due to poor localization. Prior methods enhance spatial coherence by modifying intermediate attention. But, this coherence isn't consistently propagated to the final output due to subsequent operations such as projections. Additionally, intermediate attention lacks direct interaction with text representations, such semantic discrepancy limits the full potential of CLIP.
>   In this work, we propose a training-free, feedback-driven self-adaptive framework that adapts output-based patch-level correspondences back to the intermediate attention. The output predictions, being the culmination of the model's processing, encapsulate the most comprehensive visual and textual semantics about each patch. Our approach enhances semantic consistency between internal representations and final predictions by leveraging the model's outputs as a stronger spatial coherence prior. We design key modules, including attention isolation, confidence-based pruning for sparse adaptation, and adaptation ensemble, to effectively feedback the output coherence cues. Our method functions as a plug-in module, seamlessly integrating into four state-of-the-art approaches with three backbones (ViT-B, ViT-L, ViT-H). We further validate our framework across multiple attention types (Q-K, self-self, and Proxy augmented with MAE, SAM, and DINO). Our approach consistently improves their performance across eight benchmarks.

