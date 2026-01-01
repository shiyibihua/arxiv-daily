---
layout: default
title: Dynamic Policy Learning for Legged Robot with Simplified Model Pretraining and Model Homotopy Transfer
---

# Dynamic Policy Learning for Legged Robot with Simplified Model Pretraining and Model Homotopy Transfer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.24698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.24698v1</a>
  <a href="https://arxiv.org/pdf/2512.24698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.24698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.24698v1', 'Dynamic Policy Learning for Legged Robot with Simplified Model Pretraining and Model Homotopy Transfer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongyun Kang, Min-Gyu Kim, Tae-Gyu Song, Hajun Kim, Sehoon Ha, Hae-Won Park

**分类**: cs.RO

**发布日期**: 2025-12-31

**备注**: 8 pages. Submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出基于简化模型预训练和模型同伦迁移的动态策略学习方法，用于解决腿足机器人运动控制问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `腿足机器人` `强化学习` `动态运动控制` `模型预训练` `模型同伦` `策略迁移` `四足机器人`

## 📋 核心要点

1. 腿足机器人动态运动生成面临挑战，强化学习方法通常需要大量的奖励调整或高质量的演示。
2. 论文提出一种基于连续性学习的框架，通过简化模型预训练和模型同伦迁移，实现策略从简化模型到复杂模型的平滑过渡。
3. 实验表明，该方法在动态任务中收敛速度更快，稳定性更高，并在真实四足机器人上成功部署，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种基于连续性学习框架的动态策略学习方法，用于高效生成和优化腿足机器人的复杂动态行为。该方法结合了简化模型预训练和模型同伦迁移。首先，使用单刚体模型预训练策略，以在简化环境中捕获核心运动模式。然后，采用连续性策略，逐步将策略迁移到全身动力学环境中，从而最大限度地减少性能损失。为了定义连续性路径，本文引入了一种模型同伦方法，通过逐渐重新分配躯干和腿部之间的质量和惯性，从单刚体模型过渡到全身模型。实验结果表明，与基线方法相比，该方法不仅收敛速度更快，而且在迁移过程中表现出更高的稳定性。该框架已在一系列动态任务（包括翻转和墙壁辅助动作）中得到验证，并已成功部署在真实的四足机器人上。

## 🔬 方法详解

**问题定义**：腿足机器人动态运动控制，尤其是在复杂环境下的高动态运动，是一个具有挑战性的问题。传统的强化学习方法需要大量的奖励函数调整，或者依赖于高质量的专家演示数据，这限制了其在实际应用中的可行性。此外，直接在复杂的全身动力学模型上训练策略，计算成本高昂，且容易陷入局部最优。

**核心思路**：论文的核心思路是利用简化模型进行策略预训练，然后通过模型同伦的方式，逐步将策略迁移到复杂的全身动力学模型上。这种方法利用了简化模型计算效率高、易于训练的优点，同时避免了直接在复杂模型上训练的困难。模型同伦保证了策略迁移的平滑性，从而减少了性能损失。

**技术框架**：该方法包含两个主要阶段：简化模型预训练和模型同伦迁移。在简化模型预训练阶段，使用单刚体模型训练策略，使其能够完成基本的运动模式。在模型同伦迁移阶段，通过逐渐改变模型的质量和惯性分布，从单刚体模型过渡到全身动力学模型。在每个同伦阶段，使用强化学习算法对策略进行微调，以适应新的模型。

**关键创新**：该方法最重要的创新点在于提出了模型同伦的概念，并将其应用于策略迁移。通过逐步改变模型的参数，实现从简化模型到复杂模型的平滑过渡，避免了策略在迁移过程中出现剧烈的性能下降。这种方法有效地利用了简化模型的优势，同时保证了策略在复杂模型上的性能。

**关键设计**：模型同伦的关键在于如何定义从简化模型到复杂模型的过渡路径。论文通过逐渐重新分配躯干和腿部之间的质量和惯性来实现这一目标。具体来说，定义了一个同伦参数λ，λ=0对应于单刚体模型，λ=1对应于全身动力学模型。在每个同伦阶段，根据λ的值调整模型的质量和惯性参数，并使用PPO等强化学习算法对策略进行微调。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24698v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24698v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.24698v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在翻转和墙壁辅助动作等动态任务中，与基线方法相比，收敛速度更快，稳定性更高。例如，在翻转任务中，该方法能够更快地学习到稳定的翻转动作，并且在迁移到真实机器人上时，表现出更好的鲁棒性。在真实四足机器人上的部署验证了该方法的实际可行性。

## 🎯 应用场景

该研究成果可应用于各种腿足机器人的运动控制，尤其是在复杂地形和动态环境下的应用，例如搜救、勘探、物流等。通过简化模型预训练和模型同伦迁移，可以降低腿足机器人运动控制的开发成本和时间，提高其在实际应用中的可靠性和鲁棒性。未来，该方法可以扩展到其他类型的机器人和控制任务中。

## 📄 摘要（原文）

> Generating dynamic motions for legged robots remains a challenging problem. While reinforcement learning has achieved notable success in various legged locomotion tasks, producing highly dynamic behaviors often requires extensive reward tuning or high-quality demonstrations. Leveraging reduced-order models can help mitigate these challenges. However, the model discrepancy poses a significant challenge when transferring policies to full-body dynamics environments. In this work, we introduce a continuation-based learning framework that combines simplified model pretraining and model homotopy transfer to efficiently generate and refine complex dynamic behaviors. First, we pretrain the policy using a single rigid body model to capture core motion patterns in a simplified environment. Next, we employ a continuation strategy to progressively transfer the policy to the full-body environment, minimizing performance loss. To define the continuation path, we introduce a model homotopy from the single rigid body model to the full-body model by gradually redistributing mass and inertia between the trunk and legs. The proposed method not only achieves faster convergence but also demonstrates superior stability during the transfer process compared to baseline methods. Our framework is validated on a range of dynamic tasks, including flips and wall-assisted maneuvers, and is successfully deployed on a real quadrupedal robot.

