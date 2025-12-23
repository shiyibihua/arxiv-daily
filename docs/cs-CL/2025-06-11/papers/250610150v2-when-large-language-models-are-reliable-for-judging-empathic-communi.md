---
layout: default
title: When Large Language Models are Reliable for Judging Empathic Communication
---

# When Large Language Models are Reliable for Judging Empathic Communication

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10150" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10150v2</a>
  <a href="https://arxiv.org/pdf/2506.10150.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10150v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10150v2', 'When Large Language Models are Reliable for Judging Empathic Communication')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aakriti Kumar, Nalin Poungpeth, Diyi Yang, Erina Farrell, Bruce Lambert, Matthew Groh

**分类**: cs.CL, cs.HC

**发布日期**: 2025-06-11 (更新: 2025-10-03)

---

## 💡 一句话要点

**评估大型语言模型在同理沟通判断中的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `同理沟通` `情感计算` `标注一致性` `自然语言处理` `心理学` `人机交互`

## 📋 核心要点

1. 核心问题：现有方法在判断同理沟通的细微差别时，缺乏可靠性评估标准，尤其是在情感敏感的对话场景中。
2. 方法要点：本文通过对比专家、众包工作者和LLMs的标注结果，评估不同评估框架下的同理沟通判断可靠性。
3. 实验或效果：研究表明，LLMs在同理沟通的判断上接近专家水平，且超越众包工作者的可靠性，提供了更具信息量的基准。

## 📝 摘要（中文）

大型语言模型（LLMs）在文本对话中生成同理反应方面表现出色，但它们在判断同理沟通细微差别的可靠性如何？本文通过比较专家、众包工作者和LLMs在200个真实对话中的同理沟通标注，探讨了这一问题。研究发现，专家之间的协议度较高，但在不同评估框架的子组件中存在差异。LLMs在所有四个框架中均接近专家水平，并超越了众包工作者的可靠性。这些结果表明，经过特定任务验证的LLMs可以在情感敏感应用中支持透明度和监督。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在同理沟通判断中的可靠性问题。现有方法缺乏有效的评估标准，导致对情感沟通的理解和应用存在挑战。

**核心思路**：通过比较专家、众包工作者和LLMs在同理沟通标注中的表现，提供一个多维度的评估框架，以更好地理解和验证LLMs的能力。

**技术框架**：研究采用四个评估框架，结合心理学、自然语言处理和传播学的理论，分析200个真实对话的同理沟通。主要模块包括数据收集、标注过程和结果分析。

**关键创新**：最重要的创新在于通过专家标注提供了一个更具信息量的基准，超越了传统分类指标，揭示了LLMs在特定任务中的潜力。

**关键设计**：在实验中，使用了3150个专家标注、2844个众包标注和3150个LLM标注，评估了不同框架下的协议度，关注标注的清晰度、复杂性和主观性等因素。

## 📊 实验亮点

实验结果显示，LLMs在同理沟通的判断上接近专家水平，且在所有四个评估框架中均超越了众包工作者的可靠性，提供了3150个专家标注和3150个LLM标注的高一致性，验证了其在情感应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括情感支持系统、智能客服和心理健康干预等。通过提高LLMs在同理沟通中的可靠性，可以增强其在情感敏感场景中的应用价值，促进人机交互的自然性和有效性。

## 📄 摘要（原文）

> Large language models (LLMs) excel at generating empathic responses in text-based conversations. But, how reliably do they judge the nuances of empathic communication? We investigate this question by comparing how experts, crowdworkers, and LLMs annotate empathic communication across four evaluative frameworks drawn from psychology, natural language processing, and communications applied to 200 real-world conversations where one speaker shares a personal problem and the other offers support. Drawing on 3,150 expert annotations, 2,844 crowd annotations, and 3,150 LLM annotations, we assess inter-rater reliability between these three annotator groups. We find that expert agreement is high but varies across the frameworks' sub-components depending on their clarity, complexity, and subjectivity. We show that expert agreement offers a more informative benchmark for contextualizing LLM performance than standard classification metrics. Across all four frameworks, LLMs consistently approach this expert level benchmark and exceed the reliability of crowdworkers. These results demonstrate how LLMs, when validated on specific tasks with appropriate benchmarks, can support transparency and oversight in emotionally sensitive applications including their use as conversational companions.

