---
layout: default
title: Model-Agnostic Sentiment Distribution Stability Analysis for Robust LLM-Generated Texts Detection
---

# Model-Agnostic Sentiment Distribution Stability Analysis for Robust LLM-Generated Texts Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06913" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06913v1</a>
  <a href="https://arxiv.org/pdf/2508.06913.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06913v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06913v1', 'Model-Agnostic Sentiment Distribution Stability Analysis for Robust LLM-Generated Texts Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Li, Xi Lin, Guangyan Li, Zehao Liu, Aodu Wulianghai, Li Ding, Jun Wu, Jianhua Li

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-09

---

## 💡 一句话要点

**提出SentiDetect以解决LLM生成文本检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感分析` `文本检测` `大型语言模型` `模型无关` `鲁棒性`

## 📋 核心要点

1. 现有的文本检测方法在应对LLM生成文本时，泛化能力不足且易受多种扰动影响。
2. 本文提出的SentiDetect框架通过分析情感分布的稳定性差异，提供了一种新的检测思路。
3. 实验结果显示，SentiDetect在多个数据集上表现优异，尤其在复杂场景下具有更强的鲁棒性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速发展，AI生成内容的复杂性日益增加，导致区分LLM生成文本与人类书写语言的挑战显著加大。现有检测方法主要依赖词汇启发式或微调分类器，普遍存在泛化能力有限、易受改写、对抗扰动和跨领域转移影响等问题。本文提出了SentiDetect，一个模型无关的框架，通过分析情感分布稳定性差异来检测LLM生成文本。我们定义了情感分布一致性和情感分布保持性两个互补指标，以量化在情感改变和语义保持变换下的稳定性。实验结果表明，SentiDetect在多个数据集上优于现有最先进的基线，尤其在Gemini-1.5-Pro和GPT-4-0613上分别提升了超过16%和11%的F1分数。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效区分LLM生成文本与人类书写文本的问题。现有方法在面对文本改写和对抗攻击时，表现出较低的稳定性和泛化能力。

**核心思路**：SentiDetect的核心思路是通过分析情感分布的稳定性来识别文本生成来源。LLM生成的文本通常在情感上表现出一致性，而人类文本则更具情感多样性。

**技术框架**：SentiDetect框架包括两个主要模块：情感分布一致性和情感分布保持性。这两个模块分别用于量化文本在情感改变和语义保持变换下的稳定性。

**关键创新**：SentiDetect的创新在于其模型无关性和对情感分布的深入分析，区别于传统基于词汇的检测方法，提供了更为稳健的检测能力。

**关键设计**：在设计中，情感分布一致性和保持性通过特定的数学公式进行量化，确保在不同的文本变换下，能够准确反映情感的稳定性。

## 📊 实验亮点

实验结果表明，SentiDetect在Gemini-1.5-Pro和GPT-4-0613数据集上分别提升了超过16%和11%的F1分数，显示出其在文本检测任务中的显著优势。此外，SentiDetect在面对改写、对抗攻击和文本长度变化时，展现出更强的鲁棒性，超越了现有的检测器。

## 🎯 应用场景

SentiDetect的研究成果可广泛应用于内容审核、社交媒体监控和自动化文本生成检测等领域。随着AI生成内容的普及，能够有效区分人类与机器生成文本的技术将具有重要的社会价值和商业潜力，未来可能推动相关法律法规的制定与实施。

## 📄 摘要（原文）

> The rapid advancement of large language models (LLMs) has resulted in increasingly sophisticated AI-generated content, posing significant challenges in distinguishing LLM-generated text from human-written language. Existing detection methods, primarily based on lexical heuristics or fine-tuned classifiers, often suffer from limited generalizability and are vulnerable to paraphrasing, adversarial perturbations, and cross-domain shifts. In this work, we propose SentiDetect, a model-agnostic framework for detecting LLM-generated text by analyzing the divergence in sentiment distribution stability. Our method is motivated by the empirical observation that LLM outputs tend to exhibit emotionally consistent patterns, whereas human-written texts display greater emotional variability. To capture this phenomenon, we define two complementary metrics: sentiment distribution consistency and sentiment distribution preservation, which quantify stability under sentiment-altering and semantic-preserving transformations. We evaluate SentiDetect on five diverse datasets and a range of advanced LLMs,including Gemini-1.5-Pro, Claude-3, GPT-4-0613, and LLaMa-3.3. Experimental results demonstrate its superiority over state-of-the-art baselines, with over 16% and 11% F1 score improvements on Gemini-1.5-Pro and GPT-4-0613, respectively. Moreover, SentiDetect also shows greater robustness to paraphrasing, adversarial attacks, and text length variations, outperforming existing detectors in challenging scenarios.

