---
layout: default
title: Chain or tree? Re-evaluating complex reasoning from the perspective of a matrix of thought
---

# Chain or tree? Re-evaluating complex reasoning from the perspective of a matrix of thought

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03918" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03918v2</a>
  <a href="https://arxiv.org/pdf/2509.03918.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03918v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03918v2', 'Chain or tree? Re-evaluating complex reasoning from the perspective of a matrix of thought')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengxiao Tang, Yufeng Li, Zongzong Wu, Ming Zhao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04 (更新: 2025-09-26)

**🔗 代码/项目**: [GITHUB](https://github.com/lyfiter/mtqa)

---

## 💡 一句话要点

**提出矩阵思维（MoT）框架，提升LLM在复杂推理任务中的效率与准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `复杂推理` `矩阵思维` `知识图谱` `检索增强生成`

## 📋 核心要点

1. 现有思维链和思维树方法在复杂推理中存在冗余和路径单一问题，且易受检索到的错误知识误导。
2. 提出矩阵思维（MoT）框架，通过列-单元通信机制进行多策略深度思考，并结合事实纠正机制。
3. 实验结果表明，MoT在24点游戏、问题回答和命题写作任务中优于现有方法，推理时间显著降低。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理复杂和抽象任务时，由于推理能力不足，准确性会显著下降。思维链（CoT）和思维树（ToT）等思维结构旨在增强LLMs的推理能力，但存在固有缺陷，如树结构中同一层内的冗余和链结构中路径的单一性。一些研究利用检索增强生成（RAG）方法来增强CoT和ToT，以减轻LLMs中的幻觉，但思维结构的基本缺点仍然存在。此外，在处理多实体和多跳信息时，检索到的验证知识通常包含大量碎片化、表面化甚至错误的数据，误导LLMs的推理过程。为了解决这些问题，我们提出了一种新颖而高效的LLMs思维结构——矩阵思维（MoT）。MoT通过“列-单元通信”机制在水平和垂直维度上探索问题，使LLMs能够积极参与多策略和深度思考，同时减少列单元内思维节点的冗余，从而增强LLMs的推理能力。此外，通过事实纠正机制，它利用RAG检索到的知识图谱三元组和原始文本来构建知识单元并纠正错误答案。为了验证该方法的有效性，我们在24点游戏、问题回答评估和命题写作三个任务中进行了大量实验。结果表明，我们的框架优于最先进的方法，推理时间仅为基线方法的14.4％，证明了其效率和准确性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在复杂推理任务中准确性下降的问题。现有方法，如思维链（CoT）和思维树（ToT），存在冗余、路径单一以及易受错误检索知识误导等痛点。这些问题限制了LLM在需要多步推理和外部知识验证的任务中的表现。

**核心思路**：论文的核心思路是构建一个矩阵式的思维结构，允许LLM在水平和垂直方向上探索问题。通过“列-单元通信”机制，鼓励LLM进行多策略和深度思考，同时减少冗余。此外，利用检索增强生成（RAG）和事实纠正机制，提高知识的准确性，避免LLM受到错误信息的误导。

**技术框架**：MoT框架主要包含以下几个阶段：1) 问题分解：将复杂问题分解为多个子问题。2) 矩阵构建：构建一个矩阵，其中每一列代表一种推理策略，每一行代表推理的中间步骤。3) 列-单元通信：LLM在矩阵的单元格中进行推理，并通过列之间的通信共享信息。4) 知识检索与事实纠正：利用RAG检索相关知识，并使用事实纠正机制纠正错误信息。5) 答案生成：基于矩阵中的推理结果生成最终答案。

**关键创新**：MoT的关键创新在于其矩阵式的思维结构和列-单元通信机制。与传统的链式或树状结构相比，MoT能够更全面地探索问题空间，并减少冗余。此外，事实纠正机制能够有效提高知识的准确性，避免LLM受到错误信息的误导。

**关键设计**：MoT框架中，列的数量代表推理策略的多样性，行的数量代表推理的深度。列-单元通信机制的具体实现方式未知，可能涉及注意力机制或消息传递机制。事实纠正机制的设计细节也未知，可能涉及知识图谱推理或文本蕴含识别等技术。

## 📊 实验亮点

实验结果表明，MoT框架在24点游戏、问题回答评估和命题写作三个任务中均优于现有方法。尤其是在推理时间方面，MoT仅为基线方法的14.4%，显著提高了推理效率。这表明MoT在保证准确性的同时，也具有很高的实用价值。

## 🎯 应用场景

该研究成果可应用于需要复杂推理和知识验证的领域，如智能问答系统、自动命题生成、游戏AI等。通过提高LLM的推理能力和知识准确性，可以提升这些应用的用户体验和性能，并有望在教育、科研等领域发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) face significant accuracy degradation due to insufficient reasoning ability when dealing with complex and abstract tasks. Thought structures such as Chain of Thought (CoT) and Tree of Thought (ToT) focus on enhancing the reasoning capability of LLMs. However, they suffer from inherent drawbacks such as redundancy within the same layer of the tree structure and the singularity of the paths in the chain structure. Some studies have utilized Retrieval-Augmented Generation (RAG) methods to enhance CoT and ToT in mitigating hallucinations in LLMs, yet the fundamental shortcomings of the thought structures still persist. Furthermore, when dealing with multi-entity and multi-hop information, the retrieved verification knowledge often contains large amounts of fragmented, superficial, or even erroneous data, misleading the reasoning process of LLMs. To address these issues, we propose the Matrix of Thought (MoT), a novel and efficient thought structure for LLMs. MoT explores problems in both horizontal and vertical dimensions through a "column-cell communication" mechanism, enabling LLMs to actively engage in multi-strategy and deep thinking while reducing redundancy in the thought nodes within the column cells, thereby enhancing the reasoning capability of LLMs. Additionally, through a fact-correction mechanism, it leverages the knowledge graph triples retrieved by RAG and the original text to construct knowledge units and correct erroneous answers. To validate the effectiveness of this method, we conducted extensive experiments in three tasks: 24-point game, question answering evaluation, and proposition writing.The results demonstrate that our framework outperforms state-of-the-art methods, with reasoning time only 14.4\% of that of the baseline method, proving its efficiency and accuracy. The code for framework is available at https://github.com/lyfiter/mtqa.

