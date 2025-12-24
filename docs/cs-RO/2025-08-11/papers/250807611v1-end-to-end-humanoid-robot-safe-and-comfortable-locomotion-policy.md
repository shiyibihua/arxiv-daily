---
layout: default
title: End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy
---

# End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07611" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07611v1</a>
  <a href="https://arxiv.org/pdf/2508.07611.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07611v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07611v1', 'End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zifan Wang, Xun Yang, Jianzhuang Zhao, Jiaming Zhou, Teli Ma, Ziyao Gao, Arash Ajoudani, Junwei Liang

**分类**: cs.RO

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出端到端的人形机器人安全舒适的运动策略以解决复杂环境导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `安全导航` `强化学习` `LiDAR感知` `人机交互` `控制障碍函数` `约束马尔可夫决策过程` `运动策略`

## 📋 核心要点

1. 现有的强化学习方法在复杂环境中导航时，往往缺乏环境感知能力，导致安全性和效率不足。
2. 本文提出了一种端到端的运动策略，利用LiDAR点云数据直接生成电机指令，并通过CMDP框架强化安全性。
3. 实验结果表明，该方法在物理人形机器人上实现了成功的模拟到现实转移，展现出优越的导航能力。

## 📝 摘要（中文）

人形机器人在非结构化的人类环境中的部署需要超越简单的运动能力，具备稳健的感知、可证明的安全性和社会意识行为。现有的强化学习方法常常受到缺乏环境意识的盲目控制器或无法感知复杂三维障碍的视觉系统的限制。本文提出了一种端到端的运动策略，直接将原始的时空LiDAR点云映射为电机指令，从而实现复杂动态场景中的稳健导航。我们将控制问题形式化为约束马尔可夫决策过程（CMDP），以正式区分安全性与任务目标。我们的关键贡献是将控制障碍函数（CBFs）的原则转化为CMDP中的成本，从而允许无模型的惩罚性近端策略优化（P3O）在训练过程中强制执行安全约束。此外，我们引入了一组基于人机交互研究的舒适奖励，以促进平滑、可预测和不具侵扰性的运动。我们通过成功将框架转移到物理人形机器人上，展示了其在静态和动态三维障碍物周围的敏捷和安全导航能力。

## 🔬 方法详解

**问题定义**：本文旨在解决人形机器人在复杂动态环境中导航的安全性和舒适性问题。现有方法往往依赖于盲目控制或有限的视觉感知，无法有效应对三维障碍物的挑战。

**核心思路**：我们提出了一种端到端的运动策略，通过将时空LiDAR点云直接映射为电机指令，结合CMDP框架来确保安全性与任务目标的分离。

**技术框架**：整体架构包括数据采集模块（LiDAR点云）、控制模块（CMDP框架）、以及训练模块（P3O算法），通过这些模块实现从感知到运动指令的完整流程。

**关键创新**：本研究的创新在于将控制障碍函数的原则引入CMDP中，以成本形式实现安全约束的强制执行，这在现有方法中尚属首次。

**关键设计**：在设计中，我们设置了舒适奖励机制，基于人机交互研究，鼓励机器人产生平滑和可预测的运动。此外，P3O算法的损失函数也进行了特别设计，以平衡安全性和任务完成度。

## 📊 实验亮点

实验结果显示，所提出的框架在物理人形机器人上成功实现了敏捷和安全的导航，能够有效避开静态和动态障碍物。与基线方法相比，导航成功率显著提高，且运动过程中的舒适性得到了增强。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人以及人机协作系统等，能够在复杂和动态的环境中安全有效地执行任务。未来，该方法有望推动人形机器人在日常生活中的广泛应用，提高人机交互的舒适性和安全性。

## 📄 摘要（原文）

> The deployment of humanoid robots in unstructured, human-centric environments requires navigation capabilities that extend beyond simple locomotion to include robust perception, provable safety, and socially aware behavior. Current reinforcement learning approaches are often limited by blind controllers that lack environmental awareness or by vision-based systems that fail to perceive complex 3D obstacles. In this work, we present an end-to-end locomotion policy that directly maps raw, spatio-temporal LiDAR point clouds to motor commands, enabling robust navigation in cluttered dynamic scenes. We formulate the control problem as a Constrained Markov Decision Process (CMDP) to formally separate safety from task objectives. Our key contribution is a novel methodology that translates the principles of Control Barrier Functions (CBFs) into costs within the CMDP, allowing a model-free Penalized Proximal Policy Optimization (P3O) to enforce safety constraints during training. Furthermore, we introduce a set of comfort-oriented rewards, grounded in human-robot interaction research, to promote motions that are smooth, predictable, and less intrusive. We demonstrate the efficacy of our framework through a successful sim-to-real transfer to a physical humanoid robot, which exhibits agile and safe navigation around both static and dynamic 3D obstacles.

