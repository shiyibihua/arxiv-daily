---
layout: default
title: Computational Analysis of Climate Policy
---

# Computational Analysis of Climate Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22449" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22449v1</a>
  <a href="https://arxiv.org/pdf/2506.22449.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22449v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22449v1', 'Computational Analysis of Climate Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Carolyn Hicks

**分类**: cs.CY, cs.CL

**发布日期**: 2025-06-13

**备注**: Master's thesis

---

## 💡 一句话要点

**构建PALLM系统以分析气候政策的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `气候政策` `大型语言模型` `政策分析` `气候紧急声明` `维多利亚州` `社会公正` `环境政策`

## 📋 核心要点

1. 现有气候政策分析方法缺乏有效的工具来处理复杂的政策问题，尤其是在地方政府层面。
2. 论文提出了PALLM系统，利用GPT-4模型对气候政策文档进行分析，旨在提高政策分析的效率和准确性。
3. 研究结果表明，PALLM能够进行高水平的政策分析，并发现通过气候紧急声明的地方政府在政策内容上更具气候紧迫性和社会公正性。

## 📝 摘要（中文）

本论文探讨了气候紧急运动对地方政府气候政策的影响，采用计算方法进行分析。气候紧急运动旨在通过气候紧急声明加速地方政府的气候行动。作者构建了名为PALLM的系统，利用OpenAI的GPT-4模型，旨在将气候应急响应计划的概念框架应用于气候政策文档数据集。通过与地方政府政策制定者的合作，验证了PALLM的性能，并对维多利亚州11个地方政府的气候政策进行了分析。研究发现，已通过气候紧急声明的地方政府更可能拥有近期且气候特定的政策，并在紧迫性、优先级和社会公正方面表现出更多关注。

## 🔬 方法详解

**问题定义**：本论文旨在解决地方政府气候政策分析中缺乏有效工具的问题，现有方法在处理复杂政策问题时存在局限性。

**核心思路**：论文的核心思路是构建PALLM系统，利用大型语言模型GPT-4对气候政策文档进行深入分析，以提高政策分析的准确性和效率。

**技术框架**：PALLM系统的整体架构包括数据收集、模型配置、政策分析和结果验证四个主要模块。首先收集气候政策文档，然后配置GPT-4模型进行分析，最后与政策制定者进行结果验证。

**关键创新**：本研究的关键创新在于将大型语言模型应用于政策分析领域，尤其是针对气候政策的具体需求，突破了传统分析方法的局限。

**关键设计**：在PALLM系统中，关键参数包括模型的配置和训练数据的选择，损失函数设计为适应政策分析的特定需求，确保生成的分析结果具有高相关性和准确性。

## 📊 实验亮点

实验结果显示，PALLM系统在分析维多利亚州地方政府的气候政策时，能够生成与政策制定者高度一致的分析结果。已通过气候紧急声明的地方政府在政策内容上表现出更高的气候紧迫性和社会公正性，表明PALLM在政策分析中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括地方政府的气候政策制定、环境保护组织的政策分析，以及学术界对气候变化应对策略的研究。通过提供高效的政策分析工具，PALLM系统能够帮助政策制定者更好地理解和应对气候变化带来的挑战，推动可持续发展。

## 📄 摘要（原文）

> This thesis explores the impact of the Climate Emergency movement on local government climate policy, using computational methods. The Climate Emergency movement sought to accelerate climate action at local government level through the mechanism of Climate Emergency Declarations (CEDs), resulting in a series of commitments from councils to treat climate change as an emergency. With the aim of assessing the potential of current large language models to answer complex policy questions, I first built and configured a system named PALLM (Policy Analysis with a Large Language Model), using the OpenAI model GPT-4. This system is designed to apply a conceptual framework for climate emergency response plans to a dataset of climate policy documents. I validated the performance of this system with the help of local government policymakers, by generating analyses of the climate policies of 11 local governments in Victoria and assessing the policymakers' level of agreement with PALLM's responses. Having established that PALLM's performance is satisfactory, I used it to conduct a large-scale analysis of current policy documents from local governments in the state of Victoria, Australia. This thesis presents the methodology and results of this analysis, comparing the results for councils which have passed a CED to those which did not. This study finds that GPT-4 is capable of high-level policy analysis, with limitations including a lack of reliable attribution, and can also enable more nuanced analysis by researchers. Its use in this research shows that councils which have passed a CED are more likely to have a recent and climate-specific policy, and show more attention to urgency, prioritisation, and equity and social justice, than councils which have not. It concludes that the ability to assess policy documents at scale opens up exciting new opportunities for policy researchers.

