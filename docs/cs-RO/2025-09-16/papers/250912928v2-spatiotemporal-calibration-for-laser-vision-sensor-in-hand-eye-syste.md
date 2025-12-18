---
layout: default
title: Spatiotemporal Calibration for Laser Vision Sensor in Hand-eye System Based on Straight-line Constraint
---

# Spatiotemporal Calibration for Laser Vision Sensor in Hand-eye System Based on Straight-line Constraint

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12928" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12928v2</a>
  <a href="https://arxiv.org/pdf/2509.12928.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12928v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12928v2', 'Spatiotemporal Calibration for Laser Vision Sensor in Hand-eye System Based on Straight-line Constraint')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peiwen Yang, Mingquan Jiang, Xinyue Shen, Heping Zhang

**分类**: cs.RO

**发布日期**: 2025-09-16 (更新: 2025-11-03)

**备注**: Submitted to IEEE RAL

---

## 💡 一句话要点

**提出基于直线约束的时空标定方法，解决激光视觉手眼系统中时延和外参漂移问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `激光视觉传感器` `手眼标定` `时空标定` `直线约束` `机器人焊接`

## 📋 核心要点

1. 现有激光视觉手眼系统标定忽略相机时延和手眼外参漂移，导致焊接质量下降，需要解决时空同步问题。
2. 提出基于直线约束的时空标定方法，利用机器人扫描直线焊缝时焊点共线的几何特性，构建优化模型。
3. 实验验证了该方法在弯曲焊缝扫描中的可行性和准确性，并开源了代码、数据集和仿真报告。

## 📝 摘要（中文）

激光视觉传感器(LVS)是工业机器人的关键感知模块，有助于实时获取焊接应用中的工件几何数据。然而，相机通信延迟会导致捕获的图像与机器人运动之间的时间不同步。此外，手眼外部参数在长时间测量过程中可能会发生变化。为了解决这些问题，我们引入了一个考虑相机时间偏移影响的LVS测量模型，并提出了一种利用直线约束的免示教时空标定方法。该方法涉及配备LVS的机器人使用S形轨迹重复扫描直线角焊缝。无论机器人的方向如何变化，所有测量的焊接位置都被约束在一条直线上，用Plucker坐标表示。此外，建立了一个基于直线约束的非线性优化模型。随后，采用Levenberg-Marquardt算法(LMA)来优化参数，包括时间偏移、手眼外部参数和直线参数。通过弯曲焊缝扫描实验，定量验证了该方法的可行性和准确性。我们在https://anonymous.4open.science/r/LVS_ST_CALIB-015F/README.md上开源了代码、数据集和仿真报告。

## 🔬 方法详解

**问题定义**：激光视觉传感器在工业机器人焊接应用中至关重要，但相机通信延迟导致图像与机器人运动时间不同步，长时间测量导致手眼外参漂移，这些因素降低了焊接精度。现有方法通常忽略这些时空因素，导致标定不准确，影响焊接质量。

**核心思路**：利用直线约束进行时空标定。核心思想是，当机器人使用激光视觉传感器扫描直线焊缝时，无论机器人姿态如何变化，测量得到的焊缝点都应该位于同一条直线上。通过建立基于直线约束的优化模型，可以同时估计时间偏移和手眼外参。

**技术框架**：该方法主要包含以下几个阶段：1) 数据采集：机器人配备激光视觉传感器，沿S形轨迹重复扫描直线角焊缝，获取激光点云数据和机器人运动数据。2) 直线参数化：使用Plucker坐标表示三维空间中的直线。3) 优化模型构建：建立基于直线约束的非线性优化模型，目标函数是最小化测量点到拟合直线的距离。优化变量包括时间偏移、手眼外参和直线参数。4) 参数优化：使用Levenberg-Marquardt算法(LMA)求解非线性优化问题，得到最优的时空标定参数。

**关键创新**：该方法的主要创新在于：1) 提出了一种考虑相机时间偏移的激光视觉传感器测量模型。2) 利用直线约束，实现免示教的时空标定，无需精确的标定物。3) 将时间偏移、手眼外参和直线参数同时优化，提高了标定精度。

**关键设计**：1) S形扫描轨迹设计：保证机器人姿态变化的多样性，提高标定精度。2) Plucker坐标表示直线：方便计算点到直线的距离。3) Levenberg-Marquardt算法：一种常用的非线性优化算法，具有较好的收敛性和鲁棒性。4) 损失函数设计：最小化测量点到拟合直线的距离，保证测量点共线性。

## 📊 实验亮点

该论文通过在弯曲焊缝上的扫描实验验证了所提出方法的有效性。实验结果表明，该方法能够有效地标定激光视觉手眼系统的时间偏移和手眼外参，提高了焊接精度。具体性能数据和对比基线在论文中未明确给出，但开源的代码和数据集为后续研究提供了便利。

## 🎯 应用场景

该研究成果可应用于工业机器人焊接、3D扫描、逆向工程等领域。通过精确的时空标定，可以提高机器人系统的感知精度和作业效率，尤其是在需要高精度定位和测量的自动化生产线上具有重要价值。未来，该方法可以扩展到其他类型的传感器和机器人系统，进一步提升智能化水平。

## 📄 摘要（原文）

> Laser vision sensors (LVS) are critical perception modules for industrial robots, facilitating real-time acquisition of workpiece geometric data in welding applications. However, the camera communication delay will lead to a temporal desynchronization between captured images and the robot motions. Additionally, hand-eye extrinsic parameters may vary during prolonged measurement. To address these issues, we introduce a measurement model of LVS considering the effect of the camera's time-offset and propose a teaching-free spatiotemporal calibration method utilizing line constraints. This method involves a robot equipped with an LVS repeatedly scanning straight-line fillet welds using S-shaped trajectories. Regardless of the robot's orientation changes, all measured welding positions are constrained to a straight-line, represented by Plucker coordinates. Moreover, a nonlinear optimization model based on straight-line constraints is established. Subsequently, the Levenberg-Marquardt algorithm (LMA) is employed to optimize parameters, including time-offset, hand-eye extrinsic parameters, and straight-line parameters. The feasibility and accuracy of the proposed approach are quantitatively validated through experiments on curved weld scanning. We open-sourced the code, dataset, and simulation report at https://anonymous.4open.science/r/LVS_ST_CALIB-015F/README.md.

