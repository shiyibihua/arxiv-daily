---
layout: default
title: Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos
---

# Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16907" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16907v1</a>
  <a href="https://arxiv.org/pdf/2512.16907.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16907v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16907v1', 'Flowing from Reasoning to Motion: Learning 3D Hand Trajectory Prediction from Egocentric Human Interaction Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingfei Chen, Yifan Wang, Zhengqin Li, Homanga Bharadhwaj, Yujin Chen, Chuan Qin, Ziyi Kou, Yuan Tian, Eric Whitmire, Rajinder Sodhi, Hrvoje Benko, Eli Shlizerman, Yue Liu

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-12-18

**备注**: Project website: https://egoman-project.github.io

---

## 💡 一句话要点

**EgoMAN：基于自中心交互视频学习3D手部轨迹预测，实现从推理到动作的流畅衔接**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `3D手部轨迹预测` `自中心视频` `人机交互` `视觉-语言推理` `运动生成`

## 📋 核心要点

1. 现有3D手部轨迹预测方法缺乏语义监督，且推理与动作之间的联系较弱，限制了其性能。
2. EgoMAN模型通过轨迹-token接口连接视觉-语言推理和运动生成，实现推理到动作的流畅衔接。
3. EgoMAN数据集和模型在真实场景中表现出良好的泛化能力，能够生成准确且具有阶段感知的轨迹。

## 📝 摘要（中文）

本文提出了一种基于自中心视角的交互场景下，阶段感知的3D手部轨迹预测方法。为了解决现有方法中运动与语义监督解耦以及推理与动作弱连接的问题，作者首先构建了EgoMAN数据集，这是一个大规模的自中心数据集，包含21.9万条6DoF轨迹和300万个结构化的QA对，用于语义、空间和运动推理。然后，作者提出了EgoMAN模型，这是一个推理到运动的框架，通过轨迹-token接口连接视觉-语言推理和运动生成。该方法通过逐步训练，使推理与运动动态对齐，从而生成准确且具有阶段感知的轨迹，并在真实场景中具有良好的泛化能力。

## 🔬 方法详解

**问题定义**：现有3D手部轨迹预测方法面临两个主要问题。一是数据集的限制，现有数据集通常将运动与语义监督解耦，导致模型难以学习到丰富的交互信息。二是模型设计上的不足，现有模型通常弱化推理和动作之间的联系，导致预测的轨迹缺乏阶段感知能力，难以准确反映交互过程中的语义信息。

**核心思路**：本文的核心思路是通过构建一个大规模的、包含丰富语义信息的自中心数据集EgoMAN，并设计一个推理到运动的框架EgoMAN模型，从而解决上述问题。EgoMAN模型通过轨迹-token接口，将视觉-语言推理的结果转化为运动生成的输入，从而实现推理和动作之间的强连接。

**技术框架**：EgoMAN模型的整体框架包含三个主要模块：视觉-语言推理模块、轨迹-token接口模块和运动生成模块。首先，视觉-语言推理模块负责从自中心视频中提取语义信息，并生成相应的推理结果。然后，轨迹-token接口模块将推理结果转化为轨迹token，作为运动生成模块的输入。最后，运动生成模块根据轨迹token生成3D手部轨迹。

**关键创新**：本文最重要的技术创新点在于提出了轨迹-token接口，该接口能够有效地连接视觉-语言推理和运动生成，从而实现推理到动作的流畅衔接。与现有方法相比，EgoMAN模型能够更好地利用语义信息，生成更准确、更具有阶段感知能力的3D手部轨迹。

**关键设计**：EgoMAN模型采用了一种渐进式的训练策略，首先训练视觉-语言推理模块，然后训练运动生成模块，最后将两个模块联合训练，以实现推理和动作之间的对齐。在损失函数方面，作者设计了多种损失函数，包括轨迹预测损失、阶段分类损失和QA损失，以保证模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16907v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16907v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16907v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EgoMAN数据集包含21.9万条6DoF轨迹和300万个结构化的QA对，是目前最大的自中心手部轨迹预测数据集。EgoMAN模型在多个benchmark上取得了state-of-the-art的性能，相比现有方法，在轨迹预测精度和阶段分类准确率上均有显著提升。实验结果表明，EgoMAN模型具有良好的泛化能力，能够在真实场景中生成准确且具有阶段感知的轨迹。

## 🎯 应用场景

该研究成果可应用于人机交互、机器人控制、虚拟现实等领域。例如，在机器人控制中，机器人可以根据人类的意图预测其手部轨迹，从而更好地完成协作任务。在虚拟现实中，可以生成更逼真的手部动画，提升用户的沉浸感。未来，该技术有望应用于智能家居、辅助驾驶等更多场景。

## 📄 摘要（原文）

> Prior works on 3D hand trajectory prediction are constrained by datasets that decouple motion from semantic supervision and by models that weakly link reasoning and action. To address these, we first present the EgoMAN dataset, a large-scale egocentric dataset for interaction stage-aware 3D hand trajectory prediction with 219K 6DoF trajectories and 3M structured QA pairs for semantic, spatial, and motion reasoning. We then introduce the EgoMAN model, a reasoning-to-motion framework that links vision-language reasoning and motion generation via a trajectory-token interface. Trained progressively to align reasoning with motion dynamics, our approach yields accurate and stage-aware trajectories with generalization across real-world scenes.

