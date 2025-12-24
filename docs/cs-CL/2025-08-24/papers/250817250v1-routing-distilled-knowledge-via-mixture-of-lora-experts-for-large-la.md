---
layout: default
title: Routing Distilled Knowledge via Mixture of LoRA Experts for Large Language Model based Bundle Generation
---

# Routing Distilled Knowledge via Mixture of LoRA Experts for Large Language Model based Bundle Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17250" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17250v1</a>
  <a href="https://arxiv.org/pdf/2508.17250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17250v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17250v1', 'Routing Distilled Knowledge via Mixture of LoRA Experts for Large Language Model based Bundle Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaidong Feng, Zhu Sun, Hui Fang, Jie Yang, Wenyuan Liu, Yew-Soon Ong

**分类**: cs.CL, cs.IR

**发布日期**: 2025-08-24

---

## 💡 一句话要点

**提出RouteDK框架以解决大语言模型知识蒸馏冲突问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `知识蒸馏` `LoRA专家` `自动化生成` `计算效率` `动态融合` `知识冲突`

## 📋 核心要点

1. 现有方法在知识蒸馏过程中容易导致知识冲突，影响捆绑生成的性能和效率。
2. 本文提出RouteDK框架，通过混合LoRA专家架构动态路由蒸馏知识，有效整合高层次和细粒度知识。
3. 实验结果显示，RouteDK在多个数据集上实现了与教师LLM相当或更好的准确性，同时显著提高了计算效率。

## 📝 摘要（中文）

大语言模型（LLMs）在自动化捆绑生成中展现出潜力，但面临高昂的计算成本。尽管知识蒸馏为更高效的学生模型提供了途径，但初步研究表明，简单地将来自教师LLMs的多样化蒸馏知识整合到学生LLMs中会导致知识冲突，影响捆绑生成的性能。为此，本文提出了RouteDK框架，通过混合LoRA专家架构来路由蒸馏知识。具体而言，我们首先从教师LLM中蒸馏出两种互补类型的知识：高层次知识（可推广规则）和细粒度知识（会话特定推理）。然后，我们为每种知识类型训练知识特定的LoRA专家，并与基础LoRA专家一起使用。为了有效整合，我们提出了一个动态融合模块，具有输入感知路由器，能够根据输入动态确定最优权重，从而有效缓解知识冲突。实验结果表明，RouteDK在三个公共数据集上的准确性与教师LLM相当或更优，同时保持强大的计算效率。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在知识蒸馏过程中出现的知识冲突问题。现有方法在将多种类型的蒸馏知识整合到学生模型时，往往导致性能下降，尤其是在捆绑生成任务中。

**核心思路**：论文提出的RouteDK框架通过混合LoRA专家架构，有效路由和整合来自教师模型的高层次和细粒度知识。通过动态调整专家的贡献，减少知识冲突，从而提升生成性能。

**技术框架**：RouteDK框架主要包括知识蒸馏模块、LoRA专家模块和动态融合模块。首先从教师模型中提取知识，然后为不同类型的知识训练专门的LoRA专家，最后通过动态融合模块整合这些专家的输出。

**关键创新**：RouteDK的核心创新在于引入了输入感知路由器，该路由器能够根据输入动态调整各个LoRA专家的权重，从而有效缓解知识冲突。这一设计与传统的静态权重分配方法有本质区别。

**关键设计**：在设计中，采用了知识特定的LoRA专家，并结合基础LoRA专家进行训练。动态融合模块通过输入特征来决定各专家的贡献权重，确保在推理时的可靠性和一致性。

## 📊 实验亮点

实验结果表明，RouteDK在三个公共数据集上的准确性与教师LLM相当或更优，且在计算效率上表现出显著优势。具体而言，RouteDK在捆绑生成任务中实现了比现有最先进方法更高的性能，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化内容生成和个性化推荐系统等。通过提高大语言模型的计算效率和生成性能，RouteDK能够在实际应用中显著降低资源消耗，并提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown potential in automatic bundle generation but suffer from prohibitive computational costs. Although knowledge distillation offers a pathway to more efficient student models, our preliminary study reveals that naively integrating diverse types of distilled knowledge from teacher LLMs into student LLMs leads to knowledge conflict, negatively impacting the performance of bundle generation. To address this, we propose RouteDK, a framework for routing distilled knowledge through a mixture of LoRA expert architecture. Specifically, we first distill knowledge from the teacher LLM for bundle generation in two complementary types: high-level knowledge (generalizable rules) and fine-grained knowledge (session-specific reasoning). We then train knowledge-specific LoRA experts for each type of knowledge together with a base LoRA expert. For effective integration, we propose a dynamic fusion module, featuring an input-aware router, where the router balances expert contributions by dynamically determining optimal weights based on input, thereby effectively mitigating knowledge conflicts. To further improve inference reliability, we design an inference-time enhancement module to reduce variance and mitigate suboptimal reasoning. Experiments on three public datasets show that our RouteDK achieves accuracy comparable to or even better than the teacher LLM, while maintaining strong computational efficiency. In addition, it outperforms state-of-the-art approaches for bundle generation.

