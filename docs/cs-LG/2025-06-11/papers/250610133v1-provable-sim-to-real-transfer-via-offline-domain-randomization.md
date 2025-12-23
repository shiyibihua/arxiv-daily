---
layout: default
title: Provable Sim-to-Real Transfer via Offline Domain Randomization
---

# Provable Sim-to-Real Transfer via Offline Domain Randomization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10133" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10133v1</a>
  <a href="https://arxiv.org/pdf/2506.10133.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10133v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10133v1', 'Provable Sim-to-Real Transfer via Offline Domain Randomization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arnaud Fickinger, Abderrahim Bendahi, Stuart Russell

**分类**: cs.LG, cs.RO

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出离线领域随机化以解决仿真到现实转移问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `领域随机化` `离线学习` `强化学习` `仿真到现实` `最大似然估计` `机器人控制` `策略优化`

## 📋 核心要点

1. 现有的领域随机化方法在利用离线数据方面存在不足，导致仿真到现实的转移效果不佳。
2. 本文提出了离线领域随机化（ODR），通过最大似然估计拟合仿真器参数分布，以更好地利用已有的离线数据。
3. ODR在理论上证明了其一致性，并在实验中显示出相较于传统领域随机化显著降低了仿真到现实的误差。

## 📝 摘要（中文）

强化学习代理在从仿真部署到现实世界时常常面临困难。领域随机化（DR）是减少仿真与现实之间差距的主要策略，但标准DR忽视了已有的离线数据。本文研究了离线领域随机化（ODR），首先根据离线数据集拟合仿真器参数的分布。我们将ODR形式化为参数化仿真器族上的最大似然估计，证明了在适度的正则性和可识别性条件下，该估计量的一致性，显示随着数据集的增长，它收敛于真实动态。此外，我们推导了误差界限，表明ODR的仿真到现实误差在有限仿真器情况下比均匀DR更紧，最后引入了E-DROPO，通过增加熵奖励来防止方差崩溃，从而在实践中实现更广泛的随机化和更稳健的零-shot转移。

## 🔬 方法详解

**问题定义**：本文旨在解决强化学习代理在仿真到现实转移中的困难，现有的领域随机化方法未能有效利用离线数据，导致转移效果不理想。

**核心思路**：论文提出的离线领域随机化（ODR）通过最大似然估计拟合仿真器参数分布，充分利用已有的离线数据，以提高转移的准确性和可靠性。

**技术框架**：ODR的整体架构包括数据集的构建、仿真器参数的分布拟合、最大似然估计的实现以及最终的策略训练。主要模块包括离线数据处理、参数估计和策略优化。

**关键创新**：ODR的核心创新在于其理论基础的建立，证明了在适度条件下估计量的一致性，并且在有限仿真器情况下，ODR的误差界限比均匀DR更紧。

**关键设计**：在设计中，ODR使用了最大似然估计作为损失函数，并通过引入E-DROPO增加熵奖励，以防止方差崩溃，确保更广泛的随机化和更稳健的零-shot转移。

## 📊 实验亮点

实验结果表明，ODR在仿真到现实转移中显著降低了误差，相较于传统的领域随机化方法，ODR的误差界限提高了O(M)倍，且E-DROPO在零-shot转移中表现出更强的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶和虚拟现实等，能够有效提升仿真训练的现实适应性，减少现实环境中的试错成本，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement-learning agents often struggle when deployed from simulation to the real-world. A dominant strategy for reducing the sim-to-real gap is domain randomization (DR) which trains the policy across many simulators produced by sampling dynamics parameters, but standard DR ignores offline data already available from the real system. We study offline domain randomization (ODR), which first fits a distribution over simulator parameters to an offline dataset. While a growing body of empirical work reports substantial gains with algorithms such as DROPO, the theoretical foundations of ODR remain largely unexplored. In this work, we (i) formalize ODR as a maximum-likelihood estimation over a parametric simulator family, (ii) prove consistency of this estimator under mild regularity and identifiability conditions, showing it converges to the true dynamics as the dataset grows, (iii) derive gap bounds demonstrating ODRs sim-to-real error is up to an O(M) factor tighter than uniform DR in the finite-simulator case (and analogous gains in the continuous setting), and (iv) introduce E-DROPO, a new version of DROPO which adds an entropy bonus to prevent variance collapse, yielding broader randomization and more robust zero-shot transfer in practice.

