---
layout: default
title: What do language models model? Transformers, automata, and the format of thought
---

# What do language models model? Transformers, automata, and the format of thought

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18598" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18598v1</a>
  <a href="https://arxiv.org/pdf/2508.18598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18598v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18598v1', 'What do language models model? Transformers, automata, and the format of thought')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Colin Klein

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**探讨语言模型的本质及其与人类认知的关系**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `变换器架构` `人类语言能力` `快捷自动机` `自然语言处理`

## 📋 核心要点

1. 核心问题：现有的语言模型是否真正反映了人类的语言能力，还是仅仅是对训练数据的建模？
2. 方法要点：论文提出变换器架构在处理语言时的局限性，并探讨其积极作用，特别是快捷自动机的概念。
3. 实验或效果：通过分析变换器的计算架构，得出语言不仅是表达工具，更是生成新语言的机制。

## 📝 摘要（中文）

本文探讨了大型语言模型（LLMs）究竟建模了什么，是否反映了人类的能力，还是仅仅是训练语料库的模型。作者支持后者的观点，认为人类的语言能力依赖于超线性计算格式，而变换器架构最多支持线性格式。文章还提出了变换器在处理语言时的积极作用，特别是基于Liu等（2022）关于快捷自动机的推测。最后，作者认为语言不仅是表达内心状态的工具，更是一种‘话语机器’，能够在适当的上下文中生成新语言。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型（LLMs）究竟建模了什么，尤其是它们是否反映了人类的语言能力，还是仅仅是对训练语料库的建模。现有方法未能充分解释变换器架构与人类语言能力之间的关系。

**核心思路**：作者提出，变换器架构支持的线性计算格式与人类的超线性语言能力存在根本差异。通过分析变换器的计算不变性，作者为理解其在语言处理中的作用提供了新的视角。

**技术框架**：文章的整体架构包括对变换器架构的分析、对人类语言能力的认知科学背景的探讨，以及对快捷自动机的引入。主要模块包括对变换器计算特性的讨论和对语言生成机制的阐述。

**关键创新**：最重要的技术创新在于将变换器架构与人类语言能力的超线性格式进行对比，提出了变换器在语言处理中的积极作用，尤其是快捷自动机的概念，这与现有方法的线性处理方式形成鲜明对比。

**关键设计**：在技术细节上，作者强调了变换器的计算不变性，并探讨了其在语言生成中的应用，提出了语言不仅是表达内心状态的工具，更是生成新语言的机制。作者未详细列出具体的参数设置或损失函数。

## 📊 实验亮点

文章通过对变换器架构的深入分析，提出了语言不仅是表达工具，更是生成新语言的机制。尽管未提供具体的实验数据，但通过理论推导，强调了变换器在语言处理中的独特作用，推动了对语言模型理解的深入。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、语言生成和人机交互等。通过深入理解语言模型的本质，可以改进现有的语言生成技术，推动智能助手和对话系统的发展，提升人机沟通的自然性和有效性。

## 📄 摘要（原文）

> What do large language models actually model? Do they tell us something about human capacities, or are they models of the corpus we've trained them on? I give a non-deflationary defence of the latter position. Cognitive science tells us that linguistic capabilities in humans rely supralinear formats for computation. The transformer architecture, by contrast, supports at best a linear formats for processing. This argument will rely primarily on certain invariants of the computational architecture of transformers. I then suggest a positive story about what transformers are doing, focusing on Liu et al. (2022)'s intriguing speculations about shortcut automata. I conclude with why I don't think this is a terribly deflationary story. Language is not (just) a means for expressing inner state but also a kind of 'discourse machine' that lets us make new language given appropriate context. We have learned to use this technology in one way; LLMs have also learned to use it too, but via very different means.

