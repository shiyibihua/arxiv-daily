---
layout: default
title: Sample-efficient LLM Optimization with Reset Replay
---

# Sample-efficient LLM Optimization with Reset Replay

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06412" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06412v2</a>
  <a href="https://arxiv.org/pdf/2508.06412.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06412v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06412v2', 'Sample-efficient LLM Optimization with Reset Replay')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zichuan Liu, Jinyu Wang, Lei Song, Jiang Bian

**分类**: cs.LG, cs.CL

**发布日期**: 2025-08-08 (更新: 2025-08-14)

---

## 💡 一句话要点

**提出LLM优化方法LoRR以解决样本效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `样本效率` `重置重放` `偏好优化` `强化学习`

## 📋 核心要点

1. 现有的后训练LLM优化方法在样本效率和过拟合方面存在显著不足，影响了模型的推理能力。
2. 本文提出的LoRR方法通过高重放训练和周期性重置策略，旨在提高样本利用效率并减少过拟合风险。
3. 实验结果显示，LoRR在数学任务上与复杂的RL算法相比，表现出更优的性能，验证了其有效性。

## 📝 摘要（中文）

近年来，后训练大型语言模型（LLMs）的进展，尤其是通过强化学习（RL）和偏好优化方法，推动了其推理能力的提升。然而，这些方法常常面临样本效率低和初始经验过拟合导致的首因偏差问题。为了解决这些挑战，本文提出了LLM优化的重置重放（LoRR）方法，旨在提高任何基于偏好的优化框架的样本效率。LoRR的核心机制允许在高重放次数下进行训练，最大化每个数据批次的利用率，并通过周期性重置策略来对抗过拟合风险。此外，LoRR结合了监督微调和基于偏好的损失，进一步增强数据利用。实验表明，LoRR显著提升了多种偏好优化方法在数学和一般推理基准上的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决后训练LLM优化中的样本效率低和过拟合问题。现有方法在高重放训练中容易导致模型质量下降，影响学习过程。

**核心思路**：LoRR通过引入重置重放机制，允许在高重放次数下训练，同时通过周期性重置初始数据来保持网络的可塑性，从而提高样本利用效率。

**技术框架**：LoRR的整体架构包括数据收集、重放机制和优化目标三个主要模块。数据收集阶段获取初始数据，重放机制通过高重放次数和周期性重置来优化训练，最后通过混合优化目标进行模型更新。

**关键创新**：LoRR的核心创新在于其重置重放策略和混合优化目标的结合，这与传统的偏好优化方法有本质区别，能够有效减少过拟合并提升样本利用率。

**关键设计**：在LoRR中，重放次数的设置和周期性重置的频率是关键参数，损失函数结合了监督微调和偏好损失，以增强数据的利用效率。

## 📊 实验亮点

实验结果表明，使用LoRR的迭代DPO方法在复杂数学任务上达到了与一些计算密集型RL算法相当的性能，展示了LoRR在样本效率和推理能力上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等。通过提高样本效率，LoRR能够在数据稀缺的场景中显著提升模型性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent advancements in post-training Large Language Models (LLMs), particularly through Reinforcement Learning (RL) and preference optimization methods, are key drivers for enhancing their reasoning capabilities. However, these methods are often plagued by low sample efficiency and a susceptibility to primacy bias, where overfitting to initial experiences degrades policy quality and damages the learning process. To address these challenges, we introduce LLM optimization with Reset Replay (LoRR), a general and powerful plugin designed to enhance sample efficiency in any preference-based optimization framework. LoRR core mechanism enables training at a high replay number, maximizing the utility of each collected data batch. To counteract the risk of overfitting inherent in high-replay training, LoRR incorporates a periodic reset strategy with reusing initial data, which preserves network plasticity. Furthermore, it leverages a hybrid optimization objective, combining supervised fine-tuning (SFT) and preference-based losses to further bolster data exploitation. Our extensive experiments demonstrate that LoRR significantly boosts the performance of various preference optimization methods on both mathematical and general reasoning benchmarks. Notably, an iterative DPO approach augmented with LoRR achieves comparable performance on challenging math tasks, outperforming some complex and computationally intensive RL-based algorithms. These findings highlight that LoRR offers a practical, sample-efficient, and highly effective paradigm for LLM finetuning, unlocking greater performance from limited data.

