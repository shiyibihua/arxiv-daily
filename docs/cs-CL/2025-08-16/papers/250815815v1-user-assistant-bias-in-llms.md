---
layout: default
title: User-Assistant Bias in LLMs
---

# User-Assistant Bias in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15815" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15815v1</a>
  <a href="https://arxiv.org/pdf/2508.15815.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15815v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15815v1', 'User-Assistant Bias in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Pan, Jingxuan Fan, Zidi Xiong, Ely Hahami, Jorin Overwiening, Ziqian Xie

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-08-16

---

## 💡 一句话要点

**提出用户助手偏见模型以优化多轮对话表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户助手偏见` `大型语言模型` `多轮对话` `数据集构建` `偏好优化` `微调实验` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在多轮对话中存在用户助手偏见，导致模型表现不一致，影响用户体验。
2. 论文提出了UserAssist数据集，通过基准测试和微调实验来理解和操控用户助手偏见。
3. 实验结果表明，商业模型和开源模型在用户偏见上表现不同，且通过DPO方法可有效调整偏见。

## 📝 摘要（中文）

大型语言模型（LLMs）在多轮对话中可能会偏向于依赖自身或用户的聊天记录信息，导致过于固执或过于顺从的行为。本文将这一特征形式化为用户助手偏见，并引入了一个包含8000个多轮对话的数据集UserAssist，用于基准测试、理解和操控前沿LLMs中的用户助手偏见。通过UserAssist-test，我们对26个商业模型和26个开源模型的用户助手偏见进行了基准测试，发现商业模型表现出不同程度的用户偏见。开源模型的评估显示，指令调优模型存在显著的用户偏见，而推理模型的用户偏见较弱。我们还进行了受控微调实验，发现人类偏好对齐会增加用户偏见，而基于思维链的训练则会减少偏见。最后，我们展示了通过直接偏好优化（DPO）可以双向调整用户助手偏见，并且在领域内外的对话中均表现良好。我们的结果为LLM如何整合不同来源的信息提供了洞见，并为检测和控制模型异常提供了可行的方法。

## 🔬 方法详解

**问题定义**：本文解决的是大型语言模型在多轮对话中表现出的用户助手偏见问题。现有方法未能有效识别和调整这种偏见，导致模型在对话中表现出固执或过于顺从的行为。

**核心思路**：论文的核心思路是通过引入UserAssist数据集，系统性地评估和操控用户助手偏见，利用微调和偏好优化技术来改善模型的对话表现。

**技术框架**：整体架构包括数据集构建、基准测试、微调实验和偏好优化四个主要模块。首先，通过UserAssist数据集进行基准测试，然后进行受控微调，最后应用DPO技术进行偏见调整。

**关键创新**：最重要的技术创新在于系统性地定义和量化用户助手偏见，并通过实验验证不同训练策略对偏见的影响，提供了一种新的视角来理解LLMs的行为。

**关键设计**：在实验中，采用了人类偏好对齐和思维链训练作为关键设计，前者增加了用户偏见，而后者则有效减少了偏见。

## 📊 实验亮点

实验结果显示，商业模型在用户偏见上表现出不同程度的偏差，而开源模型的指令调优模型则显著存在用户偏见。通过DPO方法，用户助手偏见可以有效地进行双向调整，且在不同对话场景中均表现良好。

## 🎯 应用场景

该研究的潜在应用场景包括智能客服、虚拟助手和教育领域等，能够提升用户与模型的交互体验，减少模型偏见带来的负面影响。未来，研究成果可为更智能的对话系统设计提供理论基础和实践指导。

## 📄 摘要（原文）

> Large language models (LLMs) can bias towards relying on their own or the user's information in chat history, leading to overly stubborn or agreeable behaviors in multi-turn conversations. In this paper, we formalize this model characteristic as user-assistant bias and introduce an 8k multi-turn conversation dataset $\textbf{UserAssist}$, which we use to benchmark, understand and manipulate the user-assistant bias in frontier LLMs. Leveraging $\textbf{UserAssist-test}$, we first benchmark the user-assistant bias of 26 commercial and 26 open-weight models. Commercial models show various levels of user bias. Evaluation on open-weight models reveals significant user bias in the instruction-tuned models, and weak user bias in reasoning (or reasoning-distilled) models. We then perform controlled fine-tuning experiments to pinpoint the post-training recipe contributing to these bias shifts: human preference alignment increases user bias, while training on chain-of-thought reasoning traces decreases it. Finally, we demonstrate that user-assistant bias can be bidirectionally adjusted by performing direct preference optimization (DPO) on $\textbf{UserAssist-train}$, and generalizes well to both in-domain and out-of-domain conversations. Our results provide insights into how the LLM integrates information from different sources, and also a viable way to detect and control model abnormalities.

