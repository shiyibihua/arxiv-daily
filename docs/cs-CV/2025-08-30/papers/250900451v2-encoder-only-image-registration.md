---
layout: default
title: Encoder-Only Image Registration
---

# Encoder-Only Image Registration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00451" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00451v2</a>
  <a href="https://arxiv.org/pdf/2509.00451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00451v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00451v2', 'Encoder-Only Image Registration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiang Chen, Renjiu Hu, Jinwei Zhang, Yuxi Zhang, Xinyao Yue, Min Liu, Yaonan Wang, Hang Zhang

**分类**: cs.CV

**发布日期**: 2025-08-30 (更新: 2025-09-04)

**🔗 代码/项目**: [GITHUB](https://github.com/XiangChen1994/EOIR)

---

## 💡 一句话要点

**提出Encoder-Only图像配准框架以解决计算复杂性与大变形问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `图像配准` `卷积神经网络` `特征提取` `流估计` `大变形` `医学图像处理` `计算机视觉`

## 📋 核心要点

1. 现有的可变形图像配准方法在处理大变形时计算复杂性较高，且难以平衡准确性与效率。
2. 本文提出的EOIR框架通过分离特征学习与流估计，利用简单的3层ConvNet和流估计器来优化配准过程。
3. 在五个不同模态和解剖区域的数据集上，EOIR展示了在准确性与效率之间的优越平衡，显著提升了配准效果。

## 📝 摘要（中文）

基于学习的技术显著提高了可变形图像配准的准确性和速度，但在降低计算复杂性和处理大变形方面仍面临挑战。为此，本文分析了卷积神经网络（ConvNets）如何影响配准性能，并提出了Encoder-Only图像配准（EOIR）框架。EOIR通过将特征学习与流估计分离，采用3层ConvNet进行特征提取，并利用一组3层流估计器构建拉普拉斯特征金字塔，逐步组合大变形模型下的微分变形。实验结果表明，EOIR在不同模态和解剖区域的五个数据集上表现出优越的准确性-效率和准确性-平滑性权衡。

## 🔬 方法详解

**问题定义**：本文旨在解决现有可变形图像配准方法在处理大变形时的计算复杂性和准确性之间的矛盾。现有方法往往难以在效率和效果之间取得良好平衡。

**核心思路**：EOIR框架的核心思想是将特征学习与流估计分开，通过使用简单的3层卷积神经网络进行特征提取，进而利用流估计器构建拉普拉斯特征金字塔，以实现更高效的配准。

**技术框架**：EOIR框架包括两个主要模块：特征提取模块和流估计模块。特征提取模块使用3层ConvNet提取图像特征，而流估计模块则使用一组3层流估计器来处理特征，逐步构建出微分变形。

**关键创新**：EOIR的创新之处在于其将特征学习与流估计分离的设计，使得在处理大变形时能够更有效地进行配准，与传统方法相比，显著降低了计算复杂性。

**关键设计**：在设计中，使用了3层的卷积神经网络和流估计器，构建了拉普拉斯特征金字塔，并在损失函数中考虑了准确性与平滑性之间的权衡。

## 📊 实验亮点

在五个不同模态和解剖区域的数据集上，EOIR框架实现了优于现有方法的准确性-效率和准确性-平滑性权衡，具体表现为在保持相似准确性的同时，显著提高了处理效率和配准平滑性。

## 🎯 应用场景

该研究的潜在应用领域包括医学图像处理、遥感图像分析以及计算机视觉中的图像配准任务。EOIR框架的高效性和准确性使其在需要快速处理和高精度配准的场景中具有实际价值，未来可能推动相关领域的技术进步。

## 📄 摘要（原文）

> Learning-based techniques have significantly improved the accuracy and speed of deformable image registration. However, challenges such as reducing computational complexity and handling large deformations persist. To address these challenges, we analyze how convolutional neural networks (ConvNets) influence registration performance using the Horn-Schunck optical flow equation. Supported by prior studies and our empirical experiments, we observe that ConvNets play two key roles in registration: linearizing local intensities and harmonizing global contrast variations. Based on these insights, we propose the Encoder-Only Image Registration (EOIR) framework, designed to achieve a better accuracy-efficiency trade-off. EOIR separates feature learning from flow estimation, employing only a 3-layer ConvNet for feature extraction and a set of 3-layer flow estimators to construct a Laplacian feature pyramid, progressively composing diffeomorphic deformations under a large-deformation model. Results on five datasets across different modalities and anatomical regions demonstrate EOIR's effectiveness, achieving superior accuracy-efficiency and accuracy-smoothness trade-offs. With comparable accuracy, EOIR provides better efficiency and smoothness, and vice versa. The source code of EOIR is publicly available on https://github.com/XiangChen1994/EOIR.

