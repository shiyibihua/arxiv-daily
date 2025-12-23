---
layout: default
title: Fine-Grained Interpretation of Political Opinions in Large Language Models
---

# Fine-Grained Interpretation of Political Opinions in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04774" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04774v1</a>
  <a href="https://arxiv.org/pdf/2506.04774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04774v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04774v1', 'Fine-Grained Interpretation of Political Opinions in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyu Hu, Mengyue Yang, Mengnan Du, Weiru Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出四维政治学习框架以解决LLMs政治意见分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `政治意见分析` `多维度学习` `可解释性` `表示工程` `向量学习` `干预机制`

## 📋 核心要点

1. 现有方法主要依赖开放式响应评估，导致LLMs的内部意图与外部表现不一致，难以准确分析其政治意见。
2. 本文提出四维政治学习框架，扩展单一维度概念为多维度，结合可解释的表示工程技术，提升政治概念学习的透明度。
3. 在八个开源LLMs上进行实验，结果显示所提向量能够有效解开政治概念混淆，并在不同政治倾向的生成任务中表现出良好的泛化能力。

## 📝 摘要（中文）

对大型语言模型（LLMs）政治意见的研究主要依赖于对其开放式响应的评估。近期研究表明，LLMs的响应与其内部意图之间存在不一致，这促使我们深入探讨LLMs的内部机制，以揭示其政治状态。此外，现有的政治意见分析往往依赖单一维度的概念，容易导致概念混淆。本文扩展了单一维度到多维度，并应用可解释的表示工程技术，以实现更透明的LLM政治概念学习。我们设计了一个四维政治学习框架，并构建了相应的数据集用于细粒度政治概念向量学习。这些向量可用于检测和干预LLMs的内部机制。实验结果表明，这些向量能够有效解开政治概念的混淆，并在OOD设置中展现出良好的泛化性和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在政治意见分析中的内部意图与外部表现不一致的问题。现有方法通常依赖单一维度的概念，导致概念混淆，难以准确捕捉LLMs的政治状态。

**核心思路**：我们提出了一个四维政治学习框架，通过扩展单一维度到多维度，结合可解释的表示工程技术，增强LLMs政治概念的学习和理解。这样的设计旨在提高模型的透明度和可解释性，帮助研究者更好地理解模型的内部机制。

**技术框架**：整体架构包括数据集构建、四维政治概念向量学习和干预机制。首先，构建一个包含多维度政治概念的数据集；其次，利用表示工程技术进行向量学习；最后，设计干预机制以生成不同政治倾向的响应。

**关键创新**：本文的主要创新在于提出了四维政治学习框架，突破了传统单一维度分析的局限，能够更全面地捕捉LLMs的政治状态。这一方法与现有方法的本质区别在于其多维度的视角和可解释性。

**关键设计**：在模型设计中，我们采用了多种表示工程技术，设置了适当的损失函数以优化向量学习效果。具体参数设置和网络结构设计旨在确保向量的语义一致性和可解释性。实验中使用的技术细节包括向量的维度选择和训练策略。

## 📊 实验亮点

实验结果表明，所提出的四维政治概念向量能够有效解开政治概念混淆，且在OOD设置中展现出良好的泛化性和鲁棒性。干预实验显示，这些向量能够成功引导LLMs生成具有不同政治倾向的响应，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括政治舆情分析、社交媒体内容监测及自动化新闻生成等。通过更准确地理解和干预LLMs的政治倾向，能够为政策制定、舆论引导等提供有价值的支持，未来可能在社会科学和人文领域产生深远影响。

## 📄 摘要（原文）

> Studies of LLMs' political opinions mainly rely on evaluations of their open-ended responses. Recent work indicates that there is a misalignment between LLMs' responses and their internal intentions. This motivates us to probe LLMs' internal mechanisms and help uncover their internal political states. Additionally, we found that the analysis of LLMs' political opinions often relies on single-axis concepts, which can lead to concept confounds. In this work, we extend the single-axis to multi-dimensions and apply interpretable representation engineering techniques for more transparent LLM political concept learning. Specifically, we designed a four-dimensional political learning framework and constructed a corresponding dataset for fine-grained political concept vector learning. These vectors can be used to detect and intervene in LLM internals. Experiments are conducted on eight open-source LLMs with three representation engineering techniques. Results show these vectors can disentangle political concept confounds. Detection tasks validate the semantic meaning of the vectors and show good generalization and robustness in OOD settings. Intervention Experiments show these vectors can intervene in LLMs to generate responses with different political leanings.

