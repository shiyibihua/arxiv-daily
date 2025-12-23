---
layout: default
title: Accurate and efficient zero-shot 6D pose estimation with frozen foundation models
---

# Accurate and efficient zero-shot 6D pose estimation with frozen foundation models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09784" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09784v1</a>
  <a href="https://arxiv.org/pdf/2506.09784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09784v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09784v1', 'Accurate and efficient zero-shot 6D pose estimation with frozen foundation models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrea Caraffa, Davide Boscaini, Fabio Poiesi

**分类**: cs.CV

**发布日期**: 2025-06-11

**备注**: Technical report

---

## 💡 一句话要点

**提出FreeZeV2以解决零-shot 6D姿态估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `6D姿态估计` `零-shot学习` `计算机视觉` `机器人技术` `增强现实` `特征提取` `模块化设计`

## 📋 核心要点

1. 现有方法在零-shot 6D姿态估计中面临泛化能力不足和计算资源消耗大的挑战。
2. FreeZeV2通过无训练的方法，利用预训练的基础模型，实现对未见物体的强泛化能力，提升了准确性和效率。
3. 在BOP基准测试中，FreeZeV2相比FreeZe实现了8倍的速度提升和5%的准确性提升，展示了其优越性。

## 📝 摘要（中文）

从RGBD数据中估计物体的6D姿态是计算机视觉中的一个基本问题，广泛应用于机器人技术和增强现实。现有方法通常依赖于针对特定任务的合成数据进行训练，消耗大量计算资源。为了解决这一问题，本文提出了FreeZeV2，这是一种无训练的方法，通过利用在无关数据上预训练的几何和视觉基础模型，实现对未见物体的强泛化能力。FreeZeV2在准确性和效率上均优于其前身FreeZe，主要贡献包括稀疏特征提取策略、特征感知评分机制和模块化设计。实验结果表明，FreeZeV2在BOP基准的七个核心数据集上建立了新的6D姿态估计的最先进水平。

## 🔬 方法详解

**问题定义**：本文旨在解决从RGBD数据中进行零-shot 6D姿态估计的问题。现有方法通常依赖于大量合成数据进行特定任务的训练，导致计算资源消耗巨大且泛化能力不足。

**核心思路**：FreeZeV2提出了一种无训练的方法，通过利用在无关数据上预训练的几何和视觉基础模型，来实现对未见物体的强泛化能力。这种设计旨在减少对特定任务训练的依赖，从而提高效率和准确性。

**技术框架**：FreeZeV2的整体架构包括三个主要模块：稀疏特征提取模块、特征感知评分机制和模块化设计。稀疏特征提取模块负责在推理时减少计算量，特征感知评分机制则用于优化RANSAC基础的3D配准过程中的姿态选择和候选姿态的最终排名。模块化设计允许集成多个实例分割模型，从而增强对分割掩膜错误的鲁棒性。

**关键创新**：FreeZeV2的主要创新在于其无训练的特性和高效的特征提取策略，与现有方法相比，显著降低了计算需求，同时保持了高准确性。

**关键设计**：在设计中，FreeZeV2采用了稀疏特征提取策略，优化了推理过程中的计算效率。此外，特征感知评分机制通过考虑特征信息来提升姿态选择的准确性，模块化设计则增强了系统的灵活性和鲁棒性。具体的参数设置和损失函数细节在论文中有详细描述。

## 📊 实验亮点

FreeZeV2在BOP基准测试中表现出色，相比FreeZe实现了8倍的速度提升和5%的准确性提升。当使用多个分割模型集成时，准确性进一步提升8%，同时运行速度仍比FreeZe快2.5倍。这些结果表明FreeZeV2在零-shot 6D姿态估计中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、增强现实和自动驾驶等。通过提高6D姿态估计的准确性和效率，FreeZeV2能够在实际场景中更好地处理未见物体的识别与定位，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Estimating the 6D pose of objects from RGBD data is a fundamental problem in computer vision, with applications in robotics and augmented reality. A key challenge is achieving generalization to novel objects that were not seen during training. Most existing approaches address this by scaling up training on synthetic data tailored to the task, a process that demands substantial computational resources. But is task-specific training really necessary for accurate and efficient 6D pose estimation of novel objects? To answer No!, we introduce FreeZeV2, the second generation of FreeZe: a training-free method that achieves strong generalization to unseen objects by leveraging geometric and vision foundation models pre-trained on unrelated data. FreeZeV2 improves both accuracy and efficiency over FreeZe through three key contributions: (i) a sparse feature extraction strategy that reduces inference-time computation without sacrificing accuracy; (ii) a feature-aware scoring mechanism that improves both pose selection during RANSAC-based 3D registration and the final ranking of pose candidates; and (iii) a modular design that supports ensembles of instance segmentation models, increasing robustness to segmentation masks errors. We evaluate FreeZeV2 on the seven core datasets of the BOP Benchmark, where it establishes a new state-of-the-art in 6D pose estimation of unseen objects. When using the same segmentation masks, FreeZeV2 achieves a remarkable 8x speedup over FreeZe while also improving accuracy by 5%. When using ensembles of segmentation models, FreeZeV2 gains an additional 8% in accuracy while still running 2.5x faster than FreeZe. FreeZeV2 was awarded Best Overall Method at the BOP Challenge 2024.

