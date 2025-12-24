---
layout: default
title: Foundation Model for Skeleton-Based Human Action Understanding
---

# Foundation Model for Skeleton-Based Human Action Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12586" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12586v1</a>
  <a href="https://arxiv.org/pdf/2508.12586.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12586v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12586v1', 'Foundation Model for Skeleton-Based Human Action Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongsong Wang, Wanjiang Weng, Junbo Wang, Fang Zhao, Guo-Sen Xie, Xin Geng, Liang Wang

**分类**: cs.CV

**发布日期**: 2025-08-18

**备注**: Accepted by TPAMI, Code is available at: https://github.com/wengwanjiang/FoundSkelModel

---

## 💡 一句话要点

**提出统一骨架基础模型以解决人类动作理解问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `骨架动作理解` `密集表示学习` `Transformer` `特征去相关` `一致性训练` `多模态学习` `人机交互`

## 📋 核心要点

1. 现有骨架动作理解方法在可扩展性和泛化能力上存在不足，无法有效处理多样化的动作理解任务。
2. 本文提出的USDRL框架通过DSTE、MG-FD和MPCT模块，旨在提升骨架动作理解的准确性和鲁棒性。
3. 在25个基准测试中，USDRL在粗预测、密集预测和迁移预测任务上显著优于当前最先进的方法。

## 📝 摘要（中文）

人类动作理解是智能运动感知领域的基础支柱。骨架作为一种与设备无关的人类建模表示，具有广泛的应用潜力。然而，现有方法在处理多样化动作理解任务时缺乏可扩展性和泛化能力。本文提出了一种统一的骨架密集表示学习框架（USDRL），作为骨架基础模型。USDRL包括基于Transformer的密集时空编码器（DSTE）、多粒度特征去相关（MG-FD）和多视角一致性训练（MPCT）。通过在25个基准上进行广泛实验，USDRL显著超越了现有最先进的方法，推动了骨架动作理解的研究进展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有骨架动作理解方法在可扩展性和泛化能力上的不足，缺乏适应多样化任务的基础模型。

**核心思路**：提出统一骨架密集表示学习框架（USDRL），通过多模块协同工作，提升动作理解的准确性和信息提取能力。

**技术框架**：USDRL框架包含三个主要模块：DSTE用于学习时空特征，MG-FD用于特征去相关，MPCT用于多视角和多模态一致性训练。

**关键创新**：DSTE模块采用双流结构，分别捕捉时间动态和空间结构特征；MG-FD模块通过跨域协作减少冗余；MPCT模块增强高层语义学习。

**关键设计**：在DSTE中，采用Transformer架构；MG-FD通过特征去相关技术减少维度冗余；MPCT结合多视角和多模态自监督学习，提升信息提取效果。

## 📊 实验亮点

在25个基准测试中，USDRL在多个骨架动作理解任务上显著超越现有最先进的方法，尤其在密集预测任务中表现出色，提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

该研究在类人机器人控制和交互等领域具有广泛的应用潜力。通过提升骨架动作理解的准确性，USDRL可以促进人机交互的自然性和智能化，推动智能机器人在复杂环境中的应用。

## 📄 摘要（原文）

> Human action understanding serves as a foundational pillar in the field of intelligent motion perception. Skeletons serve as a modality- and device-agnostic representation for human modeling, and skeleton-based action understanding has potential applications in humanoid robot control and interaction. \RED{However, existing works often lack the scalability and generalization required to handle diverse action understanding tasks. There is no skeleton foundation model that can be adapted to a wide range of action understanding tasks}. This paper presents a Unified Skeleton-based Dense Representation Learning (USDRL) framework, which serves as a foundational model for skeleton-based human action understanding. USDRL consists of a Transformer-based Dense Spatio-Temporal Encoder (DSTE), Multi-Grained Feature Decorrelation (MG-FD), and Multi-Perspective Consistency Training (MPCT). The DSTE module adopts two parallel streams to learn temporal dynamic and spatial structure features. The MG-FD module collaboratively performs feature decorrelation across temporal, spatial, and instance domains to reduce dimensional redundancy and enhance information extraction. The MPCT module employs both multi-view and multi-modal self-supervised consistency training. The former enhances the learning of high-level semantics and mitigates the impact of low-level discrepancies, while the latter effectively facilitates the learning of informative multimodal features. We perform extensive experiments on 25 benchmarks across across 9 skeleton-based action understanding tasks, covering coarse prediction, dense prediction, and transferred prediction. Our approach significantly outperforms the current state-of-the-art methods. We hope that this work would broaden the scope of research in skeleton-based action understanding and encourage more attention to dense prediction tasks.

