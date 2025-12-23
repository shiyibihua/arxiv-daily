---
layout: default
title: Synthetic Dataset Generation for Autonomous Mobile Robots Using 3D Gaussian Splatting for Vision Training
---

# Synthetic Dataset Generation for Autonomous Mobile Robots Using 3D Gaussian Splatting for Vision Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05092" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05092v1</a>
  <a href="https://arxiv.org/pdf/2506.05092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05092v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05092v1', 'Synthetic Dataset Generation for Autonomous Mobile Robots Using 3D Gaussian Splatting for Vision Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aneesh Deogan, Wout Beks, Peter Teurlings, Koen de Vos, Mark van den Brand, Rene van de Molengraft

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出基于3D高斯点云的合成数据生成方法以解决机器人视觉训练问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `合成数据` `3D高斯点云` `机器人视觉` `物体检测` `虚幻引擎` `自动化数据生成` `动态环境`

## 📋 核心要点

1. 现有的手动注释数据集创建过程耗时且容易出错，特别是在动态多变的机器人应用中更为复杂。
2. 提出了一种基于虚幻引擎的自动生成合成数据的方法，利用3D高斯点云实现快速生成和准确注释。
3. 实验结果表明，合成数据集的检测性能与真实数据集相当，且结合两者可显著提升物体检测效果。

## 📝 摘要（中文）

注释数据集对于训练神经网络进行物体检测至关重要，但其手动创建过程耗时且容易出错，且多样性有限。本文提出了一种在虚幻引擎中自动生成注释合成数据的新方法，利用逼真的3D高斯点云快速生成合成数据。研究表明，合成数据集的性能可与真实数据集相媲美，同时显著减少生成和注释数据所需的时间。此外，结合真实和合成数据可以显著提高物体检测性能。通过在机器人足球这一动态环境中进行验证实验，结果显示基于合成图像训练的检测器在测试时与基于手动注释的真实图像训练的检测器表现相当。该方法为传统数据集创建提供了一种可扩展且全面的替代方案。

## 🔬 方法详解

**问题定义**：当前手动创建注释数据集的过程不仅耗时且容易出错，尤其在机器人领域中，动态场景的多样性使得创建代表性数据集变得更加复杂。

**核心思路**：本研究提出了一种在虚幻引擎中自动生成注释合成数据的方法，利用3D高斯点云技术实现快速且高质量的数据生成，确保注释的准确性。

**技术框架**：整体流程包括数据生成、注释自动化和数据集整合三个主要模块。首先，在虚幻引擎中创建虚拟环境，然后利用3D高斯点云生成合成图像，最后将合成数据与真实数据结合以提升检测性能。

**关键创新**：本研究的创新点在于首次将合成数据应用于动态且多变的机器人足球环境中，显著提高了数据生成的效率和准确性，避免了传统方法中的人工注释错误。

**关键设计**：在技术细节上，采用了特定的参数设置以优化3D高斯点云的生成效果，损失函数设计上注重合成图像与真实图像的相似性，确保训练模型的有效性。通过这些设计，确保了合成数据的高质量和可用性。

## 📊 实验亮点

实验结果显示，基于合成图像训练的物体检测器在机器人足球比赛场景中的表现与基于手动注释的真实图像训练的检测器相当，验证了合成数据的有效性。此外，结合真实与合成数据后，物体检测性能显著提升，展示了该方法的实际应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、自动驾驶、智能监控等需要大量标注数据的场景。通过提供高效的合成数据生成方法，能够显著降低数据集创建的成本和时间，推动相关领域的技术进步和应用落地。

## 📄 摘要（原文）

> Annotated datasets are critical for training neural networks for object detection, yet their manual creation is time- and labour-intensive, subjective to human error, and often limited in diversity. This challenge is particularly pronounced in the domain of robotics, where diverse and dynamic scenarios further complicate the creation of representative datasets. To address this, we propose a novel method for automatically generating annotated synthetic data in Unreal Engine. Our approach leverages photorealistic 3D Gaussian splats for rapid synthetic data generation. We demonstrate that synthetic datasets can achieve performance comparable to that of real-world datasets while significantly reducing the time required to generate and annotate data. Additionally, combining real-world and synthetic data significantly increases object detection performance by leveraging the quality of real-world images with the easier scalability of synthetic data. To our knowledge, this is the first application of synthetic data for training object detection algorithms in the highly dynamic and varied environment of robot soccer. Validation experiments reveal that a detector trained on synthetic images performs on par with one trained on manually annotated real-world images when tested on robot soccer match scenarios. Our method offers a scalable and comprehensive alternative to traditional dataset creation, eliminating the labour-intensive error-prone manual annotation process. By generating datasets in a simulator where all elements are intrinsically known, we ensure accurate annotations while significantly reducing manual effort, which makes it particularly valuable for robotics applications requiring diverse and scalable training data.

