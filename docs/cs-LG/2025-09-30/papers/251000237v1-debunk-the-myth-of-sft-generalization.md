---
layout: default
title: Debunk the Myth of SFT Generalization
---

# Debunk the Myth of SFT Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00237" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00237v1</a>
  <a href="https://arxiv.org/pdf/2510.00237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00237v1', 'Debunk the Myth of SFT Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaofeng Lin, Hejian Sang, Zhipeng Wang, Xuezhou Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/XiaofengLin7/debunking-sft-generalization)

---

## 💡 一句话要点

**通过提示多样性和思维链，提升SFT在决策任务中的泛化能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `监督式微调` `泛化能力` `提示工程` `思维链` `决策任务` `强化学习` `数据为中心`

## 📋 核心要点

1. 现有观点认为SFT泛化能力弱于RL，但该研究发现SFT的泛化失败源于冻结提示伪影。
2. 通过引入提示多样性，SFT模型可以打破对训练语义的依赖，从而提升对未见指令的泛化能力。
3. 结合提示多样性和思维链，SFT在难度变体任务中表现出色，性能可与RL基线相媲美。

## 📝 摘要（中文）

目前普遍认为，监督式微调（SFT）会记忆训练数据，导致泛化能力不足，而强化学习（RL）则具有更广泛的鲁棒性。本文通过在Sokoban和General Points两个决策基准上进行系统评估，对这一观点进行了重新审视，并得出了不同的结论。研究表明，SFT的泛化失败很大程度上源于冻结提示伪影：当在固定的指令模板上训练时，SFT模型倾向于坚持训练语义，而不是适应新的语义。在训练过程中引入提示多样性可以打破这种捷径，从而在不损害分布内性能的情况下，实现对未见指令变体的强大泛化。此外，本文还探讨了SFT是否可以泛化到更困难的任务。思维链（CoT）监督提供了一种算法支架，显著提高了对更困难场景的迁移能力，例如具有更多箱子的大型Sokoban网格，以及具有分布外值或增加组合复杂性的五张牌组合的算术。最后，将提示多样性与CoT相结合，可以实现两全其美：在指令变体和难度变体设置中实现强大的泛化，在我们的基准测试中匹配或超过RL基线，同时保持SFT的简单性和稳定性。这些发现挑战了SFT本质上不如RL的说法，并支持以数据为中心的视角：通过适当策划的演示，普通的SFT可以像RL一样强大地泛化。

## 🔬 方法详解

**问题定义**：现有研究认为监督微调(SFT)在决策任务中泛化能力不足，容易过拟合训练数据，而强化学习(RL)则被认为具有更好的泛化性能。然而，这种观点可能忽略了SFT训练过程中的一些关键因素，例如提示工程和任务难度。

**核心思路**：本文的核心思路是通过改进SFT的训练方式，使其能够更好地泛化到未见过的指令变体和更困难的任务。具体来说，通过引入提示多样性来打破SFT对训练语义的依赖，并利用思维链(CoT)监督来提升SFT在复杂任务中的推理能力。

**技术框架**：该研究的技术框架主要包括以下几个部分：首先，使用SFT模型在决策任务上进行训练，例如Sokoban和General Points。其次，在训练过程中引入提示多样性，即使用不同的指令模板来描述相同的任务。第三，对于更困难的任务，使用CoT监督来引导SFT模型进行推理。最后，通过实验评估SFT模型在不同设置下的泛化性能，并与RL基线进行比较。

**关键创新**：该研究的关键创新在于：1) 揭示了SFT泛化能力不足的原因是冻结提示伪影；2) 提出了通过引入提示多样性和CoT监督来提升SFT泛化能力的方法；3) 证明了在适当的数据和训练策略下，SFT可以达到甚至超过RL的泛化性能。

**关键设计**：在提示多样性方面，研究人员使用了不同的指令模板来描述相同的任务，例如使用不同的词语或句式。在CoT监督方面，研究人员提供了中间推理步骤的示例，以引导SFT模型进行推理。此外，研究人员还使用了标准的SFT训练流程，并对超参数进行了调整，以获得最佳性能。

## 📊 实验亮点

实验结果表明，引入提示多样性后，SFT模型在指令变体任务上的泛化能力显著提升，与RL基线相当。结合提示多样性和CoT监督后，SFT模型在难度变体任务上的表现甚至超过了RL基线。例如，在Sokoban游戏中，SFT模型在更大的网格和更多箱子的场景下取得了更好的性能。

## 🎯 应用场景

该研究成果可应用于各种需要决策能力的AI系统，例如游戏AI、机器人控制、自动驾驶等。通过提升SFT的泛化能力，可以降低对大量标注数据的依赖，并提高AI系统在复杂环境中的适应性。此外，该研究也为如何更好地利用SFT进行任务学习提供了新的思路。

## 📄 摘要（原文）

> A prevailing view holds that supervised fine-tuning (SFT) memorizes training data and fails to generalize, whereas reinforcement learning (RL) attains broader robustness. We revisit this claim through a systematic evaluation on two decision-making benchmarks, Sokoban and General Points, and arrive at a different conclusion. We show that much of SFT's perceived failure stems from frozen-prompt artifacts: when trained on fixed instruction templates, SFT models cling to training semantics rather than adapting to new ones. Introducing prompt diversity during training breaks this shortcut and yields strong generalization to unseen instruction variants without harming in-distribution performance. Beyond instruction shifts, we ask whether SFT can generalize to strictly harder tasks. Here, chain-of-thought (CoT) supervision provides an algorithmic scaffold that markedly improves transfer to more difficult regimes, such as larger Sokoban grids with additional boxes and arithmetic with out-of-distribution values or five-card compositions that increase combinatorial complexity. Finally, combining prompt diversity with CoT achieves the best of both worlds: robust generalization across both instruction-variant and difficulty-variant settings, matching or surpassing RL baselines on our benchmarks while retaining SFT's simplicity and stability. These findings challenge the narrative that SFT is inherently inferior to RL and support a data-centric perspective: with appropriately curated demonstrations, vanilla SFT can generalize as strongly as RL. Code reproducing the results in the paper can be found at: https://github.com/XiaofengLin7/debunking-sft-generalization.

