---
layout: default
title: LSTM-Based Modeling and Reinforcement Learning Control of a Magnetically Actuated Catheter
---

# LSTM-Based Modeling and Reinforcement Learning Control of a Magnetically Actuated Catheter

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.21063" class="toolbar-btn" target="_blank">📄 arXiv: 2512.21063v1</a>
  <a href="https://arxiv.org/pdf/2512.21063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.21063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.21063v1', 'LSTM-Based Modeling and Reinforcement Learning Control of a Magnetically Actuated Catheter')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arya Rashidinejad Meibodi, Mahbod Gholamali Sinaki, Khalil Alipour

**分类**: eess.SY

**发布日期**: 2025-12-24

**备注**: Presented at the 13th RSI International Conference on Robotics and Mechatronics (ICRoM 2025), Dec. 16-18, 2025, Tehran, Iran

---

## 💡 一句话要点

**提出基于LSTM建模和强化学习控制的磁驱动导管自主导航方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `磁驱动导管` `LSTM网络` `强化学习` `DQN` `Actor-Critic` `自主导航` `微创手术`

## 📋 核心要点

1. 现有磁驱动导管系统难以精确建模其非线性与迟滞特性，限制了自主控制的实现。
2. 利用LSTM网络学习磁驱动导管的复杂动力学模型，为后续强化学习控制提供精确的仿真环境。
3. Actor-critic强化学习控制器在导管路径跟踪任务中表现优于DQN，精度更高，轨迹更平滑。

## 📝 摘要（中文）

本研究提出了一种用于磁驱动导管系统的建模与控制新方法，旨在实现微创介入的自主化。首先，利用长短期记忆（LSTM）神经网络对磁驱动导管系统的非线性及迟滞动力学进行建模。该系统由外部永磁体产生的伺服控制磁场操纵磁性导管。实验数据验证表明，该模型的均方根误差（RMSE）为0.42毫米，且99.8%的预测值在3毫米范围内，证明其是一个可靠的替代模型。该LSTM模型使得强化学习（RL）智能体能够被训练来控制系统，避免损坏真实设备，并有可能在物理系统上进行后续微调。我们实现了深度Q网络（DQN）和actor-critic两种RL控制器，并首先对它们的调节性能进行了比较，随后比较了导管尖端沿直线和半正弦路径的路径跟踪性能。结果表明，actor-critic算法优于DQN，在调节和路径跟踪方面都提供了更高的精度、更快的性能和更小的误差，以及更平滑的轨迹（采样率为10赫兹）。由于其连续动作空间，这种性能非常适合动态导航任务，例如在实际应用中导航弯曲的血管结构。

## 🔬 方法详解

**问题定义**：磁驱动导管系统在微创手术中具有重要应用，但其非线性、迟滞的动力学特性使得精确建模和控制变得困难。传统方法难以有效应对这些挑战，限制了导管的自主导航能力，增加了手术风险。

**核心思路**：本研究的核心思路是利用LSTM神经网络学习磁驱动导管系统的动力学模型，并将其作为强化学习的仿真环境。通过在仿真环境中训练强化学习智能体，可以避免在真实系统上直接训练可能造成的损坏，并最终实现导管的精确自主控制。

**技术框架**：该方法包含两个主要阶段：1) 基于LSTM的系统建模：利用实验数据训练LSTM网络，使其能够准确预测导管在不同磁场作用下的运动状态。2) 强化学习控制：使用训练好的LSTM模型作为仿真环境，训练DQN和actor-critic两种强化学习智能体，使其能够控制磁场，从而实现导管的精确导航。

**关键创新**：该方法的关键创新在于将LSTM神经网络与强化学习相结合，利用LSTM强大的建模能力为强化学习提供精确的仿真环境，从而避免了在真实系统上直接训练的风险。此外，对比了DQN和actor-critic两种强化学习算法在导管控制中的性能，发现actor-critic算法更适合连续动作空间的控制任务。

**关键设计**：LSTM网络结构的选择和训练数据的采集是关键。强化学习中，奖励函数的设计直接影响智能体的学习效果。Actor-critic算法采用连续动作空间，更适合控制磁场的连续变化。DQN算法则采用离散动作空间，需要进行离散化处理。实验中，采样率为10Hz，用于控制导管的运动。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21063v1/Schematic.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21063v1/LSTM.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.21063v1/Overview2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于LSTM建模的强化学习控制方法能够有效控制磁驱动导管。Actor-critic算法在直线和半正弦路径跟踪任务中均优于DQN算法，具有更高的精度和更平滑的轨迹。LSTM模型对导管运动的预测均方根误差（RMSE）为0.42毫米，且99.8%的预测值在3毫米范围内。

## 🎯 应用场景

该研究成果可应用于微创手术领域，实现磁驱动导管的自主导航，减少医生操作负担，提高手术精度和安全性。未来可进一步扩展到更复杂的血管结构导航，以及药物递送等应用，具有重要的临床应用价值和商业前景。

## 📄 摘要（原文）

> Autonomous magnetic catheter systems are emerging as a promising approach for the future of minimally invasive interventions. This study presents a novel approach that begins by modeling the nonlinear and hysteretic dynamics of a magnetically actuated catheter system, consists of a magnetic catheter manipulated by servo-controlled magnetic fields generated by two external permanent magnets, and its complex behavior is captured using a Long Short-Term Memory (LSTM) neural network. This model validated against experimental setup's data with a root mean square error (RMSE) of 0.42 mm and 99.8% coverage within 3 mm, establishing it as a reliable surrogate model. This LSTM enables the training of Reinforcement Learning (RL) agents for controlling the system and avoiding damage to the real setup, with the potential for subsequent fine-tuning on the physical system. We implemented Deep Q-Network (DQN) and actor-critic RL controllers, comparing these two agents first for regulation and subsequently for path following along linear and half-sinusoidal paths for the catheter tip. The actor-critic outperforms DQN, offering greater accuracy and faster performance with less error, along with smoother trajectories at a 10 Hz sampling rate, in both regulation and path following compared to the DQN controller. This performance, due to the continuous action space, suits dynamic navigation tasks like navigating curved vascular structures for practical applications.

