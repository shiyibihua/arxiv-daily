---
layout: default
title: Symmetric Behavior Regularized Policy Optimization
---

# Symmetric Behavior Regularized Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04225" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04225v3</a>
  <a href="https://arxiv.org/pdf/2508.04225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04225v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04225v3', 'Symmetric Behavior Regularized Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingwei Zhu, Haseeb Shah, Zheng Chen, Yukie Nagai, Martha White

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-06 (更新: 2025-12-01)

---

## 💡 一句话要点

**提出对称行为正则化策略优化以解决离线强化学习中的分布偏移问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `对称正则化` `策略优化` `泰勒级数` `机器人控制` `自动驾驶` `游戏智能体`

## 📋 核心要点

1. 现有的行为正则化策略优化方法在处理离线强化学习中的分布偏移时存在局限性，尤其是对称正则化的应用尚未得到充分研究。
2. 本文提出了一种新方法S$f$-AC，通过泰勒级数近似对称正则化的最优策略，并在此基础上进行条件对称项的泰勒展开，确保数值稳定性。
3. 实验结果表明，S$f$-AC在D4RL MuJoCo任务中表现优异，且有效避免了其他方法在特定环境下的失败，展示了其广泛的适用性。

## 📝 摘要（中文）

行为正则化策略优化（BRPO）利用不对称正则化来减轻离线强化学习中的分布偏移。本文首次研究了对称正则化的开放性问题，发现对称正则化不允许解析最优策略$π^*$，这对其实际应用构成挑战。通过对Pearson-Vajda $χ^n$散度的泰勒级数近似$π^*$，我们证明仅在$n=5$时存在解析策略表达。为以数值稳定的方式计算解，我们提出对称散度损失的条件对称项进行泰勒展开，进而提出了一种新算法：对称$f$-演员评论家（S$f$-AC）。S$f$-AC在各种D4RL MuJoCo任务中均取得了强劲的结果，并避免了在IQL、SQL、XQL和AWAC中观察到的每个环境失败，为离线强化学习提供了更多样化和有效的正则化选择。

## 🔬 方法详解

**问题定义**：本文旨在解决离线强化学习中由于分布偏移导致的策略优化问题，现有方法在对称正则化方面缺乏有效的解析解，限制了其实用性。

**核心思路**：通过对Pearson-Vajda $χ^n$散度进行泰勒级数近似，论文提出了一种新算法S$f$-AC，旨在实现对称正则化的有效应用，并确保数值计算的稳定性。

**技术框架**：S$f$-AC的整体架构包括对称散度损失的计算、泰勒展开的实现以及策略优化过程，主要模块涵盖了条件对称项的处理和策略更新机制。

**关键创新**：本文的主要创新在于首次提出对称正则化的策略优化方法，并通过泰勒级数近似实现了对称散度的有效计算，克服了传统方法的局限性。

**关键设计**：在算法设计中，关键参数包括泰勒级数的截断点设置（$n=5$），损失函数的构造，以及网络结构的选择，以确保算法在多种任务中的稳定性和有效性。

## 📊 实验亮点

实验结果显示，S$f$-AC在D4RL MuJoCo任务中表现出色，相较于IQL、SQL、XQL和AWAC等基线方法，成功避免了每个环境的失败，展现了其在策略优化中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶、游戏智能体等离线强化学习场景。通过提供更为稳定和有效的策略优化方法，S$f$-AC能够在多样化的环境中实现更好的学习效果，推动相关领域的技术进步。

## 📄 摘要（原文）

> Behavior Regularized Policy Optimization (BRPO) leverages asymmetric (divergence) regularization to mitigate the distribution shift in offline Reinforcement Learning. This paper is the first to study the open question of symmetric regularization. We show that symmetric regularization does not permit an analytic optimal policy $π^*$, posing a challenge to practical utility of symmetric BRPO. We approximate $π^*$ by the Taylor series of Pearson-Vajda $χ^n$ divergences and show that an analytic policy expression exists only when the series is capped at $n=5$. To compute the solution in a numerically stable manner, we propose to Taylor expand the conditional symmetry term of the symmetric divergence loss, leading to a novel algorithm: Symmetric $f$-Actor Critic (S$f$-AC). S$f$-AC achieves consistently strong results across various D4RL MuJoCo tasks. Additionally, S$f$-AC avoids per-environment failures observed in IQL, SQL, XQL and AWAC, opening up possibilities for more diverse and effective regularization choices for offline RL.

