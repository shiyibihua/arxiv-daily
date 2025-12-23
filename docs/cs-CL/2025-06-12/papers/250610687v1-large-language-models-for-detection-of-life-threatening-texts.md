---
layout: default
title: Large Language Models for Detection of Life-Threatening Texts
---

# Large Language Models for Detection of Life-Threatening Texts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10687" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10687v1</a>
  <a href="https://arxiv.org/pdf/2506.10687.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10687v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10687v1', 'Large Language Models for Detection of Life-Threatening Texts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thanh Thi Nguyen, Campbell Wilson, Janis Dalins

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**利用大型语言模型检测生命威胁文本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生命威胁检测` `大型语言模型` `文本分类` `心理健康` `不平衡数据处理`

## 📋 核心要点

1. 现有方法在检测生命威胁文本时存在准确性不足和对不平衡数据处理能力差的问题。
2. 本文提出利用大型语言模型（LLMs）进行生命威胁文本的识别，并通过微调不同的LLMs来提高检测效果。
3. 实验结果显示，Mistral和Llama-2在各种数据场景中表现优异，显著优于传统方法，尤其在不平衡数据处理上展现出优势。

## 📝 摘要（中文）

检测生命威胁语言对于保护处于困境中的个体、促进心理健康和福祉以及防止潜在伤害和生命损失至关重要。本文提出了一种有效的方法，利用大型语言模型（LLMs）识别生命威胁文本，并与传统方法（如词袋模型、词嵌入、主题建模和双向编码器表示的变换器）进行了比较。我们对三种开源LLM（Gemma、Mistral和Llama-2）进行了微调，使用其7B参数变体在不同数据集上进行实验。实验结果表明，LLMs在传统方法中表现出色，尤其是Mistral和Llama-2在平衡和不平衡数据场景中表现最佳，而Gemma稍逊一筹。我们采用上采样技术处理不平衡数据场景，结果显示该方法对传统方法有益，但对LLMs影响不大。本研究展示了LLMs在现实生命威胁语言检测问题中的巨大潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决生命威胁文本的检测问题，现有方法在准确性和对不平衡数据的处理能力上存在不足，导致潜在的生命安全风险。

**核心思路**：通过微调大型语言模型（LLMs），如Gemma、Mistral和Llama-2，利用其强大的语言理解能力来提高生命威胁文本的检测准确率，尤其是在不平衡数据场景下。

**技术框架**：研究采用了微调的LLMs作为核心模块，结合数据集的构建（包括平衡、不平衡和极度不平衡场景），并使用上采样技术来处理不平衡数据。实验流程包括数据预处理、模型训练和性能评估。

**关键创新**：本研究的主要创新在于将大型语言模型应用于生命威胁文本检测，展示了其在处理复杂语言结构和上下文理解方面的优势，与传统方法相比，LLMs能够更好地捕捉文本中的潜在威胁信息。

**关键设计**：在模型微调过程中，采用了7B参数的LLMs，并针对不同数据集进行了优化，特别是在不平衡数据场景中，虽然上采样技术对传统方法有显著提升，但对LLMs的影响相对较小，显示出LLMs的鲁棒性。

## 📊 实验亮点

实验结果表明，Mistral和Llama-2在平衡和不平衡数据场景中表现优异，准确率显著高于传统方法，尤其在不平衡数据处理上展现出优势。Gemma虽然表现稍逊，但依然显示出LLMs在生命威胁文本检测中的潜力。整体上，LLMs在该领域的应用展现出良好的前景。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康监测、社交媒体内容审核和危机干预等。通过有效检测生命威胁语言，可以及时采取干预措施，保护个体的安全与健康，具有重要的社会价值和实际意义。未来，随着技术的进步，该方法有望在更广泛的领域得到应用，进一步提升公共安全和心理健康服务的效率。

## 📄 摘要（原文）

> Detecting life-threatening language is essential for safeguarding individuals in distress, promoting mental health and well-being, and preventing potential harm and loss of life. This paper presents an effective approach to identifying life-threatening texts using large language models (LLMs) and compares them with traditional methods such as bag of words, word embedding, topic modeling, and Bidirectional Encoder Representations from Transformers. We fine-tune three open-source LLMs including Gemma, Mistral, and Llama-2 using their 7B parameter variants on different datasets, which are constructed with class balance, imbalance, and extreme imbalance scenarios. Experimental results demonstrate a strong performance of LLMs against traditional methods. More specifically, Mistral and Llama-2 models are top performers in both balanced and imbalanced data scenarios while Gemma is slightly behind. We employ the upsampling technique to deal with the imbalanced data scenarios and demonstrate that while this method benefits traditional approaches, it does not have as much impact on LLMs. This study demonstrates a great potential of LLMs for real-world life-threatening language detection problems.

