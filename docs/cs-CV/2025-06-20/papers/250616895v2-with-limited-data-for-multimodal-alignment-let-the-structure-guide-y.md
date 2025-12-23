---
layout: default
title: With Limited Data for Multimodal Alignment, Let the STRUCTURE Guide You
---

# With Limited Data for Multimodal Alignment, Let the STRUCTURE Guide You

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16895" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16895v2</a>
  <a href="https://arxiv.org/pdf/2506.16895.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16895v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16895v2', 'With Limited Data for Multimodal Alignment, Let the STRUCTURE Guide You')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fabian Gröger, Shuo Wen, Huyen Le, Maria Brbić

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-06-20 (更新: 2025-10-22)

**备注**: NeurIPS 2025 camera-ready

---

## 💡 一句话要点

**提出STRUCTURE以解决多模态对齐中的数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态对齐` `有限样本学习` `STRUCTURE技术` `预训练模型` `几何结构保持`

## 📋 核心要点

1. 现有多模态模型通常需要大量配对样本，获取成本高昂，限制了其在资源受限领域的应用。
2. 本文提出STRUCTURE正则化技术，通过保持单模态编码器的邻域几何结构，实现有限样本下的高效对齐。
3. 实验结果表明，使用该方法在零样本分类和检索任务上分别提升了51.6%和91.8%的性能，显示出良好的应用前景。

## 📝 摘要（中文）

多模态模型在需要多模态对齐的复杂任务中展现出强大的能力，但现有模型通常依赖于数百万对的多模态样本，这在许多领域是不可行的。本文探讨了在有限配对数据下构建多模态模型的可行性，通过对预训练的单模态基础模型进行对齐，展示了在仅有数万对样本的情况下实现高质量对齐的可能性。我们引入了一种有效的正则化技术STRUCTURE，以保持单模态编码器潜在空间的邻域几何结构。此外，我们还表明对齐最后一层通常不是最优的，展示了对齐具有最高表示相似性的层的好处。我们的框架在24个零样本图像分类和检索基准上取得了显著提升，分类任务平均提升51.6%，检索任务平均提升91.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决在多模态对齐任务中，现有方法依赖于大量配对样本的问题，尤其是在数据稀缺的领域。现有方法通常需要数百万对样本，获取这些数据在许多应用场景中是不切实际的。

**核心思路**：论文提出通过对预训练的单模态基础模型进行对齐，利用STRUCTURE正则化技术来保持潜在空间的几何结构，从而在有限的配对数据下实现高质量的多模态对齐。

**技术框架**：整体架构包括两个主要模块：一是通过STRUCTURE技术进行单模态编码器的对齐，二是优化对齐层的选择，优先对齐表示相似性最高的层。

**关键创新**：最重要的创新点在于引入STRUCTURE正则化技术，能够有效地保持单模态编码器的邻域几何结构，并且通过对齐高相似性层而非最后一层，显著提升对齐效果。

**关键设计**：在参数设置上，STRUCTURE正则化的具体实现方式和损失函数的设计是关键，确保了对齐过程中的几何结构保持，同时在网络结构上，选择合适的层进行对齐以提高表示能力。

## 📊 实验亮点

实验结果显示，使用STRUCTURE技术后，在24个零样本图像分类和检索基准上，分类任务平均提升51.6%，检索任务平均提升91.8%。这些显著的性能提升表明该方法在多模态学习中的有效性和广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、自动驾驶、智能监控等需要多模态数据融合的场景。通过在数据稀缺的情况下实现有效的多模态学习，能够降低模型训练的成本，提高在资源受限环境下的应用价值，推动相关领域的技术进步。

## 📄 摘要（原文）

> Multimodal models have demonstrated powerful capabilities in complex tasks requiring multimodal alignment, including zero-shot classification and cross-modal retrieval. However, existing models typically rely on millions of paired multimodal samples, which are prohibitively expensive or infeasible to obtain in many domains. In this work, we explore the feasibility of building multimodal models with limited amount of paired data by aligning pretrained unimodal foundation models. We show that high-quality alignment is possible with as few as tens of thousands of paired samples$\unicode{x2013}$less than $1\%$ of the data typically used in the field. To achieve this, we introduce STRUCTURE, an effective regularization technique that preserves the neighborhood geometry of the latent space of unimodal encoders. Additionally, we show that aligning last layers is often suboptimal and demonstrate the benefits of aligning the layers with the highest representational similarity across modalities. These two components can be readily incorporated into existing alignment methods, yielding substantial gains across 24 zero-shot image classification and retrieval benchmarks, with average relative improvement of $51.6\%$ in classification and $91.8\%$ in retrieval tasks. Our results highlight the effectiveness and broad applicability of our framework for limited-sample multimodal learning and offer a promising path forward for resource-constrained domains.

