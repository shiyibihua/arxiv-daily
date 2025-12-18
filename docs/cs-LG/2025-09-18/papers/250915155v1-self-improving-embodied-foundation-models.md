---
layout: default
title: Self-Improving Embodied Foundation Models
---

# Self-Improving Embodied Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15155" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15155v1</a>
  <a href="https://arxiv.org/pdf/2509.15155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15155v1', 'Self-Improving Embodied Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seyed Kamyar Seyed Ghasemipour, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Igor Mordatch

**分类**: cs.LG, cs.RO

**发布日期**: 2025-09-18

**备注**: Appearing in the Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**提出自提升具身基础模型，通过两阶段训练实现机器人自主技能学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `基础模型` `机器人学习` `自主学习` `强化学习` `模仿学习` `步数预测`

## 📋 核心要点

1. 现有机器人控制方法依赖大量人工标注数据，泛化性差，而具身基础模型在低级控制中的应用仍受限。
2. 受大型语言模型强化学习微调的启发，提出两阶段训练方法：监督微调和自提升，提升模型性能。
3. 实验表明，该方法比单纯增加模仿数据更高效，成功率更高，并能自主学习新技能，具备更强的泛化能力。

## 📝 摘要（中文）

本文提出了一种两阶段后训练方法，用于提升具身基础模型在机器人低级控制中的性能。第一阶段是监督微调（SFT），利用行为克隆和步数预测目标对预训练的基础模型进行微调。第二阶段是自提升，步数预测能够提取出良好形状的奖励函数和鲁棒的成功检测器，从而使机器人集群能够在最少的人工监督下自主地练习下游任务。在真实和模拟机器人上的大量实验表明，该方法在具身基础模型上取得了显著成果。与扩展模仿数据收集相比，SFT和自提升的结合更具样本效率，并能产生具有更高成功率的策略。此外，网络规模预训练和自提升的结合是实现这种样本效率的关键。该方法还能够自主地练习和获取新的技能，这些技能可以泛化到训练期间使用的模仿学习数据集中观察到的行为之外。这些发现突出了将预训练的基础模型与在线自提升相结合以实现机器人自主技能获取的潜力。

## 🔬 方法详解

**问题定义**：现有机器人控制方法，特别是行为克隆，依赖于大量的专家演示数据，成本高昂且泛化能力有限。具身基础模型虽然在其他领域表现出色，但在机器人低级控制任务中的应用仍然面临挑战，缺乏有效的训练方法来充分利用预训练模型的潜力。

**核心思路**：借鉴大型语言模型通过强化学习进行微调的成功经验，论文提出一种两阶段的后训练方法，即监督微调（SFT）和自提升。核心思想是利用预训练模型的先验知识，结合少量模仿数据和自主探索，使机器人能够自主地学习和提升技能。

**技术框架**：整体框架包含两个主要阶段：
1. **监督微调（SFT）**：使用行为克隆和步数预测作为辅助目标，对预训练的具身基础模型进行微调。行为克隆用于学习模仿数据集中的行为，步数预测则用于估计当前状态距离目标状态的距离，从而提供更丰富的监督信号。
2. **自提升**：利用SFT阶段训练的步数预测模型，构建奖励函数和成功检测器。然后，使用强化学习算法（例如PPO）让机器人自主地与环境交互，通过最大化奖励来不断提升策略。

**关键创新**：该方法最重要的创新在于将预训练的具身基础模型与在线自提升相结合，实现了机器人自主技能学习。与传统的模仿学习方法相比，该方法能够利用预训练模型的先验知识，并通过自主探索来发现新的技能，从而突破了模仿数据集的限制。

**关键设计**：
* **步数预测**：使用一个神经网络来预测当前状态距离目标状态的步数，该预测值被用作SFT阶段的辅助损失函数，并在自提升阶段用于构建奖励函数。
* **奖励函数设计**：奖励函数基于步数预测的负变化量，鼓励机器人朝着目标状态前进。同时，使用成功检测器来判断任务是否完成，并给予额外的奖励。
* **强化学习算法**：使用近端策略优化（PPO）算法进行策略优化，通过裁剪策略更新幅度来保证训练的稳定性。

## 📊 实验亮点

实验结果表明，该方法在真实和模拟机器人上均取得了显著成果。与单纯增加模仿数据相比，SFT和自提升的结合在样本效率上提升显著，成功率也更高。更重要的是，该方法能够使机器人自主学习新的技能，这些技能可以泛化到模仿数据集中未观察到的行为，证明了该方法在自主技能获取方面的潜力。

## 🎯 应用场景

该研究成果可广泛应用于各种机器人自主操作任务，例如家庭服务机器人、工业自动化机器人和医疗机器人等。通过自主学习和提升技能，机器人能够更好地适应复杂多变的环境，完成各种任务，从而提高生产效率和服务质量。未来，该方法有望推动机器人技术的进一步发展，实现更智能、更自主的机器人系统。

## 📄 摘要（原文）

> Foundation models trained on web-scale data have revolutionized robotics, but their application to low-level control remains largely limited to behavioral cloning. Drawing inspiration from the success of the reinforcement learning stage in fine-tuning large language models, we propose a two-stage post-training approach for robotics. The first stage, Supervised Fine-Tuning (SFT), fine-tunes pretrained foundation models using both: a) behavioral cloning, and b) steps-to-go prediction objectives. In the second stage, Self-Improvement, steps-to-go prediction enables the extraction of a well-shaped reward function and a robust success detector, enabling a fleet of robots to autonomously practice downstream tasks with minimal human supervision. Through extensive experiments on real-world and simulated robot embodiments, our novel post-training recipe unveils significant results on Embodied Foundation Models. First, we demonstrate that the combination of SFT and Self-Improvement is significantly more sample-efficient than scaling imitation data collection for supervised learning, and that it leads to policies with significantly higher success rates. Further ablations highlight that the combination of web-scale pretraining and Self-Improvement is the key to this sample-efficiency. Next, we demonstrate that our proposed combination uniquely unlocks a capability that current methods cannot achieve: autonomously practicing and acquiring novel skills that generalize far beyond the behaviors observed in the imitation learning datasets used during training. These findings highlight the transformative potential of combining pretrained foundation models with online Self-Improvement to enable autonomous skill acquisition in robotics. Our project website can be found at https://self-improving-efms.github.io .

