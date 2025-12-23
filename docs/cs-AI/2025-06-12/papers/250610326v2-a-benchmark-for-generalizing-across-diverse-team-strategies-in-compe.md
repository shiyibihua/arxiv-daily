---
layout: default
title: A Benchmark for Generalizing Across Diverse Team Strategies in Competitive Pokémon
---

# A Benchmark for Generalizing Across Diverse Team Strategies in Competitive Pokémon

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10326" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10326v2</a>
  <a href="https://arxiv.org/pdf/2506.10326.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10326v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10326v2', 'A Benchmark for Generalizing Across Diverse Team Strategies in Competitive Pokémon')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cameron Angliss, Jiaxun Cui, Jiaheng Hu, Arrasy Rahman, Peter Stone

**分类**: cs.AI, cs.GT, cs.LG, cs.MA

**发布日期**: 2025-06-12 (更新: 2025-06-13)

**备注**: 15 pages, 3 figures, 10 tables

**🔗 代码/项目**: [GITHUB](https://github.com/cameronangliss/VGC-Bench)

---

## 💡 一句话要点

**提出VGC-Bench以解决宝可梦团队策略泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `宝可梦` `多智能体学习` `策略泛化` `基准测试` `强化学习` `行为克隆` `博弈论`

## 📋 核心要点

1. 核心问题：现有方法在面对宝可梦VGC中多样化团队策略时，泛化能力不足，难以适应不同的战略环境。
2. 方法要点：提出VGC-Bench基准测试，提供标准化评估和多种基线方法，旨在提升AI代理的泛化能力。
3. 实验或效果：在单一团队配置下，代理能够战胜职业选手，但在团队规模扩大时，表现显著下降，显示出泛化挑战。

## 📝 摘要（中文）

开发能够在不同战略环境中稳健适应的AI代理是多智能体学习中的核心挑战。宝可梦视频游戏锦标赛（VGC）具有约$10^{139}$的团队配置空间，远超Dota或星际争霸。团队构建的高度离散和组合特性使得最佳策略因团队和对手的不同而剧烈变化，从而使泛化变得尤为困难。为推动这一问题的研究，本文提出了VGC-Bench：一个基准测试，提供关键基础设施、标准化评估协议，并提供人类游戏数据集和多种基线方法。我们的实验表明，即使在单一团队配置下训练的代理也能战胜职业选手，但在团队规模扩大时，现有最佳算法的表现却显著下降，表明跨多样化团队策略的策略泛化仍然是一个开放的挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决多智能体学习中AI代理在宝可梦VGC中泛化能力不足的问题。现有方法在面对不同团队配置时，无法有效适应新的战略环境，导致性能下降。

**核心思路**：提出VGC-Bench基准测试，通过提供标准化的评估协议和多种基线方法，帮助研究者更好地理解和提升AI代理的泛化能力。该方法通过对比不同算法在多样化团队策略下的表现，寻找最佳解决方案。

**技术框架**：VGC-Bench的整体架构包括数据集的构建、评估协议的标准化以及多种基线算法的实现。主要模块包括人类游戏数据集、强化学习、行为克隆和博弈论方法（如自我对弈、虚构对弈和双重神谕）。

**关键创新**：最重要的创新在于引入了一个全面的基准测试框架，能够系统性地评估不同AI代理在多样化团队策略下的表现。这一框架的建立为后续研究提供了重要的基础。

**关键设计**：在算法设计中，采用了多种损失函数和网络结构，以适应不同的学习任务。同时，基线方法的选择涵盖了从大语言模型到强化学习的多种策略，确保了评估的全面性和有效性。

## 📊 实验亮点

实验结果显示，在单一团队配置下，所提出的方法能够战胜职业VGC选手。然而，当团队规模扩大时，现有最佳算法的表现显著下降，表明在多样化团队策略下的泛化能力仍然是一个亟待解决的挑战。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、智能代理的开发以及多智能体系统的研究。通过提升AI在复杂环境中的泛化能力，能够推动自动化决策、策略优化等领域的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Developing AI agents that can robustly adapt to dramatically different strategic landscapes without retraining is a central challenge for multi-agent learning. Pokémon Video Game Championships (VGC) is a domain with an extraordinarily large space of possible team configurations of approximately $10^{139}$ - far larger than those of Dota or Starcraft. The highly discrete, combinatorial nature of team building in Pokémon VGC causes optimal strategies to shift dramatically depending on both the team being piloted and the opponent's team, making generalization uniquely challenging. To advance research on this problem, we introduce VGC-Bench: a benchmark that provides critical infrastructure, standardizes evaluation protocols, and supplies human-play datasets and a range of baselines - from large-language-model agents and behavior cloning to reinforcement learning and empirical game-theoretic methods such as self-play, fictitious play, and double oracle. In the restricted setting where an agent is trained and evaluated on a single-team configuration, our methods are able to win against a professional VGC competitor. We extensively evaluated all baseline methods over progressively larger team sets and find that even the best-performing algorithm in the single-team setting struggles at scaling up as team size grows. Thus, policy generalization across diverse team strategies remains an open challenge for the community. Our code is open sourced at https://github.com/cameronangliss/VGC-Bench.

