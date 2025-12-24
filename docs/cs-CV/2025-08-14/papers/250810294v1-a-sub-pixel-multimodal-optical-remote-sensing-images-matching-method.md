---
layout: default
title: A Sub-Pixel Multimodal Optical Remote Sensing Images Matching Method
---

# A Sub-Pixel Multimodal Optical Remote Sensing Images Matching Method

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10294" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10294v1</a>
  <a href="https://arxiv.org/pdf/2508.10294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10294v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10294v1', 'A Sub-Pixel Multimodal Optical Remote Sensing Images Matching Method')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Huang, Hongbo Pan, Nanxi Zhou, Shun Zhou

**分类**: cs.CV

**发布日期**: 2025-08-14

**🔗 代码/项目**: [GITHUB](https://github.com/huangtaocsu/PCWLAD)

---

## 💡 一句话要点

**提出PCWLAD方法以解决多模态光学图像匹配精度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态图像匹配` `亚像素匹配` `遥感技术` `结构相似性` `图像处理` `机器视觉`

## 📋 核心要点

1. 现有的多模态光学图像匹配方法在处理非线性辐射和几何变形差异时，匹配精度往往受到影响。
2. 本文提出的PCWLAD方法通过相位一致性加权最小绝对偏差技术，结合粗匹配和精细匹配步骤，显著提高了匹配精度。
3. 实验结果显示，PCWLAD在三种不同类型的数据集上均表现出色，平均匹配精度达到约0.4像素，优于现有方法。

## 📝 摘要（中文）

高精度的多模态光学图像匹配是几何处理的基础。然而，由于不同光谱响应引起的非线性辐射和几何变形差异，图像匹配的准确性通常会降低。为了解决这些问题，本文提出了一种相位一致性加权最小绝对偏差（PCWLAD）亚像素模板匹配方法，以提高多模态光学图像的匹配精度。该方法包括两个主要步骤：使用结构相似性指数度量（SSIM）进行粗匹配和使用WLAD进行精细匹配。通过在粗匹配步骤中计算不带噪声滤波器的PC，保留原始结构细节，并使用SSIM进行模板匹配。在精细匹配步骤中，基于粗匹配应用辐射和几何变换模型。此外，模型中采用互结构滤波以减轻噪声对结构一致性的影响，并使用WLAD标准估计亚像素偏移。实验结果表明，PCWLAD在正确匹配率（CMR）和均方根误差（RMSE）方面优于现有的八种最先进方法，三种数据集的平均匹配精度约为0.4像素。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态光学图像匹配中的精度问题，现有方法在面对不同光谱响应导致的非线性辐射和几何变形时，匹配效果不佳。

**核心思路**：提出的PCWLAD方法通过相位一致性加权最小绝对偏差，结合粗匹配和精细匹配的策略，旨在提高匹配精度并减少噪声影响。

**技术框架**：该方法分为两个主要步骤：首先进行粗匹配，使用结构相似性指数度量（SSIM）计算相位一致性（PC），然后进行精细匹配，应用WLAD标准和辐射几何变换模型。

**关键创新**：PCWLAD的核心创新在于引入相位一致性加权和互结构滤波技术，显著提升了匹配的鲁棒性和精度，区别于传统方法的简单匹配策略。

**关键设计**：在粗匹配阶段不使用噪声滤波器以保留结构细节，而在精细匹配阶段则通过WLAD标准估计亚像素偏移，确保了匹配的准确性。

## 📊 实验亮点

实验结果表明，PCWLAD方法在正确匹配率（CMR）和均方根误差（RMSE）方面超越了现有的八种最先进方法，三种数据集的平均匹配精度达到约0.4像素，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括遥感图像处理、环境监测、城市规划等。通过提高多模态图像的匹配精度，可以更好地支持地理信息系统（GIS）和其他相关领域的决策分析，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> High-accuracy matching of multimodal optical images is the basis of geometric processing. However, the image matching accuracy is usually degraded by the nonlinear radiation and geometric deformation differences caused by different spectral responses. To address these problems, we proposed a phase consistency weighted least absolute deviation (PCWLAD) sub-pixel template matching method to improve the matching accuracy of multimodal optical images. This method consists of two main steps: coarse matching with the structural similarity index measure (SSIM) and fine matching with WLAD. In the coarse matching step, PCs are calculated without a noise filter to preserve the original structural details, and template matching is performed using the SSIM. In the fine matching step, we applied the radiometric and geometric transformation models between two multimodal PC templates based on the coarse matching. Furthermore, mutual structure filtering is adopted in the model to mitigate the impact of noise within the corresponding templates on the structural consistency, and the WLAD criterion is used to estimate the sub-pixel offset. To evaluate the performance of PCWLAD, we created three types of image datasets: visible to infrared Landsat images, visible to near-infrared close-range images, and visible to infrared uncrewed aerial vehicle (UAV) images. PCWLAD outperformed existing state-of-the-art eight methods in terms of correct matching rate (CMR) and root mean square error (RMSE) and reached an average matching accuracy of approximately 0.4 pixels across all three datasets. Our software and datasets are publicly available at https://github.com/huangtaocsu/PCWLAD.

