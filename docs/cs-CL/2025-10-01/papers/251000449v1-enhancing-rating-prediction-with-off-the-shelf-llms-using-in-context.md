---
layout: default
title: Enhancing Rating Prediction with Off-the-Shelf LLMs Using In-Context User Reviews
---

# Enhancing Rating Prediction with Off-the-Shelf LLMs Using In-Context User Reviews

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00449" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00449v1</a>
  <a href="https://arxiv.org/pdf/2510.00449.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00449v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00449v1', 'Enhancing Rating Prediction with Off-the-Shelf LLMs Using In-Context User Reviews')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Koki Ryu, Hitomi Yanaka

**分类**: cs.CL

**发布日期**: 2025-10-01

**备注**: Accepted to EMNLP 2025 PALS Workshop

**🔗 代码/项目**: [GITHUB](https://github.com/ynklab/rating-prediction-with-reviews)

---

## 💡 一句话要点

**利用上下文用户评论，增强现成LLM的评分预测能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `评分预测` `大型语言模型` `上下文学习` `用户评论` `推荐系统`

## 📋 核心要点

1. 现有方法在Likert量表评分预测任务中，缺乏对语言和数学推理的有效结合，限制了LLM在工业应用中的潜力。
2. 该研究的核心思想是利用用户评论作为上下文信息，提升现成LLM在评分预测任务中的性能。
3. 实验结果表明，用户评论显著提升了LLM的评分预测性能，与传统方法相比具有竞争力，尤其是在冷启动场景下。

## 📝 摘要（中文）

本文研究如何利用大型语言模型（LLM）进行个性化评分预测，使其与用户偏好对齐。现有研究主要集中在分类或排序任务，而忽略了Likert量表评分预测这一回归任务，该任务需要语言和数学推理能力。本文探索了现成LLM在评分预测任务中的性能，并考察了不同上下文信息的影响。通过在三个数据集上对八个模型进行实验，结果表明用户评论能显著提升LLM的评分预测性能，与矩阵分解等传统方法相当，突显了LLM在冷启动问题上的潜力。此外，针对具体项目的评论比一般偏好描述更有效。提示LLM首先生成假设评论也能增强评分预测性能。代码已开源。

## 🔬 方法详解

**问题定义**：论文旨在解决评分预测问题，特别是利用LLM进行个性化评分预测。现有方法，如矩阵分解，在冷启动问题上表现不佳，且难以有效利用用户评论等文本信息。现成LLM在评分预测任务上的能力尚未得到充分探索。

**核心思路**：论文的核心思路是利用上下文学习（In-Context Learning），将用户评论作为LLM的输入，引导LLM理解用户偏好，从而提升评分预测的准确性。通过提供与特定项目相关的评论，使LLM能够更好地捕捉用户对该项目的态度。

**技术框架**：整体流程包括：1) 选择合适的现成LLM；2) 构建包含用户评论的上下文提示（Prompt）；3) 将提示输入LLM，要求其预测评分；4) 评估LLM的预测性能。论文比较了不同类型的上下文信息，例如一般偏好描述和针对具体项目的评论。此外，还探索了让LLM先生成假设评论再进行评分预测的方法。

**关键创新**：论文的关键创新在于探索了现成LLM在评分预测任务中的潜力，并证明了用户评论作为上下文信息能够显著提升预测性能。此外，提出了让LLM先生成假设评论的策略，进一步提升了预测准确性。与传统方法相比，该方法能够直接利用用户评论等非结构化数据。

**关键设计**：论文的关键设计包括：1) 上下文提示的设计，包括选择哪些评论、如何组织评论信息等；2) 提示LLM生成假设评论的具体方式；3) 实验中使用的LLM模型选择，以及超参数的设置；4) 评分预测性能的评估指标，例如均方误差（MSE）等。

## 📊 实验亮点

实验结果表明，用户评论能显著提升LLM的评分预测性能，与矩阵分解等传统方法相当。针对具体项目的评论比一般偏好描述更有效。提示LLM首先生成假设评论也能增强评分预测性能。这些发现突显了LLM在评分预测任务中的潜力，尤其是在冷启动场景下。

## 🎯 应用场景

该研究成果可应用于推荐系统、在线购物平台、电影评分网站等领域，提升用户体验。通过利用用户评论，可以更准确地预测用户对特定项目的评分，从而提供更个性化的推荐服务。尤其是在冷启动场景下，该方法具有重要的应用价值，可以有效解决新用户或新项目的评分预测问题。

## 📄 摘要（原文）

> Personalizing the outputs of large language models (LLMs) to align with individual user preferences is an active research area. However, previous studies have mainly focused on classification or ranking tasks and have not considered Likert-scale rating prediction, a regression task that requires both language and mathematical reasoning to be solved effectively. This task has significant industrial applications, but the utilization of LLMs remains underexplored, particularly regarding the capabilities of off-the-shelf LLMs. This study investigates the performance of off-the-shelf LLMs on rating prediction, providing different in-context information. Through comprehensive experiments with eight models across three datasets, we demonstrate that user-written reviews significantly improve the rating prediction performance of LLMs. This result is comparable to traditional methods like matrix factorization, highlighting the potential of LLMs as a promising solution for the cold-start problem. We also find that the reviews for concrete items are more effective than general preference descriptions that are not based on any specific item. Furthermore, we discover that prompting LLMs to first generate a hypothetical review enhances the rating prediction performance. Our code is available at https://github.com/ynklab/rating-prediction-with-reviews.

