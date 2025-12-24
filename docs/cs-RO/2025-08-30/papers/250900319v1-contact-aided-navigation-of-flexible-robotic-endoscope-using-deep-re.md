---
layout: default
title: Contact-Aided Navigation of Flexible Robotic Endoscope Using Deep Reinforcement Learning in Dynamic Stomach
---

# Contact-Aided Navigation of Flexible Robotic Endoscope Using Deep Reinforcement Learning in Dynamic Stomach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00319" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00319v1</a>
  <a href="https://arxiv.org/pdf/2509.00319.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00319v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00319v1', 'Contact-Aided Navigation of Flexible Robotic Endoscope Using Deep Reinforcement Learning in Dynamic Stomach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Kit Ng, Huxin Gao, Tian-Ao Ren, Jiewen Lai, Hongliang Ren

**分类**: cs.RO, cs.AI, eess.SY

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**提出基于深度强化学习的接触辅助导航策略以解决柔性机器人内窥镜在动态胃中的导航问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `柔性机器人内窥镜` `深度强化学习` `接触辅助导航` `动态胃` `导航精度` `物理仿真` `有限元方法` `外科手术`

## 📋 核心要点

1. 现有方法在动态胃环境中导航柔性机器人内窥镜时面临挑战，尤其是如何有效利用与胃壁的接触。
2. 本文提出了一种基于深度强化学习的接触辅助导航策略，通过接触力反馈提高导航精度和稳定性。
3. 实验结果表明，该方法在多种环境下均表现出色，成功率和精度显著优于传统基线策略。

## 📝 摘要（中文）

在胃肠道中导航柔性机器人内窥镜（FRE）对外科诊断和治疗至关重要。然而，在动态胃中导航尤其具有挑战性，因为FRE必须学习有效利用与可变形胃壁的接触，以到达目标位置。为此，本文提出了一种基于深度强化学习（DRL）的接触辅助导航（CAN）策略，利用接触力反馈来增强运动稳定性和导航精度。通过基于物理的有限元方法（FEM）模拟建立训练环境，使用近端策略优化（PPO）算法进行训练，结果显示该方法在静态和动态胃环境中均实现了100%的成功率，平均误差为1.6毫米，并在具有较强外部干扰的未见场景中保持85%的成功率。这些结果验证了基于DRL的CAN策略显著提升了FRE的导航性能。

## 🔬 方法详解

**问题定义**：本文旨在解决柔性机器人内窥镜在动态胃中导航的困难，现有方法未能有效利用与可变形胃壁的接触，导致导航精度不足。

**核心思路**：提出基于深度强化学习的接触辅助导航策略，利用接触力反馈来增强内窥镜的运动稳定性和导航精度，从而提高成功率。

**技术框架**：整体架构包括环境建模、深度强化学习训练和导航策略执行三个主要模块。通过物理仿真建立动态胃的有限元模型，训练过程中使用近端策略优化算法来优化导航策略。

**关键创新**：最重要的创新在于引入接触力反馈机制，使得内窥镜能够实时调整其运动策略，显著提升了在复杂环境中的导航能力。与传统方法相比，CAN策略在动态环境中表现出更高的适应性和精度。

**关键设计**：在训练过程中，采用了特定的损失函数以平衡导航精度和稳定性，同时设计了适应性强的神经网络结构，以处理动态环境中的各种不确定性。

## 📊 实验亮点

实验结果显示，基于深度强化学习的接触辅助导航策略在静态和动态胃环境中均实现了100%的成功率，平均误差仅为1.6毫米。在面对未见场景和外部干扰时，成功率仍保持在85%，显著优于传统基线策略，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括内窥镜手术、消化系统疾病的诊断与治疗等。通过提高柔性机器人内窥镜在复杂动态环境中的导航能力，能够显著提升外科手术的安全性与有效性，未来可能对医疗机器人技术的发展产生深远影响。

## 📄 摘要（原文）

> Navigating a flexible robotic endoscope (FRE) through the gastrointestinal tract is critical for surgical diagnosis and treatment. However, navigation in the dynamic stomach is particularly challenging because the FRE must learn to effectively use contact with the deformable stomach walls to reach target locations. To address this, we introduce a deep reinforcement learning (DRL) based Contact-Aided Navigation (CAN) strategy for FREs, leveraging contact force feedback to enhance motion stability and navigation precision. The training environment is established using a physics-based finite element method (FEM) simulation of a deformable stomach. Trained with the Proximal Policy Optimization (PPO) algorithm, our approach achieves high navigation success rates (within 3 mm error between the FRE's end-effector and target) and significantly outperforms baseline policies. In both static and dynamic stomach environments, the CAN agent achieved a 100% success rate with 1.6 mm average error, and it maintained an 85% success rate in challenging unseen scenarios with stronger external disturbances. These results validate that the DRL-based CAN strategy substantially enhances FRE navigation performance over prior methods.

