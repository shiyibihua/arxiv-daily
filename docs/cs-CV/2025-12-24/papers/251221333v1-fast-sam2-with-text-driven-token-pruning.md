---
layout: default
title: Fast SAM2 with Text-Driven Token Pruning
---

# Fast SAM2 with Text-Driven Token Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21333" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21333v1</a>
  <a href="https://arxiv.org/pdf/2512.21333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21333v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21333v1', 'Fast SAM2 with Text-Driven Token Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Avilasha Mandal, Chaoning Zhang, Fachrina Dewi Puspitasari, Xudong Wang, Jiaquan Zhang, Caiyan Qin, Guoqing Wang, Yang Yang, Heng Tao Shen

**分类**: cs.CV

**发布日期**: 2025-12-24

**备注**: 28 pages, 9 figures

---

## 💡 一句话要点

**提出基于文本驱动的token剪枝Fast SAM2，加速视频分割并降低资源消耗。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频分割` `token剪枝` `文本引导` `模型加速` `SAM2`

## 📋 核心要点

1. SAM2在视频分割中表现出色，但处理密集视觉token导致计算和内存成本高昂，限制了实际部署。
2. 该文提出文本引导的token剪枝框架，在时序传播前选择性减少token密度，提升推理效率。
3. 实验表明，该方法在保持分割精度的同时，显著提升推理速度并降低GPU内存使用。

## 📝 摘要（中文）

本文提出了一种基于文本引导的token剪枝框架，旨在提高Segment Anything Model 2 (SAM2) 在视频对象分割中的推理效率。该方法在视觉编码后、时序传播前选择性地减少token密度，无需修改底层分割架构。通过轻量级的路由机制，该方法融合局部视觉上下文、来自对象中心文本描述的语义相关性以及不确定性线索来评估token的重要性。仅保留信息量最大的token用于下游处理，从而减少冗余计算，同时保持分割精度。在多个具有挑战性的视频分割基准测试中，实验结果表明，与未剪枝的SAM2基线相比，所提出的方法实现了高达42.50%的推理速度提升和37.41%的GPU内存使用量降低，同时保持了具有竞争力的J和F性能。这突显了早期token选择在提高基于Transformer的视频分割系统在实时和资源受限应用中的可扩展性方面的潜力。

## 🔬 方法详解

**问题定义**：SAM2在视频分割任务中，需要处理大量的视觉tokens，导致计算和内存开销巨大，尤其是在处理长视频时，二次方级别的注意力机制使得资源消耗更加严重。现有的方法通常直接将所有视觉tokens传递到下游模块，而忽略了其中可能存在大量冗余信息，这限制了SAM2在资源受限设备上的应用。

**核心思路**：本文的核心思路是在视觉编码后，时序传播前，对视觉tokens进行剪枝，只保留对目标对象分割有用的tokens。通过引入文本信息，引导token选择，使得剪枝过程更加智能，能够在减少计算量的同时，保持分割精度。这种方法避免了对SAM2底层架构的修改，易于集成和部署。

**技术框架**：该方法主要包含三个阶段：视觉编码、token路由和时序传播。首先，使用SAM2的图像编码器提取视觉特征。然后，通过一个轻量级的路由机制对tokens进行排序，该机制融合了局部视觉上下文、文本语义相关性和不确定性线索。最后，只保留排名靠前的tokens进行时序传播和分割。文本信息可以是用户提供的，也可以是自动生成的。

**关键创新**：该方法最重要的创新点在于引入了文本信息来指导token剪枝。与传统的基于视觉特征的token选择方法相比，文本信息能够提供更高级别的语义指导，使得剪枝过程更加关注目标对象，从而在减少计算量的同时，更好地保持分割精度。此外，该方法还考虑了不确定性线索，保留了边界区域的tokens，进一步提升了分割的鲁棒性。

**关键设计**：token路由机制是该方法的核心。该机制使用一个轻量级的神经网络来预测每个token的重要性得分。输入包括局部视觉特征、文本嵌入和不确定性估计。局部视觉特征通过卷积操作提取，文本嵌入通过预训练的文本编码器获得，不确定性估计通过计算token特征的方差得到。损失函数采用交叉熵损失，目标是最大化保留的tokens与目标对象之间的IoU。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21333v1/tokens_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21333v1/miansam.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21333v1/architechture_1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，与未剪枝的SAM2基线相比，该方法在多个视频分割基准测试中实现了显著的性能提升。具体而言，推理速度提升了高达42.50%，GPU内存使用量降低了37.41%，同时保持了具有竞争力的J和F性能。这些结果表明，该方法是一种有效的视频分割加速方案。

## 🎯 应用场景

该研究成果可应用于实时视频监控、自动驾驶、机器人导航等领域。通过降低计算和内存需求，使得SAM2能够在资源受限的设备上运行，从而扩展了其应用范围。此外，该方法还可以用于视频编辑、内容创作等领域，提高视频处理的效率和质量。

## 📄 摘要（原文）

> Segment Anything Model 2 (SAM2), a vision foundation model has significantly advanced in prompt-driven video object segmentation, yet their practical deployment remains limited by the high computational and memory cost of processing dense visual tokens across time. The SAM2 pipelines typically propagate all visual tokens produced by the image encoder through downstream temporal reasoning modules, regardless of their relevance to the target object, resulting in reduced scalability due to quadratic memory attention overhead. In this work, we introduce a text-guided token pruning framework that improves inference efficiency by selectively reducing token density prior to temporal propagation, without modifying the underlying segmentation architecture. Operating after visual encoding and before memory based propagation, our method ranks tokens using a lightweight routing mechanism that integrates local visual context, semantic relevance derived from object-centric textual descriptions (either user-provided or automatically generated), and uncertainty cues that help preserve ambiguous or boundary critical regions. By retaining only the most informative tokens for downstream processing, the proposed approach reduces redundant computation while maintaining segmentation fidelity. Extensive experiments across multiple challenging video segmentation benchmarks demonstrate that post-encoder token pruning provides a practical and effective pathway to efficient, prompt-aware video segmentation, achieving up to 42.50 percent faster inference and 37.41 percent lower GPU memory usage compared to the unpruned baseline SAM2, while preserving competitive J and F performance. These results highlight the potential of early token selection to improve the scalability of transformer-based video segmentation systems for real-time and resource-constrained applications.

