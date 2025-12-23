---
layout: default
title: Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions
---

# Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22679" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22679v1</a>
  <a href="https://arxiv.org/pdf/2506.22679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22679v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22679v1', 'Assessing the feasibility of Large Language Models for detecting micro-behaviors in team interactions during space missions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ankush Raut, Projna Paromita, Sydney Begerowski, Suzanne Bell, Theodora Chaspari

**分类**: cs.CL

**发布日期**: 2025-06-27

**备注**: 5 pages, 4 figures. Accepted to Interspeech 2025

---

## 💡 一句话要点

**利用大型语言模型检测太空任务团队互动中的微行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `微行为检测` `团队沟通` `太空任务` `机器学习` `自然语言处理` `分类任务`

## 📋 核心要点

1. 现有方法在检测团队对话中的稀有微行为时存在显著不足，尤其是对消极言论的识别能力较弱。
2. 论文提出结合零样本分类、微调和带释义的微调等方法，利用大型语言模型进行微行为预测。
3. 实验结果显示，解码器模型Llama-3.1在分类任务中表现优越，宏F1分数显著高于编码器模型，提升效果明显。

## 📝 摘要（中文）

本研究探讨了大型语言模型（LLMs）在检测模拟太空任务中团队对话微行为的可行性。我们分析了零样本分类、微调和带释义的微调等方法，发现编码器模型如RoBERTa和DistilBERT在检测稀有微行为方面表现不佳，而解码器模型Llama-3.1的指令微调版本在分类任务中表现优越，宏F1分数分别达到44%和68%。这些发现对开发分析团队沟通动态的语音技术具有重要意义，尤其是在文本为唯一可用数据的高风险环境中。

## 🔬 方法详解

**问题定义**：本研究旨在解决在模拟太空任务中，如何有效检测团队对话中的微行为，尤其是稀有的消极言论。现有的编码器模型在此任务中表现不佳，无法准确识别这些微行为。

**核心思路**：论文的核心思路是利用大型语言模型的多种训练方式，包括零样本分类和微调，来提高对微行为的检测能力。通过对比不同模型和训练策略，寻找最佳方案以提升分类性能。

**技术框架**：整体架构包括数据收集、模型选择、训练策略和评估模块。首先收集模拟太空任务的对话文本，然后选择合适的LLMs进行训练，最后通过分类任务评估模型性能。

**关键创新**：最重要的技术创新点在于将解码器模型Llama-3.1的指令微调应用于微行为检测，显著提升了对稀有微行为的识别能力，与传统编码器模型形成鲜明对比。

**关键设计**：在模型训练中，采用加权微调策略来应对数据不平衡问题，并对模型的超参数进行优化，以提高分类精度。

## 📊 实验亮点

实验结果显示，解码器模型Llama-3.1的指令微调版本在3类分类任务中取得了44%的宏F1分数，而在二分类任务中达到了68%。相比之下，编码器模型如RoBERTa和DistilBERT在检测稀有微行为时表现不佳，未能有效识别消极言论。

## 🎯 应用场景

该研究的潜在应用领域包括太空任务、军事训练和高风险环境中的团队沟通分析。通过提高对微行为的检测能力，可以增强团队协作效率，改善沟通策略，进而提升任务成功率和安全性。

## 📄 摘要（原文）

> We explore the feasibility of large language models (LLMs) in detecting subtle expressions of micro-behaviors in team conversations using transcripts collected during simulated space missions. Specifically, we examine zero-shot classification, fine-tuning, and paraphrase-augmented fine-tuning with encoder-only sequence classification LLMs, as well as few-shot text generation with decoder-only causal language modeling LLMs, to predict the micro-behavior associated with each conversational turn (i.e., dialogue). Our findings indicate that encoder-only LLMs, such as RoBERTa and DistilBERT, struggled to detect underrepresented micro-behaviors, particularly discouraging speech, even with weighted fine-tuning. In contrast, the instruction fine-tuned version of Llama-3.1, a decoder-only LLM, demonstrated superior performance, with the best models achieving macro F1-scores of 44% for 3-way classification and 68% for binary classification. These results have implications for the development of speech technologies aimed at analyzing team communication dynamics and enhancing training interventions in high-stakes environments such as space missions, particularly in scenarios where text is the only accessible data.

