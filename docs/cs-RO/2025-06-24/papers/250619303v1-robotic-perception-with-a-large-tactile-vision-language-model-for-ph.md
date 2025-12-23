---
layout: default
title: Robotic Perception with a Large Tactile-Vision-Language Model for Physical Property Inference
---

# Robotic Perception with a Large Tactile-Vision-Language Model for Physical Property Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19303" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19303v1</a>
  <a href="https://arxiv.org/pdf/2506.19303.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19303v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19303v1', 'Robotic Perception with a Large Tactile-Vision-Language Model for Physical Property Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zexiang Guo, Hengxiang Chen, Xinheng Mai, Qiusang Qiu, Gan Ma, Zhanat Kappassov, Qiang Li, Nutan Chen

**分类**: cs.RO

**发布日期**: 2025-06-24

**备注**: This paper has been accepted by the 2025 International Conference on Climbing and Walking Robots (CLAWAR). These authors contributed equally to this work: Zexiang Guo, Hengxiang Chen, Xinheng Mai

---

## 💡 一句话要点

**提出跨模态感知框架以解决物理属性推断问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `触觉感知` `视觉-触觉融合` `物理属性推断` `多模态集成` `机器人感知`

## 📋 核心要点

1. 现有方法通常仅依赖触觉或视觉数据，无法全面捕捉物体的物理属性，限制了机器人的操作能力。
2. 本文提出了一种跨模态感知框架，结合视觉观察与触觉表示，利用多模态视觉-语言模型进行物理属性推断。
3. 在对35种物体的评估中，提出的方法在性能上超越了现有基线，并表现出良好的零样本泛化能力。

## 📝 摘要（中文）

推断物理属性能够显著提升机器人操作能力，使其通过自适应抓取策略安全高效地处理物体。以往的方法通常依赖于触觉或视觉数据，限制了对物体属性的全面捕捉。本文提出了一种新颖的跨模态感知框架，将视觉观察与触觉表示整合在一个多模态视觉-语言模型中。我们的物理推理框架采用分层特征对齐机制和精细化提示策略，使模型能够做出与真实测量高度相关的属性特定预测。在对35种多样化物体的评估中，我们的方法超越了现有基线，并展示了强大的零样本泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在物理属性推断中的局限性，现有方法仅依赖单一模态（触觉或视觉），无法全面理解物体特性。

**核心思路**：提出的跨模态感知框架通过整合视觉和触觉数据，利用多模态视觉-语言模型进行物理属性推断，以提高机器人的操作安全性和效率。

**技术框架**：整体架构包括数据采集、特征提取、特征对齐和属性推断四个主要模块。首先收集视觉和触觉数据，然后通过分层特征对齐机制进行融合，最后进行属性预测。

**关键创新**：最重要的创新在于引入了分层特征对齐机制和精细化提示策略，使得模型能够针对特定属性进行高效预测，与传统方法相比，显著提升了预测的准确性和可靠性。

**关键设计**：在模型设计中，采用了多模态融合的损失函数，优化了特征对齐的参数设置，并设计了适应不同物体属性的网络结构，以确保模型在多样化物体上的有效性。

## 📊 实验亮点

在对35种多样化物体的评估中，提出的方法在物理属性推断上超越了现有基线，表现出显著的性能提升，尤其在零样本泛化能力方面，展示了强大的适应性和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化仓储、物体识别与分类等。通过提升机器人对物体物理属性的理解能力，可以在复杂环境中实现更安全高效的操作，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Inferring physical properties can significantly enhance robotic manipulation by enabling robots to handle objects safely and efficiently through adaptive grasping strategies. Previous approaches have typically relied on either tactile or visual data, limiting their ability to fully capture properties. We introduce a novel cross-modal perception framework that integrates visual observations with tactile representations within a multimodal vision-language model. Our physical reasoning framework, which employs a hierarchical feature alignment mechanism and a refined prompting strategy, enables our model to make property-specific predictions that strongly correlate with ground-truth measurements. Evaluated on 35 diverse objects, our approach outperforms existing baselines and demonstrates strong zero-shot generalization. Keywords: tactile perception, visual-tactile fusion, physical property inference, multimodal integration, robot perception

