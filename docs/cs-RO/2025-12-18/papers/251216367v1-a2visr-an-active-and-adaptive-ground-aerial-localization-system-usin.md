---
layout: default
title: A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion
---

# A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16367" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16367v1</a>
  <a href="https://arxiv.org/pdf/2512.16367.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16367v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16367v1', 'A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sijia Chen, Wei Dong

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: accept by IEEE Transactions on Industrial Electronics

---

## 💡 一句话要点

**提出A2VISR，一种融合视觉惯性和单测距的主动自适应地-空协同定位系统**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `地空协同定位` `主动视觉` `单点测距` `视觉惯性融合` `鲁棒定位`

## 📋 核心要点

1. 现有方法依赖固定相机和标记，易受距离限制和捕获失败影响，难以在复杂环境中保持定位鲁棒性。
2. A2VISR系统融合主动视觉、单点测距、惯性里程计和光流，提升视野、重捕获能力和定位精度。
3. 实验表明，A2VISR在多种复杂条件下实现了鲁棒的在线定位，平均均方根误差约为0.09米。

## 📝 摘要（中文）

本文提出了一种地-空协同系统，旨在提升飞行机器人在复杂环境中，尤其是在视觉传感器性能下降时的定位鲁棒性。传统方法使用固定相机观测预先安装的标记来估计飞行机器人的位置，但受到距离限制且容易捕获失败。为了解决这个问题，本文以更全面的方式改进了地-空定位框架，集成了主动视觉、单点测距、惯性里程计和光流。首先，地面车辆上安装的主动视觉子系统可以动态旋转，以检测和跟踪空中机器人上的红外标记，从而扩大视野范围，并使用单个摄像头提高目标识别率。同时，单点测距的加入扩展了可行距离，并增强了视觉退化下的重捕获能力。在估计过程中，一种降维估计器基于多项式逼近的扩展滑动窗口融合多源测量，平衡了计算效率和冗余。考虑到不同传感器的可靠性，实现了一种自适应滑动置信度评估算法，以评估测量质量，并基于移动方差动态调整权重参数。最后，在烟雾干扰、光照变化、障碍物遮挡、长时间视觉丢失和扩展操作范围等条件下进行的大量实验表明，所提出的方法实现了鲁棒的在线定位，平均均方根误差约为0.09米，同时保持了对捕获丢失和传感器故障的弹性。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂环境下，飞行机器人在视觉传感器退化时定位鲁棒性差的问题。现有方法依赖固定相机观测预先安装的标记，存在视野范围有限、易受距离限制和捕获失败等痛点。这些问题限制了飞行机器人在实际场景中的应用。

**核心思路**：论文的核心思路是构建一个地-空协同定位系统，通过地面车辆搭载的主动视觉系统和单点测距传感器，辅助空中机器人进行定位。主动视觉系统可以动态调整视角，扩大视野范围，提高目标识别率。单点测距则可以扩展可行距离，增强视觉退化下的重捕获能力。同时，融合惯性里程计和光流信息，提高定位精度和鲁棒性。

**技术框架**：A2VISR系统的整体框架包括以下几个主要模块：1) 地面车辆搭载的主动视觉子系统，用于检测和跟踪空中机器人上的红外标记；2) 单点测距传感器，用于测量地面车辆和空中机器人之间的距离；3) 空中机器人上的惯性测量单元（IMU）和摄像头，用于提供惯性里程计和光流信息；4) 降维估计器，用于融合多源测量数据，估计空中机器人的位置和姿态；5) 自适应滑动置信度评估算法，用于评估测量质量，动态调整权重参数。

**关键创新**：论文的关键创新在于以下几个方面：1) 提出了一种主动视觉系统，可以动态调整视角，扩大视野范围，提高目标识别率；2) 将单点测距引入地-空协同定位系统，扩展了可行距离，增强了视觉退化下的重捕获能力；3) 提出了一种自适应滑动置信度评估算法，可以根据测量质量动态调整权重参数，提高定位精度和鲁棒性。

**关键设计**：降维估计器基于多项式逼近的扩展滑动窗口，在保证计算效率的同时，融合多源测量数据。自适应滑动置信度评估算法基于移动方差评估测量质量，并动态调整权重参数。具体的参数设置和损失函数等技术细节在论文中进行了详细描述，但具体数值未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16367v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16367v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16367v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，A2VISR系统在烟雾干扰、光照变化、障碍物遮挡、长时间视觉丢失和扩展操作范围等复杂条件下，实现了鲁棒的在线定位，平均均方根误差约为0.09米。该系统能够有效应对视觉退化和传感器故障，保持对目标的稳定跟踪，显著提升了地-空协同定位的性能。

## 🎯 应用场景

A2VISR系统可应用于复杂环境下的无人机自主导航、协同作业、目标跟踪等领域。例如，在仓库巡检、灾后救援、桥梁检测等场景中，该系统可以提高无人机的定位精度和鲁棒性，使其能够在恶劣环境下安全可靠地完成任务。该研究成果有助于推动无人机在更多实际场景中的应用。

## 📄 摘要（原文）

> It's a practical approach using the ground-aerial collaborative system to enhance the localization robustness of flying robots in cluttered environments, especially when visual sensors degrade. Conventional approaches estimate the flying robot's position using fixed cameras observing pre-attached markers, which could be constrained by limited distance and susceptible to capture failure. To address this issue, we improve the ground-aerial localization framework in a more comprehensive manner, which integrates active vision, single-ranging, inertial odometry, and optical flow. First, the designed active vision subsystem mounted on the ground vehicle can be dynamically rotated to detect and track infrared markers on the aerial robot, improving the field of view and the target recognition with a single camera. Meanwhile, the incorporation of single-ranging extends the feasible distance and enhances re-capture capability under visual degradation. During estimation, a dimension-reduced estimator fuses multi-source measurements based on polynomial approximation with an extended sliding window, balancing computational efficiency and redundancy. Considering different sensor fidelities, an adaptive sliding confidence evaluation algorithm is implemented to assess measurement quality and dynamically adjust the weighting parameters based on moving variance. Finally, extensive experiments under conditions such as smoke interference, illumination variation, obstacle occlusion, prolonged visual loss, and extended operating range demonstrate that the proposed approach achieves robust online localization, with an average root mean square error of approximately 0.09 m, while maintaining resilience to capture loss and sensor failures.

