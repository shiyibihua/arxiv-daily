---
layout: default
title: Leveraging Temporally Extended Behavior Sharing for Multi-task Reinforcement Learning
---

# Leveraging Temporally Extended Behavior Sharing for Multi-task Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20766" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20766v2</a>
  <a href="https://arxiv.org/pdf/2509.20766.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20766v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20766v2', 'Leveraging Temporally Extended Behavior Sharing for Multi-task Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gawon Lee, Daesol Cho, H. Jin Kim

**分类**: cs.RO, cs.LG

**发布日期**: 2025-09-25 (更新: 2025-09-29)

**备注**: Accepted for publication in the proceedings of the 2025 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)

---

## 💡 一句话要点

**提出MT-Lévy，结合行为共享与时序扩展探索，提升多任务强化学习在机器人领域的样本效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多任务强化学习` `机器人学习` `行为共享` `时序扩展探索` `样本效率`

## 📋 核心要点

1. 机器人多任务强化学习面临数据收集成本高昂的挑战，限制了样本效率和泛化能力。
2. MT-Lévy结合跨任务行为共享与时序扩展探索，引导智能体更高效地探索关键状态。
3. 实验证明MT-Lévy显著提升了探索效率和样本利用率，为机器人多任务学习提供了新思路。

## 📝 摘要（中文）

多任务强化学习(MTRL)通过在多个任务上训练智能体，实现知识共享，从而提高样本效率和泛化能力。然而，由于收集多样化任务数据的成本高昂，将MTRL应用于机器人领域仍然具有挑战性。为了解决这个问题，我们提出了一种新的探索策略MT-Lévy，它结合了跨任务的行为共享和受Lévy飞行启发的时序扩展探索，从而提高了MTRL环境中的样本效率。MT-Lévy利用在相关任务上训练的策略来引导探索到关键状态，同时根据任务成功率动态调整探索水平。这种方法能够更有效地覆盖状态空间，即使在复杂的机器人环境中也是如此。实验结果表明，MT-Lévy显著提高了探索和样本效率，并通过定量和定性分析得到了支持。消融研究进一步突出了每个组成部分的贡献，表明将行为共享与自适应探索策略相结合可以显著提高MTRL在机器人应用中的实用性。

## 🔬 方法详解

**问题定义**：多任务强化学习在机器人领域的应用受限于数据收集的高成本，导致样本效率低下，难以充分探索状态空间。现有方法难以在任务间有效共享知识，并且缺乏针对机器人环境的有效探索策略。

**核心思路**：MT-Lévy的核心在于结合跨任务的行为共享和受Lévy飞行启发的时序扩展探索。通过利用相关任务的策略来指导探索，智能体可以更快地找到有价值的状态。同时，动态调整探索水平，根据任务成功率自适应地进行探索，避免无效探索。

**技术框架**：MT-Lévy的整体框架包含以下几个主要模块：1) 基于相关任务策略的行为共享模块，用于引导探索方向；2) 受Lévy飞行启发的时序扩展探索模块，用于在时间维度上扩展探索范围；3) 自适应探索水平调整模块，根据任务成功率动态调整探索强度。这些模块协同工作，实现高效的状态空间覆盖。

**关键创新**：MT-Lévy的关键创新在于将行为共享与时序扩展探索相结合，并引入自适应探索水平调整机制。与传统的探索策略相比，MT-Lévy能够更有效地利用已有的知识，并根据任务的进展情况动态调整探索策略，从而提高样本效率。

**关键设计**：MT-Lévy的关键设计包括：1) 如何选择相关任务的策略进行行为共享；2) 如何设计时序扩展探索的策略，例如Lévy飞行的步长和方向；3) 如何定义任务成功率，并将其用于自适应调整探索水平。具体的参数设置和网络结构需要根据具体的机器人任务进行调整。

## 📊 实验亮点

实验结果表明，MT-Lévy在多个机器人任务上显著提高了探索效率和样本效率。与基线方法相比，MT-Lévy能够更快地学习到最优策略，并取得更高的累积奖励。消融研究进一步验证了行为共享和自适应探索策略的有效性。

## 🎯 应用场景

MT-Lévy具有广泛的应用前景，例如机器人操作、自动驾驶、智能制造等领域。通过提高多任务强化学习的样本效率，可以降低机器人学习的成本，加速机器人在复杂环境中的部署。该研究对于推动机器人智能化和自动化具有重要意义。

## 📄 摘要（原文）

> Multi-task reinforcement learning (MTRL) offers a promising approach to improve sample efficiency and generalization by training agents across multiple tasks, enabling knowledge sharing between them. However, applying MTRL to robotics remains challenging due to the high cost of collecting diverse task data. To address this, we propose MT-Lévy, a novel exploration strategy that enhances sample efficiency in MTRL environments by combining behavior sharing across tasks with temporally extended exploration inspired by Lévy flight. MT-Lévy leverages policies trained on related tasks to guide exploration towards key states, while dynamically adjusting exploration levels based on task success ratios. This approach enables more efficient state-space coverage, even in complex robotics environments. Empirical results demonstrate that MT-Lévy significantly improves exploration and sample efficiency, supported by quantitative and qualitative analyses. Ablation studies further highlight the contribution of each component, showing that combining behavior sharing with adaptive exploration strategies can significantly improve the practicality of MTRL in robotics applications.

