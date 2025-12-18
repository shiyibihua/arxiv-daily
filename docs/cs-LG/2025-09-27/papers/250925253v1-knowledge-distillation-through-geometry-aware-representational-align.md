---
layout: default
title: Knowledge distillation through geometry-aware representational alignment
---

# Knowledge distillation through geometry-aware representational alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25253" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25253v1</a>
  <a href="https://arxiv.org/pdf/2509.25253.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25253v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25253v1', 'Knowledge distillation through geometry-aware representational alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prajjwal Bhattarai, Mohammad Amjad, Dmytro Zhylko, Tuka Alhanai

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出基于几何感知的表征对齐知识蒸馏方法，提升语言模型性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `特征对齐` `几何感知` `Procrustes距离` `Frobenius范数` `语言模型` `模型压缩`

## 📋 核心要点

1. 现有特征蒸馏方法难以有效捕捉教师模型的特征空间结构，限制了蒸馏效果。
2. 论文提出利用Procrustes距离和特征Gram矩阵的Frobenius范数作为蒸馏损失，对齐特征几何。
3. 实验结果表明，该方法在BERT和OPT等语言模型上，分类和指令跟随任务的性能均有显著提升。

## 📝 摘要（中文）

知识蒸馏是一种常见的将能力从大型模型迁移到小型模型的范式。传统的蒸馏方法利用教师和学生模型输出的概率分布差异，而基于特征的蒸馏方法通常最小化隐藏层表征之间欧几里得范数的变体。其主要目标是让学生模型模仿教师模型的特征空间结构。本文从理论上证明，现有的特征蒸馏方法，如基于投影的均方误差损失或中心核对齐（CKA），即使在零损失下也无法捕获特征结构。因此，本文提出使用Procrustes距离和特征Gram矩阵的Frobenius范数（这些距离在表征对齐的上下文中已经很常见）作为蒸馏损失。实验表明，通过本文方法进行的特征蒸馏在分类和指令跟随任务中，跨语言模型系列（BERT和OPT）的蒸馏性能上实现了高达2个百分点的统计显著提升，展示了将特征几何集成到现有蒸馏方法中的潜力。

## 🔬 方法详解

**问题定义**：现有的基于特征的知识蒸馏方法，例如基于投影的均方误差损失或中心核对齐（CKA），在对齐教师和学生模型的特征表示时，无法有效地捕捉教师模型的特征空间几何结构。即使损失函数达到零，学生模型也可能无法学习到与教师模型相似的特征空间结构，从而限制了知识迁移的效果。

**核心思路**：论文的核心思路是利用Procrustes距离和特征Gram矩阵的Frobenius范数来度量和对齐教师和学生模型之间的特征表示。这些度量方法能够更好地捕捉特征空间中的几何关系，例如特征之间的距离和角度，从而使学生模型能够更准确地模仿教师模型的特征空间结构。

**技术框架**：该方法主要包含以下几个步骤：1. 使用教师模型和学生模型处理相同的输入数据。2. 提取教师模型和学生模型的中间层特征表示。3. 使用Procrustes距离或特征Gram矩阵的Frobenius范数计算教师模型和学生模型特征表示之间的距离。4. 将该距离作为蒸馏损失，用于训练学生模型。通过最小化该损失，学生模型可以学习到与教师模型相似的特征空间结构。

**关键创新**：该方法最重要的技术创新点在于使用了Procrustes距离和特征Gram矩阵的Frobenius范数作为蒸馏损失。与传统的基于欧几里得距离的损失函数相比，这些度量方法能够更好地捕捉特征空间中的几何关系，从而提高了知识蒸馏的效果。

**关键设计**：关键设计包括：1. 选择合适的中间层特征表示进行对齐。2. 选择合适的Procrustes距离或特征Gram矩阵的Frobenius范数计算方法。3. 调整蒸馏损失在总损失中的权重。4. 实验中使用了BERT和OPT等语言模型，并在分类和指令跟随任务上进行了评估。

## 📊 实验亮点

实验结果表明，使用Procrustes距离和特征Gram矩阵的Frobenius范数作为蒸馏损失，在BERT和OPT等语言模型上，分类和指令跟随任务的性能均有显著提升，最高可达2个百分点。这些结果表明，该方法能够有效地提高知识蒸馏的效果，并具有广泛的适用性。

## 🎯 应用场景

该研究成果可应用于各种需要模型压缩和加速的场景，例如移动设备上的自然语言处理、边缘计算和资源受限环境下的模型部署。通过知识蒸馏，可以将大型、复杂的模型压缩成小型、高效的模型，同时保持较高的性能水平，从而降低计算成本和延迟，提高用户体验。该方法在工业界具有广泛的应用前景。

## 📄 摘要（原文）

> Knowledge distillation is a common paradigm for transferring capabilities from larger models to smaller ones. While traditional distillation methods leverage a probabilistic divergence over the output of the teacher and student models, feature-based distillation methods often minimize variants of Euclidean norms between the hidden layer representations. The main goal is for the student to mimic the structure of the feature space of the teacher. In this work, we theoretically show that existing feature distillation methods, such as projection based mean squared loss or Centered Kernel Alignment (CKA), cannot capture the feature structure, even under zero loss. We then motivate the use of Procrustes distance and the Frobenius norm of Feature Gram Matrix, distances already common in the context of measuring representational alignment, as distillation losses. We show that feature distillation through our method showcases statistically significant improvement in distillation performance across language models families (BERT and OPT) in classification and instruction-following tasks by up to 2 percentage points, showcasing the potential of integrating feature geometry into existing distillation methods.

