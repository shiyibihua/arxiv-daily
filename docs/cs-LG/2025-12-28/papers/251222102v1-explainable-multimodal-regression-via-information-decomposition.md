---
layout: default
title: Explainable Multimodal Regression via Information Decomposition
---

# Explainable Multimodal Regression via Information Decomposition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.22102" class="toolbar-btn" target="_blank">📄 arXiv: 2512.22102v1</a>
  <a href="https://arxiv.org/pdf/2512.22102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.22102v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.22102v1', 'Explainable Multimodal Regression via Information Decomposition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaozhao Ma, Shujian Yu

**分类**: cs.LG

**发布日期**: 2025-12-26

**备注**: Project Page: https://github.com/zhaozhaoma/PIDReg

**🔗 代码/项目**: [GITHUB](https://github.com/zhaozhaoma/PIDReg)

---

## 💡 一句话要点

**提出基于信息分解的可解释多模态回归框架，提升预测精度与可解释性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态回归` `偏信息分解` `可解释性` `模态融合` `神经影像` `脑年龄预测` `信息论`

## 📋 核心要点

1. 现有方法在多模态回归中缺乏对各模态贡献及其交互的有效解耦和量化工具，导致可解释性不足。
2. 提出基于偏信息分解（PID）的多模态回归框架，将模态表示分解为独特、冗余和协同成分，提升可解释性。
3. 实验结果表明，该框架在预测精度和可解释性方面优于现有方法，并支持高效的模态选择。

## 📝 摘要（中文）

多模态回归旨在从异构输入源预测连续目标，通常依赖于早期或晚期融合等策略。然而，现有方法缺乏解耦和量化每个模态及其交互作用的贡献的有效工具，限制了多模态融合的可解释性。本文提出了一种基于偏信息分解（PID）的新型多模态回归框架，该框架将模态特定的表示分解为独特、冗余和协同成分。基本的PID框架本质上是不确定的。为了解决这个问题，我们通过在潜在表示和变换后的响应变量（经过逆正态变换后）的联合分布中强制执行高斯性来引入归纳偏置，从而实现PID项的解析计算。此外，我们推导出一个闭式条件独立正则化器，以促进每个模态内独特信息的隔离。在六个真实世界数据集上的实验，包括一个关于来自多模态神经影像数据的大规模脑年龄预测的案例研究，表明我们的框架在预测精度和可解释性方面优于最先进的方法，同时也能够进行知情的模态选择以实现高效推理。代码已开源。

## 🔬 方法详解

**问题定义**：多模态回归旨在利用来自不同模态（如图像、文本、音频等）的信息来预测一个连续的目标变量。现有的多模态回归方法，如早期融合和晚期融合，通常缺乏对各个模态贡献的细粒度理解，难以解释模型的预测结果。此外，如何有效地融合不同模态的信息，并避免冗余信息的影响，也是一个挑战。

**核心思路**：本文的核心思路是利用偏信息分解（Partial Information Decomposition, PID）来解耦和量化各个模态对预测结果的贡献。PID可以将每个模态的信息分解为独特信息（仅该模态包含的信息）、冗余信息（多个模态共享的信息）和协同信息（多个模态共同作用才能产生的信息）。通过分析这些信息成分，可以更好地理解各个模态的作用，并提高模型的可解释性。

**技术框架**：该框架主要包含以下几个阶段：1) 特征提取：对每个模态的输入数据进行特征提取，得到模态特定的表示。2) 信息分解：利用PID将每个模态的表示分解为独特、冗余和协同成分。为了解决PID的不确定性问题，论文假设潜在表示和变换后的响应变量服从高斯分布，从而实现PID项的解析计算。3) 回归预测：利用分解后的信息成分进行回归预测。4) 正则化：引入条件独立正则化器，以促进每个模态内独特信息的隔离。

**关键创新**：该论文的关键创新在于将偏信息分解（PID）应用于多模态回归问题，并提出了一种基于高斯假设的PID解析计算方法。此外，论文还设计了一个条件独立正则化器，以进一步提高模型的可解释性。与现有方法相比，该方法能够更细粒度地分析各个模态的贡献，并提高预测精度和可解释性。

**关键设计**：为了解决PID的不确定性问题，论文假设潜在表示和变换后的响应变量的联合分布服从高斯分布。这个假设使得PID的各项可以解析计算，避免了复杂的优化过程。此外，论文还设计了一个条件独立正则化器，其形式为闭式解，可以有效地促进每个模态内独特信息的隔离。损失函数包括回归损失、PID损失和条件独立正则化损失，通过调整各项的权重来平衡预测精度和可解释性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22102v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22102v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.22102v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在六个真实世界数据集上的实验结果表明，该框架在预测精度和可解释性方面均优于现有方法。例如，在脑年龄预测任务中，该方法能够有效地利用多模态神经影像数据，并准确预测脑年龄。此外，该方法还能够进行知情的模态选择，从而在保证预测精度的前提下，降低计算成本。

## 🎯 应用场景

该研究成果可应用于多个领域，例如医学影像分析（如脑年龄预测）、情感分析、多媒体内容理解等。通过理解不同模态的贡献，可以更好地诊断疾病、理解用户情感、提升多媒体内容检索的准确性。该方法还可用于模态选择，从而降低计算成本，提高推理效率。未来，该方法可以扩展到更多模态和更复杂的任务中。

## 📄 摘要（原文）

> Multimodal regression aims to predict a continuous target from heterogeneous input sources and typically relies on fusion strategies such as early or late fusion. However, existing methods lack principled tools to disentangle and quantify the individual contributions of each modality and their interactions, limiting the interpretability of multimodal fusion. We propose a novel multimodal regression framework grounded in Partial Information Decomposition (PID), which decomposes modality-specific representations into unique, redundant, and synergistic components. The basic PID framework is inherently underdetermined. To resolve this, we introduce inductive bias by enforcing Gaussianity in the joint distribution of latent representations and the transformed response variable (after inverse normal transformation), thereby enabling analytical computation of the PID terms. Additionally, we derive a closed-form conditional independence regularizer to promote the isolation of unique information within each modality. Experiments on six real-world datasets, including a case study on large-scale brain age prediction from multimodal neuroimaging data, demonstrate that our framework outperforms state-of-the-art methods in both predictive accuracy and interpretability, while also enabling informed modality selection for efficient inference. Implementation is available at https://github.com/zhaozhaoma/PIDReg.

