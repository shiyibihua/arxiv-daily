---
layout: default
title: Can Large Language Models (LLMs) Describe Pictures Like Children? A Comparative Corpus Study
---

# Can Large Language Models (LLMs) Describe Pictures Like Children? A Comparative Corpus Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13769" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13769v1</a>
  <a href="https://arxiv.org/pdf/2508.13769.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13769v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13769v1', 'Can Large Language Models (LLMs) Describe Pictures Like Children? A Comparative Corpus Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanna Woloszyn, Benjamin Gagl

**分类**: cs.CL

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**比较大型语言模型与儿童语言描述的相似性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `儿童语言` `心理语言学` `文本生成` `多模态提示`

## 📋 核心要点

1. 现有研究较少关注大型语言模型生成的文本是否能够有效模拟儿童的语言特征，存在理解不足的问题。
2. 本研究通过比较LLM生成的文本与儿童描述，采用零-shot和few-shot提示，探索LLM在儿童语言生成中的表现。
3. 研究结果表明，LLM生成的文本在长度上较长，但在词汇丰富性和名词使用上表现不足，提示方法对相似性提升有限。

## 📝 摘要（中文）

大型语言模型（LLMs）在教育中的作用日益增加，但对其生成文本是否类似儿童语言的研究较少。本研究通过比较LLM生成的文本与德国儿童对图画故事的描述，评估LLM在儿童语言方面的表现。研究生成了两个基于LLM的语料库，使用相同的图画故事和两种提示类型：零-shot和few-shot提示。分析结果显示，LLM生成的文本较长但词汇丰富性较低，依赖高频词，并且名词的表现不足。语义向量空间分析揭示了两个语料库在语义层面的低相似性。尽管few-shot提示在一定程度上增加了儿童与LLM文本之间的相似性，但仍未能完全复制词汇和语义模式。研究为理解LLM如何通过多模态提示接近儿童语言提供了见解，并对其在心理语言学研究和教育中的应用提出了重要问题。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型生成的文本是否能够有效模拟儿童语言的问题。现有方法未能充分探讨LLM生成文本的儿童语言特征，导致对其在教育中的适用性理解不足。

**核心思路**：通过比较LLM生成的文本与儿童的描述，采用不同的提示方式（零-shot和few-shot），分析其在语言特征上的相似性，以评估LLM在儿童语言生成中的能力。

**技术框架**：研究生成了两个基于LLM的语料库，使用相同的图画故事，并对生成文本进行心理语言学特性分析，包括词频、词汇丰富性、句子和单词长度、词性标记及语义相似性等。

**关键创新**：本研究的创新点在于首次系统性地比较LLM生成文本与儿童语言的相似性，揭示了LLM在儿童语言生成中的局限性，尤其是在词汇和语义层面。

**关键设计**：在实验中，采用了两种提示方式（零-shot和few-shot），并对生成文本的心理语言学特性进行了详细分析，使用了语义向量空间分析来评估文本之间的相似性。具体参数设置和损失函数等技术细节未在摘要中详细说明。

## 📊 实验亮点

实验结果显示，LLM生成的文本长度较长，但词汇丰富性较低，依赖高频词，名词使用不足。尽管few-shot提示在一定程度上提高了儿童与LLM文本之间的相似性，但仍未能完全复制儿童语言的词汇和语义模式。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术和心理语言学研究。通过理解LLM在儿童语言生成中的表现，可以为开发更有效的儿童教育工具提供理论基础，促进儿童语言学习和认知发展。

## 📄 摘要（原文）

> The role of large language models (LLMs) in education is increasing, yet little attention has been paid to whether LLM-generated text resembles child language. This study evaluates how LLMs replicate child-like language by comparing LLM-generated texts to a collection of German children's descriptions of picture stories. We generated two LLM-based corpora using the same picture stories and two prompt types: zero-shot and few-shot prompts specifying a general age from the children corpus. We conducted a comparative analysis across psycholinguistic text properties, including word frequency, lexical richness, sentence and word length, part-of-speech tags, and semantic similarity with word embeddings. The results show that LLM-generated texts are longer but less lexically rich, rely more on high-frequency words, and under-represent nouns. Semantic vector space analysis revealed low similarity, highlighting differences between the two corpora on the level of corpus semantics. Few-shot prompt increased similarities between children and LLM text to a minor extent, but still failed to replicate lexical and semantic patterns. The findings contribute to our understanding of how LLMs approximate child language through multimodal prompting (text + image) and give insights into their use in psycholinguistic research and education while raising important questions about the appropriateness of LLM-generated language in child-directed educational tools.

