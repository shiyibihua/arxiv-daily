---
layout: default
title: Robust Dynamic Material Handling via Adaptive Constrained Evolutionary Reinforcement Learning
---

# Robust Dynamic Material Handling via Adaptive Constrained Evolutionary Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16795" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16795v1</a>
  <a href="https://arxiv.org/pdf/2506.16795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16795v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16795v1', 'Robust Dynamic Material Handling via Adaptive Constrained Evolutionary Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengpeng Hu, Ziming Wang, Bo Yuan, Jialin Liu, Chengqi Zhang, Xin Yao

**分类**: cs.NE, cs.AI

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出自适应约束进化强化学习以解决动态物料处理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `动态物料处理` `强化学习` `自适应算法` `约束优化` `进化学习` `调度策略` `鲁棒性`

## 📋 核心要点

1. 现有方法在动态物料处理任务中面临稀疏奖励和约束条件的挑战，导致适应性不足。
2. 本文提出的自适应约束进化强化学习（ACERL）方法，通过维护多样化的演员群体来增强探索能力，并自适应选择训练实例。
3. 实验结果显示，ACERL在八个训练和八个未见测试实例上表现优异，能够有效满足约束条件，并在40个未见噪声实例上展现出强大的鲁棒性。

## 📝 摘要（中文）

动态物料处理（DMH）涉及将动态到达的物料运输任务实时分配给合适的车辆，以最小化完成时间和延迟。在实际场景中，通常可以利用历史任务记录来训练决策策略。近年来，强化学习被应用于解决DMH问题，但由于动态事件的发生，如新任务的出现，要求具有高度的适应性。解决DMH面临的挑战包括任务延迟等约束条件的满足。本文提出了一种新颖的自适应约束进化强化学习（ACERL）方法，该方法维护一组演员以实现多样化探索，并通过访问每个演员来应对稀疏奖励和约束违规问题。此外，ACERL还自适应地选择最有利的训练实例以改善策略。大量实验表明，ACERL在性能上优于多种最先进的算法，能够在满足约束的同时调度车辆。

## 🔬 方法详解

**问题定义**：本文旨在解决动态物料处理（DMH）中的任务分配问题，现有方法在应对动态事件和满足约束条件方面存在不足，尤其是在稀疏奖励的情况下。

**核心思路**：提出自适应约束进化强化学习（ACERL）方法，通过维护多样化的演员群体来增强探索能力，并利用历史记录自适应选择训练实例，以提高策略的鲁棒性和适应性。

**技术框架**：ACERL的整体架构包括多个演员，每个演员负责探索不同的策略，并通过反馈机制来应对稀疏奖励和约束违规。训练过程中，系统会动态选择最有利的训练实例，以优化学习过程。

**关键创新**：ACERL的主要创新在于其自适应选择训练实例的能力和对稀疏奖励的有效处理，这与传统的强化学习方法相比，显著提高了策略的适应性和鲁棒性。

**关键设计**：在ACERL中，演员的数量和选择策略是关键设计因素，损失函数考虑了奖励稀疏性和约束条件，确保策略在满足约束的同时实现最优调度。

## 📊 实验亮点

实验结果表明，ACERL在八个训练和八个未见测试实例上表现优异，相较于多种最先进的算法，提升了调度效率和约束满足率。此外，在40个未见噪声实例上的实验进一步验证了其鲁棒性，整体效果得到了交叉验证的支持。

## 🎯 应用场景

该研究的潜在应用领域包括物流、仓储管理和自动化运输系统等。通过提高动态物料处理的效率和适应性，ACERL能够在实际操作中显著降低成本和提高服务质量，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Dynamic material handling (DMH) involves the assignment of dynamically arriving material transporting tasks to suitable vehicles in real time for minimising makespan and tardiness. In real-world scenarios, historical task records are usually available, which enables the training of a decision policy on multiple instances consisting of historical records. Recently, reinforcement learning has been applied to solve DMH. Due to the occurrence of dynamic events such as new tasks, adaptability is highly required. Solving DMH is challenging since constraints including task delay should be satisfied. A feedback is received only when all tasks are served, which leads to sparse reward. Besides, making the best use of limited computational resources and historical records for training a robust policy is crucial. The time allocated to different problem instances would highly impact the learning process. To tackle those challenges, this paper proposes a novel adaptive constrained evolutionary reinforcement learning (ACERL) approach, which maintains a population of actors for diverse exploration. ACERL accesses each actor for tackling sparse rewards and constraint violation to restrict the behaviour of the policy. Moreover, ACERL adaptively selects the most beneficial training instances for improving the policy. Extensive experiments on eight training and eight unseen test instances demonstrate the outstanding performance of ACERL compared with several state-of-the-art algorithms. Policies trained by ACERL can schedule the vehicles while fully satisfying the constraints. Additional experiments on 40 unseen noised instances show the robust performance of ACERL. Cross-validation further presents the overall effectiveness of ACREL. Besides, a rigorous ablation study highlights the coordination and benefits of each ingredient of ACERL.

