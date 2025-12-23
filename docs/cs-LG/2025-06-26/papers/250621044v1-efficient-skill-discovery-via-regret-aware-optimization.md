---
layout: default
title: Efficient Skill Discovery via Regret-Aware Optimization
---

# Efficient Skill Discovery via Regret-Aware Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21044" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21044v1</a>
  <a href="https://arxiv.org/pdf/2506.21044.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21044v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21044v1', 'Efficient Skill Discovery via Regret-Aware Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: He Zhang, Ming Zhou, Shaopeng Zhai, Ying Sun, Hui Xiong

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出基于后悔感知优化的高效技能发现方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督学习` `技能发现` `强化学习` `后悔感知` `策略学习` `高维环境` `多样性探索`

## 📋 核心要点

1. 现有技能发现方法在高维环境中效率有限，难以有效探索多样化的技能。
2. 本文提出将技能发现视为技能生成与策略学习的极小极大博弈，利用后悔感知优化来引导技能探索。
3. 实验结果显示，所提方法在效率和多样性上均优于现有基线，并在高维环境中实现了显著的性能提升。

## 📝 摘要（中文）

无监督技能发现旨在在开放式强化学习中学习多样且可区分的行为。现有方法主要通过纯探索、互信息优化和学习时间表示来提高多样性，但在高维情况下效率有限。本文将技能发现框架化为技能生成与策略学习的极小极大博弈，提出了一种基于时间表示学习的后悔感知方法，扩展了可升级策略强度的技能空间。核心思想是技能发现与策略学习是对抗的，弱强度技能应进一步探索，而已收敛强度的技能则减少探索。我们通过可学习的技能生成器来引导技能发现，避免退化。实验结果表明，该方法在效率和多样性上均优于基线，并在高维环境中实现了15%的零样本改进。

## 🔬 方法详解

**问题定义**：本文解决的具体问题是现有无监督技能发现方法在高维环境中的效率不足，导致技能多样性探索受限。

**核心思路**：论文的核心思路是将技能发现视为技能生成与策略学习之间的对抗博弈，强调弱强度技能的进一步探索和已收敛技能的减少探索。

**技术框架**：整体架构包括技能生成器和策略学习模块，技能生成器根据后悔值评估技能强度，并引导技能发现过程。

**关键创新**：最重要的技术创新在于引入后悔感知机制，通过评估技能强度的收敛程度来优化技能探索策略，这与现有方法的单一探索策略形成鲜明对比。

**关键设计**：在技术细节上，使用可学习的技能生成器来动态调整技能生成过程，损失函数设计上考虑了技能强度的后悔值，以确保技能生成的多样性和有效性。

## 📊 实验亮点

实验结果表明，所提方法在多种复杂环境中均优于基线，尤其在高维环境中实现了15%的零样本改进，展示了显著的效率和多样性提升。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、游戏智能体和自动化系统等，能够有效提升这些领域中技能学习的效率和多样性。未来，随着技术的进一步发展，可能会在更复杂的环境中实现更广泛的应用，推动智能体的自主学习能力。

## 📄 摘要（原文）

> Unsupervised skill discovery aims to learn diverse and distinguishable behaviors in open-ended reinforcement learning. For existing methods, they focus on improving diversity through pure exploration, mutual information optimization, and learning temporal representation. Despite that they perform well on exploration, they remain limited in terms of efficiency, especially for the high-dimensional situations. In this work, we frame skill discovery as a min-max game of skill generation and policy learning, proposing a regret-aware method on top of temporal representation learning that expands the discovered skill space along the direction of upgradable policy strength. The key insight behind the proposed method is that the skill discovery is adversarial to the policy learning, i.e., skills with weak strength should be further explored while less exploration for the skills with converged strength. As an implementation, we score the degree of strength convergence with regret, and guide the skill discovery with a learnable skill generator. To avoid degeneration, skill generation comes from an up-gradable population of skill generators. We conduct experiments on environments with varying complexities and dimension sizes. Empirical results show that our method outperforms baselines in both efficiency and diversity. Moreover, our method achieves a 15% zero shot improvement in high-dimensional environments, compared to existing methods.

