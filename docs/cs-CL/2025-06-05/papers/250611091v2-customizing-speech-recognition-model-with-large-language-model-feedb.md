---
layout: default
title: Customizing Speech Recognition Model with Large Language Model Feedback
---

# Customizing Speech Recognition Model with Large Language Model Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11091" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11091v2</a>
  <a href="https://arxiv.org/pdf/2506.11091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11091v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11091v2', 'Customizing Speech Recognition Model with Large Language Model Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaoshi Ling, Guoli Ye

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-06-05 (更新: 2025-08-19)

---

## 💡 一句话要点

**提出基于大语言模型反馈的ASR模型定制方法以解决领域适应问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动语音识别` `领域适应` `大语言模型` `强化学习` `命名实体识别`

## 📋 核心要点

1. 现有的ASR系统在识别稀有命名实体和适应特定领域时表现不佳，导致转录质量下降。
2. 本文提出了一种利用大语言模型反馈的强化学习方法，通过无监督学习提升ASR模型在特定领域的适应能力。
3. 实验结果表明，该方法在实体词错误率上较传统自训练方法提升了21%，显示出显著的效果改善。

## 📝 摘要（中文）

自动语音识别（ASR）系统在通用转录任务中表现良好，但在识别稀有命名实体和适应领域不匹配方面仍然存在挑战。相比之下，经过大规模互联网数据集训练的大语言模型（LLMs）在多个领域的效果更佳。本文提出了一种基于强化学习的无监督领域适应方法，利用未标记数据通过LLM反馈提升转录质量，特别是受领域不匹配影响的命名实体。该框架使用LLM作为奖励模型，对ASR模型的假设进行评分，这些评分作为奖励信号用于通过强化学习微调ASR模型。该方法在实体词错误率上较传统自训练方法提高了21%。

## 🔬 方法详解

**问题定义**：本文旨在解决自动语音识别（ASR）系统在领域不匹配情况下对稀有命名实体的识别困难。现有方法在处理未标记数据时效果有限，无法有效提升转录质量。

**核心思路**：提出了一种基于强化学习的无监督领域适应方法，利用大语言模型（LLM）作为奖励模型，通过对ASR模型输出的假设进行评分，进而优化ASR模型的性能。

**技术框架**：整体架构包括数据输入、ASR模型生成假设、LLM反馈评分和强化学习微调四个主要模块。首先，ASR模型生成初步转录结果，然后LLM对这些结果进行评分，最后根据评分结果调整ASR模型。

**关键创新**：该研究的创新点在于将LLM作为奖励模型引入ASR系统，通过无监督学习方式显著提升了对命名实体的识别能力，与传统自训练方法相比，提供了更为有效的反馈机制。

**关键设计**：在参数设置上，采用了适应性学习率和特定的损失函数以优化模型训练过程，网络结构上则结合了LLM的上下文理解能力，确保了对领域特定数据的有效适应。

## 📊 实验亮点

实验结果显示，所提出的方法在实体词错误率上较传统自训练方法提升了21%，显著提高了ASR系统在领域适应中的表现，验证了大语言模型反馈的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、法律、金融等专业领域的语音识别系统，能够有效提升这些领域中对特定术语和命名实体的识别准确性。未来，该方法可扩展至更多领域，推动ASR技术的广泛应用与发展。

## 📄 摘要（原文）

> Automatic speech recognition (ASR) systems have achieved strong performance on general transcription tasks. However, they continue to struggle with recognizing rare named entities and adapting to domain mismatches. In contrast, large language models (LLMs), trained on massive internet-scale datasets, are often more effective across a wide range of domains. In this work, we propose a reinforcement learning based approach for unsupervised domain adaptation, leveraging unlabeled data to enhance transcription quality, particularly the named entities affected by domain mismatch, through feedback from a LLM. Given contextual information, our framework employs a LLM as the reward model to score the hypotheses from the ASR model. These scores serve as reward signals to fine-tune the ASR model via reinforcement learning. Our method achieves a 21\% improvement on entity word error rate over conventional self-training methods.

