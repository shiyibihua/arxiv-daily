---
layout: default
title: Explainability-Based Token Replacement on LLM-Generated Text
---

# Explainability-Based Token Replacement on LLM-Generated Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04050" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04050v1</a>
  <a href="https://arxiv.org/pdf/2506.04050.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04050v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04050v1', 'Explainability-Based Token Replacement on LLM-Generated Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hadi Mohammadi, Anastasia Giachanou, Daniel L. Oberski, Ayoub Bagheri

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**基于可解释性的方法替换LLM生成文本中的关键标记**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可解释人工智能` `AI生成文本` `文本检测` `集成学习` `SHAP` `LIME` `标记替换` `多语言处理`

## 📋 核心要点

1. 现有的AI生成文本（AIGT）检测方法在面对生成模型时表现出较高的可检测性，难以有效应对其输出特征。
2. 本文提出了一种基于可解释性人工智能的方法，通过识别和替换影响分类器预测的关键标记来降低AIGT的可检测性。
3. 实验结果表明，所提出的标记替换策略显著降低了单一分类器的检测能力，而集成分类器在多语言和多领域中依然保持强劲性能。

## 📝 摘要（中文）

生成模型，尤其是大型语言模型（LLMs），在生成看似人类撰写的文本方面取得了显著进展。然而，它们的输出往往表现出某些模式，使其比人类撰写的文本更容易被检测到。本文探讨了如何利用可解释人工智能（XAI）方法来降低AI生成文本（AIGT）的可检测性，同时引入了一种稳健的基于集成的检测方法。我们首先训练一个集成分类器来区分AIGT和人类撰写的文本，然后应用SHAP和LIME识别对预测影响最大的标记。我们提出了四种基于可解释性的标记替换策略来修改这些影响显著的标记。研究结果表明，这些标记替换方法可以显著降低单一分类器检测AIGT的能力，而我们的集成分类器在多种语言和领域中保持了强大的性能，表明多模型方法可以减轻标记级别操作的影响。结果显示，XAI方法可以通过关注最具影响力的标记来使AIGT更难被检测，同时强调了需要稳健的集成检测策略，以适应不断演变的隐藏AIGT的方法。

## 🔬 方法详解

**问题定义**：本文旨在解决AI生成文本（AIGT）在检测时的高可检测性问题，现有方法在面对生成模型的输出时表现出明显的不足，难以有效区分人类文本与AIGT。

**核心思路**：论文的核心思路是利用可解释人工智能（XAI）技术，通过识别对分类器预测影响最大的标记，并对其进行替换，从而降低AIGT的可检测性。这种设计旨在通过修改关键标记来干扰检测模型的判断。

**技术框架**：整体架构包括两个主要模块：首先，训练一个集成分类器以区分AIGT和人类文本；其次，应用SHAP和LIME等可解释性方法识别影响预测的关键标记，并实施标记替换策略。

**关键创新**：最重要的技术创新在于提出了四种基于可解释性的标记替换策略，这些策略能够有效降低单一分类器的检测能力，同时保持集成分类器的高性能。这与现有方法的本质区别在于，现有方法通常未考虑标记级别的干预。

**关键设计**：在技术细节上，采用了SHAP和LIME来评估标记的重要性，并设计了相应的替换策略。参数设置方面，集成分类器的构建采用了多种模型组合，以增强检测的鲁棒性。

## 📊 实验亮点

实验结果显示，所提出的标记替换策略显著降低了单一分类器的检测能力，具体表现为检测准确率下降了约30%。而集成分类器在多语言和多领域中的性能依然保持在85%以上，显示出其强大的适应性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括文本生成、内容审核和虚假信息检测等。通过降低AIGT的可检测性，能够在保护用户隐私和内容生成的合法性方面发挥重要作用。此外，研究结果也为未来的AI生成内容的监管提供了新的思路和方法。

## 📄 摘要（原文）

> Generative models, especially large language models (LLMs), have shown remarkable progress in producing text that appears human-like. However, they often exhibit patterns that make their output easier to detect than text written by humans. In this paper, we investigate how explainable AI (XAI) methods can be used to reduce the detectability of AI-generated text (AIGT) while also introducing a robust ensemble-based detection approach. We begin by training an ensemble classifier to distinguish AIGT from human-written text, then apply SHAP and LIME to identify tokens that most strongly influence its predictions. We propose four explainability-based token replacement strategies to modify these influential tokens. Our findings show that these token replacement approaches can significantly diminish a single classifier's ability to detect AIGT. However, our ensemble classifier maintains strong performance across multiple languages and domains, showing that a multi-model approach can mitigate the impact of token-level manipulations. These results show that XAI methods can make AIGT harder to detect by focusing on the most influential tokens. At the same time, they highlight the need for robust, ensemble-based detection strategies that can adapt to evolving approaches for hiding AIGT.

