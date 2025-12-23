---
layout: default
title: Foundation Models for Zero-Shot Segmentation of Scientific Images without AI-Ready Data
---

# Foundation Models for Zero-Shot Segmentation of Scientific Images without AI-Ready Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24039" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24039v2</a>
  <a href="https://arxiv.org/pdf/2506.24039.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24039v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24039v2', 'Foundation Models for Zero-Shot Segmentation of Scientific Images without AI-Ready Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shubhabrata Mukherjee, Jack Lang, Obeen Kwon, Iryna Zenyuk, Valerie Brogden, Adam Weber, Daniela Ushizima

**分类**: cs.CV, cs.HC

**发布日期**: 2025-06-30 (更新: 2025-08-17)

**备注**: This paper has been accepted for presentation at the 59th International Conference on Parallel Processing (ICPP 2025), DRAI workshop

---

## 💡 一句话要点

**提出Zenesis以解决科学图像零-shot分割问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `零-shot分割` `科学图像` `计算机视觉` `多模态适应` `人机协作` `图像分析` `数据准备` `FIB-SEM`

## 📋 核心要点

1. 现有的零-shot模型在处理科学图像时面临数据稀缺和领域特定挑战，导致性能不足。
2. Zenesis通过无代码平台和多模态适应技术，实现了对原始科学数据的零-shot推理，提升了图像分割效率。
3. 在FIB-SEM数据集上，Zenesis的准确率达到0.987，显著优于传统方法和现有模型，展示了其有效性。

## 📝 摘要（中文）

零-shot和基于提示的模型在视觉推理任务中表现出色，但在稀疏和特定领域的科学图像数据上常常失败。我们提出了Zenesis，一个无代码的交互式计算机视觉平台，旨在减少科学成像工作流程中的数据准备瓶颈。Zenesis集成了轻量级的多模态适应，用于原始科学数据的零-shot推理、人机协作的精细化处理和基于启发式的时间增强。我们在催化剂负载膜的聚焦离子束扫描电子显微镜（FIB-SEM）数据集上验证了我们的方法，Zenesis的表现超越了基线，取得了0.947的平均准确率、0.858的交并比（IoU）和0.923的Dice系数，显示出显著的性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决科学图像分割中的数据准备不足问题，现有方法在处理稀疏和特定领域数据时表现不佳，导致无法有效进行图像分析。

**核心思路**：提出Zenesis平台，通过无代码交互和多模态适应技术，实现对原始科学数据的零-shot推理，降低对标注数据的依赖。

**技术框架**：Zenesis的整体架构包括数据输入模块、零-shot推理模块、人机协作精细化模块和时间增强模块，形成一个完整的科学成像工作流程。

**关键创新**：Zenesis的主要创新在于其轻量级的多模态适应能力，能够在没有预先标注数据的情况下，进行有效的图像分割，与传统方法相比，显著提高了处理效率和准确性。

**关键设计**：在技术细节上，Zenesis采用了特定的损失函数和网络结构，以优化分割性能，同时结合启发式方法进行时间增强，确保在不同类型的科学图像上均能保持高效表现。

## 📊 实验亮点

Zenesis在FIB-SEM数据集上取得了显著的实验结果，催化剂样本的平均准确率为0.947，IoU为0.858，Dice系数为0.923，而晶体样本的准确率更是达到0.987。这些结果远超传统的Otsu阈值法和现有的Segment Anything Model (SAM)，展示了其在科学图像分割中的优越性。

## 🎯 应用场景

Zenesis的研究成果在科学研究领域具有广泛的应用潜力，尤其是在材料科学、生物医学和化学等领域。它能够帮助研究人员在缺乏标注数据的情况下，快速进行图像分析和数据挖掘，从而加速科学发现的进程。

## 📄 摘要（原文）

> Zero-shot and prompt-based models have excelled at visual reasoning tasks by leveraging large-scale natural image corpora, but they often fail on sparse and domain-specific scientific image data. We introduce Zenesis, a no-code interactive computer vision platform designed to reduce data readiness bottlenecks in scientific imaging workflows. Zenesis integrates lightweight multimodal adaptation for zero-shot inference on raw scientific data, human-in-the-loop refinement, and heuristic-based temporal enhancement. We validate our approach on Focused Ion Beam Scanning Electron Microscopy (FIB-SEM) datasets of catalyst-loaded membranes. Zenesis outperforms baselines, achieving an average accuracy of 0.947, Intersection over Union (IoU) of 0.858, and Dice score of 0.923 on amorphous catalyst samples; and 0.987 accuracy, 0.857 IoU, and 0.923 Dice on crystalline samples. These results represent a significant performance gain over conventional methods such as Otsu thresholding and standalone models like the Segment Anything Model (SAM). Zenesis enables effective image segmentation in domains where annotated datasets are limited, offering a scalable solution for scientific discovery.

