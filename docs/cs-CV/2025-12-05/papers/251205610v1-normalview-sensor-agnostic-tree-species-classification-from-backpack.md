---
layout: default
title: NormalView: sensor-agnostic tree species classification from backpack and aerial lidar data using geometric projections
---

# NormalView: sensor-agnostic tree species classification from backpack and aerial lidar data using geometric projections

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.05610" target="_blank" class="toolbar-btn">arXiv: 2512.05610v1</a>
    <a href="https://arxiv.org/pdf/2512.05610.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05610v1" 
            onclick="toggleFavorite(this, '2512.05610v1', 'NormalView: sensor-agnostic tree species classification from backpack and aerial lidar data using geometric projections')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Juho Korkeala, Jesse Muhojoki, Josef Taher, Klaara Salolahti, Matti Hyyppä, Antero Kukko, Juha Hyyppä

**分类**: cs.CV

**发布日期**: 2025-12-05

**备注**: 19 pages, 8 figures

---

## 💡 一句话要点

**NormalView：一种基于几何投影的传感器无关树种分类方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `树种分类` `点云处理` `激光扫描` `几何投影` `深度学习`

## 📋 核心要点

1. 现有树种分类方法依赖特定传感器或人工特征工程，泛化能力受限，难以适应不同激光扫描数据。
2. NormalView将点云局部几何信息投影为二维法向量图，利用图像分类网络进行树种分类，实现传感器无关性。
3. 实验表明，NormalView在MLS和ALS数据上均取得高精度，结合多光谱强度信息可进一步提升分类性能。

## 📝 摘要（中文）

激光扫描已成为评估森林环境分解的宝贵工具。移动激光扫描(MLS)在实现极其精确的树木级别清单方面显示出巨大的潜力。本研究提出NormalView，一种基于投影的、传感器无关的深度学习方法，用于从点云数据中分类树种。NormalView将局部几何信息以法向量估计的形式嵌入到二维投影中，并将这些投影用作图像分类网络YOLOv11的输入。此外，我们还研究了多光谱辐射强度信息对分类性能的影响。我们使用高密度MLS数据（7个树种，约5000点/平方米）以及高密度机载激光扫描(ALS)数据（9个树种，>1000点/平方米）训练和测试了我们的模型。在MLS数据上，NormalView实现了95.5%（宏平均准确率94.8%）的总体准确率，在ALS数据上实现了91.8%（宏平均准确率79.1%）。我们发现，来自多个扫描仪的强度信息有助于树种分类，并且多光谱ALS数据集上最好的模型是使用来自多光谱ALS所有三个通道的强度信息的模型。这项研究表明，当投影方法与几何信息相结合，并与最先进的图像分类骨干网络相结合时，可以取得出色的结果。至关重要的是，这些方法是传感器无关的，仅依赖于几何信息。此外，我们公开发布了本研究中使用的MLS数据集。

## 🔬 方法详解

**问题定义**：论文旨在解决利用激光扫描点云数据进行树种分类的问题。现有方法通常依赖于特定类型的传感器数据，或者需要人工设计特征，这限制了模型的泛化能力和适应性。此外，如何有效利用点云的几何信息和多光谱信息也是一个挑战。

**核心思路**：论文的核心思路是将三维点云数据转换为二维图像表示，利用图像分类的方法进行树种分类。通过将点云的局部几何信息（法向量）投影到二维平面上，可以有效地提取点云的结构特征。这种方法具有传感器无关性，因为法向量的计算只依赖于点云的几何信息，而与传感器的类型无关。

**技术框架**：NormalView方法的整体流程如下：1) 输入点云数据；2) 计算每个点的法向量；3) 将法向量投影到二维平面上，生成NormalView图像；4) 使用YOLOv11图像分类网络对NormalView图像进行分类，得到树种分类结果。该框架的关键模块包括法向量估计、投影变换和图像分类网络。

**关键创新**：该方法最重要的创新点在于其传感器无关性。通过将点云数据转换为基于几何信息的二维图像表示，该方法可以应用于来自不同类型激光扫描仪（如MLS和ALS）的数据，而无需进行特定的数据预处理或特征工程。此外，该方法还探索了多光谱强度信息对分类性能的影响。

**关键设计**：在法向量估计方面，论文采用了常用的邻域搜索算法。在投影变换方面，论文将法向量的三个分量映射到二维图像的RGB通道。在图像分类网络方面，论文选择了YOLOv11作为骨干网络，并针对树种分类任务进行了微调。此外，论文还研究了不同通道的多光谱强度信息对分类性能的影响，并选择了最佳的通道组合。

## 📊 实验亮点

NormalView在MLS数据上实现了95.5%的总体准确率（宏平均准确率94.8%），在ALS数据上实现了91.8%的总体准确率（宏平均准确率79.1%）。实验结果表明，结合多光谱强度信息可以进一步提升分类性能，尤其是在ALS数据上。该方法在两种不同类型的激光扫描数据上均取得了良好的效果，验证了其传感器无关性和泛化能力。

## 🎯 应用场景

该研究成果可应用于森林资源调查、生态环境监测、精准林业等领域。通过自动识别树种，可以提高森林资源管理的效率和精度，为制定合理的森林经营策略提供数据支持。此外，该方法具有传感器无关性，可以灵活应用于不同类型的激光扫描数据，具有广泛的应用前景。

## 📄 摘要（原文）

> Laser scanning has proven to be an invaluable tool in assessing the decomposition of forest environments. Mobile laser scanning (MLS) has shown to be highly promising for extremely accurate, tree level inventory. In this study, we present NormalView, a sensor-agnostic projection-based deep learning method for classifying tree species from point cloud data. NormalView embeds local geometric information into two-dimensional projections, in the form of normal vector estimates, and uses the projections as inputs to an image classification network, YOLOv11. In addition, we inspected the effect of multispectral radiometric intensity information on classification performance. We trained and tested our model on high-density MLS data (7 species, ~5000 pts/m^2), as well as high-density airborne laser scanning (ALS) data (9 species, >1000 pts/m^2). On the MLS data, NormalView achieves an overall accuracy (macro-average accuracy) of 95.5 % (94.8 %), and 91.8 % (79.1 %) on the ALS data. We found that having intensity information from multiple scanners provides benefits in tree species classification, and the best model on the multispectral ALS dataset was a model using intensity information from all three channels of the multispectral ALS. This study demonstrates that projection-based methods, when enhanced with geometric information and coupled with state-of-the-art image classification backbones, can achieve exceptional results. Crucially, these methods are sensor-agnostic, relying only on geometric information. Additionally, we publically release the MLS dataset used in the study.

