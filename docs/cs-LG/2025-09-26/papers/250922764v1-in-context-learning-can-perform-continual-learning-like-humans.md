---
layout: default
title: In-Context Learning can Perform Continual Learning Like Humans
---

# In-Context Learning can Perform Continual Learning Like Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22764" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22764v1</a>
  <a href="https://arxiv.org/pdf/2509.22764.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22764v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22764v1', 'In-Context Learning can Perform Continual Learning Like Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liuwang Kang, Fan Wang, Shaoshan Liu, Hung-Chyun Chou, Chuan Lin, Ning Ding

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出上下文持续学习(ICCL)，实现类人长期记忆和跨任务知识积累。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文学习` `持续学习` `大型语言模型` `灾难性遗忘` `人类记忆` `分布式实践` `提示工程`

## 📋 核心要点

1. 现有持续学习方法面临灾难性遗忘问题，且缺乏对人类认知机制的有效模拟。
2. 提出上下文持续学习(ICCL)框架，通过任务调度和提示重排实现持续学习能力。
3. 实验表明ICCL受益于分布式实践，且线性注意力模型表现出更接近人类的记忆模式。

## 📝 摘要（中文）

大型语言模型(LLMs)可以通过上下文学习(ICL)适应新任务，而无需参数更新，使其成为快速适应的强大学习引擎。虽然大量研究已经将ICL作为一种少样本学习器进行了考察，但当多任务按顺序到达时，它是否能够实现长期记忆和跨任务知识积累仍未得到充分探索。受人类记忆研究的启发，我们研究了ICL在多任务环境中的记忆特性，并将其扩展到上下文持续学习(ICCL)，其中持续学习能力通过任务调度和提示重排而产生。在马尔可夫链基准上的实验表明，对于特定的大型语言模型，ICCL以类似于人类的方式受益于分布式实践(DP)，始终揭示了用于记忆的间隔“最佳点”。除了记忆性能之外，我们还提出了一种人类记忆相似性度量，以量化持续学习(CL)方法与人类记忆动态的匹配程度。使用这种度量，我们表明，像MAMBA和RWKV这样的线性注意力模型表现出特别像人类的记忆模式，尽管它们的记忆性能落后于基于Transformer的LLM。总的来说，我们的结果将ICCL确立为一种认知上合理且实践上有效的推理式CL范例，它可以减轻灾难性遗忘，并解决传统CL方法中的稳定性-可塑性困境。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在持续学习场景下的灾难性遗忘问题，即模型在学习新任务时，会遗忘之前学习过的任务。现有的持续学习方法通常需要参数更新，计算成本高昂，并且缺乏对人类认知机制的有效模拟，导致泛化能力受限。

**核心思路**：论文的核心思路是利用大型语言模型的上下文学习能力，通过精心设计的任务调度和提示重排，使模型能够在不更新参数的情况下，持续学习新任务并保持对旧任务的记忆。这种方法模拟了人类的学习方式，即通过间隔重复和分布式实践来提高记忆效果。

**技术框架**：ICCL框架主要包含以下几个阶段：1) 任务序列生成：按照一定的策略（如随机、分布式）生成任务序列。2) 上下文构建：为每个任务构建包含少量样本的上下文提示。3) 推理：使用大型语言模型对每个任务进行推理。4) 提示重排：根据任务的记忆效果，动态调整提示的顺序和内容，以优化整体的记忆性能。

**关键创新**：论文最重要的技术创新点在于提出了上下文持续学习(ICCL)的概念，并将其与人类记忆机制相结合。ICCL是一种完全基于推理的持续学习方法，无需参数更新，从而避免了灾难性遗忘问题。此外，论文还提出了一种人类记忆相似性度量，用于评估不同持续学习方法与人类记忆动态的匹配程度。

**关键设计**：在任务调度方面，论文研究了分布式实践(DP)对ICCL的影响，发现存在一个间隔“最佳点”，可以最大化记忆效果。在提示重排方面，论文探索了不同的重排策略，如基于记忆效果的重排和基于任务相似性的重排。此外，论文还使用了马尔可夫链作为基准测试，并设计了相应的评估指标。

## 📊 实验亮点

实验结果表明，ICCL在马尔可夫链基准测试上取得了良好的记忆性能，并且受益于分布式实践。线性注意力模型（如MAMBA和RWKV）虽然记忆性能不如Transformer，但表现出更接近人类的记忆模式。论文提出的记忆相似性度量为评估持续学习方法与人类认知机制的匹配程度提供了一种新的方法。

## 🎯 应用场景

ICCL方法可应用于需要持续学习和快速适应的场景，如智能客服、对话系统、机器人导航等。该方法无需参数更新，降低了计算成本，并具有较好的泛化能力。未来可进一步研究ICCL在更复杂任务和更大规模模型上的应用，并探索更有效的任务调度和提示重排策略。

## 📄 摘要（原文）

> Large language models (LLMs) can adapt to new tasks via in-context learning (ICL) without parameter updates, making them powerful learning engines for fast adaptation. While extensive research has examined ICL as a few-shot learner, whether it can achieve long-term retention and cross-task knowledge accumulation when multitasks arrive sequentially remains underexplored. Motivated by human memory studies, we investigate the retention characteristics of ICL in multitask settings and extend it to in-context continual learning (ICCL), where continual learning ability emerges through task scheduling and prompt rearrangement. Experiments on Markov-Chain benchmarks demonstrate that, for specific large-language models, ICCL benefits from distributed practice (DP) in a manner analogous to humans, consistently revealing a spacing "sweet spot" for retention. Beyond retention performance, we propose a human-retention similarity metric to quantify how closely a continual-learning (CL) method aligns with human retention dynamics. Using this metric, we show that linear-attention models such as MAMBA and RWKV exhibit particularly human-like retention patterns, despite their retention performance lagging behind that of Transformer-based LLMs. Overall, our results establish ICCL as both cognitively plausible and practically effective, providing an inference-only CL paradigm that mitigates catastrophic forgetting and addresses the stability-plasticity dilemma in conventional CL methods.

