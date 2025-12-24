---
layout: default
title: Detecting Hope, Hate, and Emotion in Arabic Textual Speech and Multi-modal Memes Using Large Language Models
---

# Detecting Hope, Hate, and Emotion in Arabic Textual Speech and Multi-modal Memes Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15810" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15810v1</a>
  <a href="https://arxiv.org/pdf/2508.15810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15810v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15810v1', 'Detecting Hope, Hate, and Emotion in Arabic Textual Speech and Multi-modal Memes Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nouar AlDahoul, Yasir Zaki

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-15

**备注**: 26 pages, 12 figures

---

## 💡 一句话要点

**利用大型语言模型检测阿拉伯文本中的希望、仇恨与情感**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿拉伯文本分析` `大型语言模型` `情感识别` `仇恨言论检测` `多模态内容审核`

## 📋 核心要点

1. 现有方法在处理阿拉伯文本和表情包时，往往无法有效识别仇恨言论和情感表达，导致内容审核的准确性不足。
2. 论文提出利用大型语言模型，特别是微调的模型，来识别阿拉伯文本中的希望、仇恨和情感，提升内容分析的准确性。
3. 实验结果显示，微调后的模型在多个任务上取得了显著的性能提升，尤其是在MAHED 2025挑战中表现优异，整体排名第一。

## 📝 摘要（中文）

随着社交媒体和在线交流平台的兴起，阿拉伯文本和表情包作为数字表达的重要形式日益普及。这些内容虽然可以幽默和信息丰富，但也被用于传播攻击性语言和仇恨言论。因此，对阿拉伯文本和表情包内容的精确分析需求日益增长。本文探讨了大型语言模型在识别希望、仇恨言论、攻击性语言和情感表达方面的潜力。通过评估基础LLMs、微调LLMs和预训练嵌入模型的性能，结果表明，微调后的GPT-4o-mini和Gemini Flash 2.5在MAHED 2025挑战中表现优异，分别在任务1、2和3中取得了72.1%、57.8%和79.6%的宏F1分数，整体排名第一。所提出的解决方案为阿拉伯内容的准确和高效的内容审核系统提供了更细致的理解。

## 🔬 方法详解

**问题定义**：本文旨在解决阿拉伯文本和表情包中仇恨言论和情感表达的检测问题。现有方法在准确性和效率上存在不足，难以满足内容审核的需求。

**核心思路**：通过利用大型语言模型，特别是针对阿拉伯文本和表情包进行微调的模型，来提高对希望、仇恨言论和情感表达的识别能力。这样的设计旨在充分利用语言模型的上下文理解能力。

**技术框架**：整体架构包括数据收集、模型选择、微调和评估四个主要阶段。首先，收集阿拉伯文本和表情包数据，然后选择基础的LLMs进行微调，最后通过宏F1分数评估模型性能。

**关键创新**：最重要的技术创新在于微调大型语言模型以适应特定的阿拉伯文本和表情包内容，这与传统的通用模型应用有本质区别，能够更好地捕捉文化和语言的细微差别。

**关键设计**：在模型微调过程中，采用了特定的损失函数和参数设置，以确保模型能够有效学习阿拉伯语的语义特征和情感表达。

## 📊 实验亮点

实验结果显示，微调后的GPT-4o-mini和Gemini Flash 2.5在MAHED 2025挑战中分别取得了72.1%、57.8%和79.6%的宏F1分数，整体排名第一，显著提升了对阿拉伯文本和表情包的内容分析能力。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线社区管理和情感分析工具。通过提高对阿拉伯文本和表情包的理解，能够有效减少仇恨言论的传播，促进网络环境的和谐与安全。未来，该技术还可以扩展到其他语言和文化背景的内容分析中。

## 📄 摘要（原文）

> The rise of social media and online communication platforms has led to the spread of Arabic textual posts and memes as a key form of digital expression. While these contents can be humorous and informative, they are also increasingly being used to spread offensive language and hate speech. Consequently, there is a growing demand for precise analysis of content in Arabic text and memes. This paper explores the potential of large language models to effectively identify hope, hate speech, offensive language, and emotional expressions within such content. We evaluate the performance of base LLMs, fine-tuned LLMs, and pre-trained embedding models. The evaluation is conducted using a dataset of Arabic textual speech and memes proposed in the ArabicNLP MAHED 2025 challenge. The results underscore the capacity of LLMs such as GPT-4o-mini, fine-tuned with Arabic textual speech, and Gemini Flash 2.5, fine-tuned with Arabic memes, to deliver the superior performance. They achieve up to 72.1%, 57.8%, and 79.6% macro F1 scores for tasks 1, 2, and 3, respectively, and secure first place overall in the Mahed 2025 challenge. The proposed solutions offer a more nuanced understanding of both text and memes for accurate and efficient Arabic content moderation systems.

