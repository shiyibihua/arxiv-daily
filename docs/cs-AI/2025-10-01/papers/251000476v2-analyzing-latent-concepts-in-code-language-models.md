---
layout: default
title: Analyzing Latent Concepts in Code Language Models
---

# Analyzing Latent Concepts in Code Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00476" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00476v2</a>
  <a href="https://arxiv.org/pdf/2510.00476.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00476v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00476v2', 'Analyzing Latent Concepts in Code Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arushi Sharma, Vedant Pungliya, Christopher J. Quinn, Ali Jannesari

**分类**: cs.SE, cs.AI, cs.LG

**发布日期**: 2025-10-01 (更新: 2025-10-02)

---

## 💡 一句话要点

**提出代码概念分析(CoCoA)框架，用于理解代码语言模型中的潜在概念。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码语言模型` `可解释性` `概念分析` `后验解释` `聚类` `静态分析` `提示工程`

## 📋 核心要点

1. 代码语言模型的内部机制难以解释，阻碍了其在需要高透明度和鲁棒性的场景应用。
2. 提出CoCoA框架，通过聚类token嵌入来发现模型中的潜在概念，并进行可解释性分析。
3. 实验表明CoCoA发现的概念具有稳定性，且与模型微调过程一致，提升了解释性。

## 📝 摘要（中文）

理解在代码上训练的大型语言模型的内部行为仍然是一个关键挑战，尤其是在需要信任、透明度和语义鲁棒性的应用中。我们提出了代码概念分析（CoCoA）：一个全局的后验可解释性框架，通过将上下文相关的token嵌入聚类成人类可解释的概念组，来揭示代码语言模型表示空间中涌现的词汇、句法和语义结构。我们提出了一个混合标注流程，结合了基于静态分析工具的句法对齐和prompt工程化的大型语言模型（LLM），从而能够跨抽象级别对潜在概念进行可扩展的标注。我们分析了概念在不同层和三个微调任务中的分布。涌现的概念聚类可以帮助识别意想不到的潜在交互，并用于识别模型学习表示中的趋势和偏差。我们进一步将LCA与局部归因方法集成，以产生基于概念的解释，从而提高token级别显著性的连贯性和可解释性。跨多个模型和任务的经验评估表明，LCA发现的概念在语义保持扰动下保持稳定（平均聚类敏感度指数，CSI = 0.288），并且随着微调可预测地演变。在一项关于编程语言分类任务的用户研究中，与使用积分梯度的token级别归因相比，概念增强的解释消除了token角色的歧义，并将以人为中心的可解释性提高了37个百分点。

## 🔬 方法详解

**问题定义**：现有代码语言模型的可解释性不足，难以理解模型内部如何表示和处理代码的语义信息。这限制了模型在安全关键领域的应用，因为用户无法信任模型的决策过程。现有方法通常关注于token级别的归因，缺乏对更高层次抽象概念的理解。

**核心思路**：CoCoA的核心思路是通过将代码语言模型中上下文相关的token嵌入进行聚类，从而发现模型学习到的潜在概念。这些概念可以被人类理解和解释，从而提高模型的可解释性。通过分析这些概念在不同层和不同任务中的分布，可以深入了解模型的内部工作机制。

**技术框架**：CoCoA框架主要包含以下几个阶段：1) 获取上下文相关的token嵌入：使用代码语言模型对代码进行编码，得到每个token的上下文嵌入表示。2) 概念聚类：使用聚类算法（如k-means）将token嵌入聚类成不同的概念组。3) 概念标注：使用混合标注流程，结合静态分析工具和prompt工程化的LLM，对每个概念组进行语义标注。4) 概念分析：分析概念在不同层和不同任务中的分布，以及概念之间的关系。5) 概念增强的解释：将LCA与局部归因方法集成，以产生基于概念的解释。

**关键创新**：CoCoA的关键创新在于提出了一个全局的后验可解释性框架，能够自动发现代码语言模型中的潜在概念，并将其与人类可理解的语义信息对齐。该框架结合了静态分析工具和prompt工程化的LLM，实现了可扩展的概念标注。此外，CoCoA还提供了一种将概念信息融入到局部归因方法中的机制，从而提高了解释的连贯性和可解释性。

**关键设计**：CoCoA使用Transformer模型作为代码语言模型的基础架构。在概念聚类阶段，可以使用不同的聚类算法，例如k-means或层次聚类。在概念标注阶段，使用静态分析工具提取代码的句法信息，并使用prompt工程化的LLM生成概念的语义描述。聚类敏感度指数（CSI）用于评估概念的稳定性。

## 📊 实验亮点

实验结果表明，CoCoA发现的概念在语义保持扰动下具有较高的稳定性（平均CSI = 0.288），并且随着模型微调能够可预测地演变。在一项编程语言分类任务的用户研究中，概念增强的解释将以人为中心的可解释性提高了37个百分点，显著优于传统的token级别归因方法。

## 🎯 应用场景

CoCoA可应用于代码缺陷检测、代码生成、代码翻译等领域。通过理解模型内部的概念表示，可以提高模型在这些任务中的性能和可靠性。此外，CoCoA还可以用于评估代码语言模型的安全性，例如识别模型是否存在对特定类型代码的偏见。

## 📄 摘要（原文）

> Interpreting the internal behavior of large language models trained on code remains a critical challenge, particularly for applications demanding trust, transparency, and semantic robustness. We propose Code Concept Analysis (CoCoA): a global post-hoc interpretability framework that uncovers emergent lexical, syntactic, and semantic structures in a code language model's representation space by clustering contextualized token embeddings into human-interpretable concept groups. We propose a hybrid annotation pipeline that combines static analysis tool-based syntactic alignment with prompt-engineered large language models (LLMs), enabling scalable labeling of latent concepts across abstraction levels. We analyse the distribution of concepts across layers and across three finetuning tasks. Emergent concept clusters can help identify unexpected latent interactions and be used to identify trends and biases within the model's learned representations. We further integrate LCA with local attribution methods to produce concept-grounded explanations, improving the coherence and interpretability of token-level saliency. Empirical evaluations across multiple models and tasks show that LCA discovers concepts that remain stable under semantic-preserving perturbations (average Cluster Sensitivity Index, CSI = 0.288) and evolve predictably with fine-tuning. In a user study on the programming-language classification task, concept-augmented explanations disambiguated token roles and improved human-centric explainability by 37 percentage points compared with token-level attributions using Integrated Gradients.

