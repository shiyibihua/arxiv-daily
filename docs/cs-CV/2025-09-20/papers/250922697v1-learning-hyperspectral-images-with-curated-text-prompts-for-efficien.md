---
layout: default
title: Learning Hyperspectral Images with Curated Text Prompts for Efficient Multimodal Alignment
---

# Learning Hyperspectral Images with Curated Text Prompts for Efficient Multimodal Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22697" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22697v1</a>
  <a href="https://arxiv.org/pdf/2509.22697.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22697v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22697v1', 'Learning Hyperspectral Images with Curated Text Prompts for Efficient Multimodal Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abhiroop Chatterjee, Susmita Ghosh

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-09-20

**备注**: Accepted at the IEEE/CVF International Conference on Computer Vision (ICCV 2025), Workshop on Curated Data for Efficient Learning

---

## 💡 一句话要点

**利用文本提示学习高光谱图像，实现高效多模态对齐**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高光谱图像` `多模态对齐` `对比学习` `文本提示` `视觉-语言模型`

## 📋 核心要点

1. 高光谱图像处理面临高维数据带来的挑战，现有视觉-语言模型在高光谱领域的跨模态对齐效果不佳。
2. 提出一种基于CLIP风格对比学习的框架，利用文本提示作为锚点，优化视觉-语言模型，实现高效的多模态对齐。
3. 实验表明，该方法仅需更新少量参数即可达到SOTA性能，并在Indian Pines和Pavia University数据集上取得显著提升。

## 📝 摘要（中文）

随着数据需求的持续增长，高效学习越来越依赖于高质量数据的管理和提炼，而不是粗暴地扩大模型规模。对于高光谱图像（HSI）而言，由于其高维3D体素结构（每个空间位置与数百个连续光谱通道相关联），挑战更加严峻。虽然视觉和语言模型已针对自然图像或文本任务进行了有效优化，但它们在高光谱领域中的跨模态对齐仍然是一个未被充分探索的问题。本文尝试通过利用CLIP风格的对比训练框架来优化用于高光谱场景理解的视觉-语言模型（VLM）。该框架将来自视觉主干网络的体素级嵌入映射到冻结的大型嵌入模型（LEM）的潜在空间，其中可训练的探针将视觉特征与模型的文本token表示对齐。两种模态通过对比损失对齐，该对比损失仅限于精心挑选的难负样本（最接近的错误类别）和半难负样本（随机干扰项）以及正样本对。为了进一步增强对齐，引入了编码类别语义的描述性提示，并作为HSI嵌入的结构化锚点。结果表明，该方法仅更新总参数的0.07%，但产生了最先进的性能。例如，在Indian Pines（IP）数据集上，该模型比单模态和多模态基线提高了+0.92的总体精度（OA）和+1.60的Kappa（κ），而在Pavia University（PU）数据集上，它提供了+0.69的OA和+0.90的κ增益。此外，这是在参数集比DCTN小近50倍，比SS-TMNet小90倍的情况下实现的。

## 🔬 方法详解

**问题定义**：论文旨在解决高光谱图像场景理解中视觉-语言模型跨模态对齐的问题。现有方法通常需要大量的参数和计算资源，且在高光谱图像这种高维数据上的表现不佳。痛点在于如何高效地将高光谱图像的视觉特征与文本描述对齐，并利用有限的计算资源达到良好的性能。

**核心思路**：论文的核心思路是利用对比学习框架，将高光谱图像的视觉特征映射到预训练的大型语言模型的潜在空间中，并通过文本提示作为锚点来引导视觉特征的学习。通过这种方式，可以利用大型语言模型的先验知识，并减少对大量标注数据的依赖。

**技术框架**：整体框架包含以下几个主要模块：1) 视觉主干网络：用于提取高光谱图像的体素级嵌入。2) 大型嵌入模型（LEM）：一个预训练的、参数冻结的语言模型，用于生成文本嵌入。3) 可训练探针：用于将视觉特征映射到LEM的潜在空间。4) 对比损失函数：用于对齐视觉和文本嵌入。5) 文本提示：用于编码类别语义，作为结构化锚点。

**关键创新**：最重要的技术创新点在于利用文本提示作为锚点来引导视觉特征的学习。这种方法可以有效地利用大型语言模型的先验知识，并减少对大量标注数据的依赖。此外，该方法仅需更新少量参数，即可达到SOTA性能，具有很高的计算效率。

**关键设计**：关键设计包括：1) 使用CLIP风格的对比损失函数，并选择难负样本和半难负样本进行训练。2) 设计描述性的文本提示，用于编码类别语义。3) 使用可训练的探针将视觉特征映射到LEM的潜在空间。4) 冻结大型语言模型的参数，只更新少量参数，以提高计算效率。

## 📊 实验亮点

实验结果表明，该方法在Indian Pines数据集上，总体精度（OA）提升了+0.92，Kappa系数提升了+1.60；在Pavia University数据集上，OA提升了+0.69，Kappa系数提升了+0.90。该方法仅更新总参数的0.07%，参数量远小于DCTN和SS-TMNet，但性能优于单模态和多模态基线。

## 🎯 应用场景

该研究成果可应用于遥感图像分析、精准农业、环境监测等领域。通过高效的多模态对齐，可以更准确地理解高光谱图像中的场景信息，从而为相关领域的决策提供支持。未来，该方法有望推广到其他高维数据和跨模态学习任务中。

## 📄 摘要（原文）

> As data requirements continue to grow, efficient learning increasingly depends on the curation and distillation of high-value data rather than brute-force scaling of model sizes. In the case of a hyperspectral image (HSI), the challenge is amplified by the high-dimensional 3D voxel structure, where each spatial location is associated with hundreds of contiguous spectral channels. While vision and language models have been optimized effectively for natural image or text tasks, their cross-modal alignment in the hyperspectral domain remains an open and underexplored problem. In this article, we make an attempt to optimize a Vision-Language Model (VLM) for hyperspectral scene understanding by exploiting a CLIP-style contrastive training framework. Our framework maps voxel-level embeddings from a vision backbone onto the latent space of a frozen large embedding model (LEM), where a trainable probe aligns vision features with the model's textual token representations. The two modalities are aligned via a contrastive loss restricted to a curated set of hard (closest wrong classes) and semi-hard (random distractors) negatives, along with positive pairs. To further enhance alignment, descriptive prompts that encode class semantics are introduced and act as structured anchors for the HSI embeddings. It is seen that the proposed method updates only 0.07 percent of the total parameters, yet yields state-of-the-art performance. For example, on Indian Pines (IP) the model produces better results over unimodal and multimodal baselines by +0.92 Overall Accuracy (OA) and +1.60 Kappa ($κ$), while on Pavia University (PU) data it provides gains of +0.69 OA and +0.90 $κ$. Moreover, this is achieved with the set of parameters, nearly 50$\times$ smaller than DCTN and 90$\times$ smaller than SS-TMNet.

