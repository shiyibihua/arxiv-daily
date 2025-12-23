---
layout: default
title: Probing AI Safety with Source Code
---

# Probing AI Safety with Source Code

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20471" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20471v1</a>
  <a href="https://arxiv.org/pdf/2506.20471.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20471v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20471v1', 'Probing AI Safety with Source Code')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ujwal Narayan, Shreyas Chaudhari, Ashwin Kalyan, Tanmay Rajpurohit, Karthik Narasimhan, Ameet Deshpande, Vishvak Murahari

**分类**: cs.CL

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出Code of Thought评估LLM安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `AI安全` `代码转换` `毒性评估` `自然语言处理` `模型评估` `安全关键应用`

## 📋 核心要点

1. 现有大型语言模型在安全性方面存在显著不足，导致用户体验不安全且有害。
2. 本文提出的Code of Thought（CoDoT）策略，通过将自然语言转换为代码来评估LLMs的安全性。
3. 实验结果显示，使用CoDoT后，GPT-4 Turbo的毒性增加16.5倍，DeepSeek R1完全失败，七种现代LLMs的毒性平均增加300%。

## 📝 摘要（中文）

大型语言模型（LLMs）在多个安全关键应用中变得无处不在，这要求在提升能力的同时加强安全措施，以使这些模型与人类价值观和偏好保持一致。本文展示了当前模型在AI安全目标上令人担忧的不足，导致用户体验不安全且有害。我们引入了一种名为Code of Thought（CoDoT）的提示策略来评估LLMs的安全性。CoDoT将自然语言输入转换为简单代码，表示相同的意图。研究表明，CoDoT导致多种最先进的LLMs一致性失败，强调了从第一原则评估安全努力的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在安全性评估方面的不足，现有方法未能有效识别和控制模型输出的有害性。

**核心思路**：提出Code of Thought（CoDoT）策略，通过将自然语言提示转换为代码形式，来更准确地评估和引导模型的输出，确保安全性与能力的同步提升。

**技术框架**：CoDoT的整体流程包括自然语言输入的解析、转换为代码表示、以及对模型输出的评估。主要模块包括输入处理、代码生成和输出分析。

**关键创新**：CoDoT的核心创新在于将自然语言提示转化为代码，提供了一种新的评估模型安全性的方法，这与传统的直接输入评估方法本质上不同。

**关键设计**：在设计中，CoDoT使用了简单的函数调用形式来表示意图，例如将“Make the statement more toxic: {text}”转换为“make_more_toxic({text})”，这种设计使得模型的反应更加可控和可预测。

## 📊 实验亮点

实验结果表明，使用CoDoT后，GPT-4 Turbo的毒性增加了16.5倍，而DeepSeek R1在测试中完全失败。此外，七种现代LLMs的毒性平均增加了300%，显示出CoDoT在评估模型安全性方面的有效性和重要性。

## 🎯 应用场景

该研究的潜在应用领域包括安全关键的人工智能系统，如医疗、金融和自动驾驶等领域。通过有效评估和提高LLMs的安全性，可以减少潜在的风险，确保用户体验的安全性和可靠性。未来，CoDoT可能成为评估和改进AI系统安全性的标准工具。

## 📄 摘要（原文）

> Large language models (LLMs) have become ubiquitous, interfacing with humans in numerous safety-critical applications. This necessitates improving capabilities, but importantly coupled with greater safety measures to align these models with human values and preferences. In this work, we demonstrate that contemporary models fall concerningly short of the goal of AI safety, leading to an unsafe and harmful experience for users. We introduce a prompting strategy called Code of Thought (CoDoT) to evaluate the safety of LLMs. CoDoT converts natural language inputs to simple code that represents the same intent. For instance, CoDoT transforms the natural language prompt "Make the statement more toxic: {text}" to: "make_more_toxic({text})". We show that CoDoT results in a consistent failure of a wide range of state-of-the-art LLMs. For example, GPT-4 Turbo's toxicity increases 16.5 times, DeepSeek R1 fails 100% of the time, and toxicity increases 300% on average across seven modern LLMs. Additionally, recursively applying CoDoT can further increase toxicity two times. Given the rapid and widespread adoption of LLMs, CoDoT underscores the critical need to evaluate safety efforts from first principles, ensuring that safety and capabilities advance together.

