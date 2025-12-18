---
layout: default
title: Aesthetic Image Captioning with Saliency Enhanced MLLMs
---

# Aesthetic Image Captioning with Saliency Enhanced MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04378" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04378v3</a>
  <a href="https://arxiv.org/pdf/2509.04378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04378v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04378v3', 'Aesthetic Image Captioning with Saliency Enhanced MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yilin Tao, Jiashui Huang, Huaze Xu, Ling Shao

**分类**: cs.CV

**发布日期**: 2025-09-04 (更新: 2025-09-09)

---

## 💡 一句话要点

**提出ASE-MLLM，通过显著性增强多模态大语言模型提升图像美学描述生成效果**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像美学描述生成` `多模态大语言模型` `美学显著性` `交叉注意力机制` `图像编码器`

## 📋 核心要点

1. 现有AIC方法依赖微调MLLM，缺乏对美学内容的针对性关注，导致生成描述不够准确。
2. ASE-MLLM通过引入图像美学显著性模块（IASM）和IAS-ViT编码器，显式地将美学显著性融入MLLM。
3. 实验结果表明，ASE-MLLM在主流AIC基准上显著优于传统方法和通用MLLM，达到SOTA性能。

## 📝 摘要（中文）

图像美学描述生成（AIC）旨在生成图像美学的文本描述，是计算美学领域的一个关键研究方向。近年来，预训练的多模态大语言模型（MLLM）发展迅速，显著推动了整合视觉和文本模态的图像美学研究。然而，现有的大多数图像美学研究主要集中在预测美学评分，在AIC中的应用有限。现有的利用MLLM的AIC工作主要依赖于微调方法，而没有专门调整MLLM以关注目标美学内容。为了解决这个限制，我们提出了美学显著性增强多模态大语言模型（ASE-MLLM），这是一个端到端框架，它显式地将美学显著性融入到MLLM中。在这个框架中，我们引入了图像美学显著性模块（IASM），它能够高效且有效地从图像中提取美学显著性特征。此外，我们设计了IAS-ViT作为MLLM的图像编码器，该模块通过交叉注意力机制将美学显著性特征与原始图像特征融合。据我们所知，ASE-MLLM是第一个将图像美学显著性集成到MLLM中，专门用于AIC任务的框架。大量的实验表明，我们的方法在当前主流的AIC基准测试中显著优于传统方法和通用MLLM，实现了最先进（SOTA）的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决图像美学描述生成（AIC）任务中，现有方法无法有效利用多模态大语言模型（MLLM）的潜力，生成准确且具有美学针对性的图像描述的问题。现有方法主要依赖于对通用MLLM进行微调，缺乏对图像美学显著性特征的关注，导致生成的描述不够精细和准确。

**核心思路**：论文的核心思路是通过显式地将图像的美学显著性信息融入到MLLM中，引导模型关注图像中与美学相关的关键区域，从而生成更准确、更具美学价值的描述。通过引入图像美学显著性模块（IASM）提取显著性特征，并设计IAS-ViT编码器将这些特征与原始图像特征融合，使得MLLM能够更好地理解图像的美学内涵。

**技术框架**：ASE-MLLM框架包含以下主要模块：1) 图像美学显著性模块（IASM）：用于提取图像的美学显著性特征。2) IAS-ViT编码器：将IASM提取的显著性特征与原始图像特征融合，作为MLLM的图像编码器。3) MLLM：利用融合后的图像特征生成图像的美学描述。整个框架采用端到端的方式进行训练。

**关键创新**：该论文的关键创新在于首次将图像美学显著性显式地融入到MLLM中，用于AIC任务。通过IASM和IAS-ViT的设计，使得MLLM能够更好地关注图像中的美学相关区域，从而生成更准确、更具美学价值的描述。与现有方法相比，ASE-MLLM不再仅仅依赖于对通用MLLM的微调，而是通过引入专门的美学显著性模块来提升模型的性能。

**关键设计**：IASM的具体实现细节未知，但其目标是提取图像的美学显著性特征。IAS-ViT编码器通过交叉注意力机制将IASM提取的显著性特征与原始图像特征融合。损失函数的设计细节未知，但应该包含对生成描述的准确性和美学价值的约束。具体的参数设置和网络结构细节在论文中可能有所描述，但此处未知。

## 📊 实验亮点

实验结果表明，ASE-MLLM在主流AIC基准测试中显著优于传统方法和通用MLLM，实现了最先进（SOTA）的性能。具体的性能数据和提升幅度在论文中应该有详细的描述，但此处未知。该结果验证了将图像美学显著性融入MLLM的有效性，为AIC领域的研究提供了新的思路。

## 🎯 应用场景

该研究成果可应用于智能相册管理、图像搜索引擎、社交媒体内容生成等领域。例如，可以根据用户上传的照片自动生成具有美学价值的描述，方便用户分享和交流。未来，该技术还可以应用于艺术创作、设计辅助等领域，为人类提供更智能、更便捷的美学体验。

## 📄 摘要（原文）

> Aesthetic Image Captioning (AIC) aims to generate textual descriptions of image aesthetics, becoming a key research direction in the field of computational aesthetics. In recent years, pretrained Multimodal Large Language Models (MLLMs) have advanced rapidly, leading to a significant increase in image aesthetics research that integrates both visual and textual modalities. However, most existing studies on image aesthetics primarily focus on predicting aesthetic ratings and have shown limited application in AIC. Existing AIC works leveraging MLLMs predominantly rely on fine-tuning methods without specifically adapting MLLMs to focus on target aesthetic content. To address this limitation, we propose the Aesthetic Saliency Enhanced Multimodal Large Language Model (ASE-MLLM), an end-to-end framework that explicitly incorporates aesthetic saliency into MLLMs. Within this framework, we introduce the Image Aesthetic Saliency Module (IASM), which efficiently and effectively extracts aesthetic saliency features from images. Additionally, we design IAS-ViT as the image encoder for MLLMs, this module fuses aesthetic saliency features with original image features via a cross-attention mechanism. To the best of our knowledge, ASE-MLLM is the first framework to integrate image aesthetic saliency into MLLMs specifically for AIC tasks. Extensive experiments demonstrated that our approach significantly outperformed traditional methods and generic MLLMs on current mainstream AIC benchmarks, achieving state-of-the-art (SOTA) performance.

