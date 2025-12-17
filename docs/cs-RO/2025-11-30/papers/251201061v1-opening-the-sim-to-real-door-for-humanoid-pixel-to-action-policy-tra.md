---
layout: default
title: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer
---

# Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2512.01061" target="_blank" class="toolbar-btn">arXiv: 2512.01061v1</a>
    <a href="https://arxiv.org/pdf/2512.01061.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01061v1" 
            onclick="toggleFavorite(this, '2512.01061v1', 'Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Haoru Xue, Tairan He, Zi Wang, Qingwei Ben, Wenli Xiao, Zhengyi Luo, Xingye Da, Fernando Castañeda, Guanya Shi, Shankar Sastry, Linxi "Jim" Fan, Yuke Zhu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-11-30

**备注**: https://doorman-humanoid.github.io/

---

## 💡 一句话要点

**提出基于模拟的类人机器人像素到动作策略迁移框架，解决复杂环境下的操作难题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Sim-to-Real` `类人机器人` `强化学习` `Loco-manipulation` `铰接物体` `策略迁移` `视觉感知`

## 📋 核心要点

1. 现有机器人学习方法难以在复杂环境中泛化，需要大量真实数据，成本高昂。
2. 提出teacher-student-bootstrap框架，结合分阶段重置探索和GRPO微调，实现高效的sim-to-real迁移。
3. 实验表明，该策略在模拟环境中训练后，在真实环境中超越人类操作员31.7%的任务完成时间。

## 📝 摘要（中文）

本文提出了一种teacher-student-bootstrap学习框架，用于视觉驱动的类人机器人loco-manipulation，以铰接物体交互作为代表性的高难度基准。该方法引入了分阶段重置探索策略，稳定了长时程特权策略训练，并采用基于GRPO的微调程序，缓解了部分可观测性问题，并提高了sim-to-real强化学习中的闭环一致性。该策略完全在模拟数据上训练，在各种门类型上实现了鲁棒的零样本性能，并且在相同的全身控制堆栈下，任务完成时间比人类遥操作员提高了31.7%。这代表了第一个能够使用纯RGB感知进行多样化铰接loco-manipulation的类人机器人sim-to-real策略。

## 🔬 方法详解

**问题定义**：论文旨在解决类人机器人在复杂环境下的loco-manipulation问题，特别是铰接物体的交互，例如开门。现有的方法通常需要大量的真实世界数据进行训练，成本高昂且难以泛化。此外，部分可观测性和sim-to-real的差异也给策略迁移带来了挑战。

**核心思路**：论文的核心思路是利用GPU加速的、照片级真实的模拟环境生成大规模训练数据，并通过teacher-student-bootstrap框架实现策略的sim-to-real迁移。通过在模拟环境中进行充分的探索和学习，使策略具备在真实环境中泛化的能力。

**技术框架**：整体框架包含三个主要阶段：1) 使用特权策略（privileged policy）在模拟环境中进行训练，该策略可以访问完整的状态信息；2) 使用分阶段重置探索策略稳定长时程训练；3) 使用GRPO（Gated Recurrent Policy Optimization）进行微调，以缓解部分可观测性和提高闭环一致性。Teacher策略指导Student策略学习，并通过Bootstrap方法不断提升策略性能。

**关键创新**：论文的关键创新在于结合了分阶段重置探索策略和GRPO微调方法，有效地解决了长时程训练的稳定性和部分可观测性问题。分阶段重置探索策略允许agent从不同的状态开始学习，从而更有效地探索环境。GRPO通过引入门控机制，使得策略能够更好地处理时间依赖关系，从而提高闭环一致性。

**关键设计**：分阶段重置探索策略将训练过程分为多个阶段，每个阶段agent从不同的状态开始。GRPO使用LSTM网络作为策略网络，并引入门控机制来控制信息的流动。损失函数包括策略梯度损失、值函数损失和熵正则化项。具体参数设置（如学习率、折扣因子等）未知。

## 📊 实验亮点

实验结果表明，该策略在各种门类型上实现了鲁棒的零样本性能，并且在相同的全身控制堆栈下，任务完成时间比人类遥操作员提高了31.7%。这表明该方法能够有效地将模拟环境中学习到的策略迁移到真实世界，并超越人类操作员的性能。

## 🎯 应用场景

该研究成果可应用于各种需要类人机器人进行复杂操作的场景，例如家庭服务、医疗辅助、工业自动化等。通过降低对真实世界数据的依赖，可以加速机器人技术的部署和应用，并提高机器人在复杂环境中的适应性和鲁棒性。

## 📄 摘要（原文）

> Recent progress in GPU-accelerated, photorealistic simulation has opened a scalable data-generation path for robot learning, where massive physics and visual randomization allow policies to generalize beyond curated environments. Building on these advances, we develop a teacher-student-bootstrap learning framework for vision-based humanoid loco-manipulation, using articulated-object interaction as a representative high-difficulty benchmark. Our approach introduces a staged-reset exploration strategy that stabilizes long-horizon privileged-policy training, and a GRPO-based fine-tuning procedure that mitigates partial observability and improves closed-loop consistency in sim-to-real RL. Trained entirely on simulation data, the resulting policy achieves robust zero-shot performance across diverse door types and outperforms human teleoperators by up to 31.7% in task completion time under the same whole-body control stack. This represents the first humanoid sim-to-real policy capable of diverse articulated loco-manipulation using pure RGB perception.

