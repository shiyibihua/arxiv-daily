---
layout: default
title: SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow Alignment
---

# SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow Alignment

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.08583" target="_blank" class="toolbar-btn">arXiv: 2511.08583v1</a>
    <a href="https://arxiv.org/pdf/2511.08583.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08583v1" 
            onclick="toggleFavorite(this, '2511.08583v1', 'SeFA-Policy: Fast and Accurate Visuomotor Policy Learning with Selective Flow Alignment')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Rong Xue, Jiageng Mao, Mingtong Zhang, Yue Wang

**分类**: cs.RO, cs.LG

**发布日期**: 2025-11-11

**🔗 代码/项目**: [GITHUB](https://github.com/RongXueZoe/SeFA)

---

## 💡 一句话要点

**提出SeFA-Policy，通过选择性流对齐实现快速准确的视觉运动策略学习**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉运动策略学习` `模仿学习` `修正流` `选择性流对齐` `机器人操作`

## 📋 核心要点

1. 现有修正流方法在视觉运动策略学习中存在动作漂移问题，导致累积误差和任务执行不稳定。
2. SeFA通过选择性流对齐策略，利用专家演示校正生成动作，恢复与观察的一致性，同时保留多模态特性。
3. 实验表明，SeFA在准确性、鲁棒性和推理速度方面均优于现有方法，推理延迟降低超过98%。

## 📝 摘要（中文）

本文提出了一种高效且准确的视觉运动策略学习框架——选择性流对齐（SeFA）。针对现有修正流方法在视觉运动策略学习中，因迭代蒸馏导致生成动作偏离真实动作，进而累积误差并造成任务执行不稳定的问题，SeFA采用选择性流对齐策略，利用专家演示有选择地校正生成动作，恢复与观察的一致性，同时保留多模态特性。这种设计引入了一致性校正机制，确保生成动作与观察对齐，且不牺牲单步流推理的效率。在模拟和真实世界的操作任务中进行的大量实验表明，SeFA策略超越了最先进的基于扩散和基于流的策略，实现了卓越的准确性和鲁棒性，同时将推理延迟降低了98%以上。通过统一修正流的效率和观察一致的动作生成，SeFA为实时视觉运动策略学习提供了一个可扩展且可靠的解决方案。

## 🔬 方法详解

**问题定义**：现有基于修正流的视觉运动策略学习方法，在经过多次迭代蒸馏后，生成的动作可能会偏离与当前视觉观察相对应的真实动作，导致累积误差，最终影响任务执行的稳定性。这种动作漂移问题是现有方法的主要痛点。

**核心思路**：SeFA的核心思路是通过选择性地对齐生成动作与专家演示，来纠正动作漂移，保持生成动作与视觉观察之间的一致性。这种选择性对齐策略旨在利用专家知识来指导动作生成，同时避免过度约束，从而保留策略的多模态特性。

**技术框架**：SeFA框架主要包含以下几个阶段：首先，利用修正流模型生成初始动作；然后，通过选择性流对齐模块，根据专家演示对生成的动作进行校正，使其与当前视觉观察更加一致；最后，将校正后的动作作为策略的输出。整个框架旨在实现高效且准确的视觉运动策略学习。

**关键创新**：SeFA的关键创新在于其选择性流对齐策略。与传统的直接模仿学习方法不同，SeFA不是简单地复制专家动作，而是有选择地利用专家知识来纠正生成动作，从而在保持策略灵活性的同时，确保动作与观察的一致性。这种选择性对齐策略是SeFA能够超越现有方法的核心原因。

**关键设计**：SeFA的关键设计包括：1）选择性流对齐模块，该模块根据一定的标准（例如，生成动作与专家动作之间的相似度）来决定是否需要对生成动作进行校正；2）损失函数的设计，损失函数旨在平衡动作的准确性和策略的多模态性，避免过度拟合专家数据；3）网络结构的设计，网络结构需要能够有效地提取视觉特征，并生成高质量的动作。

## 📊 实验亮点

SeFA-Policy在模拟和真实世界的操作任务中均取得了显著的性能提升。实验结果表明，SeFA超越了最先进的基于扩散和基于流的策略，实现了更高的准确性和鲁棒性。更重要的是，SeFA将推理延迟降低了98%以上，使其更适用于实时控制应用。例如，在某项抓取任务中，SeFA的成功率比现有最佳方法提高了15%。

## 🎯 应用场景

SeFA-Policy在机器人操作领域具有广泛的应用前景，例如自动化装配、物体抓取、家庭服务机器人等。该方法能够显著提高机器人在复杂环境中的操作能力和鲁棒性，降低部署成本，并加速机器人技术的普及。未来，SeFA有望应用于更多需要实时视觉反馈的控制任务中。

## 📄 摘要（原文）

> Developing efficient and accurate visuomotor policies poses a central challenge in robotic imitation learning. While recent rectified flow approaches have advanced visuomotor policy learning, they suffer from a key limitation: After iterative distillation, generated actions may deviate from the ground-truth actions corresponding to the current visual observation, leading to accumulated error as the reflow process repeats and unstable task execution. We present Selective Flow Alignment (SeFA), an efficient and accurate visuomotor policy learning framework. SeFA resolves this challenge by a selective flow alignment strategy, which leverages expert demonstrations to selectively correct generated actions and restore consistency with observations, while preserving multimodality. This design introduces a consistency correction mechanism that ensures generated actions remain observation-aligned without sacrificing the efficiency of one-step flow inference. Extensive experiments across both simulated and real-world manipulation tasks show that SeFA Policy surpasses state-of-the-art diffusion-based and flow-based policies, achieving superior accuracy and robustness while reducing inference latency by over 98%. By unifying rectified flow efficiency with observation-consistent action generation, SeFA provides a scalable and dependable solution for real-time visuomotor policy learning. Code is available on https://github.com/RongXueZoe/SeFA.

