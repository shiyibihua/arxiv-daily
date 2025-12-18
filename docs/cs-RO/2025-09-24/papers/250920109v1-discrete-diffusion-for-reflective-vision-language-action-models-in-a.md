---
layout: default
title: Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving
---

# Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20109" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20109v1</a>
  <a href="https://arxiv.org/pdf/2509.20109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20109v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20109v1', 'Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengxiang Li, Yinan Zheng, Yue Wang, Huimin Wang, Hang Zhao, Jingjing Liu, Xianyuan Zhan, Kun Zhan, Xianpeng Lang

**分类**: cs.RO, cs.AI, cs.CL

**发布日期**: 2025-09-24

---

## 💡 一句话要点

**ReflectDrive：提出基于离散扩散和反射机制的自动驾驶反射式视觉-语言-动作模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `视觉-语言-动作模型` `离散扩散模型` `轨迹规划` `安全反射机制` `模仿学习` `NAVSIM`

## 📋 核心要点

1. 端到端视觉-语言-动作模型在自动驾驶中面临模仿学习的局限性，难以编码物理规则，需要复杂的后处理或依赖计算量大的扩散引导。
2. ReflectDrive通过离散化动作空间，利用预训练扩散语言模型进行轨迹规划，并引入无需梯度计算的安全感知反射机制进行迭代自校正。
3. 在NAVSIM基准测试中，ReflectDrive在安全关键轨迹生成方面表现出显著优势，为自动驾驶系统提供了一种可扩展且可靠的解决方案。

## 📝 摘要（中文）

本文提出了一种名为ReflectDrive的新型学习框架，它集成了反射机制，通过离散扩散实现安全轨迹生成。该方法首先离散化二维驾驶空间，构建动作代码本，从而能够通过微调预训练的扩散语言模型来完成规划任务。核心在于一种安全感知反射机制，它无需梯度计算即可进行迭代自校正。该方法首先生成目标条件轨迹以建模多模态驾驶行为，然后应用局部搜索方法来识别不安全token并确定可行解，这些可行解作为安全锚点用于基于修复的再生。在NAVSIM基准上的评估表明，ReflectDrive在安全关键轨迹生成方面具有显著优势，为自动驾驶系统提供了一种可扩展且可靠的解决方案。

## 🔬 方法详解

**问题定义**：现有端到端自动驾驶系统，特别是视觉-语言-动作模型，受限于模仿学习，难以直接学习物理规则和安全约束。现有方法要么依赖复杂的规则后处理，要么使用计算成本高的强化学习或扩散引导，难以在实际场景中应用。

**核心思路**：ReflectDrive的核心在于利用离散扩散模型生成轨迹，并通过一个安全感知的反射机制进行迭代修正。通过离散化动作空间，可以将轨迹规划问题转化为序列生成问题，从而利用预训练的扩散语言模型。反射机制通过局部搜索识别不安全行为，并利用安全锚点进行轨迹修复，无需梯度计算，降低了计算复杂度。

**技术框架**：ReflectDrive包含以下主要阶段：1) 动作空间离散化：将二维驾驶空间离散化为动作代码本。2) 目标条件轨迹生成：利用微调后的扩散语言模型生成目标条件轨迹，建模多模态驾驶行为。3) 安全感知反射：通过局部搜索识别不安全token，并确定可行的安全解。4) 基于修复的再生：利用安全解作为锚点，通过扩散模型进行轨迹修复，生成安全轨迹。

**关键创新**：ReflectDrive的关键创新在于其安全感知的反射机制，该机制无需梯度计算即可进行迭代自校正，显著降低了计算复杂度。此外，通过离散化动作空间，可以将轨迹规划问题转化为序列生成问题，从而能够利用预训练的扩散语言模型，提升了模型的泛化能力。

**关键设计**：动作空间的离散化粒度是一个关键参数，需要平衡轨迹的精度和计算复杂度。局部搜索算法的设计需要高效地识别不安全token，并找到可行的安全解。扩散模型的微调策略需要保证生成轨迹的多样性和安全性。损失函数的设计需要考虑轨迹的平滑性、目标达成率和安全性。

## 📊 实验亮点

ReflectDrive在NAVSIM基准测试中表现出显著优势，在安全关键轨迹生成方面优于现有方法。具体性能数据未知，但论文强调了其在安全性方面的提升，以及无需梯度计算的反射机制带来的计算效率优势。该方法为自动驾驶系统的安全轨迹生成提供了一种可扩展且可靠的解决方案。

## 🎯 应用场景

ReflectDrive可应用于各种自动驾驶场景，尤其是在安全要求高的场景中，例如城市道路、高速公路等。该方法可以提高自动驾驶系统的安全性和可靠性，降低事故风险。此外，该方法还可以应用于机器人导航、无人机飞行等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

