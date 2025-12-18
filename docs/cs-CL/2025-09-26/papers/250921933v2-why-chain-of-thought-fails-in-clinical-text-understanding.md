---
layout: default
title: Why Chain of Thought Fails in Clinical Text Understanding
---

# Why Chain of Thought Fails in Clinical Text Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21933" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21933v2</a>
  <a href="https://arxiv.org/pdf/2509.21933.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21933v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21933v2', 'Why Chain of Thought Fails in Clinical Text Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiageng Wu, Kevin Xie, Bowen Gu, Nils Krüger, Kueiyu Joshua Lin, Jie Yang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-12-08)

---

## 💡 一句话要点

**系统研究链式思维在临床文本理解中的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `链式思维` `临床文本理解` `大型语言模型` `电子健康记录` `可解释性` `可靠性` `医学推理` `系统研究`

## 📋 核心要点

1. 现有的链式思维方法在临床文本理解中表现不佳，尤其是在处理电子健康记录时，模型性能普遍下降。
2. 本文通过系统评估95个LLMs在87个临床文本任务中的表现，揭示了链式思维在临床环境中的局限性。
3. 研究发现，86.3%的模型在链式思维设置下性能下降，尤其是较弱模型的表现显著恶化，强调了可解释性与可靠性之间的矛盾。

## 📝 摘要（中文）

大型语言模型（LLMs）在临床护理中的应用日益增多，准确性和透明推理对于安全和可信的部署至关重要。链式思维（CoT）提示法在多种任务中显示出性能和可解释性的提升，但在临床环境中的有效性尚未得到充分探索。本文首次对CoT在临床文本理解中的应用进行了大规模系统研究，评估了95个先进的LLMs在87个真实世界临床文本任务中的表现。结果显示，86.3%的模型在CoT设置下表现一致下降，尤其是较弱的模型。我们的研究揭示了CoT在临床环境中失败的系统性模式，强调了可解释性与可靠性之间的关键悖论。

## 🔬 方法详解

**问题定义**：本文旨在解决链式思维在临床文本理解中的有效性问题，现有方法在处理电子健康记录时表现不佳，导致模型性能下降。

**核心思路**：通过对95个先进LLMs在87个真实世界临床文本任务中的表现进行系统评估，分析链式思维在临床环境中的失败原因，揭示其对模型可靠性的影响。

**技术框架**：研究采用了大规模的实验设计，涵盖9种语言和8种任务类型，结合LLM作为评判者的评估方法和临床专家的评估，进行细致的分析。

**关键创新**：本研究首次系统性地探讨了链式思维在临床文本理解中的局限性，揭示了可解释性与可靠性之间的悖论，提供了临床推理策略的实证基础。

**关键设计**：研究中采用了细粒度的分析方法，关注推理长度、医学概念对齐和错误特征，结合多种评估方式，确保结果的全面性和准确性。

## 📊 实验亮点

实验结果显示，86.3%的模型在链式思维设置下表现一致下降，尤其是较弱模型的性能显著恶化。这一发现与其他领域的研究结果形成鲜明对比，强调了在临床文本任务中可解释性与可靠性之间的矛盾。

## 🎯 应用场景

该研究的潜在应用领域包括临床决策支持系统、电子健康记录分析和医疗文本挖掘等。通过揭示链式思维在临床文本理解中的局限性，研究为未来开发更透明和可靠的临床推理模型提供了重要参考，推动了医疗人工智能的安全应用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly being applied to clinical care, a domain where both accuracy and transparent reasoning are critical for safe and trustworthy deployment. Chain-of-thought (CoT) prompting, which elicits step-by-step reasoning, has demonstrated improvements in performance and interpretability across a wide range of tasks. However, its effectiveness in clinical contexts remains largely unexplored, particularly in the context of electronic health records (EHRs), the primary source of clinical documentation, which are often lengthy, fragmented, and noisy. In this work, we present the first large-scale systematic study of CoT for clinical text understanding. We assess 95 advanced LLMs on 87 real-world clinical text tasks, covering 9 languages and 8 task types. Contrary to prior findings in other domains, we observe that 86.3\% of models suffer consistent performance degradation in the CoT setting. More capable models remain relatively robust, while weaker ones suffer substantial declines. To better characterize these effects, we perform fine-grained analyses of reasoning length, medical concept alignment, and error profiles, leveraging both LLM-as-a-judge evaluation and clinical expert evaluation. Our results uncover systematic patterns in when and why CoT fails in clinical contexts, which highlight a critical paradox: CoT enhances interpretability but may undermine reliability in clinical text tasks. This work provides an empirical basis for clinical reasoning strategies of LLMs, highlighting the need for transparent and trustworthy approaches.

