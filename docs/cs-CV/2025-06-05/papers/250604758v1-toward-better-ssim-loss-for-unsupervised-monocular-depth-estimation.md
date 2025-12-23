---
layout: default
title: Toward Better SSIM Loss for Unsupervised Monocular Depth Estimation
---

# Toward Better SSIM Loss for Unsupervised Monocular Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04758" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04758v1</a>
  <a href="https://arxiv.org/pdf/2506.04758.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04758v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04758v1', 'Toward Better SSIM Loss for Unsupervised Monocular Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yijun Cao, Fuya Luo, Yongjie Li

**分类**: cs.CV

**发布日期**: 2025-06-05

**备注**: 12 pages,4 figures

**期刊**: International Conference on Image and Graphics. Cham: Springer Nature Switzerland, 2023: 81-92

**DOI**: [10.1007/978-3-031-46305-1_7](https://doi.org/10.1007/978-3-031-46305-1_7)

---

## 💡 一句话要点

**提出新型SSIM损失函数以改善无监督单目深度估计**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无监督学习` `单目深度估计` `结构相似性` `损失函数优化` `计算机视觉`

## 📋 核心要点

1. 现有方法在无监督单目深度估计中，未充分考虑SSIM函数不同组件及超参数的影响，导致训练效果不佳。
2. 本文提出了一种新型SSIM损失函数，通过加法组合亮度、对比度和结构相似性组件，旨在改善训练过程中的梯度平滑性。
3. 实验结果表明，优化后的SSIM损失函数在KITTI-2015数据集上显著提升了深度估计的性能，超越了传统方法。

## 📝 摘要（中文）

无监督单目深度学习通常依赖于时间上相邻图像之间的光度关系。以往的研究多采用均值绝对误差（MAE）和传统形式的结构相似性指数（SSIM）作为训练损失，但忽略了SSIM函数中不同组件及其超参数对训练的影响。为解决这些问题，本文提出了一种新的SSIM形式。与原始SSIM函数相比，新的形式采用加法而非乘法来组合与亮度、对比度和结构相似性相关的组件。基于这一方案构建的损失函数有助于产生更平滑的梯度，并在无监督深度估计中实现更高的性能。通过大量实验，我们确定了新SSIM的相对最佳参数组合，优化后的SSIM损失函数在KITTI-2015户外数据集上显著超越了基线。

## 🔬 方法详解

**问题定义**：本文旨在解决无监督单目深度估计中，传统SSIM损失函数未能有效利用其各组件及超参数的问题，导致训练效果不理想。

**核心思路**：提出一种新型SSIM损失函数，通过加法而非乘法的方式组合亮度、对比度和结构相似性组件，以期提高训练过程中的梯度平滑性和深度估计性能。

**技术框架**：整体架构基于MonoDepth方法，主要包括图像对的光度一致性计算、SSIM损失函数的优化以及深度图的生成。

**关键创新**：最重要的创新在于提出了一种新的SSIM形式，改变了传统的乘法组合方式，使得损失函数在训练过程中表现出更好的平滑性和收敛性。

**关键设计**：在损失函数设计中，优化了SSIM的各个组件的权重和超参数设置，通过大量实验确定了最佳组合，以提升无监督深度估计的性能。

## 📊 实验亮点

实验结果显示，优化后的SSIM损失函数在KITTI-2015户外数据集上，相较于传统方法，深度估计的性能提升显著，具体表现为在多个评估指标上均超越了基线，验证了新方法的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括自动驾驶、机器人导航和增强现实等领域，能够为这些应用提供更准确的深度信息，提升系统的智能化水平。未来，优化后的SSIM损失函数可能会被广泛应用于其他计算机视觉任务中，推动无监督学习方法的发展。

## 📄 摘要（原文）

> Unsupervised monocular depth learning generally relies on the photometric relation among temporally adjacent images. Most of previous works use both mean absolute error (MAE) and structure similarity index measure (SSIM) with conventional form as training loss. However, they ignore the effect of different components in the SSIM function and the corresponding hyperparameters on the training. To address these issues, this work proposes a new form of SSIM. Compared with original SSIM function, the proposed new form uses addition rather than multiplication to combine the luminance, contrast, and structural similarity related components in SSIM. The loss function constructed with this scheme helps result in smoother gradients and achieve higher performance on unsupervised depth estimation. We conduct extensive experiments to determine the relatively optimal combination of parameters for our new SSIM. Based on the popular MonoDepth approach, the optimized SSIM loss function can remarkably outperform the baseline on the KITTI-2015 outdoor dataset.

