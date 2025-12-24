---
layout: default
title: Building and Measuring Trust between Large Language Models
---

# Building and Measuring Trust between Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15858" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15858v1</a>
  <a href="https://arxiv.org/pdf/2508.15858.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15858v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15858v1', 'Building and Measuring Trust between Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maarten Buyl, Yousra Fettach, Guillaume Bied, Tijl De Bie

**分类**: cs.MA, cs.AI, cs.CL

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出信任构建与测量方法以解决LLMs间信任关系问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信任构建` `信任测量` `多代理系统` `人机交互`

## 📋 核心要点

1. 核心问题：现有研究对LLMs之间信任关系的构建与测量缺乏深入了解，特别是隐性与显性信任之间的关系尚不明确。
2. 方法要点：论文提出通过动态建立融洽关系、使用信任脚本和调整系统提示三种方式来构建LLMs之间的信任。
3. 实验或效果：研究发现显性信任测量与隐性信任测量之间的相关性较低或负相关，提示传统测量方法可能不够准确。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在多代理设置中日益相互交互，我们期望它们之间能够建立类似于人类之间的信任关系。尽管已有研究表明LLMs能够识别情感联系和信任游戏中的互惠关系，但关于如何比较不同的信任构建策略、如何隐性测量信任以及这些与显性信任测量的关系仍然知之甚少。本文通过将隐性信任测量（如说服易感性和财务合作倾向）与心理学中已建立的显性信任测量（如二元信任问卷）进行关联，探讨这些问题。我们通过动态建立融洽关系、使用预先编写的信任证据脚本和调整LLMs的系统提示三种方式来构建信任。研究发现，显性信任测量与隐性信任测量之间的相关性较低或高度负相关，这表明通过询问LLMs的意见来测量信任可能具有误导性。相反，特定上下文的隐性测量可能更能有效理解LLMs之间的信任关系。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLMs）之间信任关系的构建与测量问题。现有方法在隐性与显性信任测量之间缺乏有效的关联，导致对LLMs信任关系的理解不足。

**核心思路**：论文通过比较不同的信任构建策略，探讨隐性信任（如说服易感性）与显性信任（如信任问卷）之间的关系，旨在提供更准确的信任测量方法。

**技术框架**：研究设计包括三个主要模块：1）动态建立融洽关系；2）使用预先编写的信任证据脚本；3）调整LLMs的系统提示。这些模块共同作用于信任的构建与测量。

**关键创新**：最重要的创新在于发现显性信任测量与隐性信任测量之间的相关性较低或负相关，挑战了传统信任测量方法的有效性。

**关键设计**：在实验中，使用了标准的二元信任问卷作为显性信任测量工具，同时设计了多种隐性信任测量指标，以确保对信任关系的全面评估。实验结果显示，隐性测量在特定上下文中更具信息价值。

## 📊 实验亮点

实验结果表明，显性信任测量与隐性信任测量之间的相关性较低或负相关，提示传统的信任测量方法可能存在误导性。研究中使用的隐性测量方法在理解LLMs之间的信任关系方面显示出更高的有效性，具有重要的理论和实践意义。

## 🎯 应用场景

该研究的潜在应用领域包括多代理系统、智能助手和人机交互等场景，能够为LLMs之间的信任构建提供理论支持和实践指导，促进更高效的协作与沟通。未来，研究成果可能推动信任机制在人工智能领域的广泛应用，提升系统的可靠性和用户体验。

## 📄 摘要（原文）

> As large language models (LLMs) increasingly interact with each other, most notably in multi-agent setups, we may expect (and hope) that `trust' relationships develop between them, mirroring trust relationships between human colleagues, friends, or partners. Yet, though prior work has shown LLMs to be capable of identifying emotional connections and recognizing reciprocity in trust games, little remains known about (i) how different strategies to build trust compare, (ii) how such trust can be measured implicitly, and (iii) how this relates to explicit measures of trust.
>   We study these questions by relating implicit measures of trust, i.e. susceptibility to persuasion and propensity to collaborate financially, with explicit measures of trust, i.e. a dyadic trust questionnaire well-established in psychology. We build trust in three ways: by building rapport dynamically, by starting from a prewritten script that evidences trust, and by adapting the LLMs' system prompt. Surprisingly, we find that the measures of explicit trust are either little or highly negatively correlated with implicit trust measures. These findings suggest that measuring trust between LLMs by asking their opinion may be deceiving. Instead, context-specific and implicit measures may be more informative in understanding how LLMs trust each other.

