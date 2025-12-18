---
layout: default
title: Geometric Uncertainty for Detecting and Correcting Hallucinations in LLMs
---

# Geometric Uncertainty for Detecting and Correcting Hallucinations in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13813" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13813v2</a>
  <a href="https://arxiv.org/pdf/2509.13813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13813v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13813v2', 'Geometric Uncertainty for Detecting and Correcting Hallucinations in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Edward Phillips, Sean Wu, Soheila Molaei, Danielle Belgrave, Anshul Thakur, David Clifton

**分类**: cs.CL

**发布日期**: 2025-09-17 (更新: 2025-12-02)

**备注**: Revision. Clarified positioning as a unified geometric framework for global and local uncertainty in LLMs. Added baselines (Degree, Eccentricity) and expanded comparison to related methods. Included ablations (PCA dimension, number of archetypes, number of samples) and complexity analysis. Extended discussion of medical QA results and model-specific behaviour

---

## 💡 一句话要点

**提出基于几何不确定性的方法，用于检测和纠正大语言模型中的幻觉问题。**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `幻觉检测` `不确定性量化` `几何分析` `原型分析`

## 📋 核心要点

1. 现有幻觉检测方法依赖启发式规则或图论近似，缺乏统一的几何解释，限制了其性能和泛化能力。
2. 该论文提出了一种基于几何不确定性的框架，通过分析响应的原型，量化全局和局部的不确定性，从而检测幻觉。
3. 实验表明，该框架在短问答和医疗数据集上表现优于现有方法，尤其在医疗领域，能有效降低幻觉带来的风险。

## 📝 摘要（中文）

大型语言模型在各种任务中表现出令人印象深刻的结果，但仍然存在幻觉问题，即生成在语言上看似合理但不正确的答案。不确定性量化已被提议作为幻觉检测的一种策略，需要估计全局不确定性（归因于一批响应）和局部不确定性（归因于单个响应）。虽然最近的黑盒方法已经显示出一些成功，但它们通常依赖于不相交的启发式方法或缺乏统一几何解释的图论近似。本文提出了一种几何框架来解决这个问题，该框架基于仅通过黑盒模型访问采样的批次响应的原型分析。在全局层面，我们提出了几何体积，它测量从响应嵌入导出的原型凸包体积。在局部层面，我们提出了几何怀疑，它利用响应和这些原型之间的空间关系来对可靠性进行排序，从而通过优先选择响应来减少幻觉。与依赖于离散成对比较的先前方法不同，我们的方法提供了连续的语义边界点，这些边界点对于将可靠性归因于单个响应很有用。实验表明，我们的框架在简短问答数据集上表现与先前方法相当或更好，并且在医疗数据集中取得了优异的结果，在医疗数据集中，幻觉会带来特别严重的风险。我们还通过证明凸包体积和熵之间的联系来提供理论依据。

## 🔬 方法详解

**问题定义**：大语言模型（LLM）的幻觉问题，即生成看似合理但错误的答案，是阻碍其可靠应用的关键挑战。现有方法，如基于启发式规则或图论近似的方法，缺乏统一的几何解释，难以准确量化响应的不确定性，导致幻觉检测效果不佳。

**核心思路**：该论文的核心思路是将LLM的响应视为高维空间中的点，并利用几何方法分析这些点的分布，从而量化响应的不确定性。通过计算响应集合的凸包体积（Geometric Volume）来衡量全局不确定性，并利用响应与原型之间的空间关系（Geometric Suspicion）来评估局部不确定性。

**技术框架**：该框架主要包含以下几个阶段：1) **响应采样**：使用黑盒LLM对同一问题生成多个响应。2) **嵌入表示**：将每个响应转换为高维向量嵌入。3) **原型分析**：使用原型分析方法从响应嵌入中提取代表性的原型。4) **不确定性量化**：计算响应集合的凸包体积（Geometric Volume）作为全局不确定性，并计算每个响应与原型之间的距离作为局部不确定性（Geometric Suspicion）。5) **幻觉检测与纠正**：根据全局和局部不确定性，检测并纠正LLM的幻觉。

**关键创新**：该方法最重要的创新在于将几何不确定性引入LLM的幻觉检测。与现有方法相比，该方法提供了一种统一的几何解释，能够更准确地量化响应的不确定性。此外，该方法利用原型分析，能够有效地提取响应集合的代表性特征，从而提高幻觉检测的准确性。该方法通过连续的语义边界点来评估单个响应的可靠性，避免了离散的成对比较。

**关键设计**：该方法的关键设计包括：1) 使用原型分析（Archetypal Analysis）提取响应集合的代表性原型。2) 定义Geometric Volume作为全局不确定性度量，计算响应嵌入凸包的体积。3) 定义Geometric Suspicion作为局部不确定性度量，衡量响应与原型之间的空间关系。4) 利用Geometric Suspicion对响应进行排序，优先选择更可靠的响应以减少幻觉。

## 📊 实验亮点

实验结果表明，该框架在短问答数据集上表现与现有方法相当或更好，在医疗数据集上取得了显著的性能提升。尤其是在医疗数据集上，该方法能够更有效地检测和纠正LLM的幻觉，从而降低医疗风险。该研究还提供了凸包体积和熵之间的理论联系，为该方法的有效性提供了理论支持。

## 🎯 应用场景

该研究成果可广泛应用于需要高可靠性的大语言模型应用场景，例如医疗诊断、金融分析、法律咨询等。通过降低幻觉，可以提高LLM在这些领域的应用价值，并减少因错误信息带来的风险。未来，该方法可以扩展到其他类型的生成模型，提高生成内容的质量和可靠性。

## 📄 摘要（原文）

> Large language models demonstrate impressive results across diverse tasks but are still known to hallucinate, generating linguistically plausible but incorrect answers to questions. Uncertainty quantification has been proposed as a strategy for hallucination detection, requiring estimates for both global uncertainty (attributed to a batch of responses) and local uncertainty (attributed to individual responses). While recent black-box approaches have shown some success, they often rely on disjoint heuristics or graph-theoretic approximations that lack a unified geometric interpretation. We introduce a geometric framework to address this, based on archetypal analysis of batches of responses sampled with only black-box model access. At the global level, we propose Geometric Volume, which measures the convex hull volume of archetypes derived from response embeddings. At the local level, we propose Geometric Suspicion, which leverages the spatial relationship between responses and these archetypes to rank reliability, enabling hallucination reduction through preferential response selection. Unlike prior methods that rely on discrete pairwise comparisons, our approach provides continuous semantic boundary points which have utility for attributing reliability to individual responses. Experiments show that our framework performs comparably to or better than prior methods on short form question-answering datasets, and achieves superior results on medical datasets where hallucinations carry particularly critical risks. We also provide theoretical justification by proving a link between convex hull volume and entropy.

