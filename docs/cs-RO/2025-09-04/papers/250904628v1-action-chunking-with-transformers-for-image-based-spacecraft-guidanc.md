---
layout: default
title: Action Chunking with Transformers for Image-Based Spacecraft Guidance and Control
---

# Action Chunking with Transformers for Image-Based Spacecraft Guidance and Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04628" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04628v1</a>
  <a href="https://arxiv.org/pdf/2509.04628.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04628v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04628v1', 'Action Chunking with Transformers for Image-Based Spacecraft Guidance and Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alejandro Posadas-Nava, Andrea Scorsoglio, Luca Ghilardi, Roberto Furfaro, Richard Linares

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-04

**备注**: 12 pages, 6 figures, 2025 AAS/AIAA Astrodynamics Specialist Conference

---

## 💡 一句话要点

**提出基于变换器的动作分块方法以提升航天器引导与控制性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `航天器控制` `模仿学习` `变换器` `样本效率` `轨迹生成` `自主导航` `空间任务`

## 📋 核心要点

1. 现有的航天器引导与控制方法在数据稀缺的情况下性能不足，难以实现高效的控制策略。
2. 本文提出的动作分块与变换器（ACT）方法，通过模仿学习从有限的专家演示中学习控制策略，提升了样本效率。
3. 实验结果表明，ACT在与国际空间站对接任务中，表现出更高的准确性和更平滑的控制，相较于传统方法有显著提升。

## 📝 摘要（中文）

本文提出了一种模仿学习方法，旨在提高航天器的引导、导航和控制（GNC）性能，尤其是在数据有限的情况下。通过仅使用100个专家演示（相当于6300次环境交互），我们的方法实现了动作分块与变换器（ACT），能够将视觉和状态观察映射为推力和扭矩指令。与使用4000万次交互训练的元强化学习（meta-RL）基线相比，ACT生成了更平滑、更一致的轨迹。我们在与国际空间站（ISS）对接的任务中评估了ACT，结果显示该方法在准确性、控制平滑性和样本效率方面均表现优越。

## 🔬 方法详解

**问题定义**：本文旨在解决航天器引导与控制中的数据稀缺问题，现有方法通常依赖大量交互数据，导致样本效率低下。

**核心思路**：提出的ACT方法通过模仿学习，从少量专家演示中提取有效信息，利用变换器模型处理视觉和状态信息，从而生成控制指令。

**技术框架**：ACT的整体架构包括数据收集、特征提取、控制策略学习和执行四个主要模块。首先收集专家演示数据，然后通过变换器模型提取特征，最后生成推力和扭矩指令。

**关键创新**：ACT的主要创新在于将动作分块与变换器结合，显著提高了控制策略的平滑性和一致性，与传统的强化学习方法相比，减少了对大量交互数据的依赖。

**关键设计**：在模型设计中，采用了特定的损失函数以优化控制精度，并在变换器结构中引入了自注意力机制，以增强模型对重要特征的关注。

## 📊 实验亮点

实验结果显示，ACT方法在与国际空间站对接任务中，控制精度显著提高，轨迹更加平滑。与传统的元强化学习基线相比，ACT在样本效率上提升了数倍，证明了其在数据有限情况下的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括航天器的自主导航与控制，尤其是在复杂环境下的任务执行，如空间站对接、卫星轨道调整等。其高效的样本利用率和控制精度将为未来的航天任务提供重要支持，推动航天技术的进步与发展。

## 📄 摘要（原文）

> We present an imitation learning approach for spacecraft guidance, navigation, and control(GNC) that achieves high performance from limited data. Using only 100 expert demonstrations, equivalent to 6,300 environment interactions, our method, which implements Action Chunking with Transformers (ACT), learns a control policy that maps visual and state observations to thrust and torque commands. ACT generates smoother, more consistent trajectories than a meta-reinforcement learning (meta-RL) baseline trained with 40 million interactions. We evaluate ACT on a rendezvous task: in-orbit docking with the International Space Station (ISS). We show that our approach achieves greater accuracy, smoother control, and greater sample efficiency.

