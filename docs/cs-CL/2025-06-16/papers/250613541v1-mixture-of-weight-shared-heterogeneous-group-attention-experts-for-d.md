---
layout: default
title: Mixture of Weight-shared Heterogeneous Group Attention Experts for Dynamic Token-wise KV Optimization
---

# Mixture of Weight-shared Heterogeneous Group Attention Experts for Dynamic Token-wise KV Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13541" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13541v1</a>
  <a href="https://arxiv.org/pdf/2506.13541.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13541v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13541v1', 'Mixture of Weight-shared Heterogeneous Group Attention Experts for Dynamic Token-wise KV Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanghui Song, Dongping Liao, Yiren Zhao, Kejiang Ye, Cheng-zhong Xu, Xitong Gao

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出mixSGA以解决Transformer模型动态KV优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Transformer` `动态优化` `混合专家` `键值缓存` `自然语言处理` `资源分配` `模型效率`

## 📋 核心要点

1. 现有方法在动态资源分配上存在不足，无法有效处理token的重要性变化，导致资源浪费。
2. mixSGA通过动态路由机制和权重共享策略，优化token的计算和内存分配，避免了低优先级token的丢弃。
3. 在Llama3、TinyLlama等模型上，mixSGA在指令跟随和持续预训练任务中表现优越，ROUGE-L更高且困惑度更低。

## 📝 摘要（中文）

Transformer模型在因果语言建模中面临可扩展性挑战，主要由于对不断增长的键值(KV)缓存的内存分配效率低下，导致计算和存储资源紧张。现有方法如分组查询注意力(GQA)和基于token的KV优化虽然提高了效率，但依赖于刚性的资源分配，常常丢弃“低优先级”token或静态分组，未能有效应对token重要性的动态变化。为此，本文提出了一种新颖的混合专家(moE)方法mixSGA，能够动态优化token级别的计算和内存分配。与以往方法不同，mixSGA保留所有token，并根据学习到的重要性分数自适应地将其路由到具有不同KV组大小的专业专家，从而在粒度和效率之间取得平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决Transformer模型在因果语言建模中因KV缓存内存分配效率低下而导致的可扩展性问题。现有方法如GQA和token级KV优化在资源分配上过于刚性，常常丢弃低优先级token，无法适应token重要性的动态变化。

**核心思路**：mixSGA的核心思路是通过动态优化token级别的计算和内存分配，保留所有token，并根据学习到的重要性分数自适应地将其路由到不同的专家，从而实现资源的有效利用。

**技术框架**：mixSGA的整体架构包括一个token-wise专家选择路由机制、权重共享的分组注意力投影模块，以及一个辅助损失函数以确保训练和推理的一致性。

**关键创新**：mixSGA的主要创新在于引入了动态路由机制和权重共享策略，能够在不丢弃token的情况下实现资源的动态分配，与现有方法相比，显著提高了模型的灵活性和效率。

**关键设计**：在设计上，mixSGA采用了基于学习的重要性分数的路由机制，确保了资源的比例分配；同时，通过分组注意力的权重共享，降低了参数开销。此外，辅助损失函数的引入确保了训练和推理过程中的一致性，提升了模型的稳定性。

## 📊 实验亮点

在多个模型（如Llama3、TinyLlama、OPT和Gemma2）的评估中，mixSGA相较于静态基线表现出显著优势。在指令跟随和持续预训练任务中，mixSGA实现了更高的ROUGE-L分数和更低的困惑度，显示出在相同KV预算下的优越性能。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等，能够有效提升模型在动态环境中的适应能力和资源利用效率。未来，mixSGA有望在更大规模的语言模型中推广应用，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Transformer models face scalability challenges in causal language modeling (CLM) due to inefficient memory allocation for growing key-value (KV) caches, which strains compute and storage resources. Existing methods like Grouped Query Attention (GQA) and token-level KV optimization improve efficiency but rely on rigid resource allocation, often discarding "low-priority" tokens or statically grouping them, failing to address the dynamic spectrum of token importance. We propose mixSGA, a novel mixture-of-expert (MoE) approach that dynamically optimizes token-wise computation and memory allocation. Unlike prior approaches, mixSGA retains all tokens while adaptively routing them to specialized experts with varying KV group sizes, balancing granularity and efficiency. Our key novelties include: (1) a token-wise expert-choice routing mechanism guided by learned importance scores, enabling proportional resource allocation without token discard; (2) weight-sharing across grouped attention projections to minimize parameter overhead; and (3) an auxiliary loss to ensure one-hot routing decisions for training-inference consistency in CLMs. Extensive evaluations across Llama3, TinyLlama, OPT, and Gemma2 model families show mixSGA's superiority over static baselines. On instruction-following and continued pretraining tasks, mixSGA achieves higher ROUGE-L and lower perplexity under the same KV budgets.

