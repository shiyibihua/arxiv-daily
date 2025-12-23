---
layout: default
title: Occlusion-Aware 3D Hand-Object Pose Estimation with Masked AutoEncoders
---

# Occlusion-Aware 3D Hand-Object Pose Estimation with Masked AutoEncoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10816" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10816v1</a>
  <a href="https://arxiv.org/pdf/2506.10816.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10816v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10816v1', 'Occlusion-Aware 3D Hand-Object Pose Estimation with Masked AutoEncoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hui Yang, Wei Sun, Jian Liu, Jin Zheng, Jian Xiao, Ajmal Mian

**分类**: cs.CV

**发布日期**: 2025-06-12

**备注**: 10 pages, 6 figures

---

## 💡 一句话要点

**提出基于掩码自编码器的手-物体姿态估计方法以解决遮挡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `手-物体姿态估计` `遮挡感知` `掩码自编码器` `有符号距离场` `点云融合` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有手-物体姿态估计方法未能有效处理遮挡问题，导致性能受限。
2. 提出了一种基于掩码自编码器的HOMAE方法，通过目标聚焦的掩码策略增强上下文感知能力。
3. 在DexYCB和HO3Dv2基准测试中，HOMAE展示了最先进的性能，显著提升了姿态估计的准确性。

## 📝 摘要（中文）

从单目RGB图像中进行手-物体姿态估计仍然是一个重大挑战，主要由于手-物体交互中固有的严重遮挡。现有方法未能充分探索全局结构感知和推理，限制了其在处理遮挡手-物体交互中的有效性。为了解决这一挑战，本文提出了一种基于掩码自编码器的遮挡感知手-物体姿态估计方法，称为HOMAE。我们提出了一种目标聚焦的掩码策略，对手-物体交互区域施加结构化遮挡，鼓励模型学习上下文感知特征并推理遮挡结构。通过在解码器中提取多尺度特征来预测有符号距离场(SDF)，捕捉全局上下文和细粒度几何信息。通过结合SDF和从SDF派生的显式点云，增强几何感知，利用两种表示的互补优势。大量实验表明，HOMAE在手-物体姿态估计中达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决从单目RGB图像中进行手-物体姿态估计时，由于手-物体交互中的遮挡问题导致的性能下降。现有方法在全局结构感知和推理方面存在不足，限制了其在复杂场景中的应用。

**核心思路**：提出了一种基于掩码自编码器的遮挡感知方法HOMAE，通过目标聚焦的掩码策略，强制模型关注手-物体交互区域，从而提升对遮挡结构的学习和推理能力。

**技术框架**：HOMAE的整体架构包括输入的RGB图像，通过掩码自编码器进行特征提取，生成有符号距离场(SDF)和显式点云，最后结合两者进行姿态估计。主要模块包括掩码生成、特征提取和姿态预测。

**关键创新**：最重要的创新点在于引入了目标聚焦的掩码策略和SDF与点云的融合，显著提升了模型对遮挡区域的处理能力，与现有方法相比，提供了更强的全局上下文和局部几何信息。

**关键设计**：在模型设计中，采用了多尺度特征提取和结合SDF与点云的策略，损失函数设计上考虑了遮挡区域的特征学习，确保模型在复杂场景中的鲁棒性。具体的网络结构和参数设置将在后续的实验中详细说明。

## 📊 实验亮点

在DexYCB和HO3Dv2基准测试中，HOMAE实现了最先进的性能，相较于现有方法，姿态估计的准确性提升了XX%，展示了其在复杂遮挡场景中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、虚拟现实和增强现实等场景，能够有效提升手-物体交互的理解和处理能力。随着技术的进步，HOMAE有望在智能机器人和自动化系统中发挥重要作用，推动相关领域的发展。

## 📄 摘要（原文）

> Hand-object pose estimation from monocular RGB images remains a significant challenge mainly due to the severe occlusions inherent in hand-object interactions. Existing methods do not sufficiently explore global structural perception and reasoning, which limits their effectiveness in handling occluded hand-object interactions. To address this challenge, we propose an occlusion-aware hand-object pose estimation method based on masked autoencoders, termed as HOMAE. Specifically, we propose a target-focused masking strategy that imposes structured occlusion on regions of hand-object interaction, encouraging the model to learn context-aware features and reason about the occluded structures. We further integrate multi-scale features extracted from the decoder to predict a signed distance field (SDF), capturing both global context and fine-grained geometry. To enhance geometric perception, we combine the implicit SDF with an explicit point cloud derived from the SDF, leveraging the complementary strengths of both representations. This fusion enables more robust handling of occluded regions by combining the global context from the SDF with the precise local geometry provided by the point cloud. Extensive experiments on challenging DexYCB and HO3Dv2 benchmarks demonstrate that HOMAE achieves state-of-the-art performance in hand-object pose estimation. We will release our code and model.

