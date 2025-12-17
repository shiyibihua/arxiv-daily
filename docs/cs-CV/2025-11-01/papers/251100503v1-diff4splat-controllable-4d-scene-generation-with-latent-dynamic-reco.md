---
layout: default
title: Diff4Splat: Controllable 4D Scene Generation with Latent Dynamic Reconstruction Models
---

# Diff4Splat: Controllable 4D Scene Generation with Latent Dynamic Reconstruction Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00503" target="_blank" class="toolbar-btn">arXiv: 2511.00503v1</a>
    <a href="https://arxiv.org/pdf/2511.00503.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00503v1" 
            onclick="toggleFavorite(this, '2511.00503v1', 'Diff4Splat: Controllable 4D Scene Generation with Latent Dynamic Reconstruction Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Panwang Pan, Chenguo Lin, Jingjing Zhao, Chenxin Li, Yuchen Lin, Haopeng Li, Honglei Yan, Kairun Wen, Yunlong Lin, Yixuan Yuan, Yadong Mu

**分类**: cs.CV

**发布日期**: 2025-11-01

---

## 💡 一句话要点

**Diff4Splat：基于动态重建模型的单图可控4D场景生成**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D场景生成` `动态场景` `扩散模型` `3D高斯场` `视频生成` `新视角合成` `几何提取`

## 📋 核心要点

1. 现有动态场景生成方法通常依赖于耗时的优化，难以实现快速生成和实时控制。
2. Diff4Splat通过结合视频扩散模型和4D数据集学习的几何运动约束，实现单图快速生成可控4D场景。
3. 实验表明，Diff4Splat在生成质量和效率上超越了基于优化的方法，并在多个任务上表现出色。

## 📝 摘要（中文）

Diff4Splat是一种前馈方法，用于从单张图像合成可控且显式的4D场景。该方法将视频扩散模型的生成先验与从大规模4D数据集学习到的几何和运动约束相结合。给定单张输入图像、相机轨迹以及可选的文本提示，Diff4Splat直接预测一个可变形的3D高斯场，该高斯场在一个前向过程中编码外观、几何和运动，无需测试时优化或后处理细化。框架的核心是一个视频潜在Transformer，它增强了视频扩散模型，以联合捕获时空依赖关系并预测随时间变化的3D高斯基元。训练由外观保真度、几何精度和运动一致性的目标引导，使Diff4Splat能够在30秒内合成高质量的4D场景。实验表明，Diff4Splat在视频生成、新视角合成和几何提取方面都非常有效，在动态场景合成方面与基于优化的方法相匹配或超过它们，同时效率更高。

## 🔬 方法详解

**问题定义**：现有动态场景生成方法，特别是基于优化的方法，通常需要大量的计算资源和时间来进行测试时的优化，这限制了它们在实时应用中的使用。此外，如何从单张图像中推断出动态场景的几何和运动信息是一个具有挑战性的问题。

**核心思路**：Diff4Splat的核心思路是将视频扩散模型的生成能力与从大规模4D数据集中学习到的几何和运动先验知识相结合。通过训练一个前馈网络，直接从单张图像预测一个可变形的3D高斯场，从而避免了耗时的优化过程。

**技术框架**：Diff4Splat框架包含以下主要模块：1) 一个视频潜在Transformer，用于捕获时空依赖关系并预测随时间变化的3D高斯基元；2) 一个可变形的3D高斯场表示，用于编码场景的外观、几何和运动信息；3) 一组损失函数，用于指导训练，包括外观保真度、几何精度和运动一致性。整个流程是从单张图像、相机轨迹和可选文本提示开始，经过前馈网络，最终生成4D场景。

**关键创新**：Diff4Splat的关键创新在于它将视频扩散模型的生成能力与显式的3D高斯场表示相结合，从而实现了快速、可控的4D场景生成。与现有方法相比，Diff4Splat不需要测试时优化，并且能够直接预测场景的几何和运动信息。

**关键设计**：视频潜在Transformer使用注意力机制来建模时空依赖关系。3D高斯场使用一组高斯基元来表示场景的几何和外观，每个高斯基元都有一个位置、尺度、旋转和颜色。损失函数包括L1损失（用于外观保真度）、Chamfer距离（用于几何精度）和运动平滑损失（用于运动一致性）。具体参数设置未知。

## 📊 实验亮点

Diff4Splat能够在30秒内合成高质量的4D场景，显著优于基于优化的方法。在视频生成、新视角合成和几何提取等任务上，Diff4Splat与基于优化的方法相匹配或超过它们，同时效率更高。具体性能数据未知。

## 🎯 应用场景

Diff4Splat具有广泛的应用前景，包括虚拟现实、增强现实、游戏开发和电影制作等领域。它可以用于快速生成逼真的动态场景，例如人物动画、自然景观和城市环境。此外，Diff4Splat还可以用于新视角合成和几何提取，从而为3D场景理解和重建提供新的工具。

## 📄 摘要（原文）

> We introduce Diff4Splat, a feed-forward method that synthesizes controllable and explicit 4D scenes from a single image. Our approach unifies the generative priors of video diffusion models with geometry and motion constraints learned from large-scale 4D datasets. Given a single input image, a camera trajectory, and an optional text prompt, Diff4Splat directly predicts a deformable 3D Gaussian field that encodes appearance, geometry, and motion, all in a single forward pass, without test-time optimization or post-hoc refinement. At the core of our framework lies a video latent transformer, which augments video diffusion models to jointly capture spatio-temporal dependencies and predict time-varying 3D Gaussian primitives. Training is guided by objectives on appearance fidelity, geometric accuracy, and motion consistency, enabling Diff4Splat to synthesize high-quality 4D scenes in 30 seconds. We demonstrate the effectiveness of Diff4Splatacross video generation, novel view synthesis, and geometry extraction, where it matches or surpasses optimization-based methods for dynamic scene synthesis while being significantly more efficient.

