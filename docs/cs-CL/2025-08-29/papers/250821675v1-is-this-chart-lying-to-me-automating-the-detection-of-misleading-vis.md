---
layout: default
title: Is this chart lying to me? Automating the detection of misleading visualizations
---

# Is this chart lying to me? Automating the detection of misleading visualizations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21675" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21675v1</a>
  <a href="https://arxiv.org/pdf/2508.21675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21675v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21675v1', 'Is this chart lying to me? Automating the detection of misleading visualizations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonathan Tonglet, Jan Zimny, Tinne Tuytelaars, Iryna Gurevych

**分类**: cs.CL, cs.CV, cs.GR

**发布日期**: 2025-08-29

**备注**: Preprint under review. Code and data available at: https://github.com/UKPLab/arxiv2025-misviz

---

## 💡 一句话要点

**提出Misviz基准以自动检测误导性可视化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `误导性可视化` `数据集构建` `多模态学习` `信息传播` `虚假信息检测`

## 📋 核心要点

1. 现有方法在自动检测误导性可视化方面面临数据集缺乏和评估标准不统一的挑战。
2. 本文提出了Misviz和Misviz-synth数据集，旨在为模型训练提供丰富的标注和合成可视化数据。
3. 实验结果显示，尽管采用了先进的MLLMs和分类器，检测任务仍然具有较高的复杂性和挑战性。

## 📝 摘要（中文）

误导性可视化是社交媒体和网络上虚假信息的重要驱动因素。通过违反图表设计原则，它们扭曲数据，导致读者得出不准确的结论。以往研究表明，无论是人类还是多模态大型语言模型（MLLMs）都容易受到这些可视化的误导。自动检测误导性可视化并识别其违反的具体设计规则，有助于保护读者并减少虚假信息的传播。然而，AI模型的训练和评估受到缺乏大型、多样化和公开可用数据集的限制。本文介绍了Misviz，一个包含2604个真实可视化的基准数据集，并标注了12种误导类型。同时，我们还发布了Misviz-synth，一个基于真实数据表生成的合成数据集，包含81814个可视化。我们在这两个数据集上使用最先进的MLLMs、基于规则的系统和微调分类器进行了全面评估，结果表明该任务仍然具有很高的挑战性。我们发布了Misviz、Misviz-synth及相关代码。

## 🔬 方法详解

**问题定义**：本文旨在解决自动检测误导性可视化的问题，现有方法面临数据集不足和评估标准不统一的痛点。

**核心思路**：论文通过引入Misviz和Misviz-synth数据集，提供了丰富的标注和合成数据，以支持模型的训练和评估。

**技术框架**：整体架构包括数据集的构建、模型训练和评估三个主要阶段。Misviz提供真实数据的标注，而Misviz-synth则生成合成数据以扩展训练集。

**关键创新**：最重要的技术创新在于构建了一个包含2604个真实可视化和81814个合成可视化的综合数据集，填补了现有研究的空白。

**关键设计**：在模型训练中，采用了先进的MLLMs和微调分类器，结合规则基础系统进行综合评估，确保了检测的准确性和有效性。

## 📊 实验亮点

实验结果表明，尽管采用了最先进的多模态大型语言模型和微调分类器，检测误导性可视化的任务仍然具有较高的挑战性。具体性能数据尚未披露，但研究显示该领域仍需进一步探索和优化。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、新闻报道的真实性验证以及教育领域的可视化教学。通过自动检测误导性可视化，能够有效减少虚假信息的传播，提升公众的信息素养和判断能力。未来，该技术可能扩展到更广泛的数据可视化和信息传播领域。

## 📄 摘要（原文）

> Misleading visualizations are a potent driver of misinformation on social media and the web. By violating chart design principles, they distort data and lead readers to draw inaccurate conclusions. Prior work has shown that both humans and multimodal large language models (MLLMs) are frequently deceived by such visualizations. Automatically detecting misleading visualizations and identifying the specific design rules they violate could help protect readers and reduce the spread of misinformation. However, the training and evaluation of AI models has been limited by the absence of large, diverse, and openly available datasets. In this work, we introduce Misviz, a benchmark of 2,604 real-world visualizations annotated with 12 types of misleaders. To support model training, we also release Misviz-synth, a synthetic dataset of 81,814 visualizations generated using Matplotlib and based on real-world data tables. We perform a comprehensive evaluation on both datasets using state-of-the-art MLLMs, rule-based systems, and fine-tuned classifiers. Our results reveal that the task remains highly challenging. We release Misviz, Misviz-synth, and the accompanying code.

