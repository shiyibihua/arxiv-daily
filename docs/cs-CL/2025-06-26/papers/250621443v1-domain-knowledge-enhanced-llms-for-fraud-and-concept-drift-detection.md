---
layout: default
title: Domain Knowledge-Enhanced LLMs for Fraud and Concept Drift Detection
---

# Domain Knowledge-Enhanced LLMs for Fraud and Concept Drift Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21443" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21443v1</a>
  <a href="https://arxiv.org/pdf/2506.21443.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21443v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21443v1', 'Domain Knowledge-Enhanced LLMs for Fraud and Concept Drift Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Şenol, Garima Agrawal, Huan Liu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出领域知识增强的LLM框架以解决欺诈和概念漂移检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `欺诈检测` `概念漂移` `大型语言模型` `领域知识` `自然语言处理` `动态对话` `模型鲁棒性`

## 📋 核心要点

1. 现有方法在动态对话中难以应对语言模式的变化和概念漂移，导致欺诈检测的准确性下降。
2. 论文提出的领域知识增强LLM框架，通过结合预训练LLM与领域知识，提升了欺诈和概念漂移的检测能力。
3. 实验结果显示，该框架在SEConvo数据集上实现了98%的分类准确率，相较于零-shot基线显著提升了性能和可解释性。

## 📝 摘要（中文）

在动态平台上检测欺诈性对话变得愈发困难，主要由于语言模式的演变和概念漂移（CD），即语义或主题的变化，这些变化可能会模糊恶意意图或伪装成正常对话，导致准确分类的挑战。虽然大型语言模型（LLMs）在自然语言任务中表现出色，但在风险敏感场景中，它们常常面临上下文歧义和幻觉问题。为了解决这些挑战，本文提出了一种领域知识增强的LLM框架，将预训练的LLM与结构化的任务特定见解相结合，以进行欺诈和概念漂移检测。实验结果表明，系统在检测虚假对话和有效分类漂移方面具有高准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决在动态对话平台上检测欺诈性对话和概念漂移的问题。现有方法在应对语言模式变化和上下文歧义时表现不佳，导致分类准确性低下。

**核心思路**：论文提出的领域知识增强LLM框架，通过集成预训练的LLM与结构化的领域知识，增强了模型对欺诈和概念漂移的检测能力，旨在提高分类的准确性和鲁棒性。

**技术框架**：该框架由三个主要模块组成：1) DK-LLM模块用于检测虚假对话；2) 漂移检测单元（OCDD）用于判断语义漂移是否发生；3) 第二个DK-LLM模块用于将漂移分类为良性或欺诈性。

**关键创新**：最重要的创新在于将领域知识与LLM相结合，显著提升了模型在高风险NLP应用中的性能和可解释性。这一方法与传统的零-shot学习方法相比，能够更好地处理上下文变化。

**关键设计**：在模型设计中，采用了结构化提示来引导LLaMA模型的训练，确保了模型在特定任务上的有效性。实验中使用的损失函数和网络结构经过精心调整，以优化欺诈检测和漂移分类的效果。

## 📊 实验亮点

实验结果显示，基于LLaMA的实现达到了98%的分类准确率，较零-shot基线显著提升了性能。通过引入领域知识和漂移意识，系统在高风险NLP应用中表现出更好的可解释性和鲁棒性，展示了其在欺诈检测中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括在线评论监测、社交媒体对话分析和金融欺诈检测等。通过提高欺诈检测的准确性和鲁棒性，该框架能够在实际应用中有效识别恶意行为，保护用户安全，提升平台信任度。未来，该方法还可能扩展到其他需要实时监控和分析的动态对话场景。

## 📄 摘要（原文）

> Detecting deceptive conversations on dynamic platforms is increasingly difficult due to evolving language patterns and Concept Drift (CD)-i.e., semantic or topical shifts that alter the context or intent of interactions over time. These shifts can obscure malicious intent or mimic normal dialogue, making accurate classification challenging. While Large Language Models (LLMs) show strong performance in natural language tasks, they often struggle with contextual ambiguity and hallucinations in risk-sensitive scenarios. To address these challenges, we present a Domain Knowledge (DK)-Enhanced LLM framework that integrates pretrained LLMs with structured, task-specific insights to perform fraud and concept drift detection. The proposed architecture consists of three main components: (1) a DK-LLM module to detect fake or deceptive conversations; (2) a drift detection unit (OCDD) to determine whether a semantic shift has occurred; and (3) a second DK-LLM module to classify the drift as either benign or fraudulent. We first validate the value of domain knowledge using a fake review dataset and then apply our full framework to SEConvo, a multiturn dialogue dataset that includes various types of fraud and spam attacks. Results show that our system detects fake conversations with high accuracy and effectively classifies the nature of drift. Guided by structured prompts, the LLaMA-based implementation achieves 98% classification accuracy. Comparative studies against zero-shot baselines demonstrate that incorporating domain knowledge and drift awareness significantly improves performance, interpretability, and robustness in high-stakes NLP applications.

