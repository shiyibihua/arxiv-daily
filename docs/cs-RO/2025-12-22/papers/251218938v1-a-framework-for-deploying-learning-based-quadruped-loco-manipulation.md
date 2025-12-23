---
layout: default
title: A Framework for Deploying Learning-based Quadruped Loco-Manipulation
---

# A Framework for Deploying Learning-based Quadruped Loco-Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.18938" class="toolbar-btn" target="_blank">📄 arXiv: 2512.18938v1</a>
  <a href="https://arxiv.org/pdf/2512.18938.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.18938v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.18938v1', 'A Framework for Deploying Learning-based Quadruped Loco-Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yadong Liu, Jianwei Liu, He Liang, Dimitrios Kanoulas

**分类**: cs.RO

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出基于强化学习的四足机器人灵巧操作部署框架，解决仿真到现实迁移难题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `四足机器人` `灵巧操作` `强化学习` `仿真到现实` `机器人控制`

## 📋 核心要点

1. 四足机器人灵巧操作控制复杂，现有强化学习框架难以在真实硬件上复现。
2. 提出一个开放的pipeline，统一sim-to-sim和sim-to-real迁移，实现策略在不同仿真器和真实机器人上的部署。
3. 实验表明，协调的全身控制扩展了操作范围，并改善了物体拾取操作的性能。

## 📝 摘要（中文）

四足移动操作机器人具有敏捷操作的巨大潜力，但其控制和从仿真到现实的可靠迁移仍然困难。强化学习(RL)在全身控制方面显示出希望，但大多数框架是专有的，难以在真实硬件上重现。本文提出了一个开放的pipeline，用于在配备Z1机械臂的宇树B1四足机器人上训练、基准测试和部署基于RL的控制器。该框架通过ROS统一了sim-to-sim和sim-to-real的迁移，重新实现了在Isaac Gym中训练的策略，通过硬件抽象层将其扩展到MuJoCo，并在物理硬件上部署相同的控制器。Sim-to-sim实验揭示了Isaac Gym和MuJoCo接触模型之间的差异，这些差异影响了策略行为，而真实世界的遥操作物体拾取试验表明，协调的全身控制扩展了范围，并改善了对浮动基线操作的改进。该pipeline为开发和分析基于RL的loco-manipulation控制器提供了一个透明、可复现的基础，并将开源发布以支持未来的研究。

## 🔬 方法详解

**问题定义**：四足机器人灵巧操作的控制策略设计复杂，尤其是在将仿真环境中训练的策略迁移到真实机器人时，由于仿真环境与真实环境的差异，往往难以保证控制策略的有效性。现有的强化学习框架大多是专有的，缺乏透明性和可复现性，阻碍了相关研究的进展。

**核心思路**：本文的核心思路是构建一个开放、可复现的pipeline，通过ROS统一sim-to-sim和sim-to-real的迁移，使得在仿真环境中训练的策略能够顺利地部署到真实机器人上。通过硬件抽象层，策略可以方便地在不同的仿真器（Isaac Gym和MuJoCo）之间切换，从而更好地适应不同的仿真环境。

**技术框架**：该框架包含以下几个主要模块：1) 基于Isaac Gym的强化学习训练环境；2) 基于ROS的通信接口，用于连接仿真环境和真实机器人；3) 硬件抽象层，用于屏蔽不同仿真器和硬件平台的差异；4) 基于MuJoCo的仿真环境，用于验证策略的有效性；5) 宇树B1四足机器人平台，用于真实环境的部署和测试。整体流程是从Isaac Gym训练策略，通过ROS和硬件抽象层迁移到MuJoCo，最后部署到真实机器人。

**关键创新**：该论文的关键创新在于构建了一个开放、可复现的四足机器人灵巧操作部署框架，该框架能够有效地解决仿真到现实的迁移问题。通过统一的接口和硬件抽象层，策略可以在不同的仿真环境和真实机器人之间无缝切换，大大降低了开发和部署的难度。

**关键设计**：论文中使用了强化学习算法来训练四足机器人的控制策略。具体的参数设置和网络结构在论文中没有详细描述，但可以推测使用了常见的Actor-Critic算法，并针对四足机器人的特点进行了优化。损失函数的设计可能包括奖励函数，用于鼓励机器人完成特定的任务，例如移动到目标位置或拾取物体。硬件抽象层屏蔽了不同仿真器和硬件平台的差异，使得策略能够方便地在不同的平台上部署。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18938v1/Figures/banner_no_text_cropped.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18938v1/Figures/3_methods/method_robot_platform_shrinked.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.18938v1/Figures/3_methods/low_level_network_arch_redo.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该框架能够成功地将仿真环境中训练的策略部署到真实机器人上，并实现了较好的控制效果。真实世界的遥操作物体拾取试验表明，协调的全身控制扩展了范围，并改善了对浮动基线操作的改进。Sim-to-sim实验揭示了Isaac Gym和MuJoCo接触模型之间的差异，这些差异影响了策略行为。

## 🎯 应用场景

该研究成果可应用于物流、救援、巡检等领域。例如，在复杂地形或狭小空间内，四足机器人可以利用其灵巧的操作能力进行物品搬运、灾情侦察或设备维护。该框架的开源发布将促进四足机器人技术的发展，加速其在各行业的应用。

## 📄 摘要（原文）

> Quadruped mobile manipulators offer strong potential for agile loco-manipulation but remain difficult to control and transfer reliably from simulation to reality. Reinforcement learning (RL) shows promise for whole-body control, yet most frameworks are proprietary and hard to reproduce on real hardware. We present an open pipeline for training, benchmarking, and deploying RL-based controllers on the Unitree B1 quadruped with a Z1 arm. The framework unifies sim-to-sim and sim-to-real transfer through ROS, re-implementing a policy trained in Isaac Gym, extending it to MuJoCo via a hardware abstraction layer, and deploying the same controller on physical hardware. Sim-to-sim experiments expose discrepancies between Isaac Gym and MuJoCo contact models that influence policy behavior, while real-world teleoperated object-picking trials show that coordinated whole-body control extends reach and improves manipulation over floating-base baselines. The pipeline provides a transparent, reproducible foundation for developing and analyzing RL-based loco-manipulation controllers and will be released open source to support future research.

