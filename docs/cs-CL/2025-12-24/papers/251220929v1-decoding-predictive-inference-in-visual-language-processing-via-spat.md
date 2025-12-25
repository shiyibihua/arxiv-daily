---
layout: default
title: Decoding Predictive Inference in Visual Language Processing via Spatiotemporal Neural Coherence
---

# Decoding Predictive Inference in Visual Language Processing via Spatiotemporal Neural Coherence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20929" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20929v1</a>
  <a href="https://arxiv.org/pdf/2512.20929.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20929v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20929v1', 'Decoding Predictive Inference in Visual Language Processing via Spatiotemporal Neural Coherence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sean C. Borneman, Julia Krebs, Ronnie B. Wilbur, Evie A. Malaia

**分类**: q-bio.NC, cs.CL

**发布日期**: 2025-12-24

**备注**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025) Workshop: Foundation Models for the Brain and Body

---

## 💡 一句话要点

**提出基于时空神经相干性的视觉语言处理预测推理解码框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言处理` `预测推理` `神经相干性` `脑电信号` `光流` `聋人语言` `时空表示`

## 📋 核心要点

1. 现有方法在解码动态视觉语言刺激的神经反应方面存在不足，难以有效捕捉预测推理过程。
2. 利用神经信号与光流运动特征的相干性，构建时空表示，从而解码预测神经动力学。
3. 实验结果表明，左半球和额叶低频相干性是语言理解的关键，且神经特征与年龄相关。

## 📝 摘要（中文）

本文提出了一种机器学习框架，用于解码聋人对动态视觉语言刺激的神经（EEG）反应。通过神经信号与光流导出的运动特征之间的相干性，构建了预测神经动力学的时空表示。利用基于熵的特征选择，识别出特定频率的神经特征，这些特征能够区分可解释的语言输入和语言中断（时间反转）的刺激。结果表明，分布式的左半球和额叶低频相干性是语言理解的关键特征，并且经验依赖的神经特征与年龄相关。这项工作展示了一种新颖的多模态方法，用于探究大脑中经验驱动的生成式感知模型。

## 🔬 方法详解

**问题定义**：论文旨在解决如何解码大脑在处理动态视觉语言（例如手语）时的神经活动，特别是预测推理过程。现有方法可能无法充分捕捉这种动态过程，并且难以区分有意义的语言输入和无意义的输入。

**核心思路**：核心思路是利用神经信号（EEG）与视觉输入（光流导出的运动特征）之间的时空相干性来表征大脑的预测推理过程。通过分析不同频率的神经信号与视觉运动之间的关联，可以识别出与语言理解相关的特定神经特征。

**技术框架**：整体框架包括以下几个主要步骤：1) 收集聋人观看动态视觉语言刺激（手语）时的EEG数据；2) 从视觉刺激中提取光流特征，表征运动信息；3) 计算EEG信号与光流特征之间的相干性，构建时空表示；4) 使用基于熵的特征选择方法，选择区分可解释语言输入和时间反转刺激的关键神经特征；5) 分析这些特征与年龄等因素的关系。

**关键创新**：关键创新在于将神经信号与视觉运动特征的相干性作为解码预测推理过程的桥梁。通过这种多模态融合的方法，可以更有效地捕捉大脑在处理动态语言时的复杂神经活动。此外，基于熵的特征选择方法能够自动识别出与语言理解相关的关键神经特征，避免了人工选择的偏见。

**关键设计**：论文中关键的设计包括：1) 使用光流来表征视觉运动信息，这是一种有效且常用的方法；2) 计算EEG信号与光流特征之间的相干性，捕捉它们之间的时空关联；3) 使用基于熵的特征选择方法，自动选择关键神经特征；4) 分析不同频率的神经信号，因为不同频率的信号可能反映不同的认知过程。具体的参数设置和网络结构等细节在论文中可能没有详细描述，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20929v1/BetterAlgorithmsAllFeatures.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20929v1/BetterAlgorithmsUFSFeaturesNoDirection.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20929v1/corr_post.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，分布式的左半球和额叶低频相干性是语言理解的关键特征。通过区分可解释的语言输入和时间反转的刺激，验证了该方法的有效性。此外，研究还发现经验依赖的神经特征与年龄相关，表明该方法能够捕捉个体差异。

## 🎯 应用场景

该研究成果可应用于开发辅助聋人语言学习和交流的工具，例如实时手语翻译系统。此外，该方法还可以用于研究其他类型的动态视觉语言处理过程，例如阅读和观看电影。未来，该研究有望为理解人类大脑的语言处理机制提供更深入的见解，并促进人机交互技术的发展。

## 📄 摘要（原文）

> Human language processing relies on the brain's capacity for predictive inference. We present a machine learning framework for decoding neural (EEG) responses to dynamic visual language stimuli in Deaf signers. Using coherence between neural signals and optical flow-derived motion features, we construct spatiotemporal representations of predictive neural dynamics. Through entropy-based feature selection, we identify frequency-specific neural signatures that differentiate interpretable linguistic input from linguistically disrupted (time-reversed) stimuli. Our results reveal distributed left-hemispheric and frontal low-frequency coherence as key features in language comprehension, with experience-dependent neural signatures correlating with age. This work demonstrates a novel multimodal approach for probing experience-driven generative models of perception in the brain.

