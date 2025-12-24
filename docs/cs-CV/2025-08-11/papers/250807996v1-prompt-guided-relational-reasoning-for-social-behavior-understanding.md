---
layout: default
title: Prompt-Guided Relational Reasoning for Social Behavior Understanding with Vision Foundation Models
---

# Prompt-Guided Relational Reasoning for Social Behavior Understanding with Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07996" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07996v1</a>
  <a href="https://arxiv.org/pdf/2508.07996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07996v1', 'Prompt-Guided Relational Reasoning for Social Behavior Understanding with Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thinesh Thiyakesan Ponbagavathi, Chengzheng Yang, Alina Roitberg

**分类**: cs.CV

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出ProGraD以解决群体活动检测中的社交行为理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `群体活动检测` `社交行为理解` `视觉基础模型` `Transformer` `可解释性` `多模态学习` `深度学习`

## 📋 核心要点

1. 现有的群体活动检测方法主要依赖于特定任务的架构，且在使用视觉基础模型时未能显著提升性能。
2. 论文提出的ProGraD方法通过学习群体提示和GroupContext Transformer实现对社交配置的引导和推理。
3. 在两个GAD基准上，ProGraD在复杂多群体场景中表现优异，提升幅度达到6.5%和8.2%。

## 📝 摘要（中文）

群体活动检测（GAD）涉及在视频中识别社交群体及其集体行为。尽管视觉基础模型（VFM）如DinoV2提供了优秀的特征，但其主要在物体中心数据上进行预训练，尚未充分探索用于建模群体动态。我们提出了基于提示的群体活动检测方法（ProGraD），通过可学习的群体提示引导VFM关注社交配置，以及轻量级的两层GroupContext Transformer推断演员与群体的关联及集体行为。我们在两个GAD基准上评估了该方法，尤其在复杂的多群体场景中，ProGraD显示出显著的性能提升，且生成可解释的注意力图，提供了对演员与群体推理的洞察。

## 🔬 方法详解

**问题定义**：本论文旨在解决群体活动检测中的社交行为理解问题。现有方法在使用视觉基础模型时，未能有效捕捉群体动态，导致性能提升有限。

**核心思路**：ProGraD方法通过引入可学习的群体提示，指导视觉基础模型关注社交配置，同时利用轻量级的GroupContext Transformer推断演员与群体的关系，增强模型的群体意识。

**技术框架**：整体架构包括两个主要模块：可学习的群体提示模块和GroupContext Transformer。前者用于引导模型注意力，后者负责推断群体行为和演员关联。

**关键创新**：ProGraD的核心创新在于结合了可学习的群体提示与轻量级Transformer结构，显著提升了对复杂多群体场景的理解能力，与传统方法相比，提供了更为灵活和高效的解决方案。

**关键设计**：在设计中，ProGraD使用了仅10M的可训练参数，且通过特定的损失函数优化群体提示的学习效果，确保模型在多群体场景中具备较强的推理能力。该方法还生成可解释的注意力图，帮助理解模型的决策过程。

## 📊 实验亮点

在两个GAD基准上，ProGraD方法超越了现有的最先进技术，尤其在复杂的多群体场景中，Group mAP@1.0提升了6.5%，Group mAP@0.5提升了8.2%。该方法仅使用10M的可训练参数，显示出高效性与可扩展性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在社交行为分析、视频监控、智能交通和人机交互等领域。通过提升群体活动检测的准确性，ProGraD能够为社会行为理解提供更深入的洞察，促进相关技术的发展与应用。

## 📄 摘要（原文）

> Group Activity Detection (GAD) involves recognizing social groups and their collective behaviors in videos. Vision Foundation Models (VFMs), like DinoV2, offer excellent features, but are pretrained primarily on object-centric data and remain underexplored for modeling group dynamics. While they are a promising alternative to highly task-specific GAD architectures that require full fine-tuning, our initial investigation reveals that simply swapping CNN backbones used in these methods with VFMs brings little gain, underscoring the need for structured, group-aware reasoning on top.
>   We introduce Prompt-driven Group Activity Detection (ProGraD) -- a method that bridges this gap through 1) learnable group prompts to guide the VFM attention toward social configurations, and 2) a lightweight two-layer GroupContext Transformer that infers actor-group associations and collective behavior. We evaluate our approach on two recent GAD benchmarks: Cafe, which features multiple concurrent social groups, and Social-CAD, which focuses on single-group interactions. While we surpass state-of-the-art in both settings, our method is especially effective in complex multi-group scenarios, where we yield a gain of 6.5\% (Group mAP\@1.0) and 8.2\% (Group mAP\@0.5) using only 10M trainable parameters. Furthermore, our experiments reveal that ProGraD produces interpretable attention maps, offering insights into actor-group reasoning. Code and models will be released.

