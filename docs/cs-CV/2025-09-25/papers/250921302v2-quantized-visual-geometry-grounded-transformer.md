---
layout: default
title: Quantized Visual Geometry Grounded Transformer
---

# Quantized Visual Geometry Grounded Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21302" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21302v2</a>
  <a href="https://arxiv.org/pdf/2509.21302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21302v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21302v2', 'Quantized Visual Geometry Grounded Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weilun Feng, Haotong Qin, Mingqiang Wu, Chuanguang Yang, Yuqi Li, Xiangqi Li, Zhulin An, Libo Huang, Yulun Zhang, Michele Magno, Yongjun Xu

**分类**: cs.CV

**发布日期**: 2025-09-25 (更新: 2025-09-30)

**🔗 代码/项目**: [GITHUB](https://github.com/wlfeng0509/QuantVGGT)

---

## 💡 一句话要点

**提出QuantVGGT，解决VGGT量化难题，实现资源受限场景下的高效3D重建。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `模型量化` `视觉几何引导Transformer` `后训练量化` `重尾分布`

## 📋 核心要点

1. 现有VGGT模型计算和内存成本高昂，难以在资源受限的场景中部署，后训练量化(PTQ)在VGGT上的应用面临重尾激活分布和校准样本选择不稳定的挑战。
2. QuantVGGT通过双重平滑细粒度量化缓解重尾分布和通道间方差，并利用噪声过滤多样性采样确保稳定的量化范围。
3. 实验结果表明，4位QuantVGGT在保持较高重建精度的同时，实现了3.7倍的内存减少和2.5倍的加速，优于现有量化方法。

## 📝 摘要（中文）

视觉几何引导Transformer (VGGT) 等基于学习的3D重建模型，受益于大规模Transformer，取得了显著进展。然而，其巨大的计算和内存成本严重阻碍了实际部署。后训练量化 (PTQ) 已成为压缩和加速模型的常用方法。但是，我们通过实验观察到，在压缩十亿级VGGT时，PTQ面临着独特的障碍：数据无关的特殊token导致重尾激活分布，而3D数据的多视角特性使得校准样本的选择非常不稳定。本文提出了第一个针对VGGT的量化框架，即QuantVGGT。这主要依赖于两项技术贡献：首先，我们引入了双重平滑细粒度量化，它集成了预全局Hadamard旋转和后局部通道平滑，以稳健地减轻重尾分布和通道间方差。其次，我们设计了噪声过滤多样性采样，通过深层统计信息过滤异常值，并构建帧感知多样性校准集群，以确保稳定的量化范围。综合实验表明，QuantVGGT在不同的基准和位宽上实现了最先进的结果，大大超过了以前最先进的通用量化方法。我们强调，我们的4位QuantVGGT可以在实际硬件推理中实现3.7倍的内存减少和2.5倍的加速，同时保持重建精度高于其全精度版本的98%。这证明了QuantVGGT在资源受限场景中的巨大优势和实用性。

## 🔬 方法详解

**问题定义**：现有基于Transformer的3D重建模型（如VGGT）参数量巨大，计算复杂度高，难以部署在资源受限的设备上。直接应用后训练量化（PTQ）方法压缩VGGT时，会遇到两个主要问题：一是数据无关的特殊token导致激活值呈现重尾分布，影响量化精度；二是多视角3D数据使得校准样本的选择不稳定，导致量化范围偏差。

**核心思路**：QuantVGGT的核心思路是针对VGGT的特性，设计专门的量化策略，以解决PTQ在VGGT上遇到的重尾激活分布和校准样本选择不稳定的问题。通过双重平滑细粒度量化来处理重尾分布，并通过噪声过滤多样性采样来稳定校准样本的选择。

**技术框架**：QuantVGGT的整体框架包含两个主要模块：双重平滑细粒度量化和噪声过滤多样性采样。首先，对VGGT模型进行预全局Hadamard旋转，然后进行量化，之后进行后局部通道平滑。同时，利用噪声过滤多样性采样方法选择合适的校准数据集，用于确定量化参数。

**关键创新**：QuantVGGT的关键创新在于针对VGGT的特性，提出了双重平滑细粒度量化和噪声过滤多样性采样两种技术。双重平滑细粒度量化通过预全局Hadamard旋转和后局部通道平滑，有效缓解了重尾激活分布和通道间方差，提高了量化精度。噪声过滤多样性采样通过深层统计信息过滤异常值，并构建帧感知多样性校准集群，确保了量化范围的稳定。

**关键设计**：双重平滑细粒度量化中，Hadamard旋转是一种正交变换，用于降低通道间的相关性，从而缓解重尾分布。后局部通道平滑则通过对量化后的激活值进行平滑处理，进一步降低量化误差。噪声过滤多样性采样中，深层统计信息用于识别和过滤异常值，帧感知多样性校准集群则保证了校准样本的多样性和代表性。具体的量化位宽选择和参数设置需要根据实际应用场景进行调整。

## 📊 实验亮点

QuantVGGT在多个3D重建基准测试中取得了state-of-the-art的结果，显著优于现有的通用量化方法。特别是在4位量化下，QuantVGGT实现了3.7倍的内存减少和2.5倍的加速，同时保持了重建精度高于全精度模型的98%。这些结果表明QuantVGGT在实际硬件上的高效性和实用性。

## 🎯 应用场景

QuantVGGT在资源受限的场景下具有广泛的应用前景，例如移动设备上的3D重建、机器人导航、增强现实等。通过降低模型的计算和内存需求，QuantVGGT使得这些应用能够在低功耗、低成本的硬件平台上运行，加速了3D重建技术的普及和应用。

## 📄 摘要（原文）

> Learning-based 3D reconstruction models, represented by Visual Geometry Grounded Transformers (VGGTs), have made remarkable progress with the use of large-scale transformers. Their prohibitive computational and memory costs severely hinder real-world deployment. Post-Training Quantization (PTQ) has become a common practice for compressing and accelerating models. However, we empirically observe that PTQ faces unique obstacles when compressing billion-scale VGGTs: the data-independent special tokens induce heavy-tailed activation distributions, while the multi-view nature of 3D data makes calibration sample selection highly unstable. This paper proposes the first Quantization framework for VGGTs, namely QuantVGGT. This mainly relies on two technical contributions: First, we introduce Dual-Smoothed Fine-Grained Quantization, which integrates pre-global Hadamard rotation and post-local channel smoothing to mitigate heavy-tailed distributions and inter-channel variance robustly. Second, we design Noise-Filtered Diverse Sampling, which filters outliers via deep-layer statistics and constructs frame-aware diverse calibration clusters to ensure stable quantization ranges. Comprehensive experiments demonstrate that QuantVGGT achieves the state-of-the-art results across different benchmarks and bit-width, surpassing the previous state-of-the-art generic quantization method with a great margin. We highlight that our 4-bit QuantVGGT can deliver a 3.7$\times$ memory reduction and 2.5$\times$ acceleration in real-hardware inference, while maintaining reconstruction accuracy above 98\% of its full-precision counterpart. This demonstrates the vast advantages and practicality of QuantVGGT in resource-constrained scenarios. Our code is released in https://github.com/wlfeng0509/QuantVGGT.

