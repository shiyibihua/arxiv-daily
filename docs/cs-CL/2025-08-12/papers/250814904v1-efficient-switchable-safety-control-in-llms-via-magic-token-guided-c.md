---
layout: default
title: Efficient Switchable Safety Control in LLMs via Magic-Token-Guided Co-Training
---

# Efficient Switchable Safety Control in LLMs via Magic-Token-Guided Co-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14904" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14904v1</a>
  <a href="https://arxiv.org/pdf/2508.14904.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14904v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14904v1', 'Efficient Switchable Safety Control in LLMs via Magic-Token-Guided Co-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianfeng Si, Lin Sun, Zhewen Tan, Xiangzheng Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-12

**备注**: 12 pages,5 figures,4 tables

---

## 💡 一句话要点

**提出统一共训练框架以提升大型语言模型的内容安全性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `内容安全` `共训练` `魔法令牌` `安全对齐` `动态切换` `深度学习` `模型优化`

## 📋 核心要点

1. 现有内容安全方法依赖多阶段训练，缺乏灵活的后期控制，影响模型的实用性。
2. 提出的共训练框架通过魔法令牌实现多种安全行为的动态切换，提升了模型的灵活性和可控性。
3. 实验结果显示，8B模型在安全性能上超越671B的DeepSeek-R1，同时降低了训练和部署成本。

## 📝 摘要（中文）

当前大型语言模型（LLMs）在内容安全方面的方法，如监督微调（SFT）和基于人类反馈的强化学习（RLHF），通常依赖于多阶段训练流程，缺乏细粒度的后期可控性。为了解决这些局限性，本文提出了一种统一的共训练框架，能够在单一的SFT阶段中高效整合多种安全行为：积极（合法/亲社会）、消极（未过滤/风险倾向）和拒绝（拒绝导向/保守）。每种行为通过简单的系统级指令或魔法令牌动态激活，实现推理时的隐秘和高效行为切换。这种灵活性支持多种部署场景，实验表明该方法在安全对齐质量上与SFT+DPO相当，且在安全性能上显著超越DeepSeek-R1，同时大幅降低训练复杂性和部署成本。

## 🔬 方法详解

**问题定义**：当前大型语言模型在内容安全方面的训练方法多依赖于复杂的多阶段流程，导致后期可控性不足，难以满足不同场景的需求。

**核心思路**：本文提出的共训练框架通过引入魔法令牌，实现了在单一SFT阶段中动态激活多种安全行为，从而提升了模型的灵活性和可控性。

**技术框架**：该框架整合了积极、消极和拒绝三种安全行为，使用魔法令牌作为指令，支持在推理时快速切换行为，适应不同的应用场景。

**关键创新**：最重要的创新在于引入了安全对齐边际的概念，通过明确的响应分布区分不同的安全模式，增强了模型的安全性和可控性。

**关键设计**：在训练过程中，设计了特定的损失函数以优化安全行为的分布，同时调整了模型的网络结构以支持魔法令牌的动态激活。具体参数设置和训练策略在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，提出的8B模型在安全性能上超越了DeepSeek-R1（671B），在安全对齐质量上与SFT+DPO相当，同时显著降低了训练复杂性和部署成本，展示了该方法的高效性和可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线客服系统和教育平台等，能够有效提升用户交互的安全性和可靠性。未来，随着模型的进一步优化，该框架有望在更广泛的场景中应用，推动内容安全技术的发展。

## 📄 摘要（原文）

> Current methods for content safety in Large Language Models (LLMs), such as Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF), often rely on multi-stage training pipelines and lack fine-grained, post-deployment controllability. To address these limitations, we propose a unified co-training framework that efficiently integrates multiple safety behaviors: positive (lawful/prosocial), negative (unfiltered/risk-prone) and rejective (refusal-oriented/conservative) within a single SFT stage. Notably, each behavior is dynamically activated via a simple system-level instruction, or magic token, enabling stealthy and efficient behavioral switching at inference time. This flexibility supports diverse deployment scenarios, such as positive for safe user interaction, negative for internal red-teaming, and rejective for context-aware refusals triggered by upstream moderation signals. This co-training strategy induces a distinct Safety Alignment Margin in the output space, characterized by well-separated response distributions corresponding to each safety mode. The existence of this margin provides empirical evidence for the model's safety robustness and enables unprecedented fine-grained control. Experiments show that our method matches the safety alignment quality of SFT+DPO, with our 8B model notably surpassing DeepSeek-R1 (671B) in safety performance, while significantly reducing both training complexity and deployment costs. This work presents a scalable, efficient, and highly controllable solution for LLM content safety.

