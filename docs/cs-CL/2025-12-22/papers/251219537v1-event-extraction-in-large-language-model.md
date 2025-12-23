---
layout: default
title: Event Extraction in Large Language Model
---

# Event Extraction in Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19537" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19537v1</a>
  <a href="https://arxiv.org/pdf/2512.19537.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19537v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19537v1', 'Event Extraction in Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bobo Li, Xudong Han, Jiang Liu, Yuzhe Ding, Liqiang Jing, Zhaoqi Zhang, Jinheng Li, Xinya Du, Fei Li, Meishan Zhang, Min Zhang, Aixin Sun, Philip S. Yu, Hao Fei

**分类**: cs.CL

**发布日期**: 2025-12-22

**备注**: 38 pages, 9 Figures, 5 Tables

---

## 💡 一句话要点

**综述性论文：探讨大语言模型在事件抽取中的应用，并展望未来发展方向。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `事件抽取` `大型语言模型` `认知支架` `知识图谱` `信息抽取` `自然语言处理` `多模态学习`

## 📋 核心要点

1. 现有基于大语言模型的事件抽取方法在弱约束下容易产生幻觉，且难以处理长上下文和跨文档的时间因果关系。
2. 论文提出将事件抽取视为LLM解决方案的认知支架，利用事件模式、结构、链接和存储来增强LLM的可靠性和长期记忆能力。
3. 该综述全面回顾了事件抽取领域的发展历程，并对未来基于LLM的事件抽取系统提出了挑战和发展方向。

## 📝 摘要（中文）

大型语言模型（LLMs）和多模态LLMs正在改变事件抽取（EE）领域：提示和生成通常可以在零样本或少样本设置中产生结构化输出。然而，基于LLM的流程面临部署差距，包括弱约束下的幻觉、长上下文和跨文档中脆弱的时间和因果链接，以及有限的上下文窗口内的长期知识管理。我们认为，EE应该被视为一个系统组件，为以LLM为中心的解决方案提供认知支架。事件模式和槽约束为 grounding 和验证创建接口；以事件为中心的结构充当逐步推理的可控中间表示；事件链接支持基于图的RAG的关系感知检索；事件存储提供超出上下文窗口的可更新的情节和代理记忆。本综述涵盖了文本和多模态环境中的EE，组织了任务和分类，追溯了从基于规则和神经模型到指令驱动和生成框架的方法演变，并总结了公式、解码策略、架构、表示、数据集和评估。我们还回顾了跨语言、低资源和特定领域的设置，并强调了可靠的以事件为中心的系统的开放挑战和未来方向。最后，我们概述了LLM时代的核心开放挑战和未来方向，旨在将EE从静态抽取发展为开放世界系统的结构可靠、代理就绪的感知和记忆层。

## 🔬 方法详解

**问题定义**：事件抽取旨在从文本或多模态数据中识别和提取事件信息，包括事件类型、参与者、时间和地点等。现有方法，特别是基于大型语言模型的方法，虽然在零样本或少样本设置下表现出潜力，但仍存在幻觉问题，难以处理长上下文和跨文档的复杂关系，并且上下文窗口限制了长期知识的管理。

**核心思路**：论文的核心思路是将事件抽取视为一个认知支架，为大型语言模型提供结构化的信息和约束，从而提高其可靠性和推理能力。通过将事件模式和槽约束作为 grounding 和验证的接口，将事件结构作为中间表示，将事件链接用于关系感知检索，以及将事件存储用于长期记忆，可以有效地解决现有方法的不足。

**技术框架**：该综述性论文没有提出具体的模型架构，而是从宏观层面分析了事件抽取在LLM时代的角色。它涵盖了事件抽取的任务和分类，回顾了从基于规则和神经模型到指令驱动和生成框架的方法演变，并总结了公式、解码策略、架构、表示、数据集和评估。此外，还讨论了跨语言、低资源和特定领域的设置。

**关键创新**：该论文的关键创新在于将事件抽取重新定位为LLM的认知支架，强调了事件模式、结构、链接和存储在提高LLM可靠性和长期记忆能力方面的作用。这种观点为未来的事件抽取研究提供了新的方向，即如何将事件抽取与LLM更好地结合，构建更强大的事件感知系统。

**关键设计**：由于是综述性论文，没有具体的参数设置、损失函数或网络结构等技术细节。但是，论文强调了事件模式和槽约束的重要性，可以将其视为一种软约束，用于指导LLM的生成过程，减少幻觉的产生。此外，事件链接和事件存储的设计可以有效地扩展LLM的上下文窗口，使其能够处理更长的文本和更复杂的事件关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19537v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19537v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19537v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该论文是一篇全面的综述，总结了事件抽取领域的发展历程，并深入分析了LLM在事件抽取中的应用。它强调了将事件抽取作为LLM认知支架的重要性，并为未来的研究方向提供了有价值的见解。虽然没有提供具体的性能数据，但其对现有方法的不足和未来发展方向的分析具有重要的指导意义。

## 🎯 应用场景

该研究成果对信息抽取、知识图谱构建、问答系统、智能助手等领域具有重要应用价值。通过构建可靠的事件感知和记忆层，可以提升LLM在开放世界系统中的表现，例如在新闻分析、金融风险评估、医疗诊断等领域。

## 📄 摘要（原文）

> Large language models (LLMs) and multimodal LLMs are changing event extraction (EE): prompting and generation can often produce structured outputs in zero shot or few shot settings. Yet LLM based pipelines face deployment gaps, including hallucinations under weak constraints, fragile temporal and causal linking over long contexts and across documents, and limited long horizon knowledge management within a bounded context window. We argue that EE should be viewed as a system component that provides a cognitive scaffold for LLM centered solutions. Event schemas and slot constraints create interfaces for grounding and verification; event centric structures act as controlled intermediate representations for stepwise reasoning; event links support relation aware retrieval with graph based RAG; and event stores offer updatable episodic and agent memory beyond the context window. This survey covers EE in text and multimodal settings, organizing tasks and taxonomy, tracing method evolution from rule based and neural models to instruction driven and generative frameworks, and summarizing formulations, decoding strategies, architectures, representations, datasets, and evaluation. We also review cross lingual, low resource, and domain specific settings, and highlight open challenges and future directions for reliable event centric systems. Finally, we outline open challenges and future directions that are central to the LLM era, aiming to evolve EE from static extraction into a structurally reliable, agent ready perception and memory layer for open world systems.

