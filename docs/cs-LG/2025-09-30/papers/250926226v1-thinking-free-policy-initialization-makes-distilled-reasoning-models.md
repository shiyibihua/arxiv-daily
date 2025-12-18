---
layout: default
title: Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners
---

# Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26226" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26226v1</a>
  <a href="https://arxiv.org/pdf/2509.26226.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26226v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26226v1', 'Thinking-Free Policy Initialization Makes Distilled Reasoning Models More Effective and Efficient Reasoners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Xu, Cliveb AI, Kai Yang, Tianhao Chen, Yang Wang, Saiyong Yang, Can Yang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出TFPI，加速RLVR训练，提升推理模型效率与性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `链式思维` `策略初始化` `模型蒸馏` `推理效率`

## 📋 核心要点

1. RLVR解决复杂任务有效，但训练时上下文长度要求高，计算成本巨大。
2. TFPI通过*ThinkFree*操作显式丢弃思维内容，减少推理token使用，连接CoT蒸馏和RLVR。
3. 实验表明，TFPI加速RL收敛，提升性能上限，并产生更节省token的推理模型。

## 📝 摘要（中文）

基于可验证奖励的强化学习(RLVR)能够有效解决复杂任务，但训练时需要极长的上下文长度，导致巨大的计算成本。多阶段训练虽然可以部分缓解这个问题，但从过短的上下文开始训练往往会导致不可逆转的性能下降，最终无法显著降低整体训练计算量。本文提出了一种简单而有效的RLVR改进方法——无思维策略初始化(TFPI)，它连接了长链式思维(CoT)蒸馏和标准RLVR。TFPI采用简单的*ThinkFree*操作，通过直接添加*</think>*来显式丢弃思维内容，从而减少推理期间的token使用量。使用*ThinkFree*调整后的输入进行训练可以提高性能并降低token消耗，即使在原始的慢速思维模式下也是如此。在各种基准测试中进行的大量实验表明，TFPI加速了RL收敛，实现了更高的性能上限，并产生了更节省token的推理模型，而无需专门的奖励或复杂的训练设计。仅使用TFPI，我们训练了一个4B模型，使用不到4K H20小时，在AIME24上达到89.0%的准确率，在LiveCodeBench上达到65.5%的准确率。

## 🔬 方法详解

**问题定义**：RLVR在解决复杂推理任务时，需要极长的上下文长度，导致训练计算成本非常高昂。虽然多阶段训练可以缓解，但如果初始阶段使用过短的上下文，会导致性能不可逆转的下降，无法有效降低整体训练成本。现有方法难以在保证性能的同时，降低计算资源消耗。

**核心思路**：TFPI的核心思路是在训练初期，通过引入*ThinkFree*操作，显式地截断模型的思考过程，减少token的使用。这使得模型能够在较短的上下文长度下进行有效的策略学习，避免了因上下文过短导致的性能下降。通过逐步增加上下文长度，最终实现高性能和高效率的推理模型。

**技术框架**：TFPI方法主要包含以下几个阶段：1) 使用CoT数据进行蒸馏训练，初始化模型；2) 在训练过程中，引入*ThinkFree*操作，即在输入序列中直接添加*</think>*标签，强制模型停止思考，直接输出答案；3) 使用RLVR进行强化学习，优化模型策略。整个框架旨在平衡训练效率和模型性能。

**关键创新**：TFPI的关键创新在于*ThinkFree*操作的引入。它允许模型在训练初期快速学习策略，避免了因上下文长度不足导致的性能瓶颈。与传统的RLVR方法相比，TFPI能够显著降低训练所需的计算资源，并提高模型的推理效率。

**关键设计**：*ThinkFree*操作的具体实现是在输入序列中添加一个特殊的token *</think>*，该token指示模型停止思考，直接输出答案。在训练过程中，可以调整*ThinkFree*操作的频率，以平衡训练效率和模型性能。论文中没有明确提及损失函数和网络结构的特殊设计，推测沿用了RLVR的常用设置。

## 📊 实验亮点

实验结果表明，使用TFPI方法训练的4B模型，在AIME24上达到了89.0%的准确率，在LiveCodeBench上达到了65.5%的准确率，而训练时间仅为不到4K H20小时。这表明TFPI能够显著加速RL收敛，提高模型性能，并降低训练成本。与没有使用TFPI的基线模型相比，性能和效率均有显著提升。

## 🎯 应用场景

TFPI方法可以应用于各种需要复杂推理的任务，例如数学问题求解、代码生成、知识图谱推理等。该方法能够降低训练成本，提高模型推理效率，使得大规模推理模型的部署和应用成为可能。未来，该方法可以进一步扩展到其他强化学习场景，例如机器人控制、游戏AI等。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Reward (RLVR) effectively solves complex tasks but demands extremely long context lengths during training, leading to substantial computational costs. While multi-stage training can partially mitigate this, starting with overly short contexts often causes irreversible performance degradation, ultimately failing to reduce overall training compute significantly. In this paper, we introduce **T**hinking-**F**ree **P**olicy **I**nitialization (**TFPI**), a simple yet effective adaptation to RLVR that bridges long Chain-of-Thought (CoT) distillation and standard RLVR. TFPI employs a simple *ThinkFree* operation, explicitly discarding the thinking content via a direct *</think>* append, to reduce token usage during inference. Training with *ThinkFree*-adapted inputs improves performance and lowers token consumption, even in the original slow-thinking mode. Extensive experiments across various benchmarks have shown that TFPI accelerates RL convergence, achieves a higher performance ceiling, and yields more token-efficient reasoning models without specialized rewards or complex training designs. With TFPI only, we train a 4B model to reach 89.0% accuracy on AIME24 and 65.5% on LiveCodeBench using less than 4K H20 hours.

