---
layout: default
title: ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
---

# ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14099" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14099v1</a>
  <a href="https://arxiv.org/pdf/2512.14099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14099v1" onclick="toggleFavorite(this, '2512.14099v1', 'ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruishu Zhu, Zhihao Huang, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ViewMask-1-to-3：基于多模态扩散模型实现多视角一致的图像生成**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视角图像生成` `离散扩散模型` `跨视角一致性` `MAGVIT-v2` `Transformer模型`

## 📋 核心要点

1. 多视角图像生成面临跨视角几何一致性难题，现有方法依赖3D感知架构或专用扩散模型，需要大量多视角训练数据和复杂的几何先验。
2. ViewMask-1-to-3将多视角合成建模为离散序列预测，利用MAGVIT-v2将视角表示为视觉token，通过掩码token预测统一语言和视觉信息。
3. 该方法通过随机掩码和自注意力实现跨视角一致性，无需复杂几何约束，在GSO和3D-FUTURE数据集上取得了领先的性能。

## 📝 摘要（中文）

本文提出ViewMask-1-to-3，一种利用离散扩散模型进行多视角图像生成的新方法。与在潜在空间中操作的连续扩散方法不同，ViewMask-1-to-3将多视角合成问题建模为离散序列建模问题，其中每个视角表示为通过MAGVIT-v2分词获得的视觉token。通过基于掩码token预测统一语言和视觉，该方法能够通过迭代token解掩码和文本输入逐步生成多个视角。ViewMask-1-to-3通过简单的随机掩码和自注意力实现跨视角一致性，无需复杂的3D几何约束或专门的注意力架构。实验结果表明，离散扩散为现有的多视角生成方法提供了一种可行且简单的替代方案，在GSO和3D-FUTURE数据集上，ViewMask-1-to-3在PSNR、SSIM和LPIPS指标上平均排名第一，同时保持了架构的简洁性。

## 🔬 方法详解

**问题定义**：多视角图像生成旨在从单个图像和文本描述生成多个视角的图像，关键挑战在于保持不同视角之间的几何一致性。现有方法通常依赖于3D感知架构或专门设计的扩散模型，这些方法需要大量的多视角训练数据以及复杂的几何先验知识，限制了其应用范围和灵活性。

**核心思路**：ViewMask-1-to-3的核心思路是将多视角图像生成问题转化为一个离散序列建模问题。通过将每个视角表示为离散的视觉token，并利用掩码token预测的方式，模型可以学习到不同视角之间的关系，从而生成具有一致性的多视角图像。这种方法避免了对复杂3D几何信息的依赖，简化了模型的设计和训练过程。

**技术框架**：ViewMask-1-to-3的整体框架包括以下几个主要步骤：1) 使用MAGVIT-v2将输入图像和文本描述转换为视觉token和文本token；2) 对视觉token进行随机掩码；3) 使用Transformer模型进行token预测，逐步解掩码，生成新的视角；4) 将生成的token解码为图像。整个过程通过迭代进行，逐步完善多视角图像的生成。

**关键创新**：ViewMask-1-to-3的关键创新在于将离散扩散模型应用于多视角图像生成。与传统的连续扩散模型不同，离散扩散模型直接在token空间进行操作，避免了对潜在空间的复杂推理。此外，该方法通过简单的随机掩码和自注意力机制实现了跨视角一致性，无需复杂的3D几何约束或专门的注意力架构。

**关键设计**：ViewMask-1-to-3的关键设计包括：1) 使用MAGVIT-v2进行token化，将图像和文本转换为统一的token表示；2) 采用随机掩码策略，迫使模型学习不同视角之间的关系；3) 使用Transformer模型进行token预测，利用自注意力机制实现跨视角信息交互；4) 通过迭代解掩码的方式逐步生成多视角图像。

## 📊 实验亮点

ViewMask-1-to-3在GSO和3D-FUTURE数据集上取得了显著的性能提升，在PSNR、SSIM和LPIPS指标上平均排名第一。该方法在保持架构简洁性的同时，实现了优于现有方法的性能，证明了离散扩散模型在多视角图像生成方面的有效性。

## 🎯 应用场景

ViewMask-1-to-3在3D内容生成、虚拟现实、增强现实、游戏开发等领域具有广泛的应用前景。它可以用于从单张图像生成3D模型，创建沉浸式虚拟体验，以及辅助游戏场景的设计和开发。该研究的成果有助于降低多视角内容生成的门槛，促进相关技术的发展和应用。

## 📄 摘要（原文）

> Multi-view image generation from a single image and text description remains challenging due to the difficulty of maintaining geometric consistency across different viewpoints. Existing approaches typically rely on 3D-aware architectures or specialized diffusion models that require extensive multi-view training data and complex geometric priors. In this work, we introduce ViewMask-1-to-3, a pioneering approach to apply discrete diffusion models to multi-view image generation. Unlike continuous diffusion methods that operate in latent spaces, ViewMask-1-to-3 formulates multi-view synthesis as a discrete sequence modeling problem, where each viewpoint is represented as visual tokens obtained through MAGVIT-v2 tokenization. By unifying language and vision through masked token prediction, our approach enables progressive generation of multiple viewpoints through iterative token unmasking with text input. ViewMask-1-to-3 achieves cross-view consistency through simple random masking combined with self-attention, eliminating the requirement for complex 3D geometric constraints or specialized attention architectures. Our approach demonstrates that discrete diffusion provides a viable and simple alternative to existing multi-view generation methods, ranking first on average across GSO and 3D-FUTURE datasets in terms of PSNR, SSIM, and LPIPS, while maintaining architectural simplicity.

