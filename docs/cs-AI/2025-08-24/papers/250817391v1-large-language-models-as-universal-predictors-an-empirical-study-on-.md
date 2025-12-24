---
layout: default
title: Large Language Models as Universal Predictors? An Empirical Study on Small Tabular Datasets
---

# Large Language Models as Universal Predictors? An Empirical Study on Small Tabular Datasets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17391" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17391v1</a>
  <a href="https://arxiv.org/pdf/2508.17391.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17391v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17391v1', 'Large Language Models as Universal Predictors? An Empirical Study on Small Tabular Datasets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikolaos Pavlidis, Vasilis Perifanis, Symeon Symeonidis, Pavlos S. Efraimidis

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-24

---

## 💡 一句话要点

**探讨大型语言模型在小型表格数据集上的预测能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `函数逼近` `小型数据集` `分类任务` `回归任务` `聚类任务` `上下文学习` `商业智能`

## 📋 核心要点

1. 现有机器学习方法在小型结构化数据集上的表现受限，尤其在数据稀缺情况下。
2. 本文提出利用大型语言模型的上下文学习能力，进行小型表格数据的预测任务，避免显式微调。
3. 实验结果显示，LLMs在分类任务中表现强劲，而在回归和聚类任务中存在明显局限性。

## 📝 摘要（中文）

大型语言模型（LLMs）最初为自然语言处理（NLP）而开发，已显示出跨模态和领域的泛化潜力。本文研究了LLMs在小规模结构化数据集上的函数逼近能力，涵盖分类、回归和聚类任务。通过对比多种先进LLMs（如GPT-5、GPT-4o等）与传统机器学习基线模型，结果表明LLMs在有限数据下的分类任务表现优异，但在回归和聚类任务中表现较差。该研究为商业智能和探索性分析提供了低开销的数据探索替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在小型结构化数据集上的预测能力，现有方法在数据稀缺情况下表现不佳，尤其在回归和聚类任务中。

**核心思路**：通过利用LLMs的上下文学习（ICL）能力，进行分类、回归和聚类任务的预测，避免了传统方法的显式微调过程。

**技术框架**：研究采用了多种先进的LLMs（如GPT-5、Gemini-2.5-Flash等）进行实验，并与线性模型、集成方法和表格基础模型（TFMs）进行对比，评估其在少量样本提示下的表现。

**关键创新**：本文的创新在于将LLMs应用于小型结构化数据集的预测任务，展示了其在分类任务中的强大能力，同时揭示了其在回归和聚类任务中的局限性。

**关键设计**：实验中关注上下文大小和提示结构对预测质量的影响，识别出影响预测性能的权衡因素。

## 📊 实验亮点

实验结果表明，在分类任务中，LLMs在有限数据下表现优异，建立了实际的零训练基线；而在回归任务中，LLMs的表现明显低于传统机器学习模型，显示出其在不同任务上的性能差异。

## 🎯 应用场景

该研究为商业智能和探索性分析提供了新的思路，尤其在数据稀缺的情况下，LLMs可以作为快速、低开销的数据探索工具，帮助企业在决策过程中更有效地利用有限的数据资源。

## 📄 摘要（原文）

> Large Language Models (LLMs), originally developed for natural language processing (NLP), have demonstrated the potential to generalize across modalities and domains. With their in-context learning (ICL) capabilities, LLMs can perform predictive tasks over structured inputs without explicit fine-tuning on downstream tasks. In this work, we investigate the empirical function approximation capability of LLMs on small-scale structured datasets for classification, regression and clustering tasks. We evaluate the performance of state-of-the-art LLMs (GPT-5, GPT-4o, GPT-o3, Gemini-2.5-Flash, DeepSeek-R1) under few-shot prompting and compare them against established machine learning (ML) baselines, including linear models, ensemble methods and tabular foundation models (TFMs). Our results show that LLMs achieve strong performance in classification tasks under limited data availability, establishing practical zero-training baselines. In contrast, the performance in regression with continuous-valued outputs is poor compared to ML models, likely because regression demands outputs in a large (often infinite) space, and clustering results are similarly limited, which we attribute to the absence of genuine ICL in this setting. Nonetheless, this approach enables rapid, low-overhead data exploration and offers a viable alternative to traditional ML pipelines in business intelligence and exploratory analytics contexts. We further analyze the influence of context size and prompt structure on approximation quality, identifying trade-offs that affect predictive performance. Our findings suggest that LLMs can serve as general-purpose predictive engines for structured data, with clear strengths in classification and significant limitations in regression and clustering.

