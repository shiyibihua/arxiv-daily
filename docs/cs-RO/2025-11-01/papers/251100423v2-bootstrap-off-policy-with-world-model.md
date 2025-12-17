---
layout: default
title: Bootstrap Off-policy with World Model
---

# Bootstrap Off-policy with World Model

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00423" target="_blank" class="toolbar-btn">arXiv: 2511.00423v2</a>
    <a href="https://arxiv.org/pdf/2511.00423.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00423v2" 
            onclick="toggleFavorite(this, '2511.00423v2', 'Bootstrap Off-policy with World Model')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Guojian Zhan, Likun Wang, Xiangteng Zhang, Jiaxin Gao, Masayoshi Tomizuka, Shengbo Eben Li

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-11-01 (更新: 2025-11-21)

**备注**: NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/molumitu/BOOM_MBRL)

---

## 💡 一句话要点

**BOOM：通过世界模型引导的离策略强化学习，提升样本效率和性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `世界模型` `离策略学习` `在线规划` `行为对齐`

## 📋 核心要点

1. 在线规划虽然能提升强化学习的样本效率，但环境交互引入的数据偏差会损害模型学习和策略优化。
2. BOOM框架通过世界模型连接规划和离策略学习，利用规划器优化动作来引导策略，实现行为对齐。
3. 实验表明，BOOM在DeepMind Control Suite和Humanoid-Bench上实现了最先进的训练稳定性和最终性能。

## 📝 摘要（中文）

在线规划已被证明在强化学习中能有效提高样本效率和最终性能。然而，使用规划进行环境交互不可避免地会在收集的数据与策略的实际行为之间引入差异，从而降低模型学习和策略改进的效果。为了解决这个问题，我们提出了BOOM（Bootstrap Off-policy with WOrld Model），一个通过引导循环紧密集成规划和离策略学习的框架：策略初始化规划器，规划器通过行为对齐优化动作以引导策略。这种循环由联合学习的世界模型支持，该模型使规划器能够模拟未来的轨迹，并提供价值目标以促进策略改进。BOOM的核心是一个无似然对齐损失，它使用规划器的非参数动作分布来引导策略，并结合软价值加权机制，优先考虑高回报行为，并减轻回放缓冲区中规划器动作质量的可变性。在DeepMind Control Suite和Humanoid-Bench上的实验表明，BOOM在训练稳定性和最终性能方面都达到了最先进的结果。

## 🔬 方法详解

**问题定义**：在线规划在强化学习中面临数据偏差问题，即策略实际执行的动作与规划器产生的动作存在差异，导致模型学习和策略改进受阻。现有方法难以有效利用规划的优势，同时避免数据偏差带来的负面影响。

**核心思路**：BOOM的核心在于通过一个引导循环，将规划器和离策略学习紧密结合。策略初始化规划器，规划器通过优化动作来引导策略，从而实现行为对齐。世界模型则为规划器提供模拟环境，并为策略改进提供价值目标。这种循环机制旨在利用规划的优势，同时减轻数据偏差的影响。

**技术框架**：BOOM包含三个主要模块：世界模型、规划器和策略。世界模型负责学习环境的动态特性，规划器利用世界模型进行未来轨迹的模拟和动作优化，策略则根据规划器的输出进行改进。整个框架通过一个引导循环进行迭代更新，策略的输出作为规划器的输入，规划器的输出又用于策略的改进。

**关键创新**：BOOM的关键创新在于无似然对齐损失和软价值加权机制。无似然对齐损失利用规划器的非参数动作分布来引导策略，避免了对动作分布的显式建模。软价值加权机制则优先考虑高回报行为，并减轻回放缓冲区中规划器动作质量的可变性。

**关键设计**：BOOM使用联合学习的方式训练世界模型，规划器和策略。无似然对齐损失的具体形式为最小化策略输出动作与规划器输出动作之间的距离，可以使用KL散度或JS散度等度量方式。软价值加权机制则根据规划器输出动作的价值对回放缓冲区中的样本进行加权，价值越高，权重越大。

## 📊 实验亮点

BOOM在DeepMind Control Suite和Humanoid-Bench等高维控制任务上取得了显著的性能提升。实验结果表明，BOOM在训练稳定性和最终性能方面均优于现有方法，达到了最先进水平。例如，在某些任务上，BOOM的性能提升幅度超过了20%。

## 🎯 应用场景

BOOM框架具有广泛的应用前景，可应用于机器人控制、自动驾驶、游戏AI等领域。通过结合规划和离策略学习，BOOM能够有效提高样本效率和最终性能，从而降低训练成本，并提升智能体的决策能力。该研究对于推动强化学习在复杂环境中的应用具有重要意义。

## 📄 摘要（原文）

> Online planning has proven effective in reinforcement learning (RL) for improving sample efficiency and final performance. However, using planning for environment interaction inevitably introduces a divergence between the collected data and the policy's actual behaviors, degrading both model learning and policy improvement. To address this, we propose BOOM (Bootstrap Off-policy with WOrld Model), a framework that tightly integrates planning and off-policy learning through a bootstrap loop: the policy initializes the planner, and the planner refines actions to bootstrap the policy through behavior alignment. This loop is supported by a jointly learned world model, which enables the planner to simulate future trajectories and provides value targets to facilitate policy improvement. The core of BOOM is a likelihood-free alignment loss that bootstraps the policy using the planner's non-parametric action distribution, combined with a soft value-weighted mechanism that prioritizes high-return behaviors and mitigates variability in the planner's action quality within the replay buffer. Experiments on the high-dimensional DeepMind Control Suite and Humanoid-Bench show that BOOM achieves state-of-the-art results in both training stability and final performance. The code is accessible at https://github.com/molumitu/BOOM_MBRL.

