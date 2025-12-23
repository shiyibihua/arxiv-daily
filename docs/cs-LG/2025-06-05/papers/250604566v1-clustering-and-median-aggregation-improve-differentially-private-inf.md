---
layout: default
title: Clustering and Median Aggregation Improve Differentially Private Inference
---

# Clustering and Median Aggregation Improve Differentially Private Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04566" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04566v1</a>
  <a href="https://arxiv.org/pdf/2506.04566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04566v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04566v1', 'Clustering and Median Aggregation Improve Differentially Private Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kareem Amin, Salman Avestimehr, Sara Babakniya, Alex Bie, Weiwei Kong, Natalia Ponomareva, Umar Syed

**分类**: cs.LG, cs.AI, cs.CL, cs.CR

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**通过聚类与中位数聚合提升差分隐私推断质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `差分隐私` `语言模型` `聚类` `中位数聚合` `合成文本` `隐私保护` `文本生成`

## 📋 核心要点

1. 现有的差分隐私推断方法通过随机均匀抽样创建推断批次，导致生成文本质量下降，尤其是在处理异质主题时。
2. 本文提出通过聚类输入数据来选择推断批次，并引入中位数聚合算法，以提高相似下一个标记预测的质量和隐私保护。
3. 实验结果显示，所提方法在代表性指标和下游任务性能上均有显著提升，且在隐私成本上优于现有最先进方法。

## 📝 摘要（中文）

差分隐私（DP）语言模型推断是一种生成私密合成文本的方法。以敏感输入示例为提示，促使大型语言模型（LLM）生成相似示例。现有方法通过随机均匀抽样敏感输入来创建推断批次，但这种方法在处理异质主题时会降低生成文本的质量。本文提出通过聚类输入数据来改善推断批次选择，并引入中位数聚合算法，以提高相似下一个标记预测的隐私保护效果。实验结果表明，该方法在代表性指标（如MAUVE）和下游任务性能上均有显著提升，且在隐私成本上优于之前的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有差分隐私推断方法中，由于随机均匀抽样导致的生成文本质量下降的问题，尤其是在处理异质主题时。

**核心思路**：通过聚类输入数据，选择更具相似性的推断批次，从而提高生成文本的质量。同时，利用中位数聚合算法替代平均值聚合，以增强隐私保护效果。

**技术框架**：整体流程包括数据聚类、推断批次选择和中位数聚合三个主要模块。首先对输入数据进行聚类，然后从每个聚类中选择推断样本，最后通过中位数计算生成下一个标记的统计信息。

**关键创新**：本文的主要创新在于结合聚类和中位数聚合，形成了一种新的隐私保护算法，显著提高了生成文本的质量和隐私保障，与现有方法相比具有本质区别。

**关键设计**：在聚类过程中，采用了基于主题相似性的聚类算法；在聚合阶段，使用中位数而非平均值，以降低局部灵敏度，确保隐私保护的有效性。

## 📊 实验亮点

实验结果表明，所提方法在MAUVE指标上较之前的最先进方法提升了显著的代表性，同时在下游任务的性能上也有明显改善，且隐私成本显著降低，展示了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、个性化推荐系统以及任何需要生成私密文本的场景。通过提高合成文本的质量和隐私保护能力，能够更好地满足用户对隐私的需求，同时提升文本生成的实用性和可靠性。

## 📄 摘要（原文）

> Differentially private (DP) language model inference is an approach for generating private synthetic text. A sensitive input example is used to prompt an off-the-shelf large language model (LLM) to produce a similar example. Multiple examples can be aggregated together to formally satisfy the DP guarantee.
>   Prior work creates inference batches by sampling sensitive inputs uniformly at random. We show that uniform sampling degrades the quality of privately generated text, especially when the sensitive examples concern heterogeneous topics.
>   We remedy this problem by clustering the input data before selecting inference batches. Next, we observe that clustering also leads to more similar next-token predictions across inferences. We use this insight to introduce a new algorithm that aggregates next token statistics by privately computing medians instead of averages. This approach leverages the fact that the median has decreased local sensitivity when next token predictions are similar, allowing us to state a data-dependent and ex-post DP guarantee about the privacy properties of this algorithm. Finally, we demonstrate improvements in terms of representativeness metrics (e.g., MAUVE) as well as downstream task performance. We show that our method produces high-quality synthetic data at significantly lower privacy cost than a previous state-of-the-art method.

