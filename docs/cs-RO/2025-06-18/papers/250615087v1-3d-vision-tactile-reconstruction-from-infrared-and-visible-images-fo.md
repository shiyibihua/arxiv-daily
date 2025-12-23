---
layout: default
title: 3D Vision-tactile Reconstruction from Infrared and Visible Images for Robotic Fine-grained Tactile Perception
---

# 3D Vision-tactile Reconstruction from Infrared and Visible Images for Robotic Fine-grained Tactile Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15087" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15087v1</a>
  <a href="https://arxiv.org/pdf/2506.15087.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15087v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15087v1', '3D Vision-tactile Reconstruction from Infrared and Visible Images for Robotic Fine-grained Tactile Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuankai Lin, Xiaofan Lu, Jiahui Chen, Hua Yang

**分类**: cs.RO

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出GelSplitter3D以解决传统平面触觉传感器在曲面重建中的不足**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉触觉传感器` `曲面重建` `光度立体` `法线估计` `机器人抓取` `生物仿生` `深度学习`

## 📋 核心要点

1. 传统平面触觉传感器在曲面重建中存在光照不足、重建模糊等挑战，限制了其在类人抓取中的应用。
2. 本文提出GelSplitter3D，通过扩展成像通道和近红外相机，结合光度立体神经网络和法线积分方法，解决了触觉几何校准问题。
3. 实验结果表明，触觉感知性能显著提升，法线估计准确率提高了40%，在抓取和操作任务中表现出更好的传感器形状优势。

## 📝 摘要（中文）

为了实现类人触觉感知，本文提出了一种新型的视觉触觉传感器（VTS），其感应表面从传统的平面配置演变为生物仿生的曲面拓扑。传统平面VTS在曲面扩展时面临光照不足、重建模糊及复杂的空间边界条件等挑战。为此，研究开发了GelSplitter3D，通过扩展成像通道与近红外相机结合，提出了基于光度立体的神经网络及CAD生成的法线真值校准方法，并设计了结合深度先验信息的法线积分方法以修正表面积分的累积误差。实验结果显示，触觉感知性能显著提升，法线估计准确率提高了40%。

## 🔬 方法详解

**问题定义**：本文旨在解决传统平面触觉传感器在曲面重建中的不足，特别是光照不足、重建模糊和复杂的空间边界条件等问题。

**核心思路**：通过开发GelSplitter3D，结合近红外相机和扩展成像通道，提出了一种新的光度立体神经网络和法线校准方法，以提高触觉传感器的几何重建精度。

**技术框架**：整体架构包括三个主要模块：1) GelSplitter3D的成像系统，2) 基于光度立体的神经网络，3) 法线积分方法，确保在重建过程中考虑深度先验信息。

**关键创新**：最重要的创新在于结合了近红外成像与光度立体技术，提出了一种新的法线校准方法，显著提高了法线估计的准确性，与传统方法相比具有本质的提升。

**关键设计**：在网络结构上，采用了特定的损失函数以优化法线估计，同时在法线积分过程中引入了边界约束，确保了重建的准确性和稳定性。

## 📊 实验亮点

实验结果显示，使用GelSplitter3D后，触觉传感器的法线估计准确率提高了40%。在抓取和操作任务中，传感器形状的优化显著提升了性能，展示了该方法在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、精细操作及人机交互等场景。通过提升触觉感知能力，未来可在医疗、服务机器人及智能制造等领域实现更高效的自动化和人性化交互，具有重要的实际价值和影响。

## 📄 摘要（原文）

> To achieve human-like haptic perception in anthropomorphic grippers, the compliant sensing surfaces of vision tactile sensor (VTS) must evolve from conventional planar configurations to biomimetically curved topographies with continuous surface gradients. However, planar VTSs have challenges when extended to curved surfaces, including insufficient lighting of surfaces, blurring in reconstruction, and complex spatial boundary conditions for surface structures. With an end goal of constructing a human-like fingertip, our research (i) develops GelSplitter3D by expanding imaging channels with a prism and a near-infrared (NIR) camera, (ii) proposes a photometric stereo neural network with a CAD-based normal ground truth generation method to calibrate tactile geometry, and (iii) devises a normal integration method with boundary constraints of depth prior information to correcting the cumulative error of surface integrals. We demonstrate better tactile sensing performance, a 40$\%$ improvement in normal estimation accuracy, and the benefits of sensor shapes in grasping and manipulation tasks.

