---
layout: default
title: A Stepwise-Enhanced Reasoning Framework for Large Language Models Based on External Subgraph Generation
---

# A Stepwise-Enhanced Reasoning Framework for Large Language Models Based on External Subgraph Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23356" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23356v1</a>
  <a href="https://arxiv.org/pdf/2512.23356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23356v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23356v1', 'A Stepwise-Enhanced Reasoning Framework for Large Language Models Based on External Subgraph Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Zhang, Yang Cao, Baoxing Wu, Xinyi Chen, Kai Song, Siying Li

**分类**: cs.CL

**发布日期**: 2025-12-29

---

## 💡 一句话要点

**提出基于外部子图生成的逐步增强推理框架SGR，提升大语言模型在复杂推理任务中的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `知识图谱` `推理增强` `外部知识` `子图生成`

## 📋 核心要点

1. 现有大语言模型在复杂推理任务中易受噪声信息干扰，导致错误预测或与事实不符的输出。
2. SGR框架通过动态构建外部知识子图，引导模型在结构化知识上进行逐步推理，减少噪声影响。
3. 实验结果表明，SGR在多个基准数据集上优于现有方法，有效提升了大语言模型的推理能力。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在机器翻译、文本生成和问答等自然语言处理任务中取得了显著成果。然而，当应用扩展到日益复杂的场景时，LLMs在需要深度推理和逻辑推断的任务中仍然面临挑战。特别是在大规模文本语料库上训练的模型，在生成过程中可能会包含噪声或不相关的信息，从而导致不正确的预测或与事实知识不一致的输出。为了解决这一局限性，我们提出了一种基于外部子图生成的LLMs逐步推理增强框架，称为SGR。该框架动态地从外部知识库构建与查询相关的子图，并利用其语义结构来指导推理过程。通过在结构化子图上逐步执行推理，SGR减少了噪声信息的影响，提高了推理准确性。具体来说，该框架首先生成一个针对输入查询量身定制的外部子图，然后引导模型在子图的基础上进行多步推理，最后整合多个推理路径以产生最终答案。在多个基准数据集上的实验结果表明，SGR始终优于强大的基线模型，表明其在增强LLMs推理能力方面的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在复杂推理任务中，由于受到训练数据中噪声或不相关信息的影响，导致推理准确性下降的问题。现有方法难以有效利用外部知识，容易产生与事实知识不一致的输出。

**核心思路**：论文的核心思路是利用外部知识库构建与输入查询相关的子图，并引导LLM在这些结构化的子图上进行逐步推理。通过限制推理过程在相关知识范围内，减少噪声信息的干扰，从而提高推理的准确性和可靠性。

**技术框架**：SGR框架包含三个主要阶段：1) **子图生成**：根据输入查询，从外部知识库中提取相关的子图。2) **多步推理**：引导LLM在生成的子图上进行多步推理，每一步推理都基于子图的结构化信息。3) **答案整合**：整合多条推理路径的结果，生成最终答案。

**关键创新**：SGR的关键创新在于动态构建与查询相关的外部子图，并将LLM的推理过程限制在这些子图的范围内。这种方法有效地利用了外部知识，并减少了噪声信息的干扰，从而提高了推理的准确性。与现有方法相比，SGR能够更好地利用外部知识，并避免生成与事实知识不一致的输出。

**关键设计**：子图生成过程依赖于知识库的结构和查询的语义信息，具体实现可能涉及实体链接、关系抽取等技术。多步推理过程可以通过提示工程（Prompt Engineering）引导LLM逐步探索子图中的信息。答案整合可以采用投票、加权平均等方法，根据不同推理路径的可靠性进行整合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23356v1/Fig1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23356v1/Fig2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23356v1/Fig3.png" alt="img_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SGR框架在多个基准数据集上 consistently 优于现有的强大基线模型，证明了其在增强LLMs推理能力方面的有效性。具体的性能提升数据在摘要中未给出，但强调了SGR在多个数据集上的一致性表现优越。

## 🎯 应用场景

该研究成果可应用于问答系统、知识图谱推理、智能助手等领域。通过提升大语言模型的推理能力，可以提高这些应用在复杂场景下的准确性和可靠性，例如在医疗诊断、金融分析等需要精确推理的领域具有重要价值。未来，该方法可以进一步扩展到其他需要利用外部知识进行推理的任务中。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved strong performance across a wide range of natural language processing tasks in recent years, including machine translation, text generation, and question answering. As their applications extend to increasingly complex scenarios, however, LLMs continue to face challenges in tasks that require deep reasoning and logical inference. In particular, models trained on large scale textual corpora may incorporate noisy or irrelevant information during generation, which can lead to incorrect predictions or outputs that are inconsistent with factual knowledge. To address this limitation, we propose a stepwise reasoning enhancement framework for LLMs based on external subgraph generation, termed SGR. The proposed framework dynamically constructs query relevant subgraphs from external knowledge bases and leverages their semantic structure to guide the reasoning process. By performing reasoning in a step by step manner over structured subgraphs, SGR reduces the influence of noisy information and improves reasoning accuracy. Specifically, the framework first generates an external subgraph tailored to the input query, then guides the model to conduct multi step reasoning grounded in the subgraph, and finally integrates multiple reasoning paths to produce the final answer. Experimental results on multiple benchmark datasets demonstrate that SGR consistently outperforms strong baselines, indicating its effectiveness in enhancing the reasoning capabilities of LLMs.

