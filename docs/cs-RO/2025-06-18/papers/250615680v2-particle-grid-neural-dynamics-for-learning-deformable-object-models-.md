---
layout: default
title: Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos
---

# Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15680" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15680v2</a>
  <a href="https://arxiv.org/pdf/2506.15680.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15680v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15680v2', 'Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaifeng Zhang, Baoyu Li, Kris Hauser, Yunzhu Li

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-06-18 (更新: 2025-11-06)

**备注**: Project page: https://kywind.github.io/pgnd

**🔗 代码/项目**: [PROJECT_PAGE](https://kywind.github.io/pgnd)

---

## 💡 一句话要点

**提出粒子-网格神经动力学以解决可变形物体建模问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `可变形物体建模` `粒子-网格模型` `神经动力学` `机器人交互` `高斯渲染`

## 📋 核心要点

1. 现有方法在建模可变形物体动态时面临物理属性多样性和视觉信息不足的挑战。
2. 本文提出的粒子-网格模型通过结合粒子和空间网格，捕捉物体的全局形状和运动信息，提升学习效率。
3. 实验结果表明，该模型在多种物体（如绳子、布料等）的动态学习上优于现有方法，尤其在视角有限的情况下表现突出。

## 📝 摘要（中文）

建模可变形物体的动态特性面临多样的物理属性和有限视觉信息带来的挑战。本文提出了一种结合物体粒子和空间网格的混合表示的神经动力学框架。该模型能够捕捉全局形状和运动信息，同时预测密集的粒子运动，从而实现对形状和材料各异的物体建模。通过实验，我们展示了该模型在从稀疏视角RGB-D录制的机器人-物体交互中学习多样物体动态的能力，并在类别层面上对未见实例进行泛化。我们的框架在有限相机视角的场景中超越了现有的学习和物理模拟器，展示了在基于模型的规划中的应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决可变形物体动态建模中的挑战，现有方法在处理多样物理属性和有限视觉信息时效果不佳。

**核心思路**：提出的粒子-网格模型通过粒子表示物体形状，空间网格离散化三维空间，以确保空间连续性并增强学习效率。

**技术框架**：整体架构包括粒子表示模块、空间网格模块和高斯渲染模块，形成一个完整的学习框架，能够生成3D动作条件视频。

**关键创新**：最重要的创新在于将粒子与空间网格结合，形成混合表示，能够有效捕捉物体的动态特性，与传统方法相比具有更好的泛化能力。

**关键设计**：模型设计中采用了高斯渲染技术，确保视觉效果的真实感，同时在损失函数和网络结构上进行了优化，以提高学习效率和准确性。

## 📊 实验亮点

实验结果显示，所提出的模型在多样物体动态学习上显著优于现有的学习和物理模拟器，尤其在有限相机视角下，模型在准确性和泛化能力上均有显著提升，具体性能数据未提供。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、虚拟现实和增强现实等，能够为物体操作和交互提供更为精确的动态模型。未来，该技术可能在智能制造和自动化领域产生深远影响，提升机器人与环境的交互能力。

## 📄 摘要（原文）

> Modeling the dynamics of deformable objects is challenging due to their diverse physical properties and the difficulty of estimating states from limited visual information. We address these challenges with a neural dynamics framework that combines object particles and spatial grids in a hybrid representation. Our particle-grid model captures global shape and motion information while predicting dense particle movements, enabling the modeling of objects with varied shapes and materials. Particles represent object shapes, while the spatial grid discretizes the 3D space to ensure spatial continuity and enhance learning efficiency. Coupled with Gaussian Splattings for visual rendering, our framework achieves a fully learning-based digital twin of deformable objects and generates 3D action-conditioned videos. Through experiments, we demonstrate that our model learns the dynamics of diverse objects -- such as ropes, cloths, stuffed animals, and paper bags -- from sparse-view RGB-D recordings of robot-object interactions, while also generalizing at the category level to unseen instances. Our approach outperforms state-of-the-art learning-based and physics-based simulators, particularly in scenarios with limited camera views. Furthermore, we showcase the utility of our learned models in model-based planning, enabling goal-conditioned object manipulation across a range of tasks. The project page is available at https://kywind.github.io/pgnd .

