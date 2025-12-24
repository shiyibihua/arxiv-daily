---
layout: default
title: Self-Exploring Language Models for Explainable Link Forecasting on Temporal Graphs via Reinforcement Learning
---

# Self-Exploring Language Models for Explainable Link Forecasting on Temporal Graphs via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00975" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00975v2</a>
  <a href="https://arxiv.org/pdf/2509.00975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00975v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00975v2', 'Self-Exploring Language Models for Explainable Link Forecasting on Temporal Graphs via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zifeng Ding, Shenyang Huang, Zeyu Cao, Emma Kondrup, Zachary Yang, Xingyue Huang, Yuan Sui, Zhangdie Yuan, Yuqicheng Zhu, Xianglong Hu, Yuan He, Farimah Poursafaei, Michael Bronstein, Andreas Vlachos

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-08-31 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出ReaL-TG框架以实现可解释的时间图链接预测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间图` `链接预测` `可解释性` `强化学习` `大型语言模型`

## 📋 核心要点

1. 现有的时间图链接预测方法缺乏可解释性，且在未见图上无法直接应用，限制了其实际应用。
2. 本文提出的ReaL-TG框架通过强化学习微调LLMs，旨在实现可解释的链接预测，并鼓励模型自我探索推理策略。
3. 实验结果显示，ReaL-TG-4B在排名指标上超越了更大的LLMs，并生成了高质量的解释，得到了评判系统和人类评估的认可。

## 📝 摘要（中文）

链接预测是时间图推理中的核心任务，需要模型利用历史交互来预测即将发生的链接。传统的神经网络方法，如时间图神经网络，虽然表现良好，但缺乏可解释性，并且在未见图上无法应用而无需重新训练。近期研究开始探索使用大型语言模型（LLMs）进行图推理，但大多数研究局限于静态图或小型合成时间图，且缺乏对LLM生成的推理轨迹质量的评估。本文提出了基于强化学习的时间图推理增强学习框架（ReaL-TG），该框架微调LLMs以在真实世界的时间图上执行可解释的链接预测。ReaL-TG使用基于结果的奖励，鼓励模型自我探索图结构中的推理策略，并生成直接证明其预测的解释。我们还提出了一种新的评估协议，结合排名指标与LLM评判系统，评估推理质量及幻觉影响。实验结果表明，ReaL-TG-4B在排名指标上优于更大的前沿LLMs，并生成高质量的解释，得到了LLM评判和人工评估的确认。

## 🔬 方法详解

**问题定义**：本文解决的具体问题是如何在时间图上进行可解释的链接预测。现有方法如时间图神经网络虽然表现良好，但缺乏可解释性，且在未见图上无法应用，导致其在实际场景中的局限性。

**核心思路**：论文的核心解决思路是通过强化学习框架（ReaL-TG）微调大型语言模型，以实现可解释的链接预测。通过使用基于结果的奖励机制，模型能够自我探索推理策略，并生成能够解释其预测的理由。

**技术框架**：ReaL-TG的整体架构包括数据输入模块、LLM微调模块和评估模块。数据输入模块负责处理时间图数据，LLM微调模块则通过强化学习进行模型训练，评估模块则用于评估生成的推理轨迹的质量。

**关键创新**：最重要的技术创新点在于结合了强化学习与大型语言模型的微调，能够在真实世界的时间图上进行可解释的链接预测。这与传统方法的静态性和缺乏自我解释能力形成了鲜明对比。

**关键设计**：在关键设计方面，使用了基于结果的奖励机制来引导模型探索推理策略，同时设计了新的评估协议，结合排名指标与LLM评判系统，以全面评估推理质量和幻觉影响。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，ReaL-TG-4B在排名指标上超越了更大的前沿LLMs，如GPT-5 mini，且在生成的解释质量上得到了LLM评判和人类评估的高度认可，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括社交网络分析、交通流量预测和金融交易网络等。通过实现可解释的链接预测，ReaL-TG能够帮助决策者理解模型的预测依据，从而在实际应用中提高决策的透明度和可靠性。未来，该方法可能会推动更多领域的图推理研究，促进智能系统的可解释性发展。

## 📄 摘要（原文）

> Forecasting future links is a central task in temporal graph (TG) reasoning, requiring models to leverage historical interactions to predict upcoming ones. Traditional neural approaches, such as temporal graph neural networks, achieve strong performance but lack explainability and cannot be applied to unseen graphs without retraining. Recent studies have begun to explore using large language models (LLMs) for graph reasoning, but most of them are constrained to static graphs or small synthetic TGs and lack the evaluation of the quality of reasoning traces generated by LLMs. In this work, we present Reasoning-Enhanced Learning for Temporal Graphs (ReaL-TG), a reinforcement learning framework that fine-tunes LLMs to perform explainable link forecasting on real-world TGs. ReaL-TG uses outcome-based reward to encourage models to self-explore reasoning strategies from graph structure and to produce explanations that directly justify their predictions. To enable evaluation on LLM-generated reasoning traces, we propose a new evaluation protocol combining ranking metrics with an LLM-as-a-Judge system that assesses both the quality of reasoning and the impact of hallucinations. Experiments with ReaL-TG-4B, obtained by fine-tuning Qwen3-4B under our framework, show that it outperforms much larger frontier LLMs, including GPT-5 mini, on ranking metrics, while producing high-quality explanations confirmed by both the LLM judge and human evaluation.

