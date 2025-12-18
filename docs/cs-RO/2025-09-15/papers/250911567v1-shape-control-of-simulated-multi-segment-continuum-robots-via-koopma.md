---
layout: default
title: Shape control of simulated multi-segment continuum robots via Koopman operators with per-segment projection
---

# Shape control of simulated multi-segment continuum robots via Koopman operators with per-segment projection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11567" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11567v1</a>
  <a href="https://arxiv.org/pdf/2509.11567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11567v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11567v1', 'Shape control of simulated multi-segment continuum robots via Koopman operators with per-segment projection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eron Ristich, Jiahe Wang, Lei Zhang, Sultan Haidar Ali, Wanxin Jin, Yi Ren, Jiefeng Sun

**分类**: cs.RO

**发布日期**: 2025-09-15

**备注**: 7 pages (+2 pages of references), 8 figures

---

## 💡 一句话要点

**提出基于分段投影Koopman算子的软体机器人形状控制方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `软体机器人` `形状控制` `Koopman算子` `模型预测控制` `分段投影`

## 📋 核心要点

1. 现有软体机器人主要实现末端控制，难以实现整体形状的实时控制，主要原因是其无限自由度导致计算成本过高。
2. 论文提出基于Koopman算子的数据驱动方法，通过分段投影方案，提高控制仿射Koopman模型的精度。
3. 实验结果表明，该方法能够实现计算高效的闭环控制，验证了软体机器人实时形状控制的可行性。

## 📝 摘要（中文）

本文提出了一种基于数据驱动的Koopman算子方法，用于模拟多段肌腱驱动软体机器人的形状控制，该机器人使用Kirchhoff杆模型。通过从这些模拟软体机器人收集的数据，我们对机器人的状态进行分段投影，从而识别出控制仿射Koopman模型，其精度比没有投影方案的模型高出一个数量级。利用这些学习到的Koopman模型，我们使用线性模型预测控制（MPC）来控制机器人达到一系列不同复杂度的目标形状。我们的方法实现了计算高效的闭环控制，并证明了软体机器人实时形状控制的可行性。我们设想这项工作可以为软体连续机器人的实际形状控制铺平道路。

## 🔬 方法详解

**问题定义**：现有软体机器人控制方法主要集中在末端控制，无法实现对机器人整体形状的精确控制。这是因为软体机器人具有无限自由度，导致动力学建模和控制算法的计算复杂度极高，难以满足实时性要求。因此，如何降低计算成本，实现软体机器人的实时形状控制是一个关键问题。

**核心思路**：论文的核心思路是利用Koopman算子将非线性系统线性化，从而简化控制器的设计。此外，通过对机器人状态进行分段投影，降低状态空间的维度，进一步提高计算效率和模型精度。这种方法旨在利用数据驱动的方式学习系统的动态特性，避免复杂的物理建模。

**技术框架**：该方法主要包含以下几个阶段：1) 使用Kirchhoff杆模型对多段肌腱驱动软体机器人进行仿真；2) 通过仿真数据训练基于Koopman算子的动态模型；3) 在训练过程中，对机器人状态进行分段投影，以提高模型精度；4) 使用线性模型预测控制（MPC）器，基于学习到的Koopman模型，实现对机器人形状的闭环控制。

**关键创新**：该论文的关键创新在于提出了分段投影方案，用于提高Koopman算子模型的精度。传统的Koopman算子方法直接对整个机器人的状态进行建模，忽略了不同段之间的局部特性。通过分段投影，可以更好地捕捉每个段的动态特性，从而提高整体模型的精度。

**关键设计**：论文中，分段投影的具体实现方式未知，但可以推测是对每个segment的状态向量进行降维或者特征提取，然后将这些低维特征拼接起来作为Koopman算子的输入。MPC控制器的设计采用标准的线性MPC方法，目标是最小化机器人当前形状与目标形状之间的差异。具体的损失函数和参数设置未知。

## 📊 实验亮点

实验结果表明，通过分段投影方案，Koopman算子模型的精度提高了一个数量级。此外，该方法能够实现对软体机器人形状的实时闭环控制，验证了其在实际应用中的可行性。具体的性能指标（如控制精度、响应时间等）和对比基线（如其他控制算法）的数据未知。

## 🎯 应用场景

该研究成果可应用于医疗机器人、搜救机器人、工业检测等领域。软体机器人的形状控制能力使其能够在复杂环境中进行操作，例如在人体内进行微创手术，在灾难现场进行搜救，或在狭小空间内进行工业检测。该研究为软体机器人的实际应用提供了理论基础和技术支持。

## 📄 摘要（原文）

> Soft continuum robots can allow for biocompatible yet compliant motions, such as the ability of octopus arms to swim, crawl, and manipulate objects. However, current state-of-the-art continuum robots can only achieve real-time task-space control (i.e., tip control) but not whole-shape control, mainly due to the high computational cost from its infinite degrees of freedom. In this paper, we present a data-driven Koopman operator-based approach for the shape control of simulated multi-segment tendon-driven soft continuum robots with the Kirchhoff rod model. Using data collected from these simulated soft robots, we conduct a per-segment projection scheme on the state of the robots allowing for the identification of control-affine Koopman models that are an order of magnitude more accurate than without the projection scheme. Using these learned Koopman models, we use a linear model predictive control (MPC) to control the robots to a collection of target shapes of varying complexity. Our method realizes computationally efficient closed-loop control, and demonstrates the feasibility of real-time shape control for soft robots. We envision this work can pave the way for practical shape control of soft continuum robots.

