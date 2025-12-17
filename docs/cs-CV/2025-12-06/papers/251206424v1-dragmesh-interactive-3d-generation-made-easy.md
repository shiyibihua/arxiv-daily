---
layout: default
title: DragMesh: Interactive 3D Generation Made Easy
---

# DragMesh: Interactive 3D Generation Made Easy

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.06424" target="_blank" class="toolbar-btn">arXiv: 2512.06424v1</a>
    <a href="https://arxiv.org/pdf/2512.06424.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06424v1" 
            onclick="toggleFavorite(this, '2512.06424v1', 'DragMesh: Interactive 3D Generation Made Easy')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianshan Zhang, Zeyu Zhang, Hao Tang

**分类**: cs.CV

**发布日期**: 2025-12-06

**🔗 代码/项目**: [GITHUB](https://github.com/AIGeeksGroup/DragMesh) | [PROJECT_PAGE](https://aigeeksgroup.github.io/DragMesh)

---

## 💡 一句话要点

**DragMesh：提出解耦运动生成框架，实现实时交互式3D模型可动性生成。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D生成` `铰接运动` `运动学推理` `对偶四元数` `VAE` `实时交互` `运动生成`

## 📋 核心要点

1. 现有铰接运动方法难以兼顾物理一致性和实时性，且生成式方法常违反运动学约束。
2. DragMesh提出解耦的运动学推理和运动生成框架，利用KPP-Net预测关节参数，DQ-VAE生成运动轨迹。
3. DragMesh无需重新训练即可对新物体进行实时交互式铰接，为生成式3D智能提供有效方案。

## 📝 摘要（中文）

生成模型在创建静态3D内容方面表现出色，但构建能够理解物体如何移动和响应交互的系统仍然是一个根本性的挑战。目前，用于铰接运动的方法正处于十字路口：它们要么在物理上一致，但速度太慢而无法实时使用，要么是生成式的，但违反了基本的运动学约束。我们提出了DragMesh，这是一个围绕轻量级运动生成核心构建的鲁棒的实时交互式3D铰接框架。我们的核心贡献是一种新颖的解耦运动学推理和运动生成框架。首先，我们通过将语义意图推理（确定关节类型）与几何回归（使用我们的运动学预测网络（KPP-Net）确定轴和原点）解耦来推断潜在的关节参数。其次，为了利用对偶四元数的紧凑、连续和无奇异性的特性来表示刚体运动，我们开发了一种新的对偶四元数VAE（DQ-VAE）。该DQ-VAE接收这些预测的先验，以及原始的用户拖动，以生成完整、合理的运动轨迹。为了确保严格遵守运动学，我们使用FiLM（特征线性调制）条件作用将关节先验注入到DQ-VAE非自回归Transformer解码器的每一层。这种持久的、多尺度的指导由一个数值稳定的叉积损失来补充，以保证轴对齐。这种解耦设计允许DragMesh实现实时性能，并能够在不重新训练的情况下对新对象进行合理的生成式铰接，为生成式3D智能提供了一个实际的步骤。

## 🔬 方法详解

**问题定义**：现有铰接运动生成方法面临两个主要问题。一是物理模拟方法虽然保证了运动的物理真实性，但计算复杂度高，难以实现实时交互。二是基于生成模型的方法虽然速度快，但难以保证运动的运动学约束，例如关节的正确旋转轴和角度范围，导致生成的运动不自然甚至错误。

**核心思路**：DragMesh的核心思路是将运动学推理和运动生成解耦。首先，通过一个专门的网络（KPP-Net）预测关节的类型、轴和原点等运动学参数，这些参数作为先验知识指导后续的运动生成过程。其次，利用对偶四元数（Dual Quaternion）的特性，设计了一个DQ-VAE模型，用于生成平滑且符合运动学约束的运动轨迹。这种解耦的设计使得模型可以在保证运动学约束的前提下，实现快速的运动生成。

**技术框架**：DragMesh的整体框架包含两个主要模块：运动学预测网络（KPP-Net）和对偶四元数VAE（DQ-VAE）。首先，用户通过拖拽操作指定物体的运动意图。KPP-Net接收物体的初始状态和用户的拖拽信息，预测物体各个关节的类型、轴和原点等运动学参数。然后，DQ-VAE接收KPP-Net预测的运动学参数和用户的拖拽信息，生成完整的运动轨迹。为了保证运动的运动学约束，KPP-Net的预测结果会通过FiLM条件作用注入到DQ-VAE的每一层。

**关键创新**：DragMesh最重要的技术创新在于解耦的运动学推理和运动生成框架。传统的运动生成方法通常将运动学约束作为后处理步骤进行优化，而DragMesh则将运动学约束融入到运动生成的过程中，通过KPP-Net预测运动学参数，并将其作为先验知识指导DQ-VAE的运动生成。这种解耦的设计使得模型可以在保证运动学约束的前提下，实现快速的运动生成。

**关键设计**：KPP-Net是一个回归网络，用于预测关节的类型、轴和原点等运动学参数。DQ-VAE是一个基于Transformer的VAE模型，用于生成运动轨迹。为了保证运动的运动学约束，KPP-Net的预测结果会通过FiLM条件作用注入到DQ-VAE的每一层。此外，论文还设计了一个叉积损失函数，用于保证关节轴的对齐。

## 📊 实验亮点

DragMesh在实时性和运动学约束方面都取得了显著的成果。实验表明，DragMesh能够以实时帧率生成合理的铰接运动，并且生成的运动轨迹能够严格遵守运动学约束。与现有的方法相比，DragMesh在运动的真实性和交互性方面都有明显的优势。此外，DragMesh还具有良好的泛化能力，能够在不重新训练的情况下对新物体进行铰接。

## 🎯 应用场景

DragMesh具有广泛的应用前景，例如虚拟现实/增强现实（VR/AR）中的物体交互、游戏开发中的角色动画、机器人控制中的运动规划等。该研究能够提升用户在虚拟环境中的交互体验，降低3D内容创作的门槛，并为机器人提供更自然、更智能的运动控制能力。未来，DragMesh有望成为通用3D交互平台的重要组成部分。

## 📄 摘要（原文）

> While generative models have excelled at creating static 3D content, the pursuit of systems that understand how objects move and respond to interactions remains a fundamental challenge. Current methods for articulated motion lie at a crossroads: they are either physically consistent but too slow for real-time use, or generative but violate basic kinematic constraints. We present DragMesh, a robust framework for real-time interactive 3D articulation built around a lightweight motion generation core. Our core contribution is a novel decoupled kinematic reasoning and motion generation framework. First, we infer the latent joint parameters by decoupling semantic intent reasoning (which determines the joint type) from geometric regression (which determines the axis and origin using our Kinematics Prediction Network (KPP-Net)). Second, to leverage the compact, continuous, and singularity-free properties of dual quaternions for representing rigid body motion, we develop a novel Dual Quaternion VAE (DQ-VAE). This DQ-VAE receives these predicted priors, along with the original user drag, to generate a complete, plausible motion trajectory. To ensure strict adherence to kinematics, we inject the joint priors at every layer of the DQ-VAE's non-autoregressive Transformer decoder using FiLM (Feature-wise Linear Modulation) conditioning. This persistent, multi-scale guidance is complemented by a numerically-stable cross-product loss to guarantee axis alignment. This decoupled design allows DragMesh to achieve real-time performance and enables plausible, generative articulation on novel objects without retraining, offering a practical step toward generative 3D intelligence. Code: https://github.com/AIGeeksGroup/DragMesh. Website: https://aigeeksgroup.github.io/DragMesh.

