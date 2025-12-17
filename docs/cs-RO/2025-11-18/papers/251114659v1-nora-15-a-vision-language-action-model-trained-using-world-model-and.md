---
layout: default
title: NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards
---

# NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.14659" target="_blank" class="toolbar-btn">arXiv: 2511.14659v1</a>
    <a href="https://arxiv.org/pdf/2511.14659.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14659v1" 
            onclick="toggleFavorite(this, '2511.14659v1', 'NORA-1.5: A Vision-Language-Action Model Trained using World Model- and Action-based Preference Rewards')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Chia-Yu Hung, Navonil Majumder, Haoyuan Deng, Liu Renhang, Yankang Ang, Amir Zadeh, Chuan Li, Dorien Herremans, Ziwei Wang, Soujanya Poria

**分类**: cs.RO, cs.AI

**发布日期**: 2025-11-18

**备注**: https://declare-lab.github.io/nora-1.5

---

## 💡 一句话要点

**NORA-1.5：基于世界模型和动作偏好奖励训练的视觉-语言-动作模型，提升具身智能体的可靠性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉-语言-动作模型` `具身智能` `世界模型` `偏好学习` `直接偏好优化` `流匹配` `机器人`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在可靠性和泛化性方面存在不足，尤其是在不同环境或真实世界部署时。
2. NORA-1.5通过增加基于流匹配的动作专家，并结合世界模型和动作偏好奖励进行训练，提升模型性能。
3. 实验表明，奖励驱动的后训练能够持续提高模拟和真实机器人环境中的性能，显著提高VLA模型的可靠性。

## 📝 摘要（中文）

本文介绍了NORA-1.5，一个视觉-语言-动作（VLA）模型，它基于预训练的NORA骨干网络，并增加了一个基于流匹配的动作专家。这种架构上的增强显著提高了性能，使NORA-1.5在模拟和真实世界的基准测试中优于NORA和几种最先进的VLA模型。为了进一步提高鲁棒性和任务成功率，我们开发了一套奖励模型，用于对VLA策略进行后训练。我们的奖励结合了（i）一个动作条件世界模型（WM），用于评估生成的动作是否导向期望的目标，以及（ii）一个偏离真实值的启发式方法，用于区分好动作和坏动作。利用这些奖励信号，我们构建了偏好数据集，并通过直接偏好优化（DPO）使NORA-1.5适应目标环境。广泛的评估表明，奖励驱动的后训练能够持续提高模拟和真实机器人环境中的性能，通过简单而有效的奖励模型显著提高VLA模型的可靠性。我们的研究结果表明，NORA-1.5和奖励引导的后训练是实现更可靠的、适用于真实世界部署的具身智能体的可行途径。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作模型在真实世界部署时可靠性和泛化性不足的问题。现有VLA模型在面对不同环境和具身智能体时，难以保证任务的成功率和稳定性，限制了其在实际场景中的应用。

**核心思路**：论文的核心思路是通过增强模型架构和引入奖励驱动的后训练来提高VLA模型的可靠性。具体来说，首先通过添加基于流匹配的动作专家来提升模型的基础性能，然后利用世界模型和动作偏好奖励来指导模型的策略优化，使其更好地适应目标环境。

**技术框架**：NORA-1.5的整体框架包括以下几个主要模块：1) 预训练的NORA骨干网络；2) 基于流匹配的动作专家，用于生成动作；3) 动作条件世界模型（WM），用于评估动作的有效性；4) 偏离真实值的启发式方法，用于区分好坏动作；5) 直接偏好优化（DPO）算法，用于根据奖励信号优化模型策略。

**关键创新**：论文的关键创新在于结合了模型架构增强和奖励驱动的后训练。通过添加动作专家，模型能够更好地生成动作；通过世界模型和动作偏好奖励，模型能够学习到更有效的策略。这种结合使得NORA-1.5在可靠性和泛化性方面都取得了显著提升。

**关键设计**：论文的关键设计包括：1) 使用流匹配方法训练动作专家，使其能够生成更流畅自然的动作；2) 设计动作条件世界模型，使其能够准确预测动作对环境的影响；3) 设计偏离真实值的启发式奖励，用于区分好坏动作；4) 使用直接偏好优化算法，根据奖励信号直接优化模型策略，避免了传统强化学习中的一些问题。

## 📊 实验亮点

NORA-1.5在模拟和真实世界的基准测试中均取得了显著的性能提升。通过添加动作专家和进行奖励驱动的后训练，NORA-1.5在多个任务上超越了NORA和其他最先进的VLA模型。实验结果表明，奖励驱动的后训练能够持续提高性能，显著提高VLA模型的可靠性。

## 🎯 应用场景

该研究成果可应用于各种需要具身智能体的实际场景，如家庭服务机器人、工业自动化、自动驾驶等。通过提高VLA模型的可靠性和泛化性，可以使这些智能体更好地适应复杂多变的环境，完成各种任务，从而提升生产效率和服务质量，具有重要的实际应用价值和广阔的发展前景。

## 📄 摘要（原文）

> Vision--language--action (VLA) models have recently shown promising performance on a variety of embodied tasks, yet they still fall short in reliability and generalization, especially when deployed across different embodiments or real-world environments. In this work, we introduce NORA-1.5, a VLA model built from the pre-trained NORA backbone by adding to it a flow-matching-based action expert. This architectural enhancement alone yields substantial performance gains, enabling NORA-1.5 to outperform NORA and several state-of-the-art VLA models across both simulated and real-world benchmarks. To further improve robustness and task success, we develop a set of reward models for post-training VLA policies. Our rewards combine (i) an action-conditioned world model (WM) that evaluates whether generated actions lead toward the desired goal, and (ii) a deviation-from-ground-truth heuristic that distinguishes good actions from poor ones. Using these reward signals, we construct preference datasets and adapt NORA-1.5 to target embodiments through direct preference optimization (DPO). Extensive evaluations show that reward-driven post-training consistently improves performance in both simulation and real-robot settings, demonstrating significant VLA model-reliability gains through simple yet effective reward models. Our findings highlight NORA-1.5 and reward-guided post-training as a viable path toward more dependable embodied agents suitable for real-world deployment.

