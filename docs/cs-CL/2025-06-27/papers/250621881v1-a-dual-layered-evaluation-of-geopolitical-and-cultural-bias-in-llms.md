---
layout: default
title: A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs
---

# A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21881" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21881v1</a>
  <a href="https://arxiv.org/pdf/2506.21881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21881v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21881v1', 'A Dual-Layered Evaluation of Geopolitical and Cultural Bias in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sean Kim, Hyuhng Joon Kim

**分类**: cs.CL

**发布日期**: 2025-06-27

**备注**: This paper is accepted to ACL Student Research Workshop (SRW) 2025

---

## 💡 一句话要点

**提出双层评估框架以分析LLMs中的地缘政治与文化偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `偏见分析` `多语言评估` `地缘政治` `文化敏感性` `数据集构建` `模型训练`

## 📋 核心要点

1. 当前大型语言模型在多语言和文化背景下的表现尚未得到充分理解，尤其是在事实与争议问题上。
2. 本文提出了一个双层评估框架，分别针对模型偏见和推理偏见进行分析，以揭示LLMs的行为。
3. 实验结果表明，模型在事实问题上保持一致性，但在地缘政治敏感问题上则受到训练背景和查询语言的影响。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在多样化语言和文化背景中的广泛应用，理解其在事实和争议场景中的表现至关重要，尤其是当其输出可能影响公众舆论或强化主导叙事时。本文定义了LLMs中的两种偏见：模型偏见（源于模型训练）和推理偏见（由查询语言引起），通过两阶段评估进行分析。第一阶段评估LLMs在存在单一可验证答案的事实问题上的一致性，第二阶段则探讨地缘政治敏感争议，响应可能反映文化嵌入或意识形态倾向。我们构建了一个手动策划的数据集，涵盖四种语言和问题类型的事实与争议问答。结果显示，第一阶段表现出查询语言引起的对齐，而第二阶段则反映模型训练背景与查询语言之间的相互作用。本文为评估LLM在中立和敏感主题上的表现提供了结构化框架，为未来的LLM部署和多语言环境中的文化敏感评估实践提供了见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多语言和文化背景下的偏见问题，现有方法未能有效区分模型偏见与推理偏见的影响。

**核心思路**：通过双阶段评估框架，分别分析模型在事实问题和地缘政治敏感问题上的表现，揭示偏见来源。

**技术框架**：整体评估分为两个阶段：第一阶段针对事实问题进行一致性评估，第二阶段探讨地缘政治争议，使用手动策划的数据集进行分析。

**关键创新**：提出了模型偏见与推理偏见的明确区分，构建了多语言数据集，提供了系统的评估框架，填补了现有研究的空白。

**关键设计**：在数据集构建中，涵盖了四种语言和多种问题类型，确保评估的全面性和代表性。

## 📊 实验亮点

实验结果显示，在第一阶段的事实问题评估中，模型在不同查询语言上保持了一致性，而在第二阶段的地缘政治敏感问题中，模型的响应则受到训练背景和查询语言的显著影响。这表明模型的行为在不同场景下存在明显差异，为后续研究提供了重要依据。

## 🎯 应用场景

该研究为大型语言模型在多语言和文化背景下的应用提供了重要的评估框架，能够帮助开发者识别和减轻模型输出中的偏见，促进更公平和透明的AI系统。未来，研究成果可广泛应用于社交媒体、新闻生成、教育等领域，提升公众对AI生成内容的信任度。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly deployed across diverse linguistic and cultural contexts, understanding their behavior in both factual and disputable scenarios is essential, especially when their outputs may shape public opinion or reinforce dominant narratives. In this paper, we define two types of bias in LLMs: model bias (bias stemming from model training) and inference bias (bias induced by the language of the query), through a two-phase evaluation. Phase 1 evaluates LLMs on factual questions where a single verifiable answer exists, assessing whether models maintain consistency across different query languages. Phase 2 expands the scope by probing geopolitically sensitive disputes, where responses may reflect culturally embedded or ideologically aligned perspectives. We construct a manually curated dataset spanning both factual and disputable QA, across four languages and question types. The results show that Phase 1 exhibits query language induced alignment, while Phase 2 reflects an interplay between the model's training context and query language. This paper offers a structured framework for evaluating LLM behavior across neutral and sensitive topics, providing insights for future LLM deployment and culturally aware evaluation practices in multilingual contexts.

