---
layout: default
title: Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?
---

# Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19467" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19467v2</a>
  <a href="https://arxiv.org/pdf/2506.19467.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19467v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19467v2', 'Can Reasoning Help Large Language Models Capture Human Annotator Disagreement?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingwei Ni, Yu Fan, Vilém Zouhar, Donya Rooein, Alexander Hoyle, Mrinmaya Sachan, Markus Leippold, Dirk Hovy, Elliott Ash

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-24 (更新: 2025-08-04)

**备注**: Preprint Under Review

---

## 💡 一句话要点

**研究表明推理方法对大语言模型捕捉人类标注者分歧的影响**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `人类标注` `推理方法` `分歧建模` `自然语言处理` `机器学习` `强化学习`

## 📋 核心要点

1. 现有方法在捕捉人类标注者的分歧时存在不足，尤其是RLVR推理未能有效建模这种变异。
2. 论文提出通过系统评估不同推理设置，探索其对LLM分歧建模的影响，特别关注简单思维链推理的效果。
3. 实验结果表明，RLVR推理降低了分歧建模的性能，而简单思维链推理显著提升了基于人类反馈的LLM的表现。

## 📝 摘要（中文）

人类标注中的变异（即分歧）在自然语言处理（NLP）中很常见，通常反映了任务的主观性和样本的模糊性。建模这种变异对敏感于此信息的应用至关重要。尽管RLVR风格的推理（可验证奖励的强化学习）在许多任务上提升了大语言模型（LLM）的性能，但尚不清楚这种推理是否能帮助LLM捕捉人类标注的有意义变异。本文评估了不同推理设置对LLM分歧建模的影响，系统地评估了模型规模、分布表达方法和引导方法下的每种推理设置，结果显示RLVR风格的推理在分歧建模中降低了性能，而简单的思维链（CoT）推理则提升了基于人类反馈的RLHF LLM的性能。这些发现强调了在分歧重要时用推理LLM替代人类标注者的潜在风险。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在捕捉人类标注者分歧时的不足，现有的RLVR推理方法未能有效建模这种变异，导致性能下降。

**核心思路**：通过系统评估不同的推理设置，特别是比较RLVR推理与简单思维链推理（CoT），以探讨其对LLM分歧建模的影响。

**技术框架**：研究设计了60个实验设置，涵盖3个任务，评估了不同模型规模、分布表达方法和引导方法下的推理效果。

**关键创新**：最重要的创新在于发现RLVR推理在分歧建模中反而降低了性能，而简单思维链推理则能有效提升基于人类反馈的LLM的表现，这与现有方法的预期效果截然相反。

**关键设计**：实验中对模型规模、推理方法和引导策略进行了细致的参数设置，确保了评估的全面性和结果的可靠性。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，RLVR推理在分歧建模中导致性能下降，而简单思维链推理使基于人类反馈的LLM性能提升，具体提升幅度未在摘要中给出，但这一发现对推理方法的选择具有重要指导意义。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的标注任务、情感分析和文本生成等。通过更好地理解人类标注者的分歧，LLM可以在处理主观性和模糊性较高的任务时提供更准确的结果，未来可能推动更智能的自动标注系统的发展。

## 📄 摘要（原文）

> Variation in human annotation (i.e., disagreements) is common in NLP, often reflecting important information like task subjectivity and sample ambiguity. Modeling this variation is important for applications that are sensitive to such information. Although RLVR-style reasoning (Reinforcement Learning with Verifiable Rewards) has improved Large Language Model (LLM) performance on many tasks, it remains unclear whether such reasoning enables LLMs to capture informative variation in human annotation. In this work, we evaluate the influence of different reasoning settings on LLM disagreement modeling. We systematically evaluate each reasoning setting across model sizes, distribution expression methods, and steering methods, resulting in 60 experimental setups across 3 tasks. Surprisingly, our results show that RLVR-style reasoning degrades performance in disagreement modeling, while naive Chain-of-Thought (CoT) reasoning improves the performance of RLHF LLMs (RL from human feedback). These findings underscore the potential risk of replacing human annotators with reasoning LLMs, especially when disagreements are important.

