---
layout: default
title: Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting
---

# Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14288" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14288v1</a>
  <a href="https://arxiv.org/pdf/2512.14288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14288v1" onclick="toggleFavorite(this, '2512.14288v1', 'Leveraging LLMs for Collaborative Ontology Engineering in Parkinson Disease Monitoring and Alerting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Bouchouras, Dimitrios Doumanas, Andreas Soularidis, Konstantinos Kotis, George A. Vouros

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**利用大型语言模型进行帕金森病监测和预警的协同本体工程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `本体工程` `大型语言模型` `帕金森病` `人机协作` `知识图谱` `医疗健康` `自动化本体构建`

## 📋 核心要点

1. 现有本体工程方法在处理复杂领域（如帕金森病）时，面临本体构建不全面、准确性不足的挑战。
2. 论文提出人机协作的本体工程方法，结合LLM的生成能力和人类专家的知识，迭代优化本体。
3. 实验表明，人机协作方法（X-HCOME和SimX-HCOME+）显著提高了本体的全面性和准确性，接近专家构建的本体。

## 📝 摘要（中文）

本文探讨了将大型语言模型（LLM）集成到帕金森病（PD）监测和预警本体的工程中，通过四种关键方法：One Shot（OS）提示技术、Chain of Thought（CoT）提示、X-HCOME 和 SimX-HCOME+。主要目标是确定 LLM 是否能够独立创建全面的本体，如果不能，人机协作是否能够实现这一目标。因此，本文评估了 LLM 在自动化本体开发中的有效性，以及通过人机协作实现的增强。

## 🔬 方法详解

**问题定义**：论文旨在解决帕金森病（PD）监测和预警领域本体构建的问题。现有本体构建方法，尤其是完全依赖人工的方法，耗时且容易出错，难以保证本体的全面性和准确性。而完全依赖LLM的方法，虽然可以自动化生成本体，但往往缺乏领域知识和常识，导致生成的本体不完整或不准确。

**核心思路**：论文的核心思路是结合人类专家和LLM的优势，通过人机协作的方式进行本体工程。LLM负责生成初始本体和提供建议，人类专家负责审核、修正和补充LLM的输出，从而迭代优化本体，最终得到高质量的PD监测和预警本体。

**技术框架**：论文提出了两种人机协作的本体工程方法：X-HCOME和SimX-HCOME+。X-HCOME是一种混合方法，人类专家和LLM共同参与本体构建过程。SimX-HCOME+则强调持续的人工监督和迭代改进，人类专家在整个过程中对LLM的输出进行评估和修正。两种方法都包含以下主要阶段：1) LLM生成初始本体；2) 人类专家审核和修正；3) 基于修正后的本体，LLM进行迭代优化；4) 重复步骤2和3，直到本体达到满意的质量。

**关键创新**：论文的关键创新在于提出了人机协作的本体工程框架，并验证了其在PD监测和预警领域的有效性。与完全依赖人工或LLM的方法相比，该框架能够更好地平衡效率和质量，生成更全面、更准确的本体。此外，SimX-HCOME+方法强调持续的人工监督和迭代改进，进一步提高了本体的质量。

**关键设计**：论文使用了One Shot和Chain of Thought提示技术来引导LLM生成初始本体。在人机协作过程中，人类专家使用本体编辑工具（如Protégé）对LLM的输出进行审核和修正。论文没有明确说明具体的参数设置、损失函数或网络结构，因为重点在于人机协作的流程和方法，而不是LLM的具体实现。

## 📊 实验亮点

实验结果表明，X-HCOME和SimX-HCOME+方法显著提高了本体的全面性和准确性，生成的本体与专家构建的本体非常相似。这表明人机协作在本体工程中具有巨大的潜力，可以有效利用LLM的生成能力和人类专家的领域知识。

## 🎯 应用场景

该研究成果可应用于医疗健康领域，特别是帕金森病等慢性疾病的监测和预警。构建的本体可以作为知识库，支持智能诊断、个性化治疗方案推荐和患者管理。此外，该研究提出的人机协作本体工程方法，可以推广到其他复杂领域的知识图谱构建，提高知识工程的效率和质量。

## 📄 摘要（原文）

> This paper explores the integration of Large Language Models (LLMs) in the engineering of a Parkinson's Disease (PD) monitoring and alerting ontology through four key methodologies: One Shot (OS) prompt techniques, Chain of Thought (CoT) prompts, X-HCOME, and SimX-HCOME+. The primary objective is to determine whether LLMs alone can create comprehensive ontologies and, if not, whether human-LLM collaboration can achieve this goal. Consequently, the paper assesses the effectiveness of LLMs in automated ontology development and the enhancement achieved through human-LLM collaboration.
>   Initial ontology generation was performed using One Shot (OS) and Chain of Thought (CoT) prompts, demonstrating the capability of LLMs to autonomously construct ontologies for PD monitoring and alerting. However, these outputs were not comprehensive and required substantial human refinement to enhance their completeness and accuracy.
>   X-HCOME, a hybrid ontology engineering approach that combines human expertise with LLM capabilities, showed significant improvements in ontology comprehensiveness. This methodology resulted in ontologies that are very similar to those constructed by experts.
>   Further experimentation with SimX-HCOME+, another hybrid methodology emphasizing continuous human supervision and iterative refinement, highlighted the importance of ongoing human involvement. This approach led to the creation of more comprehensive and accurate ontologies.
>   Overall, the paper underscores the potential of human-LLM collaboration in advancing ontology engineering, particularly in complex domains like PD. The results suggest promising directions for future research, including the development of specialized GPT models for ontology construction.

