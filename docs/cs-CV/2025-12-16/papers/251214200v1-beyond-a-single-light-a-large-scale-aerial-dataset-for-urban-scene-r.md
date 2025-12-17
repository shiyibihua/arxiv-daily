---
layout: default
title: Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination
---

# Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.14200" target="_blank" class="toolbar-btn">arXiv: 2512.14200v1</a>
    <a href="https://arxiv.org/pdf/2512.14200.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14200v1" 
            onclick="toggleFavorite(this, '2512.14200v1', 'Beyond a Single Light: A Large-Scale Aerial Dataset for Urban Scene Reconstruction Under Varying Illumination')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zhuoxiao Li, Wenzong Ma, Taoyu Wu, Jinjing Zhu, Zhenchao Q, Shuai Zhang, Jing Ou, Yinrui Ren, Weiqing Qi, Guobin Shen, Hui Xiong, Wufan Zhao

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**SkyLume：一个大规模多光照城市重建航拍数据集，用于解决光照变化下的三维重建问题。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `三维重建` `无人机` `数据集` `光照变化` `逆渲染` `城市建模` `时间一致性` `多视角几何`

## 📋 核心要点

1. 现有基于NeRF和3D Gaussian Splatting的方法在无人机三维重建中表现出色，但多时相数据采集导致的光照不一致会引起伪影。
2. SkyLume数据集通过在不同时间段系统地捕捉同一区域的图像，并提供LiDAR扫描和3D ground-truth，从而解决光照变化带来的挑战。
3. 论文引入了时间一致性系数（TCC）指标，用于评估逆渲染中光照和材质解耦的鲁棒性，为后续研究提供评估标准。

## 📝 摘要（中文）

本文提出了SkyLume，一个大规模的真实世界航拍数据集，专门用于研究城市场景建模中光照鲁棒的三维重建。该数据集包含来自10个城市区域的超过10万张高分辨率无人机图像（四个倾斜视图和垂直视图），每个区域在一天中的三个不同时段进行拍摄，从而系统地隔离光照变化。为了支持对几何和外观的精确评估，我们提供了每个场景的激光雷达扫描和精确的3D ground-truth，用于评估不同光照下的深度、表面法线和重建质量。此外，针对逆渲染任务，我们引入了时间一致性系数（TCC），该指标衡量跨时间的albedo稳定性，并直接评估光照和材质解耦的鲁棒性。我们希望该资源能够为大规模逆渲染、几何重建和新视角合成的研究和实际评估奠定基础。

## 🔬 方法详解

**问题定义**：现有基于无人机图像的三维重建方法在处理大规模场景时，容易受到不同时间段光照变化的影响，导致重建结果出现颜色伪影、几何不准确和外观不一致等问题。缺乏系统性地捕捉不同光照条件下的数据集，使得这一问题难以得到充分研究。

**核心思路**：论文的核心思路是通过构建一个大规模的、包含多时相光照信息的无人机数据集，为研究光照鲁棒的三维重建提供数据基础。通过在同一区域的不同时间段进行拍摄，并提供精确的几何ground-truth，可以系统地评估和改进现有方法在光照变化下的性能。

**技术框架**：SkyLume数据集的构建流程主要包括以下几个阶段：1) 选择10个不同的城市区域；2) 使用无人机在每个区域的不同时间段（例如早晨、中午和傍晚）进行数据采集，获取多时相图像；3) 对每个区域进行激光雷达扫描，获取高精度的点云数据；4) 对图像和点云数据进行配准和校正，生成精确的3D ground-truth；5) 引入时间一致性系数（TCC）指标，用于评估逆渲染结果的质量。

**关键创新**：该论文的关键创新在于构建了一个大规模的、专门针对光照变化的三维重建数据集。与现有数据集相比，SkyLume数据集具有以下特点：1) 包含多时相光照信息，可以系统地研究光照变化对重建结果的影响；2) 提供高精度的激光雷达扫描和3D ground-truth，可以精确地评估重建结果的几何和外观质量；3) 引入了时间一致性系数（TCC）指标，可以定量地评估逆渲染结果的质量。

**关键设计**：在数据采集方面，论文选择了10个不同的城市区域，以保证数据集的多样性。在每个区域，论文在一天中的三个不同时间段进行拍摄，以系统地捕捉光照变化。无人机采用四个倾斜视图和一个垂直视图的拍摄方式，以获取更全面的场景信息。在评估指标方面，论文引入了时间一致性系数（TCC），该指标通过计算不同时间段albedo的一致性来评估逆渲染结果的质量。

## 📊 实验亮点

SkyLume数据集包含超过10万张高分辨率无人机图像，覆盖10个城市区域，并在三个不同时间段捕捉数据，系统性地隔离了光照变化。论文提出的时间一致性系数（TCC）为逆渲染任务提供了一种新的评估指标，能够有效衡量跨时间的albedo稳定性，为后续研究提供了可靠的评估工具。

## 🎯 应用场景

该研究成果可广泛应用于城市建模、自动驾驶、虚拟现实、增强现实等领域。通过利用SkyLume数据集，可以开发出更鲁棒、更精确的三维重建算法，从而提高城市建模的自动化程度，提升自动驾驶系统的环境感知能力，并为虚拟现实和增强现实应用提供更逼真的场景。

## 📄 摘要（原文）

> Recent advances in Neural Radiance Fields and 3D Gaussian Splatting have demonstrated strong potential for large-scale UAV-based 3D reconstruction tasks by fitting the appearance of images. However, real-world large-scale captures are often based on multi-temporal data capture, where illumination inconsistencies across different times of day can significantly lead to color artifacts, geometric inaccuracies, and inconsistent appearance. Due to the lack of UAV datasets that systematically capture the same areas under varying illumination conditions, this challenge remains largely underexplored. To fill this gap, we introduceSkyLume, a large-scale, real-world UAV dataset specifically designed for studying illumination robust 3D reconstruction in urban scene modeling: (1) We collect data from 10 urban regions data comprising more than 100k high resolution UAV images (four oblique views and nadir), where each region is captured at three periods of the day to systematically isolate illumination changes. (2) To support precise evaluation of geometry and appearance, we provide per-scene LiDAR scans and accurate 3D ground-truth for assessing depth, surface normals, and reconstruction quality under varying illumination. (3) For the inverse rendering task, we introduce the Temporal Consistency Coefficient (TCC), a metric that measuress cross-time albedo stability and directly evaluates the robustness of the disentanglement of light and material. We aim for this resource to serve as a foundation that advances research and real-world evaluation in large-scale inverse rendering, geometry reconstruction, and novel view synthesis.

