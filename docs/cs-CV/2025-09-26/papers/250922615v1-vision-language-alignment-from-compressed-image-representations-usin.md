---
layout: default
title: Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting
---

# Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22615" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22615v1</a>
  <a href="https://arxiv.org/pdf/2509.22615.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22615v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22615v1', 'Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yasmine Omri, Connor Ding, Tsachy Weissman, Thierry Tambe

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**利用2D高斯溅射压缩图像表示实现视觉-语言对齐**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `2D高斯溅射` `视觉-语言对齐` `图像压缩` `边缘计算` `零样本学习`

## 📋 核心要点

1. 现有视觉-语言模型依赖RGB图像，存在传输成本高和token序列过长的问题。
2. 论文提出使用2D高斯溅射(2DGS)作为视觉表示，实现图像压缩和高效的视觉-语言对齐。
3. 实验表明，基于2DGS的编码器在压缩图像的同时，实现了可观的零样本ImageNet-1K性能。

## 📝 摘要（中文）

现代视觉语言流程依赖于在海量图像文本语料库上训练的RGB视觉编码器。尽管这些流程实现了令人印象深刻的零样本能力和强大的跨任务迁移，但它们仍然继承了像素域的两个结构性低效问题：(i) 从边缘设备向云端传输密集的RGB图像既耗能又昂贵，(ii) 基于patch的tokenization会使序列长度爆炸，给注意力机制和上下文限制带来压力。我们探索使用2D高斯溅射(2DGS)作为视觉对齐的替代基底：一种紧凑的、空间自适应的表示，通过一组彩色各向异性高斯函数来参数化图像。我们开发了一个可扩展的2DGS流程，具有结构化初始化、亮度感知剪枝和批处理CUDA内核，与之前的实现相比，实现了超过90倍的拟合速度提升和约97%的GPU利用率。我们进一步通过重用一个冻结的基于RGB的Transformer骨干网络，以及一个轻量级的splat感知输入stem和一个perceiver resampler，将对比语言图像预训练(CLIP)适配到2DGS，仅训练约7%的总参数。在大型DataComp子集上，GS编码器在相对于像素压缩3到20倍输入的同时，产生了有意义的零样本ImageNet-1K性能。虽然准确率目前落后于RGB编码器，但我们的结果确立了2DGS作为一种可行的多模态基底，指出了架构瓶颈，并为语义强大且传输高效的边缘云学习表示开辟了一条道路。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型依赖于RGB图像，这导致了两个主要问题：一是将密集的RGB图像从边缘设备传输到云端需要大量的能量和成本；二是基于patch的tokenization方法会显著增加序列长度，给模型的计算资源带来压力。因此，需要一种更紧凑、更高效的图像表示方法，以降低传输成本和计算复杂度。

**核心思路**：论文的核心思路是使用2D高斯溅射(2DGS)来表示图像。2DGS是一种基于一组彩色各向异性高斯函数的图像参数化方法，它能够以紧凑且空间自适应的方式表示图像。通过将图像表示为一组高斯函数，可以显著减少需要传输和处理的数据量，从而降低传输成本和计算复杂度。

**技术框架**：该论文提出的技术框架主要包含以下几个阶段：1) 2DGS pipeline：包括结构化初始化、亮度感知剪枝和批处理CUDA内核，用于高效地拟合2DGS表示。2) CLIP适配：重用冻结的RGB-based Transformer骨干网络，并添加一个轻量级的splat感知输入stem和一个perceiver resampler，将CLIP模型适配到2DGS表示。3) 训练：仅训练splat感知输入stem和perceiver resampler，保持Transformer骨干网络不变。

**关键创新**：该论文的关键创新点在于：1) 将2DGS引入视觉-语言对齐任务，探索了一种新的图像表示方法。2) 开发了一个高效的2DGS pipeline，显著提高了拟合速度和GPU利用率。3) 通过重用现有的RGB-based Transformer骨干网络，并添加轻量级的适配模块，实现了高效的CLIP模型迁移。与现有方法的本质区别在于，该方法不再依赖于像素级别的图像表示，而是使用一种更紧凑、更高效的高斯函数表示。

**关键设计**：在2DGS pipeline中，采用了结构化初始化方法，以加速高斯函数的收敛。亮度感知剪枝用于去除不重要的高斯函数，进一步压缩图像表示。批处理CUDA内核用于加速计算过程，提高GPU利用率。在CLIP适配中，splat感知输入stem用于将2DGS表示转换为Transformer可以处理的输入格式。Perceiver resampler用于将不同数量的高斯函数转换为固定长度的向量表示。

## 📊 实验亮点

实验结果表明，该方法在大型DataComp子集上，能够在相对于像素压缩3到20倍输入的同时，产生有意义的零样本ImageNet-1K性能。与之前的实现相比，该方法实现了超过90倍的拟合速度提升和约97%的GPU利用率。虽然准确率目前落后于RGB编码器，但该研究确立了2DGS作为一种可行的多模态基底。

## 🎯 应用场景

该研究成果可应用于边缘计算、移动设备视觉、云端图像处理等领域。通过使用2DGS压缩图像，可以降低数据传输带宽需求，减少计算资源消耗，从而实现更高效、更经济的视觉-语言应用。未来，该技术有望推动视觉-语言模型在资源受限环境下的部署和应用。

## 📄 摘要（原文）

> Modern vision language pipelines are driven by RGB vision encoders trained on massive image text corpora. While these pipelines have enabled impressive zero shot capabilities and strong transfer across tasks, they still inherit two structural inefficiencies from the pixel domain: (i) transmitting dense RGB images from edge devices to the cloud is energy intensive and costly, and (ii) patch based tokenization explodes sequence length, stressing attention budgets and context limits. We explore 2D Gaussian Splatting (2DGS) as an alternative visual substrate for alignment: a compact, spatially adaptive representation that parameterizes images by a set of colored anisotropic Gaussians. We develop a scalable 2DGS pipeline with structured initialization, luminance aware pruning, and batched CUDA kernels, achieving over 90x faster fitting and about 97% GPU utilization compared to prior implementations. We further adapt contrastive language image pretraining (CLIP) to 2DGS by reusing a frozen RGB-based transformer backbone with a lightweight splat aware input stem and a perceiver resampler, training only about 7% of the total parameters. On large DataComp subsets, GS encoders yield meaningful zero shot ImageNet-1K performance while compressing inputs 3 to 20x relative to pixels. While accuracy currently trails RGB encoders, our results establish 2DGS as a viable multimodal substrate, pinpoint architectural bottlenecks, and open a path toward representations that are both semantically powerful and transmission efficient for edge cloud learning.

