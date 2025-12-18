---
layout: default
title: Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning
---

# Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15103" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15103v2</a>
  <a href="https://arxiv.org/pdf/2509.15103.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15103v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15103v2', 'Vulnerable Agent Identification in Large-Scale Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simin Li, Zheng Yuwei, Zihao Mao, Linhao Wang, Ruixiao Xu, Chengdong Ma, Xin Yu, Yuqing Ma, Qi Dou, Xin Wang, Jie Luo, Bo An, Yaodong Yang, Weifeng Lv, Xianglong Liu

**分类**: cs.MA, cs.AI

**发布日期**: 2025-09-18 (更新: 2025-09-19)

**备注**: submitted to NIPS 2025

---

## 💡 一句话要点

**提出HAD-MFC框架，用于大规模多智能体强化学习中脆弱智能体的识别。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `脆弱智能体识别` `均场控制` `分层优化` `对抗学习`

## 📋 核心要点

1. 大规模多智能体系统中部分智能体失效不可避免，现有方法难以有效识别导致系统性能严重下降的脆弱智能体。
2. 论文提出分层对抗去中心化均场控制(HAD-MFC)框架，通过解耦上下层优化问题，实现高效的脆弱智能体识别。
3. 实验表明，该方法能有效识别大规模MARL中的脆弱智能体，诱导系统产生更严重的故障，并学习脆弱性价值函数。

## 📝 摘要（中文）

本文研究了大规模多智能体强化学习(MARL)中的脆弱智能体识别(VAI)问题，即识别出那些一旦被攻击就会严重降低系统整体性能的智能体子集。我们将VAI建模为一个分层对抗去中心化均场控制(HAD-MFC)问题，其中上层涉及选择最脆弱智能体的NP-hard组合优化任务，下层使用均场MARL为这些智能体学习最坏情况下的对抗策略。为了解决上下层耦合的问题，我们首先通过Fenchel-Rockafellar变换解耦分层过程，从而为上层产生一个正则化的均场贝尔曼算子，实现每层独立学习，降低计算复杂度。然后，我们将上层组合优化问题重新表述为一个MDP，其奖励来自正则化的均场贝尔曼算子，从而可以通过贪婪和强化学习算法依次识别最脆弱的智能体。这种分解可以证明保留了原始HAD-MFC的最优解。实验表明，我们的方法能够有效地识别大规模MARL和基于规则的系统中的更脆弱的智能体，诱导系统产生更严重的故障，并学习一个能够揭示每个智能体脆弱性的价值函数。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模多智能体强化学习(MARL)中脆弱智能体识别(VAI)的问题。当系统规模增大时，部分智能体失效变得不可避免，而识别出哪些智能体的失效会对系统整体性能造成最严重的影响至关重要。现有方法难以在大规模场景下有效地识别这些脆弱智能体，面临计算复杂度和策略探索的挑战。

**核心思路**：论文的核心思路是将VAI问题建模为分层对抗优化问题，即HAD-MFC。上层负责选择最脆弱的智能体，下层则学习针对这些智能体的最坏情况下的对抗策略。通过Fenchel-Rockafellar变换解耦上下层，使得每层可以独立学习，从而降低计算复杂度。同时，将上层组合优化问题转化为MDP，利用强化学习算法进行求解。

**技术框架**：HAD-MFC框架包含两个主要层次：上层脆弱智能体选择和下层对抗策略学习。首先，使用Fenchel-Rockafellar变换将原始问题解耦，得到一个正则化的均场贝尔曼算子。然后，上层将智能体选择问题建模为MDP，使用贪婪算法或强化学习算法选择最脆弱的智能体。下层使用均场MARL算法学习针对这些智能体的对抗策略。上下层交替迭代，直至收敛。

**关键创新**：论文的关键创新在于：1) 将VAI问题建模为分层对抗优化问题，并提出HAD-MFC框架；2) 使用Fenchel-Rockafellar变换解耦上下层优化问题，降低计算复杂度；3) 将上层组合优化问题转化为MDP，利用强化学习算法进行求解。与现有方法相比，该方法能够更有效地识别大规模MARL中的脆弱智能体。

**关键设计**：上层MDP的状态空间为已选择的脆弱智能体集合，动作空间为剩余未选择的智能体集合，奖励函数为正则化的均场贝尔曼算子输出的价值函数增益。下层使用均场MARL算法，例如Mean Field Actor-Critic (MFAC)，学习对抗策略。正则化项的设计旨在平衡探索和利用，避免过早收敛到局部最优解。

## 📊 实验亮点

实验结果表明，该方法在多个大规模MARL环境中能够有效地识别出更脆弱的智能体，并诱导系统产生更严重的故障。例如，在星际争霸II环境中，该方法能够识别出关键的兵种组合，使得敌方更容易突破防线。此外，该方法学习到的价值函数能够准确地反映每个智能体的脆弱性，为系统设计和优化提供了有价值的信息。

## 🎯 应用场景

该研究成果可应用于大规模机器人集群、智能交通系统、分布式计算系统等领域。通过识别系统中的脆弱节点，可以提前采取防御措施，提高系统的鲁棒性和可靠性，降低系统崩溃的风险。此外，该方法还可以用于评估不同智能体的价值，为资源分配和系统优化提供指导。

## 📄 摘要（原文）

> Partial agent failure becomes inevitable when systems scale up, making it crucial to identify the subset of agents whose compromise would most severely degrade overall performance. In this paper, we study this Vulnerable Agent Identification (VAI) problem in large-scale multi-agent reinforcement learning (MARL). We frame VAI as a Hierarchical Adversarial Decentralized Mean Field Control (HAD-MFC), where the upper level involves an NP-hard combinatorial task of selecting the most vulnerable agents, and the lower level learns worst-case adversarial policies for these agents using mean-field MARL. The two problems are coupled together, making HAD-MFC difficult to solve. To solve this, we first decouple the hierarchical process by Fenchel-Rockafellar transform, resulting a regularized mean-field Bellman operator for upper level that enables independent learning at each level, thus reducing computational complexity. We then reformulate the upper-level combinatorial problem as a MDP with dense rewards from our regularized mean-field Bellman operator, enabling us to sequentially identify the most vulnerable agents by greedy and RL algorithms. This decomposition provably preserves the optimal solution of the original HAD-MFC. Experiments show our method effectively identifies more vulnerable agents in large-scale MARL and the rule-based system, fooling system into worse failures, and learns a value function that reveals the vulnerability of each agent.

