---
layout: default
title: A biologically inspired separable learning vision model for real-time traffic object perception in Dark
---

# A biologically inspired separable learning vision model for real-time traffic object perception in Dark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05012" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05012v1</a>
  <a href="https://arxiv.org/pdf/2509.05012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05012v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05012v1', 'A biologically inspired separable learning vision model for real-time traffic object perception in Dark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hulin Li, Qiliang Ren, Jun Li, Hanbing Wei, Zheng Liu, Linfang Fan

**分类**: cs.CV

**发布日期**: 2025-09-05

**DOI**: [10.1016/j.eswa.2025.129529](https://doi.org/10.1016/j.eswa.2025.129529)

**🔗 代码/项目**: [GITHUB](https://github.com/alanli1997/slvm)

---

## 💡 一句话要点

**提出一种生物启发式可分离学习视觉模型，用于黑暗环境下的实时交通目标感知。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `低光照感知` `目标检测` `实例分割` `光流估计` `生物启发` `可分离学习` `交通场景` `深度学习`

## 📋 核心要点

1. 现有方法在低光照交通场景中目标感知面临光照退化和视觉线索不足的挑战，难以快速适应和准确预测。
2. 提出可分离学习视觉模型（SLVM），通过光自适应瞳孔机制、可分离学习策略和空间错位感知融合来增强低光照下的感知能力。
3. 实验表明，SLVM在Dark-traffic和LIS数据集上均取得了SOTA性能，并在目标检测、实例分割和光流估计任务上显著优于现有方法。

## 📝 摘要（中文）

在低光照交通场景中，快速准确的目标感知越来越受到关注。然而，由于严重的光照退化和缺乏可靠的视觉线索，现有的感知模型和方法难以快速适应并在低光照环境中进行准确预测。此外，目前缺乏专门针对低光照交通场景的大规模基准数据集。为了弥补这一差距，我们引入了一种基于物理原理的光照退化方法，该方法专为真实世界的低光照环境而设计，并构建了Dark-traffic，这是迄今为止最大的、密集注释的低光照交通场景数据集，支持目标检测、实例分割和光流估计。我们进一步提出了可分离学习视觉模型（SLVM），这是一种受生物学启发的框架，旨在增强恶劣光照条件下的感知能力。SLVM集成了四个关键组件：用于光照敏感特征提取的光自适应瞳孔机制、用于高效表示的特征级可分离学习策略、用于多任务可分离学习的任务特定解耦分支，以及用于精确多特征对齐的空间错位感知融合模块。大量实验表明，SLVM以更低的计算开销实现了最先进的性能。值得注意的是，在Dark-traffic数据集上，它在检测方面优于RT-DETR 11.2个百分点，在实例分割方面优于YOLOv12 6.1个百分点，并降低了基线的端点误差（EPE）12.37%。在LIS基准测试中，端到端训练的SLVM在关键指标上平均超过Swin Transformer+EnlightenGAN和ConvNeXt-T+EnlightenGAN 11个百分点，并超过Mask RCNN（具有光照增强）3.1个百分点。Dark-traffic数据集和完整代码已在https://github.com/alanli1997/slvm上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决低光照交通场景下目标感知精度和速度的问题。现有方法在光照严重退化的情况下，难以提取可靠的视觉特征，导致感知性能下降。同时，缺乏针对低光照场景的大规模数据集也限制了模型的训练和泛化能力。

**核心思路**：论文的核心思路是模仿生物视觉系统在光照变化下的适应机制，设计一种可分离学习的视觉模型。通过光自适应瞳孔机制模拟瞳孔对光照的调节作用，增强模型对光照变化的鲁棒性。采用可分离学习策略，降低计算复杂度，提高模型推理速度。

**技术框架**：SLVM整体框架包含四个主要模块：1) 光自适应瞳孔机制：用于提取光照敏感的特征；2) 特征级可分离学习策略：用于高效表示特征；3) 任务特定解耦分支：用于多任务可分离学习；4) 空间错位感知融合模块：用于精确的多特征对齐。模型首先通过光自适应模块提取特征，然后利用可分离学习策略进行特征表示，再通过解耦分支进行多任务学习，最后通过融合模块进行特征融合和预测。

**关键创新**：SLVM的关键创新在于其生物启发式的设计和可分离学习策略。光自适应瞳孔机制模拟了生物视觉系统对光照的调节作用，增强了模型对光照变化的鲁棒性。可分离学习策略将传统的卷积操作分解为多个可分离的卷积操作，降低了计算复杂度，提高了模型推理速度。

**关键设计**：光自适应瞳孔机制的具体实现未知，但推测可能包含可学习的参数来模拟瞳孔的收缩和扩张。可分离学习策略可能采用了深度可分离卷积或类似的结构。任务特定解耦分支的设计取决于具体的任务类型，例如目标检测、实例分割和光流估计。空间错位感知融合模块可能采用了注意力机制或可变形卷积等技术，用于对齐不同尺度的特征。

## 📊 实验亮点

SLVM在Dark-traffic数据集上，目标检测性能优于RT-DETR 11.2个百分点，实例分割性能优于YOLOv12 6.1个百分点，光流估计的端点误差（EPE）降低了12.37%。在LIS基准测试中，SLVM也显著优于Swin Transformer+EnlightenGAN和ConvNeXt-T+EnlightenGAN等模型，平均提升11个百分点。

## 🎯 应用场景

该研究成果可应用于智能交通系统、自动驾驶、安防监控等领域，尤其是在夜间或低光照环境下的目标检测、跟踪和识别。通过提高低光照条件下的感知能力，可以提升交通安全，减少事故发生率，并为自动驾驶车辆提供更可靠的环境感知。

## 📄 摘要（原文）

> Fast and accurate object perception in low-light traffic scenes has attracted increasing attention. However, due to severe illumination degradation and the lack of reliable visual cues, existing perception models and methods struggle to quickly adapt to and accurately predict in low-light environments. Moreover, there is the absence of available large-scale benchmark specifically focused on low-light traffic scenes. To bridge this gap, we introduce a physically grounded illumination degradation method tailored to real-world low-light settings and construct Dark-traffic, the largest densely annotated dataset to date for low-light traffic scenes, supporting object detection, instance segmentation, and optical flow estimation. We further propose the Separable Learning Vision Model (SLVM), a biologically inspired framework designed to enhance perception under adverse lighting. SLVM integrates four key components: a light-adaptive pupillary mechanism for illumination-sensitive feature extraction, a feature-level separable learning strategy for efficient representation, task-specific decoupled branches for multi-task separable learning, and a spatial misalignment-aware fusion module for precise multi-feature alignment. Extensive experiments demonstrate that SLVM achieves state-of-the-art performance with reduced computational overhead. Notably, it outperforms RT-DETR by 11.2 percentage points in detection, YOLOv12 by 6.1 percentage points in instance segmentation, and reduces endpoint error (EPE) of baseline by 12.37% on Dark-traffic. On the LIS benchmark, the end-to-end trained SLVM surpasses Swin Transformer+EnlightenGAN and ConvNeXt-T+EnlightenGAN by an average of 11 percentage points across key metrics, and exceeds Mask RCNN (with light enhancement) by 3.1 percentage points. The Dark-traffic dataset and complete code is released at https://github.com/alanli1997/slvm.

