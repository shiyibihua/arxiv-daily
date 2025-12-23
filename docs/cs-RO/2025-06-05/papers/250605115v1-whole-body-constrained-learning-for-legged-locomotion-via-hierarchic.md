---
layout: default
title: Whole-Body Constrained Learning for Legged Locomotion via Hierarchical Optimization
---

# Whole-Body Constrained Learning for Legged Locomotion via Hierarchical Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05115" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05115v1</a>
  <a href="https://arxiv.org/pdf/2506.05115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05115v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05115v1', 'Whole-Body Constrained Learning for Legged Locomotion via Hierarchical Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Wang, Ruyi Zhou, Liang Ding, Tie Liu, Zhelin Zhang, Peng Xu, Haibo Gao, Zongquan Deng

**分类**: cs.RO

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出层次优化的全身约束学习以提升四足机器人安全性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `强化学习` `四足机器人` `层次优化` `安全性` `约束学习` `复杂环境` `模型控制`

## 📋 核心要点

1. 现有的无约束强化学习策略在实际应用中存在安全隐患，如关节碰撞和过大扭矩，限制了其在高安全性要求任务中的应用。
2. 本文提出了一种层次优化的全身跟随器，通过整合硬约束和软约束，提升了机器人在复杂环境中的安全性和鲁棒性。
3. 实验结果表明，经过约束训练的策略在多种户外环境中表现出色，显示出显著的可穿越性和安全性提升。

## 📝 摘要（中文）

强化学习（RL）在四足机器人运动控制中表现出色，但由于模拟与现实之间的差距以及缺乏可解释性，现有的无约束RL策略在实际应用中面临安全问题，如关节碰撞、过大扭矩和低摩擦环境下的滑动等。为了解决这些问题，本文设计了一种基于层次优化的全身跟随器，将硬约束和软约束整合到RL框架中，以提高机器人的安全性。该方法利用基于模型的控制优势，在训练或部署过程中定义多种硬软约束，从而实现策略微调，并缓解模拟到现实转移的挑战。经过训练的策略在六足机器人上进行部署，并在雪坡和楼梯等多种户外环境中测试，展示了良好的可穿越性和安全性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有无约束强化学习策略在实际应用中面临的安全问题，包括关节碰撞、过大扭矩和低摩擦环境下的滑动等。这些问题限制了四足机器人在高安全性要求任务中的应用。

**核心思路**：论文提出的核心思路是设计一个基于层次优化的全身跟随器，将硬约束和软约束整合到强化学习框架中，以提高机器人的安全性和鲁棒性。通过这种方式，机器人能够在复杂环境中更安全地移动，同时减小模拟与现实之间的差距。

**技术框架**：整体架构包括多个模块，首先是约束定义模块，用于在训练和部署过程中定义硬约束和软约束；其次是强化学习模块，负责策略的训练和优化；最后是执行模块，确保机器人在实际环境中的安全移动。

**关键创新**：本文的关键创新在于将硬约束和软约束有效整合到强化学习中，形成了一种新的层次优化策略。这与现有方法的本质区别在于，现有方法通常缺乏对安全性的系统性考虑。

**关键设计**：在设计中，关键参数包括约束的类型和强度，损失函数需要同时考虑安全性和性能，网络结构则采用了深度神经网络以处理复杂的环境输入。

## 📊 实验亮点

实验结果显示，经过约束训练的六足机器人在雪坡和楼梯等多种户外环境中表现出色，成功避免了关节碰撞和过大扭矩，提升了安全性和可穿越性，展示了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括行星探索、核设施检查和深海作业等高风险任务。通过提升四足机器人的安全性和鲁棒性，能够有效拓展其在复杂和危险环境中的应用范围，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning (RL) has demonstrated impressive performance in legged locomotion over various challenging environments. However, due to the sim-to-real gap and lack of explainability, unconstrained RL policies deployed in the real world still suffer from inevitable safety issues, such as joint collisions, excessive torque, or foot slippage in low-friction environments. These problems limit its usage in missions with strict safety requirements, such as planetary exploration, nuclear facility inspection, and deep-sea operations. In this paper, we design a hierarchical optimization-based whole-body follower, which integrates both hard and soft constraints into RL framework to make the robot move with better safety guarantees. Leveraging the advantages of model-based control, our approach allows for the definition of various types of hard and soft constraints during training or deployment, which allows for policy fine-tuning and mitigates the challenges of sim-to-real transfer. Meanwhile, it preserves the robustness of RL when dealing with locomotion in complex unstructured environments. The trained policy with introduced constraints was deployed in a hexapod robot and tested in various outdoor environments, including snow-covered slopes and stairs, demonstrating the great traversability and safety of our approach.

