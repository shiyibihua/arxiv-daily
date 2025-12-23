---
layout: default
title: Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis
---

# Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04142" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04142v1</a>
  <a href="https://arxiv.org/pdf/2506.04142.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04142v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04142v1', 'Establishing Trustworthy LLM Evaluation via Shortcut Neuron Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kejian Zhu, Shangqing Tu, Zhuoran Jin, Lei Hou, Juanzi Li, Jun Zhao

**分类**: cs.CL

**发布日期**: 2025-06-04

**备注**: Accepted to ACL 2025 Main Conference

**🔗 代码/项目**: [GITHUB](https://github.com/GaryStack/Trustworthy-Evaluation)

---

## 💡 一句话要点

**通过快捷神经元分析提出可信赖的LLM评估方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数据污染` `快捷神经元` `模型评估` `可信赖性` `因果分析` `动态基准`

## 📋 核心要点

1. 现有的大型语言模型评估方法依赖公共基准，容易受到数据污染影响，导致评估结果不公正。
2. 本研究通过分析污染模型的机制，提出了一种识别快捷神经元的方法，并引入快捷神经元修补的评估方法。
3. 实验结果显示，该方法有效减轻了污染影响，并与MixEval基准的相关性超过0.95，表明其可信度高。

## 📝 摘要（中文）

大型语言模型（LLMs）的发展依赖于可信赖的评估。然而，目前的评估大多依赖公共基准，容易受到数据污染问题的影响，严重影响公平性。以往研究集中在构建动态基准以应对污染，但持续构建新基准成本高且周期性强。本研究通过分析污染模型的机制来解决这一问题。实验发现，污染模型的过高估计可能源于参数在训练中获得了快捷解决方案。我们提出了一种通过比较和因果分析识别快捷神经元的新方法，并引入了一种称为快捷神经元修补的评估方法以抑制快捷神经元。实验验证了我们的方法在减轻污染方面的有效性，并且评估结果与最近发布的可信基准MixEval展现出强线性相关性，Spearman系数超过0.95，表明我们的方法能够真实反映模型的能力，值得信赖。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型评估中的数据污染问题。现有方法依赖公共基准，容易受到污染影响，导致评估结果失真。

**核心思路**：论文的核心思路是通过分析污染模型的内部机制，识别并抑制训练过程中形成的快捷神经元，以提高评估的可信度。

**技术框架**：整体架构包括两个主要模块：首先，通过比较和因果分析识别快捷神经元；其次，应用快捷神经元修补方法对模型进行评估，抑制这些快捷神经元的影响。

**关键创新**：最重要的技术创新在于提出了快捷神经元的识别方法和修补评估方法，这与以往依赖动态基准的评估方法本质上不同，提供了一种新的思路来解决污染问题。

**关键设计**：在方法实现中，关键设计包括对模型参数的分析、损失函数的调整，以及在不同超参数设置下的实验验证，以确保方法的有效性和通用性。

## 📊 实验亮点

实验结果显示，提出的方法在减轻数据污染方面表现出色，与MixEval基准的Spearman系数超过0.95，表明其评估结果与真实能力高度相关，显著提升了评估的可信度。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过提供更可信赖的评估方法，可以帮助研究人员更准确地评估和优化大型语言模型的性能，推动相关技术的发展与应用。未来，该方法有望在更广泛的AI评估领域中得到应用，提升模型的公平性与可靠性。

## 📄 摘要（原文）

> The development of large language models (LLMs) depends on trustworthy evaluation. However, most current evaluations rely on public benchmarks, which are prone to data contamination issues that significantly compromise fairness. Previous researches have focused on constructing dynamic benchmarks to address contamination. However, continuously building new benchmarks is costly and cyclical. In this work, we aim to tackle contamination by analyzing the mechanisms of contaminated models themselves. Through our experiments, we discover that the overestimation of contaminated models is likely due to parameters acquiring shortcut solutions in training. We further propose a novel method for identifying shortcut neurons through comparative and causal analysis. Building on this, we introduce an evaluation method called shortcut neuron patching to suppress shortcut neurons. Experiments validate the effectiveness of our approach in mitigating contamination. Additionally, our evaluation results exhibit a strong linear correlation with MixEval, a recently released trustworthy benchmark, achieving a Spearman coefficient ($ρ$) exceeding 0.95. This high correlation indicates that our method closely reveals true capabilities of the models and is trustworthy. We conduct further experiments to demonstrate the generalizability of our method across various benchmarks and hyperparameter settings. Code: https://github.com/GaryStack/Trustworthy-Evaluation

