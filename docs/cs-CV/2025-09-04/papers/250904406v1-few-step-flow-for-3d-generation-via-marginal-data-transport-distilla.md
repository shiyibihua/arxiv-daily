---
layout: default
title: Few-step Flow for 3D Generation via Marginal-Data Transport Distillation
---

# Few-step Flow for 3D Generation via Marginal-Data Transport Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04406" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04406v1</a>
  <a href="https://arxiv.org/pdf/2509.04406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04406v1', 'Few-step Flow for 3D Generation via Marginal-Data Transport Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zanwei Zhou, Taoran Yi, Jiemin Fang, Chen Yang, Lingxi Xie, Xinggang Wang, Wei Shen, Qi Tian

**分类**: cs.CV

**发布日期**: 2025-09-04

**备注**: Project page: https://github.com/Zanue/MDT-dist

---

## 💡 一句话要点

**提出MDT-dist以解决3D生成模型的采样效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `3D生成` `流模型` `蒸馏训练` `速度匹配` `速度蒸馏` `计算机视觉` `模型优化`

## 📋 核心要点

1. 现有的基于流的3D生成模型在推理时需要大量的采样步骤，导致效率低下。
2. 论文提出MDT-dist框架，通过速度匹配和速度蒸馏来实现少步3D流蒸馏，显著提升采样效率。
3. 在TRELLIS框架上，方法将采样步骤减少至1或2，实现了9.0x和6.5x的速度提升，同时保持高质量生成效果。

## 📝 摘要（中文）

基于流的3D生成模型通常在推理过程中需要数十个采样步骤。尽管少步蒸馏方法，特别是一致性模型（CMs），在加速2D扩散模型方面取得了显著进展，但在更复杂的3D生成任务中仍然未得到充分探索。本研究提出了一种新颖的框架MDT-dist，用于少步3D流蒸馏。该方法的主要目标是蒸馏预训练模型以学习边际数据传输。我们提出了两个可优化的目标：速度匹配（VM）和速度蒸馏（VD），以将优化目标从传输层面等效转换为速度和分布层面。实验表明，我们的方法在TRELLIS框架上将每个流变换器的采样步骤从25减少到1或2，同时保持高视觉和几何保真度。

## 🔬 方法详解

**问题定义**：本论文旨在解决基于流的3D生成模型在推理过程中需要大量采样步骤的问题，现有方法在效率上存在显著不足。

**核心思路**：提出MDT-dist框架，通过蒸馏预训练模型来学习边际数据传输，利用速度匹配和速度蒸馏两个目标来优化模型。

**技术框架**：整体架构包括两个主要模块：速度匹配（VM）和速度蒸馏（VD）。VM用于稳定地匹配学生和教师模型之间的速度场，而VD则利用已学习的速度场进行概率密度蒸馏。

**关键创新**：本研究的关键创新在于将优化目标从传输层面转化为速度和分布层面，解决了直接学习速度场的不可行性，显著提升了3D生成的效率。

**关键设计**：在损失函数设计上，采用了速度匹配和速度蒸馏的组合，确保了模型在少步采样时的稳定性和准确性，同时优化了网络结构以适应新的目标。

## 📊 实验亮点

实验结果显示，MDT-dist方法在TRELLIS框架上将每个流变换器的采样步骤从25减少到1或2，分别实现了0.68秒和0.94秒的延迟，速度提升幅度达到9.0x和6.5x，且保持了高视觉和几何保真度，显著优于现有的CM蒸馏方法。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发以及计算机图形学等领域，能够显著提升3D生成模型的效率和质量，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Flow-based 3D generation models typically require dozens of sampling steps during inference. Though few-step distillation methods, particularly Consistency Models (CMs), have achieved substantial advancements in accelerating 2D diffusion models, they remain under-explored for more complex 3D generation tasks. In this study, we propose a novel framework, MDT-dist, for few-step 3D flow distillation. Our approach is built upon a primary objective: distilling the pretrained model to learn the Marginal-Data Transport. Directly learning this objective needs to integrate the velocity fields, while this integral is intractable to be implemented. Therefore, we propose two optimizable objectives, Velocity Matching (VM) and Velocity Distillation (VD), to equivalently convert the optimization target from the transport level to the velocity and the distribution level respectively. Velocity Matching (VM) learns to stably match the velocity fields between the student and the teacher, but inevitably provides biased gradient estimates. Velocity Distillation (VD) further enhances the optimization process by leveraging the learned velocity fields to perform probability density distillation. When evaluated on the pioneer 3D generation framework TRELLIS, our method reduces sampling steps of each flow transformer from 25 to 1 or 2, achieving 0.68s (1 step x 2) and 0.94s (2 steps x 2) latency with 9.0x and 6.5x speedup on A800, while preserving high visual and geometric fidelity. Extensive experiments demonstrate that our method significantly outperforms existing CM distillation methods, and enables TRELLIS to achieve superior performance in few-step 3D generation.

