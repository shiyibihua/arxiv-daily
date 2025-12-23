---
layout: default
title: Is There a Case for Conversation Optimized Tokenizers in Large Language Models?
---

# Is There a Case for Conversation Optimized Tokenizers in Large Language Models?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18674" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18674v1</a>
  <a href="https://arxiv.org/pdf/2506.18674.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18674v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18674v1', 'Is There a Case for Conversation Optimized Tokenizers in Large Language Models?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raquel Ferrando, Javier Conde, Gonzalo Martínez, Pedro Reviriego

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出对话优化的分词器以提升大型语言模型的效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `分词器优化` `聊天机器人` `自然语言处理` `能量节省` `对话系统` `计算效率`

## 📋 核心要点

1. 现有的分词器主要针对训练语料库进行了优化，未考虑聊天机器人等应用场景的特定需求。
2. 论文提出了一种针对聊天对话优化的分词器，通过重新设计词汇来提高在用户输入和响应中的表现。
3. 实验结果显示，对话优化的分词器能够减少5%到10%的token数量，带来显著的能量节省。

## 📝 摘要（中文）

大型语言模型（LLMs）的计算和能耗成本因模型规模的增长和用户的广泛采用而呈指数级上升。LLM的单位成本是计算一个token，因此分词器在模型效率中扮演着重要角色。现有的分词器主要针对训练语料库进行了优化，而对于聊天机器人等应用场景，用户输入和聊天机器人响应的文本可能与训练语料库不同。本文探讨了针对聊天对话优化分词器的潜在益处，通过使用公开的聊天对话语料库重新设计分词器的词汇，并评估其在该领域的表现。结果表明，对话优化的分词器在聊天对话中能够持续减少token数量，从而实现5%到10%的能量节省，同时对原训练语料的token化效率影响较小或略有正面影响。

## 🔬 方法详解

**问题定义**：本文旨在解决现有分词器在聊天机器人应用中效率不足的问题，现有方法未能考虑用户输入和响应的特定文本特征。

**核心思路**：论文提出通过分析聊天对话语料库，重新设计分词器的词汇，以优化其在对话场景中的表现，提升token化效率。

**技术框架**：研究首先收集公开的聊天对话语料库，然后对比不同分词器在该语料库上的表现，最后评估优化后的分词器在能耗和效率上的改进。

**关键创新**：最重要的创新在于提出了对话优化的分词器设计思路，针对聊天场景的特定需求进行优化，与传统分词器的设计思路形成鲜明对比。

**关键设计**：在设计过程中，研究者对词汇进行了重新构建，关注token数量的减少，同时保持对原训练语料的token化效率，确保优化的分词器在不同场景下均能有效运作。

## 📊 实验亮点

实验结果表明，对话优化的分词器在聊天对话中能够减少token数量5%到10%，实现显著的能量节省，同时对原训练语料的token化效率影响较小或略有正面影响。这一发现为分词器的应用提供了新的视角，具有重要的实际意义。

## 🎯 应用场景

该研究的潜在应用领域包括聊天机器人、智能客服系统和其他需要自然语言处理的交互式应用。通过优化分词器，可以显著降低计算成本和能耗，从而提升用户体验和系统的可持续性。未来，这一研究成果可能推动更多针对特定应用场景的分词器设计，促进自然语言处理技术的进一步发展。

## 📄 摘要（原文）

> The computational and energy costs of Large Language Models (LLMs) have increased exponentially driven by the growing model sizes and the massive adoption of LLMs by hundreds of millions of users. The unit cost of an LLM is the computation of a token. Therefore, the tokenizer plays an important role in the efficiency of a model, and they are carefully optimized to minimize the number of tokens for the text in their training corpus. One of the most popular applications of LLMs are chatbots that interact with users. A key observation is that, for those chatbots, what is important is the performance of the tokenizer in the user text input and the chatbot responses. Those are most likely different from the text in the training corpus. So, a question that immediately arises is whether there is a potential benefit in optimizing tokenizers for chatbot conversations. In this paper, this idea is explored for different tokenizers by using a publicly available corpus of chatbot conversations to redesign their vocabularies and evaluate their performance in this domain. The results show that conversation-optimized tokenizers consistently reduce the number of tokens in chatbot dialogues, which can lead to meaningful energy savings, in the range of 5% to 10% while having minimal or even slightly positive impact on tokenization efficiency for the original training corpus.

