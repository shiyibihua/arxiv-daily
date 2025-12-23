---
layout: default
title: Do LLMs Really Forget? Evaluating Unlearning with Knowledge Correlation and Confidence Awareness
---

# Do LLMs Really Forget? Evaluating Unlearning with Knowledge Correlation and Confidence Awareness

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05735" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05735v4</a>
  <a href="https://arxiv.org/pdf/2506.05735.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05735v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05735v4', 'Do LLMs Really Forget? Evaluating Unlearning with Knowledge Correlation and Confidence Awareness')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rongzhe Wei, Peizhi Niu, Hans Hao-Hsun Hsu, Ruihan Wu, Haoteng Yin, Mohsen Ghassemi, Yifan Li, Vamsi K. Potluru, Eli Chien, Kamalika Chaudhuri, Olgica Milenkovic, Pan Li

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-06 (更新: 2025-10-22)

**备注**: NeurIPS Camera-Ready Version. Code available at: https://github.com/Graph-COM/Knowledge_Unlearning

**🔗 代码/项目**: [GITHUB](https://github.com/Graph-COM/Knowledge_Unlearning.git)

---

## 💡 一句话要点

**提出知识去学习评估框架以解决大语言模型遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识去学习` `大语言模型` `知识图谱` `评估框架` `推理评估` `置信度评分` `隐性知识`

## 📋 核心要点

1. 现有的去学习方法主要关注显式删除孤立事实，忽视了知识的潜在推理依赖和非确定性特征。
2. 本文提出了一种知识去学习评估框架，通过知识图谱和置信度分数更准确地捕捉知识结构。
3. 实验结果显示，该框架提供了更严格的评估，揭示了现有策略高估去学习效果的问题。

## 📝 摘要（中文）

机器去学习技术旨在减轻大语言模型（LLMs）中的意外记忆。然而，现有方法主要集中于显式删除孤立事实，往往忽视潜在的推理依赖关系和LLMs中知识的非确定性特征。因此，假定被遗忘的事实可能通过相关信息隐性存在。为了解决这些挑战，本文提出了一种知识去学习评估框架，通过将相关事实上下文表示为知识图谱并附加置信度分数，更准确地捕捉现实世界知识的隐含结构。我们进一步开发了一种基于推理的评估协议，利用强大的LLMs作为评判者，评估去学习的成功率。实验表明，该框架提供了更现实和严格的去学习性能评估，并揭示了当前评估策略往往高估了去学习的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型中知识去学习的评估问题，现有方法往往忽视了知识的隐性依赖关系，导致评估结果不准确。

**核心思路**：提出了一种基于知识图谱的评估框架，通过将相关事实上下文表示为图谱，并结合置信度分数，来更全面地捕捉知识的隐含结构。

**技术框架**：整体架构包括知识图谱构建模块、置信度评分模块和基于推理的评估协议，利用LLMs作为评判者进行知识去学习的效果评估。

**关键创新**：最重要的创新在于引入知识图谱和置信度分数的结合，能够更准确地反映知识的隐性结构，与现有方法的显式删除策略形成鲜明对比。

**关键设计**：在设计中，采用了精心设计的提示语以引导LLMs进行推理，并通过与人类评估的校准来确保评判的可靠性和稳定性。实验中构建了新的基准数据集以验证框架的有效性。

## 📊 实验亮点

实验结果表明，提出的评估框架在去学习性能评估上显著优于现有方法，能够更真实地反映模型的遗忘效果。具体而言，评估结果显示当前策略高估了去学习的有效性，提供了更为严谨的评估标准。

## 🎯 应用场景

该研究的潜在应用领域包括大语言模型的安全性和可靠性评估，尤其是在涉及敏感信息的场景中。通过改进的去学习评估框架，可以更有效地管理和控制模型的知识记忆，提升模型在实际应用中的安全性和可信度。

## 📄 摘要（原文）

> Machine unlearning techniques aim to mitigate unintended memorization in large language models (LLMs). However, existing approaches predominantly focus on the explicit removal of isolated facts, often overlooking latent inferential dependencies and the non-deterministic nature of knowledge within LLMs. Consequently, facts presumed forgotten may persist implicitly through correlated information. To address these challenges, we propose a knowledge unlearning evaluation framework that more accurately captures the implicit structure of real-world knowledge by representing relevant factual contexts as knowledge graphs with associated confidence scores. We further develop an inference-based evaluation protocol leveraging powerful LLMs as judges; these judges reason over the extracted knowledge subgraph to determine unlearning success. Our LLM judges utilize carefully designed prompts and are calibrated against human evaluations to ensure their trustworthiness and stability. Extensive experiments on our newly constructed benchmark demonstrate that our framework provides a more realistic and rigorous assessment of unlearning performance. Moreover, our findings reveal that current evaluation strategies tend to overestimate unlearning effectiveness. Our code is publicly available at https://github.com/Graph-COM/Knowledge_Unlearning.git.

