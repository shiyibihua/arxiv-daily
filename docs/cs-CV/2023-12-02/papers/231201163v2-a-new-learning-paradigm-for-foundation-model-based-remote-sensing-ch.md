---
layout: default
title: A New Learning Paradigm for Foundation Model-based Remote Sensing Change Detection
---

# A New Learning Paradigm for Foundation Model-based Remote Sensing Change Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01163" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01163v2</a>
  <a href="https://arxiv.org/pdf/2312.01163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01163v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01163v2', 'A New Learning Paradigm for Foundation Model-based Remote Sensing Change Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiyu Li, Xiangyong Cao, Deyu Meng

**分类**: cs.CV

**发布日期**: 2023-12-02 (更新: 2024-02-11)

**🔗 代码/项目**: [GITHUB](https://github.com/likyoo/BAN)

---

## 💡 一句话要点

**提出基于Foundation Model的双时相遥感影像变化检测框架BAN，提升现有方法性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感影像` `变化检测` `Foundation Model` `适配器网络` `深度学习`

## 📋 核心要点

1. 现有基于深度学习的变化检测模型受限于标注数据，难以充分提取知识。
2. 提出双时相适配器网络BAN，利用冻结的Foundation Model提取通用特征，并适配到变化检测任务。
3. 实验表明，BAN能有效提升现有变化检测方法的性能，IoU最多提升4.08%。

## 📝 摘要（中文）

变化检测（CD）是观察和分析地表覆盖动态过程的关键任务。尽管许多基于深度学习的CD模型表现出色，但其性能提升受到从有限标注数据中提取知识的限制。另一方面，最近出现的Foundation Model通过跨数据模态和代理任务的扩展，包含了大量知识。本文提出了一种双时相适配器网络（BAN），这是一个通用的基于Foundation Model的CD适配框架，旨在提取Foundation Model的知识用于CD。所提出的BAN包含三个部分，即冻结的Foundation Model（例如，CLIP）、双时相适配器分支（Bi-TAB）以及它们之间的桥接模块。具体而言，BAN通过冻结的Foundation Model提取通用特征，然后通过桥接模块将这些特征选择、对齐并注入到Bi-TAB中。Bi-TAB被设计为一种模型无关的概念，用于提取特定任务/领域的特征，它可以是现有的任意CD模型或一些手工堆叠的块。BAN是首次将Foundation Model适配到CD任务的广泛尝试，超越了当前定制的模型。实验结果表明，BAN能够有效提高现有CD方法的性能（例如，IoU最多提高4.08%），且仅需少量额外的可学习参数。更重要的是，这些成功的实践向我们展示了Foundation Model在遥感CD中的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决遥感影像变化检测任务中，现有深度学习模型因训练数据有限而导致的知识提取不足的问题。现有方法通常依赖于特定数据集的标注，泛化能力较弱，且难以利用大规模无标注数据中蕴含的丰富知识。

**核心思路**：论文的核心思路是利用预训练的Foundation Model（如CLIP）所具备的通用知识，通过适配器网络将其迁移到变化检测任务中。通过冻结Foundation Model的主体，仅训练少量的适配器参数，从而避免了从头训练的巨大开销，并有效利用了Foundation Model的先验知识。

**技术框架**：BAN框架主要包含三个模块：1) 冻结的Foundation Model：用于提取输入图像的通用特征；2) 双时相适配器分支（Bi-TAB）：用于提取特定任务/领域的特征，可以是现有的变化检测模型或自定义模块；3) 桥接模块：用于将Foundation Model提取的特征选择、对齐并注入到Bi-TAB中。整体流程是，首先通过Foundation Model提取双时相图像的特征，然后通过桥接模块将特征传递给Bi-TAB，最后由Bi-TAB进行变化检测。

**关键创新**：论文的关键创新在于提出了一个通用的基于Foundation Model的变化检测适配框架BAN，能够将预训练的Foundation Model的知识迁移到变化检测任务中，并有效提升现有方法的性能。与以往针对特定数据集定制的模型不同，BAN具有更强的通用性和可扩展性。

**关键设计**：Bi-TAB的设计具有模型无关性，可以灵活选择现有的变化检测模型或自定义模块。桥接模块的设计至关重要，需要考虑如何有效地将Foundation Model提取的通用特征与Bi-TAB提取的特定任务特征进行融合。具体的参数设置、损失函数和网络结构等细节取决于所选择的Bi-TAB和桥接模块的具体实现。

## 📊 实验亮点

实验结果表明，所提出的BAN框架能够有效提升现有变化检测方法的性能，例如，IoU指标最多提升4.08%。该方法仅需少量额外的可学习参数，即可实现显著的性能提升，表明了Foundation Model在遥感影像变化检测中的巨大潜力。代码已开源，方便研究人员进行复现和进一步研究。

## 🎯 应用场景

该研究成果可广泛应用于遥感影像变化检测领域，例如城市扩张监测、自然灾害评估、土地利用变化分析等。通过利用Foundation Model的强大知识，可以提高变化检测的精度和效率，为相关领域的决策提供更可靠的依据。未来，该方法有望推广到其他遥感影像分析任务中。

## 📄 摘要（原文）

> Change detection (CD) is a critical task to observe and analyze dynamic processes of land cover. Although numerous deep learning-based CD models have performed excellently, their further performance improvements are constrained by the limited knowledge extracted from the given labelled data. On the other hand, the foundation models that emerged recently contain a huge amount of knowledge by scaling up across data modalities and proxy tasks. In this paper, we propose a Bi-Temporal Adapter Network (BAN), which is a universal foundation model-based CD adaptation framework aiming to extract the knowledge of foundation models for CD. The proposed BAN contains three parts, i.e. frozen foundation model (e.g., CLIP), bi-temporal adapter branch (Bi-TAB), and bridging modules between them. Specifically, BAN extracts general features through a frozen foundation model, which are then selected, aligned, and injected into Bi-TAB via the bridging modules. Bi-TAB is designed as a model-agnostic concept to extract task/domain-specific features, which can be either an existing arbitrary CD model or some hand-crafted stacked blocks. Beyond current customized models, BAN is the first extensive attempt to adapt the foundation model to the CD task. Experimental results show the effectiveness of our BAN in improving the performance of existing CD methods (e.g., up to 4.08\% IoU improvement) with only a few additional learnable parameters. More importantly, these successful practices show us the potential of foundation models for remote sensing CD. The code is available at \url{https://github.com/likyoo/BAN} and will be supported in our Open-CD.

