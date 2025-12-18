---
layout: default
title: Neural network embeddings recover value dimensions from psychometric survey items on par with human data
---

# Neural network embeddings recover value dimensions from psychometric survey items on par with human data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24906" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24906v1</a>
  <a href="https://arxiv.org/pdf/2509.24906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24906v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24906v1', 'Neural network embeddings recover value dimensions from psychometric survey items on par with human data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Max Pellert, Clemens M. Lechner, Indira Sen, Markus Strohmaier

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出SQuID方法，利用神经网络嵌入从心理测量问卷条目中恢复价值维度，性能与人类数据相当。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理测量学` `问卷调查` `语义嵌入` `大型语言模型` `价值观` `维度恢复` `SQuID`

## 📋 核心要点

1. 现有方法难以在心理测量学中有效提取问卷条目的潜在维度，尤其是在维度间存在负相关时，需要领域知识进行微调。
2. 论文提出SQuID方法，利用大型语言模型生成的嵌入，通过差异化处理，无需领域微调即可恢复人类价值观结构。
3. 实验结果表明，SQuID方法能够解释维度间相似性中55%的方差，多维尺度配置与人类数据具有较好的因子同余系数。

## 📝 摘要（中文）

本研究提出了一种名为“问卷条目嵌入差异”（SQuID）的新方法，该方法使神经网络嵌入能够有效地从心理测量问卷条目中恢复潜在维度。我们证明，通过SQuID处理的大型语言模型生成的嵌入可以恢复从修订版肖像价值问卷（PVQ-RR）的人类评估中获得的人类价值观结构。我们的实验验证比较了多个嵌入模型在多个评估指标上的表现。与以往的方法不同，SQuID成功地解决了在不需要领域特定微调的情况下获得维度之间负相关的问题。定量分析表明，与人类数据相比，我们基于嵌入的方法解释了维度间相似性中55%的方差。来自两种类型数据的多维尺度配置显示出相当的因子同余系数，并且在很大程度上遵循了底层理论。这些结果表明，语义嵌入可以有效地复制先前通过广泛的人类调查建立的心理测量结构。该方法在成本、可扩展性和灵活性方面具有显著优势，同时保持了与传统方法相当的质量。我们的发现对心理测量学和社会科学研究具有重要意义，提供了一种补充方法，可以扩展测量工具中表示的人类行为和经验的范围。

## 🔬 方法详解

**问题定义**：心理测量学中，如何从问卷调查条目中准确提取潜在的价值维度是一个重要问题。现有方法，特别是基于传统统计的方法，往往难以捕捉维度之间的复杂关系，尤其是在存在负相关的情况下。此外，这些方法通常需要领域专家的参与和大量的先验知识，限制了其可扩展性和通用性。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语义理解能力，将问卷条目嵌入到高维语义空间中。然后，通过一种新的差异化处理方法（SQuID），从这些嵌入中提取出能够反映人类价值观结构的潜在维度。这种方法的核心在于，它能够自动地学习维度之间的关系，包括负相关，而无需人工干预或领域特定的微调。

**技术框架**：该方法主要包含以下几个阶段：1) 使用大型语言模型（如BERT、RoBERTa等）将问卷条目转换为语义嵌入。2) 应用SQuID方法，计算条目嵌入之间的差异，以捕捉维度之间的关系。3) 使用多维尺度分析（MDS）等方法，将高维嵌入映射到低维空间，以便可视化和分析。4) 将提取的维度与人类评估数据进行比较，评估方法的有效性。

**关键创新**：该方法最重要的创新点在于SQuID（Survey and Questionnaire Item Embeddings Differentials）方法，它能够有效地从语言模型嵌入中恢复潜在维度，并且能够处理维度之间的负相关关系，而无需领域特定的微调。这与以往需要人工干预或领域知识的方法形成了鲜明对比。

**关键设计**：SQuID方法的关键在于计算条目嵌入之间的差异。具体来说，对于每个维度，SQuID计算属于该维度的条目嵌入与其他条目嵌入之间的差异。这些差异被用来构建一个维度表示向量，该向量能够反映该维度与其他维度之间的关系。此外，论文还使用了多种评估指标，如方差解释率和因子同余系数，来评估方法的有效性。

## 📊 实验亮点

实验结果表明，基于SQuID的嵌入方法能够解释维度间相似性中55%的方差，与人类数据相比具有很高的吻合度。多维尺度配置显示出相当的因子同余系数，并且在很大程度上遵循了底层理论。重要的是，该方法无需领域特定的微调，即可成功恢复维度之间的负相关关系。

## 🎯 应用场景

该研究成果可广泛应用于心理学、社会学、市场调研等领域。通过自动分析问卷调查数据，可以更高效、更经济地了解人群的价值观、态度和行为模式。此外，该方法还可以用于构建更精确的心理测量工具，例如人格测试和价值观评估。

## 📄 摘要（原文）

> This study introduces "Survey and Questionnaire Item Embeddings Differentials" (SQuID), a novel methodological approach that enables neural network embeddings to effectively recover latent dimensions from psychometric survey items. We demonstrate that embeddings derived from large language models, when processed with SQuID, can recover the structure of human values obtained from human rater judgments on the Revised Portrait Value Questionnaire (PVQ-RR). Our experimental validation compares multiple embedding models across a number of evaluation metrics. Unlike previous approaches, SQuID successfully addresses the challenge of obtaining negative correlations between dimensions without requiring domain-specific fine-tuning. Quantitative analysis reveals that our embedding-based approach explains 55% of variance in dimension-dimension similarities compared to human data. Multidimensional scaling configurations from both types of data show fair factor congruence coefficients and largely follow the underlying theory. These results demonstrate that semantic embeddings can effectively replicate psychometric structures previously established through extensive human surveys. The approach offers substantial advantages in cost, scalability and flexibility while maintaining comparable quality to traditional methods. Our findings have significant implications for psychometrics and social science research, providing a complementary methodology that could expand the scope of human behavior and experience represented in measurement tools.

