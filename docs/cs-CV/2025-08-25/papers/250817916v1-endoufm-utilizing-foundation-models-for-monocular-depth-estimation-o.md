---
layout: default
title: EndoUFM: Utilizing Foundation Models for Monocular depth estimation of endoscopic images
---

# EndoUFM: Utilizing Foundation Models for Monocular depth estimation of endoscopic images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17916" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17916v1</a>
  <a href="https://arxiv.org/pdf/2508.17916.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17916v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17916v1', 'EndoUFM: Utilizing Foundation Models for Monocular depth estimation of endoscopic images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinning Yao, Bo Liu, Bojian Li, Jingjing Wang, Jinghua Yue, Fugen Zhou

**分类**: cs.CV

**发布日期**: 2025-08-25

**备注**: 12 pages

---

## 💡 一句话要点

**提出EndoUFM以解决内窥镜图像单目深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `单目深度估计` `内窥镜图像` `基础模型` `微创手术` `深度学习` `自适应微调` `平滑损失`

## 📋 核心要点

1. 现有的单目深度估计方法在复杂的手术环境中受限于光照变化和纹理复杂性，导致性能不足。
2. 论文提出EndoUFM框架，通过整合双重基础模型和自适应微调策略，提升内窥镜图像的深度估计能力。
3. 在SCARED、Hamlyn、SERV-CT和EndoNeRF数据集上的实验结果显示，该方法在性能上达到了最先进水平，且模型规模高效。

## 📝 摘要（中文）

深度估计是微创内窥镜手术中3D重建的基础组成部分。然而，现有的单目深度估计技术在手术环境中由于光照变化和复杂纹理的影响，表现出有限的性能。尽管强大的视觉基础模型提供了有希望的解决方案，但其在自然图像上的训练导致在内窥镜应用中存在显著的领域适应性限制和语义感知不足。本研究提出了EndoUFM，一个无监督的单目深度估计框架，创新性地整合了双重基础模型以增强手术场景的深度估计性能。该框架采用了随机向量低秩适应（RVLoRA）的自适应微调策略，并基于深度可分离卷积的残差块（Res-DSC）来改善细粒度局部特征的捕捉。此外，我们设计了一种掩膜引导的平滑损失，以增强解剖组织结构内的深度一致性。大量实验表明，我们的方法在多个数据集上实现了最先进的性能，同时保持了高效的模型规模。

## 🔬 方法详解

**问题定义**：本研究旨在解决内窥镜图像的单目深度估计问题。现有方法在复杂的手术环境中表现不佳，主要由于光照变化和纹理复杂性导致的性能限制。

**核心思路**：EndoUFM框架通过整合双重基础模型，利用预学习的先验知识来增强深度估计性能，同时采用自适应微调策略以提高模型的适应性。

**技术框架**：该框架包括两个主要模块：首先是基于双重基础模型的深度估计模块，其次是采用随机向量低秩适应（RVLoRA）进行自适应微调的模块。此外，设计了掩膜引导的平滑损失以确保深度一致性。

**关键创新**：最重要的创新点在于将双重基础模型与自适应微调策略相结合，显著提高了模型在复杂手术场景中的适应性和深度估计精度。

**关键设计**：采用了基于深度可分离卷积的残差块（Res-DSC）来捕捉细粒度局部特征，并设计了掩膜引导的平滑损失函数，以增强解剖结构内的深度一致性。

## 📊 实验亮点

在SCARED、Hamlyn、SERV-CT和EndoNeRF数据集上的实验结果表明，EndoUFM方法在深度估计性能上达到了最先进水平，相较于基线方法有显著提升，具体性能数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括微创手术中的深度感知、增强现实和导航系统。通过提高外科医生在手术过程中的空间感知能力，EndoUFM有助于提升手术的精确性和安全性，具有重要的临床价值和未来影响。

## 📄 摘要（原文）

> Depth estimation is a foundational component for 3D reconstruction in minimally invasive endoscopic surgeries. However, existing monocular depth estimation techniques often exhibit limited performance to the varying illumination and complex textures of the surgical environment. While powerful visual foundation models offer a promising solution, their training on natural images leads to significant domain adaptability limitations and semantic perception deficiencies when applied to endoscopy. In this study, we introduce EndoUFM, an unsupervised monocular depth estimation framework that innovatively integrating dual foundation models for surgical scenes, which enhance the depth estimation performance by leveraging the powerful pre-learned priors. The framework features a novel adaptive fine-tuning strategy that incorporates Random Vector Low-Rank Adaptation (RVLoRA) to enhance model adaptability, and a Residual block based on Depthwise Separable Convolution (Res-DSC) to improve the capture of fine-grained local features. Furthermore, we design a mask-guided smoothness loss to enforce depth consistency within anatomical tissue structures. Extensive experiments on the SCARED, Hamlyn, SERV-CT, and EndoNeRF datasets confirm that our method achieves state-of-the-art performance while maintaining an efficient model size. This work contributes to augmenting surgeons' spatial perception during minimally invasive procedures, thereby enhancing surgical precision and safety, with crucial implications for augmented reality and navigation systems.

