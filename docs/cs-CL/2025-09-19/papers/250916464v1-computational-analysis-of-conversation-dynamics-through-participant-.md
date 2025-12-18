---
layout: default
title: Computational Analysis of Conversation Dynamics through Participant Responsivity
---

# Computational Analysis of Conversation Dynamics through Participant Responsivity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16464" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16464v1</a>
  <a href="https://arxiv.org/pdf/2509.16464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16464v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16464v1', 'Computational Analysis of Conversation Dynamics through Participant Responsivity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Margaret Hughes, Brandon Roy, Elinor Poole-Dayan, Deb Roy, Jad Kabbara

**分类**: cs.CL, cs.CY

**发布日期**: 2025-09-19

**期刊**: Proc. EMNLP (2025) 35500--35519

---

## 💡 一句话要点

**通过参与者响应性分析对话动态，量化对话质量并区分不同对话。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话分析` `响应性` `大型语言模型` `对话质量` `语义相似性`

## 📋 核心要点

1. 现有工作较少关注如何表征亲社会和建设性的对话，对话质量的量化缺乏有效方法。
2. 论文核心思想是基于“响应性”来量化对话质量，即衡量对话中发言之间的回应关系。
3. 通过语义相似性和大型语言模型两种方法量化响应性，并使用人工标注数据进行评估，验证了方法的有效性。

## 📝 摘要（中文）

本文旨在探索对话中的亲社会和建设性因素，重点研究“响应性”——即一方的发言是否回应了前一方的发言。研究提出了量化响应性的方法，包括基于语义相似性的方法和利用大型语言模型（LLM）识别发言间关系的方法。通过人工标注的对话数据集对这些方法进行了评估。研究选择了表现较好的基于LLM的方法，并分析了响应的性质，判断其是否对前一发言做出了实质性回应。研究将响应性连接视为对话的基本方面，并开发了对话级别的衍生指标，用于表征对话的不同方面。最后，利用这些指标分析了不同的对话，证明它们能够支持对各种对话进行有意义的表征和区分。

## 🔬 方法详解

**问题定义**：本文旨在解决如何量化对话质量，特别是如何衡量对话的“响应性”这一问题。现有方法在表征对话的亲社会和建设性方面存在不足，缺乏有效手段来区分不同类型的对话。

**核心思路**：论文的核心思路是通过分析对话中发言之间的回应关系来量化对话质量。响应性被定义为一方的发言是否回应了前一方的发言。通过量化响应性，可以更好地理解对话的动态和质量。

**技术框架**：该方法包含以下几个主要阶段：1) 使用语义相似性或大型语言模型（LLM）来识别发言之间的响应关系。2) 评估这些方法在人工标注数据集上的性能。3) 选择表现较好的方法，并分析响应的性质（实质性回应或非实质性回应）。4) 基于响应性连接构建对话级别的衍生指标，用于表征对话的不同方面。

**关键创新**：该研究的关键创新在于将“响应性”这一概念引入对话质量的量化中，并提出了基于语义相似性和大型语言模型两种方法来量化响应性。此外，该研究还开发了对话级别的衍生指标，用于更全面地表征对话的动态。

**关键设计**：在基于LLM的方法中，需要选择合适的LLM模型，并设计合适的prompt来指导模型识别发言之间的响应关系。此外，还需要定义响应的性质（例如，实质性回应或非实质性回应），并设计相应的分类器来判断响应的性质。对话级别的衍生指标的设计也需要仔细考虑，以确保能够有效地表征对话的不同方面。

## 📊 实验亮点

研究通过实验验证了基于大型语言模型的方法在量化对话响应性方面的有效性。该方法在人工标注数据集上取得了良好的性能，能够准确识别发言之间的响应关系，并区分不同类型的响应。此外，研究还证明了对话级别的衍生指标能够有效地表征和区分不同类型的对话。

## 🎯 应用场景

该研究成果可应用于多个领域，例如在线社区管理、客户服务、教育和心理咨询。通过量化对话质量，可以帮助识别和促进建设性的对话，减少有害言论和极化现象。此外，该研究还可以用于评估对话机器人的性能，并改进其对话策略。

## 📄 摘要（原文）

> Growing literature explores toxicity and polarization in discourse, with comparatively less work on characterizing what makes dialogue prosocial and constructive. We explore conversational discourse and investigate a method for characterizing its quality built upon the notion of ``responsivity'' -- whether one person's conversational turn is responding to a preceding turn. We develop and evaluate methods for quantifying responsivity -- first through semantic similarity of speaker turns, and second by leveraging state-of-the-art large language models (LLMs) to identify the relation between two speaker turns. We evaluate both methods against a ground truth set of human-annotated conversations. Furthermore, selecting the better performing LLM-based approach, we characterize the nature of the response -- whether it responded to that preceding turn in a substantive way or not.
>   We view these responsivity links as a fundamental aspect of dialogue but note that conversations can exhibit significantly different responsivity structures. Accordingly, we then develop conversation-level derived metrics to address various aspects of conversational discourse. We use these derived metrics to explore other conversations and show that they support meaningful characterizations and differentiations across a diverse collection of conversations.

