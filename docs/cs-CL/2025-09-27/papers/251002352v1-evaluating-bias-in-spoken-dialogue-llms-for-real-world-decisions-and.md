---
layout: default
title: Evaluating Bias in Spoken Dialogue LLMs for Real-World Decisions and Recommendations
---

# Evaluating Bias in Spoken Dialogue LLMs for Real-World Decisions and Recommendations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02352" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02352v1</a>
  <a href="https://arxiv.org/pdf/2510.02352.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02352v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02352v1', 'Evaluating Bias in Spoken Dialogue LLMs for Real-World Decisions and Recommendations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihao Wu, Tianrui Wang, Yizhou Peng, Yi-Wen Chao, Xuyi Zhuang, Xinsheng Wang, Shunshun Yin, Ziyang Ma

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**系统评估语音对话大模型在决策和推荐中的偏见，揭示多轮对话下的偏见放大效应。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音对话模型` `偏见评估` `公平性` `多轮对话` `副语言特征` `决策推荐` `群体不公平性`

## 📋 核心要点

1. 现有研究较少关注语音对话模型中存在的偏见，特别是副语言特征（如年龄、性别、口音）对模型输出的影响。
2. 该研究系统性地评估了语音LLM中的偏见，并研究了多轮对话中重复负反馈对偏见的影响，着重关注决策和推荐任务。
3. 实验结果表明，闭源模型偏见较低，开源模型对年龄和性别更敏感，推荐任务易放大群体差异，且偏见决策可能在多轮对话中持续存在。

## 📝 摘要（中文）

本文系统性地评估了语音大型语言模型（LLM）中的偏见，重点关注音频输入和输出的口语对话模型（SDM）。研究考察了年龄、性别和口音等副语言特征对模型输出的影响，以及多轮对话中重复负反馈如何加剧偏见，从而影响决策和推荐任务的公平性。论文使用群体不公平分数（GUS）和基于相似性的归一化统计率（SNSR）来衡量偏见，评估了Qwen2.5-Omni、GLM-4-Voice等开源模型以及GPT-4o Audio、Gemini-2.5-Flash等闭源API。结果表明，闭源模型通常表现出较低的偏见，而开源模型对年龄和性别更敏感，推荐任务更容易放大群体差异。此外，偏见决策可能在多轮对话中持续存在。该研究首次对端到端语音对话模型中的偏见进行了系统性研究，为构建公平可靠的音频交互系统提供了见解。为了促进进一步研究，论文发布了FairDialogue数据集和评估代码。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）偏见研究主要集中在文本领域，而忽略了语音对话模型（SDM）中由于音频输入带来的偏见。特别是，年龄、性别、口音等副语言特征如何影响模型的决策和推荐，以及多轮对话如何放大这些偏见，缺乏系统性的研究。现有方法难以有效评估和缓解这些偏见，可能导致不公平的决策和推荐结果。

**核心思路**：该研究的核心思路是通过设计特定的评估指标和实验场景，系统性地量化语音对话模型在决策和推荐任务中的偏见。通过对比不同模型（开源和闭源）在不同副语言特征下的表现，揭示偏见的来源和影响因素。同时，研究多轮对话中偏见的演变，分析重复负反馈是否会加剧偏见。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据集构建：构建包含不同年龄、性别、口音的语音对话数据集FairDialogue。2) 偏见评估指标：采用群体不公平分数（GUS）衡量决策任务中的偏见，采用基于相似性的归一化统计率（SNSR）衡量推荐任务中的偏见。3) 模型评估：在FairDialogue数据集上评估开源模型（如Qwen2.5-Omni、GLM-4-Voice）和闭源API（如GPT-4o Audio、Gemini-2.5-Flash）的偏见。4) 多轮对话分析：设计多轮对话场景，分析偏见在对话过程中的演变。

**关键创新**：该研究的创新点在于：1) 首次系统性地评估了端到端语音对话模型中的偏见。2) 提出了适用于语音对话场景的偏见评估指标（GUS和SNSR）。3) 揭示了多轮对话中偏见的放大效应。4) 构建了FairDialogue数据集，为后续研究提供了基准。

**关键设计**：在偏见评估指标方面，GUS用于衡量不同群体在决策任务中的不公平程度，SNSR用于衡量推荐任务中不同群体的推荐相似度差异。在多轮对话设计方面，通过引入重复的负反馈，模拟真实场景中用户对模型推荐的不满，观察模型是否会因为负反馈而加剧偏见。具体参数设置和网络结构取决于所评估的语音对话模型，研究重点在于评估而非修改模型本身。

## 📊 实验亮点

实验结果表明，闭源模型（如GPT-4o Audio、Gemini-2.5-Flash）通常表现出较低的偏见，而开源模型（如Qwen2.5-Omni、GLM-4-Voice）对年龄和性别更敏感。推荐任务更容易放大群体差异。此外，研究发现，在多轮对话中，即使给予重复的负反馈，模型仍然可能坚持带有偏见的决策。

## 🎯 应用场景

该研究成果可应用于开发更公平、更可靠的语音助手、智能客服和个性化推荐系统。通过识别和缓解语音对话模型中的偏见，可以避免歧视性决策和推荐，提升用户体验，并促进人工智能技术的公平应用。未来的研究可以进一步探索如何利用该研究的发现来设计更有效的偏见缓解策略。

## 📄 摘要（原文）

> While biases in large language models (LLMs), such as stereotypes and cultural tendencies in outputs, have been examined and identified, their presence and characteristics in spoken dialogue models (SDMs) with audio input and output remain largely unexplored. Paralinguistic features, such as age, gender, and accent, can affect model outputs; when compounded by multi-turn conversations, these effects may exacerbate biases, with potential implications for fairness in decision-making and recommendation tasks. In this paper, we systematically evaluate biases in speech LLMs and study the impact of multi-turn dialogues with repeated negative feedback. Bias is measured using Group Unfairness Score (GUS) for decisions and similarity-based normalized statistics rate (SNSR) for recommendations, across both open-source models like Qwen2.5-Omni and GLM-4-Voice, as well as closed-source APIs such as GPT-4o Audio and Gemini-2.5-Flash. Our analysis reveals that closed-source models generally exhibit lower bias, while open-source models are more sensitive to age and gender, and recommendation tasks tend to amplify cross-group disparities. We found that biased decisions may persist in multi-turn conversations. This work provides the first systematic study of biases in end-to-end spoken dialogue models, offering insights towards fair and reliable audio-based interactive systems. To facilitate further research, we release the FairDialogue dataset and evaluation code.

