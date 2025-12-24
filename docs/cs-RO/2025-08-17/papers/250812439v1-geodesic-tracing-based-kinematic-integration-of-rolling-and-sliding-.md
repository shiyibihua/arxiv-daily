---
layout: default
title: Geodesic Tracing-Based Kinematic Integration of Rolling and Sliding Contact on Manifold Meshes for Dexterous In-Hand Manipulation
---

# Geodesic Tracing-Based Kinematic Integration of Rolling and Sliding Contact on Manifold Meshes for Dexterous In-Hand Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12439" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12439v1</a>
  <a href="https://arxiv.org/pdf/2508.12439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12439v1', 'Geodesic Tracing-Based Kinematic Integration of Rolling and Sliding Contact on Manifold Meshes for Dexterous In-Hand Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sunyu Wang, Arjun S. Lakshmipathy, Jean Oh, Nancy S. Pollard

**分类**: cs.RO

**发布日期**: 2025-08-17

---

## 💡 一句话要点

**提出基于测地线追踪的运动学集成方法以解决复杂接触问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `滚滑接触` `流形网格` `灵巧操作` `测地线追踪` `运动规划` `机器人技术` `接触建模`

## 📋 核心要点

1. 现有的滚滑接触建模方法主要集中在连续形状上，难以处理复杂的离散网格结构。
2. 本研究提出了一种基于测地线追踪的集成方案，能够在网格上直接进行滚滑接触的时间积分。
3. 实验结果显示，该方法在准确性和精度上优于基于碰撞检测和原始形状的基线方法，尤其适用于粗糙网格。

## 📝 摘要（中文）

关于滚动和滑动接触的推理对于涉及复杂几何形状的灵巧操作任务至关重要。然而，现有的滚滑接触研究主要集中在具有可微分参数化的连续形状上。本研究将滚滑接触建模扩展到流形网格，提出了一种基于测地线追踪的集成方案，能够直接在网格上进行一阶时间积分，从而使灵巧操作能够在物体真实几何的高保真离散表示上进行推理。我们的方法在仿真中规划了多指机器人手对五个物体的灵巧运动，使用最小二乘优化器来保持最稳定的瞬时抓取，减少接触滑动和旋转。实验结果表明，我们的方法在准确性和精度上优于基线方法，尤其是在粗糙网格上。最后，我们讨论了未来的工作方向，包括整合多个接触和接触力，以实现准确且稳健的网格表面接触建模。

## 🔬 方法详解

**问题定义**：本论文旨在解决在复杂几何形状上进行灵巧操作时，现有滚滑接触建模方法无法有效处理离散网格的问题。现有方法多集中于连续形状，缺乏对高保真离散表示的支持。

**核心思路**：论文提出了一种基于测地线追踪的集成方案，能够在网格上进行一阶时间积分，从而实现对滚滑接触的有效建模。该设计旨在提高灵巧操作的精度和稳定性。

**技术框架**：整体架构包括接触建模、运动规划和优化三个主要模块。首先，通过测地线追踪实现滚滑接触的建模；然后，使用最小二乘优化器进行运动规划，最后评估与基线方法的性能对比。

**关键创新**：最重要的技术创新在于将滚滑接触建模扩展到流形网格，并通过测地线追踪实现直接的时间积分。这一方法与现有的基于连续形状的建模方法有本质区别，能够处理更复杂的几何形状。

**关键设计**：在优化过程中，使用了最小二乘损失函数，旨在减少接触滑动和旋转，确保抓取的稳定性。具体参数设置和优化策略在实验中进行了详细验证，以确保方法的有效性。

## 📊 实验亮点

实验结果表明，提出的方法在准确性和精度上优于基于碰撞检测的基线方法和使用原始形状的基线方法，尤其是在处理粗糙网格时，表现出显著的性能提升，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、自动化装配和人机交互等。通过提高对复杂几何形状的操作能力，能够在实际应用中实现更高效的物体操控，推动智能机器人技术的发展。未来，整合多个接触和接触力的研究将进一步提升模型的准确性和鲁棒性。

## 📄 摘要（原文）

> Reasoning about rolling and sliding contact, or roll-slide contact for short, is critical for dexterous manipulation tasks that involve intricate geometries. But existing works on roll-slide contact mostly focus on continuous shapes with differentiable parametrizations. This work extends roll-slide contact modeling to manifold meshes. Specifically, we present an integration scheme based on geodesic tracing to first-order time-integrate roll-slide contact directly on meshes, enabling dexterous manipulation to reason over high-fidelity discrete representations of an object's true geometry. Using our method, we planned dexterous motions of a multi-finger robotic hand manipulating five objects in-hand in simulation. The planning was achieved with a least-squares optimizer that strives to maintain the most stable instantaneous grasp by minimizing contact sliding and spinning. Then, we evaluated our method against a baseline using collision detection and a baseline using primitive shapes. The results show that our method performed the best in accuracy and precision, even for coarse meshes. We conclude with a future work discussion on incorporating multiple contacts and contact forces to achieve accurate and robust mesh-based surface contact modeling.

