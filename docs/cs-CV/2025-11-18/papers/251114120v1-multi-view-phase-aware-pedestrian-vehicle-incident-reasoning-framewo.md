---
layout: default
title: Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning Framework with Vision-Language Models
---

# Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning Framework with Vision-Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.14120" target="_blank" class="toolbar-btn">arXiv: 2511.14120v1</a>
    <a href="https://arxiv.org/pdf/2511.14120.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14120v1" 
            onclick="toggleFavorite(this, '2511.14120v1', 'Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning Framework with Vision-Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hao Zhen, Yunxiang Yang, Jidong J. Yang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-18

**备注**: 23 pages, 4 figures, 3 tables

---

## 💡 一句话要点

**提出MP-PVIR框架，利用多视角和视觉-语言模型解决行人-车辆事故的推理问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多视角视频` `行人-车辆事故` `视觉-语言模型` `行为阶段分割` `交通安全` `事件推理` `智能交通系统`

## 📋 核心要点

1. 现有基于视频的行人-车辆事故检测系统缺乏对事件发展过程的深入理解，尤其是在行人行为的不同认知阶段。
2. MP-PVIR框架通过将多视角视频流分解为不同的认知阶段，并在每个阶段进行同步分析，从而实现更细粒度的事件推理。
3. 实验结果表明，MP-PVIR框架在行为阶段分割和多视角分析方面取得了显著的性能提升，并能生成可操作的交通安全建议。

## 📝 摘要（中文）

行人-车辆事故是城市安全面临的严峻挑战。虽然现有的视频系统可以检测到事故发生，但缺乏对行人行为不同认知阶段的事件发展过程的深入理解。本文提出了多视角相位感知行人-车辆事故推理（MP-PVIR）框架，该框架通过四个阶段将多视角视频流处理成结构化的诊断报告：（1）事件触发的多视角视频采集；（2）行人行为阶段分割；（3）阶段特定的多视角推理；（4）分层综合和诊断推理。该框架通过自动将事件分割成认知阶段，在每个阶段执行同步的多视角分析，并将结果综合成具有针对性预防策略的因果链，从而实现行为理论的应用。特别是，两个专门的视觉-语言模型支撑MP-PVIR流程：用于行为阶段分割的TG-VLM（mIoU = 0.4881）和用于阶段感知多视角分析的PhaVR-VLM（captioning score为33.063，问答准确率高达64.70%）。最后，使用指定的大型语言模型生成全面的报告，详细说明场景理解、行为解释、因果推理和预防建议。在Woven Traffic Safety数据集上的评估表明，MP-PVIR有效地将多视角视频数据转化为可操作的见解，从而推进了用于车辆-基础设施协同系统的AI驱动的交通安全分析。

## 🔬 方法详解

**问题定义**：论文旨在解决行人-车辆事故分析中，现有方法无法有效利用多视角信息和缺乏对行人行为认知阶段理解的问题。现有方法通常孤立地处理视频，忽略了事件发生的时间结构和多视角关联，导致对事故原因和发展过程的理解不足。

**核心思路**：论文的核心思路是将行人-车辆事故分解为不同的认知阶段，并在每个阶段利用多视角信息进行分析和推理。通过这种方式，可以更准确地理解事故发生的原因和过程，并制定更有针对性的预防措施。论文还利用视觉-语言模型（VLM）来增强对视频内容的理解和推理能力。

**技术框架**：MP-PVIR框架包含四个主要阶段：（1）事件触发的多视角视频采集，用于获取事故发生时的多视角视频数据；（2）行人行为阶段分割，使用TG-VLM将事故过程分割为不同的认知阶段；（3）阶段特定的多视角推理，使用PhaVR-VLM在每个阶段进行多视角分析和推理；（4）分层综合和诊断推理，使用大型语言模型生成全面的事故报告，包括场景理解、行为解释、因果推理和预防建议。

**关键创新**：该论文的关键创新在于提出了一个统一的框架，能够系统地处理多视角视频流，并将其转化为结构化的诊断报告。此外，论文还提出了两个专门的视觉-语言模型（TG-VLM和PhaVR-VLM），用于行为阶段分割和阶段感知的多视角分析。将行为理论融入到AI驱动的交通安全分析中，是另一个重要的创新点。

**关键设计**：TG-VLM用于行为阶段分割，其具体网络结构和损失函数未知，但目标是最大化阶段分割的准确率（mIoU）。PhaVR-VLM用于阶段感知的多视角分析，其具体网络结构和损失函数也未知，但目标是提高captioning score和问答准确率。大型语言模型用于生成事故报告，其具体模型选择和prompt设计未知，但目标是生成全面、准确和可操作的报告。

## 📊 实验亮点

MP-PVIR框架在Woven Traffic Safety数据集上进行了评估，实验结果表明，TG-VLM在行为阶段分割方面取得了0.4881的mIoU，PhaVR-VLM在阶段感知的多视角分析方面取得了33.063的captioning score和高达64.70%的问答准确率。这些结果表明，MP-PVIR框架能够有效地将多视角视频数据转化为可操作的见解。

## 🎯 应用场景

该研究成果可应用于智能交通系统、自动驾驶安全、城市规划和交通管理等领域。通过对行人-车辆事故的深入分析，可以为车辆-基础设施协同系统提供更有效的安全保障，减少交通事故的发生，并为城市交通规划提供数据支持，从而提升城市交通安全水平。

## 📄 摘要（原文）

> Pedestrian-vehicle incidents remain a critical urban safety challenge, with pedestrians accounting for over 20% of global traffic fatalities. Although existing video-based systems can detect when incidents occur, they provide little insight into how these events unfold across the distinct cognitive phases of pedestrian behavior. Recent vision-language models (VLMs) have shown strong potential for video understanding, but they remain limited in that they typically process videos in isolation, without explicit temporal structuring or multi-view integration. This paper introduces Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning (MP-PVIR), a unified framework that systematically processes multi-view video streams into structured diagnostic reports through four stages: (1) event-triggered multi-view video acquisition, (2) pedestrian behavior phase segmentation, (3) phase-specific multi-view reasoning, and (4) hierarchical synthesis and diagnostic reasoning. The framework operationalizes behavioral theory by automatically segmenting incidents into cognitive phases, performing synchronized multi-view analysis within each phase, and synthesizing results into causal chains with targeted prevention strategies. Particularly, two specialized VLMs underpin the MP-PVIR pipeline: TG-VLM for behavioral phase segmentation (mIoU = 0.4881) and PhaVR-VLM for phase-aware multi-view analysis, achieving a captioning score of 33.063 and up to 64.70% accuracy on question answering. Finally, a designated large language model is used to generate comprehensive reports detailing scene understanding, behavior interpretation, causal reasoning, and prevention recommendations. Evaluation on the Woven Traffic Safety dataset shows that MP-PVIR effectively translates multi-view video data into actionable insights, advancing AI-driven traffic safety analytics for vehicle-infrastructure cooperative systems.

