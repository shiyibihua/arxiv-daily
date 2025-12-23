---
layout: default
title: Self driving algorithm for an active four wheel drive racecar
---

# Self driving algorithm for an active four wheel drive racecar

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06077" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06077v1</a>
  <a href="https://arxiv.org/pdf/2506.06077.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06077v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06077v1', 'Self driving algorithm for an active four wheel drive racecar')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gergely Bari, Laszlo Palkovics

**分类**: cs.RO

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出深度强化学习算法以优化四轮驱动赛车的自动驾驶控制**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `四轮驱动` `自动驾驶` `车辆动力学` `近端策略优化` `赛车控制` `智能交通`

## 📋 核心要点

1. 核心问题：现有的车辆动力学控制方法依赖复杂的物理模型，难以在极限操控条件下实现最佳性能。
2. 方法要点：本研究采用深度强化学习，利用PPO算法训练智能体，直接映射车辆状态到控制命令，简化了传统控制逻辑。
3. 实验或效果：实验结果显示，智能体能够动态优化轮子扭矩分配，提升操控性并在圈速上与传统控制器相媲美。

## 📝 摘要（中文）

在控制自主车辆于极限操控条件下，尤其是电动四轮驱动（A4WD）系统中，存在显著挑战。传统的车辆动力学控制（VDC）方法依赖复杂的物理模型，而本研究探索了深度强化学习（DRL）以开发统一的高性能控制器。我们采用近端策略优化（PPO）算法训练智能体，以在模拟赛车（TORCS）中实现最佳圈速。智能体学习了一种端到端策略，直接将车辆状态映射为转向角命令和四个轮子的独立扭矩命令。实验结果表明，强化学习智能体能够动态优化轮子扭矩分配，提升操控性并减轻车辆的固有推头现象，展示了DRL在复杂车辆动力学中的适应性控制系统的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决在极限操控条件下，如何有效控制电动四轮驱动赛车的问题。现有的车辆动力学控制方法通常依赖复杂的物理模型，难以适应快速变化的驾驶环境，导致性能不足。

**核心思路**：本研究的核心思路是采用深度强化学习（DRL）来开发一个高性能的控制器。通过使用近端策略优化（PPO）算法，智能体能够学习如何将车辆状态（如速度、加速度和偏航率）直接映射为转向角和独立的轮子扭矩命令，从而简化了传统的控制逻辑。

**技术框架**：整体架构包括一个模拟环境（TORCS），在该环境中训练智能体。智能体通过与环境的交互，学习到最佳的控制策略。主要模块包括状态感知、策略学习和控制输出。

**关键创新**：本研究的关键创新在于智能体能够学习到一种端到端的控制策略，绕过了传统的踏板输入和显式的扭矩矢量控制算法。这种方法使得智能体能够隐式学习A4WD控制逻辑，从而在性能和稳定性上达到更高水平。

**关键设计**：在训练过程中，采用了PPO算法作为主要的强化学习策略，设置了适当的奖励函数以鼓励智能体优化圈速。同时，网络结构设计为深度神经网络，以处理复杂的状态输入，并输出相应的控制命令。具体的参数设置和损失函数设计在实验中经过多次调优，以确保学习效果的最大化。

## 📊 实验亮点

实验结果表明，强化学习智能体在动态优化轮子扭矩分配方面表现出色，能够有效减轻车辆的推头现象。与传统的物理基础A4WD控制器相比，智能体在圈速上具有竞争力，展示了在极限操控条件下的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括赛车运动和日常驾驶安全。通过实现高效的自动驾驶控制，能够在极限操控条件下提升车辆的性能和稳定性，进而为未来的智能交通系统提供技术支持。随着技术的进步，该方法有望在更广泛的自动驾驶场景中得到应用，提升驾驶安全性和效率。

## 📄 摘要（原文）

> Controlling autonomous vehicles at their handling limits is a significant challenge, particularly for electric vehicles with active four wheel drive (A4WD) systems offering independent wheel torque control. While traditional Vehicle Dynamics Control (VDC) methods use complex physics-based models, this study explores Deep Reinforcement Learning (DRL) to develop a unified, high-performance controller. We employ the Proximal Policy Optimization (PPO) algorithm to train an agent for optimal lap times in a simulated racecar (TORCS) at the tire grip limit. Critically, the agent learns an end-to-end policy that directly maps vehicle states, like velocities, accelerations, and yaw rate, to a steering angle command and independent torque commands for each of the four wheels. This formulation bypasses conventional pedal inputs and explicit torque vectoring algorithms, allowing the agent to implicitly learn the A4WD control logic needed for maximizing performance and stability. Simulation results demonstrate the RL agent learns sophisticated strategies, dynamically optimizing wheel torque distribution corner-by-corner to enhance handling and mitigate the vehicle's inherent understeer. The learned behaviors mimic and, in aspects of grip utilization, potentially surpass traditional physics-based A4WD controllers while achieving competitive lap times. This research underscores DRL's potential to create adaptive control systems for complex vehicle dynamics, suggesting RL is a potent alternative for advancing autonomous driving in demanding, grip-limited scenarios for racing and road safety.

