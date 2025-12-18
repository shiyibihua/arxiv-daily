---
layout: default
title: LLM-Guided Task- and Affordance-Level Exploration in Reinforcement Learning
---

# LLM-Guided Task- and Affordance-Level Exploration in Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16615" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16615v1</a>
  <a href="https://arxiv.org/pdf/2509.16615.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16615v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16615v1', 'LLM-Guided Task- and Affordance-Level Exploration in Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jelle Luijkx, Runyu Ma, Zlatan Ajanović, Jens Kober

**分类**: cs.RO

**发布日期**: 2025-09-20

**备注**: 8 pages, 7 figures

---

## 💡 一句话要点

**LLM引导强化学习中的任务和可供性探索，提升机器人操作效率**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `机器人操作` `可供性` `任务规划`

## 📋 核心要点

1. 传统强化学习在机器人操作中面临样本效率低和探索空间大的挑战。
2. LLM-TALE利用LLM进行任务级和可供性级的规划，引导RL探索，提升学习效率。
3. 实验表明，LLM-TALE在样本效率和成功率上优于现有方法，并具有良好的sim-to-real迁移能力。

## 📝 摘要（中文）

强化学习(RL)是机器人操作的一个有前景的方法，但它可能受到样本效率低的影响，并且需要对大型状态-动作空间进行广泛的探索。最近的方法利用大型语言模型(LLM)的常识知识和推理能力来引导探索更有意义的状态。然而，LLM可以产生在语义上合理但物理上不可行的计划，从而产生不可靠的行为。我们引入了LLM-TALE，一个使用LLM的规划来直接引导RL探索的框架。LLM-TALE集成了任务级别和可供性级别的规划，通过引导智能体执行语义上有意义的动作来提高学习效率。与假设LLM生成的最优计划或奖励的先前方法不同，LLM-TALE在线纠正次优性，并探索无需人工监督的多模态可供性级别计划。我们在标准RL基准测试中的抓取和放置任务上评估LLM-TALE，观察到与强大的基线相比，样本效率和成功率都有所提高。真实机器人实验表明了有希望的零样本sim-to-real迁移。代码和补充材料可在https://llm-tale.github.io获得。

## 🔬 方法详解

**问题定义**：现有强化学习方法在机器人操作任务中，由于状态-动作空间巨大，探索效率低下，导致学习速度慢，难以应用到复杂场景。即使利用LLM进行指导，也可能生成语义合理但物理上不可行的计划，影响最终性能。

**核心思路**：LLM-TALE的核心在于利用LLM的规划能力，在任务级别和可供性级别上引导强化学习的探索过程。通过LLM提供的高层指令和对物体可供性的理解，缩小探索范围，使智能体能够更快地找到有意义的动作序列。

**技术框架**：LLM-TALE框架包含以下几个主要模块：1) LLM规划器：生成任务级别的计划（例如，拿起物体A，放置到位置B）和可供性级别的计划（例如，使用抓取动作拿起物体A）。2) 强化学习智能体：根据LLM提供的计划，在环境中执行动作并学习策略。3) 在线纠正机制：检测LLM生成的次优计划，并通过强化学习进行修正，避免完全依赖LLM的输出。

**关键创新**：LLM-TALE的关键创新在于同时利用LLM进行任务级和可供性级的规划，并将其与强化学习探索相结合。与以往方法不同，LLM-TALE不假设LLM生成最优计划，而是通过在线纠正机制来处理LLM的次优输出，从而提高了鲁棒性。此外，该方法无需人工监督即可探索多模态的可供性级别计划。

**关键设计**：LLM规划器使用预训练的LLM，通过prompting的方式生成计划。强化学习智能体可以使用各种RL算法，例如PPO或SAC。在线纠正机制可以通过比较LLM计划的预期结果和实际执行结果来检测次优性，并使用额外的奖励信号来引导智能体学习更优的策略。具体参数设置和网络结构的选择取决于具体的任务和环境。

## 📊 实验亮点

实验结果表明，LLM-TALE在抓取和放置任务中，相较于传统强化学习方法和仅使用LLM指导的方法，在样本效率和成功率上均有显著提升。真实机器人实验也验证了LLM-TALE具有良好的零样本sim-to-real迁移能力，表明该方法具有实际应用潜力。

## 🎯 应用场景

LLM-TALE具有广泛的应用前景，可应用于各种机器人操作任务，例如自动化装配、物流分拣、家庭服务等。通过结合LLM的知识和推理能力以及强化学习的自适应能力，可以实现更智能、更高效的机器人系统，从而提高生产效率和服务质量。

## 📄 摘要（原文）

> Reinforcement learning (RL) is a promising approach for robotic manipulation, but it can suffer from low sample efficiency and requires extensive exploration of large state-action spaces. Recent methods leverage the commonsense knowledge and reasoning abilities of large language models (LLMs) to guide exploration toward more meaningful states. However, LLMs can produce plans that are semantically plausible yet physically infeasible, yielding unreliable behavior. We introduce LLM-TALE, a framework that uses LLMs' planning to directly steer RL exploration. LLM-TALE integrates planning at both the task level and the affordance level, improving learning efficiency by directing agents toward semantically meaningful actions. Unlike prior approaches that assume optimal LLM-generated plans or rewards, LLM-TALE corrects suboptimality online and explores multimodal affordance-level plans without human supervision. We evaluate LLM-TALE on pick-and-place tasks in standard RL benchmarks, observing improvements in both sample efficiency and success rates over strong baselines. Real-robot experiments indicate promising zero-shot sim-to-real transfer. Code and supplementary material are available at https://llm-tale.github.io.

