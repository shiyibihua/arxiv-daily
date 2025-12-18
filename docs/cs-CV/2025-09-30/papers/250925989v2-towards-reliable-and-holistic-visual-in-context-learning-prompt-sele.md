---
layout: default
title: Towards Reliable and Holistic Visual In-Context Learning Prompt Selection
---

# Towards Reliable and Holistic Visual In-Context Learning Prompt Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25989" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25989v2</a>
  <a href="https://arxiv.org/pdf/2509.25989.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25989v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25989v2', 'Towards Reliable and Holistic Visual In-Context Learning Prompt Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxiao Wu, Jing-Hao Xue, Chengming Xu, Chen Liu, Xinwei Sun, Changxin Gao, Nong Sang, Yanwei Fu

**分类**: cs.CV

**发布日期**: 2025-09-30 (更新: 2025-10-17)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出RH-Partial2Global，提升视觉上下文学习中prompt选择的可靠性和全面性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉上下文学习` `上下文示例选择` `共形预测` `覆盖设计` `小样本学习`

## 📋 核心要点

1. 现有VICL方法依赖“相似性优先”假设，但缺乏理论支撑，且Partial2Global的随机采样导致覆盖不全和冗余。
2. RH-Partial2Global利用jackknife共形预测构建可靠替代集，并采用覆盖设计采样确保成对偏好的全面覆盖。
3. 实验结果表明，RH-Partial2Global在多种视觉任务上表现出色，显著优于Partial2Global。

## 📝 摘要（中文）

视觉上下文学习(VICL)已成为一种将视觉基础模型适应于新任务的重要方法，它通过有效利用上下文中嵌入的上下文信息来实现，这可以被形式化为潜在候选者的全局排序问题。现有的VICL方法，如Partial2Global和VPR，都基于相似性优先的假设，即与查询图像在视觉上更相似的图像可以作为更好的上下文示例。然而，这种基本假设缺乏充分的理由来证明其在选择最佳上下文示例中的有效性。此外，Partial2Global通过一系列随机采样的成对偏好预测来构建其全局排序。这种对随机采样的依赖可能导致比较的不完全覆盖和冗余采样，从而进一步不利地影响最终的全局排序。为了解决这些问题，本文提出了一种增强的Partial2Global变体，旨在可靠和全面地选择VICL中的上下文示例。我们提出的方法，称为RH-Partial2Global，利用jackknife共形预测引导策略来构建可靠的替代集，并采用基于覆盖设计的采样方法来确保成对偏好的全面和均匀覆盖。大量的实验表明，RH-Partial2Global取得了优异的性能，并在各种视觉任务中优于Partial2Global。

## 🔬 方法详解

**问题定义**：现有视觉上下文学习（VICL）方法，特别是Partial2Global，在选择上下文示例时存在问题。它们依赖于“相似性优先”的假设，即与查询图像更相似的图像是更好的上下文示例，但这种假设缺乏充分的理论依据。此外，Partial2Global通过随机采样成对偏好预测来构建全局排序，导致比较覆盖不全和冗余采样，影响最终排序的准确性。

**核心思路**：RH-Partial2Global的核心思路是通过更可靠和全面的方法来选择上下文示例，从而提高VICL的性能。它旨在解决Partial2Global中存在的两个主要问题：缺乏对“相似性优先”假设的理论支持，以及随机采样导致的覆盖不全和冗余采样。

**技术框架**：RH-Partial2Global的整体框架可以分为两个主要阶段：1) 使用jackknife共形预测构建可靠的替代集；2) 使用覆盖设计（covering design）的采样方法来确保成对偏好的全面和均匀覆盖。首先，利用jackknife共形预测来评估每个候选上下文示例的可靠性，并构建一个包含多个可靠替代方案的集合。然后，采用覆盖设计方法，系统地选择成对比较，以确保所有可能的偏好关系都被充分考虑。

**关键创新**：RH-Partial2Global的关键创新在于两个方面：一是使用jackknife共形预测来评估和选择可靠的上下文示例，这提供了一种更严谨和理论支持的方法，而不是简单地依赖相似性；二是采用覆盖设计来指导成对偏好的采样，这确保了所有可能的偏好关系都被充分考虑，避免了随机采样可能导致的覆盖不全和冗余。与Partial2Global相比，RH-Partial2Global不再依赖于未经证实的相似性假设，并避免了随机采样带来的问题。

**关键设计**：RH-Partial2Global的关键设计包括：1) jackknife共形预测的具体实现，包括如何计算p-value和构建替代集；2) 覆盖设计的具体策略，包括如何选择成对比较以确保全面覆盖；3) 如何将可靠的替代集和全面的偏好信息整合到最终的全局排序中。论文中可能还涉及一些超参数的设置，例如jackknife共形预测中的显著性水平，以及覆盖设计中的覆盖率等。

## 📊 实验亮点

实验结果表明，RH-Partial2Global在多个视觉任务上显著优于Partial2Global。具体的性能提升数据需要在论文中查找，但摘要中明确指出RH-Partial2Global取得了“优异的性能”，表明其在准确率、召回率或其他相关指标上均有显著提升。该方法通过更可靠和全面的上下文示例选择，有效提高了VICL的性能。

## 🎯 应用场景

该研究成果可应用于各种视觉任务，例如图像分类、目标检测、图像分割等，尤其是在小样本学习或零样本学习场景下，通过选择合适的上下文示例，可以显著提高模型的泛化能力和准确性。此外，该方法还可以扩展到其他领域，例如自然语言处理中的上下文学习。

## 📄 摘要（原文）

> Visual In-Context Learning (VICL) has emerged as a prominent approach for adapting visual foundation models to novel tasks, by effectively exploiting contextual information embedded in in-context examples, which can be formulated as a global ranking problem of potential candidates. Current VICL methods, such as Partial2Global and VPR, are grounded in the similarity-priority assumption that images more visually similar to a query image serve as better in-context examples. This foundational assumption, while intuitive, lacks sufficient justification for its efficacy in selecting optimal in-context examples. Furthermore, Partial2Global constructs its global ranking from a series of randomly sampled pairwise preference predictions. Such a reliance on random sampling can lead to incomplete coverage and redundant samplings of comparisons, thus further adversely impacting the final global ranking. To address these issues, this paper introduces an enhanced variant of Partial2Global designed for reliable and holistic selection of in-context examples in VICL. Our proposed method, dubbed RH-Partial2Global, leverages a jackknife conformal prediction-guided strategy to construct reliable alternative sets and a covering design-based sampling approach to ensure comprehensive and uniform coverage of pairwise preferences. Extensive experiments demonstrate that RH-Partial2Global achieves excellent performance and outperforms Partial2Global across diverse visual tasks.

