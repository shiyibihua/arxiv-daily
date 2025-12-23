---
layout: default
title: Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation
---

# Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02206" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02206v1</a>
  <a href="https://arxiv.org/pdf/2506.02206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02206v1', 'Reinforcement Learning with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengyang Peng, Zhihao Zhang, Shiting Gong, Sankalp Agrawal, Keith A. Redmill, Ayonga Hereid

**分类**: cs.RO

**发布日期**: 2025-06-02

**备注**: 8 pages, 5 figures, 3 tables

---

## 💡 一句话要点

**提出动态子目标追踪方法以解决人形机器人导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `动态子目标` `强化学习` `模型预测控制` `导航` `数据自助技术` `步态生成`

## 📋 核心要点

1. 现有的双足机器人导航方法在计算效率与步态稳定性之间存在显著矛盾，难以满足实时导航需求。
2. 本文提出了一种分层框架，通过动态子目标引导机器人，结合高层次强化学习与低层次模型预测控制。
3. 实验结果显示，所提框架在多场景下的导航成功率和适应性显著优于传统模型方法及其他学习方法。

## 📝 摘要（中文）

安全且实时的导航对于人形机器人应用至关重要。然而，现有的双足机器人导航框架常常难以在计算效率与稳定步态所需的精度之间取得平衡。本文提出了一种新颖的分层框架，能够持续生成动态子目标，引导机器人穿越复杂环境。该方法包括一个高层次的强化学习规划器，用于在机器人中心坐标系中选择子目标，以及一个基于模型预测控制的低层次规划器，生成稳健的步态以达到这些子目标。为了加速和稳定训练过程，我们结合了数据自助技术，利用基于模型的导航方法生成多样化且信息丰富的数据集。通过在多个随机障碍场景中对Agility Robotics Digit人形机器人进行模拟验证，结果表明我们的框架显著提高了导航成功率和适应性。

## 🔬 方法详解

**问题定义**：本研究旨在解决人形机器人在复杂环境中实时导航的挑战，现有方法在计算效率与步态稳定性之间存在矛盾，导致导航效果不佳。

**核心思路**：我们提出的框架通过动态生成子目标，结合高层次的强化学习和低层次的模型预测控制，旨在提高导航的灵活性和稳定性。

**技术框架**：整体架构分为两个主要模块：高层次的强化学习规划器负责选择子目标，低层次的模型预测控制规划器则负责生成稳健的步态以实现目标。

**关键创新**：本研究的创新点在于引入数据自助技术，通过模型驱动的方法生成多样化的数据集，从而加速和稳定训练过程，这在现有方法中尚未得到充分利用。

**关键设计**：在设计中，我们优化了模型预测控制的参数设置，并采用了特定的损失函数以提高步态的稳定性和适应性，同时确保高层次规划器的决策效率。

## 📊 实验亮点

实验结果表明，所提框架在多个随机障碍场景中，导航成功率提高了显著的百分比，相较于原始模型方法和其他学习方法，适应性也有明显提升，验证了框架的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人及其他需要在动态环境中进行自主导航的机器人系统。通过提高导航的成功率和适应性，能够在实际应用中显著提升机器人的工作效率和安全性，未来可能推动人形机器人在更多复杂场景中的应用。

## 📄 摘要（原文）

> Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion. We propose a novel hierarchical framework that continuously generates dynamic subgoals to guide the robot through cluttered environments. Our method comprises a high-level reinforcement learning (RL) planner for subgoal selection in a robot-centric coordinate system and a low-level Model Predictive Control (MPC) based planner which produces robust walking gaits to reach these subgoals. To expedite and stabilize the training process, we incorporate a data bootstrapping technique that leverages a model-based navigation approach to generate a diverse, informative dataset. We validate our method in simulation using the Agility Robotics Digit humanoid across multiple scenarios with random obstacles. Results show that our framework significantly improves navigation success rates and adaptability compared to both the original model-based method and other learning-based methods.

