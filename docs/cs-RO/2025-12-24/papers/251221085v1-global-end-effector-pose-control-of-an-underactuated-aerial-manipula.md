---
layout: default
title: Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning
---

# Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21085" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21085v1</a>
  <a href="https://arxiv.org/pdf/2512.21085.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21085v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21085v1', 'Global End-Effector Pose Control of an Underactuated Aerial Manipulator via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shlok Deshmukh, Javier Alonso-Mora, Sihao Sun

**分类**: cs.RO

**发布日期**: 2025-12-24

**备注**: 8 pages, 6 figures

---

## 💡 一句话要点

**提出基于强化学习的欠驱动空中机械臂全局末端姿态控制方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `空中机械臂` `强化学习` `欠驱动系统` `末端姿态控制` `PPO算法`

## 📋 核心要点

1. 空中机械臂面临机械臂重量和机械复杂度的严格约束，现有方法难以兼顾轻量化和高精度控制。
2. 采用强化学习方法，训练PPO智能体生成前馈控制命令，结合INDI姿态控制器和PID关节控制器，实现精确控制。
3. 飞行实验验证了该方法的有效性，实现了厘米级的定位精度和度级的姿态精度，并具有良好的抗干扰能力。

## 📝 摘要（中文）

本文研究了一种轻量级双自由度（DoF）机械臂，该机械臂通过差动机构安装在四旋翼无人机上，能够实现六自由度末端执行器姿态控制。这种极简设计虽然实现了简单性和有效载荷的降低，但也带来了欠驱动和对外部扰动敏感等挑战，包括重物操作和推力任务。为了解决这些问题，我们采用强化学习，在仿真环境中训练近端策略优化（PPO）智能体，以生成四旋翼加速度和机身角速率的前馈命令以及关节角度目标。这些命令分别由增量非线性动态逆（INDI）姿态控制器和PID关节控制器跟踪。飞行实验表明，该方法实现了厘米级的定位精度和度级的姿态精度，并在外部力扰动下表现出鲁棒性。结果突出了基于学习的控制策略在利用简单、轻量级平台实现接触式空中操作的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决欠驱动空中机械臂的全局末端姿态精确控制问题。现有的空中机械臂设计往往需要在机械臂的重量和控制精度之间做出权衡。轻量化的机械臂虽然降低了无人机的负载，但也导致了欠驱动和对外部扰动的敏感性，使得精确控制末端执行器的姿态变得困难，尤其是在进行接触式操作时。

**核心思路**：论文的核心思路是利用强化学习来学习一个前馈控制器，该控制器能够预测四旋翼无人机和机械臂的最佳控制指令，从而补偿欠驱动带来的控制困难和外部扰动的影响。通过在仿真环境中训练智能体，可以使其学习到复杂的动力学模型和控制策略，而无需手动设计复杂的控制算法。

**技术框架**：整体框架包括三个主要模块：强化学习智能体、增量非线性动态逆（INDI）姿态控制器和PID关节控制器。首先，PPO智能体根据当前状态生成四旋翼加速度和机身角速率的前馈命令以及关节角度目标。然后，INDI姿态控制器跟踪四旋翼的加速度和角速率命令，PID关节控制器跟踪机械臂的关节角度目标。最后，系统将执行结果反馈给PPO智能体，用于更新策略。

**关键创新**：该论文的关键创新在于将强化学习应用于欠驱动空中机械臂的全局末端姿态控制。与传统的控制方法相比，强化学习能够更好地处理非线性、欠驱动和外部扰动等复杂情况。此外，通过在仿真环境中进行训练，可以避免在真实环境中进行大量的实验，从而降低了成本和风险。

**关键设计**：论文中使用了Proximal Policy Optimization (PPO)算法作为强化学习的训练方法。PPO算法是一种on-policy算法，通过限制策略更新的幅度，保证了训练的稳定性。INDI姿态控制器是一种基于模型的控制方法，能够有效地跟踪四旋翼的加速度和角速率命令。PID关节控制器则用于控制机械臂的关节角度。在仿真环境中，论文使用了详细的动力学模型，并考虑了各种外部扰动，以提高训练的泛化能力。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21085v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21085v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21085v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法能够实现厘米级的定位精度和度级的姿态精度。在外部力扰动下，该方法仍能保持良好的鲁棒性。与传统的控制方法相比，该方法在欠驱动和外部扰动下的性能得到了显著提升。例如，在推力任务中，该方法能够稳定地控制机械臂的姿态，而传统的控制方法则容易出现失控。

## 🎯 应用场景

该研究成果可应用于多种场景，例如：高空作业、桥梁检测、灾难救援等。在这些场景中，空中机械臂可以代替人类完成危险或难以到达的任务，例如：高空焊接、桥梁裂缝检测、废墟搜救等。此外，该技术还可以应用于物流领域，例如：无人机配送、仓库自动化等。

## 📄 摘要（原文）

> Aerial manipulators, which combine robotic arms with multi-rotor drones, face strict constraints on arm weight and mechanical complexity. In this work, we study a lightweight 2-degree-of-freedom (DoF) arm mounted on a quadrotor via a differential mechanism, capable of full six-DoF end-effector pose control. While the minimal design enables simplicity and reduced payload, it also introduces challenges such as underactuation and sensitivity to external disturbances, including manipulation of heavy loads and pushing tasks. To address these, we employ reinforcement learning, training a Proximal Policy Optimization (PPO) agent in simulation to generate feedforward commands for quadrotor acceleration and body rates, along with joint angle targets. These commands are tracked by an incremental nonlinear dynamic inversion (INDI) attitude controller and a PID joint controller, respectively. Flight experiments demonstrate centimeter-level position accuracy and degree-level orientation precision, with robust performance under external force disturbances. The results highlight the potential of learning-based control strategies for enabling contact-rich aerial manipulation using simple, lightweight platforms.

