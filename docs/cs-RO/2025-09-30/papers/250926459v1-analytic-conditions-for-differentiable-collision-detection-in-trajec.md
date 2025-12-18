---
layout: default
title: Analytic Conditions for Differentiable Collision Detection in Trajectory Optimization
---

# Analytic Conditions for Differentiable Collision Detection in Trajectory Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26459" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26459v1</a>
  <a href="https://arxiv.org/pdf/2509.26459.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26459v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26459v1', 'Analytic Conditions for Differentiable Collision Detection in Trajectory Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Akshay Jaitly, Devesh K. Jha, Kei Ota, Yuki Shirai

**分类**: cs.RO, cs.CG

**发布日期**: 2025-09-30

**备注**: 8 pages, 8 figures. Accepted to the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2025

---

## 💡 一句话要点

**提出可微碰撞检测解析条件，加速轨迹优化中的非穿透约束**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `轨迹优化` `碰撞检测` `可微编程` `非穿透约束` `机器人规划`

## 📋 核心要点

1. 基于优化的方法被广泛用于计算复杂任务的快速、多样化解决方案，但需要强制执行对象之间的非穿透约束，计算成本高昂。
2. 论文提出了一种新的可微条件，具有解析表达式，可以有效地强制执行集合的非穿透，从而避免碰撞。
3. 通过数值实验验证了所提出方法的性能，并与现有方法进行了比较，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种在配置空间优化中有效实施集合非穿透的方法，该方法直接适用于碰撞感知轨迹优化等问题。为了实现这一目标，我们引入了具有解析表达式的新型可微条件。为了使用这些条件来强制非光滑物体之间的非碰撞，我们提出了一种将多面体近似为光滑半代数集的方法。我们进行了多个数值实验，以证明所提出方法的性能，并将性能与文献中最近提出的其他基线方法进行了比较。

## 🔬 方法详解

**问题定义**：在轨迹优化中，保证物体之间不发生碰撞是一个关键问题。现有的方法通常需要强制执行物体之间的非穿透约束，这导致了非平凡且计算量大的优化问题，严重影响了规划和控制的效率。尤其是在处理非光滑物体时，问题更加复杂。

**核心思路**：论文的核心思路是引入可微的碰撞检测条件，并提供解析表达式，从而避免了复杂的数值计算。通过将非光滑物体近似为光滑的半代数集，可以利用这些可微条件来有效地强制执行非碰撞约束。这种方法旨在简化优化过程，提高计算效率。

**技术框架**：该方法主要包含以下几个阶段：1) 将环境中的物体表示为集合；2) 引入可微的非穿透条件，这些条件具有解析表达式，易于计算梯度；3) 对于非光滑物体，使用光滑的半代数集进行近似；4) 将这些条件作为约束添加到轨迹优化问题中；5) 使用优化求解器求解轨迹。

**关键创新**：论文的关键创新在于提出了具有解析表达式的可微碰撞检测条件。与传统的碰撞检测方法相比，该方法可以直接计算梯度，从而可以更有效地进行优化。此外，使用光滑半代数集近似非光滑物体也是一个重要的创新，使得可以应用可微条件。

**关键设计**：论文的关键设计包括：1) 可微非穿透条件的具体形式，需要保证其可微性和有效性；2) 将多面体近似为光滑半代数集的方法，需要保证近似的精度和计算效率；3) 轨迹优化问题的具体形式，包括目标函数和约束条件；4) 优化求解器的选择和参数设置。

## 📊 实验亮点

论文通过数值实验验证了所提出方法的性能，并与现有方法进行了比较。实验结果表明，该方法可以有效地强制执行非碰撞约束，并且具有较高的计算效率。具体的性能数据和提升幅度在论文中进行了详细的展示。

## 🎯 应用场景

该研究成果可应用于机器人运动规划、自动驾驶、游戏开发等领域。通过高效的碰撞检测，可以实现更快速、更安全的轨迹规划，提高机器人的自主性和适应性。在虚拟环境中，可以实现更真实的物理交互效果。

## 📄 摘要（原文）

> Optimization-based methods are widely used for computing fast, diverse solutions for complex tasks such as collision-free movement or planning in the presence of contacts. However, most of these methods require enforcing non-penetration constraints between objects, resulting in a non-trivial and computationally expensive problem. This makes the use of optimization-based methods for planning and control challenging. In this paper, we present a method to efficiently enforce non-penetration of sets while performing optimization over their configuration, which is directly applicable to problems like collision-aware trajectory optimization. We introduce novel differentiable conditions with analytic expressions to achieve this. To enforce non-collision between non-smooth bodies using these conditions, we introduce a method to approximate polytopes as smooth semi-algebraic sets. We present several numerical experiments to demonstrate the performance of the proposed method and compare the performance with other baseline methods recently proposed in the literature.

