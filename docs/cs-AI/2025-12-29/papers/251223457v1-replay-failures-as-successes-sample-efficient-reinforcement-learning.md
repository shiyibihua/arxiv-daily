---
layout: default
title: "Replay Failures as Successes: Sample-Efficient Reinforcement Learning for Instruction Following"
---

# Replay Failures as Successes: Sample-Efficient Reinforcement Learning for Instruction Following

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.23457" class="toolbar-btn" target="_blank">📄 arXiv: 2512.23457v1</a>
  <a href="https://arxiv.org/pdf/2512.23457.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.23457v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.23457v1', 'Replay Failures as Successes: Sample-Efficient Reinforcement Learning for Instruction Following')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kongcheng Zhang, Qi Yao, Shunyu Liu, Wenjian Zhang, Min Cen, Yang Zhou, Wenkai Fang, Yiru Zhao, Baisheng Lai, Mingli Song

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-12-29

**🔗 代码/项目**: [GITHUB](https://github.com/sastpg/HIR)

---

## 💡 一句话要点

**提出HiR，通过回溯式指令重放提升指令跟随任务中强化学习的样本效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `指令跟随` `样本效率` `回溯式学习` `语言模型`

## 📋 核心要点

1. 现有强化学习方法在指令跟随任务中面临奖励稀疏问题，初始模型难以生成满足所有约束的响应，导致学习效率低下。
2. HiR通过回溯式指令重放，将失败的尝试根据事后满足的约束改写为成功案例，增加有效样本，提升学习效率。
3. 实验结果表明，HiR在不同指令跟随任务中表现出色，显著提升了样本效率，降低了计算成本。

## 📝 摘要（中文）

强化学习(RL)在对齐大型语言模型(LLM)以遵循具有各种约束的指令方面显示出前景。尽管结果令人鼓舞，但RL的改进不可避免地依赖于采样成功的、高质量的响应；然而，由于初始模型的能力有限，通常难以生成满足所有约束的响应，从而产生稀疏或难以区分的奖励，阻碍了学习。本文提出了一种新颖的、样本高效的RL框架——回溯式指令重放(HiR)，用于复杂的指令跟随任务。HiR采用了一种先选择后重写的策略，基于事后满足的约束，将失败的尝试重放为成功。我们在这些重放的样本以及原始样本上执行RL，从理论上将目标构建为指令和响应级别的双重偏好学习，从而仅使用二元奖励信号即可实现高效优化。大量的实验表明，所提出的HiR在不同的指令跟随任务中产生了有希望的结果，同时需要的计算预算更少。我们的代码和数据集可在https://github.com/sastpg/HIR 获得。

## 🔬 方法详解

**问题定义**：论文旨在解决指令跟随任务中，强化学习训练样本效率低下的问题。现有方法依赖于采样成功的、高质量的响应，但初始模型往往难以满足所有指令约束，导致奖励信号稀疏，学习过程受阻。这种稀疏奖励问题严重限制了强化学习在复杂指令跟随任务中的应用。

**核心思路**：HiR的核心思路是将失败的尝试转化为成功的经验。它不是简单地丢弃不满足所有约束的响应，而是通过“选择-重写”策略，根据事后满足的约束条件，将失败的尝试改写为成功的案例。这样可以有效增加训练样本的多样性和有效性，从而提升强化学习的样本效率。

**技术框架**：HiR的整体框架包含以下几个主要步骤：1) 初始模型生成响应；2) 根据指令和响应计算奖励信号（二元奖励）；3) 选择满足部分约束的失败尝试；4) 根据满足的约束，重写失败的尝试，使其成为“伪成功”样本；5) 使用原始样本和重写后的样本进行强化学习训练。该框架在指令和响应两个层面进行双重偏好学习。

**关键创新**：HiR的关键创新在于回溯式指令重放机制。与传统强化学习方法不同，HiR充分利用了失败的尝试，通过重写将其转化为有价值的训练样本。这种方法有效地解决了奖励稀疏问题，显著提升了样本效率。此外，HiR将目标构建为指令和响应级别的双重偏好学习，进一步提升了优化效率。

**关键设计**：HiR使用二元奖励信号，简化了奖励函数的设计。选择-重写策略是关键，具体实现可能涉及规则、启发式方法或学习模型。损失函数的设计需要同时考虑原始样本和重写样本，以实现双重偏好学习。具体的网络结构取决于具体的指令跟随任务，但通常会采用Transformer等模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23457v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23457v1/x4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.23457v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HiR在多个指令跟随任务上取得了显著的性能提升，实验结果表明，HiR能够以更少的计算资源达到与现有方法相当甚至更好的性能。具体的性能数据和对比基线在论文中详细给出，证明了HiR在样本效率方面的优势。

## 🎯 应用场景

HiR可应用于各种需要指令跟随的场景，例如机器人控制、对话系统、代码生成等。通过提升样本效率，HiR能够降低训练成本，加速模型迭代，使得强化学习能够更好地应用于实际复杂的任务中。该方法在智能助手、自动化流程等领域具有广泛的应用前景。

## 📄 摘要（原文）

> Reinforcement Learning (RL) has shown promise for aligning Large Language Models (LLMs) to follow instructions with various constraints. Despite the encouraging results, RL improvement inevitably relies on sampling successful, high-quality responses; however, the initial model often struggles to generate responses that satisfy all constraints due to its limited capabilities, yielding sparse or indistinguishable rewards that impede learning. In this work, we propose Hindsight instruction Replay (HiR), a novel sample-efficient RL framework for complex instruction following tasks, which employs a select-then-rewrite strategy to replay failed attempts as successes based on the constraints that have been satisfied in hindsight. We perform RL on these replayed samples as well as the original ones, theoretically framing the objective as dual-preference learning at both the instruction- and response-level to enable efficient optimization using only a binary reward signal. Extensive experiments demonstrate that the proposed HiR yields promising results across different instruction following tasks, while requiring less computational budget. Our code and dataset is available at https://github.com/sastpg/HIR.

