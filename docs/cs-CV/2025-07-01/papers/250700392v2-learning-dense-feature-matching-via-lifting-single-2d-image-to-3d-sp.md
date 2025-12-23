---
layout: default
title: Learning Dense Feature Matching via Lifting Single 2D Image to 3D Space
---

# Learning Dense Feature Matching via Lifting Single 2D Image to 3D Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00392" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00392v2</a>
  <a href="https://arxiv.org/pdf/2507.00392.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00392v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00392v2', 'Learning Dense Feature Matching via Lifting Single 2D Image to 3D Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingping Liang, Yutao Hu, Wenqi Shao, Ying Fu

**分类**: cs.CV

**发布日期**: 2025-07-01 (更新: 2025-07-05)

**备注**: Official Code: https://github.com/Sharpiless/L2M

---

## 💡 一句话要点

**提出L2M框架以解决单视图图像特征匹配问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `特征匹配` `计算机视觉` `3D感知` `单视图图像` `多视图合成` `深度学习` `鲁棒性` `泛化能力`

## 📋 核心要点

1. 现有特征匹配方法依赖于稀缺的多视图图像，限制了其在复杂场景中的应用。
2. 提出的L2M框架通过将2D图像提升至3D空间，利用单视图图像进行特征匹配。
3. 实验结果表明，L2M在零样本评估基准上表现优异，展示了其良好的泛化能力。

## 📝 摘要（中文）

特征匹配在许多计算机视觉任务中起着基础性作用，但现有方法依赖于稀缺且干净的多视图图像集合，限制了其在多样化和具有挑战性的场景中的泛化能力。此外，传统特征编码器通常在单视图2D图像上训练，限制了其捕捉3D感知对应关系的能力。本文提出了一种新颖的两阶段框架，将2D图像提升至3D空间，称为Lift to Match (L2M)，充分利用大规模和多样化的单视图图像。在第一阶段，我们通过多视图图像合成和3D特征高斯表示的结合，学习了一个3D感知特征编码器，将3D几何知识注入编码器。第二阶段采用新视图渲染策略，结合从单视图图像生成的大规模合成数据，学习特征解码器以实现稳健的特征匹配，从而在不同领域中实现泛化。大量实验表明，我们的方法在零样本评估基准上实现了优越的泛化能力，突显了所提框架在稳健特征匹配中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有特征匹配方法对多视图图像的依赖，导致其在复杂场景中的泛化能力不足的问题。现有方法通常在单视图2D图像上训练，无法有效捕捉3D对应关系。

**核心思路**：本文提出的L2M框架通过将2D图像提升至3D空间，利用多视图图像合成和3D特征表示，增强特征编码器的3D感知能力，从而实现更为稳健的特征匹配。

**技术框架**：L2M框架分为两个阶段：第一阶段学习3D感知特征编码器，第二阶段通过新视图渲染策略和合成数据生成学习特征解码器。整体流程包括数据准备、特征编码、特征解码和匹配。

**关键创新**：最重要的创新在于将2D图像提升至3D空间的过程，使得特征编码器能够融入3D几何知识，显著提升了特征匹配的鲁棒性和泛化能力。

**关键设计**：在特征编码器中，采用多视图图像合成和3D特征高斯表示相结合的方式，设计了特定的损失函数以优化3D特征的学习，同时在特征解码器中使用新视图渲染策略以增强特征匹配的效果。

## 📊 实验亮点

实验结果显示，L2M框架在多个零样本评估基准上表现优异，相较于传统方法，特征匹配的准确率提升了XX%，展示了其在复杂场景中的强大泛化能力和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、增强现实和机器人视觉等，能够在多样化和复杂的环境中实现高效的特征匹配。未来，L2M框架有望推动计算机视觉领域的进一步发展，尤其是在缺乏多视图数据的情况下，提升特征匹配的可靠性和准确性。

## 📄 摘要（原文）

> Feature matching plays a fundamental role in many computer vision tasks, yet existing methods heavily rely on scarce and clean multi-view image collections, which constrains their generalization to diverse and challenging scenarios. Moreover, conventional feature encoders are typically trained on single-view 2D images, limiting their capacity to capture 3D-aware correspondences. In this paper, we propose a novel two-stage framework that lifts 2D images to 3D space, named as \textbf{Lift to Match (L2M)}, taking full advantage of large-scale and diverse single-view images. To be specific, in the first stage, we learn a 3D-aware feature encoder using a combination of multi-view image synthesis and 3D feature Gaussian representation, which injects 3D geometry knowledge into the encoder. In the second stage, a novel-view rendering strategy, combined with large-scale synthetic data generation from single-view images, is employed to learn a feature decoder for robust feature matching, thus achieving generalization across diverse domains. Extensive experiments demonstrate that our method achieves superior generalization across zero-shot evaluation benchmarks, highlighting the effectiveness of the proposed framework for robust feature matching.

