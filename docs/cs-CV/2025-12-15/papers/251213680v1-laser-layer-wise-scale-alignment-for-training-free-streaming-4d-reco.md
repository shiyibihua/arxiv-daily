---
layout: default
title: LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction
---

# LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.13680" target="_blank" class="toolbar-btn">arXiv: 2512.13680v1</a>
    <a href="https://arxiv.org/pdf/2512.13680.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13680v1" 
            onclick="toggleFavorite(this, '2512.13680v1', 'LASER: Layer-wise Scale Alignment for Training-Free Streaming 4D Reconstruction')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianye Ding, Yiming Xie, Yiqing Liang, Moitreya Chatterjee, Pedro Miraldo, Huaizu Jiang

**分类**: cs.CV

**发布日期**: 2025-12-15

**备注**: 16 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://neu-vi.github.io/LASER/)

---

## 💡 一句话要点

**提出LASER以解决流媒体4D重建中的训练需求问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `流媒体重建` `深度学习` `几何先验` `实时视频处理` `相机姿态估计` `点图重建` `无训练框架`

## 📋 核心要点

1. 现有的重建模型在处理流媒体视频时面临内存复杂度高的问题，限制了其实际应用。
2. LASER通过层级尺度对齐技术，将离线重建模型转化为流媒体系统，避免了重新训练的需求。
3. 实验结果显示，LASER在相机姿态估计和点图重建上达到了最先进的性能，且运行效率高。

## 📝 摘要（中文）

近年来，VGGT和$π^3$等前馈重建模型在重建质量上取得了显著进展，但由于其二次内存复杂度，无法处理流媒体视频，限制了实际应用。现有的流媒体方法通过学习的记忆机制或因果注意力来解决这一问题，但需要大量的重新训练，并且可能无法充分利用最先进的离线模型的几何先验。为此，本文提出LASER，一个无训练的框架，通过对连续时间窗口的预测进行对齐，将离线重建模型转换为流媒体系统。我们观察到简单的相似变换对齐由于层深度不对齐而失败，因此引入了分层尺度对齐，计算每层的尺度因子，并在相邻窗口和时间戳之间传播。实验表明，LASER在相机姿态估计和点图重建质量上达到了最先进的性能，同时在RTX A6000 GPU上以14 FPS的速度运行，具备了实际应用于千米级流媒体视频的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有重建模型在处理流媒体视频时的高内存需求和训练复杂性问题。现有方法往往需要大量的重新训练，且未能充分利用离线模型的几何先验。

**核心思路**：LASER的核心思路是通过层级尺度对齐，将离线重建模型转换为流媒体系统，避免了训练过程中的复杂性。通过对连续时间窗口的预测进行对齐，解决了深度不一致性的问题。

**技术框架**：LASER框架主要包括三个模块：1) 深度预测分层，将深度信息分为多个层次；2) 计算每层的尺度因子；3) 在相邻时间窗口之间传播这些尺度因子，以实现一致的深度重建。

**关键创新**：LASER的关键创新在于引入了层级尺度对齐技术，解决了简单相似变换对齐失败的问题。这一方法与现有的流媒体重建方法相比，显著提高了深度预测的一致性。

**关键设计**：在设计中，LASER采用了分层深度预测机制，确保每层的尺度因子能够准确计算并有效传播。此外，系统在内存使用上进行了优化，使其在高效运行的同时保持高重建质量。

## 📊 实验亮点

LASER在相机姿态估计和点图重建方面达到了最先进的性能，运行速度为14 FPS，内存峰值为6 GB，显著优于现有的流媒体重建方法。这一成果展示了LASER在实际应用中的可行性和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括实时视频监控、无人驾驶汽车的环境感知以及虚拟现实中的场景重建等。LASER的高效性和准确性使其在处理大规模流媒体视频时具有实际价值，未来可能推动相关技术的广泛应用。

## 📄 摘要（原文）

> Recent feed-forward reconstruction models like VGGT and $π^3$ achieve impressive reconstruction quality but cannot process streaming videos due to quadratic memory complexity, limiting their practical deployment. While existing streaming methods address this through learned memory mechanisms or causal attention, they require extensive retraining and may not fully leverage the strong geometric priors of state-of-the-art offline models. We propose LASER, a training-free framework that converts an offline reconstruction model into a streaming system by aligning predictions across consecutive temporal windows. We observe that simple similarity transformation ($\mathrm{Sim}(3)$) alignment fails due to layer depth misalignment: monocular scale ambiguity causes relative depth scales of different scene layers to vary inconsistently between windows. To address this, we introduce layer-wise scale alignment, which segments depth predictions into discrete layers, computes per-layer scale factors, and propagates them across both adjacent windows and timestamps. Extensive experiments show that LASER achieves state-of-the-art performance on camera pose estimation and point map reconstruction %quality with offline models while operating at 14 FPS with 6 GB peak memory on a RTX A6000 GPU, enabling practical deployment for kilometer-scale streaming videos. Project website: $\href{https://neu-vi.github.io/LASER/}{\texttt{https://neu-vi.github.io/LASER/}}$

