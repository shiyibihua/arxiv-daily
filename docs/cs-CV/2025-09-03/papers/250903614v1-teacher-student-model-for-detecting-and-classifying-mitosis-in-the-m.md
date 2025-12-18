---
layout: default
title: Teacher-Student Model for Detecting and Classifying Mitosis in the MIDOG 2025 Challenge
---

# Teacher-Student Model for Detecting and Classifying Mitosis in the MIDOG 2025 Challenge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03614" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03614v1</a>
  <a href="https://arxiv.org/pdf/2509.03614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03614v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03614v1', 'Teacher-Student Model for Detecting and Classifying Mitosis in the MIDOG 2025 Challenge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seungho Choe, Xiaoli Qin, Abubakr Shafique, Amanda Dy, Susan Done, Dimitrios Androutsos, April Khademi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-03

**备注**: 4 pages, 1 figures, final submission for MIDOG 2025 challenge

---

## 💡 一句话要点

**提出基于Teacher-Student模型的有丝分裂检测与分类方法，提升领域泛化性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `有丝分裂检测` `Teacher-Student模型` `领域泛化` `对比表示学习` `领域对抗训练` `病理图像分析` `多任务学习`

## 📋 核心要点

1. 现有有丝分裂检测方法易受领域偏移影响，在不同器官、物种和染色协议下性能下降，且数据不平衡问题严重。
2. 提出Teacher-Student模型，利用对比表示学习和领域对抗训练增强领域泛化性，并为正常细胞核生成伪掩码。
3. 实验结果表明，该方法在有丝分裂检测和非典型有丝分裂分类任务中均取得了较好的性能，F1 score 0.7660，平衡准确率0.8414。

## 📝 摘要（中文）

病理学家进行有丝分裂计数耗时且存在观察者间差异。人工智能有望通过自动检测有丝分裂像并保持决策一致性来解决此问题。然而，AI工具易受领域偏移的影响，即由于训练集和测试集之间的差异（包括器官、物种的形态多样性和染色协议的变化）而导致性能显著下降。此外，有丝分裂的数量远少于正常细胞核的数量，这为检测任务带来了严重的不平衡数据。本文将有丝分裂检测转化为像素级分割问题，并提出了一种Teacher-Student模型，该模型同时解决了有丝分裂检测（Track 1）和非典型有丝分裂分类（Track 2）。该方法基于UNet分割骨干网络，集成了领域泛化模块，即对比表示学习和领域对抗训练。采用Teacher-Student策略，不仅为带注释的有丝分裂和难负样本生成像素级伪掩码，还为正常细胞核生成伪掩码，从而增强了特征区分能力并提高了对领域偏移的鲁棒性。对于分类任务，引入了一种多尺度CNN分类器，该分类器利用分割模型中的特征图，采用多任务学习范式。在初步测试集上，该算法在Track 1中实现了0.7660的F1分数，在Track 2中实现了0.8414的平衡准确率，证明了将基于分割的检测和分类集成到统一框架中进行稳健的有丝分裂分析的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决病理学中人工有丝分裂检测耗时、主观性强，且现有AI方法在面对不同数据集（器官、物种、染色协议）时泛化能力不足的问题。现有方法在数据不平衡的情况下表现不佳，难以区分有丝分裂和正常细胞核。

**核心思路**：论文的核心思路是利用Teacher-Student模型，通过对比表示学习和领域对抗训练来提高模型的领域泛化能力。Teacher模型生成高质量的伪标签，指导Student模型学习，从而增强模型对不同领域数据的适应性。同时，对正常细胞核也生成伪标签，以增强特征区分能力。

**技术框架**：整体框架包含两个主要部分：基于UNet的分割模型和多尺度CNN分类器。分割模型负责有丝分裂的检测，分类器负责非典型有丝分裂的分类。分割模型集成了对比表示学习和领域对抗训练模块。Teacher-Student策略用于生成像素级伪掩码。分割模型的特征图被用于分类任务，形成多任务学习范式。

**关键创新**：最重要的创新点在于Teacher-Student框架在有丝分裂检测中的应用，以及对正常细胞核生成伪标签的设计。这使得模型能够更好地学习有丝分裂和正常细胞核之间的差异，从而提高检测精度和鲁棒性。同时，结合对比表示学习和领域对抗训练，有效提升了模型的领域泛化能力。

**关键设计**：分割模型采用UNet作为骨干网络，并集成了对比表示学习和领域对抗训练模块。Teacher模型和Student模型共享网络结构，但参数更新方式不同。损失函数包括分割损失、对比损失和对抗损失。多尺度CNN分类器利用分割模型的不同层级的特征图，以捕捉不同尺度的信息。具体的参数设置和损失函数权重等细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

该算法在MIDOG 2025挑战赛的初步测试集上取得了显著成果，在有丝分裂检测（Track 1）中实现了0.7660的F1分数，在非典型有丝分裂分类（Track 2）中实现了0.8414的平衡准确率。这些结果表明，该方法在解决领域偏移和数据不平衡问题方面具有有效性，并为有丝分裂分析提供了一个稳健的框架。

## 🎯 应用场景

该研究成果可应用于病理诊断辅助系统，帮助病理学家更快速、准确地检测和分类有丝分裂像，减少人为误差，提高诊断效率。该技术具有潜力应用于多种癌症类型的诊断和预后评估，并可扩展到其他医学图像分析任务。

## 📄 摘要（原文）

> Counting mitotic figures is time-intensive for pathologists and leads to inter-observer variability. Artificial intelligence (AI) promises a solution by automatically detecting mitotic figures while maintaining decision consistency. However, AI tools are susceptible to domain shift, where a significant drop in performance can occur due to differences in the training and testing sets, including morphological diversity between organs, species, and variations in staining protocols. Furthermore, the number of mitoses is much less than the count of normal nuclei, which introduces severely imbalanced data for the detection task. In this work, we formulate mitosis detection as a pixel-level segmentation and propose a teacher-student model that simultaneously addresses mitosis detection (Track 1) and atypical mitosis classification (Track 2). Our method is based on a UNet segmentation backbone that integrates domain generalization modules, namely contrastive representation learning and domain-adversarial training. A teacher-student strategy is employed to generate pixel-level pseudo-masks not only for annotated mitoses and hard negatives but also for normal nuclei, thereby enhancing feature discrimination and improving robustness against domain shift. For the classification task, we introduce a multi-scale CNN classifier that leverages feature maps from the segmentation model within a multi-task learning paradigm. On the preliminary test set, the algorithm achieved an F1 score of 0.7660 in Track 1 and balanced accuracy of 0.8414 in Track 2, demonstrating the effectiveness of integrating segmentation-based detection and classification into a unified framework for robust mitosis analysis.

