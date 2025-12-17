---
layout: default
title: CoRL-MPPI: Enhancing MPPI With Learnable Behaviours For Efficient And Provably-Safe Multi-Robot Collision Avoidance
---

# CoRL-MPPI: Enhancing MPPI With Learnable Behaviours For Efficient And Provably-Safe Multi-Robot Collision Avoidance

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.09331" target="_blank" class="toolbar-btn">arXiv: 2511.09331v1</a>
    <a href="https://arxiv.org/pdf/2511.09331.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09331v1" 
            onclick="toggleFavorite(this, '2511.09331v1', 'CoRL-MPPI: Enhancing MPPI With Learnable Behaviours For Efficient And Provably-Safe Multi-Robot Collision Avoidance')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Stepan Dergachev, Artem Pshenitsyn, Aleksandr Panov, Alexey Skrynnik, Konstantin Yakovlev

**分类**: cs.RO, cs.MA

**发布日期**: 2025-11-12

**备注**: The manuscript includes 9 pages, 4 figures, and 1 table

---

## 💡 一句话要点

**CoRL-MPPI：融合强化学习与MPPI，提升多机器人避障效率与安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `多机器人系统` `碰撞避免` `模型预测控制` `强化学习` `路径积分` `去中心化控制` `合作导航`

## 📋 核心要点

1. 多机器人去中心化避障面临挑战，传统MPPI依赖随机采样，易产生次优轨迹。
2. CoRL-MPPI融合强化学习与MPPI，学习合作避障策略，引导MPPI采样分布。
3. 实验表明，CoRL-MPPI在导航效率和安全性方面显著优于现有方法。

## 📝 摘要（中文）

去中心化碰撞避免是可扩展多机器人系统的核心挑战。模型预测路径积分(MPPI)是一种有前景的方法，它自然适用于处理任何机器人运动模型并提供强大的理论保证。然而，在实践中，基于MPPI的控制器可能提供次优轨迹，因为其性能严重依赖于无信息的随机采样。本文提出了CoRL-MPPI，一种合作强化学习和MPPI的新型融合方法，以解决这一局限性。我们在仿真中训练一个动作策略（近似为深度神经网络），学习局部合作避碰行为。然后，将学习到的策略嵌入到MPPI框架中，以指导其采样分布，使其偏向更智能和协作的动作。值得注意的是，CoRL-MPPI保留了常规MPPI的所有理论保证。我们在密集的动态仿真环境中，针对最先进的基线（包括ORCA、BVC和多智能体MPPI实现）评估了我们的方法。结果表明，CoRL-MPPI显著提高了导航效率（通过成功率和完工时间衡量）和安全性，从而实现了敏捷而稳健的多机器人导航。

## 🔬 方法详解

**问题定义**：论文旨在解决多机器人系统中去中心化碰撞避免问题。现有基于MPPI的方法依赖于随机采样，导致探索效率低，容易陷入局部最优，无法保证高效和安全的导航。现有方法难以在复杂动态环境中实现鲁棒的多机器人协作。

**核心思路**：论文的核心思路是利用强化学习预训练一个合作避障策略，然后将该策略嵌入到MPPI框架中，以指导MPPI的采样过程。通过学习到的策略来引导采样，可以提高采样效率，减少无效探索，从而更快地找到安全且高效的轨迹。

**技术框架**：CoRL-MPPI包含两个主要阶段：1) 合作强化学习阶段：使用深度神经网络训练一个动作策略，该策略学习如何在局部环境中进行合作避障。2) MPPI控制阶段：将学习到的策略嵌入到MPPI框架中，用于指导采样分布。具体来说，学习到的策略输出一个动作建议，该建议被用来调整MPPI的采样分布，使其偏向于更智能和协作的动作。

**关键创新**：CoRL-MPPI的关键创新在于将强化学习和MPPI相结合，利用强化学习学习到的先验知识来指导MPPI的采样过程。与传统的MPPI相比，CoRL-MPPI不再依赖于无信息的随机采样，而是利用学习到的策略进行智能采样，从而提高了采样效率和性能。同时，CoRL-MPPI保留了MPPI的理论保证。

**关键设计**：在强化学习阶段，使用深度神经网络作为动作策略的近似。损失函数的设计需要考虑碰撞避免、目标导向和协作等因素。在MPPI控制阶段，学习到的策略输出的动作建议被用来调整MPPI的采样分布，例如通过调整采样噪声的均值或方差。具体的网络结构和参数设置需要根据具体的机器人运动模型和环境进行调整。

## 📊 实验亮点

CoRL-MPPI在密集、动态的仿真环境中进行了评估，并与ORCA、BVC和多智能体MPPI等最先进的基线进行了比较。实验结果表明，CoRL-MPPI显著提高了导航效率（通过成功率和完工时间衡量）和安全性。例如，CoRL-MPPI的成功率比传统MPPI提高了XX%，完工时间缩短了YY%。

## 🎯 应用场景

CoRL-MPPI可应用于仓库机器人、自动驾驶、无人机编队等需要多智能体协作的场景。该方法能够提高多智能体系统的导航效率和安全性，降低碰撞风险，提升整体任务完成效率。未来可进一步扩展到更复杂的环境和任务中，例如动态障碍物环境、异构机器人系统等。

## 📄 摘要（原文）

> Decentralized collision avoidance remains a core challenge for scalable multi-robot systems. One of the promising approaches to tackle this problem is Model Predictive Path Integral (MPPI) -- a framework that is naturally suited to handle any robot motion model and provides strong theoretical guarantees. Still, in practice MPPI-based controller may provide suboptimal trajectories as its performance relies heavily on uninformed random sampling. In this work, we introduce CoRL-MPPI, a novel fusion of Cooperative Reinforcement Learning and MPPI to address this limitation. We train an action policy (approximated as deep neural network) in simulation that learns local cooperative collision avoidance behaviors. This learned policy is then embedded into the MPPI framework to guide its sampling distribution, biasing it towards more intelligent and cooperative actions. Notably, CoRL-MPPI preserves all the theoretical guarantees of regular MPPI. We evaluate our approach in dense, dynamic simulation environments against state-of-the-art baselines, including ORCA, BVC, and a multi-agent MPPI implementation. Our results demonstrate that CoRL-MPPI significantly improves navigation efficiency (measured by success rate and makespan) and safety, enabling agile and robust multi-robot navigation.

