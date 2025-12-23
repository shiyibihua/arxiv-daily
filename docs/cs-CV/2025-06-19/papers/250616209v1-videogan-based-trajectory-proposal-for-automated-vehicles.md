---
layout: default
title: VideoGAN-based Trajectory Proposal for Automated Vehicles
---

# VideoGAN-based Trajectory Proposal for Automated Vehicles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16209" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16209v1</a>
  <a href="https://arxiv.org/pdf/2506.16209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16209v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16209v1', 'VideoGAN-based Trajectory Proposal for Automated Vehicles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Annajoyce Mariani, Kira Maag, Hanno Gottschalk

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**基于VideoGAN的轨迹提议方法以解决自动驾驶车辆轨迹生成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成对抗网络` `轨迹生成` `自动驾驶` `鸟瞰视角` `视频生成` `多模态学习` `交通场景`

## 📋 核心要点

1. 现有的轨迹生成方法在捕捉复杂的多模态未来轨迹分布方面存在不足，难以满足自动驾驶的需求。
2. 本文提出了一种基于VideoGAN的轨迹生成管道，利用鸟瞰视角交通场景视频进行训练，以生成准确的轨迹。
3. 实验结果表明，所提方法在100 GPU小时内训练，推理时间低于20毫秒，且生成轨迹在空间和动态参数上与真实数据高度一致。

## 📝 摘要（中文）

生成真实的轨迹选项是提高道路车辆自动化程度的核心。现有的模型驱动、基于规则和经典学习方法在捕捉未来轨迹的复杂多模态分布方面存在困难。本文探讨了使用在鸟瞰视角交通场景视频上训练的生成对抗网络（GAN）来生成统计上准确的轨迹，以正确捕捉代理之间的空间关系。我们提出了一种使用低分辨率BEV占用网格视频作为视频生成模型训练数据的管道，并通过单帧物体检测和帧间物体匹配从生成的视频中提取抽象轨迹数据。我们选择GAN架构以实现快速的训练和推理时间，最终在100 GPU小时的训练内获得最佳结果，推理时间低于20毫秒。我们展示了所提轨迹在空间和动态参数分布对齐方面的物理现实性，基于Waymo开放运动数据集的真实视频。

## 🔬 方法详解

**问题定义**：本文旨在解决自动驾驶车辆轨迹生成的挑战，现有方法难以有效捕捉未来轨迹的复杂多模态分布，导致生成的轨迹不够真实。

**核心思路**：我们提出使用生成对抗网络（GAN）来训练模型，利用鸟瞰视角的交通场景视频作为训练数据，以生成符合统计特性的轨迹，确保轨迹之间的空间关系得到准确捕捉。

**技术框架**：整体架构包括数据收集、GAN训练、轨迹提取和评估四个主要模块。首先收集低分辨率BEV占用网格视频，然后训练GAN生成交通场景视频，最后通过单帧物体检测和帧间物体匹配提取轨迹数据。

**关键创新**：本研究的主要创新在于将GAN应用于轨迹生成任务，利用视频数据而非传统的静态数据，从而提高了生成轨迹的真实性和多样性。与现有方法相比，GAN在训练和推理速度上具有显著优势。

**关键设计**：在网络结构上，我们选择了适合快速训练的GAN架构，并在损失函数设计上进行了优化，以确保生成轨迹的空间和动态参数与真实数据对齐。

## 📊 实验亮点

实验结果显示，所提方法在100 GPU小时的训练时间内实现了最佳性能，推理时间低于20毫秒。生成的轨迹在空间和动态参数的分布上与Waymo开放运动数据集的真实视频高度一致，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在自动驾驶、智能交通系统和机器人导航等领域。通过生成更真实的轨迹选项，可以显著提高自动驾驶系统的决策能力和安全性，推动智能交通技术的发展。

## 📄 摘要（原文）

> Being able to generate realistic trajectory options is at the core of increasing the degree of automation of road vehicles. While model-driven, rule-based, and classical learning-based methods are widely used to tackle these tasks at present, they can struggle to effectively capture the complex, multimodal distributions of future trajectories. In this paper we investigate whether a generative adversarial network (GAN) trained on videos of bird's-eye view (BEV) traffic scenarios can generate statistically accurate trajectories that correctly capture spatial relationships between the agents. To this end, we propose a pipeline that uses low-resolution BEV occupancy grid videos as training data for a video generative model. From the generated videos of traffic scenarios we extract abstract trajectory data using single-frame object detection and frame-to-frame object matching. We particularly choose a GAN architecture for the fast training and inference times with respect to diffusion models. We obtain our best results within 100 GPU hours of training, with inference times under 20\,ms. We demonstrate the physical realism of the proposed trajectories in terms of distribution alignment of spatial and dynamic parameters with respect to the ground truth videos from the Waymo Open Motion Dataset.

