---
layout: default
title: Zero-shot Whole-Body Manipulation with a Large-Scale Soft Robotic Torso via Guided Reinforcement Learning
---

# Zero-shot Whole-Body Manipulation with a Large-Scale Soft Robotic Torso via Guided Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23556" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23556v1</a>
  <a href="https://arxiv.org/pdf/2509.23556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23556v1', 'Zero-shot Whole-Body Manipulation with a Large-Scale Soft Robotic Torso via Guided Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Curtis C. Johnson, Carlo Alessi, Egidio Falotico, Marc D. Killpack

**分类**: cs.RO

**发布日期**: 2025-09-28

**备注**: Submitted to IEEE Transactions on Robotics for review

---

## 💡 一句话要点

**基于引导强化学习的大型软体机器人零样本全身操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `软体机器人` `全身操作` `强化学习` `零样本迁移` `运动原语`

## 📋 核心要点

1. 软体机器人全身操作在处理大型或异形物体时具有优势，但其不确定性给控制带来挑战。
2. 论文提出一种基于快速仿真的引导强化学习方法，实现软体机器人全身操作策略的零样本迁移。
3. 实验表明，该方法在真实机器人上实现了88%的成功率，并展现了策略的自适应性和鲁棒性。

## 📝 摘要（中文）

本文提出了一种基于引导强化学习的零样本全身操作方法，用于控制大型软体机器人。软体机器人擅长接触丰富的操作任务，但其运动学和动力学的不确定性给仿真和控制带来了挑战。本文利用MuJoCo构建了单线程上可达350倍实时速度的仿真环境，并详细分析了仿真速度和精度之间的权衡。实验结果表明，该方法成功地将学习到的全身操作策略零样本迁移到Baloo硬件平台上，成功率达到88%。引导强化学习对于实现稳定的全身操作策略至关重要。分析表明，学习到的策略并非简单模仿运动原语，而是表现出有益的反应行为，例如重新抓取和扰动恢复。与开环基线相比，该策略在扰动下也表现出积极的过度校正。据我们所知，这是首次在大型平台（10公斤负载）上使用两个连续软臂进行强力的六自由度全身操作，并实现零样本策略迁移。

## 🔬 方法详解

**问题定义**：现有方法难以有效控制软体机器人进行全身操作，主要痛点在于软体机器人的高维度、非线性以及运动学和动力学的不确定性，导致仿真和控制策略设计困难。传统的奖励函数设计难以引导强化学习算法学习到稳定的全身操作策略。

**核心思路**：论文的核心思路是利用快速且相对精确的仿真环境，结合引导强化学习，训练出能够在真实环境中零样本迁移的全身操作策略。通过运动原语引导强化学习，克服了传统奖励函数设计的困难，提高了策略的稳定性和泛化能力。

**技术框架**：整体框架包括三个主要部分：1) 基于MuJoCo的快速软体机器人仿真环境；2) 运动原语引导的强化学习算法；3) 零样本策略迁移到真实机器人。首先，在仿真环境中，利用运动原语生成初始轨迹，然后使用强化学习算法优化策略，最后将学习到的策略直接部署到真实机器人上。

**关键创新**：最重要的技术创新点在于利用运动原语引导强化学习，克服了传统奖励函数设计的困难，提高了策略的稳定性和泛化能力。此外，该方法实现了大型软体机器人全身操作策略的零样本迁移，减少了真实环境中的训练成本。

**关键设计**：仿真环境的关键设计在于平衡仿真速度和精度，选择合适的模型参数和积分方法。强化学习算法的关键设计在于运动原语的选择和奖励函数的设计，运动原语需要能够提供合理的初始轨迹，奖励函数需要能够引导策略学习到期望的行为。具体参数设置未知。

## 📊 实验亮点

实验结果表明，该方法成功地将学习到的全身操作策略零样本迁移到Baloo硬件平台上，成功率达到88%。与传统的奖励函数设计方法相比，引导强化学习能够更有效地学习到稳定的全身操作策略。此外，学习到的策略展现出良好的自适应性和鲁棒性，能够应对环境中的扰动。

## 🎯 应用场景

该研究成果可应用于物流、仓储、医疗等领域，尤其是在需要处理大型、重型或异形物体的场景中。例如，在物流领域，软体机器人可以利用全身操作搬运大型包裹；在医疗领域，可以辅助医生进行手术操作。该研究为软体机器人在复杂环境中的应用提供了新的解决方案。

## 📄 摘要（原文）

> Whole-body manipulation is a powerful yet underexplored approach that enables robots to interact with large, heavy, or awkward objects using more than just their end-effectors. Soft robots, with their inherent passive compliance, are particularly well-suited for such contact-rich manipulation tasks, but their uncertainties in kinematics and dynamics pose significant challenges for simulation and control. In this work, we address this challenge with a simulation that can run up to 350x real time on a single thread in MuJoCo and provide a detailed analysis of the critical tradeoffs between speed and accuracy for this simulation. Using this framework, we demonstrate a successful zero-shot sim-to-real transfer of a learned whole-body manipulation policy, achieving an 88% success rate on the Baloo hardware platform. We show that guiding RL with a simple motion primitive is critical to this success where standard reward shaping methods struggled to produce a stable and successful policy for whole-body manipulation. Furthermore, our analysis reveals that the learned policy does not simply mimic the motion primitive. It exhibits beneficial reactive behavior, such as re-grasping and perturbation recovery. We analyze and contrast this learned policy against an open-loop baseline to show that the policy can also exhibit aggressive over-corrections under perturbation. To our knowledge, this is the first demonstration of forceful, six-DoF whole-body manipulation using two continuum soft arms on a large-scale platform (10 kg payloads), with zero-shot policy transfer.

