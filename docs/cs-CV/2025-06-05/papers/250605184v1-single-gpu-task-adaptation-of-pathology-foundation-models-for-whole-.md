---
layout: default
title: Single GPU Task Adaptation of Pathology Foundation Models for Whole Slide Image Analysis
---

# Single GPU Task Adaptation of Pathology Foundation Models for Whole Slide Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05184" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05184v1</a>
  <a href="https://arxiv.org/pdf/2506.05184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05184v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05184v1', 'Single GPU Task Adaptation of Pathology Foundation Models for Whole Slide Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Neeraj Kumar, Swaraj Nanda, Siddharth Singi, Jamal Benhamida, David Kim, Jie-Fu Chen, Amir Momeni-Boroujeni, Gregory M. Goldgof, Gabriele Campanella, Chad Vanderbilt

**分类**: cs.CV

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出TAPFM以解决病理基础模型在全切片图像分析中的适应性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理基础模型` `全切片图像` `多实例学习` `视觉变换器` `临床应用` `突变预测` `多标签分类`

## 📋 核心要点

1. 现有方法在将预训练的病理基础模型适应于特定临床任务时面临挑战，尤其是缺乏足够的标签信息。
2. 论文提出的TAPFM方法利用视觉变换器的注意力机制进行多实例学习聚合，优化特征表示和注意力权重。
3. 在膀胱癌和肺腺癌的突变预测任务中，TAPFM表现优于传统方法，显示出显著的性能提升。

## 📝 摘要（中文）

病理基础模型（PFMs）已成为分析全切片图像（WSIs）的强大工具。然而，将这些预训练的PFMs适应于特定临床任务面临重大挑战，主要是由于仅有的弱标签（WSI级别）对于千兆像素图像的限制， necessitating multiple instance learning (MIL)范式以有效进行WSI分析。本文提出了一种新颖的单GPU任务适应PFMs的方法（TAPFM），该方法利用视觉变换器（ViT）注意力进行MIL聚合，同时优化特征表示和注意力权重。所提出的方法为MIL聚合器和PFM维护独立的计算图，以创建稳定的训练动态，与下游任务目标对齐。通过在膀胱癌和肺腺癌的突变预测任务上进行评估，TAPFM始终优于传统方法，H-Optimus-0（TAPFM）超越了基准。TAPFM还有效处理可操作突变的多标签分类。因此，TAPFM使得在标准硬件上对强大的预训练PFMs进行适应成为可能，适用于各种临床应用。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效地将预训练的病理基础模型（PFMs）适应于特定的临床任务，尤其是在仅有WSI级别的弱标签情况下，现有方法在处理千兆像素图像时表现不佳。

**核心思路**：论文提出的TAPFM方法通过使用视觉变换器（ViT）注意力机制进行多实例学习（MIL）聚合，优化特征表示和注意力权重，从而提高模型在特定任务上的适应性和性能。

**技术框架**：TAPFM的整体架构包括两个主要模块：MIL聚合器和PFM。它们分别维护独立的计算图，以确保训练过程的稳定性，并与下游任务目标保持一致。

**关键创新**：TAPFM的核心创新在于其独特的训练动态设计，通过分离MIL聚合器和PFM的计算图，显著提升了模型的适应能力和稳定性。这与现有方法的单一计算图设计形成鲜明对比。

**关键设计**：在参数设置上，TAPFM采用了特定的损失函数以优化多标签分类任务，同时在网络结构中引入了视觉变换器的注意力机制，以增强特征提取能力。

## 📊 实验亮点

在膀胱癌和肺腺癌的突变预测任务中，TAPFM的表现显著优于传统方法，H-Optimus-0（TAPFM）在多个基准测试中均取得了更高的准确率，展示了其在多标签分类任务中的有效性和可靠性。

## 🎯 应用场景

该研究具有广泛的潜在应用场景，尤其是在医学影像分析领域。通过提高病理基础模型在特定任务上的适应性，TAPFM可以帮助临床医生更准确地进行疾病诊断和突变预测，进而推动个性化医疗的发展。未来，TAPFM的技术框架也可扩展至其他医学图像分析任务，提升整体医疗效率。

## 📄 摘要（原文）

> Pathology foundation models (PFMs) have emerged as powerful tools for analyzing whole slide images (WSIs). However, adapting these pretrained PFMs for specific clinical tasks presents considerable challenges, primarily due to the availability of only weak (WSI-level) labels for gigapixel images, necessitating multiple instance learning (MIL) paradigm for effective WSI analysis. This paper proposes a novel approach for single-GPU \textbf{T}ask \textbf{A}daptation of \textbf{PFM}s (TAPFM) that uses vision transformer (\vit) attention for MIL aggregation while optimizing both for feature representations and attention weights. The proposed approach maintains separate computational graphs for MIL aggregator and the PFM to create stable training dynamics that align with downstream task objectives during end-to-end adaptation. Evaluated on mutation prediction tasks for bladder cancer and lung adenocarcinoma across institutional and TCGA cohorts, TAPFM consistently outperforms conventional approaches, with H-Optimus-0 (TAPFM) outperforming the benchmarks. TAPFM effectively handles multi-label classification of actionable mutations as well. Thus, TAPFM makes adaptation of powerful pre-trained PFMs practical on standard hardware for various clinical applications.

