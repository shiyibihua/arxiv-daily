---
layout: default
title: Musculoskeletal simulation of limb movement biomechanics in Drosophila melanogaster
---

# Musculoskeletal simulation of limb movement biomechanics in Drosophila melanogaster

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06426" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06426v2</a>
  <a href="https://arxiv.org/pdf/2509.06426.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06426v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06426v2', 'Musculoskeletal simulation of limb movement biomechanics in Drosophila melanogaster')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pembe Gizem Özdil, Chuanfang Ning, Jasper S. Phelps, Sibo Wang-Chen, Guy Elisha, Alexander Blanke, Auke Ijspeert, Pavan Ramdya

**分类**: q-bio.NC, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-09-08 (更新: 2025-09-11)

**备注**: 23 pages, 11 figures

---

## 💡 一句话要点

**构建果蝇腿部肌肉骨骼模型，揭示运动控制的生物力学机制。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `肌肉骨骼建模` `果蝇运动` `生物力学` `运动控制` `OpenSim` `MuJoCo` `模仿学习`

## 📋 核心要点

1. 现有计算模型缺乏果蝇腿部肌肉的解剖学和物理基础模型，无法有效连接运动神经元活动和关节运动。
2. 论文构建了首个基于数据的果蝇腿部肌肉骨骼3D模型，并结合形态学数据优化了肌肉参数。
3. 通过模拟果蝇行为，预测了肌肉协同作用，并发现关节阻尼和刚度有助于模仿学习。

## 📝 摘要（中文）

本文提出了一种基于数据的果蝇腿部肌肉骨骼3D模型，该模型在OpenSim和MuJoCo模拟环境中实现。该模型基于多个固定样本的高分辨率X射线扫描，采用了Hill型肌肉表示。论文提出了一套利用形态学图像数据构建肌肉模型并优化果蝇特有未知肌肉参数的流程。通过结合肌肉骨骼模型和行为果蝇的详细3D姿态估计数据，实现了OpenSim中的肌肉驱动行为重现。对不同行走和梳理行为的肌肉活动模拟预测了可实验验证的协调肌肉协同作用。此外，通过在MuJoCo中训练模仿学习策略，测试了不同被动关节属性对学习速度的影响，发现阻尼和刚度有助于学习。该模型有助于研究实验上易于处理的模型生物中的运动控制，深入了解生物力学如何促进复杂肢体运动的产生。此外，该模型可用于控制具身人工智能体，以在模拟环境中生成自然且顺应的运动。

## 🔬 方法详解

**问题定义**：现有研究缺乏对果蝇腿部肌肉的精确建模，无法充分理解神经系统、生物力学和物理系统如何协同控制果蝇的运动行为。特别是，缺乏连接运动神经元活动和关节运动的肌肉骨骼模型。现有方法难以利用果蝇的肌肉、骨骼和外骨骼的近乎完整的重建数据。

**核心思路**：论文的核心思路是构建一个基于数据的、解剖学精确的果蝇腿部肌肉骨骼模型，并利用该模型来模拟和分析果蝇的运动行为。通过结合高分辨率的形态学数据和行为数据，可以推断出肌肉的活动模式和生物力学特性，从而深入理解运动控制的机制。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 基于高分辨率X射线扫描数据构建果蝇腿部肌肉的3D模型；2) 采用Hill型肌肉模型来表示肌肉的力学特性；3) 开发一个流程，用于利用形态学图像数据构建肌肉模型，并优化果蝇特有的未知肌肉参数；4) 将肌肉骨骼模型与行为果蝇的3D姿态估计数据相结合，在OpenSim中实现肌肉驱动的行为重现；5) 在MuJoCo中训练模仿学习策略，研究不同被动关节属性对学习速度的影响。

**关键创新**：该研究的关键创新在于构建了首个果蝇腿部肌肉骨骼的3D模型，并将其应用于运动控制的研究。该模型结合了形态学数据、生物力学模型和机器学习方法，能够更准确地模拟和分析果蝇的运动行为。此外，该研究还提出了一套利用形态学图像数据构建肌肉模型并优化肌肉参数的流程。

**关键设计**：在肌肉建模方面，采用了Hill型肌肉模型，该模型能够较好地描述肌肉的力学特性。在参数优化方面，采用了基于形态学数据的优化方法，能够更准确地估计果蝇特有的肌肉参数。在模仿学习方面，采用了强化学习算法，并研究了不同被动关节属性对学习速度的影响。

## 📊 实验亮点

该研究通过模拟不同行走和梳理行为的肌肉活动，预测了可实验验证的协调肌肉协同作用。此外，通过在MuJoCo中训练模仿学习策略，发现关节阻尼和刚度有助于学习。这些结果表明，该模型能够较好地模拟和预测果蝇的运动行为，并为研究运动控制的机制提供了新的见解。

## 🎯 应用场景

该研究成果可应用于生物力学、神经科学和机器人学等领域。在生物力学方面，可以帮助研究人员深入理解动物运动的生物力学机制。在神经科学方面，可以为研究运动控制的神经机制提供新的工具和方法。在机器人学方面，可以用于设计和控制具有生物启发式的机器人，例如，可以控制具身人工智能体，以在模拟环境中生成自然且顺应的运动。

## 📄 摘要（原文）

> Computational models are critical to advance our understanding of how neural, biomechanical, and physical systems interact to orchestrate animal behaviors. Despite the availability of near-complete reconstructions of the Drosophila melanogaster central nervous system, musculature, and exoskeleton, anatomically and physically grounded models of fly leg muscles are still missing. These models provide an indispensable bridge between motor neuron activity and joint movements. Here, we introduce the first 3D, data-driven musculoskeletal model of Drosophila legs, implemented in both OpenSim and MuJoCo simulation environments. Our model incorporates a Hill-type muscle representation based on high-resolution X-ray scans from multiple fixed specimens. We present a pipeline for constructing muscle models using morphological imaging data and for optimizing unknown muscle parameters specific to the fly. We then combine our musculoskeletal models with detailed 3D pose estimation data from behaving flies to achieve muscle-actuated behavioral replay in OpenSim. Simulations of muscle activity across diverse walking and grooming behaviors predict coordinated muscle synergies that can be tested experimentally. Furthermore, by training imitation learning policies in MuJoCo, we test the effect of different passive joint properties on learning speed and find that damping and stiffness facilitate learning. Overall, our model enables the investigation of motor control in an experimentally tractable model organism, providing insights into how biomechanics contribute to generation of complex limb movements. Moreover, our model can be used to control embodied artificial agents to generate naturalistic and compliant locomotion in simulated environments.

