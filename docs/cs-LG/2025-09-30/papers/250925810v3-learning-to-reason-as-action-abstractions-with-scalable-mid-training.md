---
layout: default
title: Learning to Reason as Action Abstractions with Scalable Mid-Training RL
---

# Learning to Reason as Action Abstractions with Scalable Mid-Training RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25810" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25810v3</a>
  <a href="https://arxiv.org/pdf/2509.25810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25810v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25810v3', 'Learning to Reason as Action Abstractions with Scalable Mid-Training RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shenao Zhang, Donghan Yu, Yihao Feng, Bowen Jin, Zhaoran Wang, John Peebles, Zirui Wang

**分类**: cs.LG, cs.AI, cs.CL, stat.ML

**发布日期**: 2025-09-30 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出RA3算法，通过可扩展的中期训练强化学习提升代码生成任务性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `大型语言模型` `动作抽象` `中期训练` `代码生成`

## 📋 核心要点

1. 现有方法难以充分利用大型语言模型在强化学习中的潜力，尤其缺乏有效的中期训练策略。
2. RA3算法通过强化学习发现时间一致的潜在结构，并基于此进行微调，从而实现高效的动作抽象。
3. 实验表明，RA3在代码生成任务上显著优于基线模型，并在多个数据集上实现了更快的收敛和更高的性能。

## 📝 摘要（中文）

大型语言模型在强化学习中表现出色，但要充分发挥其潜力，需要一个中期训练阶段。有效的中期训练阶段应识别出一组紧凑且有用的动作，并通过在线强化学习实现它们之间的快速选择。本文提出了首个关于中期训练如何塑造后期训练的理论结果：它描述了一个动作子空间，该子空间可最大限度地减少剪枝带来的价值近似误差以及后续规划期间的强化学习误差。分析表明，中期训练效果的两个关键决定因素是：剪枝效率（它塑造了初始强化学习策略的先验）及其对强化学习收敛的影响（它决定了该策略可以通过在线交互改进的程度）。这些结果表明，当决策空间紧凑且有效范围较短时，中期训练最有效，突出了在动作抽象空间而不是原始动作空间中操作的重要性。基于这些见解，本文提出了一种可扩展的中期训练算法，即推理即动作抽象（RA3）。具体来说，推导了一个序列变分下界，并通过迭代地发现时间一致的潜在结构（通过强化学习）来优化它，然后在引导数据上进行微调。在代码生成任务上的实验证明了该方法的有效性。在多个基础模型上，RA3在HumanEval和MBPP上的平均性能比基础模型和下一个token预测基线提高了8和4个点。此外，RA3在HumanEval+、MBPP+、LiveCodeBench和Codeforces上的RLVR中实现了更快的收敛速度和更高的渐近性能。

## 🔬 方法详解

**问题定义**：现有方法在利用大型语言模型进行强化学习时，通常直接在原始动作空间进行操作，导致决策空间庞大、探索效率低下，难以充分发挥大型语言模型的潜力。此外，缺乏对中期训练阶段的理论指导，难以设计有效的训练策略。

**核心思路**：本文的核心思路是将推理过程视为一系列动作抽象，通过中期训练学习一个紧凑的动作子空间，从而降低决策复杂度，提高强化学习的效率。通过理论分析，揭示了剪枝效率和RL收敛对中期训练效果的关键影响，并据此设计了RA3算法。

**技术框架**：RA3算法包含两个主要阶段：动作抽象发现和策略优化。首先，通过强化学习迭代地发现时间一致的潜在结构，构建动作抽象空间。然后，在引导数据上对策略进行微调，优化动作选择策略。整体流程可以看作是一个序列变分下界的优化过程。

**关键创新**：RA3的关键创新在于将推理过程建模为动作抽象，并提出了一种可扩展的中期训练算法来学习这些抽象。与直接在原始动作空间进行强化学习的方法相比，RA3能够更有效地探索和利用大型语言模型的知识。此外，本文还提供了关于中期训练的理论分析，为算法设计提供了指导。

**关键设计**：RA3算法的关键设计包括：1) 使用强化学习来发现时间一致的潜在结构，确保动作抽象的时序一致性；2) 通过序列变分下界来指导训练过程，平衡探索和利用；3) 在引导数据上进行微调，提高策略的泛化能力。具体的损失函数和网络结构细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

RA3算法在代码生成任务上取得了显著的性能提升。在HumanEval和MBPP数据集上，RA3的平均性能比基础模型和下一个token预测基线分别提高了8和4个点。此外，RA3在HumanEval+、MBPP+、LiveCodeBench和Codeforces等数据集上的RLVR实验中，实现了更快的收敛速度和更高的渐近性能，验证了其有效性。

## 🎯 应用场景

RA3算法可应用于各种需要复杂推理和决策的任务，例如代码生成、游戏AI、机器人控制等。通过学习有效的动作抽象，RA3能够提高强化学习的效率和性能，从而解决更复杂的问题。该研究有助于推动大型语言模型在强化学习领域的应用，并为开发更智能的AI系统提供新的思路。

## 📄 摘要（原文）

> Large language models excel with reinforcement learning (RL), but fully unlocking this potential requires a mid-training stage. An effective mid-training phase should identify a compact set of useful actions and enable fast selection among them through online RL. We formalize this intuition by presenting the first theoretical result on how mid-training shapes post-training: it characterizes an action subspace that minimizes both the value approximation error from pruning and the RL error during subsequent planning. Our analysis reveals two key determinants of mid-training effectiveness: pruning efficiency, which shapes the prior of the initial RL policy, and its impact on RL convergence, which governs the extent to which that policy can be improved via online interactions. These results suggest that mid-training is most effective when the decision space is compact and the effective horizon is short, highlighting the importance of operating in the space of action abstractions rather than primitive actions. Building on these insights, we propose Reasoning as Action Abstractions (RA3), a scalable mid-training algorithm. Specifically, we derive a sequential variational lower bound and optimize it by iteratively discovering temporally-consistent latent structures via RL, followed by fine-tuning on the bootstrapped data. Experiments on code generation tasks demonstrate the effectiveness of our approach. Across multiple base models, RA3 improves the average performance on HumanEval and MBPP by 8 and 4 points over the base model and the next-token prediction baseline. Furthermore, RA3 achieves faster convergence and higher asymptotic performance in RLVR on HumanEval+, MBPP+, LiveCodeBench, and Codeforces.

