---
layout: default
title: Harnessing Input-Adaptive Inference for Efficient VLN
---

# Harnessing Input-Adaptive Inference for Efficient VLN

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09262" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09262v1</a>
  <a href="https://arxiv.org/pdf/2508.09262.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09262v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09262v1', 'Harnessing Input-Adaptive Inference for Efficient VLN')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongwoo Kang, Akhil Perincherry, Zachary Coalson, Aiden Gabriel, Stefan Lee, Sanghyun Hong

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-12

**备注**: Accepted to ICCV 2025 [Poster]

**🔗 代码/项目**: [GITHUB](https://github.com/secure-ai-systems-group/adaptive-vision-and-language-navigation)

---

## 💡 一句话要点

**提出输入自适应推理方法以提升视觉语言导航效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `输入自适应` `多模态变换器` `计算效率` `智能代理`

## 📋 核心要点

1. 现有的输入自适应机制在减少计算时，往往会导致性能显著下降，限制了其实际应用。
2. 本文提出三种自适应算法，分别针对空间、模型内部和时间效率进行优化，以提升VLN模型的计算效率。
3. 在七个VLN基准测试中，展示了在标准和连续环境下，计算量减少超过2倍的显著效果。

## 📝 摘要（中文）

在视觉语言导航（VLN）领域，历史感知的多模态变换器模型正逐渐成为新兴范式。这些模型在接收语言指令后，处理观察和导航历史，以预测代理的最优行动。尽管这些模型显著提升了性能，但其规模在计算资源有限的实际应用中成为瓶颈。本文提出了一种新颖的输入自适应导航方法，以提高VLN模型的效率。我们首先表明现有的输入自适应机制在不显著降低性能的情况下无法减少计算。为此，我们引入了三种自适应算法，分别在不同层面上部署：选择性处理全景视图、基于重要性的自适应阈值方法以及缓存机制。通过在七个VLN基准上的评估，我们展示了在标准和连续环境中，三种现成代理的计算量减少超过2倍。我们的代码已公开可用。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言导航（VLN）模型在计算资源有限情况下的效率问题。现有方法在减少计算时常常伴随性能显著下降，影响实际应用。

**核心思路**：论文提出的核心思路是通过输入自适应机制来优化计算效率，具体包括选择性处理视图、重要性阈值和缓存机制，以减少不必要的计算。

**技术框架**：整体架构包括三个主要模块：1) 选择性处理全景视图以提高空间效率；2) 采用基于重要性的自适应阈值方法以提升模型内部效率；3) 实施缓存机制以提高时间效率，避免重复处理已见视图。

**关键创新**：最重要的技术创新在于引入了三种自适应算法，分别针对不同层面进行优化，显著提升了VLN模型的计算效率，且在性能上保持了较高水平。

**关键设计**：在设计中，选择性处理全景视图的策略基于代理的当前状态，重要性阈值方法则通过动态调整阈值来决定是否提前退出计算，缓存机制则确保了对已处理视图的有效利用。具体的参数设置和损失函数设计在实验中进行了详细验证。

## 📊 实验亮点

在七个VLN基准测试中，本文的方法在标准和连续环境下实现了超过2倍的计算量减少，显著提升了三种现成代理的效率。这一结果表明，提出的输入自适应推理方法在实际应用中具有较强的优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人导航、自动驾驶系统以及人机交互等场景。通过提升视觉语言导航的效率，能够在资源受限的环境中实现更高效的决策和行动，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> An emerging paradigm in vision-and-language navigation (VLN) is the use of history-aware multi-modal transformer models. Given a language instruction, these models process observation and navigation history to predict the most appropriate action for an agent. While they have significantly improved performance, the scale of these models can be a bottleneck in practical settings with limited computational resources. In this work, we propose a novel input-adaptive navigation method to enhance VLN model efficiency. We first show that existing input-adaptive mechanisms fail to reduce computations without substantial performance degradation. To address this, we introduce three adaptive algorithms, each deployed at a different level: (1) To improve spatial efficiency, we selectively process panoramic views at each observation of an agent. (2) To improve intra-model efficiency, we propose importance-based adaptive thresholding for the early-exit methods. (3) To improve temporal efficiency, we implement a caching mechanism that prevents reprocessing of views previously seen by the agent. In evaluations on seven VLN benchmarks, we demonstrate over a 2$\times$ reduction in computation across three off-the-shelf agents in both standard and continuous environments. Our code is publicly available at https://github.com/secure-ai-systems-group/adaptive-vision-and-language-navigation.

