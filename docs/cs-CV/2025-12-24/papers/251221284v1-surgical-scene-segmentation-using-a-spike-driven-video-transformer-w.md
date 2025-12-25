---
layout: default
title: Surgical Scene Segmentation using a Spike-Driven Video Transformer with Real-Time Potential
---

# Surgical Scene Segmentation using a Spike-Driven Video Transformer with Real-Time Potential

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21284" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21284v1</a>
  <a href="https://arxiv.org/pdf/2512.21284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21284v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21284v1', 'Surgical Scene Segmentation using a Spike-Driven Video Transformer with Real-Time Potential')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shihao Zou, Jingjing Li, Wei Ji, Jincai Huang, Kai Wang, Guo Dan, Weixin Si, Yi Pan

**分类**: cs.CV

**发布日期**: 2025-12-24

---

## 💡 一句话要点

**提出SpikeSurgSeg，一种基于脉冲神经网络的视频Transformer，用于实时手术场景分割。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手术场景分割` `脉冲神经网络` `视频Transformer` `实时性` `掩码自动编码`

## 📋 核心要点

1. 现有深度学习模型在手术场景分割中计算量大、功耗高，难以在资源受限环境中实时部署。
2. 提出SpikeSurgSeg，利用脉冲神经网络（SNN）和视频Transformer，结合掩码自动编码预训练，实现高效分割。
3. 实验表明，SpikeSurgSeg在保持分割精度的同时，显著降低了推理延迟，加速比超过传统模型。

## 📝 摘要（中文）

现代手术系统越来越依赖智能场景理解，以提供及时的态势感知，从而增强术中安全性。其中，手术场景分割在准确感知手术事件方面起着核心作用。虽然最近的深度学习模型，特别是大型基础模型，取得了显著的分割精度，但它们巨大的计算需求和功耗阻碍了在资源受限的手术环境中进行实时部署。为了解决这个限制，我们探索了新兴的脉冲神经网络（SNN），作为高效手术智能的有希望的范例。然而，它们的性能仍然受到标记手术数据稀缺和手术视频表示固有稀疏性的限制。为此，我们提出了SpikeSurgSeg，这是第一个为手术场景分割量身定制的脉冲驱动视频Transformer框架，具有在非GPU平台上实现实时性的潜力。为了解决手术注释的有限可用性，我们引入了一种用于SNN的手术场景掩码自动编码预训练策略，该策略通过分层管掩码实现鲁棒的时空表示学习。在此预训练骨干网络的基础上，我们进一步采用了一种轻量级的脉冲驱动分割头，该分割头产生时间上一致的预测，同时保持了SNN的低延迟特性。在EndoVis18和我们内部的SurgBleed数据集上的大量实验表明，SpikeSurgSeg实现了与基于ANN的SOTA模型相当的mIoU，同时将推理延迟降低了至少8倍。值得注意的是，相对于大多数基础模型基线，它提供了超过20倍的加速，突显了其在时间关键型手术场景分割中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决手术场景分割中现有深度学习模型计算量大、功耗高，难以实时部署的问题。现有方法，特别是基于大型基础模型的方案，虽然精度高，但计算资源需求巨大，无法满足手术环境的实时性要求。此外，手术数据标注稀缺以及手术视频的稀疏性也限制了SNN的性能。

**核心思路**：论文的核心思路是利用脉冲神经网络（SNN）的低功耗、高效率特性，结合Transformer架构强大的时空建模能力，构建一个适用于手术场景分割的实时系统。通过掩码自动编码预训练，解决手术数据标注稀缺的问题，提升SNN的性能。

**技术框架**：SpikeSurgSeg框架主要包含两个阶段：预训练阶段和分割阶段。预训练阶段采用手术场景掩码自动编码（Surgical-Scene Masked Autoencoding）策略，对SNN骨干网络进行预训练，学习鲁棒的时空表示。分割阶段则使用一个轻量级的脉冲驱动分割头，基于预训练的骨干网络进行手术场景分割，生成时间一致的预测。

**关键创新**：论文的关键创新在于：1) 提出了SpikeSurgSeg，这是第一个基于脉冲神经网络的视频Transformer框架，专门为手术场景分割设计。2) 引入了手术场景掩码自动编码预训练策略，有效解决了手术数据标注稀缺的问题，提升了SNN的性能。3) 设计了一个轻量级的脉冲驱动分割头，保证了分割的实时性和时间一致性。

**关键设计**：在预训练阶段，采用了分层管掩码（layer-wise tube masking）策略，对输入视频进行掩码，迫使网络学习被掩码部分的信息，从而提升模型的鲁棒性。分割头的设计注重轻量化和低延迟，采用简单的卷积层和脉冲神经元，以保证实时性。损失函数方面，可能采用了交叉熵损失或Dice损失等常用的分割损失函数，具体细节未在摘要中明确说明。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21284v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21284v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21284v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SpikeSurgSeg在EndoVis18和SurgBleed数据集上取得了与SOTA的ANN模型相当的mIoU，同时将推理延迟降低了至少8倍。相对于大多数基础模型基线，它提供了超过20倍的加速，充分证明了其在时间关键型手术场景分割中的潜力。

## 🎯 应用场景

该研究成果可应用于智能手术机器人、术中导航系统和增强现实手术辅助等领域。通过实时分割手术场景，可以为医生提供更准确的术中信息，提高手术安全性，减少手术并发症，并有望实现更精准的手术操作。未来，该技术还可扩展到其他医疗影像分析任务，如病灶检测和器官分割。

## 📄 摘要（原文）

> Modern surgical systems increasingly rely on intelligent scene understanding to provide timely situational awareness for enhanced intra-operative safety. Within this pipeline, surgical scene segmentation plays a central role in accurately perceiving operative events. Although recent deep learning models, particularly large-scale foundation models, achieve remarkable segmentation accuracy, their substantial computational demands and power consumption hinder real-time deployment in resource-constrained surgical environments. To address this limitation, we explore the emerging SNN as a promising paradigm for highly efficient surgical intelligence. However, their performance is still constrained by the scarcity of labeled surgical data and the inherently sparse nature of surgical video representations. To this end, we propose \textit{SpikeSurgSeg}, the first spike-driven video Transformer framework tailored for surgical scene segmentation with real-time potential on non-GPU platforms. To address the limited availability of surgical annotations, we introduce a surgical-scene masked autoencoding pretraining strategy for SNNs that enables robust spatiotemporal representation learning via layer-wise tube masking. Building on this pretrained backbone, we further adopt a lightweight spike-driven segmentation head that produces temporally consistent predictions while preserving the low-latency characteristics of SNNs. Extensive experiments on EndoVis18 and our in-house SurgBleed dataset demonstrate that SpikeSurgSeg achieves mIoU comparable to SOTA ANN-based models while reducing inference latency by at least $8\times$. Notably, it delivers over $20\times$ acceleration relative to most foundation-model baselines, underscoring its potential for time-critical surgical scene segmentation.

