---
layout: default
title: Reinforcement Learning Driven Generalizable Feature Representation for Cross-User Activity Recognition
---

# Reinforcement Learning Driven Generalizable Feature Representation for Cross-User Activity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.01031" class="toolbar-btn" target="_blank">📄 arXiv: 2509.01031v1</a>
  <a href="https://arxiv.org/pdf/2509.01031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.01031v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.01031v1', 'Reinforcement Learning Driven Generalizable Feature Representation for Cross-User Activity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaozhou Ye, Kevin I-Kai Wang

**分类**: cs.LG, cs.AI, cs.HC

**发布日期**: 2025-08-31

---

## 💡 一句话要点

**提出TPRL-DG框架以解决跨用户活动识别问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人类活动识别` `跨用户泛化` `强化学习` `自回归生成` `时间序列分析` `医疗保健` `智能环境`

## 📋 核心要点

1. 现有的HAR方法在面对不同用户的多样性时表现不佳，容易过拟合于特定用户的模式，导致在未见用户上的性能下降。
2. 本文提出TPRL-DG框架，将特征提取视为强化学习驱动的序列决策过程，利用自回归生成器生成时间标记，优化用户不变的活动动态。
3. 在DSADS和PAMAP2数据集上的实验结果显示，TPRL-DG在跨用户泛化方面超越了现有方法，且无需针对每个用户的校准。

## 📝 摘要（中文）

人类活动识别（HAR）在医疗保健、健身追踪和智能环境中至关重要，但由于用户间的多样性，传统的监督学习方法常常无法有效泛化。现有的领域泛化方法往往忽视时间依赖性或依赖于不切实际的领域特定标签。本文提出了一种新的框架——时间保持强化学习领域泛化（TPRL-DG），将特征提取重新定义为由强化学习驱动的序列决策过程。TPRL-DG利用基于Transformer的自回归生成器生成捕捉用户不变活动动态的时间标记，通过多目标奖励函数优化，平衡类别区分和跨用户不变性。实验结果表明，TPRL-DG在DSADS和PAMAP2数据集上超越了现有的最先进方法，显著提高了跨用户的识别准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决跨用户活动识别中的泛化问题，现有方法往往因用户间的运动模式、传感器位置和生理特征的差异而表现不佳，导致在未见用户上的识别准确性低下。

**核心思路**：TPRL-DG框架通过将特征提取视为一个序列决策过程，利用强化学习来优化特征的提取，旨在捕捉用户不变的活动动态，从而提高跨用户的泛化能力。

**技术框架**：该框架主要包括三个模块：自回归生成器用于生成时间标记，强化学习模块用于优化特征提取过程，以及多目标奖励函数用于平衡类别区分和跨用户不变性。

**关键创新**：TPRL-DG的主要创新在于引入了强化学习驱动的领域泛化方法，采用自回归的时间标记生成方式，且设计了无标签的奖励机制，消除了对目标用户注释的需求。

**关键设计**：在设计中，采用了基于Transformer的生成器，设置了多目标奖励函数以优化特征提取，并确保时间一致性，具体的参数设置和网络结构细节在实验中进行了验证。

## 📊 实验亮点

在DSADS和PAMAP2数据集上的实验结果显示，TPRL-DG在跨用户识别准确性上超越了现有的最先进方法，具体提升幅度达到XX%，且无需进行每个用户的校准，显示出其优越的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括个性化医疗、适应性健身追踪和上下文感知环境。通过学习用户不变的时间模式，TPRL-DG能够促进HAR系统的可扩展性，为未来的智能健康监测和个性化服务提供支持。

## 📄 摘要（原文）

> Human Activity Recognition (HAR) using wearable sensors is crucial for healthcare, fitness tracking, and smart environments, yet cross-user variability -- stemming from diverse motion patterns, sensor placements, and physiological traits -- hampers generalization in real-world settings. Conventional supervised learning methods often overfit to user-specific patterns, leading to poor performance on unseen users. Existing domain generalization approaches, while promising, frequently overlook temporal dependencies or depend on impractical domain-specific labels. We propose Temporal-Preserving Reinforcement Learning Domain Generalization (TPRL-DG), a novel framework that redefines feature extraction as a sequential decision-making process driven by reinforcement learning. TPRL-DG leverages a Transformer-based autoregressive generator to produce temporal tokens that capture user-invariant activity dynamics, optimized via a multi-objective reward function balancing class discrimination and cross-user invariance. Key innovations include: (1) an RL-driven approach for domain generalization, (2) autoregressive tokenization to preserve temporal coherence, and (3) a label-free reward design eliminating the need for target user annotations. Evaluations on the DSADS and PAMAP2 datasets show that TPRL-DG surpasses state-of-the-art methods in cross-user generalization, achieving superior accuracy without per-user calibration. By learning robust, user-invariant temporal patterns, TPRL-DG enables scalable HAR systems, facilitating advancements in personalized healthcare, adaptive fitness tracking, and context-aware environments.

