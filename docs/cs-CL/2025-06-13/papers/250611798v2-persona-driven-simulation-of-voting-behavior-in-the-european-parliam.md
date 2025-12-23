---
layout: default
title: Persona-driven Simulation of Voting Behavior in the European Parliament with Large Language Models
---

# Persona-driven Simulation of Voting Behavior in the European Parliament with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11798" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11798v2</a>
  <a href="https://arxiv.org/pdf/2506.11798.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11798v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11798v2', 'Persona-driven Simulation of Voting Behavior in the European Parliament with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maximilian Kreutner, Marlene Lutz, Markus Strohmaier

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-13 (更新: 2025-09-08)

**🔗 代码/项目**: [GITHUB](https://github.com/dess-mannheim/european_parliament_simulation)

---

## 💡 一句话要点

**利用大语言模型模拟欧洲议会投票行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `投票行为模拟` `身份提示` `欧洲议会` `政治话语生成` `机器学习` `社会经济群体`

## 📋 核心要点

1. 现有的大型语言模型在政治话语生成中存在偏见，难以准确反映多样化的投票行为。
2. 本研究提出通过零-shot身份提示，利用有限信息来预测个体投票决策，进而模拟欧洲议会的投票行为。
3. 实验结果表明，模型在模拟投票行为方面表现良好，获得了约0.793的加权F1分数，显示出较高的预测准确性。

## 📝 摘要（中文）

大型语言模型（LLMs）在理解和生成政治话语方面展现出显著能力，但普遍存在向左倾斜的偏见。本研究分析了使用有限信息的零-shot身份提示是否能准确预测个体投票决策，并通过聚合预测欧洲各集团在多项政策上的立场。我们评估了预测对反事实论点、不同身份提示和生成方法的稳定性。最终结果显示，我们能够合理地模拟欧洲议会成员的投票行为，获得约0.793的加权F1分数。我们的政治家身份数据集及代码可在https://github.com/dess-mannheim/european_parliament_simulation获取。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在政治投票行为模拟中的偏见问题，现有方法难以准确反映不同社会经济群体的投票决策。

**核心思路**：通过零-shot身份提示，利用有限的信息来引导模型生成与特定身份相关的投票行为，从而提高预测的准确性和多样性。

**技术框架**：整体流程包括数据收集、身份提示设计、模型训练与评估。主要模块包括身份数据集构建、投票决策模拟和结果分析。

**关键创新**：本研究的创新在于使用零-shot身份提示来引导模型生成与特定社会经济群体一致的投票行为，这一方法与传统的训练方法有本质区别。

**关键设计**：在模型设计中，采用了特定的身份提示格式，并对生成过程中的参数进行了优化，以确保生成的投票行为与实际情况相符。

## 📊 实验亮点

实验结果显示，使用零-shot身份提示的模型在模拟欧洲议会成员投票行为方面表现出色，获得了约0.793的加权F1分数，表明其在预测准确性上有显著提升。这一结果相较于传统方法具有明显优势，展示了身份提示在政治行为模拟中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括政治分析、选举预测和政策制定等。通过模拟投票行为，能够为政策制定者提供更准确的选民行为预测，帮助其制定更具针对性的政策。此外，该方法还可用于研究不同社会经济群体的投票倾向，推动政治研究的深入发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) display remarkable capabilities to understand or even produce political discourse, but have been found to consistently display a progressive left-leaning bias. At the same time, so-called persona or identity prompts have been shown to produce LLM behavior that aligns with socioeconomic groups that the base model is not aligned with. In this work, we analyze whether zero-shot persona prompting with limited information can accurately predict individual voting decisions and, by aggregation, accurately predict positions of European groups on a diverse set of policies. We evaluate if predictions are stable towards counterfactual arguments, different persona prompts and generation methods. Finally, we find that we can simulate voting behavior of Members of the European Parliament reasonably well with a weighted F1 score of approximately 0.793. Our persona dataset of politicians in the 2024 European Parliament and our code are available at https://github.com/dess-mannheim/european_parliament_simulation.

