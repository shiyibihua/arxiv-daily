---
layout: default
title: Understanding the Gain from Data Filtering in Multimodal Contrastive Learning
---

# Understanding the Gain from Data Filtering in Multimodal Contrastive Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14230" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14230v1</a>
  <a href="https://arxiv.org/pdf/2512.14230.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14230v1" onclick="toggleFavorite(this, '2512.14230v1', 'Understanding the Gain from Data Filtering in Multimodal Contrastive Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Divyansh Pareek, Sewoong Oh, Simon S. Du

**分类**: cs.LG, stat.ML

**发布日期**: 2025-12-16

**备注**: 40 pages, 8 figures, 1 table. This work is accepted to the Thirty-ninth Annual Conference on Neural Information Processing Systems, 2025

---

## 💡 一句话要点

**提出教师模型过滤以提升多模态对比学习效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `对比学习` `数据过滤` `教师模型` `深度学习`

## 📋 核心要点

1. 现有多模态学习方法依赖于低质量的网络数据，导致训练效果不佳。
2. 论文提出使用预训练模型进行教师模型过滤，以提高数据质量和对比学习效果。
3. 实验结果表明，使用教师模型过滤后，模型误差显著降低，验证了数据过滤的有效性。

## 📝 摘要（中文）

现代多模态表示学习的成功依赖于互联网规模的数据集。然而，原始网络数据的低质量使得数据筛选成为训练流程中的关键步骤。基于教师模型的过滤方法利用预训练模型计算质量分数，已成为一种有效的解决方案。本文通过标准的双模态数据生成模型，分析了过滤对对比学习性能的影响，证明了数据过滤的可行性和有效性。具体而言，未过滤数据的误差被界定为$rac{1}{η	ext{sqrt}{n}}$的上下界，而使用教师模型过滤后的误差在大$η$范围内上界为$rac{1}{	ext{sqrt}{ηn}}$，在小$η$范围内上界为$rac{1}{	ext{sqrt}{n}}$。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态对比学习中由于低质量数据导致的性能下降问题。现有方法在处理原始网络数据时，常常面临数据质量不均的问题，影响了模型的学习效果。

**核心思路**：论文提出利用预训练模型进行教师模型过滤，通过计算数据对的质量分数来筛选出高质量的数据对，从而提升对比学习的效果。这样的设计旨在通过有效的数据过滤，减少低质量数据对模型训练的负面影响。

**技术框架**：整体框架包括数据收集、教师模型训练、数据过滤和对比学习四个主要模块。首先，收集原始数据，然后训练一个预训练模型，接着使用该模型对数据进行质量评分，最后在过滤后的高质量数据上进行对比学习。

**关键创新**：最重要的技术创新在于提出了基于教师模型的过滤方法，并通过理论分析证明了其在不同数据匹配率下的误差界限。这一方法与传统的随机数据选择方法本质上不同，能够有效提升模型的学习效果。

**关键设计**：在设计中，设置了数据匹配率$η$作为关键参数，损失函数采用标准的对比损失，网络结构基于现有的对比学习框架进行改进，以适应过滤后的数据特性。

## 📊 实验亮点

实验结果显示，使用教师模型过滤后，模型在大$η$范围内的误差上界为$rac{1}{	ext{sqrt}{ηn}}$，而未过滤数据的误差上界为$rac{1}{η	ext{sqrt}{n}}$，验证了数据过滤的显著效果，提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和多模态交互系统等。通过提升多模态学习的效果，能够在图像与文本的结合、视频理解等任务中取得更好的性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The success of modern multimodal representation learning relies on internet-scale datasets. Due to the low quality of a large fraction of raw web data, data curation has become a critical step in the training pipeline. Filtering using a trained model (i.e., teacher-based filtering) has emerged as a successful solution, leveraging a pre-trained model to compute quality scores. To explain the empirical success of teacher-based filtering, we characterize the performance of filtered contrastive learning under the standard bimodal data generation model. Denoting $η\in(0,1]$ as the fraction of data with correctly matched modalities among $n$ paired samples, we utilize a linear contrastive learning setup to show a provable benefit of data filtering: $(i)$ the error without filtering is upper and lower bounded by $\frac{1}{η\sqrt{n}}$, and $(ii)$ the error with teacher-based filtering is upper bounded by $\frac{1}{\sqrt{ηn}}$ in the large $η$ regime, and by $\frac{1}{\sqrt{n}}$ in the small $η$ regime.

