---
layout: default
title: Deep Imbalanced Multi-Target Regression: 3D Point Cloud Voxel Content Estimation in Simulated Forests
---

# Deep Imbalanced Multi-Target Regression: 3D Point Cloud Voxel Content Estimation in Simulated Forests

**arXiv**: [2511.12740v1](https://arxiv.org/abs/2511.12740) | [PDF](https://arxiv.org/pdf/2511.12740.pdf)

**作者**: Amirhossein Hassanzadeh, Bartosz Krawczyk, Michael Saunders, Rob Wible, Keith Krause, Dimah Dera, Jan van Aardt

**分类**: cs.CV

**发布日期**: 2025-11-16

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出基于KPConv的深度不平衡多目标回归方法，用于模拟森林中三维点云体素内容估计。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `三维点云` `激光雷达` `体素化` `多目标回归` `不平衡学习` `核点卷积` `森林模拟`

## 📋 核心要点

1. 现有LiDAR数据处理方法在体素化过程中损失了精细结构信息，难以准确估计体素内的目标占据百分比。
2. 提出一种基于KPConv的多目标回归方法，并结合成本敏感学习(DBR)解决类别不平衡问题，优化模型。
3. 实验表明，体素大小的选择对估计精度有显著影响，较大的体素尺寸误差较低，但会损失细节信息。

## 📝 摘要（中文）

体素化是降低激光雷达(LiDAR)数据处理计算成本的有效方法，但会导致精细结构信息的丢失。本研究探讨了是否可以从数字成像和遥感图像生成(DIRSIG)软件收集的高级体素化LiDAR点云数据中推断出低级体素内容信息，特别是体素内的目标占据百分比。研究目标包括树皮、树叶、土壤和杂项材料。我们提出了一种在不平衡学习背景下使用核点卷积(KPConv)的多目标回归方法。我们的研究利用成本敏感学习来解决称为基于密度的相关性(DBR)的类别不平衡问题。我们采用加权均方误差(MSE)、焦点回归(FocalR)和正则化来改进KPConv的优化。本研究对体素大小(0.25 - 2米)进行了敏感性分析，以评估各种网格表示在捕获森林细微差别方面的效果。敏感性分析表明，较大的体素尺寸(如2米)由于变异性降低而导致较低的误差，而较小的体素尺寸(如0.25或0.5米)表现出较高的误差，尤其是在变异性最大的树冠内。对于树皮和树叶目标，较小体素尺寸数据集(0.25和0.5米)的误差值明显高于较大体素尺寸数据集(2米)的误差值，突出了在精细分辨率下准确估计树冠内体素内容的难度。这表明体素尺寸的选择取决于应用。我们的工作填补了用于森林三维LiDAR点云的多目标回归深度不平衡学习模型和模拟数据集的空白。

## 🔬 方法详解

**问题定义**：论文旨在解决从体素化的LiDAR点云数据中准确估计体素内不同目标（树皮、树叶、土壤等）的占据百分比的问题。现有方法在体素化过程中会损失精细结构信息，导致难以准确估计体素内容。此外，不同目标的数量通常存在显著不平衡，进一步加剧了估计的难度。

**核心思路**：论文的核心思路是利用深度学习模型KPConv进行多目标回归，并结合成本敏感学习来解决类别不平衡问题。通过学习点云的局部几何特征，并对不同目标赋予不同的权重，从而提高对少数类目标的估计精度。

**技术框架**：整体框架包括以下几个主要步骤：1) 数据预处理：将LiDAR点云数据体素化，并计算每个体素内不同目标的占据百分比作为标签。2) 模型构建：使用KPConv作为基础网络，提取点云的局部特征。3) 损失函数设计：采用加权MSE、Focal Regression等损失函数，并结合正则化项，以提高模型的泛化能力。4) 训练与评估：使用模拟森林数据集训练模型，并评估其在不同体素大小下的性能。

**关键创新**：论文的关键创新在于：1) 将KPConv应用于多目标回归问题，并取得了良好的效果。2) 提出了基于密度的相关性(DBR)的成本敏感学习方法，有效解决了类别不平衡问题。3) 对体素大小进行了敏感性分析，揭示了体素大小对估计精度的影响。

**关键设计**：论文的关键设计包括：1) 使用KPConv提取点云的局部特征，能够有效捕捉点云的几何结构信息。2) 采用加权MSE和Focal Regression作为损失函数，能够平衡不同目标的贡献，提高对少数类目标的估计精度。3) 使用L1和L2正则化，防止过拟合，提高模型的泛化能力。

## 📊 实验亮点

实验结果表明，所提出的方法在模拟森林数据集上取得了良好的性能。敏感性分析表明，较大的体素尺寸(如2米)导致较低的误差，而较小的体素尺寸(如0.25或0.5米)表现出较高的误差，尤其是在树冠内。对于树皮和树叶目标，较小体素尺寸数据集的误差值明显高于较大体素尺寸数据集的误差值。

## 🎯 应用场景

该研究成果可应用于森林资源调查、生物量估算、火灾风险评估等领域。通过准确估计森林中不同目标的含量，可以为森林管理和保护提供更可靠的数据支持。未来，该方法还可以扩展到其他类型的遥感数据和应用场景，例如城市环境建模、农业监测等。

## 📄 摘要（原文）

> Voxelization is an effective approach to reduce the computational cost of processing Light Detection and Ranging (LiDAR) data, yet it results in a loss of fine-scale structural information. This study explores whether low-level voxel content information, specifically target occupancy percentage within a voxel, can be inferred from high-level voxelized LiDAR point cloud data collected from Digital Imaging and remote Sensing Image Generation (DIRSIG) software. In our study, the targets include bark, leaf, soil, and miscellaneous materials. We propose a multi-target regression approach in the context of imbalanced learning using Kernel Point Convolutions (KPConv). Our research leverages cost-sensitive learning to address class imbalance called density-based relevance (DBR). We employ weighted Mean Saquared Erorr (MSE), Focal Regression (FocalR), and regularization to improve the optimization of KPConv. This study performs a sensitivity analysis on the voxel size (0.25 - 2 meters) to evaluate the effect of various grid representations in capturing the nuances of the forest. This sensitivity analysis reveals that larger voxel sizes (e.g., 2 meters) result in lower errors due to reduced variability, while smaller voxel sizes (e.g., 0.25 or 0.5 meter) exhibit higher errors, particularly within the canopy, where variability is greatest. For bark and leaf targets, error values at smaller voxel size datasets (0.25 and 0.5 meter) were significantly higher than those in larger voxel size datasets (2 meters), highlighting the difficulty in accurately estimating within-canopy voxel content at fine resolutions. This suggests that the choice of voxel size is application-dependent. Our work fills the gap in deep imbalance learning models for multi-target regression and simulated datasets for 3D LiDAR point clouds of forests.

