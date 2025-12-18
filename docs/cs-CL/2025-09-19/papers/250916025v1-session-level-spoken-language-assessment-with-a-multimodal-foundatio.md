---
layout: default
title: Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning
---

# Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16025" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16025v1</a>
  <a href="https://arxiv.org/pdf/2509.16025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16025v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16025v1', 'Session-Level Spoken Language Assessment with a Multimodal Foundation Model via Multi-Target Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hong-Yun Lin, Jhen-Ke Lin, Chung-Chun Wang, Hao-Chien Lu, Berlin Chen

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-19

**备注**: Copyright 2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works

---

## 💡 一句话要点

**提出基于多模态基础模型和多目标学习的会话级口语评估方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `口语评估` `多模态学习` `基础模型` `多目标学习` `语音识别` `计算机辅助语言学习`

## 📋 核心要点

1. 现有口语评估方法依赖级联pipeline或短音频窗口，存在误差传播和忽略语篇信息的不足。
2. 提出一种基于多模态基础模型的方法，结合多目标学习和语音先验，实现会话级整体评估。
3. 实验表明，该方法优于现有技术，具有良好的泛化能力，适用于计算机辅助语言学习。

## 📝 摘要（中文）

口语评估（SLA）旨在评估学习者在自然语音中的口语能力。随着第二语言为英语的学习者数量不断增长，对可靠SLA的需求也日益增加，这对于计算机辅助语言学习（CALL）至关重要。现有的方法通常依赖于级联pipeline，容易产生误差传播，或者使用短音频窗口的端到端模型，可能忽略语篇层面的证据。本文提出了一种新颖的多模态基础模型方法，可以在单次处理中执行会话级别的评估。我们的方法将多目标学习与基于冻结的Whisper ASR模型的语音先验相结合，用于声学感知校准，从而可以在不依赖手工特征的情况下，联合学习SLA的整体和特征级别目标。通过连贯地处理L2学习者的整个回答会话，该模型擅长预测整体口语能力。在Speak & Improve基准上进行的实验表明，我们提出的方法优于先前的最先进的级联系统，并表现出强大的跨部分泛化能力，从而产生了一个紧凑的可部署的评分器，专为CALL应用而设计。

## 🔬 方法详解

**问题定义**：现有口语评估方法主要存在两个痛点。一是依赖于级联的pipeline，例如先进行语音识别，再提取语言特征，最后进行评分。这种方式容易导致误差在各个阶段之间传播，降低整体评估的准确性。二是现有的端到端模型通常只处理短音频窗口，无法捕捉到会话级别的语篇信息，例如连贯性、逻辑性等，这些信息对于评估口语能力至关重要。

**核心思路**：本文的核心思路是利用多模态基础模型，直接对整个会话进行建模，从而避免误差传播和捕捉语篇信息。具体来说，作者利用预训练的Whisper ASR模型作为语音先验，并结合多目标学习，同时预测整体口语能力和各个细粒度的语言特征。这样可以充分利用语音信息，并学习到更鲁棒的特征表示。

**技术框架**：该方法的技术框架主要包括以下几个模块：1) Whisper ASR模型：用于提取语音特征，并进行声学感知校准。2) 多目标学习模块：用于同时预测整体口语能力和各个细粒度的语言特征。3) 融合模块：用于将语音特征和文本特征进行融合，得到最终的特征表示。整个流程是端到端的，可以直接对整个会话进行建模。

**关键创新**：该方法最重要的技术创新点在于将多模态基础模型和多目标学习相结合，用于会话级别的口语评估。与现有方法相比，该方法可以避免误差传播，捕捉语篇信息，并学习到更鲁棒的特征表示。此外，利用预训练的Whisper ASR模型作为语音先验，可以充分利用语音信息，提高评估的准确性。

**关键设计**：在关键设计方面，作者使用了冻结的Whisper ASR模型，以保证语音特征的稳定性和泛化能力。在多目标学习方面，作者使用了不同的损失函数来优化整体口语能力和各个细粒度的语言特征。此外，作者还设计了一个融合模块，用于将语音特征和文本特征进行融合。具体的网络结构和参数设置在论文中有详细描述。

## 📊 实验亮点

该方法在Speak & Improve基准测试中取得了显著的成果，超越了先前的最先进的级联系统。实验结果表明，该方法不仅在整体口语能力评估方面表现出色，而且具有很强的跨部分泛化能力。这表明该方法能够有效地捕捉到口语能力的核心特征，并能够适应不同的语料和场景。

## 🎯 应用场景

该研究成果可广泛应用于计算机辅助语言学习（CALL）领域，为L2英语学习者提供自动化的口语评估服务。它可以用于在线口语练习、模拟考试、以及个性化学习路径推荐等方面，帮助学习者更有效地提高口语能力。此外，该技术还可以应用于招聘面试、语言能力认证等场景，具有重要的实际应用价值和广阔的市场前景。

## 📄 摘要（原文）

> Spoken Language Assessment (SLA) estimates a learner's oral proficiency from spontaneous speech. The growing population of L2 English speakers has intensified the demand for reliable SLA, a critical component of Computer Assisted Language Learning (CALL). Existing efforts often rely on cascaded pipelines, which are prone to error propagation, or end-to-end models that often operate on a short audio window, which might miss discourse-level evidence. This paper introduces a novel multimodal foundation model approach that performs session-level evaluation in a single pass. Our approach couples multi-target learning with a frozen, Whisper ASR model-based speech prior for acoustic-aware calibration, allowing for jointly learning holistic and trait-level objectives of SLA without resorting to handcrafted features. By coherently processing the entire response session of an L2 speaker, the model excels at predicting holistic oral proficiency. Experiments conducted on the Speak & Improve benchmark demonstrate that our proposed approach outperforms the previous state-of-the-art cascaded system and exhibits robust cross-part generalization, producing a compact deployable grader that is tailored for CALL applications.

