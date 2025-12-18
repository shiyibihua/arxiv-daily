---
layout: default
title: EHWGesture -- A dataset for multimodal understanding of clinical gestures
---

# EHWGesture -- A dataset for multimodal understanding of clinical gestures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07525" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07525v1</a>
  <a href="https://arxiv.org/pdf/2509.07525.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07525v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07525v1', 'EHWGesture -- A dataset for multimodal understanding of clinical gestures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gianluca Amprimo, Alberto Ancilotto, Alessandro Savino, Fabio Quazzolo, Claudia Ferraris, Gabriella Olmo, Elisabetta Farella, Stefano Di Carlo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-09

**备注**: Accepted at ICCV 2025 Workshop on AI-driven Skilled Activity Understanding, Assessment & Feedback Generation

---

## 💡 一句话要点

**EHWGesture：用于临床手势多模态理解的数据集**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `临床手势理解` `多模态数据集` `手部关键点追踪` `动作质量评估` `RGB-D相机` `事件相机` `人机交互`

## 📋 核心要点

1. 动态手势理解因其复杂的时空变化而充满挑战，现有数据集缺乏多模态、多视角数据以及精确的真值追踪。
2. EHWGesture数据集利用RGB-D相机、事件相机和运动捕捉系统，提供多模态数据和精确的手部关键点真值，并包含动作质量评估。
3. 基线实验表明，EHWGesture数据集在手势分类、手势触发检测和动作质量评估方面具有潜力，可作为临床手势理解的基准。

## 📝 摘要（中文）

本文提出了EHWGesture，一个用于手势理解的多模态视频数据集，专注于五个临床相关的手势。该数据集包含超过1100个录制视频（6小时），由25名健康受试者使用两个高分辨率RGB-Depth相机和一个事件相机采集。同时，利用运动捕捉系统提供精确的手部关键点追踪真值。所有设备经过空间校准和同步，确保跨模态对齐。为了将动作质量评估融入手势理解，录制视频按照执行速度分类，模拟临床手部灵巧性评估。基线实验验证了该数据集在手势分类、手势触发检测和动作质量评估方面的潜力。EHWGesture有望成为推进多模态临床手势理解的综合基准。

## 🔬 方法详解

**问题定义**：现有手势理解数据集在临床应用方面存在不足，尤其是在动态手势理解中，缺乏多模态信息、多视角数据以及精确的动作质量评估。这限制了深度学习模型在临床手部灵巧性自动评估等方面的应用。现有方法难以有效捕捉手势的时空变化和细微的动作质量差异。

**核心思路**：本文的核心思路是构建一个包含多模态信息、精确真值和动作质量标签的临床手势数据集，从而为训练和评估更强大的手势理解模型提供基础。通过结合RGB-D相机、事件相机和运动捕捉系统，全面捕捉手势的视觉信息和运动信息。

**技术框架**：EHWGesture数据集的构建流程包括以下几个主要阶段：1) 数据采集：使用RGB-D相机、事件相机和运动捕捉系统同步记录25名受试者执行五个临床相关手势的视频。2) 数据校准：对所有设备进行空间校准和时间同步，确保跨模态数据对齐。3) 真值标注：利用运动捕捉系统提供精确的手部关键点追踪真值。4) 动作质量分类：根据执行速度将录制视频分为不同类别，模拟临床手部灵巧性评估。

**关键创新**：EHWGesture数据集的关键创新在于其多模态性、精确真值和动作质量评估的结合。与现有数据集相比，EHWGesture提供了更全面的手势信息，包括RGB-D图像、事件数据和精确的手部关键点位置。此外，动作质量分类的引入使得该数据集能够用于训练和评估能够理解手势动作质量的模型。

**关键设计**：数据集中使用了两个高分辨率RGB-D相机和一个事件相机，以捕捉不同视角的视觉信息。运动捕捉系统用于提供精确的手部关键点追踪真值，确保标注的准确性。数据集中的手势按照执行速度分为不同类别，模拟临床手部灵巧性评估，从而可以训练模型来评估动作质量。

## 📊 实验亮点

EHWGesture数据集包含超过1100个录制视频，总时长达6小时，涵盖五个临床相关的手势。基线实验表明，该数据集在手势分类、手势触发检测和动作质量评估方面具有潜力。例如，在手势分类任务中，基于该数据集训练的模型取得了具有竞争力的性能。这些结果验证了EHWGesture数据集作为临床手势理解基准的价值。

## 🎯 应用场景

EHWGesture数据集可广泛应用于人机交互、临床评估和康复训练等领域。例如，可用于开发自动化的手部灵巧性评估系统，辅助医生进行诊断和治疗方案制定。此外，该数据集还可用于开发基于手势的交互界面，提升用户体验。未来，该数据集有望推动临床手势理解技术的发展，为医疗健康领域带来更多创新应用。

## 📄 摘要（原文）

> Hand gesture understanding is essential for several applications in human-computer interaction, including automatic clinical assessment of hand dexterity. While deep learning has advanced static gesture recognition, dynamic gesture understanding remains challenging due to complex spatiotemporal variations. Moreover, existing datasets often lack multimodal and multi-view diversity, precise ground-truth tracking, and an action quality component embedded within gestures. This paper introduces EHWGesture, a multimodal video dataset for gesture understanding featuring five clinically relevant gestures. It includes over 1,100 recordings (6 hours), captured from 25 healthy subjects using two high-resolution RGB-Depth cameras and an event camera. A motion capture system provides precise ground-truth hand landmark tracking, and all devices are spatially calibrated and synchronized to ensure cross-modal alignment. Moreover, to embed an action quality task within gesture understanding, collected recordings are organized in classes of execution speed that mirror clinical evaluations of hand dexterity. Baseline experiments highlight the dataset's potential for gesture classification, gesture trigger detection, and action quality assessment. Thus, EHWGesture can serve as a comprehensive benchmark for advancing multimodal clinical gesture understanding.

