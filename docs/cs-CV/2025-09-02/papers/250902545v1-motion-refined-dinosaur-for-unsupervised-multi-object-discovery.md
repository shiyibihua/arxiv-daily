---
layout: default
title: Motion-Refined DINOSAUR for Unsupervised Multi-Object Discovery
---

# Motion-Refined DINOSAUR for Unsupervised Multi-Object Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02545" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02545v1</a>
  <a href="https://arxiv.org/pdf/2509.02545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02545v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02545v1', 'Motion-Refined DINOSAUR for Unsupervised Multi-Object Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinrui Gong, Oliver Hahn, Christoph Reich, Krishnakant Singh, Simone Schaub-Meyer, Daniel Cremers, Stefan Roth

**分类**: cs.CV

**发布日期**: 2025-09-02

**备注**: To appear at ICCVW 2025. Xinrui Gong and Oliver Hahn - both authors contributed equally. Code: https://github.com/visinf/mr-dinosaur

---

## 💡 一句话要点

**提出Motion-Refined DINOSAUR，用于无监督多目标发现，无需伪标签。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `无监督学习` `多目标发现` `目标中心学习` `运动分割` `光流估计`

## 📋 核心要点

1. 现有无监督多目标发现方法依赖伪标签，而伪标签的生成通常需要一定程度的监督，限制了其无监督的程度。
2. MR-DINOSAUR利用无相机运动帧的光流运动分割生成高质量伪标签，并以此细化DINOSAUR的slot表示，实现真正的无监督学习。
3. 实验表明，MR-DINOSAUR在TRI-PD和KITTI数据集上超越了之前的state-of-the-art方法，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种名为Motion-Refined DINOSAUR (MR-DINOSAUR) 的无监督多目标发现(MOD)方法，旨在无需任何人工监督的情况下，检测和定位视觉场景中不同的目标实例。现有方法通常利用目标中心学习(OCL)和视频中的运动线索来识别单个目标，但依赖于监督信息生成伪标签来训练OCL模型。MR-DINOSAUR扩展了自监督预训练的OCL模型DINOSAUR，通过检索无相机运动的视频帧，并对无监督光流进行运动分割，生成高质量的无监督伪标签。利用这些伪标签细化DINOSAUR的slot表示，并训练一个slot停用模块，将slot分配给前景和背景。实验表明，MR-DINOSAUR在TRI-PD和KITTI数据集上取得了强大的多目标发现结果，优于之前的state-of-the-art方法，且完全无监督。

## 🔬 方法详解

**问题定义**：无监督多目标发现旨在无需人工标注的情况下，从图像或视频中自动检测和分割出不同的目标实例。现有基于目标中心学习的方法通常需要伪标签来训练模型，而这些伪标签的生成过程往往依赖于一定程度的监督信息，例如人工设计的先验知识或启发式规则，这限制了方法的无监督性。因此，如何设计一种完全无监督的多目标发现方法是一个关键挑战。

**核心思路**：MR-DINOSAUR的核心思路是利用视频中的运动信息来生成高质量的无监督伪标签，并以此来指导目标中心学习模型的训练。具体来说，该方法选择无相机运动的视频帧，因为在这些帧中，场景中的运动主要由独立运动的目标引起，从而可以通过运动分割来区分前景目标和背景。这种方法避免了对人工设计的先验知识或启发式规则的依赖，实现了真正的无监督学习。

**技术框架**：MR-DINOSAUR的整体框架包括以下几个主要步骤：1) 利用自监督预训练的DINOSAUR模型提取图像的slot表示；2) 检索无相机运动的视频帧；3) 对这些帧进行无监督光流估计和运动分割，生成伪标签；4) 利用伪标签细化DINOSAUR的slot表示，训练一个slot停用模块，将slot分配给前景和背景。

**关键创新**：MR-DINOSAUR最重要的创新点在于其完全无监督的伪标签生成方法。通过选择无相机运动的视频帧，并利用无监督光流估计和运动分割，该方法能够自动生成高质量的伪标签，而无需任何人工干预或先验知识。这使得该方法能够真正实现无监督的多目标发现。

**关键设计**：在伪标签生成方面，论文使用了预训练的光流估计模型来计算视频帧之间的光流，并使用一种基于聚类的运动分割算法将光流场分割成不同的运动区域。在模型训练方面，论文设计了一个slot停用模块，该模块通过学习一个二元掩码来控制每个slot是否应该被激活，从而将slot分配给前景或背景。损失函数包括一个用于细化slot表示的对比损失和一个用于训练slot停用模块的交叉熵损失。

## 📊 实验亮点

MR-DINOSAUR在TRI-PD和KITTI数据集上取得了显著的成果。在TRI-PD数据集上，MR-DINOSAUR的性能超越了之前的state-of-the-art方法，且无需任何人工监督。在KITTI数据集上，MR-DINOSAUR也取得了具有竞争力的结果，证明了其在真实场景中的有效性。这些结果表明，MR-DINOSAUR是一种有效的无监督多目标发现方法。

## 🎯 应用场景

MR-DINOSAUR在机器人感知、自动驾驶、视频监控等领域具有广泛的应用前景。例如，在自动驾驶中，它可以用于无监督地学习车辆、行人等目标的表示，从而提高感知系统的鲁棒性和泛化能力。在机器人操作中，它可以用于无监督地发现和分割场景中的物体，从而实现更智能的物体抓取和操作。

## 📄 摘要（原文）

> Unsupervised multi-object discovery (MOD) aims to detect and localize distinct object instances in visual scenes without any form of human supervision. Recent approaches leverage object-centric learning (OCL) and motion cues from video to identify individual objects. However, these approaches use supervision to generate pseudo labels to train the OCL model. We address this limitation with MR-DINOSAUR -- Motion-Refined DINOSAUR -- a minimalistic unsupervised approach that extends the self-supervised pre-trained OCL model, DINOSAUR, to the task of unsupervised multi-object discovery. We generate high-quality unsupervised pseudo labels by retrieving video frames without camera motion for which we perform motion segmentation of unsupervised optical flow. We refine DINOSAUR's slot representations using these pseudo labels and train a slot deactivation module to assign slots to foreground and background. Despite its conceptual simplicity, MR-DINOSAUR achieves strong multi-object discovery results on the TRI-PD and KITTI datasets, outperforming the previous state of the art despite being fully unsupervised.

