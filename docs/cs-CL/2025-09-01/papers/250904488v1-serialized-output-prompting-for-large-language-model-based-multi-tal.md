---
layout: default
title: Serialized Output Prompting for Large Language Model-based Multi-Talker Speech Recognition
---

# Serialized Output Prompting for Large Language Model-based Multi-Talker Speech Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04488" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04488v1</a>
  <a href="https://arxiv.org/pdf/2509.04488.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04488v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04488v1', 'Serialized Output Prompting for Large Language Model-based Multi-Talker Speech Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Shi, Yusuke Fujita, Tomoya Mizumoto, Lianbo Liu, Atsushi Kojima, Yui Sudo

**分类**: cs.CL, cs.AI, cs.SD, eess.AS

**发布日期**: 2025-09-01

---

## 💡 一句话要点

**提出序列化输出提示以提升多说话者语音识别性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多说话者识别` `序列化输出` `语言模型` `语音识别` `深度学习`

## 📋 核心要点

1. 现有的LLM基础多说话者ASR系统要么省略提示，要么仅依赖简单的任务定义提示，未能有效提升性能。
2. 本文提出序列化输出提示（SOP），通过结构化提示显式引导LLM，从而改善多说话者语音识别的性能。
3. 在LibriMix数据集上的实验结果显示，所提出的SOP方法在双说话者和三说话者场景中均显著提升了识别性能。

## 📝 摘要（中文）

提示在任务定义和提升大型语言模型（LLM）系统性能中至关重要。然而，现有的基于LLM的多说话者自动语音识别（ASR）系统要么省略提示，要么依赖简单的任务定义提示，缺乏针对提示设计以增强性能的研究。本文提出提取序列化输出提示（SOP），并通过结构化提示显式引导LLM，以改善系统性能（SOP-MT-ASR）。在语音编码器后插入分隔符和序列化连接时序分类（CTC）层，以FIFO方式分离和提取混合语音编码中的多说话者内容。随后，通过贪婪搜索解码序列化CTC输出获得SOP，作为LLM的提示。为有效训练模型，设计了三阶段训练策略，包括序列化输出训练（SOT）微调、序列化语音信息提取和基于SOP的适应。实验结果表明，尽管LLM基于SOT模型在双说话者场景中表现良好，但在更复杂的三说话者场景中未能充分利用LLM。所提SOP方法在双说话者和三说话者条件下显著提高了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于LLM的多说话者自动语音识别系统在复杂场景下性能不足的问题。现有方法往往忽视提示设计，导致无法充分利用LLM的潜力。

**核心思路**：论文提出通过提取序列化输出提示（SOP）来显式引导LLM，利用结构化提示来提升多说话者语音识别的效果。该方法通过FIFO方式处理混合语音编码，确保有效提取多说话者内容。

**技术框架**：整体架构包括三个主要模块：语音编码器、序列化连接时序分类（CTC）层和LLM提示生成。首先，语音编码器处理输入语音信号，接着CTC层分离并提取多说话者内容，最后生成SOP作为LLM的输入提示。

**关键创新**：最重要的技术创新在于引入序列化输出提示（SOP），通过结构化提示显著提升了多说话者语音识别的性能。这一方法与传统的简单任务定义提示有本质区别，能够更好地引导LLM。

**关键设计**：在模型训练中，设计了三阶段训练策略，包括序列化输出训练（SOT）微调、序列化语音信息提取和基于SOP的适应。具体参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

实验结果表明，所提出的SOP方法在双说话者和三说话者场景中均显著提高了识别性能。在双说话者场景中，LLM基于SOT模型表现良好，但在三说话者场景中，SOP方法的引入使得性能得到了显著提升，具体提升幅度在实验中有详细数据支持。

## 🎯 应用场景

该研究的潜在应用领域包括会议记录、语音助手和多方通话的语音识别等场景。通过提升多说话者语音识别的准确性，能够为用户提供更优质的语音交互体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Prompts are crucial for task definition and for improving the performance of large language models (LLM)-based systems. However, existing LLM-based multi-talker (MT) automatic speech recognition (ASR) systems either omit prompts or rely on simple task-definition prompts, with no prior work exploring the design of prompts to enhance performance. In this paper, we propose extracting serialized output prompts (SOP) and explicitly guiding the LLM using structured prompts to improve system performance (SOP-MT-ASR). A Separator and serialized Connectionist Temporal Classification (CTC) layers are inserted after the speech encoder to separate and extract MT content from the mixed speech encoding in a first-speaking-first-out manner. Subsequently, the SOP, which serves as a prompt for LLMs, is obtained by decoding the serialized CTC outputs using greedy search. To train the model effectively, we design a three-stage training strategy, consisting of serialized output training (SOT) fine-tuning, serialized speech information extraction, and SOP-based adaptation. Experimental results on the LibriMix dataset show that, although the LLM-based SOT model performs well in the two-talker scenario, it fails to fully leverage LLMs under more complex conditions, such as the three-talker scenario. The proposed SOP approach significantly improved performance under both two- and three-talker conditions.

