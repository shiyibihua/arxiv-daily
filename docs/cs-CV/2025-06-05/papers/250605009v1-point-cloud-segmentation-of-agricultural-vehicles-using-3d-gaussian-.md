---
layout: default
title: Point Cloud Segmentation of Agricultural Vehicles using 3D Gaussian Splatting
---

# Point Cloud Segmentation of Agricultural Vehicles using 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05009" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05009v1</a>
  <a href="https://arxiv.org/pdf/2506.05009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05009v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05009v1', 'Point Cloud Segmentation of Agricultural Vehicles using 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alfred T. Christiansen, Andreas H. Højrup, Morten K. Stephansen, Md Ibtihaj A. Sakib, Taman S. Poojary, Filip Slezak, Morten S. Laursen, Thomas B. Moeslund, Joakim B. Haurum

**分类**: cs.CV

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出3D高斯点云分割方法以解决农业车辆语义分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D点云` `语义分割` `合成数据` `农业车辆` `深度学习` `高斯点云` `模型泛化`

## 📋 核心要点

1. 现有方法在获取和标注真实点云数据时成本高且耗时，限制了3D语义分割的研究和应用。
2. 论文提出通过3D高斯点云和高斯不透明度场生成合成数据，灵活模拟不同的LiDAR规格以提高数据生成效率。
3. 实验结果显示，PTv3模型在仅使用合成数据训练的情况下，mIoU达91.35%，并在某些场景中优于使用真实数据训练的模型。

## 📝 摘要（中文）

训练神经网络进行3D点云语义分割任务需要大量数据，但获取和标注真实世界的点云成本高且劳动密集。本文提出了一种新颖的合成数据生成管道，利用3D高斯点云和高斯不透明度场生成多种农业车辆的3D资产，并在模拟环境中生成点云。通过在合成数据上训练和验证模型，实验结果显示PTv3模型的mIoU达91.35%，且在某些情况下，合成数据训练的模型表现优于真实数据训练的模型。最后，实验表明模型能够跨语义类别进行泛化，准确预测未见过的网格模型。

## 🔬 方法详解

**问题定义**：本文旨在解决农业车辆的3D点云语义分割问题，现有方法在真实数据获取和标注上存在高成本和低效率的痛点。

**核心思路**：通过利用3D高斯点云和高斯不透明度场生成合成数据，避免了对真实数据的依赖，同时能够灵活调整LiDAR的参数设置。

**技术框架**：整体流程包括生成3D资产、在模拟环境中布置这些资产、使用模拟LiDAR生成点云，并在此基础上进行模型训练和验证。

**关键创新**：最重要的创新在于合成数据生成的灵活性和高效性，能够在不增加成本的情况下适应不同的LiDAR规格，与传统方法相比具有显著优势。

**关键设计**：在模型训练中，使用了PointNet++、Point Transformer V3和OACNN等网络架构，损失函数设计上注重语义分割的准确性，确保模型在合成数据上的有效学习。

## 📊 实验亮点

实验结果显示，PTv3模型在仅使用合成数据训练的情况下，mIoU达91.35%。在某些场景中，合成数据训练的模型表现优于真实数据训练的模型，显示出合成数据的有效性和模型的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括农业自动化、无人驾驶技术和智能监控系统。通过提供高质量的合成数据，能够加速模型的训练过程，降低对真实数据的依赖，提升农业车辆的智能化水平，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Training neural networks for tasks such as 3D point cloud semantic segmentation demands extensive datasets, yet obtaining and annotating real-world point clouds is costly and labor-intensive. This work aims to introduce a novel pipeline for generating realistic synthetic data, by leveraging 3D Gaussian Splatting (3DGS) and Gaussian Opacity Fields (GOF) to generate 3D assets of multiple different agricultural vehicles instead of using generic models. These assets are placed in a simulated environment, where the point clouds are generated using a simulated LiDAR. This is a flexible approach that allows changing the LiDAR specifications without incurring additional costs. We evaluated the impact of synthetic data on segmentation models such as PointNet++, Point Transformer V3, and OACNN, by training and validating the models only on synthetic data. Remarkably, the PTv3 model had an mIoU of 91.35\%, a noteworthy result given that the model had neither been trained nor validated on any real data. Further studies even suggested that in certain scenarios the models trained only on synthetically generated data performed better than models trained on real-world data. Finally, experiments demonstrated that the models can generalize across semantic classes, enabling accurate predictions on mesh models they were never trained on.

