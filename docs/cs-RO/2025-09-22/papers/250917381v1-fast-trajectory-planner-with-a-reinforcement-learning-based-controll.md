---
layout: default
title: Fast Trajectory Planner with a Reinforcement Learning-based Controller for Robotic Manipulators
---

# Fast Trajectory Planner with a Reinforcement Learning-based Controller for Robotic Manipulators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17381" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17381v1</a>
  <a href="https://arxiv.org/pdf/2509.17381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17381v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17381v1', 'Fast Trajectory Planner with a Reinforcement Learning-based Controller for Robotic Manipulators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongliang Wang, Hamidreza Kasaei

**分类**: cs.RO

**发布日期**: 2025-09-22

**备注**: Project page available at: https://sites.google.com/view/ftp4rm/home

---

## 💡 一句话要点

**提出基于强化学习控制器的快速轨迹规划器，用于机器人操作臂在复杂环境中进行实时避障。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人操作臂` `轨迹规划` `强化学习` `近端策略优化` `视觉伺服`

## 📋 核心要点

1. 现有运动规划方法在生成机器人操作臂轨迹时，通常需要额外的计算量来求解运动学或动力学方程，效率较低。
2. 该论文提出了一种结合视觉路径规划和强化学习控制的快速轨迹规划系统，在任务空间和关节空间分别进行规划和避障。
3. 通过改进PPO算法，集成动作集成和策略反馈，提升了算法在复杂环境下的避障效率和目标到达精度，并验证了其在仿真和真实环境中的有效性。

## 📝 摘要（中文）

本文针对机器人操作臂在非结构化和复杂环境中生成无碰撞轨迹的难题，提出了一种快速轨迹规划系统。该系统结合了基于视觉的任务空间路径规划和基于强化学习的关节空间避障。首先，利用大规模快速分割模型（FSA）和B样条优化的运动学路径搜索，提出了一种创新的基于视觉的任务空间轨迹规划器。其次，通过集成动作集成（AE）和策略反馈（PF）来增强近端策略优化（PPO）算法，从而显著提高关节空间中目标到达和避障的精度和稳定性。这些PPO增强功能提高了算法在各种机器人任务中的适应性，确保操作臂一致地执行来自第一部分的命令，同时提高避障效率和到达精度。实验结果表明，PPO增强功能以及仿真到仿真（Sim-to-Sim）和仿真到现实（Sim-to-Real）的迁移，有效地提高了复杂场景中模型的鲁棒性和规划器的效率，使机器人能够在受阻环境中执行避障和实时轨迹规划。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人操作臂在复杂、非结构化环境中进行快速、实时的无碰撞轨迹规划问题。现有方法通常计算成本高昂，难以满足实时性要求，并且在复杂环境中鲁棒性不足。

**核心思路**：论文的核心思路是将轨迹规划分解为两个阶段：首先在任务空间利用视觉信息进行全局路径规划，然后在关节空间利用强化学习进行局部避障和轨迹优化。这种分解降低了问题的复杂度，并允许利用强化学习的自适应能力来处理复杂环境。

**技术框架**：该系统包含两个主要模块：1) 基于视觉的任务空间轨迹规划器：利用快速分割模型（FSA）提取环境信息，并结合B样条优化的运动学路径搜索生成初始轨迹。2) 基于强化学习的关节空间控制器：使用改进的近端策略优化（PPO）算法，通过动作集成（AE）和策略反馈（PF）来提高避障和目标到达的精度和稳定性。两个模块协同工作，实现快速、鲁棒的轨迹规划。

**关键创新**：论文的关键创新在于：1) 将视觉信息融入轨迹规划，利用FSA快速提取环境信息。2) 改进PPO算法，通过动作集成和策略反馈显著提升了强化学习控制器的性能。3) 结合任务空间规划和关节空间控制，实现了全局路径规划和局部避障的有效协同。

**关键设计**：在任务空间规划中，使用B样条曲线优化初始路径，保证轨迹的光滑性。在强化学习控制中，动作集成（AE）通过集成多个动作建议来提高探索效率，策略反馈（PF）则利用历史策略信息来稳定训练过程。PPO算法的奖励函数设计考虑了目标到达、避障和动作惩罚等因素，以引导机器人学习期望的行为。

## 📊 实验亮点

实验结果表明，所提出的PPO增强算法在避障效率和目标到达精度方面均优于传统PPO算法。仿真实验验证了该方法在复杂环境下的鲁棒性，并成功实现了从仿真到现实的迁移，证明了其在实际应用中的可行性。具体的性能数据（如成功率、轨迹长度、运行时间等）未在摘要中明确给出，但强调了PPO增强在提升模型鲁棒性和规划器效率方面的有效性。

## 🎯 应用场景

该研究成果可应用于工业机器人、服务机器人等领域，使其能够在复杂、动态的环境中安全、高效地完成任务，例如自动化装配、物流搬运、医疗辅助等。通过结合视觉感知和强化学习控制，机器人能够更好地适应未知环境，提高其智能化水平和应用范围。未来，该方法有望进一步扩展到多机器人协同、人机协作等更复杂的场景。

## 📄 摘要（原文）

> Generating obstacle-free trajectories for robotic manipulators in unstructured and cluttered environments remains a significant challenge. Existing motion planning methods often require additional computational effort to generate the final trajectory by solving kinematic or dynamic equations. This paper highlights the strong potential of model-free reinforcement learning methods over model-based approaches for obstacle-free trajectory planning in joint space. We propose a fast trajectory planning system for manipulators that combines vision-based path planning in task space with reinforcement learning-based obstacle avoidance in joint space. We divide the framework into two key components. The first introduces an innovative vision-based trajectory planner in task space, leveraging the large-scale fast segment anything (FSA) model in conjunction with basis spline (B-spline)-optimized kinodynamic path searching. The second component enhances the proximal policy optimization (PPO) algorithm by integrating action ensembles (AE) and policy feedback (PF), which greatly improve precision and stability in goal-reaching and obstacle avoidance within the joint space. These PPO enhancements increase the algorithm's adaptability across diverse robotic tasks, ensuring consistent execution of commands from the first component by the manipulator, while also enhancing both obstacle avoidance efficiency and reaching accuracy. The experimental results demonstrate the effectiveness of PPO enhancements, as well as simulation-to-simulation (Sim-to-Sim) and simulation-to-reality (Sim-to-Real) transfer, in improving model robustness and planner efficiency in complex scenarios. These enhancements allow the robot to perform obstacle avoidance and real-time trajectory planning in obstructed environments. Project page available at: https://sites.google.com/view/ftp4rm/home

