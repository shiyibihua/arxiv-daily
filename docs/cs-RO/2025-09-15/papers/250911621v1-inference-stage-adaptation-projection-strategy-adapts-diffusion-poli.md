---
layout: default
title: Inference-stage Adaptation-projection Strategy Adapts Diffusion Policy to Cross-manipulators Scenarios
---

# Inference-stage Adaptation-projection Strategy Adapts Diffusion Policy to Cross-manipulators Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11621" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11621v1</a>
  <a href="https://arxiv.org/pdf/2509.11621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11621v1', 'Inference-stage Adaptation-projection Strategy Adapts Diffusion Policy to Cross-manipulators Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangtong Yao, Yirui Zhou, Yuan Meng, Yanwen Liu, Liangyu Dong, Zitao Zhang, Zhenshan Bing, Kai Huang, Fuchun Sun, Alois Knoll

**分类**: cs.RO

**发布日期**: 2025-09-15

**备注**: 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works

---

## 💡 一句话要点

**提出一种推理阶段的自适应-投影策略，使扩散策略适应跨机械臂场景**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散策略` `机器人操作` `跨机械臂` `零样本学习` `自适应控制` `运动学约束` `推理阶段适应`

## 📋 核心要点

1. 现有扩散策略在机器人操作中表现出色，但难以泛化到未见过的机械臂和末端执行器，需要大量数据和重新训练。
2. 提出一种自适应-投影策略，在推理阶段将扩散策略生成的轨迹投影到满足新机械臂和任务约束的空间，实现零样本迁移。
3. 在真实世界的跨机械臂操作任务中验证，包括抓取放置、推和倾倒，结果表明该方法具有很高的成功率和实用性。

## 📝 摘要（中文）

扩散策略是强大的机器人操作视觉运动模型，但它们通常无法泛化到训练中未见过的机械臂或末端执行器，并且难以适应推理时的新任务需求。解决这个问题通常需要为每个新的硬件或任务配置重新收集数据和重新训练策略，成本高昂。为了克服这一点，我们引入了一种自适应-投影策略，使扩散策略能够在完全推理时零样本适应新的机械臂和动态任务设置，而无需任何重新训练。我们的方法首先使用来自基础机械臂的演示在SE(3)空间中训练扩散策略。在在线部署期间，它将策略生成的轨迹投影以满足新硬件和目标施加的运动学和特定于任务的约束。此外，这种投影动态适应物理差异（例如，工具中心点偏移、钳爪宽度）和任务要求（例如，障碍物高度），确保稳健和成功的执行。我们在包括Franka Panda和Kuka iiwa 14在内的多个机械臂上，通过配备各种末端执行器（如柔性夹爪、Robotiq 2F/3F夹爪和各种3D打印设计）的真实世界抓取放置、推和倾倒任务中验证了我们的方法。我们的结果表明，在这些跨机械臂场景中，成功率始终很高，证明了我们的自适应-投影策略的有效性和实用性。代码将在同行评审后发布。

## 🔬 方法详解

**问题定义**：现有基于扩散模型的机器人操作策略，在面对新的机械臂和末端执行器时，需要重新训练，成本高昂。痛点在于缺乏泛化能力和在线适应能力，无法快速部署到新的硬件环境中。

**核心思路**：核心思想是在推理阶段，通过一个自适应-投影模块，将预训练的扩散策略生成的轨迹，投影到新的机械臂和任务约束所定义的空间中。这样，无需重新训练，即可实现零样本的跨机械臂泛化。

**技术框架**：整体框架包含两个主要阶段：1) 离线训练阶段：使用基础机械臂的数据训练一个通用的扩散策略，该策略在SE(3)空间中生成轨迹。2) 在线推理阶段：将扩散策略生成的轨迹输入到自适应-投影模块，该模块根据新机械臂的运动学约束和任务要求，对轨迹进行投影和调整，生成可执行的动作。

**关键创新**：最重要的创新点在于自适应-投影模块，它能够在推理阶段动态地适应新的机械臂和任务约束，而无需重新训练。与现有方法相比，该方法具有更高的效率和灵活性，能够快速部署到新的环境中。

**关键设计**：自适应-投影模块的关键设计包括：1) 运动学约束建模：使用机械臂的运动学模型，将轨迹投影到可达空间。2) 任务约束建模：根据任务要求，例如避障、目标位置等，设计相应的约束条件。3) 优化算法：使用优化算法，例如梯度下降法，求解满足约束条件的轨迹。

## 📊 实验亮点

实验结果表明，该方法在跨机械臂的抓取放置、推和倾倒任务中取得了显著的成功率。例如，在Franka Panda和Kuka iiwa 14等不同机械臂上，配备不同末端执行器，均能实现较高的任务成功率，验证了该方法的有效性和泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于柔性制造、自动化装配、智能物流等领域。通过该方法，机器人可以快速适应不同的工作环境和任务需求，提高生产效率和灵活性。例如，在生产线上，机器人可以根据不同的产品型号自动调整操作策略，实现柔性化生产。

## 📄 摘要（原文）

> Diffusion policies are powerful visuomotor models for robotic manipulation, yet they often fail to generalize to manipulators or end-effectors unseen during training and struggle to accommodate new task requirements at inference time. Addressing this typically requires costly data recollection and policy retraining for each new hardware or task configuration. To overcome this, we introduce an adaptation-projection strategy that enables a diffusion policy to perform zero-shot adaptation to novel manipulators and dynamic task settings, entirely at inference time and without any retraining. Our method first trains a diffusion policy in SE(3) space using demonstrations from a base manipulator. During online deployment, it projects the policy's generated trajectories to satisfy the kinematic and task-specific constraints imposed by the new hardware and objectives. Moreover, this projection dynamically adapts to physical differences (e.g., tool-center-point offsets, jaw widths) and task requirements (e.g., obstacle heights), ensuring robust and successful execution. We validate our approach on real-world pick-and-place, pushing, and pouring tasks across multiple manipulators, including the Franka Panda and Kuka iiwa 14, equipped with a diverse array of end-effectors like flexible grippers, Robotiq 2F/3F grippers, and various 3D-printed designs. Our results demonstrate consistently high success rates in these cross-manipulator scenarios, proving the effectiveness and practicality of our adaptation-projection strategy. The code will be released after peer review.

