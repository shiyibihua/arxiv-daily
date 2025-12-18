---
layout: default
title: Factorizing Diffusion Policies for Observation Modality Prioritization
---

# Factorizing Diffusion Policies for Observation Modality Prioritization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16830" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16830v1</a>
  <a href="https://arxiv.org/pdf/2509.16830.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16830v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16830v1', 'Factorizing Diffusion Policies for Observation Modality Prioritization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Omkar Patil, Prabin Rath, Kartikay Pangaonkar, Eric Rosen, Nakul Gopalan

**分类**: cs.RO

**发布日期**: 2025-09-20

**备注**: 14 pages; website: https://fdp-policy.github.io/fdp-policy/

**🔗 代码/项目**: [PROJECT_PAGE](https://fdp-policy.github.io/fdp-policy/)

---

## 💡 一句话要点

**提出因子分解扩散策略FDP，实现机器人策略中观测模态的优先级排序。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `扩散模型` `机器人策略` `模态优先级` `因子分解` `鲁棒性` `低数据学习` `视觉运动` `条件作用`

## 📋 核心要点

1. 现有扩散策略无法有效区分不同观测模态（如视觉、触觉）对机器人任务的不同影响程度。
2. FDP通过因子分解观测模态的条件作用，使策略能够学习并优先考虑对特定任务更重要的模态。
3. 实验表明，FDP在低数据和分布偏移情况下，显著提升了策略的性能和鲁棒性，优于标准扩散策略。

## 📝 摘要（中文）

扩散模型已被广泛用于从演示中学习机器人技能。这些策略通常以多种观测模态为条件，如本体感受、视觉和触觉。然而，不同观测模态对不同任务的影响程度不同，而扩散策略未能捕捉到这一点。本文提出了一种名为“因子分解扩散策略”（FDP）的新型策略，该策略通过设计使观测模态对动作扩散过程产生不同的影响。这使得学习到的策略能够优先考虑某些观测模态，例如视觉>触觉或本体感受>视觉。FDP通过分解扩散过程的观测条件来实现模态优先级排序，从而产生更高效和鲁棒的策略。在低数据情况下，与联合调节所有输入模态的标准扩散策略相比，我们的因子分解方法在多个模拟基准测试中显示出强大的性能改进，成功率绝对提高了15%。此外，我们的基准测试和真实世界实验表明，因子分解策略在视觉干扰或相机遮挡等分布偏移下，具有更高的鲁棒性，在多个视觉运动任务中的绝对成功率提高了40%，而现有的扩散策略则彻底失败。因此，FDP为实际部署提供了一种比标准扩散策略更安全、更稳健的替代方案。

## 🔬 方法详解

**问题定义**：现有的基于扩散模型的机器人策略通常将所有观测模态（如本体感受、视觉、触觉）平等对待，联合作为扩散模型的条件输入。然而，在实际任务中，不同模态的重要性往往不同，例如视觉在某些任务中可能比触觉更关键。这种平等对待的方式限制了策略的性能和鲁棒性，尤其是在数据量有限或环境发生变化时。

**核心思路**：FDP的核心思想是将观测模态的条件作用进行因子分解，使得每个模态可以独立地影响扩散过程。通过这种方式，策略可以学习到不同模态的权重，并优先考虑对当前任务更重要的模态。这种设计允许策略在低数据情况下更快地学习，并在环境变化时保持鲁棒性。

**技术框架**：FDP的整体框架仍然基于扩散模型，但其关键在于条件作用的方式。传统的扩散策略将所有观测模态连接起来，然后输入到扩散模型中。而FDP将每个观测模态分别输入到独立的网络中，得到每个模态的embedding。然后，这些embedding被融合起来，作为扩散模型的条件输入。融合的方式可以是简单的拼接，也可以是更复杂的注意力机制。

**关键创新**：FDP最重要的技术创新点在于观测模态条件作用的因子分解。这种分解使得策略可以学习到不同模态的权重，并根据任务的需求动态地调整这些权重。与现有方法相比，FDP能够更好地利用有限的数据，并在环境变化时保持鲁棒性。

**关键设计**：FDP的关键设计包括：1) 每个观测模态对应的独立网络结构，用于提取模态特征；2) 融合不同模态embedding的方式，例如使用注意力机制来动态调整模态权重；3) 损失函数的设计，鼓励策略学习到对任务更重要的模态。

## 📊 实验亮点

FDP在多个模拟基准测试中，与标准扩散策略相比，成功率绝对提高了15%。在视觉干扰或相机遮挡等分布偏移下，FDP的绝对成功率提高了40%，而现有扩散策略则性能急剧下降。这些结果表明，FDP在低数据和环境变化的情况下，具有更强的鲁棒性和泛化能力。

## 🎯 应用场景

FDP适用于各种需要机器人与环境交互的场景，尤其是在数据获取成本高昂或环境存在不确定性的情况下。例如，在医疗机器人手术、家庭服务机器人、以及工业自动化等领域，FDP可以帮助机器人更有效地学习和执行任务，提高安全性和可靠性。此外，FDP的模态优先级排序能力也使其在多模态传感器融合方面具有潜在的应用价值。

## 📄 摘要（原文）

> Diffusion models have been extensively leveraged for learning robot skills from demonstrations. These policies are conditioned on several observational modalities such as proprioception, vision and tactile. However, observational modalities have varying levels of influence for different tasks that diffusion polices fail to capture. In this work, we propose 'Factorized Diffusion Policies' abbreviated as FDP, a novel policy formulation that enables observational modalities to have differing influence on the action diffusion process by design. This results in learning policies where certain observations modalities can be prioritized over the others such as $\texttt{vision>tactile}$ or $\texttt{proprioception>vision}$. FDP achieves modality prioritization by factorizing the observational conditioning for diffusion process, resulting in more performant and robust policies. Our factored approach shows strong performance improvements in low-data regimes with $15\%$ absolute improvement in success rate on several simulated benchmarks when compared to a standard diffusion policy that jointly conditions on all input modalities. Moreover, our benchmark and real-world experiments show that factored policies are naturally more robust with $40\%$ higher absolute success rate across several visuomotor tasks under distribution shifts such as visual distractors or camera occlusions, where existing diffusion policies fail catastrophically. FDP thus offers a safer and more robust alternative to standard diffusion policies for real-world deployment. Videos are available at https://fdp-policy.github.io/fdp-policy/ .

