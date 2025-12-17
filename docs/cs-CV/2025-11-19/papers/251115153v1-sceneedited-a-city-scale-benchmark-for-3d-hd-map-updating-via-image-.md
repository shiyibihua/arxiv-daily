---
layout: default
title: SceneEdited: A City-Scale Benchmark for 3D HD Map Updating via Image-Guided Change Detection
---

# SceneEdited: A City-Scale Benchmark for 3D HD Map Updating via Image-Guided Change Detection

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.15153" target="_blank" class="toolbar-btn">arXiv: 2511.15153v1</a>
    <a href="https://arxiv.org/pdf/2511.15153.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15153v1" 
            onclick="toggleFavorite(this, '2511.15153v1', 'SceneEdited: A City-Scale Benchmark for 3D HD Map Updating via Image-Guided Change Detection')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Chun-Jung Lin, Tat-Jun Chin, Sourav Garg, Feras Dayoub

**分类**: cs.CV

**发布日期**: 2025-11-19

**备注**: accepted by WACV 2026

**🔗 代码/项目**: [GITHUB](https://github.com/ChadLin9596/ScenePoint-ETK)

---

## 💡 一句话要点

**SceneEdited：提出城市级3D高清地图更新基准，通过图像引导的变更检测。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `高清地图更新` `三维重建` `变更检测` `城市级数据集` `自动驾驶`

## 📋 核心要点

1. 现有高清地图更新方法难以有效利用2D图像变更检测结果，将其转化为准确的3D地图更新。
2. SceneEdited数据集通过合成真实城市环境变化，提供大规模、多样化的3D地图更新训练数据。
3. 论文提供基于图像结构重建的基线方法和工具包，为后续研究提供标准化的评估平台。

## 📝 摘要（中文）

精确且最新的高清（HD）地图对于城市规划、基础设施监控和自动驾驶至关重要。然而，随着环境的演变，这些地图会迅速过时，因此需要强大的方法，不仅能检测到变化，还能将这些变化整合到更新的3D表示中。虽然变更检测技术已经取得了显著进展，但在检测变更和实际更新3D地图之间仍然存在明显的差距，尤其是在依赖于基于2D图像的变更检测时。为了解决这一差距，我们推出了SceneEdited，这是第一个城市级数据集，专门用于支持通过3D点云更新进行高清地图维护的研究。SceneEdited包含800多个最新场景，覆盖73公里的驾驶里程和约3平方公里的城市区域，超过23000个合成对象变更，这些变更通过手动和自动方式在2000多个过时版本中创建，模拟了现实的城市修改，例如缺失的路边基础设施、建筑物、立交桥和电线杆。每个场景都包括校准的RGB图像、激光雷达扫描和详细的变更掩码，用于训练和评估。我们还提供了使用基于图像的基础结构重建（Structure-from-Motion）流程更新过时场景的基线方法，以及一个全面的工具包，支持可扩展性、可跟踪性和可移植性，以便未来数据集的扩展和过时对象注释的统一。数据集和工具包均已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决如何利用图像引导的变更检测结果，高效、准确地更新3D高清地图的问题。现有方法在将2D图像信息转化为3D地图更新方面存在不足，难以处理大规模城市环境中的复杂变化，并且缺乏统一的评估基准。

**核心思路**：论文的核心思路是构建一个大规模、高质量的城市级数据集，包含真实场景的RGB图像、LiDAR点云以及精确的变更标注。通过该数据集，可以训练和评估基于图像的3D地图更新算法，并促进相关研究的进展。

**技术框架**：论文主要贡献在于数据集的构建，同时也提供了一个基于图像的结构重建（Structure-from-Motion）的基线方法。该基线方法首先利用图像进行稀疏的3D重建，然后将检测到的2D图像变更投影到3D空间，最后更新3D点云地图。数据集包含多个城市区域的场景，每个场景包含最新版本的RGB图像和LiDAR点云，以及多个模拟了不同变化的过时版本。

**关键创新**：该论文的关键创新在于构建了首个城市级3D高清地图更新数据集SceneEdited。该数据集规模大、场景多样，包含了各种类型的城市环境变化，并且提供了精确的变更标注，为3D地图更新研究提供了一个标准化的评估平台。

**关键设计**：数据集的构建过程中，采用了手动和自动相结合的方式生成对象变更。手动标注保证了变更的准确性，而自动生成则提高了数据集的规模和多样性。基线方法采用标准的Structure-from-Motion流程，并针对3D地图更新任务进行了优化。工具包的设计考虑了可扩展性、可跟踪性和可移植性，方便未来的数据集扩展和统一的标注管理。

## 📊 实验亮点

论文构建了包含超过800个场景、覆盖73公里驾驶里程的城市级数据集SceneEdited。该数据集包含超过23000个合成对象变更，模拟了真实的城市环境变化。论文还提供了一个基于图像结构重建的基线方法，为后续研究提供了一个参考。

## 🎯 应用场景

该研究成果可应用于自动驾驶、城市规划、基础设施监控等领域。通过利用图像信息自动更新高清地图，可以降低地图维护成本，提高地图的准确性和时效性，从而提升自动驾驶系统的安全性和可靠性，并为城市管理提供更精确的数据支持。

## 📄 摘要（原文）

> Accurate, up-to-date High-Definition (HD) maps are critical for urban planning, infrastructure monitoring, and autonomous navigation. However, these maps quickly become outdated as environments evolve, creating a need for robust methods that not only detect changes but also incorporate them into updated 3D representations. While change detection techniques have advanced significantly, there remains a clear gap between detecting changes and actually updating 3D maps, particularly when relying on 2D image-based change detection. To address this gap, we introduce SceneEdited, the first city-scale dataset explicitly designed to support research on HD map maintenance through 3D point cloud updating. SceneEdited contains over 800 up-to-date scenes covering 73 km of driving and approximate 3 $\text{km}^2$ of urban area, with more than 23,000 synthesized object changes created both manually and automatically across 2000+ out-of-date versions, simulating realistic urban modifications such as missing roadside infrastructure, buildings, overpasses, and utility poles. Each scene includes calibrated RGB images, LiDAR scans, and detailed change masks for training and evaluation. We also provide baseline methods using a foundational image-based structure-from-motion pipeline for updating outdated scenes, as well as a comprehensive toolkit supporting scalability, trackability, and portability for future dataset expansion and unification of out-of-date object annotations. Both the dataset and the toolkit are publicly available at https://github.com/ChadLin9596/ScenePoint-ETK, establising a standardized benchmark for 3D map updating research.

