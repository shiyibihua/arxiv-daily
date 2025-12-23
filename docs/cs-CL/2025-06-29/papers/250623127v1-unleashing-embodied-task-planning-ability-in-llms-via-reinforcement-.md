---
layout: default
title: Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning
---

# Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23127" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23127v1</a>
  <a href="https://arxiv.org/pdf/2506.23127.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23127v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23127v1', 'Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoye Fei, Li Ji, Siyin Wang, Junhao Shi, Jingjing Gong, Xipeng Qiu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-29

---

## 💡 一句话要点

**提出Embodied Planner-R1以解决LLMs在环境任务规划中的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `环境任务规划` `强化学习` `自主探索` `交互式策略优化` `稀疏奖励` `泛化能力`

## 📋 核心要点

1. 现有方法在环境任务规划中依赖静态知识，难以处理因果关系和环境反馈，尤其在部分可观察环境中表现不佳。
2. 提出的Embodied Planner-R1框架通过纯强化学习和组回合设计，支持LLMs在自主探索中学习互动能力，减少对人工标注的依赖。
3. 在ALFWorld和ScienceWorld基准测试中，Embodied Planner-R1分别达到了97.78%和79.92%的完成率，显示出显著的性能提升和良好的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在多种任务中展现出卓越的能力，但在需要持续环境理解和动作生成的环境任务规划场景中面临重大挑战。现有方法基于静态知识生成开放式动作脚本，难以学习动作与环境反馈之间的因果关系，尤其是在部分可观察环境中。我们提出了Embodied Planner-R1，这是一种新颖的以结果为驱动的强化学习框架，使LLMs通过自主探索在最小监督下发展互动能力。该框架包含三项关键创新：1）采用纯强化学习与组回合，无需人工标注，通过并行探索实现环境内互动；2）基于完成驱动的稀疏奖励；3）交互式策略优化（IPO），以高效学习分组轨迹。在两个具有挑战性的文本基础环境规划基准上，Embodied Planner-R1在ALFWorld上实现了97.78%的完成率，在ScienceWorld上达到了79.92%，大幅超越了先前的方法，并在未见环境中仅下降了-3.66%，显示出强大的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在环境任务规划中面临的挑战，尤其是如何在部分可观察环境中有效学习动作与环境反馈之间的因果关系。现有方法多依赖静态知识，难以适应动态环境。

**核心思路**：论文提出的Embodied Planner-R1框架通过引入纯强化学习和组回合的方式，使LLMs能够在自主探索中学习互动能力，减少对人工标注的依赖，从而提高任务完成率。

**技术框架**：该框架主要包括三个模块：1）环境交互模块，通过并行探索实现多样化的环境反馈；2）奖励机制模块，采用基于完成驱动的稀疏奖励；3）策略优化模块，使用交互式策略优化（IPO）来高效学习分组轨迹。

**关键创新**：最重要的创新在于采用了纯强化学习与组回合的结合，允许模型在没有人工标注的情况下，通过环境交互自主学习，从而显著提升了学习效率和任务完成率。

**关键设计**：在参数设置上，框架优化了奖励函数设计，采用稀疏奖励机制以激励有效的任务完成，同时在网络结构上，结合了深度学习与强化学习的优势，确保了模型的高效性和稳定性。

## 📊 实验亮点

Embodied Planner-R1在ALFWorld和ScienceWorld基准测试中分别达到了97.78%和79.92%的完成率，显著超越了现有方法，且在未见环境中仅下降了-3.66%，显示出强大的泛化能力和学习效率。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、智能助手和游戏AI等，能够在动态和复杂环境中实现更高效的任务规划与执行。通过提升LLMs的环境理解和互动能力，未来可能推动更智能的自动化系统的发展，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated remarkable capabilities across various tasks, yet they face significant challenges in embodied task planning scenarios that require continuous environmental understanding and action generation. Existing approaches generate open-loop action scripts based on static knowledge, making it difficult to learn causal relationships between actions and environmental feedback, particularly in partially observable environments. We introduce Embodied Planner-R1, a novel outcome-driven reinforcement learning framework that enables LLMs to develop interactive capabilities through autonomous exploration with minimal supervision. Our framework incorporates three key innovations: (1) Without human annotations, we employ pure reinforcement learning with group rollout, incorporating in-environment interaction through parallel exploration; (2) completion-driven sparse reward; and (3) Interactive Policy Optimization (IPO) for efficient learning from grouped trajectories. Across two challenging text-based Embodied planning benchmarks, Embodied Planner-R1 achieves impressive completion rates of 97.78% on ALFWorld and 79.92% on ScienceWorld, surpassing prior methods by a large margin, and suffers only a -3.66% drop in previously unseen environments, evidencing strong generalization.

