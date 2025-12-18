---
layout: default
title: Deep Reinforcement Learning for Ranking Utility Tuning in the Ad Recommender System at Pinterest
---

# Deep Reinforcement Learning for Ranking Utility Tuning in the Ad Recommender System at Pinterest

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05292" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05292v1</a>
  <a href="https://arxiv.org/pdf/2509.05292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05292v1', 'Deep Reinforcement Learning for Ranking Utility Tuning in the Ad Recommender System at Pinterest')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Yang, Mehdi Ben Ayed, Longyu Zhao, Fan Zhou, Yuchen Shen, Abe Engle, Jinfeng Zhuang, Ling Leng, Jiajing Xu, Charles Rosenberg, Prathibha Deshikachar

**分类**: cs.LG

**发布日期**: 2025-09-05

---

## 💡 一句话要点

**提出DRL-PUT框架，利用深度强化学习优化Pinterest广告推荐系统中排序效用函数。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `广告推荐系统` `效用函数优化` `多目标优化` `在线学习`

## 📋 核心要点

1. 传统广告推荐系统中的效用函数手动调整方法存在目标不明确、参数组合爆炸以及缺乏个性化等问题。
2. 论文提出DRL-PUT框架，利用深度强化学习直接从在线日志中学习最优策略，避免了值函数估计的困难。
3. 在线A/B实验表明，DRL-PUT显著提升了点击率和长期点击率，验证了该方法的有效性和优越性。

## 📝 摘要（中文）

本文提出了一种通用的深度强化学习框架，用于个性化效用调整（DRL-PUT），以解决广告推荐系统中多目标优化问题。广告推荐系统中的排序效用函数线性地结合了各种业务目标的预测，在平衡平台、广告商和用户之间的价值方面起着核心作用。传统的手动调整虽然简单且易于解释，但由于其不合理的调整目标、大量的参数组合以及缺乏个性化和对季节性的适应性，通常会产生次优结果。该框架将问题建模为一个强化学习任务：给定广告请求的状态，预测最优超参数以最大化预定义的奖励。该方法直接使用在线服务日志学习最优策略模型，避免了估计值函数的需求，因为值函数的估计本质上具有高方差和不平衡的即时奖励分布。在Pinterest的广告推荐系统中进行的在线A/B实验评估表明，与基线手动效用调整方法相比，DRL-PUT使点击率提高了9.7％，长期点击率提高了7.7％。此外，论文还对不同奖励定义的影响进行了详细的消融研究，并分析了学习策略模型的个性化方面。

## 🔬 方法详解

**问题定义**：论文旨在解决广告推荐系统中排序效用函数的手动调整问题。传统方法依赖人工经验，难以应对复杂的多目标优化，且无法根据用户行为和环境变化进行自适应调整。现有方法的痛点在于无法有效平衡平台、广告商和用户之间的利益，导致推荐效果不佳。

**核心思路**：论文的核心思路是将效用函数调整问题建模成一个强化学习任务。通过将广告请求的状态作为输入，利用深度神经网络学习一个策略模型，该模型能够预测最优的超参数，从而最大化预定义的奖励函数。这种方法能够自动学习最优策略，并根据用户行为和环境变化进行自适应调整。

**技术框架**：DRL-PUT框架主要包含以下几个模块：1) 状态表示模块：将广告请求的上下文信息（如用户画像、广告特征等）编码成状态向量。2) 策略网络模块：使用深度神经网络学习一个策略模型，该模型以状态向量作为输入，输出最优的超参数。3) 奖励函数模块：定义一个奖励函数，用于衡量推荐效果的好坏。4) 训练模块：使用在线服务日志训练策略网络，目标是最大化累积奖励。

**关键创新**：该论文的关键创新在于直接从在线服务日志中学习最优策略模型，避免了估计值函数的需求。传统的强化学习方法通常需要估计值函数，但由于广告推荐系统中的奖励具有高方差和不平衡的分布，导致值函数估计非常困难。通过直接学习策略模型，可以有效地解决这个问题。

**关键设计**：论文中使用了深度神经网络作为策略网络，并采用策略梯度算法进行训练。奖励函数的设计至关重要，需要综合考虑点击率、长期点击率等多个指标。此外，论文还对不同的奖励函数进行了消融研究，以评估其对推荐效果的影响。

## 📊 实验亮点

在线A/B实验结果表明，DRL-PUT框架在Pinterest的广告推荐系统中取得了显著的性能提升。与基线手动效用调整方法相比，DRL-PUT使点击率提高了9.7％，长期点击率提高了7.7％。这些结果表明，DRL-PUT能够有效地优化排序效用函数，并提升推荐效果。

## 🎯 应用场景

该研究成果可广泛应用于各种在线广告推荐系统，尤其是在需要平衡多个业务目标的场景下。通过自动优化排序效用函数，可以提升用户体验、增加广告收入，并提高平台的整体价值。未来，该方法还可以扩展到其他推荐场景，如商品推荐、内容推荐等。

## 📄 摘要（原文）

> The ranking utility function in an ad recommender system, which linearly combines predictions of various business goals, plays a central role in balancing values across the platform, advertisers, and users. Traditional manual tuning, while offering simplicity and interpretability, often yields suboptimal results due to its unprincipled tuning objectives, the vast amount of parameter combinations, and its lack of personalization and adaptability to seasonality. In this work, we propose a general Deep Reinforcement Learning framework for Personalized Utility Tuning (DRL-PUT) to address the challenges of multi-objective optimization within ad recommender systems. Our key contributions include: 1) Formulating the problem as a reinforcement learning task: given the state of an ad request, we predict the optimal hyperparameters to maximize a pre-defined reward. 2) Developing an approach to directly learn an optimal policy model using online serving logs, avoiding the need to estimate a value function, which is inherently challenging due to the high variance and unbalanced distribution of immediate rewards. We evaluated DRL-PUT through an online A/B experiment in Pinterest's ad recommender system. Compared to the baseline manual utility tuning approach, DRL-PUT improved the click-through rate by 9.7% and the long click-through rate by 7.7% on the treated segment. We conducted a detailed ablation study on the impact of different reward definitions and analyzed the personalization aspect of the learned policy model.

