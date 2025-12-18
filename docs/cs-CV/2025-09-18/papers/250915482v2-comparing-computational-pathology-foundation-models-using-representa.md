---
layout: default
title: Comparing Computational Pathology Foundation Models using Representational Similarity Analysis
---

# Comparing Computational Pathology Foundation Models using Representational Similarity Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15482" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15482v2</a>
  <a href="https://arxiv.org/pdf/2509.15482.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15482v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15482v2', 'Comparing Computational Pathology Foundation Models using Representational Similarity Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vaibhav Mishra, William Lotter

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-18 (更新: 2025-11-05)

**备注**: Proceedings of the 5th Machine Learning for Health (ML4H) Symposium

---

## 💡 一句话要点

**利用表征相似性分析比较计算病理学领域多个预训练模型，揭示其表征结构差异。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算病理学` `预训练模型` `表征相似性分析` `模型集成` `医学影像`

## 📋 核心要点

1. 计算病理学预训练模型发展迅速，但对其内部表征的结构和差异性缺乏深入了解，阻碍了模型优化和集成。
2. 论文采用表征相似性分析（RSA）方法，系统比较了六个主流计算病理学预训练模型的表征空间。
3. 实验发现不同模型表征结构差异显著，且模型表征对切片依赖性高，染色标准化能有效降低这种依赖性。

## 📝 摘要（中文）

计算病理学（CPath）领域中，预训练模型因其在促进下游任务方面的潜力而得到越来越多的发展。尽管最近的研究已经评估了不同模型在任务上的性能，但对其学习到的表征的结构和变异性知之甚少。本文系统地分析了六个CPath预训练模型的表征空间，使用了计算神经科学中流行的技术。分析的模型涵盖了视觉-语言对比学习（CONCH、PLIP、KEEP）和自蒸馏（UNI (v2)、Virchow (v2)、Prov-GigaPath）方法。通过使用来自TCGA的H&E图像块进行表征相似性分析，发现UNI2和Virchow2具有最独特的表征结构，而Prov-Gigapath在模型中具有最高的平均相似性。具有相同的训练范式（仅视觉与视觉-语言）并不能保证更高的表征相似性。所有模型的表征都表现出高度的切片依赖性，但疾病依赖性相对较低。染色标准化使所有模型的切片依赖性降低了5.5%（CONCH）到20.5%（PLIP）。在内在维度方面，与仅视觉模型的更分布式表征相比，视觉-语言模型表现出相对紧凑的表征。这些发现突出了提高对切片特定特征的鲁棒性的机会，为模型集成策略提供了信息，并深入了解了训练范式如何塑造模型表征。我们的框架可以扩展到医学成像领域，在这些领域中，探测预训练模型的内部表征可以支持其有效开发和部署。

## 🔬 方法详解

**问题定义**：计算病理学领域涌现出大量预训练模型，但如何理解和比较这些模型的内部表征，以及如何利用这些信息来改进模型性能和集成策略，是一个重要的挑战。现有方法主要关注模型在特定任务上的性能，而忽略了对其内部表征结构的深入分析。

**核心思路**：论文的核心思路是利用表征相似性分析（RSA）这一工具，将不同预训练模型对同一批图像的表征进行比较，从而揭示它们在学习到的特征空间上的差异和相似性。通过分析这些差异，可以更好地理解不同训练范式对模型表征的影响，并为模型集成和优化提供指导。

**技术框架**：论文的技术框架主要包括以下几个步骤：1）选择六个具有代表性的计算病理学预训练模型，涵盖视觉-语言对比学习和自蒸馏等不同训练范式；2）使用来自TCGA的H&E染色病理图像块作为输入；3）提取每个模型对这些图像块的表征向量；4）计算不同模型表征之间的相似性矩阵；5）分析相似性矩阵，揭示不同模型表征结构的差异和相似性，以及它们对切片和疾病的依赖性。

**关键创新**：论文的关键创新在于将表征相似性分析这一在计算神经科学中广泛应用的方法引入到计算病理学领域，用于比较和理解不同预训练模型的内部表征。这种方法能够提供比传统任务性能评估更深入的洞察，帮助研究人员更好地理解模型行为，并指导模型设计和集成。

**关键设计**：论文的关键设计包括：1）选择具有代表性的预训练模型，覆盖不同的训练范式；2）使用来自TCGA的H&E染色图像块，保证了实验数据的多样性和代表性；3）采用多种表征相似性度量方法，以确保结果的稳健性；4）分析模型表征对切片和疾病的依赖性，揭示了模型潜在的偏差。

## 📊 实验亮点

实验结果表明，UNI2和Virchow2具有最独特的表征结构，而Prov-Gigapath具有最高的平均相似性。视觉-语言模型展现出相对紧凑的表征，而仅视觉模型则具有更分散的表征。染色标准化能够显著降低模型对切片的依赖性，最高可降低20.5%（PLIP）。

## 🎯 应用场景

该研究成果可应用于计算病理学模型的选择、集成与优化。通过理解不同模型的表征差异，可以选择互补的模型进行集成，提高整体性能。此外，该方法还可以用于诊断模型偏差，例如对特定切片或疾病的过度依赖，从而指导模型改进，提升泛化能力。该方法还可推广到其他医学影像领域。

## 📄 摘要（原文）

> Foundation models are increasingly developed in computational pathology (CPath) given their promise in facilitating many downstream tasks. While recent studies have evaluated task performance across models, less is known about the structure and variability of their learned representations. Here, we systematically analyze the representational spaces of six CPath foundation models using techniques popularized in computational neuroscience. The models analyzed span vision-language contrastive learning (CONCH, PLIP, KEEP) and self-distillation (UNI (v2), Virchow (v2), Prov-GigaPath) approaches. Through representational similarity analysis using H&E image patches from TCGA, we find that UNI2 and Virchow2 have the most distinct representational structures, whereas Prov-Gigapath has the highest average similarity across models. Having the same training paradigm (vision-only vs. vision-language) did not guarantee higher representational similarity. The representations of all models showed a high slide-dependence, but relatively low disease-dependence. Stain normalization decreased slide-dependence for all models by a range of 5.5% (CONCH) to 20.5% (PLIP). In terms of intrinsic dimensionality, vision-language models demonstrated relatively compact representations, compared to the more distributed representations of vision-only models. These findings highlight opportunities to improve robustness to slide-specific features, inform model ensembling strategies, and provide insights into how training paradigms shape model representations. Our framework is extendable across medical imaging domains, where probing the internal representations of foundation models can support their effective development and deployment.

