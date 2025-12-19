---
layout: default
title: ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation
---

# ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16302" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16302v1</a>
  <a href="https://arxiv.org/pdf/2512.16302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16302v1', 'ManiLong-Shot: Interaction-Aware One-Shot Imitation Learning for Long-Horizon Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixuan Chen, Chongkai Gao, Lin Shao, Jieqi Shi, Jing Huo, Yang Gao

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**ManiLong-Shot：交互感知的单样本模仿学习用于长时程操作任务**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `单样本模仿学习` `长时程操作` `交互感知` `视觉-语言模型` `机器人控制`

## 📋 核心要点

1. 现有单样本模仿学习方法主要局限于短时程任务，难以应用于复杂的长时程操作。
2. ManiLong-Shot将长时程任务分解为交互感知的原语序列，通过视觉-语言模型或规则启发式方法驱动分解。
3. 实验表明，ManiLong-Shot在仿真和真实机器人上均表现出优异的泛化能力和任务执行效果。

## 📝 摘要（中文）

本文提出ManiLong-Shot，一个新颖的框架，旨在实现长时程灵巧操作任务的有效单样本模仿学习(OSIL)。ManiLong-Shot围绕物理交互事件构建长时程任务，将问题重新定义为对交互感知原语进行排序，而不是直接模仿连续轨迹。这种原语分解可以由视觉-语言模型(VLM)的高级推理驱动，或者由机器人状态变化推导出的基于规则的启发式方法驱动。对于每个原语，ManiLong-Shot预测对交互至关重要的不变区域，建立演示和当前观察之间的对应关系，并计算目标末端执行器姿态，从而实现有效的任务执行。大量的仿真实验表明，ManiLong-Shot仅在10个短时程任务上训练，即可通过单样本模仿泛化到20个未见过的长时程任务，跨越三个难度级别，相对于SOTA方法实现了22.8%的相对改进。此外，真实机器人实验验证了ManiLong-Shot通过OSIL稳健地执行三个长时程操作任务的能力，证实了其在实际应用中的可行性。

## 🔬 方法详解

**问题定义**：现有单样本模仿学习(OSIL)方法在长时程操作任务中面临挑战，因为直接模仿连续轨迹难以泛化到未见过的任务。此外，长时程任务的状态空间巨大，使得学习过程更加复杂和不稳定。因此，需要一种能够有效分解长时程任务并实现泛化的OSIL方法。

**核心思路**：ManiLong-Shot的核心思路是将长时程任务分解为一系列交互感知的原语。每个原语代表一个基本的物理交互动作，例如抓取、放置等。通过学习如何执行这些原语，并将它们组合起来，可以实现对长时程任务的模仿学习。这种分解方法降低了学习的复杂性，并提高了泛化能力。

**技术框架**：ManiLong-Shot的整体框架包括以下几个主要模块：1) 任务分解模块：使用视觉-语言模型(VLM)或基于规则的启发式方法将长时程任务分解为交互原语序列。2) 原语执行模块：对于每个原语，预测对交互至关重要的不变区域，建立演示和当前观察之间的对应关系，并计算目标末端执行器姿态。3) 控制模块：根据计算出的目标姿态，控制机器人执行相应的动作。

**关键创新**：ManiLong-Shot的关键创新在于其交互感知的原语分解方法。与直接模仿连续轨迹的方法不同，ManiLong-Shot关注于任务中的物理交互事件，并将任务分解为一系列交互原语。这种分解方法使得模型能够更好地理解任务的结构，并提高泛化能力。此外，使用VLM或规则启发式方法进行任务分解也提高了框架的灵活性和适应性。

**关键设计**：在原语执行模块中，论文可能使用了特定的损失函数来训练模型预测不变区域和目标姿态。例如，可以使用对比损失来学习不变区域的表示，并使用均方误差损失来优化目标姿态的预测。此外，网络结构的设计也可能对性能产生影响，例如使用卷积神经网络(CNN)来提取图像特征，并使用循环神经网络(RNN)来处理原语序列。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16302v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16302v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16302v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ManiLong-Shot在仿真实验中，仅使用10个短时程任务进行训练，即可泛化到20个未见过的长时程任务，相对于SOTA方法实现了22.8%的相对改进。在真实机器人实验中，ManiLong-Shot成功执行了三个长时程操作任务，验证了其在实际应用中的可行性。这些结果表明，ManiLong-Shot是一种有效的长时程操作任务单样本模仿学习方法。

## 🎯 应用场景

ManiLong-Shot具有广泛的应用前景，例如在智能制造、家庭服务、医疗康复等领域。它可以用于教导机器人执行各种复杂的长时程操作任务，例如装配产品、整理物品、辅助病人等。该研究的实际价值在于降低了机器人编程的难度，提高了机器人的智能化水平，并有望推动机器人技术在各个领域的应用。

## 📄 摘要（原文）

> One-shot imitation learning (OSIL) offers a promising way to teach robots new skills without large-scale data collection. However, current OSIL methods are primarily limited to short-horizon tasks, thus limiting their applicability to complex, long-horizon manipulations. To address this limitation, we propose ManiLong-Shot, a novel framework that enables effective OSIL for long-horizon prehensile manipulation tasks. ManiLong-Shot structures long-horizon tasks around physical interaction events, reframing the problem as sequencing interaction-aware primitives instead of directly imitating continuous trajectories. This primitive decomposition can be driven by high-level reasoning from a vision-language model (VLM) or by rule-based heuristics derived from robot state changes. For each primitive, ManiLong-Shot predicts invariant regions critical to the interaction, establishes correspondences between the demonstration and the current observation, and computes the target end-effector pose, enabling effective task execution. Extensive simulation experiments show that ManiLong-Shot, trained on only 10 short-horizon tasks, generalizes to 20 unseen long-horizon tasks across three difficulty levels via one-shot imitation, achieving a 22.8% relative improvement over the SOTA. Additionally, real-robot experiments validate ManiLong-Shot's ability to robustly execute three long-horizon manipulation tasks via OSIL, confirming its practical applicability.

