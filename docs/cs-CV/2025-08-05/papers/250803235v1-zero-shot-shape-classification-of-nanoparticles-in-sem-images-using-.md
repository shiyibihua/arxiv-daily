---
layout: default
title: Zero-shot Shape Classification of Nanoparticles in SEM Images using Vision Foundation Models
---

# Zero-shot Shape Classification of Nanoparticles in SEM Images using Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03235" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03235v1</a>
  <a href="https://arxiv.org/pdf/2508.03235.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03235v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03235v1', 'Zero-shot Shape Classification of Nanoparticles in SEM Images using Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Freida Barnatan, Emunah Goldstein, Einav Kalimian, Orchen Madar, Avi Huri, David Zitoun, Ya'akov Mandelbaum, Moshe Amitay

**分类**: cs.CV

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出零-shot分类方法以解决纳米颗粒形态识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `纳米颗粒` `形态分类` `扫描电子显微镜` `零-shot学习` `基础视觉模型` `自动化分析` `深度学习`

## 📋 核心要点

1. 现有深度学习方法在纳米颗粒形态分类中依赖大量标注数据和高计算成本，限制了其应用。
2. 本研究提出一种零-shot分类流程，结合SAM和DINOv2模型，实现高效的形状分类。
3. 实验结果显示，该方法在多个数据集上优于微调的YOLOv11和ChatGPT o4-mini-high基线，具有更好的鲁棒性。

## 📝 摘要（中文）

在扫描电子显微镜（SEM）图像中，准确高效地表征纳米颗粒形态对于确保纳米材料合成的产品质量至关重要。然而，传统深度学习方法在形状分类中需要大量标注数据和计算资源，限制了其在研究和工业中的应用。本研究提出了一种零-shot分类流程，利用Segment Anything Model（SAM）进行对象分割和DINOv2进行特征嵌入。通过将这些模型与轻量级分类器结合，我们在三个形态各异的纳米颗粒数据集上实现了高精度的形状分类，而无需大量参数微调。我们的方案在小数据集、细微形态变化和从自然到科学成像的领域转移中表现出色，展示了基础模型在自动显微镜图像分析中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决纳米颗粒在扫描电子显微镜图像中的形态分类问题。现有方法需要大量标注数据和高计算资源，导致其在实际应用中的局限性。

**核心思路**：本研究提出的零-shot分类方法利用了两个基础视觉模型，分别是Segment Anything Model（SAM）用于对象分割和DINOv2用于特征嵌入，结合轻量级分类器以实现高效分类。

**技术框架**：整体流程包括三个主要模块：首先使用SAM进行图像中的对象分割，然后通过DINOv2提取特征，最后利用轻量级分类器进行形状分类。该流程避免了复杂的参数微调。

**关键创新**：本研究的主要创新在于将基础视觉模型应用于零-shot分类任务，显著降低了对标注数据的依赖，同时提高了分类精度。与传统深度学习方法相比，该方法更为高效和易于使用。

**关键设计**：在模型设计中，SAM和DINOv2的结合使得特征提取和分类过程更加流畅，轻量级分类器的使用则确保了计算效率。具体的参数设置和损失函数设计在论文中进行了详细讨论。

## 📊 实验亮点

实验结果表明，所提出的方法在三个不同的纳米颗粒数据集上实现了高精度的形状分类，超越了微调的YOLOv11和ChatGPT o4-mini-high基线，展示了在小数据集和细微形态变化下的鲁棒性，具体提升幅度未明确给出。

## 🎯 应用场景

该研究的潜在应用领域包括纳米材料的质量控制、材料科学研究以及自动化显微镜图像分析。通过提高形态分类的效率和准确性，该方法能够加速纳米材料的开发和应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Accurate and efficient characterization of nanoparticle morphology in Scanning Electron Microscopy (SEM) images is critical for ensuring product quality in nanomaterial synthesis and accelerating development. However, conventional deep learning methods for shape classification require extensive labeled datasets and computationally demanding training, limiting their accessibility to the typical nanoparticle practitioner in research and industrial settings. In this study, we introduce a zero-shot classification pipeline that leverages two vision foundation models: the Segment Anything Model (SAM) for object segmentation and DINOv2 for feature embedding. By combining these models with a lightweight classifier, we achieve high-precision shape classification across three morphologically diverse nanoparticle datasets - without the need for extensive parameter fine-tuning. Our methodology outperforms a fine-tuned YOLOv11 and ChatGPT o4-mini-high baselines, demonstrating robustness to small datasets, subtle morphological variations, and domain shifts from natural to scientific imaging. Quantitative clustering metrics on PCA plots of the DINOv2 features are discussed as a means of assessing the progress of the chemical synthesis. This work highlights the potential of foundation models to advance automated microscopy image analysis, offering an alternative to traditional deep learning pipelines in nanoparticle research which is both more efficient and more accessible to the user.

