---
layout: default
title: Towards Understanding Bias in Synthetic Data for Evaluation
---

# Towards Understanding Bias in Synthetic Data for Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10301" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10301v2</a>
  <a href="https://arxiv.org/pdf/2506.10301.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10301v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10301v2', 'Towards Understanding Bias in Synthetic Data for Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hossein A. Rahmani, Varsha Ramineni, Emine Yilmaz, Nick Craswell, Bhaskar Mitra

**分类**: cs.IR, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-10-04)

**备注**: CIKM 2025

**🔗 代码/项目**: [GITHUB](https://github.com/rahmanidashti/BiasSyntheticData)

---

## 💡 一句话要点

**探讨合成数据中的偏差以优化信息检索系统评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据` `信息检索` `偏差分析` `大型语言模型` `系统评估` `线性混合效应模型`

## 📋 核心要点

1. 现有方法在创建多样化用户查询和获取相关性判断时面临高成本和资源密集的问题。
2. 本文提出利用大型语言模型生成合成测试集合，并分析其在评估中的偏差。
3. 实验证明合成测试集合中的偏差对绝对性能评估影响显著，但对相对性能比较影响较小。

## 📝 摘要（中文）

测试集合对于评估信息检索（IR）系统至关重要。然而，创建多样化的用户查询集合具有挑战性，获取相关性判断通常成本高昂且资源密集。近期，利用大型语言模型（LLMs）生成合成数据集的研究逐渐受到关注。尽管已有研究表明合成测试集合在系统评估中具有潜力，但对其可靠性的分析仍显不足。本文深入探讨使用LLMs构建的合成测试集合的可靠性，特别是评估过程中可能出现的偏差。通过实证分析，我们展示了评估结果中存在的偏差及其对系统评估的影响，并使用线性混合效应模型验证了这一偏差的存在。我们的分析表明，尽管合成测试集合中偏差对绝对系统性能的影响可能显著，但在比较相对系统性能时，其影响可能不那么显著。

## 🔬 方法详解

**问题定义**：本文旨在解决使用合成数据集进行信息检索系统评估时可能出现的偏差问题。现有方法在生成多样化测试集合时，往往忽视了合成数据的潜在偏差，导致评估结果不可靠。

**核心思路**：论文的核心思路是通过使用大型语言模型生成合成查询和标签，构建合成测试集合，并系统性地分析其在评估中的偏差。这种设计旨在揭示合成数据在评估中的可靠性和潜在问题。

**技术框架**：整体架构包括三个主要模块：首先，使用LLMs生成合成查询和相关性标签；其次，构建合成测试集合并进行系统评估；最后，应用线性混合效应模型分析评估结果中的偏差。

**关键创新**：本文的主要创新在于系统性地分析合成测试集合中的偏差，并通过实证研究验证其对评估结果的影响。这与以往仅关注合成查询生成的研究有本质区别。

**关键设计**：在实验中，设置了多个参数以控制LLMs生成的查询和标签的多样性，并采用了特定的损失函数来优化生成过程。此外，使用线性混合效应模型来量化偏差的影响，确保分析的严谨性。

## 📊 实验亮点

实验结果表明，合成测试集合中的偏差对绝对系统性能评估的影响显著，尤其在计算性能时，偏差可能导致误导性结果。然而，在比较不同系统的相对性能时，偏差的影响相对较小。这一发现为合成数据在IR系统评估中的应用提供了重要的实证支持。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索系统的评估、合成数据生成技术的优化以及相关性判断的自动化。通过提高合成测试集合的可靠性，研究成果可以帮助开发更高效的IR系统，降低评估成本，提升用户体验。未来，随着合成数据技术的进步，可能会在更多领域得到应用，如推荐系统和自然语言处理等。

## 📄 摘要（原文）

> Test collections are crucial for evaluating Information Retrieval (IR) systems. Creating a diverse set of user queries for these collections can be challenging, and obtaining relevance judgments, which indicate how well retrieved documents match a query, is often costly and resource-intensive. Recently, generating synthetic datasets using Large Language Models (LLMs) has gained attention in various applications. While previous work has used LLMs to generate synthetic queries or documents to improve ranking models, using LLMs to create synthetic test collections is still relatively unexplored. Previous work~\cite{rahmani2024synthetic} showed that synthetic test collections have the potential to be used for system evaluation, however, more analysis is needed to validate this claim. In this paper, we thoroughly investigate the reliability of synthetic test collections constructed using LLMs, where LLMs are used to generate synthetic queries, labels, or both. In particular, we examine the potential biases that might occur when such test collections are used for evaluation. We first empirically show the presence of such bias in evaluation results and analyse the effects it might have on system evaluation. We further validate the presence of such bias using a linear mixed-effects model. Our analysis shows that while the effect of bias present in evaluation results obtained using synthetic test collections could be significant, for e.g.~computing absolute system performance, its effect may not be as significant in comparing relative system performance. Codes and data are available at: https://github.com/rahmanidashti/BiasSyntheticData.

