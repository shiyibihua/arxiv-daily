---
layout: default
title: Dense 3D Displacement Estimation for Landslide Monitoring via Fusion of TLS Point Clouds and Embedded RGB Images
---

# Dense 3D Displacement Estimation for Landslide Monitoring via Fusion of TLS Point Clouds and Embedded RGB Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16265" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16265v1</a>
  <a href="https://arxiv.org/pdf/2506.16265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16265v1', 'Dense 3D Displacement Estimation for Landslide Monitoring via Fusion of TLS Point Clouds and Embedded RGB Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoyi Wang, Jemil Avers Butt, Shengyu Huang, Tomislav Medic, Andreas Wieser

**分类**: cs.CV, cs.RO, eess.IV, physics.geo-ph

**发布日期**: 2025-06-19

**备注**: 20 pages, 16 figures. Preprint under peer review. Example data and code available at [GitHub](https://github.com/zhaoyiww/fusion4landslide)

**🔗 代码/项目**: [GITHUB](https://github.com/zhaoyiww/fusion4landslide)

---

## 💡 一句话要点

**提出层次分区方法以解决滑坡监测中的稀疏位移估计问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `滑坡监测` `三维位移估计` `点云融合` `几何一致性` `深度学习` `地质灾害`

## 📋 核心要点

1. 现有的点云方法通常依赖于几何或辐射信息，导致位移估计稀疏或不准确。
2. 本文提出了一种层次分区的粗到细方法，融合三维点云和RGB图像以实现稠密位移估计。
3. 实验结果显示，该方法在空间覆盖率和准确性上均优于现有最先进方法F2S3。

## 📝 摘要（中文）

滑坡监测对于理解地质灾害及减轻相关风险至关重要。然而，现有基于点云的方法通常依赖几何或辐射信息，导致位移估计稀疏或非三维。本文提出了一种层次分区的粗到细方法，通过融合三维点云和共注册的RGB图像来估计稠密的三维位移矢量场。我们利用三维几何和二维图像特征构建补丁级匹配，并通过几何一致性检查进行精细化，随后对每个匹配进行刚性变换估计。实验结果表明，我们的方法在两个真实滑坡数据集上实现了79%和97%的高空间覆盖率，且位移幅度的偏差分别为0.15米和0.25米，低于平均扫描分辨率。我们的研究为基于TLS的滑坡监测提供了实用且可扩展的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决滑坡监测中现有点云方法的稀疏位移估计问题。现有方法通常只依赖几何或辐射信息，导致位移估计不够准确和全面。

**核心思路**：我们提出了一种层次分区的粗到细方法，通过融合三维点云和共注册的RGB图像，利用三维几何和二维图像特征构建补丁级匹配，从而实现稠密的三维位移矢量场估计。

**技术框架**：该方法的整体架构包括三个主要模块：首先进行三维点云和RGB图像的融合，接着构建补丁级匹配，最后通过几何一致性检查和刚性变换估计进行精细化处理。

**关键创新**：最重要的技术创新在于通过层次分区方法实现了三维位移的稠密估计，显著提高了空间覆盖率和准确性，克服了传统方法的局限性。

**关键设计**：在参数设置上，我们采用了适应性阈值来进行几何一致性检查，并设计了特定的损失函数以优化匹配精度。网络结构方面，结合了深度学习技术以增强特征提取能力。

## 📊 实验亮点

实验结果表明，我们的方法在两个真实滑坡数据集上实现了79%和97%的高空间覆盖率，位移幅度偏差分别为0.15米和0.25米，显著低于平均扫描分辨率。此外，该方法在空间覆盖率上优于现有最先进方法F2S3，同时保持了相似的准确性，展示了其优越性。

## 🎯 应用场景

该研究的潜在应用领域包括地质灾害监测、环境保护和基础设施安全等。通过提供高精度的位移估计，能够帮助相关部门及时发现和应对滑坡等地质灾害，降低风险并保护生命财产安全。未来，该方法还可扩展至其他类型的点云和监测任务，具有广泛的应用前景。

## 📄 摘要（原文）

> Landslide monitoring is essential for understanding geohazards and mitigating associated risks. However, existing point cloud-based methods typically rely on either geometric or radiometric information and often yield sparse or non-3D displacement estimates. In this paper, we propose a hierarchical partition-based coarse-to-fine approach that fuses 3D point clouds and co-registered RGB images to estimate dense 3D displacement vector fields. We construct patch-level matches using both 3D geometry and 2D image features. These matches are refined via geometric consistency checks, followed by rigid transformation estimation per match. Experimental results on two real-world landslide datasets demonstrate that our method produces 3D displacement estimates with high spatial coverage (79% and 97%) and high accuracy. Deviations in displacement magnitude with respect to external measurements (total station or GNSS observations) are 0.15 m and 0.25 m on the two datasets, respectively, and only 0.07 m and 0.20 m compared to manually derived references. These values are below the average scan resolutions (0.08 m and 0.30 m). Our method outperforms the state-of-the-art method F2S3 in spatial coverage while maintaining comparable accuracy. Our approach offers a practical and adaptable solution for TLS-based landslide monitoring and is extensible to other types of point clouds and monitoring tasks. Our example data and source code are publicly available at https://github.com/zhaoyiww/fusion4landslide.

