---
layout: default
title: Can We Challenge Open-Vocabulary Object Detectors with Generated Content in Street Scenes?
---

# Can We Challenge Open-Vocabulary Object Detectors with Generated Content in Street Scenes?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23751" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23751v1</a>
  <a href="https://arxiv.org/pdf/2506.23751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23751v1', 'Can We Challenge Open-Vocabulary Object Detectors with Generated Content in Street Scenes?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Annika Mütze, Sadia Ilyas, Christian Dörpelkus, Matthias Rottmann

**分类**: cs.CV

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**利用生成内容挑战开放词汇物体检测器的局限性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇检测` `合成数据` `物体检测` `模型泛化` `安全关键应用`

## 📋 核心要点

1. 现有的开放词汇物体检测器在真实场景中表现出色，但其局限性尚不明确，尤其在安全关键应用中。
2. 本文提出利用合成生成的数据，通过稳定扩散技术填充不寻常物体，以系统性地挑战开放词汇物体检测器。
3. 实验结果表明，开放词汇模型在物体位置上表现出强依赖性，填充技术能够有效挑战这些模型的检测能力。

## 📝 摘要（中文）

开放词汇物体检测器如Grounding DINO在多样化数据上训练，表现出色，但其局限性尚不明确，尤其在安全关键应用中。真实数据无法提供足够的控制来评估模型的泛化能力，而合成数据则能系统性地探索模型的能力边界。本文设计了两个自动化管道，利用稳定扩散技术对不寻常的物体进行填充，并在合成数据上评估多种开放词汇物体检测器，发现这些模型在物体位置上表现出强依赖性，而非物体语义。这为挑战开放词汇模型提供了系统性的方法，并为如何有效改进这些模型提供了宝贵的见解。

## 🔬 方法详解

**问题定义**：本文旨在探讨开放词汇物体检测器在合成生成内容下的表现及其局限性。现有方法在真实数据上评估模型泛化能力时缺乏控制，导致难以发现模型的潜在失败模式。

**核心思路**：通过合成生成的数据，利用稳定扩散技术对不寻常的物体进行填充，系统性地挑战开放词汇物体检测器的能力。此设计旨在揭示模型在特定条件下的表现及其局限性。

**技术框架**：研究设计了两个自动化管道，首先从WordNet和ChatGPT中采样多个名词，生成多样化的合成图像，然后将这些图像与开放词汇物体检测器进行比较评估。

**关键创新**：本研究的创新点在于利用合成生成的数据系统性地挑战开放词汇物体检测器，揭示其对物体位置的强依赖性，而非仅仅依赖物体的语义信息。

**关键设计**：在实验中，采用了稳定扩散技术进行图像填充，确保生成的物体具有高语义多样性。同时，评估了多种开放词汇物体检测器与传统检测器的性能差异，提供了全面的比较分析。

## 📊 实验亮点

实验结果显示，开放词汇物体检测器在合成生成的图像上表现出明显的局限性，特别是在物体位置的依赖性方面。相比传统检测器，开放词汇模型在特定条件下的检测能力显著下降，提供了对模型改进的方向和依据。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、智能监控和机器人视觉等安全关键场景。通过识别和改进开放词汇物体检测器的局限性，可以提高这些系统在复杂环境中的可靠性和安全性，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Open-vocabulary object detectors such as Grounding DINO are trained on vast and diverse data, achieving remarkable performance on challenging datasets. Due to that, it is unclear where to find their limitations, which is of major concern when using in safety-critical applications. Real-world data does not provide sufficient control, required for a rigorous evaluation of model generalization. In contrast, synthetically generated data allows to systematically explore the boundaries of model competence/generalization. In this work, we address two research questions: 1) Can we challenge open-vocabulary object detectors with generated image content? 2) Can we find systematic failure modes of those models? To address these questions, we design two automated pipelines using stable diffusion to inpaint unusual objects with high diversity in semantics, by sampling multiple substantives from WordNet and ChatGPT. On the synthetically generated data, we evaluate and compare multiple open-vocabulary object detectors as well as a classical object detector. The synthetic data is derived from two real-world datasets, namely LostAndFound, a challenging out-of-distribution (OOD) detection benchmark, and the NuImages dataset. Our results indicate that inpainting can challenge open-vocabulary object detectors in terms of overlooking objects. Additionally, we find a strong dependence of open-vocabulary models on object location, rather than on object semantics. This provides a systematic approach to challenge open-vocabulary models and gives valuable insights on how data could be acquired to effectively improve these models.

