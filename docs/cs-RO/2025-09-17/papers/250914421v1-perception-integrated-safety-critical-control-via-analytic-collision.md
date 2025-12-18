---
layout: default
title: Perception-Integrated Safety Critical Control via Analytic Collision Cone Barrier Functions on 3D Gaussian Splatting
---

# Perception-Integrated Safety Critical Control via Analytic Collision Cone Barrier Functions on 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14421" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14421v1</a>
  <a href="https://arxiv.org/pdf/2509.14421.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14421v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14421v1', 'Perception-Integrated Safety Critical Control via Analytic Collision Cone Barrier Functions on 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dario Tscholl, Yashwanth Nakka, Brian Gunter

**分类**: cs.RO

**发布日期**: 2025-09-17

**备注**: Preprint for IEEE L-CSS/ACC

---

## 💡 一句话要点

**提出基于3D高斯溅射分析碰撞锥的感知集成安全控制方法，用于机器人安全导航。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `控制障碍函数` `碰撞避免` `安全控制` `机器人导航`

## 📋 核心要点

1. 现有基于距离的控制障碍函数(CBF)在障碍物临近时才激活，导致反应迟缓，难以保证复杂环境下的安全。
2. 论文提出一种基于3D高斯溅射(3DGS)的分析碰撞锥CBF，实现主动避障，提升安全性和平滑性。
3. 实验表明，该方法在大型场景中显著降低了规划时间和轨迹抖动，同时保持了安全水平。

## 📝 摘要（中文）

本文提出了一种感知驱动的安全滤波器，它将每个3D高斯溅射(3DGS)转换为闭式前向碰撞锥，进而产生一个嵌入在二次规划(QP)中的一阶控制障碍函数(CBF)。通过利用溅射的解析几何特性，我们的公式提供了一种连续的、闭式碰撞约束表示，它既简单又计算高效。与仅在障碍物已经很近时才反应性激活的基于距离的CBF不同，我们的碰撞锥CBF主动激活，允许机器人更早地调整，从而以更低的计算成本产生更平滑和更安全的避障动作。我们在一个包含约17万个溅射的大型合成场景中验证了该方法，结果表明，与最先进的3DGS规划器相比，我们的滤波器将规划时间减少了3倍，并显著降低了轨迹抖动，同时保持了相同的安全水平。该方法完全是解析的，不需要高阶CBF扩展(HOCBF)，并且通过对溅射进行有原则的闵可夫斯基和膨胀，自然地推广到具有物理尺寸的机器人。这些特性使得该方法广泛适用于在拥挤的、感知导出的极端环境中进行实时导航，包括空间机器人和卫星系统。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人如何在复杂、感知不确定环境中安全导航的问题。现有方法，特别是基于距离的控制障碍函数（CBF），通常在机器人非常接近障碍物时才激活，导致反应滞后，难以应对动态和拥挤的环境。此外，直接使用点云进行碰撞检测计算量大，难以满足实时性要求。

**核心思路**：论文的核心思路是将3D高斯溅射（3DGS）表示的环境信息转化为解析的碰撞锥，并利用这些碰撞锥构建控制障碍函数。通过分析3DGS的几何特性，可以将复杂的碰撞检测问题转化为简单的解析计算，从而实现高效的碰撞避免。这种方法允许机器人提前感知潜在的碰撞风险，并主动调整其运动轨迹，从而提高安全性和运动平滑性。

**技术框架**：该方法主要包含以下几个阶段：1) 使用3DGS表示环境；2) 将每个3DGS转化为一个前向碰撞锥；3) 基于碰撞锥构建一阶控制障碍函数（CBF）；4) 将CBF嵌入到二次规划（QP）问题中，求解最优控制量。整体框架利用3DGS的解析特性，避免了复杂的距离计算和高阶CBF扩展。

**关键创新**：该方法最重要的创新在于将3DGS与碰撞锥的概念相结合，提出了一种解析的碰撞避免方法。与传统的基于距离的CBF相比，该方法能够主动预测碰撞风险，并提前进行避障规划。此外，该方法不需要高阶CBF扩展，简化了控制器的设计和计算复杂度。

**关键设计**：关键设计包括：1) 使用3DGS表示环境，每个3DGS包含位置、协方差等信息；2) 基于3DGS的协方差矩阵，计算碰撞锥的参数；3) 设计一阶CBF，确保机器人的运动轨迹始终位于安全区域内；4) 通过闵可夫斯基和膨胀，将该方法推广到具有物理尺寸的机器人。

## 📊 实验亮点

实验结果表明，在包含约17万个溅射的大型合成场景中，该方法相比于最先进的3DGS规划器，将规划时间减少了3倍，并显著降低了轨迹抖动，同时保持了相同的安全水平。这表明该方法在计算效率和运动平滑性方面具有显著优势。

## 🎯 应用场景

该研究成果可广泛应用于需要在复杂、感知受限环境中进行自主导航的机器人系统，例如空间机器人、卫星系统、无人机、自动驾驶汽车等。尤其在需要高安全性和实时性的场景下，该方法具有重要的应用价值。未来，该方法可以进一步扩展到动态环境和多机器人系统。

## 📄 摘要（原文）

> We present a perception-driven safety filter that converts each 3D Gaussian Splat (3DGS) into a closed-form forward collision cone, which in turn yields a first-order control barrier function (CBF) embedded within a quadratic program (QP). By exploiting the analytic geometry of splats, our formulation provides a continuous, closed-form representation of collision constraints that is both simple and computationally efficient. Unlike distance-based CBFs, which tend to activate reactively only when an obstacle is already close, our collision-cone CBF activates proactively, allowing the robot to adjust earlier and thereby produce smoother and safer avoidance maneuvers at lower computational cost. We validate the method on a large synthetic scene with approximately 170k splats, where our filter reduces planning time by a factor of 3 and significantly decreased trajectory jerk compared to a state-of-the-art 3DGS planner, while maintaining the same level of safety. The approach is entirely analytic, requires no high-order CBF extensions (HOCBFs), and generalizes naturally to robots with physical extent through a principled Minkowski-sum inflation of the splats. These properties make the method broadly applicable to real-time navigation in cluttered, perception-derived extreme environments, including space robotics and satellite systems.

