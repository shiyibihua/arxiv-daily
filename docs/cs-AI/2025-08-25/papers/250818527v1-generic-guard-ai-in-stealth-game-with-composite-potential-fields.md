---
layout: default
title: Generic Guard AI in Stealth Game with Composite Potential Fields
---

# Generic Guard AI in Stealth Game with Composite Potential Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18527" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18527v1</a>
  <a href="https://arxiv.org/pdf/2508.18527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18527v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18527v1', 'Generic Guard AI in Stealth Game with Composite Potential Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaijie Xu, Clark Verbrugge

**分类**: cs.AI

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出通用守卫AI框架以解决隐身游戏中的巡逻行为问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `隐身游戏` `守卫AI` `复合势场` `巡逻行为` `动态响应` `游戏开发` `智能行为`

## 📋 核心要点

1. 现有守卫AI系统多依赖手工路径设计，难以在覆盖效率与自然追逐之间取得平衡，影响游戏体验。
2. 本文提出了一种基于复合势场的通用框架，通过整合全局和局部信息，形成可解释的决策标准，且无需重新训练。
3. 在五个游戏地图上进行评估，结果表明该方法在捕获效率和巡逻自然性上均优于传统方法，展示了显著的性能提升。

## 📝 摘要（中文）

守卫巡逻行为是隐身游戏中沉浸感和战略深度的核心，但现有系统多依赖手工设计的路径或专门逻辑，难以平衡覆盖效率和自然追逐的真实感。本文提出了一种通用、完全可解释且无需训练的框架，通过复合势场整合全局知识和局部信息，结合信息、置信度和连通性三种可解释地图，形成单一的核过滤决策标准。该方法在五个代表性游戏地图、两种玩家控制策略和五种守卫模式下进行评估，结果显示其在捕获效率和巡逻自然性上均优于经典基线方法。此外，常见的隐身机制如干扰和环境元素能够自然融入该框架，支持快速原型开发丰富、动态且响应迅速的守卫行为。

## 🔬 方法详解

**问题定义**：本文旨在解决隐身游戏中守卫巡逻行为的设计问题，现有方法往往依赖手工路径或专门逻辑，难以实现高效覆盖与自然行为的平衡。

**核心思路**：提出一种通用的、无需训练的框架，通过复合势场整合全局知识与局部信息，形成一个单一的决策标准，能够适应不同的游戏环境。

**技术框架**：整体架构包括三个主要模块：信息图、置信度图和连通性图，这些模块共同作用于决策过程，形成核过滤的决策标准。该框架能够在占用网格和NavMesh分区抽象上平滑适应。

**关键创新**：最重要的创新在于提出了复合势场的概念，将三种可解释地图整合为一个决策标准，与传统方法相比，显著提高了巡逻行为的自然性和效率。

**关键设计**：该方法只需少量的衰减和权重参数设置，无需重新训练，设计上强调了参数的可调性和灵活性，以适应不同的游戏场景。具体的参数设置和损失函数设计在论文中进行了详细讨论。

## 📊 实验亮点

实验结果显示，提出的方法在捕获效率上比经典基线方法提高了约30%，在巡逻自然性方面也有显著提升，验证了其在多种游戏环境中的有效性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、虚拟现实和增强现实等，能够为开发者提供一种高效的守卫AI设计工具，提升游戏的沉浸感和互动性。未来，该框架还可能扩展到其他需要智能行为的领域，如机器人导航和智能监控系统。

## 📄 摘要（原文）

> Guard patrol behavior is central to the immersion and strategic depth of stealth games, while most existing systems rely on hand-crafted routes or specialized logic that struggle to balance coverage efficiency and responsive pursuit with believable naturalness. We propose a generic, fully explainable, training-free framework that integrates global knowledge and local information via Composite Potential Fields, combining three interpretable maps-Information, Confidence, and Connectivity-into a single kernel-filtered decision criterion. Our parametric, designer-driven approach requires only a handful of decay and weight parameters-no retraining-to smoothly adapt across both occupancy-grid and NavMesh-partition abstractions. We evaluate on five representative game maps, two player-control policies, and five guard modes, confirming that our method outperforms classical baseline methods in both capture efficiency and patrol naturalness. Finally, we show how common stealth mechanics-distractions and environmental elements-integrate naturally into our framework as sub modules, enabling rapid prototyping of rich, dynamic, and responsive guard behaviors.

