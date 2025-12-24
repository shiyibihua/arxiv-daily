---
layout: default
title: Can You Trick the Grader? Adversarial Persuasion of LLM Judges
---

# Can You Trick the Grader? Adversarial Persuasion of LLM Judges

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07805" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07805v1</a>
  <a href="https://arxiv.org/pdf/2508.07805.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07805v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07805v1', 'Can You Trick the Grader? Adversarial Persuasion of LLM Judges')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yerin Hwang, Dongryeol Lee, Taegwan Kang, Yongil Kim, Kyomin Jung

**分类**: cs.CL

**发布日期**: 2025-08-11

**备注**: 19 pages, 8 figures

---

## 💡 一句话要点

**揭示语言模型评估中的说服性偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `自动评估` `说服技巧` `数学推理` `评分偏见` `亚里士多德修辞` `模型脆弱性`

## 📋 核心要点

1. 核心问题：现有的语言模型在数学推理任务中可能受到说服性语言的影响，导致评分不公正。
2. 方法要点：本文提出了七种说服技巧，并通过嵌入这些技巧来评估其对语言模型评分的影响。
3. 实验或效果：实验表明，使用说服性语言可以使错误解答的评分平均提高8%，且模型规模的增加未能有效缓解这一问题。

## 📝 摘要（中文）

随着大型语言模型在实际应用中作为自动评估者的角色日益增加，本文首次揭示了嵌入策略性说服语言可能导致语言模型评估者在数学推理任务中给予不公正高分的现象。基于亚里士多德的修辞原则，研究形式化了七种说服技巧，并在相同的回答中嵌入这些技巧。实验结果显示，使用说服性语言会导致语言模型评估者对错误解答的评分平均提高8%，其中一致性技巧造成的偏差最为严重。增加模型规模并未显著减轻这种脆弱性，且多种说服技巧的结合会进一步放大偏见，表明在评估过程中存在重要的脆弱性，亟需对抗说服性攻击的有效防御措施。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学推理任务中可能受到说服性语言影响而导致评分不公正的问题。现有方法未能有效识别和抵御这种偏见，造成评估结果的不可靠性。

**核心思路**：研究通过形式化七种说服技巧，探讨其在相同回答中嵌入的效果，揭示语言模型在评估时的脆弱性。这样的设计旨在系统性地分析说服语言对评分的影响。

**技术框架**：整体架构包括对七种说服技巧的定义与嵌入，随后在六个数学基准上进行评估。主要模块包括说服技巧的实现、模型评分的收集与分析。

**关键创新**：最重要的创新点在于首次系统性地揭示了说服性语言对语言模型评估的影响，尤其是不同技巧的组合如何放大评分偏见，这在现有文献中尚未被充分探讨。

**关键设计**：研究中使用了标准的数学推理任务作为基准，设计了相应的实验流程，确保了说服技巧的有效嵌入与评估，且对比了不同模型规模的表现。

## 📊 实验亮点

实验结果显示，使用说服性语言的错误解答评分平均提高8%，且一致性技巧造成的偏差最为显著。增加模型规模未能有效减轻这种偏见，表明当前评估系统存在重要的脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、自动评分系统及其他依赖于语言模型进行评估的场景。通过识别和理解说服性语言的影响，可以为未来的评估系统设计提供重要的参考，增强其公正性和可靠性。

## 📄 摘要（原文）

> As large language models take on growing roles as automated evaluators in practical settings, a critical question arises: Can individuals persuade an LLM judge to assign unfairly high scores? This study is the first to reveal that strategically embedded persuasive language can bias LLM judges when scoring mathematical reasoning tasks, where correctness should be independent of stylistic variation. Grounded in Aristotle's rhetorical principles, we formalize seven persuasion techniques (Majority, Consistency, Flattery, Reciprocity, Pity, Authority, Identity) and embed them into otherwise identical responses. Across six math benchmarks, we find that persuasive language leads LLM judges to assign inflated scores to incorrect solutions, by up to 8% on average, with Consistency causing the most severe distortion. Notably, increasing model size does not substantially mitigate this vulnerability. Further analysis demonstrates that combining multiple persuasion techniques amplifies the bias, and pairwise evaluation is likewise susceptible. Moreover, the persuasive effect persists under counter prompting strategies, highlighting a critical vulnerability in LLM-as-a-Judge pipelines and underscoring the need for robust defenses against persuasion-based attacks.

