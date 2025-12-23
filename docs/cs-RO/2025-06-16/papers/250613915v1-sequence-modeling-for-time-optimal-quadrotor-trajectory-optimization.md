---
layout: default
title: Sequence Modeling for Time-Optimal Quadrotor Trajectory Optimization with Sampling-based Robustness Analysis
---

# Sequence Modeling for Time-Optimal Quadrotor Trajectory Optimization with Sampling-based Robustness Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13915" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13915v1</a>
  <a href="https://arxiv.org/pdf/2506.13915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13915v1', 'Sequence Modeling for Time-Optimal Quadrotor Trajectory Optimization with Sampling-based Robustness Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Katherine Mao, Hongzhan Yu, Ruipeng Zhang, Igor Spasojevic, M Ani Hsieh, Sicun Gao, Vijay Kumar

**分类**: cs.RO

**发布日期**: 2025-06-16

**🔗 代码/项目**: [GITHUB](https://github.com/maokat12/lbTOPPQuad)

---

## 💡 一句话要点

**提出基于学习的模型以加速四旋翼时间最优轨迹生成**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四旋翼` `轨迹优化` `学习模型` `数据增强` `实时控制` `机器人技术`

## 📋 核心要点

1. 现有的时间最优轨迹规划方法在计算上复杂且成本高，难以满足实时应用需求。
2. 本文提出了一种基于学习的模型，通过模仿时间最优轨迹规划器，加速轨迹生成过程。
3. 实验结果显示，所提方法在速度上有显著提升，并能够处理未见路径长度的情况。

## 📝 摘要（中文）

时间最优轨迹使四旋翼飞行器达到其动态极限，但计算此类轨迹涉及通过迭代非线性优化解决非凸问题，导致实时应用成本高昂。本文研究了模仿基于模型的时间最优轨迹规划器的学习模型，以加速轨迹生成。通过分析学习模型的局部解析特性，并将其与几何跟踪控制器的反向可达管相联系，提出了一种数据增强方案以提高鲁棒性。与经典规划器相比，我们的方法显著加快了速度，并在硬件四旋翼平台上验证了其实时可行性。实验表明，学习模型能够推广到之前未见的路径长度。

## 🔬 方法详解

**问题定义**：本文旨在解决四旋翼时间最优轨迹生成的计算复杂性问题。现有方法依赖于迭代非线性优化，导致实时应用受限。

**核心思路**：通过学习模型模仿基于模型的时间最优轨迹规划器，快速生成轨迹，并引入数据增强以提高模型的鲁棒性。

**技术框架**：整体架构包括数据收集、模型训练和轨迹生成三个主要阶段。首先收集无碰撞的几何路径数据，然后训练学习模型，最后利用训练好的模型生成时间最优轨迹。

**关键创新**：最重要的创新在于提出了一种定量框架来分析学习模型的局部解析特性，并将其与几何跟踪控制器的反向可达管相结合，提升了轨迹生成的效率和鲁棒性。

**关键设计**：在模型训练中，采用了随机扰动的数据增强策略，以提高模型对输入路径的适应性。损失函数设计上，关注于轨迹的时间最优性和安全性，确保生成的轨迹既快速又安全。

## 📊 实验亮点

实验结果表明，所提方法在轨迹生成速度上相比传统规划器有显著提升，具体速度提升幅度达到数倍。同时，学习模型在处理未见路径长度时表现出良好的泛化能力，验证了其实时可行性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机自动驾驶、物流运输、搜索与救援等场景。通过加速轨迹生成过程，能够在动态环境中实现更高效的飞行控制，提升无人机的实用性和安全性。未来，该方法有望推广到更多类型的机器人和自动化系统中。

## 📄 摘要（原文）

> Time-optimal trajectories drive quadrotors to their dynamic limits, but computing such trajectories involves solving non-convex problems via iterative nonlinear optimization, making them prohibitively costly for real-time applications. In this work, we investigate learning-based models that imitate a model-based time-optimal trajectory planner to accelerate trajectory generation. Given a dataset of collision-free geometric paths, we show that modeling architectures can effectively learn the patterns underlying time-optimal trajectories. We introduce a quantitative framework to analyze local analytic properties of the learned models, and link them to the Backward Reachable Tube of the geometric tracking controller. To enhance robustness, we propose a data augmentation scheme that applies random perturbations to the input paths. Compared to classical planners, our method achieves substantial speedups, and we validate its real-time feasibility on a hardware quadrotor platform. Experiments demonstrate that the learned models generalize to previously unseen path lengths. The code for our approach can be found here: https://github.com/maokat12/lbTOPPQuad

