---
layout: default
title: Self-correcting Reward Shaping via Language Models for Reinforcement Learning Agents in Games
---

# Self-correcting Reward Shaping via Language Models for Reinforcement Learning Agents in Games

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23626" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23626v1</a>
  <a href="https://arxiv.org/pdf/2506.23626.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23626v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23626v1', 'Self-correcting Reward Shaping via Language Models for Reinforcement Learning Agents in Games')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: António Afonso, Iolanda Leite, Alessandro Sestini, Florian Fuchs, Konrad Tollmar, Linus Gisslén

**分类**: cs.AI

**发布日期**: 2025-06-30

**备注**: 16 pages in total, 10 pages of main paper, 5 figures

---

## 💡 一句话要点

**提出自校正奖励塑形方法以解决强化学习代理的奖励设计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `奖励塑形` `语言模型` `自动化调优` `游戏代理` `自我校正` `性能提升`

## 📋 核心要点

1. 现有的强化学习代理在游戏中部署时，设计有效的奖励函数通常需要专家的参与，且在游戏内容变化后，原有的奖励权重可能失效。
2. 本文提出了一种基于语言模型的自动化方法，通过用户定义的行为目标，迭代调整RL代理的奖励函数权重，减少手动干预。
3. 在赛车任务中，LM引导的代理在一次迭代中成功率提升至74%，最终达到80%的成功率，表现与专家调优的代理相当。

## 📝 摘要（中文）

近年来，游戏中的强化学习（RL）取得了显著进展，能够创造出不同的代理行为，改变玩家的游戏体验。然而，在生产环境中部署RL代理面临两个主要挑战：设计有效的奖励函数通常需要RL专家的参与，以及当游戏内容或机制发生变化时，之前调优的奖励权重可能不再最佳。为了解决后一个挑战，本文提出了一种自动化方法，通过用户定义的基于语言的行为目标，迭代微调RL代理的奖励函数权重。语言模型（LM）在每次迭代中根据目标行为和先前训练轮次的性能统计摘要提出更新的权重。这个闭环过程使得LM能够自我校正并随着时间推移不断优化输出，产生越来越一致的行为，而无需手动奖励工程。我们在赛车任务中评估了该方法，结果显示代理性能在迭代中持续提升。LM引导的代理在一次迭代中成功率从9%提升至74%。与人类专家的手动权重设计相比，LM调优的代理在最终迭代中达到了80%的成功率，平均完成圈数为855个时间步，表现与专家调优代理的最高94%成功率和850个时间步相当。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习代理在游戏中部署时，奖励函数设计的复杂性和游戏内容变化导致的奖励权重失效问题。现有方法通常依赖于专家的手动调优，效率低下且不够灵活。

**核心思路**：论文提出通过语言模型（LM）自动化奖励权重的微调过程，利用用户定义的行为目标和历史性能数据，使得代理能够自我校正，逐步优化其行为。

**技术框架**：整体架构包括用户定义的行为目标输入、LM生成的奖励权重更新、以及基于性能统计的反馈循环。每次迭代中，LM根据目标行为和先前训练结果提出新的权重，形成闭环优化过程。

**关键创新**：最重要的创新在于将语言模型应用于奖励塑形，使得RL代理能够在没有手动干预的情况下，自主调整和优化其行为策略。这种方法显著提高了代理的适应性和性能。

**关键设计**：在设计中，LM的输入包括用户定义的行为目标和历史训练数据，输出为更新的奖励权重。损失函数和网络结构的具体细节未在摘要中详细说明，需参考论文的完整内容以获取更多信息。

## 📊 实验亮点

实验结果显示，LM引导的代理在一次迭代中成功率从9%提升至74%，最终成功率达到80%。与人类专家的手动调优相比，LM调优的代理在性能上表现出竞争力，完成圈数的平均时间步为855，接近专家调优代理的850时间步。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发、智能代理系统和自适应学习环境。通过自动化奖励设计，开发者可以更快速地调整代理行为，提升用户体验。同时，该方法也可推广至其他需要动态调整策略的强化学习任务中，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement Learning (RL) in games has gained significant momentum in recent years, enabling the creation of different agent behaviors that can transform a player's gaming experience. However, deploying RL agents in production environments presents two key challenges: (1) designing an effective reward function typically requires an RL expert, and (2) when a game's content or mechanics are modified, previously tuned reward weights may no longer be optimal. Towards the latter challenge, we propose an automated approach for iteratively fine-tuning an RL agent's reward function weights, based on a user-defined language based behavioral goal. A Language Model (LM) proposes updated weights at each iteration based on this target behavior and a summary of performance statistics from prior training rounds. This closed-loop process allows the LM to self-correct and refine its output over time, producing increasingly aligned behavior without the need for manual reward engineering. We evaluate our approach in a racing task and show that it consistently improves agent performance across iterations. The LM-guided agents show a significant increase in performance from $9\%$ to $74\%$ success rate in just one iteration. We compare our LM-guided tuning against a human expert's manual weight design in the racing task: by the final iteration, the LM-tuned agent achieved an $80\%$ success rate, and completed laps in an average of $855$ time steps, a competitive performance against the expert-tuned agent's peak $94\%$ success, and $850$ time steps.

