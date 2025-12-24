---
layout: default
title: Aerobatic maneuvers in insect-scale flapping-wing aerial robots via deep-learned robust tube model predictive control
---

# Aerobatic maneuvers in insect-scale flapping-wing aerial robots via deep-learned robust tube model predictive control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03043" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03043v1</a>
  <a href="https://arxiv.org/pdf/2508.03043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03043v1', 'Aerobatic maneuvers in insect-scale flapping-wing aerial robots via deep-learned robust tube model predictive control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi-Hsuan Hsiao, Andrea Tagliabue, Owen Matteson, Suhan Kim, Tong Zhao, Jonathan P. How, YuFeng Chen

**分类**: cs.RO, cs.LG, eess.SY

**发布日期**: 2025-08-05

**备注**: 27 pages, 26 supplementary pages, 6 main figures, 16 supplementary figures, 1 table

---

## 💡 一句话要点

**通过深度学习鲁棒管道模型预测控制实现昆虫级飞行机器人特技机动**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `昆虫级飞行` `深度学习` `模型预测控制` `鲁棒控制` `飞行机器人` `机动能力` `环境适应性`

## 📋 核心要点

1. 现有的昆虫级飞行机器人在执行高动态机动时受限于硬件能力和环境干扰，无法实现灵活的飞行表现。
2. 论文提出了一种深度学习鲁棒管道模型预测控制器，能够生成激进的飞行轨迹并应对环境的不确定性。
3. 实验表明，机器人在风干扰下仍能执行快速的机动，并在11秒内完成10次连续翻转，展现出显著的性能提升。

## 📝 摘要（中文）

昆虫在飞行中展现出高度灵活的机动能力，如急刹车、快速移动和翻转等。然而，昆虫级飞行机器人在执行这些高动态机动时受到硬件限制和环境干扰的影响，表现不佳。本文提出了一种深度学习鲁棒管道模型预测控制器，能够在750毫克的拍翼机器人上实现昆虫般的飞行灵活性和鲁棒性。该控制器能够在干扰下跟踪激进的飞行轨迹，并通过模仿学习训练出一个两层全连接神经网络，模拟昆虫的飞行控制架构。实验结果显示，该机器人在侧向速度和加速度上分别达到197厘米每秒和11.7米每秒平方，较之前的结果提升了447%和255%。

## 🔬 方法详解

**问题定义**：本文旨在解决昆虫级飞行机器人在执行高动态机动时的性能不足，现有方法在面对环境干扰和硬件限制时表现不佳。

**核心思路**：提出了一种深度学习鲁棒管道模型预测控制器，通过模仿昆虫的飞行控制机制，生成激进的飞行轨迹并提高反馈控制的频率。

**技术框架**：整体架构包括深度学习模块和模型预测控制模块，深度学习模块通过模仿学习训练神经网络，模型预测控制模块则用于实时跟踪飞行轨迹。

**关键创新**：最重要的创新在于结合深度学习与模型预测控制，形成了一种新的控制策略，能够在不确定环境中保持高效的飞行表现。

**关键设计**：采用两层全连接神经网络作为控制器，设计了适应性损失函数以优化控制性能，并通过高频反馈机制确保实时响应。

## 📊 实验亮点

实验结果显示，机器人在侧向速度和加速度上分别达到197厘米每秒和11.7米每秒平方，较之前的结果提升了447%和255%。此外，机器人在160厘米每秒的风干扰下仍能执行快速的机动，并在11秒内完成10次连续翻转，展现出卓越的飞行灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括无人机、农业监测、环境监测等，能够为小型飞行器的自主飞行和复杂环境中的机动能力提供新的解决方案。未来可能推动智能飞行器在动态环境中的自主导航和任务执行能力的提升。

## 📄 摘要（原文）

> Aerial insects exhibit highly agile maneuvers such as sharp braking, saccades, and body flips under disturbance. In contrast, insect-scale aerial robots are limited to tracking non-aggressive trajectories with small body acceleration. This performance gap is contributed by a combination of low robot inertia, fast dynamics, uncertainty in flapping-wing aerodynamics, and high susceptibility to environmental disturbance. Executing highly dynamic maneuvers requires the generation of aggressive flight trajectories that push against the hardware limit and a high-rate feedback controller that accounts for model and environmental uncertainty. Here, through designing a deep-learned robust tube model predictive controller, we showcase insect-like flight agility and robustness in a 750-millgram flapping-wing robot. Our model predictive controller can track aggressive flight trajectories under disturbance. To achieve a high feedback rate in a compute-constrained real-time system, we design imitation learning methods to train a two-layer, fully connected neural network, which resembles insect flight control architecture consisting of central nervous system and motor neurons. Our robot demonstrates insect-like saccade movements with lateral speed and acceleration of 197 centimeters per second and 11.7 meters per second square, representing 447$\%$ and 255$\%$ improvement over prior results. The robot can also perform saccade maneuvers under 160 centimeters per second wind disturbance and large command-to-force mapping errors. Furthermore, it performs 10 consecutive body flips in 11 seconds - the most challenging maneuver among sub-gram flyers. These results represent a milestone in achieving insect-scale flight agility and inspire future investigations on sensing and compute autonomy.

