---
layout: default
title: Tractable Asymmetric Verification for Large Language Models via Deterministic Replicability
---

# Tractable Asymmetric Verification for Large Language Models via Deterministic Replicability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11068" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11068v1</a>
  <a href="https://arxiv.org/pdf/2509.11068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11068v1', 'Tractable Asymmetric Verification for Large Language Models via Deterministic Replicability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zan-Kai Chong, Hiroyuki Ohsaki, Bryan Ng

**分类**: cs.AI

**发布日期**: 2025-09-14

---

## 💡 一句话要点

**提出基于确定性可复制性的LLM非对称验证框架，降低验证成本。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `可信AI` `非对称验证` `确定性可复制性` `多智能体系统`

## 📋 核心要点

1. 现有LLM多智能体系统缺乏有效的验证机制，难以保证输出结果的真实性和可靠性。
2. 该论文提出基于确定性可复制性的非对称验证框架，降低验证成本，提高验证效率。
3. 实验表明，该方法比完全重新生成快12倍以上，并可通过参数调整检测概率。

## 📝 摘要（中文）

大型语言模型（LLM）正迅速发展为动态的多智能体系统。这带来了一个根本性的挑战，即如何建立计算信任，特别是如何验证一个智能体的输出确实是由其声称的LLM生成的，而不是伪造的或由更便宜或更差的模型生成的。为了应对这一挑战，本文提出了一个验证框架，该框架实现了可处理的非对称努力，其中验证计算的成本远低于执行计算的成本。我们的方法建立在确定性可复制性的原则之上，这是自回归模型固有的属性，严格要求计算同构环境，其中所有智能体在相同的硬件和软件堆栈上运行。在这个定义的上下文中，我们的框架允许多个验证者概率性地审计LLM输出的小型随机片段，并有效地分配验证工作负载。模拟表明，有针对性的验证比完全重新生成快12倍以上，并且具有可调参数来调整检测概率。通过为可审计的LLM系统建立一个可处理的机制，我们的工作为负责任的AI提供了一个基础层，并为未来对更复杂、异构的多智能体系统的研究奠定了基石。

## 🔬 方法详解

**问题定义**：在多智能体系统中，如何验证一个智能体的输出确实来自其声称的LLM，而不是来自更廉价或性能更差的模型，或者被恶意篡改？现有方法通常需要完全重新生成输出进行比对，计算成本高昂，难以实际应用。

**核心思路**：利用自回归模型的确定性可复制性，即在相同的硬件和软件环境下，给定相同的输入，LLM应该产生相同的输出。通过随机抽样LLM输出的一小部分进行验证，降低验证成本。

**技术框架**：该框架包含以下几个关键步骤：1) 确定计算同构环境，保证所有智能体运行在相同的硬件和软件堆栈上；2) 智能体生成LLM输出；3) 多个验证者随机抽样LLM输出的一小部分；4) 验证者独立重新生成抽样部分，并与原始输出进行比对；5) 根据比对结果，判断原始输出是否可信。

**关键创新**：该方法的核心创新在于利用了LLM的确定性可复制性，将验证问题转化为一个抽样检测问题，从而大大降低了验证成本。与传统的完全重新生成验证方法相比，该方法具有更高的效率和可扩展性。

**关键设计**：关键参数包括抽样比例（即验证者抽取的输出片段的长度占总输出长度的比例）、验证者数量以及检测概率阈值。抽样比例决定了验证的精度和成本，验证者数量决定了验证的可靠性，检测概率阈值决定了判断输出是否可信的标准。这些参数可以根据实际应用场景进行调整，以达到最佳的验证效果。

## 📊 实验亮点

实验结果表明，该方法在保证一定检测概率的前提下，验证速度比完全重新生成快12倍以上。通过调整抽样比例和验证者数量，可以灵活控制验证的精度和成本。该方法为LLM的非对称验证提供了一种高效可行的解决方案。

## 🎯 应用场景

该研究成果可应用于构建可信赖的LLM多智能体系统，例如在金融交易、医疗诊断等对安全性要求较高的领域。通过该验证框架，可以有效防止恶意攻击和欺诈行为，提高系统的可靠性和安全性。此外，该方法还可以用于评估不同LLM的性能和安全性，为LLM的开发和应用提供指导。

## 📄 摘要（原文）

> The landscape of Large Language Models (LLMs) shifts rapidly towards dynamic, multi-agent systems. This introduces a fundamental challenge in establishing computational trust, specifically how one agent can verify that another's output was genuinely produced by a claimed LLM, and not falsified or generated by a cheaper or inferior model. To address this challenge, this paper proposes a verification framework that achieves tractable asymmetric effort, where the cost to verify a computation is substantially lower than the cost to perform it. Our approach is built upon the principle of deterministic replicability, a property inherent to autoregressive models that strictly necessitates a computationally homogeneous environment where all agents operate on identical hardware and software stacks. Within this defined context, our framework enables multiple validators to probabilistically audit small, random segments of an LLM's output and it distributes the verification workload effectively. The simulations demonstrated that targeted verification can be over 12 times faster than full regeneration, with tunable parameters to adjust the detection probability. By establishing a tractable mechanism for auditable LLM systems, our work offers a foundational layer for responsible AI and serves as a cornerstone for future research into the more complex, heterogeneous multi-agent systems.

