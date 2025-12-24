---
layout: default
title: Tree-Guided Diffusion Planner
---

# Tree-Guided Diffusion Planner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21800" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21800v2</a>
  <a href="https://arxiv.org/pdf/2508.21800.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21800v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21800v2', 'Tree-Guided Diffusion Planner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyeonseong Jeon, Cheolhong Min, Jaesik Park

**分类**: cs.AI, cs.RO

**发布日期**: 2025-08-29 (更新: 2025-11-09)

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出树导向扩散规划器以解决非凸优化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `扩散模型` `规划算法` `树搜索` `机器人控制` `零-shot学习` `多目标优化` `轨迹生成`

## 📋 核心要点

1. 现有的规划方法在处理非凸目标和复杂约束时效果不佳，限制了其在实际应用中的灵活性。
2. 本文提出的树导向扩散规划器（TDP）通过双层采样过程实现了探索与利用的平衡，支持零-shot测试时规划。
3. TDP在迷宫金块采集、机器人手臂块操作和AntMaze多目标探索等任务中表现优异，超越了现有的最先进方法。

## 📝 摘要（中文）

使用预训练扩散模型进行规划已成为解决测试时引导控制问题的一种有前景的方法。然而，标准的梯度引导在非凸目标、非可微约束和多奖励结构的实际场景中效果显著降低。为此，本文提出了一种零-shot测试时规划框架——树导向扩散规划器（TDP），通过结构化轨迹生成平衡探索与利用。TDP将测试时规划视为树搜索问题，采用双层采样过程生成多样的父轨迹，并通过快速条件去噪精炼子轨迹。TDP在三个多样化任务上进行评估，均优于现有最先进的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在非凸、非可微的奖励结构下进行有效规划的问题。现有的梯度引导方法在这些复杂场景中表现不佳，且需要特定任务的训练，限制了其灵活性和零-shot泛化能力。

**核心思路**：论文提出的TDP通过将测试时规划视为树搜索问题，采用双层采样策略，首先生成多样的父轨迹以促进广泛探索，然后根据任务目标快速精炼子轨迹，从而实现有效的规划。

**技术框架**：TDP的整体架构包括两个主要阶段：第一阶段是通过无训练的粒子引导生成多样的父轨迹，第二阶段是通过条件去噪快速优化子轨迹。该框架利用预训练模型和测试时奖励信号，避免了对特定任务的依赖。

**关键创新**：TDP的核心创新在于其双层采样过程，能够在扩展的解空间中探索多样的轨迹区域，并利用梯度信息进行优化。这一方法显著克服了传统梯度引导的局限性。

**关键设计**：在设计中，TDP采用了无训练的粒子引导机制，确保了探索的多样性，同时在条件去噪阶段使用了与任务目标相结合的快速优化策略，以提高效率和效果。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在实验中，TDP在迷宫金块采集、机器人手臂块操作和AntMaze多目标探索等任务上均表现优异， consistently outperforming state-of-the-art approaches，提升幅度达到XX%。具体性能数据和对比基线在论文中详细列出。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动化规划、智能交通系统等。通过提供一种灵活的零-shot规划框架，TDP能够在多种复杂环境中实现高效的决策制定，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Planning with pretrained diffusion models has emerged as a promising approach for solving test-time guided control problems. Standard gradient guidance typically performs optimally under convex, differentiable reward landscapes. However, it shows substantially reduced effectiveness in real-world scenarios with non-convex objectives, non-differentiable constraints, and multi-reward structures. Furthermore, recent supervised planning approaches require task-specific training or value estimators, which limits test-time flexibility and zero-shot generalization. We propose a Tree-guided Diffusion Planner (TDP), a zero-shot test-time planning framework that balances exploration and exploitation through structured trajectory generation. We frame test-time planning as a tree search problem using a bi-level sampling process: (1) diverse parent trajectories are produced via training-free particle guidance to encourage broad exploration, and (2) sub-trajectories are refined through fast conditional denoising guided by task objectives. TDP addresses the limitations of gradient guidance by exploring diverse trajectory regions and harnessing gradient information across this expanded solution space using only pretrained models and test-time reward signals. We evaluate TDP on three diverse tasks: maze gold-picking, robot arm block manipulation, and AntMaze multi-goal exploration. TDP consistently outperforms state-of-the-art approaches on all tasks. The project page can be found at: https://tree-diffusion-planner.github.io.

