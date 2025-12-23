---
layout: default
title: Reinforcement Learning with Physics-Informed Symbolic Program Priors for Zero-Shot Wireless Indoor Navigation
---

# Reinforcement Learning with Physics-Informed Symbolic Program Priors for Zero-Shot Wireless Indoor Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22365" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22365v1</a>
  <a href="https://arxiv.org/pdf/2506.22365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22365v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22365v1', 'Reinforcement Learning with Physics-Informed Symbolic Program Priors for Zero-Shot Wireless Indoor Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Li, Haozhe Lei, Mingsheng Yin, Yaqi Hu

**分类**: cs.LG, cs.RO

**发布日期**: 2025-06-27

**备注**: Spotlight paper at Reinforcement Learning Conference 2025, Workshop on Inductive Biases in Reinforcement Learning

---

## 💡 一句话要点

**提出物理信息符号程序先验的强化学习框架以解决零样本室内导航问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `物理信息` `符号程序` `室内导航` `神经符号集成` `样本效率` `归纳偏置`

## 📋 核心要点

1. 现有方法在将物理先验融入强化学习中时，往往需要大量的人工干预和领域知识，限制了其普适性。
2. 本文提出了一种物理信息程序引导的强化学习框架（PiPRL），通过符号编程将物理先验以人类可读的形式整合进RL代理中。
3. 实验结果显示，PiPRL在室内导航任务中表现优异，训练时间减少超过26%，显著提升了样本效率和泛化能力。

## 📝 摘要（中文）

在使用强化学习（RL）解决物理控制任务时，编码物理先验的归纳偏置可以提高训练的样本效率并增强测试的泛化能力。然而，当前将这些物理信息归纳偏置纳入RL的做法不可避免地需要大量的人工劳动和领域专业知识，使其对普通用户而言难以实现。本研究探索了一种符号方法，将物理信息归纳偏置提炼到RL代理中，物理先验以人类可读且自然可解释的领域特定语言（DSL）表达。为了解决DSL先验无法直接转化为可实施策略的问题，我们开发了一个物理信息程序引导的RL（PiPRL）框架，应用于室内导航。PiPRL采用层次化和模块化的神经符号集成，元符号程序接收来自神经感知模块的语义特征，这些特征构成了编码物理先验并引导低级神经控制器RL过程的符号编程基础。大量实验表明，PiPRL在性能上始终优于纯符号或神经策略，并通过程序化的归纳偏置将训练时间减少了超过26%。

## 🔬 方法详解

**问题定义**：本研究旨在解决在物理控制任务中，如何有效地将物理先验融入强化学习代理的问题。现有方法通常依赖于大量的人工设计和领域知识，导致普适性差和效率低下。

**核心思路**：论文提出了一种符号方法，通过领域特定语言（DSL）将物理先验表达为可读的符号程序，从而减少对领域专家的依赖，并提高RL的样本效率和泛化能力。

**技术框架**：PiPRL框架采用层次化和模块化的设计，主要包括一个神经感知模块和一个元符号程序。神经感知模块提取语义特征，元符号程序则利用这些特征进行符号编程，最终引导低级神经控制器的RL过程。

**关键创新**：最重要的创新在于将物理信息归纳偏置以符号程序的形式引入RL中，形成了一种新的神经符号集成方法，与传统的纯符号或纯神经方法相比，显著提高了性能和效率。

**关键设计**：在设计中，使用了特定的损失函数来优化符号程序的生成，并通过模块化结构使得各个部分可以独立优化，确保了系统的灵活性和可扩展性。具体的网络结构和参数设置在实验中经过多次调优，以达到最佳效果。

## 📊 实验亮点

实验结果表明，PiPRL框架在室内导航任务中表现优于传统的纯符号或神经策略，训练时间减少超过26%。这一显著提升不仅提高了样本效率，还增强了模型的泛化能力，展示了物理信息归纳偏置在强化学习中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括室内导航、机器人控制和自动驾驶等场景。通过将物理先验有效整合进强化学习，能够显著提高系统的智能化水平和适应能力，未来可广泛应用于智能家居、无人机导航等实际场景，推动相关技术的发展。

## 📄 摘要（原文）

> When using reinforcement learning (RL) to tackle physical control tasks, inductive biases that encode physics priors can help improve sample efficiency during training and enhance generalization in testing. However, the current practice of incorporating these helpful physics-informed inductive biases inevitably runs into significant manual labor and domain expertise, making them prohibitive for general users. This work explores a symbolic approach to distill physics-informed inductive biases into RL agents, where the physics priors are expressed in a domain-specific language (DSL) that is human-readable and naturally explainable. Yet, the DSL priors do not translate directly into an implementable policy due to partial and noisy observations and additional physical constraints in navigation tasks. To address this gap, we develop a physics-informed program-guided RL (PiPRL) framework with applications to indoor navigation. PiPRL adopts a hierarchical and modularized neuro-symbolic integration, where a meta symbolic program receives semantically meaningful features from a neural perception module, which form the bases for symbolic programming that encodes physics priors and guides the RL process of a low-level neural controller. Extensive experiments demonstrate that PiPRL consistently outperforms purely symbolic or neural policies and reduces training time by over 26% with the help of the program-based inductive biases.

