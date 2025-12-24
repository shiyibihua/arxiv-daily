---
layout: default
title: Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions
---

# Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08287" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08287v1</a>
  <a href="https://arxiv.org/pdf/2508.08287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08287v1', 'Sacred or Synthetic? Evaluating LLM Reliability and Abstention for Religious Questions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Farah Atif, Nursultan Askarbekuly, Kareem Darwish, Monojit Choudhury

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-08-04

**备注**: 8th AAAI/ACM Conference on AI, Ethics, and Society (AIES 2025)

---

## 💡 一句话要点

**提出FiqhQA基准以评估LLM在宗教问题上的可靠性与回避行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `宗教问题` `伊斯兰教法` `模型评估` `回避行为` `多语言处理` `基准测试`

## 📋 核心要点

1. 现有研究未能充分评估LLMs在宗教领域的可靠性，尤其是对不同宗教学派的区分和回避行为的考量。
2. 本文提出FiqhQA基准，专注于生成伊斯兰教法判决，并评估LLMs在准确性和回避能力上的表现。
3. 实验结果显示，GPT-4o在准确性上优于其他模型，而Gemini和Fanar在回避行为上表现更佳，尤其在阿拉伯语中存在性能下降。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在多个领域的问答中得到广泛应用，但其在宗教领域的可靠性和准确性尚未得到充分研究。本文引入了一个新基准FiqhQA，专注于由四大主要逊尼派学派明确分类的伊斯兰教法判决，涵盖阿拉伯语和英语。与以往研究不同，本文不仅评估LLMs的准确性，还考察其识别何时不回答的能力。我们的零-shot和回避实验显示，LLMs在准确性和回避行为上存在显著差异，尤其在阿拉伯语中表现出性能下降，强调了在非英语语言中进行宗教推理的局限性。此研究首次对LLMs在特定伊斯兰学派判决生成的有效性进行基准测试，并评估其在伊斯兰法学查询中的回避能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在宗教问题回答中的可靠性和准确性不足，特别是在不同宗教学派的区分和回避行为的评估上存在的挑战。

**核心思路**：通过引入FiqhQA基准，专注于伊斯兰教法判决的生成，评估LLMs在准确性和回避能力上的表现，以填补现有研究的空白。

**技术框架**：研究采用零-shot学习和回避实验，比较不同LLMs在阿拉伯语和英语中的表现，分析其在四大逊尼派学派中的准确性和回避能力。

**关键创新**：本研究首次针对特定伊斯兰学派的判决生成进行基准测试，并评估LLMs在宗教法学查询中的回避能力，强调了任务特定评估的重要性。

**关键设计**：实验中使用了多种LLMs，包括GPT-4o、Gemini和Fanar，设置了不同的评估标准，关注模型在不同语言和学派下的表现差异。具体的损失函数和参数设置未详细披露，需进一步研究。

## 📊 实验亮点

实验结果显示，GPT-4o在准确性上优于其他模型，而Gemini和Fanar在回避行为上表现更佳，尤其在阿拉伯语中所有模型的性能均有所下降，强调了在非英语环境中进行宗教推理的挑战。

## 🎯 应用场景

该研究的潜在应用领域包括宗教教育、法律咨询和智能问答系统等。通过提高LLMs在宗教问题上的可靠性和准确性，可以为用户提供更为可信的答案，减少错误信息的传播。此外，研究结果也为未来在其他领域的模型评估提供了借鉴。

## 📄 摘要（原文）

> Despite the increasing usage of Large Language Models (LLMs) in answering questions in a variety of domains, their reliability and accuracy remain unexamined for a plethora of domains including the religious domains. In this paper, we introduce a novel benchmark FiqhQA focused on the LLM generated Islamic rulings explicitly categorized by the four major Sunni schools of thought, in both Arabic and English. Unlike prior work, which either overlooks the distinctions between religious school of thought or fails to evaluate abstention behavior, we assess LLMs not only on their accuracy but also on their ability to recognize when not to answer. Our zero-shot and abstention experiments reveal significant variation across LLMs, languages, and legal schools of thought. While GPT-4o outperforms all other models in accuracy, Gemini and Fanar demonstrate superior abstention behavior critical for minimizing confident incorrect answers. Notably, all models exhibit a performance drop in Arabic, highlighting the limitations in religious reasoning for languages other than English. To the best of our knowledge, this is the first study to benchmark the efficacy of LLMs for fine-grained Islamic school of thought specific ruling generation and to evaluate abstention for Islamic jurisprudence queries. Our findings underscore the need for task-specific evaluation and cautious deployment of LLMs in religious applications.

