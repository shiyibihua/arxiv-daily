---
layout: default
title: From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment
---

# From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16532" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16532v1</a>
  <a href="https://arxiv.org/pdf/2512.16532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16532v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16532v1', 'From Personalization to Prejudice: Bias and Discrimination in Memory-Enhanced AI Agents for Recruitment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Himanshu Gharat, Himanshi Agrawal, Gourab K. Patro

**分类**: cs.AI, cs.IR

**发布日期**: 2025-12-18

**备注**: In Proceedings of the Nineteenth ACM International Conference on Web Search and Data Mining (WSDM '26)

**期刊**: In Proceedings of the Nineteenth ACM International Conference on Web Search and Data Mining (WSDM '26), 2026, Boise, ID, USA. ACM, New York, NY, USA

**DOI**: [10.1145/3773966.3779376](https://doi.org/10.1145/3773966.3779376)

---

## 💡 一句话要点

**揭示记忆增强型AI招聘Agent中的偏见引入与强化机制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `AI Agent` `记忆增强` `个性化` `偏见` `招聘` `公平性` `机器学习`

## 📋 核心要点

1. 现有研究较少关注记忆增强型AI Agent中的偏见问题，尤其是在个性化过程中偏见的引入和强化机制。
2. 该研究通过模拟招聘场景中的AI Agent行为，分析了偏见在Agent操作的各个阶段如何产生和演变。
3. 实验结果表明，即使使用安全训练的LLM，记忆增强型个性化仍然会导致偏见的系统性引入和强化。

## 📝 摘要（中文）

大型语言模型（LLMs）赋予了AI Agent强大的理解、推理和交互能力，使其能够胜任各种任务。通过添加记忆功能，AI Agent能够跨交互保持连贯性，从过去的经验中学习，并随着时间的推移提高行动和响应的相关性，从而实现记忆增强型个性化。虽然这种通过记忆实现的个性化具有明显的优势，但也带来了偏见风险。尽管之前的研究已经强调了ML和LLM中的偏见，但关于记忆增强型个性化Agent所带来的偏见在很大程度上尚未被探索。本文以招聘为例，模拟了记忆增强型个性化Agent的行为，并研究了偏见是如何在各个操作阶段被引入和强化的。对使用安全训练LLM的Agent进行的实验表明，偏见通过个性化被系统地引入和强化，强调了在基于记忆增强型LLM的AI Agent中采取额外保护措施或Agent防护措施的必要性。

## 🔬 方法详解

**问题定义**：论文旨在研究在招聘场景下，记忆增强型AI Agent在个性化过程中引入和强化偏见的问题。现有方法缺乏对这种偏见来源和演化过程的深入理解，难以有效缓解。

**核心思路**：论文的核心思路是通过模拟AI Agent在招聘过程中的行为，观察和分析Agent在与不同候选人交互后，其记忆中积累的经验如何影响后续的决策，从而揭示偏见的产生和强化机制。这种模拟方法能够控制实验变量，更清晰地观察偏见的影响。

**技术框架**：论文构建了一个模拟招聘环境，AI Agent与一系列模拟的候选人进行交互。Agent使用LLM作为其核心推理引擎，并配备记忆模块来存储交互历史。整个流程包括：候选人信息输入、Agent基于记忆和LLM进行评估、Agent给出招聘建议、Agent更新记忆。通过多次迭代，观察Agent的招聘偏好变化。

**关键创新**：该研究的关键创新在于关注了记忆增强型AI Agent在个性化过程中产生的偏见，并提出了一种模拟方法来研究这种偏见的产生和强化机制。与以往关注静态数据集偏见的研究不同，该研究关注的是Agent在动态交互过程中学习到的偏见。

**关键设计**：论文的关键设计包括：1) 使用安全训练的LLM作为Agent的核心，以降低LLM本身带来的偏见；2) 设计合理的记忆更新机制，模拟Agent如何从过去的经验中学习；3) 设计多种评估指标，量化Agent的招聘偏好，例如不同性别或种族候选人的录取率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16532v1/Figure_1_overview.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，即使使用经过安全训练的LLM，记忆增强型个性化仍然会导致偏见的系统性引入和强化。具体而言，Agent在与特定群体（例如，特定性别或种族）的候选人交互后，会逐渐形成对该群体的偏见，并在后续的招聘决策中体现出来。这表明，仅仅依靠LLM的安全训练不足以消除偏见，需要额外的保护措施。

## 🎯 应用场景

该研究成果可应用于各种需要个性化推荐或决策的AI系统中，例如金融信贷、教育评估等。通过理解和缓解记忆增强型AI Agent中的偏见，可以提高AI系统的公平性和可靠性，避免歧视性行为，从而促进社会公平。

## 📄 摘要（原文）

> Large Language Models (LLMs) have empowered AI agents with advanced capabilities for understanding, reasoning, and interacting across diverse tasks. The addition of memory further enhances them by enabling continuity across interactions, learning from past experiences, and improving the relevance of actions and responses over time; termed as memory-enhanced personalization. Although such personalization through memory offers clear benefits, it also introduces risks of bias. While several previous studies have highlighted bias in ML and LLMs, bias due to memory-enhanced personalized agents is largely unexplored. Using recruitment as an example use case, we simulate the behavior of a memory-enhanced personalized agent, and study whether and how bias is introduced and amplified in and across various stages of operation. Our experiments on agents using safety-trained LLMs reveal that bias is systematically introduced and reinforced through personalization, emphasizing the need for additional protective measures or agent guardrails in memory-enhanced LLM-based AI agents.

