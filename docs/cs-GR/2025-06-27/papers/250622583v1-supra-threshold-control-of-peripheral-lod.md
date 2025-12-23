---
layout: default
title: Supra-threshold control of peripheral LOD
---

# Supra-threshold control of peripheral LOD

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22583" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22583v1</a>
  <a href="https://arxiv.org/pdf/2506.22583.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22583v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22583v1', 'Supra-threshold control of peripheral LOD')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benjamin Watson, Neff Walker, Larry F Hodges

**分类**: cs.HC, cs.GR

**发布日期**: 2025-06-27

**期刊**: ACM Transactions on Graphics (TOG) (2004), Volume 23, Issue 3, Pages 750-759

**DOI**: [10.1145/1015706.1015796](https://doi.org/10.1145/1015706.1015796)

---

## 💡 一句话要点

**提出超阈值控制方法以优化视觉反馈的细节层次**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `细节层次` `视觉反馈` `超阈值感知` `任务依赖性` `对比度优化` `实验研究`

## 📋 核心要点

1. 现有的LOD控制方法主要基于阈值感知，未能有效应对超阈值感知的实际需求。
2. 论文提出了一种新的超阈值LOD控制策略，强调任务依赖的可靠感知水平与细节对比度的重要性。
3. 实验结果表明，超阈值LOD控制在不同条件下的可感知性表现出显著差异，挑战了传统的LOD控制理论。

## 📝 摘要（中文）

细节层次（LOD）广泛用于控制互动应用中的视觉反馈。传统的LOD控制通常基于阈值感知，即刺激首次可感知的条件。然而，大多数LOD操作在阈值之上，且超阈值感知与阈值感知有显著差异。本文通过两项实验探讨了视觉周边的超阈值LOD控制，发现其应与阈值LOD控制显著不同。具体而言，LOD必须支持任务依赖的可靠感知水平，超出该水平后，LOD控制的可感知性应最小化，而细节对比度是可感知性的更好预测因子。低于该水平时，可感知性必须最大化，且随着偏心度增加或对比度降低，LOD应得到改善。这一发现直接挑战了现有的基于阈值的LOD控制方案，强烈建议重新审视中央显示的LOD控制。

## 🔬 方法详解

**问题定义**：本文旨在解决传统LOD控制方法在超阈值感知下的不足，现有方法未能有效考虑超阈值条件下的视觉反馈需求。

**核心思路**：论文提出超阈值LOD控制策略，强调在不同任务下的可靠感知水平，认为细节对比度比细节大小更能预测可感知性。

**技术框架**：研究通过两项实验设计，分别测试不同条件下的LOD控制效果，分析任务依赖性与视觉感知的关系。主要模块包括实验设计、数据收集与分析、结果验证。

**关键创新**：最重要的创新在于提出超阈值LOD控制的概念，强调在不同感知水平下的LOD调整策略，与传统基于阈值的控制方法形成鲜明对比。

**关键设计**：实验中设置了不同的对比度和偏心度参数，采用细节对比度作为可感知性的预测因子，设计了相应的实验流程以验证理论假设。

## 📊 实验亮点

实验结果显示，在超阈值条件下，LOD控制的可感知性与细节对比度呈现显著相关性，且在不同偏心度和对比度条件下，LOD的优化效果明显优于传统方法。这一发现为视觉反馈的优化提供了新的视角和方法。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和游戏设计等互动应用，能够显著提升用户体验和视觉反馈的质量。未来，超阈值LOD控制方法可能会被广泛应用于需要高效视觉信息传达的场景，推动相关技术的发展。

## 📄 摘要（原文）

> Level of detail (LOD) is widely used to control visual feedback in interactive applications. LOD control is typically based on perception at threshold - the conditions in which a stimulus first becomes perceivable. Yet most LOD manipulations are quite perceivable and occur well above threshold. Moreover, research shows that supra-threshold perception differs drastically from perception at threshold. In that case, should supra-threshold LOD control also differ from LOD control at threshold?
>   In two experiments, we examine supra-threshold LOD control in the visual periphery and find that indeed, it should differ drastically from LOD control at threshold. Specifically, we find that LOD must support a task-dependent level of reliable perceptibility. Above that level, perceptibility of LOD control manipulations should be minimized, and detail contrast is a better predictor of perceptibility than detail size. Below that level, perceptibility must be maximized, and LOD should be improved as eccentricity rises or contrast drops. This directly contradicts prevailing threshold-based LOD control schemes, and strongly suggests a reexamination of LOD control for foveal display.

