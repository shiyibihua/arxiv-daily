---
layout: default
title: Physically Plausible Data Augmentations for Wearable IMU-based Human Activity Recognition Using Physics Simulation
---

# Physically Plausible Data Augmentations for Wearable IMU-based Human Activity Recognition Using Physics Simulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13284" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13284v1</a>
  <a href="https://arxiv.org/pdf/2508.13284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13284v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13284v1', 'Physically Plausible Data Augmentations for Wearable IMU-based Human Activity Recognition Using Physics Simulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nobuyuki Oishi, Philip Birch, Daniel Roggen, Paula Lago

**分类**: cs.LG, cs.HC

**发布日期**: 2025-08-18

**备注**: 12 pages, 4 figures

---

## 💡 一句话要点

**提出物理可行的数据增强方法以解决传感器基础的人体活动识别问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `人体活动识别` `数据增强` `物理模拟` `深度学习` `传感器技术` `运动捕捉` `合成数据`

## 📋 核心要点

1. 现有的基于信号变换的数据增强方法在物理可行性方面存在不足，可能导致增强数据与原始标签不一致。
2. 本文提出的物理可行数据增强（PPDA）利用物理模拟技术，结合真实的人体运动数据，增强数据的多样性和真实性。
3. 实验结果显示，PPDA方法在多个数据集上显著提升了模型性能，宏观F1分数平均提高3.7个百分点，且减少了对训练数据的需求。

## 📝 摘要（中文）

传感器基础的人体活动识别（HAR）中，高质量标注数据的稀缺限制了模型性能和在真实场景中的泛化能力。数据增强是缓解这一问题的关键策略。现有的基于信号变换的数据增强（STDA）方法常常缺乏物理可行性，可能导致增强数据无法保留原始活动标签的意义。本文提出了一种基于物理模拟的物理可行数据增强（PPDA），通过运动捕捉或视频姿态估计的数据，结合物理模拟引入多种现实变异性。实验结果表明，PPDA在三个公共数据集上相较于传统STDA方法，宏观F1分数平均提高了3.7个百分点，且在训练主体数量减少60%的情况下仍能保持竞争力。

## 🔬 方法详解

**问题定义**：本文旨在解决传感器基础的人体活动识别中高质量标注数据稀缺的问题。现有的信号变换数据增强方法（STDA）往往缺乏物理可行性，导致生成的数据可能无法准确反映活动标签的真实含义。

**核心思路**：论文提出的物理可行数据增强（PPDA）通过物理模拟技术，结合运动捕捉或视频姿态估计的数据，生成更真实的增强数据。这种方法旨在引入多种现实变异性，从而提升数据的多样性和真实性。

**技术框架**：PPDA的整体架构包括数据采集、物理模拟和数据增强三个主要模块。首先，通过运动捕捉或视频姿态估计获取人体运动数据；然后，利用物理模拟技术对数据进行处理，生成多样化的增强数据；最后，将增强数据用于训练深度学习模型。

**关键创新**：PPDA的主要创新在于其物理可行性，通过物理模拟生成的数据能够更好地保留原始活动标签的意义，与传统的STDA方法相比，PPDA在数据增强的真实性和有效性上具有显著优势。

**关键设计**：在技术细节上，PPDA采用了多种物理模拟参数设置，以确保生成的数据能够反映真实的运动特征。此外，损失函数设计上也考虑了增强数据与原始数据之间的一致性，以提高模型的训练效果。

## 📊 实验亮点

实验结果表明，PPDA方法在三个公共数据集上相较于传统STDA方法，宏观F1分数平均提高了3.7个百分点，最高可达13个百分点。同时，在训练主体数量减少60%的情况下，PPDA仍能保持竞争力，显示出其在数据增强中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能穿戴设备、健康监测和运动分析等。通过生成高质量的合成数据，PPDA可以有效降低对标注数据的需求，促进深度学习模型在实际应用中的推广与应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The scarcity of high-quality labeled data in sensor-based Human Activity Recognition (HAR) hinders model performance and limits generalization across real-world scenarios. Data augmentation is a key strategy to mitigate this issue by enhancing the diversity of training datasets. Signal Transformation-based Data Augmentation (STDA) techniques have been widely used in HAR. However, these methods are often physically implausible, potentially resulting in augmented data that fails to preserve the original meaning of the activity labels. In this study, we introduce and systematically characterize Physically Plausible Data Augmentation (PPDA) enabled by physics simulation. PPDA leverages human body movement data from motion capture or video-based pose estimation and incorporates various realistic variabilities through physics simulation, including modifying body movements, sensor placements, and hardware-related effects. We compare the performance of PPDAs with traditional STDAs on three public datasets of daily activities and fitness workouts. First, we evaluate each augmentation method individually, directly comparing PPDAs to their STDA counterparts. Next, we assess how combining multiple PPDAs can reduce the need for initial data collection by varying the number of subjects used for training. Experiments show consistent benefits of PPDAs, improving macro F1 scores by an average of 3.7 pp (up to 13 pp) and achieving competitive performance with up to 60% fewer training subjects than STDAs. As the first systematic study of PPDA in sensor-based HAR, these results highlight the advantages of pursuing physical plausibility in data augmentation and the potential of physics simulation for generating synthetic Inertial Measurement Unit data for training deep learning HAR models. This cost-effective and scalable approach therefore helps address the annotation scarcity challenge in HAR.

