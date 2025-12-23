---
layout: default
title: Aerial Multi-View Stereo via Adaptive Depth Range Inference and Normal Cues
---

# Aerial Multi-View Stereo via Adaptive Depth Range Inference and Normal Cues

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05655" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05655v1</a>
  <a href="https://arxiv.org/pdf/2506.05655.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05655v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05655v1', 'Aerial Multi-View Stereo via Adaptive Depth Range Inference and Normal Cues')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yimei Liu, Yakun Ju, Yuan Rao, Hao Fan, Junyu Dong, Feng Gao, Qian Du

**分类**: cs.CV, eess.IV

**发布日期**: 2025-06-06

**备注**: IEEE TGRS 2025

---

## 💡 一句话要点

**提出自适应深度范围MVS以解决航空多视图立体重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `多视图立体` `深度估计` `航空图像` `几何线索` `深度范围预测` `法线引导` `城市重建` `计算机视觉`

## 📋 核心要点

1. 现有的多视图立体重建方法未能有效处理航空图像中的深度范围变化和特征匹配问题。
2. 本文提出的自适应深度范围MVS（ADR-MVS）通过单目几何线索来改善深度估计的准确性。
3. 实验结果显示，ADR-MVS在多个数据集上表现出色，超越了现有技术，且计算复杂度更低。

## 📝 摘要（中文）

三维数字城市重建是多视角航空图像的重要应用，深度多视图立体（MVS）方法在此领域优于传统技术。然而，现有方法往往忽视航空与近距离设置之间的关键差异，如沿极线的深度范围变化及低细节航空图像的特征匹配不敏感。为了解决这些问题，本文提出了一种自适应深度范围MVS（ADR-MVS），通过整合单目几何线索来提高多视图深度估计的准确性。ADR-MVS的关键组件是深度范围预测器，它利用交叉注意力差异学习生成自适应范围图。实验结果表明，ADR-MVS在WHU、LuoJia-MVS和慕尼黑数据集上实现了最先进的性能，并展现出优越的计算复杂度。

## 🔬 方法详解

**问题定义**：本文旨在解决航空多视图立体重建中的深度估计不准确和特征匹配困难等问题。现有方法在处理航空图像时，常常忽略了深度范围的变化和低细节特征的影响。

**核心思路**：ADR-MVS的核心思想是通过单目几何线索来增强深度估计的准确性，利用深度范围预测器生成自适应范围图，从而改善特征匹配的可辨别性。

**技术框架**：ADR-MVS的整体架构包括多个阶段，首先通过单目线索生成初步的范围图，随后逐步收窄范围图，最终与级联MVS框架对接以实现精确的深度回归。

**关键创新**：最重要的创新在于引入了深度范围预测器和基于法线引导的成本聚合操作，显著提升了航空立体图像的几何感知能力，与现有的RGB引导方法相比，效果更佳。

**关键设计**：在技术细节上，采用了交叉注意力差异学习来生成范围图，并设计了法线引导的成本聚合模块，以增强成本体积中的几何信息。

## 📊 实验亮点

实验结果表明，ADR-MVS在WHU、LuoJia-MVS和慕尼黑数据集上均取得了最先进的性能，相较于基线方法，深度估计精度提升了XX%，并且在计算复杂度上表现出明显优势。

## 🎯 应用场景

该研究在城市三维重建、无人机航拍图像处理及地理信息系统等领域具有广泛的应用潜力。通过提高航空图像的深度估计精度，能够为城市规划、环境监测及灾后重建等提供更为准确的数据支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Three-dimensional digital urban reconstruction from multi-view aerial images is a critical application where deep multi-view stereo (MVS) methods outperform traditional techniques. However, existing methods commonly overlook the key differences between aerial and close-range settings, such as varying depth ranges along epipolar lines and insensitive feature-matching associated with low-detailed aerial images. To address these issues, we propose an Adaptive Depth Range MVS (ADR-MVS), which integrates monocular geometric cues to improve multi-view depth estimation accuracy. The key component of ADR-MVS is the depth range predictor, which generates adaptive range maps from depth and normal estimates using cross-attention discrepancy learning. In the first stage, the range map derived from monocular cues breaks through predefined depth boundaries, improving feature-matching discriminability and mitigating convergence to local optima. In later stages, the inferred range maps are progressively narrowed, ultimately aligning with the cascaded MVS framework for precise depth regression. Moreover, a normal-guided cost aggregation operation is specially devised for aerial stereo images to improve geometric awareness within the cost volume. Finally, we introduce a normal-guided depth refinement module that surpasses existing RGB-guided techniques. Experimental results demonstrate that ADR-MVS achieves state-of-the-art performance on the WHU, LuoJia-MVS, and München datasets, while exhibits superior computational complexity.

