---
layout: default
title: Efficient Manipulation-Enhanced Semantic Mapping With Uncertainty-Informed Action Selection
---

# Efficient Manipulation-Enhanced Semantic Mapping With Uncertainty-Informed Action Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02286" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02286v2</a>
  <a href="https://arxiv.org/pdf/2506.02286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02286v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02286v2', 'Efficient Manipulation-Enhanced Semantic Mapping With Uncertainty-Informed Action Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nils Dengler, Jesper Mücke, Rohit Menon, Maren Bennewitz

**分类**: cs.RO

**发布日期**: 2025-06-02 (更新: 2025-09-02)

---

## 💡 一句话要点

**提出基于操作增强的语义映射框架以解决不确定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `语义映射` `服务机器人` `不确定性` `强化学习` `动态环境` `信息增益` `操作选择`

## 📋 核心要点

1. 现有方法在处理杂乱环境中的物体重排时，难以高效且准确地进行语义和空间映射，导致不确定性增加。
2. 本文提出了一种新的框架，通过结合证据度量语义映射与强化学习，优化视角选择和目标动作，以降低不确定性。
3. 实验结果显示，该框架在准确映射杂乱场景的同时，显著减少了物体位移，并将规划时间缩短至95%。

## 📝 摘要（中文）

服务机器人在家庭、办公室和学校等杂乱的人类环境中，无法依赖预定义的物体排列，必须在频繁的物体重排中持续更新其语义和空间估计。为此，本文提出了一种操作增强的语义映射框架，结合了证据度量语义映射、基于强化学习的下一个最佳视角规划和目标动作选择。该方法利用Dirichlet和Beta分布的估计不确定性，指导主动传感器放置和物体操作，重点关注高不确定性区域，并选择具有高预期信息增益的动作。实验结果表明，该框架能够准确映射杂乱场景，同时显著减少物体位移，并将规划时间减少95%，实现了实际应用的可能性。

## 🔬 方法详解

**问题定义**：本文旨在解决服务机器人在杂乱环境中进行语义映射时面临的高不确定性和物体重排问题。现有方法往往无法有效应对频繁的环境变化，导致映射精度下降。

**核心思路**：提出的框架通过结合证据度量语义映射与强化学习，主动选择信息量大的视角和动作，以减少环境中的不确定性。该设计旨在提高机器人在复杂环境中的适应能力和映射精度。

**技术框架**：整体架构包括三个主要模块：证据度量语义映射模块、基于强化学习的下一个最佳视角规划模块和目标动作选择模块。首先，通过语义映射模块生成环境的初步估计，然后利用强化学习算法选择最佳视角，最后执行针对性操作以减少不确定性。

**关键创新**：本研究的创新点在于引入不确定性信息驱动的推理策略，特别是针对遮挡物体的操作选择。这一策略与传统方法相比，能够更有效地揭示隐藏区域，降低整体不确定性。

**关键设计**：在网络结构上，采用了Dirichlet和Beta分布来估计不确定性，并设计了相应的损失函数以优化信息增益。此外，推理策略的参数设置经过精心调整，以确保在动态环境中保持高效性和准确性。

## 📊 实验亮点

实验结果表明，提出的框架在准确映射杂乱场景方面表现优异，物体位移显著减少，同时规划时间较现有最先进方法缩短了95%。这一成果展示了该方法在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人在家庭、办公室和学校等复杂环境中的导航和操作。通过提高机器人在动态环境中的映射能力，可以显著提升其在实际应用中的效率和可靠性，推动智能家居和自动化办公的发展。

## 📄 摘要（原文）

> Service robots operating in cluttered human environments such as homes, offices, and schools cannot rely on predefined object arrangements and must continuously update their semantic and spatial estimates while dealing with possible frequent rearrangements. Efficient and accurate mapping under such conditions demands selecting informative viewpoints and targeted manipulations to reduce occlusions and uncertainty. In this work, we present a manipulation-enhanced semantic mapping framework for occlusion-heavy shelf scenes that integrates evidential metric-semantic mapping with reinforcement-learning-based next-best view planning and targeted action selection. Our method thereby exploits uncertainty estimates from Dirichlet and Beta distributions in the map prediction networks to guide both active sensor placement and object manipulation, focusing on areas with high uncertainty and selecting actions with high expected information gain. Furthermore, we introduce an uncertainty-informed push strategy that targets occlusion-critical objects and generates minimally invasive actions to reveal hidden regions by reducing overall uncertainty in the scene. The experimental evaluation shows that our framework enables to accurately map cluttered scenes, while substantially reducing object displacement and achieving a 95% reduction in planning time compared to the state-of-the-art, thereby realizing real-world applicability.

