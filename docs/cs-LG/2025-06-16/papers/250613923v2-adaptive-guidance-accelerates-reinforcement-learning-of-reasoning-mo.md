---
layout: default
title: Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models
---

# Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13923" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13923v2</a>
  <a href="https://arxiv.org/pdf/2506.13923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13923v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13923v2', 'Adaptive Guidance Accelerates Reinforcement Learning of Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vaskar Nath, Elaine Lau, Anisha Gunjal, Manasi Sharma, Nikhil Baharte, Sean Hendryx

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-16 (更新: 2025-06-20)

---

## 💡 一句话要点

**提出自适应引导方法以加速推理模型的强化学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自适应引导` `强化学习` `推理模型` `能力提升` `自蒸馏`

## 📋 核心要点

1. 现有的推理模型在解决新问题时表现不佳，尤其是在高复杂度任务中。
2. 论文提出的$	ext{Guide}$方法通过自适应引导模型学习新问题，结合自然语言提示以提升模型性能。
3. 实验结果表明，$	ext{Guide}$在7B和32B参数模型上相较于传统方法提升了最多4%的宏平均性能，尤其在数学基准测试中表现突出。

## 📝 摘要（中文）

本研究探讨了通过可验证奖励进行强化学习的推理模型如何学习解决新问题的过程。研究发现，强化学习驱动性能的主要方式有两种：一是将pass@$k$压缩为pass@1，二是通过“能力提升”使模型能够解决之前无法解决的新问题。尽管能力提升在不同规模的模型中普遍存在，但学习新问题主要依赖自蒸馏。我们在超过500,000个数学、科学和代码领域的推理问题上验证了这些发现，并提出了一种新的在线训练算法$	ext{Guide}$，该算法通过自适应地将提示融入模型上下文中来优化策略。我们还展示了$	ext{Guide}$在不同参数规模模型上的有效性，显著提高了通用性。

## 🔬 方法详解

**问题定义**：本研究旨在解决推理模型在强化学习过程中对新问题的学习能力不足的问题。现有方法在高复杂度任务中表现不佳，尤其是在模型未见过的情境下。

**核心思路**：论文提出的核心思路是通过自适应引导（$	ext{Guide}$）将自然语言提示融入模型上下文中，帮助模型在解决新问题时更有效地利用已有知识。这样的设计旨在提高模型的学习效率和解决能力。

**技术框架**：整体架构包括模型的自蒸馏过程、引导提示的集成以及重要性采样的调整。具体流程为：首先识别所有初始错误的回合，然后将提示信息融入上下文中，最后优化策略以适应没有提示的情境。

**关键创新**：最重要的技术创新在于引入了自适应引导机制，使得模型在面对新问题时能够动态调整学习策略，与传统的静态学习方法形成鲜明对比。

**关键设计**：在参数设置上，$	ext{Guide}$方法针对不同模型规模（如7B和32B参数）进行了优化，损失函数设计上考虑了引导提示的影响，并在网络结构中引入了自蒸馏机制以提升学习效率。

## 📊 实验亮点

实验结果显示，使用$	ext{Guide}$方法的7B和32B参数模型在数学基准测试中相较于传统方法提高了最多4%的宏平均性能，验证了该方法在提升模型推理能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、科学计算和编程辅助等，能够帮助推理模型在复杂任务中更好地理解和解决问题。未来，这种自适应引导方法可能会在更广泛的人工智能应用中发挥重要作用，提升模型的通用性和适应性。

## 📄 摘要（原文）

> We study the process through which reasoning models trained with reinforcement learning on verifiable rewards (RLVR) can learn to solve new problems. We find that RLVR drives performance in two main ways: (1) by compressing pass@$k$ into pass@1 and (2) via "capability gain" in which models learn to solve new problems that they previously could not solve even at high $k$. We find that while capability gain exists across model scales, learning to solve new problems is primarily driven through self-distillation. We demonstrate these findings across model scales ranging from 0.5B to 72B parameters on >500,000 reasoning problems with prompts and verifiable final answers across math, science, and code domains. We further show that we can significantly improve pass@$k$ rates by leveraging natural language guidance for the model to consider within context while still requiring the model to derive a solution chain from scratch. Based of these insights, we derive $\text{Guide}$ -- a new class of online training algorithms. $\text{Guide}$ adaptively incorporates hints into the model's context on problems for which all rollouts were initially incorrect and adjusts the importance sampling ratio for the "off-policy" trajectories in order to optimize the policy for contexts in which the hints are no longer present. We describe variants of $\text{Guide}$ for GRPO and PPO and empirically show that Guide-GRPO on 7B and 32B parameter models improves generalization over its vanilla counterpart with up to 4$\%$ macro-average improvement across math benchmarks. We include careful ablations to analyze $\text{Guide}$'s components and theoretically analyze Guide's learning efficiency.

