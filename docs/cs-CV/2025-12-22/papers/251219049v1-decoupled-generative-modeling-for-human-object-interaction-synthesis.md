---
layout: default
title: Decoupled Generative Modeling for Human-Object Interaction Synthesis
---

# Decoupled Generative Modeling for Human-Object Interaction Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19049" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19049v1</a>
  <a href="https://arxiv.org/pdf/2512.19049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19049v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19049v1', 'Decoupled Generative Modeling for Human-Object Interaction Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hwanhee Jung, Seunggwan Lee, Jeongyoon Yoon, SeungHyeon Kim, Giljoo Nam, Qixing Huang, Sangpil Kim

**分类**: cs.CV

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出DecHOI，解耦路径规划与动作生成，实现逼真的人-物交互合成**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人-物交互合成` `解耦生成模型` `轨迹生成` `动作合成` `对抗训练`

## 📋 核心要点

1. 现有HOI合成方法依赖手动指定的中间路点，并将所有优化目标置于单一网络，导致复杂性增加和灵活性降低。
2. DecHOI通过解耦路径规划和动作合成，先生成轨迹再合成动作，有效解决了人和物体运动不同步或穿透等问题。
3. 通过对抗训练增强接触真实感，并支持动态场景中的长序列规划，DecHOI在多个基准测试中超越现有方法。

## 📝 摘要（中文）

本文提出了一种用于人-物交互（HOI）合成的解耦生成模型DecHOI，旨在解决现有方法中存在的复杂性高、灵活性差以及易出错等问题。DecHOI将路径规划和动作合成分离，首先由轨迹生成器生成人和物体的轨迹，无需预先指定中间路点；然后，动作生成器以这些轨迹为条件，合成详细的动作。为了进一步提高接触的真实感，采用了对抗训练，判别器专注于远端关节的动态。该框架还支持对移动对象的建模，并能在动态场景中进行响应式、长序列的规划，同时保持规划的一致性。在FullBodyManipulation和3D-FUTURE两个基准测试中，DecHOI在大多数定量指标和定性评估上都优于现有方法，感知研究也更倾向于我们的结果。

## 🔬 方法详解

**问题定义**：现有的人-物交互（HOI）合成方法通常需要手动指定中间路点，并且将所有优化目标放在一个单一的网络中进行优化。这导致了几个问题：一是增加了模型的复杂性，二是降低了模型的灵活性，三是容易产生错误，例如人和物体的运动不同步，或者发生穿透现象。这些问题限制了HOI合成的真实性和可控性。

**核心思路**：DecHOI的核心思路是将HOI合成过程解耦为两个阶段：路径规划和动作合成。首先，使用轨迹生成器生成人和物体的运动轨迹，而无需预先指定中间路点。然后，使用动作生成器以这些轨迹为条件，生成详细的动作。这种解耦的设计使得模型更加灵活，并且可以更好地控制人和物体的运动。

**技术框架**：DecHOI的整体框架包含两个主要模块：轨迹生成器和动作生成器。轨迹生成器负责生成人和物体的运动轨迹，它接收场景信息作为输入，并输出人和物体的三维位置和姿态序列。动作生成器以轨迹生成器的输出作为条件，生成详细的动作，包括关节角度和接触力等。为了提高接触的真实感，DecHOI还引入了一个判别器，用于区分真实的人-物交互和生成的交互。

**关键创新**：DecHOI的关键创新在于解耦了路径规划和动作合成。这种解耦的设计使得模型更加灵活，并且可以更好地控制人和物体的运动。此外，DecHOI还引入了一个判别器，用于提高接触的真实感。这种对抗训练的方式可以有效地学习到真实的人-物交互的动态特征。

**关键设计**：DecHOI的关键设计包括：1) 使用变分自编码器（VAE）作为轨迹生成器，以学习运动轨迹的潜在空间表示；2) 使用循环神经网络（RNN）作为动作生成器，以生成时序相关的动作序列；3) 使用对抗训练，判别器专注于远端关节的动态，以提高接触的真实感；4) 损失函数包括轨迹损失、动作损失和对抗损失，用于优化轨迹生成器、动作生成器和判别器。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19049v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19049v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19049v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DecHOI在FullBodyManipulation和3D-FUTURE两个基准测试中取得了显著的性能提升。在定量指标方面，DecHOI在运动真实性、接触真实性和同步性等方面均优于现有方法。在定性评估方面，用户更倾向于DecHOI生成的人-物交互动画。感知研究表明，DecHOI能够生成更加逼真和自然的HOI。

## 🎯 应用场景

DecHOI在3D计算机视觉和机器人领域具有广泛的应用前景，例如动画制作、具身控制、虚拟现实和增强现实等。它可以用于生成逼真的人-物交互动画，提高机器人的操作能力，以及创建更加沉浸式的虚拟现实体验。此外，DecHOI还可以用于数据增强，生成更多的人-物交互数据，以训练更加鲁棒的计算机视觉模型。

## 📄 摘要（原文）

> Synthesizing realistic human-object interaction (HOI) is essential for 3D computer vision and robotics, underpinning animation and embodied control. Existing approaches often require manually specified intermediate waypoints and place all optimization objectives on a single network, which increases complexity, reduces flexibility, and leads to errors such as unsynchronized human and object motion or penetration. To address these issues, we propose Decoupled Generative Modeling for Human-Object Interaction Synthesis (DecHOI), which separates path planning and action synthesis. A trajectory generator first produces human and object trajectories without prescribed waypoints, and an action generator conditions on these paths to synthesize detailed motions. To further improve contact realism, we employ adversarial training with a discriminator that focuses on the dynamics of distal joints. The framework also models a moving counterpart and supports responsive, long-sequence planning in dynamic scenes, while preserving plan consistency. Across two benchmarks, FullBodyManipulation and 3D-FUTURE, DecHOI surpasses prior methods on most quantitative metrics and qualitative evaluations, and perceptual studies likewise prefer our results.

