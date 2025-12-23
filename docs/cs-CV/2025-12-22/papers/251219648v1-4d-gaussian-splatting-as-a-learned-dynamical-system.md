---
layout: default
title: 4D Gaussian Splatting as a Learned Dynamical System
---

# 4D Gaussian Splatting as a Learned Dynamical System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19648" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19648v1</a>
  <a href="https://arxiv.org/pdf/2512.19648.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19648v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19648v1', '4D Gaussian Splatting as a Learned Dynamical System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arnold Caleb Asiimwe, Carl Vondrick

**分类**: cs.CV

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**EvoGS：将4D高斯溅射重构为可学习的动态系统，实现时序一致性动态场景建模**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `4D高斯溅射` `动态场景建模` `神经动态场` `连续时间动态系统` `时间外推` `可控场景合成` `运动连贯性` `时间一致性`

## 📋 核心要点

1. 现有基于形变的4D高斯溅射方法在处理复杂动态场景时，存在运动不连贯和时间一致性差的问题。
2. EvoGS将4D高斯溅射视为连续时间动态系统，通过学习神经动态场来模拟场景运动，实现更自然的运动建模。
3. 实验表明，EvoGS在动态场景建模中，相比形变场基线，显著提升了运动连贯性和时间一致性，并支持时间外推和可控场景合成。

## 📝 摘要（中文）

本文将4D高斯溅射重新解释为一个连续时间的动态系统，其中场景运动源于对学习到的神经动态场的积分，而不是应用逐帧形变。这种被称为EvoGS的公式将高斯表示视为一个演化的物理系统，其状态在学习到的运动规律下连续演变。这解锁了基于形变的方法所不具备的能力：（1）通过对底层运动规律建模，实现从稀疏时间监督中进行样本高效学习；（2）时间外推，能够进行超出观察时间范围的前向和后向预测；（3）组合动力学，允许局部动力学注入以实现可控的场景合成。在动态场景基准上的实验表明，EvoGS相比于形变场基线，实现了更好的运动连贯性和时间一致性，同时保持了实时渲染。

## 🔬 方法详解

**问题定义**：现有4D高斯溅射方法通常采用逐帧形变来模拟动态场景，这种方法在处理复杂运动时容易出现运动不连贯和时间一致性问题。尤其是在稀疏时间监督下，形变场的泛化能力有限，难以准确预测未观测时间点的场景状态。此外，基于形变的方法难以实现对场景运动的精细控制和时间外推。

**核心思路**：EvoGS的核心思想是将4D高斯溅射视为一个连续时间动态系统，场景中的高斯粒子不再是简单地逐帧形变，而是根据学习到的神经动态场进行连续演化。通过对底层运动规律进行建模，EvoGS能够更好地捕捉场景的动态特性，从而提高运动连贯性和时间一致性。

**技术框架**：EvoGS的整体框架包括以下几个主要模块：1) 高斯粒子初始化：在初始时刻，使用一组高斯粒子来表示场景。2) 神经动态场学习：使用神经网络学习一个神经动态场，该场描述了高斯粒子在每个位置的速度和加速度。3) 动态系统积分：使用数值积分方法，根据学习到的神经动态场，对高斯粒子的状态进行连续时间演化。4) 渲染：在每个时间点，使用演化后的高斯粒子进行渲染，生成场景图像。

**关键创新**：EvoGS最重要的技术创新在于将4D高斯溅射与连续时间动态系统相结合。与传统的基于形变的方法相比，EvoGS能够直接学习场景的运动规律，从而更好地捕捉场景的动态特性。此外，EvoGS还支持时间外推和可控场景合成，这为动态场景建模提供了更大的灵活性。

**关键设计**：EvoGS的关键设计包括：1) 神经动态场的网络结构：可以使用MLP或其他神经网络结构来表示神经动态场。2) 损失函数：可以使用图像重建损失、运动平滑损失等来训练神经动态场。3) 数值积分方法：可以使用欧拉法、龙格-库塔法等数值积分方法来对高斯粒子的状态进行演化。4) 局部动力学注入：通过修改特定区域的神经动态场，可以实现对场景运动的局部控制。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19648v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19648v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19648v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EvoGS在动态场景基准测试中表现出色，相比于基于形变场的基线方法，在运动连贯性和时间一致性方面取得了显著提升。实验结果表明，EvoGS能够更好地捕捉场景的动态特性，生成更逼真的动态场景。此外，EvoGS还支持时间外推和可控场景合成，这为动态场景建模提供了更大的灵活性。

## 🎯 应用场景

EvoGS具有广泛的应用前景，例如：视频编辑、虚拟现实、增强现实、机器人导航等。它可以用于生成高质量的动态场景，实现逼真的虚拟体验。此外，EvoGS还可以用于预测未来场景状态，为机器人导航和决策提供支持。通过对场景运动进行精细控制，EvoGS还可以用于创建各种特效和动画。

## 📄 摘要（原文）

> We reinterpret 4D Gaussian Splatting as a continuous-time dynamical system, where scene motion arises from integrating a learned neural dynamical field rather than applying per-frame deformations. This formulation, which we call EvoGS, treats the Gaussian representation as an evolving physical system whose state evolves continuously under a learned motion law. This unlocks capabilities absent in deformation-based approaches:(1) sample-efficient learning from sparse temporal supervision by modeling the underlying motion law; (2) temporal extrapolation enabling forward and backward prediction beyond observed time ranges; and (3) compositional dynamics that allow localized dynamics injection for controllable scene synthesis. Experiments on dynamic scene benchmarks show that EvoGS achieves better motion coherence and temporal consistency compared to deformation-field baselines while maintaining real-time rendering

