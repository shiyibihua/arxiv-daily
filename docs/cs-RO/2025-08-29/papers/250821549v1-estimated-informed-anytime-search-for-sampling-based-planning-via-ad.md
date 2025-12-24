---
layout: default
title: Estimated Informed Anytime Search for Sampling-Based Planning via Adaptive Sampler
---

# Estimated Informed Anytime Search for Sampling-Based Planning via Adaptive Sampler

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21549" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21549v1</a>
  <a href="https://arxiv.org/pdf/2508.21549.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21549v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21549v1', 'Estimated Informed Anytime Search for Sampling-Based Planning via Adaptive Sampler')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liding Zhang, Kuanqi Cai, Yu Zhang, Zhenshan Bing, Chaoqun Wang, Fan Wu, Sami Haddadin, Alois Knoll

**分类**: cs.RO

**发布日期**: 2025-08-29

**期刊**: IEEE Transactions on Automation Science and Engineering 2025

**DOI**: [10.1109/TASE.2025.3590084](https://doi.org/10.1109/TASE.2025.3590084)

---

## 💡 一句话要点

**提出MIT*以解决高维路径规划中的采样效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `路径规划` `采样方法` `自适应采样` `机器人操作` `高维空间` `知情采样` `碰撞检测` `算法优化`

## 📋 核心要点

1. 现有的知情采样规划方法在未找到解决方案时需重新探索整个配置空间，导致效率低下。
2. MIT*通过在初始解决方案之前构建估计的知情集，并采用自适应采样策略，显著提高了路径规划效率。
3. 实验结果表明，MIT*在高维空间中表现优异，成功率高，且在实际机器人操作中应用效果良好。

## 📝 摘要（中文）

机器人路径规划通常涉及解决连续值的高维问题。现有的知情采样方法在未找到解决方案时需重新采样，导致时间和计算成本高昂。本文提出了一种新型规划器MIT*，通过在找到初始解决方案之前构建估计的知情集，显著加快初始收敛速度。同时，MIT*采用自适应采样器，根据探索过程动态调整采样策略，并利用与路径长度相关的稀疏碰撞检查来指导懒惰反向搜索。这些特性提高了路径成本效率和计算时间，同时确保在受限场景中的高成功率。通过一系列仿真和实际实验，MIT*在R^4到R^16的问题上超越了现有的单查询采样规划器，并成功应用于实际机器人操作任务。

## 🔬 方法详解

**问题定义**：本文旨在解决高维路径规划中的采样效率问题。现有的知情采样方法在未找到解决方案时需要重新探索整个配置空间，导致时间和计算成本的浪费。

**核心思路**：MIT*的核心思路是通过在找到初始解决方案之前构建估计的知情集，从而加速初始收敛率。该方法还引入了自适应采样器，根据探索过程动态调整采样策略，以提高效率。

**技术框架**：MIT*的整体架构包括三个主要模块：估计知情集构建模块、自适应采样模块和懒惰反向搜索模块。首先，构建基于先前可接受解决方案成本的知情集；其次，动态调整采样策略以优化探索过程；最后，通过稀疏碰撞检查指导反向搜索。

**关键创新**：MIT*的主要创新在于其估计知情集的构建方法和自适应采样策略。这与现有方法的本质区别在于，MIT*在初始解决方案找到之前就进行知情集的构建，从而避免了无效的全局重新采样。

**关键设计**：MIT*采用了与路径长度相关的稀疏碰撞检查技术，以减少计算负担。此外，自适应采样器的设计允许根据实时探索反馈调整采样策略，从而提高了路径规划的效率和成功率。

## 📊 实验亮点

实验结果显示，MIT*在R^4到R^16的高维问题上，相较于现有的单查询采样规划器，成功率显著提高，路径成本效率和计算时间也得到了优化。具体而言，MIT*在多次实验中表现出更快的收敛速度和更低的计算开销，验证了其优越性。

## 🎯 应用场景

MIT*在高维路径规划中的应用潜力巨大，尤其适用于复杂的机器人操作任务，如工业机器人、无人机导航和自动驾驶等领域。其高效的路径规划能力能够显著提升机器人在动态环境中的适应性和操作效率，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Path planning in robotics often involves solving continuously valued, high-dimensional problems. Popular informed approaches include graph-based searches, such as A*, and sampling-based methods, such as Informed RRT*, which utilize informed set and anytime strategies to expedite path optimization incrementally. Informed sampling-based planners define informed sets as subsets of the problem domain based on the current best solution cost. However, when no solution is found, these planners re-sample and explore the entire configuration space, which is time-consuming and computationally expensive. This article introduces Multi-Informed Trees (MIT*), a novel planner that constructs estimated informed sets based on prior admissible solution costs before finding the initial solution, thereby accelerating the initial convergence rate. Moreover, MIT* employs an adaptive sampler that dynamically adjusts the sampling strategy based on the exploration process. Furthermore, MIT* utilizes length-related adaptive sparse collision checks to guide lazy reverse search. These features enhance path cost efficiency and computation times while ensuring high success rates in confined scenarios. Through a series of simulations and real-world experiments, it is confirmed that MIT* outperforms existing single-query, sampling-based planners for problems in R^4 to R^16 and has been successfully applied to real-world robot manipulation tasks. A video showcasing our experimental results is available at: https://youtu.be/30RsBIdexTU

