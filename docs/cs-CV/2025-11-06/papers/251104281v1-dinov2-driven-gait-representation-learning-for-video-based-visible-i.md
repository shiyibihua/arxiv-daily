---
layout: default
title: DINOv2 Driven Gait Representation Learning for Video-Based Visible-Infrared Person Re-identification
---

# DINOv2 Driven Gait Representation Learning for Video-Based Visible-Infrared Person Re-identification

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.04281" target="_blank" class="toolbar-btn">arXiv: 2511.04281v1</a>
    <a href="https://arxiv.org/pdf/2511.04281.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04281v1" 
            onclick="toggleFavorite(this, '2511.04281v1', 'DINOv2 Driven Gait Representation Learning for Video-Based Visible-Infrared Person Re-identification')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yujie Yang, Shuang Li, Jun Ye, Neng Dong, Fan Li, Huafeng Li

**分类**: cs.CV

**发布日期**: 2025-11-06

---

## 💡 一句话要点

**提出DinoGRL框架，利用DINOv2驱动的步态特征学习，解决视频可见光-红外行人重识别问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频行人重识别` `可见光-红外` `步态特征学习` `DINOv2` `跨模态检索` `特征融合` `深度学习`

## 📋 核心要点

1. 现有VVI-ReID方法忽略了步态特征中蕴含的时空动态信息，限制了跨模态视频匹配的能力。
2. DinoGRL框架利用DINOv2的视觉先验学习步态特征，并设计SASGL和PBMGE模块增强特征表示。
3. 在HITSZ-VCM和BUPT数据集上，DinoGRL显著优于现有方法，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种DINOv2驱动的步态表示学习(DinoGRL)框架，用于解决基于视频的可见光-红外行人重识别(VVI-ReID)问题。现有方法侧重于利用模态不变的视觉特征，但忽略了步态特征，而步态特征不仅模态不变，而且富含时间动态信息，限制了它们对跨模态视频匹配至关重要的时空一致性进行建模的能力。DinoGRL框架利用DINOv2丰富的视觉先验知识来学习步态特征，作为外观线索的补充，从而促进了鲁棒的序列级跨模态检索表示。具体而言，我们引入了一个语义感知轮廓和步态学习(SASGL)模型，该模型利用DINOv2的通用语义先验生成并增强轮廓表示，并将其与ReID目标联合优化，以实现语义丰富的任务自适应步态特征学习。此外，我们开发了一个渐进式双向多粒度增强(PBMGE)模块，通过在多个空间粒度上实现步态和外观流之间的双向交互来逐步细化特征表示，充分利用它们的互补性来增强具有丰富局部细节的全局表示，并产生高度区分性的特征。在HITSZ-VCM和BUPT数据集上的大量实验表明了我们方法的优越性，显著优于现有的最先进方法。

## 🔬 方法详解

**问题定义**：视频可见光-红外行人重识别(VVI-ReID)旨在从视频序列中检索跨可见光和红外模态的同一行人。现有方法主要依赖于模态不变的视觉特征，但忽略了步态特征，而步态特征具有模态不变性和丰富的时序信息，对于跨模态视频匹配至关重要。因此，如何有效利用步态特征，提升VVI-ReID的性能是一个关键问题。

**核心思路**：本文的核心思路是利用预训练的DINOv2模型提供的视觉先验知识，来指导步态特征的学习，并将其与外观特征进行互补增强。通过这种方式，可以学习到更具判别性和鲁棒性的序列级特征表示，从而提升跨模态检索的准确率。

**技术框架**：DinoGRL框架主要包含两个核心模块：语义感知轮廓和步态学习(SASGL)模型和渐进式双向多粒度增强(PBMGE)模块。SASGL模型负责生成和增强轮廓表示，并利用DINOv2的语义先验进行指导。PBMGE模块则通过在多个空间粒度上进行步态和外观特征的双向交互，逐步细化特征表示。整体流程是首先通过SASGL学习步态特征，然后通过PBMGE将步态特征和外观特征融合增强，最后用于行人重识别。

**关键创新**：该论文的关键创新在于以下几点：1) 利用DINOv2的视觉先验来指导步态特征学习，这是一种新颖的思路，可以有效提升步态特征的质量。2) 提出了SASGL模型，能够生成和增强轮廓表示，并利用DINOv2的语义先验进行指导，从而学习到更具判别性的步态特征。3) 提出了PBMGE模块，通过在多个空间粒度上进行步态和外观特征的双向交互，能够充分利用它们的互补性，从而提升整体的特征表示能力。

**关键设计**：SASGL模型使用DINOv2提取的语义信息来增强轮廓表示，具体实现方式未知。PBMGE模块采用渐进式的方式，逐步融合不同粒度的特征，具体粒度划分和融合方式未知。损失函数方面，除了ReID的损失函数外，可能还使用了其他的辅助损失函数来约束步态特征的学习，具体细节未知。

## 📊 实验亮点

实验结果表明，DinoGRL框架在HITSZ-VCM和BUPT数据集上均取得了显著的性能提升，超越了现有的最先进方法。具体的性能数据和提升幅度在论文中给出，但摘要中未明确提及。这些结果验证了DinoGRL框架在VVI-ReID任务中的有效性。

## 🎯 应用场景

该研究成果可应用于智能安防、智慧城市等领域，例如在跨摄像头场景下进行行人追踪和身份识别。通过结合可见光和红外模态的信息，可以提高在光照条件不佳或存在遮挡情况下的行人重识别准确率，具有重要的实际应用价值。未来，该方法还可以扩展到其他模态的行人重识别任务中。

## 📄 摘要（原文）

> Video-based Visible-Infrared person re-identification (VVI-ReID) aims to retrieve the same pedestrian across visible and infrared modalities from video sequences. Existing methods tend to exploit modality-invariant visual features but largely overlook gait features, which are not only modality-invariant but also rich in temporal dynamics, thus limiting their ability to model the spatiotemporal consistency essential for cross-modal video matching. To address these challenges, we propose a DINOv2-Driven Gait Representation Learning (DinoGRL) framework that leverages the rich visual priors of DINOv2 to learn gait features complementary to appearance cues, facilitating robust sequence-level representations for cross-modal retrieval. Specifically, we introduce a Semantic-Aware Silhouette and Gait Learning (SASGL) model, which generates and enhances silhouette representations with general-purpose semantic priors from DINOv2 and jointly optimizes them with the ReID objective to achieve semantically enriched and task-adaptive gait feature learning. Furthermore, we develop a Progressive Bidirectional Multi-Granularity Enhancement (PBMGE) module, which progressively refines feature representations by enabling bidirectional interactions between gait and appearance streams across multiple spatial granularities, fully leveraging their complementarity to enhance global representations with rich local details and produce highly discriminative features. Extensive experiments on HITSZ-VCM and BUPT datasets demonstrate the superiority of our approach, significantly outperforming existing state-of-the-art methods.

