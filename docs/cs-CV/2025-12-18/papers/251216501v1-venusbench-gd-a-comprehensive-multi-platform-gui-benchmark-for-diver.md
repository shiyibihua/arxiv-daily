---
layout: default
title: VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks
---

# VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16501" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16501v1</a>
  <a href="https://arxiv.org/pdf/2512.16501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16501v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16501v1', 'VenusBench-GD: A Comprehensive Multi-Platform GUI Benchmark for Diverse Grounding Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Beitong Zhou, Zhexiao Huang, Yuan Guo, Zhangxuan Gu, Tianyu Xia, Zichen Luo, Fei Tang, Dehan Kong, Yanyi Shang, Suling Ou, Zhenlin Guo, Changhua Meng, Shuheng Shen

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**VenusBench-GD：一个全面的多平台GUI基准，用于评估多样化的Grounding任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI grounding` `多平台基准` `用户界面` `多模态学习` `分层任务` `基准数据集` `人机交互` `计算机视觉`

## 📋 核心要点

1. 现有GUI grounding基准数据量不足、领域覆盖窄，或过度关注单一平台，限制了GUI代理的发展。
2. VenusBench-GD构建了一个大规模、跨平台、双语的GUI grounding基准，包含丰富的标注数据和分层任务分类。
3. 实验表明，通用多模态模型在基本任务上可与专用GUI模型媲美，但高级任务仍需专用模型，且存在过拟合问题。

## 📝 摘要（中文）

GUI grounding是构建强大GUI代理的关键组成部分。然而，现有的grounding基准存在显著的局限性：它们要么提供的数据量不足且领域覆盖范围狭窄，要么过度关注单一平台并需要高度专业化的领域知识。本文提出了VenusBench-GD，这是一个全面的、双语的GUI grounding基准，跨越多个平台，能够对真实世界的应用程序进行分层评估。VenusBench-GD的贡献如下：（i）我们引入了一个大规模的、跨平台的基准，具有广泛的应用程序覆盖、多样的UI元素和丰富的标注数据；（ii）我们建立了一个高质量的数据构建流程，用于grounding任务，实现了比现有基准更高的标注准确率；（iii）我们通过提出一个分层任务分类法来扩展元素grounding的范围，该分类法将grounding分为基本和高级类别，包含六个不同的子任务，旨在从互补的角度评估模型。我们的实验结果揭示了关键的见解：通用多模态模型现在在基本grounding任务上匹配甚至超过了专门的GUI模型。相比之下，高级任务仍然偏爱GUI专用模型，尽管它们表现出显著的过拟合和较差的鲁棒性。这些结果强调了全面、多层评估框架的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有GUI grounding基准数据集不足、领域覆盖范围有限以及平台单一的问题。现有方法难以全面评估GUI代理的grounding能力，且标注质量不高，阻碍了相关研究的进展。

**核心思路**：论文的核心思路是构建一个大规模、跨平台、高质量的GUI grounding基准数据集VenusBench-GD，并设计分层任务分类，以全面评估模型的grounding能力。通过提供更丰富的数据和更细粒度的评估，促进GUI grounding技术的发展。

**技术框架**：VenusBench-GD的构建流程包括数据收集、数据清洗、数据标注和任务划分等步骤。首先，从多个平台收集GUI数据，然后进行清洗和过滤，去除噪声数据。接着，对UI元素进行标注，包括位置、类型、文本等信息。最后，将grounding任务划分为基本和高级类别，并设计六个不同的子任务。

**关键创新**：VenusBench-GD的关键创新在于其大规模、跨平台和分层任务分类。与现有基准相比，VenusBench-GD覆盖了更广泛的应用程序和UI元素，提供了更丰富的标注数据，并能够从多个角度评估模型的grounding能力。此外，该基准还采用了高质量的数据构建流程，保证了标注的准确性。

**关键设计**：VenusBench-GD的关键设计包括UI元素的标注规范、任务的划分标准以及评估指标的选择。UI元素的标注规范定义了不同类型UI元素的标注方式，确保标注的一致性。任务的划分标准基于grounding的复杂程度，将任务分为基本和高级类别。评估指标包括准确率、召回率和F1值等，用于评估模型在不同任务上的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16501v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16501v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16501v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，通用多模态模型在基本grounding任务上可以达到甚至超过专门的GUI模型性能。然而，在高级任务上，GUI专用模型仍然更胜一筹，但存在严重的过拟合问题，鲁棒性较差。这些结果突出了VenusBench-GD在评估模型泛化能力方面的重要性。

## 🎯 应用场景

VenusBench-GD可应用于开发更智能的GUI代理，例如自动化测试工具、辅助技术和人机交互系统。通过利用该基准，研究人员可以训练和评估更强大的GUI grounding模型，从而提高GUI代理的可用性和效率。此外，该基准还可以促进跨平台GUI应用程序的开发和维护。

## 📄 摘要（原文）

> GUI grounding is a critical component in building capable GUI agents. However, existing grounding benchmarks suffer from significant limitations: they either provide insufficient data volume and narrow domain coverage, or focus excessively on a single platform and require highly specialized domain knowledge. In this work, we present VenusBench-GD, a comprehensive, bilingual benchmark for GUI grounding that spans multiple platforms, enabling hierarchical evaluation for real-word applications. VenusBench-GD contributes as follows: (i) we introduce a large-scale, cross-platform benchmark with extensive coverage of applications, diverse UI elements, and rich annotated data, (ii) we establish a high-quality data construction pipeline for grounding tasks, achieving higher annotation accuracy than existing benchmarks, and (iii) we extend the scope of element grounding by proposing a hierarchical task taxonomy that divides grounding into basic and advanced categories, encompassing six distinct subtasks designed to evaluate models from complementary perspectives. Our experimental findings reveal critical insights: general-purpose multimodal models now match or even surpass specialized GUI models on basic grounding tasks. In contrast, advanced tasks, still favor GUI-specialized models, though they exhibit significant overfitting and poor robustness. These results underscore the necessity of comprehensive, multi-tiered evaluation frameworks.

