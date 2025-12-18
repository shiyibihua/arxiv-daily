---
layout: default
title: Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks
---

# Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19696" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19696v2</a>
  <a href="https://arxiv.org/pdf/2509.19696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19696v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19696v2', 'Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Noah Geiger, Tamim Asfour, Neville Hogan, Johannes Lachner

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-09-24 (更新: 2025-09-29)

**备注**: 15 pages, 12 figures

---

## 💡 一句话要点

**提出基于扩散模型的阻抗学习框架，用于接触丰富的操作任务**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `扩散模型` `阻抗学习` `接触操作` `机器人控制` `物理人工智能`

## 📋 核心要点

1. 现有学习方法擅长信息域的运动生成，但在能量域的物理交互方面存在不足。
2. 论文提出基于扩散模型的阻抗学习框架，通过重构零力轨迹并估计阻抗参数，实现物理交互。
3. 实验表明，该模型在跑酷和插拔任务中表现出色，实现了高精度和实时控制，代码已开源。

## 📝 摘要（中文）

本文提出了一种基于扩散的阻抗学习框架，该框架结合了信息域的运动生成和能量域的物理交互。该框架使用一个基于Transformer的扩散模型，通过交叉注意力机制关注外部力矩，重构模拟的零力轨迹（sZFT），从而捕捉平移和旋转的任务空间行为。对于旋转，引入了一种基于SLERP的四元数噪声调度器，以确保几何一致性。重构的sZFT随后被传递给一个基于能量的估计器，用于更新刚度和阻尼参数。采用了一种方向性规则，降低非任务轴上的阻抗，同时保持任务方向上的刚性。使用Apple Vision Pro进行遥操作，收集了跑酷场景和机器人辅助治疗任务的训练数据。仅使用数万个样本，该模型就实现了亚毫米级的位置精度和亚度级的旋转精度。其紧凑的模型尺寸实现了KUKA LBR iiwa机器人上的实时扭矩控制和自主刚度调整。该控制器在力和速度限制内实现了平稳的跑酷穿越，并且在没有训练数据集中任何特定于插拔演示的情况下，圆柱形、方形和星形插拔的成功率达到30/30。Transformer扩散模型、机器人控制器和Apple Vision Pro遥操作框架的所有代码均已公开。这些结果标志着物理人工智能的重要一步，将用于物理交互的基于模型的控制与用于轨迹生成的基于学习的方法融合在一起。

## 🔬 方法详解

**问题定义**：现有方法在接触丰富的操作任务中，难以同时兼顾运动生成和物理交互。传统的阻抗控制需要手动调整参数，缺乏任务自适应性。学习方法虽然可以生成运动轨迹，但难以直接控制物理交互过程中的力和力矩。因此，需要一种能够自动学习并适应任务的阻抗控制方法，以实现更鲁棒和高效的接触操作。

**核心思路**：论文的核心思路是将学习方法与阻抗控制相结合。通过扩散模型学习任务的运动轨迹，并利用重构的零力轨迹估计阻抗参数。这种方法能够将任务的运动信息转化为阻抗控制器的参数，从而实现任务自适应的阻抗控制。同时，通过方向性规则调整阻抗参数，提高控制器的稳定性和性能。

**技术框架**：该框架主要包含两个阶段：1) 基于Transformer的扩散模型重构模拟零力轨迹（sZFT）。该模型以外部力矩为输入，通过交叉注意力机制学习任务的运动轨迹。为了保证旋转的几何一致性，引入了基于SLERP的四元数噪声调度器。2) 基于能量的估计器更新刚度和阻尼参数。该估计器以重构的sZFT为输入，估计阻抗参数。同时，采用一种方向性规则，降低非任务轴上的阻抗，同时保持任务方向上的刚性。

**关键创新**：该论文的关键创新在于：1) 将扩散模型应用于阻抗学习，实现了任务自适应的阻抗控制。2) 引入了基于SLERP的四元数噪声调度器，保证了旋转的几何一致性。3) 提出了一种方向性规则，提高了控制器的稳定性和性能。

**关键设计**：Transformer扩散模型采用标准的Transformer架构，并使用交叉注意力机制关注外部力矩。基于SLERP的四元数噪声调度器通过在四元数空间中进行插值，保证了旋转的平滑性和几何一致性。方向性规则通过调整阻抗矩阵的对角线元素，降低非任务轴上的阻抗，同时保持任务方向上的刚性。损失函数包括轨迹重构损失和阻抗参数估计损失。

## 📊 实验亮点

该模型仅使用数万个样本，就实现了亚毫米级的位置精度和亚度级的旋转精度。在KUKA LBR iiwa机器人上实现了实时扭矩控制和自主刚度调整。在跑酷任务中实现了平稳的穿越，并且在没有特定于插拔演示的情况下，圆柱形、方形和星形插拔的成功率达到30/30。

## 🎯 应用场景

该研究成果可应用于各种接触丰富的操作任务，例如机器人装配、医疗康复、人机协作等。通过学习任务的运动轨迹和阻抗参数，机器人可以更好地适应环境变化，实现更鲁棒和高效的操作。该方法还可以用于开发更智能的机器人辅助系统，提高工作效率和安全性。

## 📄 摘要（原文）

> Learning methods excel at motion generation in the information domain but are not primarily designed for physical interaction in the energy domain. Impedance Control shapes physical interaction but requires task-aware tuning by selecting feasible impedance parameters. We present Diffusion-Based Impedance Learning, a framework that combines both domains. A Transformer-based Diffusion Model with cross-attention to external wrenches reconstructs a simulated Zero-Force Trajectory (sZFT). This captures both translational and rotational task-space behavior. For rotations, we introduce a novel SLERP-based quaternion noise scheduler that ensures geometric consistency. The reconstructed sZFT is then passed to an energy-based estimator that updates stiffness and damping parameters. A directional rule is applied that reduces impedance along non task axes while preserving rigidity along task directions. Training data were collected for a parkour scenario and robotic-assisted therapy tasks using teleoperation with Apple Vision Pro. With only tens of thousands of samples, the model achieved sub-millimeter positional accuracy and sub-degree rotational accuracy. Its compact model size enabled real-time torque control and autonomous stiffness adaptation on a KUKA LBR iiwa robot. The controller achieved smooth parkour traversal within force and velocity limits and 30/30 success rates for cylindrical, square, and star peg insertions without any peg-specific demonstrations in the training data set. All code for the Transformer-based Diffusion Model, the robot controller, and the Apple Vision Pro telemanipulation framework is publicly available. These results mark an important step towards Physical AI, fusing model-based control for physical interaction with learning-based methods for trajectory generation.

