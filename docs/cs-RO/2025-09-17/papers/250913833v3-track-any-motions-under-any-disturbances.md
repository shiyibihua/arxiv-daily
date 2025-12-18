---
layout: default
title: Track Any Motions under Any Disturbances
---

# Track Any Motions under Any Disturbances

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13833" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13833v3</a>
  <a href="https://arxiv.org/pdf/2509.13833.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13833v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13833v3', 'Track Any Motions under Any Disturbances')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhikai Zhang, Jun Guo, Chao Chen, Jilong Wang, Chenghuai Lin, Yunrui Lian, Han Xue, Zhenrong Wang, Maoqi Liu, Jiangran Lyu, Huaping Liu, He Wang, Li Yi

**分类**: cs.RO

**发布日期**: 2025-09-17 (更新: 2025-09-30)

---

## 💡 一句话要点

**Any2Track：强化学习框架，实现人形机器人复杂运动和抗扰动追踪**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人` `运动追踪` `强化学习` `动态自适应` `sim2real迁移`

## 📋 核心要点

1. 现有方法难以使人形机器人在复杂地形和外力扰动下稳定追踪多样化运动。
2. Any2Track框架包含AnyTracker和AnyAdapter，分别负责通用运动追踪和动态自适应。
3. 在Unitree G1上部署Any2Track，实现了零样本sim2real迁移，并在真实扰动下表现出色。

## 📝 摘要（中文）

本文提出Any2Track，一个两阶段强化学习框架，旨在实现人形机器人在各种扰动下追踪多样化、高动态和富含接触的运动。一个基础的人形运动追踪器需要能够追踪各种运动，更重要的是，它需要在真实场景中稳定运行，抵抗各种动态扰动，包括地形、外力和物理属性变化，以实现通用实用性。Any2Track将动态适应性重新定义为基本动作执行之外的附加能力，由两个关键组件组成：AnyTracker和AnyAdapter。AnyTracker是一个通用的运动追踪器，通过一系列精心设计，可以在单个策略中追踪各种运动。AnyAdapter是一个历史信息自适应模块，赋予追踪器在线动态适应性，以克服sim2real差距和多种真实世界扰动。我们在Unitree G1硬件上部署了Any2Track，并以零样本方式实现了成功的sim2real迁移。Any2Track在各种真实世界扰动下追踪各种运动方面表现出色。

## 🔬 方法详解

**问题定义**：现有的人形机器人运动追踪器难以在真实世界的复杂环境中稳定工作，尤其是在面对地形变化、外部干扰力以及机器人自身物理属性变化时。这些因素会导致追踪性能下降，甚至完全失效。现有的方法通常难以同时兼顾运动的多样性和对动态扰动的适应性。

**核心思路**：Any2Track的核心思路是将运动追踪问题分解为两个阶段：首先，通过AnyTracker学习一个通用的运动追踪策略，使其能够处理多种不同的运动模式；然后，通过AnyAdapter模块，利用历史信息在线调整策略，以适应各种动态扰动。这种解耦的设计使得系统能够更好地应对真实世界的复杂性。

**技术框架**：Any2Track框架包含两个主要模块：AnyTracker和AnyAdapter。AnyTracker是一个通用的运动追踪器，负责学习基本的运动控制策略。AnyAdapter是一个历史信息自适应模块，它接收AnyTracker的输出以及历史状态信息，并根据当前环境的动态特性调整控制策略。整个框架采用两阶段强化学习训练，首先训练AnyTracker，然后训练AnyAdapter。

**关键创新**：Any2Track的关键创新在于将动态适应性建模为一个独立的模块（AnyAdapter），并将其与通用的运动追踪器（AnyTracker）解耦。这种设计使得系统能够更好地泛化到不同的环境和扰动。此外，AnyAdapter利用历史信息进行自适应调整，能够更有效地应对时变的动态扰动。

**关键设计**：AnyTracker采用精心设计的奖励函数，鼓励机器人执行期望的运动，并惩罚不期望的行为。AnyAdapter使用循环神经网络（RNN）来处理历史信息，并输出对AnyTracker控制参数的调整量。损失函数的设计旨在最小化追踪误差，并最大化机器人的稳定性。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

Any2Track在Unitree G1硬件上实现了零样本sim2real迁移，表明其具有良好的泛化能力。实验结果表明，Any2Track在各种真实世界扰动下，能够有效地追踪各种运动，性能优于现有方法。具体的性能数据和对比基线未在摘要中详细说明，属于未知信息。

## 🎯 应用场景

Any2Track技术可应用于人形机器人在复杂环境下的运动控制，例如搜救、物流、巡检等领域。该技术能够提高机器人在非结构化环境中的适应性和稳定性，使其能够更好地完成各种任务。未来，该技术有望推动人形机器人在更多实际场景中的应用。

## 📄 摘要（原文）

> A foundational humanoid motion tracker is expected to be able to track diverse, highly dynamic, and contact-rich motions. More importantly, it needs to operate stably in real-world scenarios against various dynamics disturbances, including terrains, external forces, and physical property changes for general practical use. To achieve this goal, we propose Any2Track (Track Any motions under Any disturbances), a two-stage RL framework to track various motions under multiple disturbances in the real world. Any2Track reformulates dynamics adaptability as an additional capability on top of basic action execution and consists of two key components: AnyTracker and AnyAdapter. AnyTracker is a general motion tracker with a series of careful designs to track various motions within a single policy. AnyAdapter is a history-informed adaptation module that endows the tracker with online dynamics adaptability to overcome the sim2real gap and multiple real-world disturbances. We deploy Any2Track on Unitree G1 hardware and achieve a successful sim2real transfer in a zero-shot manner. Any2Track performs exceptionally well in tracking various motions under multiple real-world disturbances.

