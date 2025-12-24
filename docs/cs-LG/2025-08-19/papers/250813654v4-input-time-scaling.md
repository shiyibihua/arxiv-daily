---
layout: default
title: Input-Time Scaling
---

# Input-Time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13654" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13654v4</a>
  <a href="https://arxiv.org/pdf/2508.13654.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13654v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13654v4', 'Input-Time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rapheal Huang, Weilong Guo

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-19 (更新: 2025-09-12)

---

## 💡 一句话要点

**提出输入时间缩放方法以提升大语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `输入时间缩放` `大型语言模型` `训练-测试共设计` `元知识` `自然语言处理`

## 📋 核心要点

1. 现有的大型语言模型在数据和训练的缩放方面存在局限，推理时间的优化也未能充分利用输入的潜力。
2. 本文提出的输入时间缩放方法，通过在训练和测试阶段优化输入，利用元知识提升模型性能。
3. 在Qwen2.5-32B-Instruct模型上，实验结果显示该方法在AIME24和AIME25任务上达到了76.7%的SOTA性能，且通过模型投票进一步提升了结果。

## 📝 摘要（中文）

当前的大型语言模型（LLMs）通常依赖于后期训练和推理时间的缩放方法。本文提出了一种新的缩放范式——输入时间缩放，通过在查询上投入资源来补充之前的缩放方法。在训练和测试过程中，我们利用LLMs的元知识，通过不同策略优化输入。此外，我们发现了一种新的现象——训练-测试共设计，要求在训练和测试中整体应用查询策略。实验表明，低质量数据集也能表现出色，甚至在添加无关信息的情况下，使用最小过滤数据集的随机1k示例也能获得最佳性能。这些发现挑战了“垃圾进，垃圾出”的传统观点，并与“少即是多”的现象相兼容。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在数据和推理时间缩放方面的不足，特别是如何有效利用输入信息以提升模型性能。

**核心思路**：提出输入时间缩放的概念，通过在训练和测试阶段整体应用查询策略，利用元知识优化输入，从而提升模型的推理能力。

**技术框架**：整体流程包括数据准备、模型训练和测试阶段。在训练阶段，应用不同的查询策略来优化输入；在测试阶段，保持一致的策略以确保性能提升。

**关键创新**：最重要的创新在于提出了训练-测试共设计的概念，强调在两个阶段中一致性的重要性，这与传统的单一阶段优化方法形成鲜明对比。

**关键设计**：在实验中，使用了随机选择的1k示例进行训练，发现即使在低质量数据集上，模型也能获得较好的性能，挑战了传统的高质量数据集的必要性。

## 📊 实验亮点

实验结果显示，使用输入时间缩放方法，Qwen2.5-32B-Instruct模型在AIME24和AIME25任务上达到了76.7%的SOTA性能。通过三模型的多数投票，进一步提升至AIME24的90.0%和AIME25的80%，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过优化输入策略，模型能够在资源有限的情况下实现更高的推理能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Current Large Language Models (LLMs) are usually post-trained on large-scale carefully curated datasets (data & training scaling) and doing reasoning in test time (inference time scaling). In this work, we present a new scaling paradigm, Input-Time Scaling, to complement previous scaling methods by putting resources on queries (input time). During training and testing, we utilize meta-knowledge from LLMs to refine inputs with different strategies. We also discover a new phenomenon, train-test co-design. It requires us to apply query strategies during training and testing as a whole. Only applying strategies on training or testing would seriously degrade the performance gained. We are also surprised to find that seemingly low data quality datasets can perform better. We can get the best performance even by adding irrelevant information to the queries, with randomly selected 1k examples from a minimally filtered dataset. These findings contradict the widely held inductive bias, "garbage in, garbage out". Curating datasets with seemingly high-quality data can even potentially limit the performance ceiling. In addition, models trained on more data with similar quality (15k VS 1k) perform worse, the intuition of simply scaling the size should also be carefully inspected. The good news is that our findings are compatible with the Less is More phenomenon. 1K examples are enough to invoke high-level reasoning ability. With experiments on Qwen2.5-32B-Instruct, we are able to reach SOTA performance among 32B models on AIME24(76.7%) and AIME25(76.7%) pass@1. We can further achieve AIME24(76.7%) and AIME25(80%) with a majority vote of three models. Starting from DeepSeek-R1-Distill-Qwen-32B, the result would be 90.0% on AIME24 and 80.0% on AIME25. To facilitate reproducibility and further research, we are working on open-source our datasets, data pipelines, evaluation results, and checkpoints.

