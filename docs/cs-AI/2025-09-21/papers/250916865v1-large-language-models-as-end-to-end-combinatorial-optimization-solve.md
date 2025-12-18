---
layout: default
title: Large Language Models as End-to-end Combinatorial Optimization Solvers
---

# Large Language Models as End-to-end Combinatorial Optimization Solvers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16865" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16865v1</a>
  <a href="https://arxiv.org/pdf/2509.16865.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16865v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16865v1', 'Large Language Models as End-to-end Combinatorial Optimization Solvers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang

**分类**: cs.AI

**发布日期**: 2025-09-21

**期刊**: The 39th Annual Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**提出基于LLM的端到端组合优化求解器，无需代码生成或调用外部求解器。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `组合优化` `大型语言模型` `端到端求解器` `强化学习` `自然语言处理`

## 📋 核心要点

1. 传统组合优化方法依赖领域专家知识和特定算法，通用性与可访问性受限。
2. 提出一种端到端框架，利用LLM直接将自然语言问题描述映射到解决方案。
3. 通过两阶段训练，显著提升LLM在NP-hard问题上的可行性和最优性，优于现有方法。

## 📝 摘要（中文）

本文提出了一种新颖的框架，使大型语言模型（LLM）能够作为端到端的组合优化（CO）求解器，直接将自然语言问题描述映射到解决方案。传统上，组合优化问题（如物流和制造中的决策问题）使用需要大量领域知识的特定算法来解决。虽然LLM在自动化CO问题求解方面显示出潜力，但现有方法依赖于代码生成或求解器调用等中间步骤，限制了其通用性和可访问性。该方法采用两阶段训练策略：监督微调（SFT）使LLM掌握来自领域特定求解器的解决方案生成模式，而可行性和最优性感知强化学习（FOARL）过程显式地缓解了约束违反并优化了解决方案质量。在七个NP-hard CO问题上的评估表明，通过调整一个70亿参数的LLM，该方法实现了高可行率，并将平均最优性差距降低到1.03-8.20%，超过了通用LLM（如GPT-4o）、推理模型（如DeepSeek-R1）和领域特定的启发式方法。该方法建立了一个统一的、基于语言的CO流程，无需大量代码执行或针对不同问题进行手动架构调整，为传统求解器设计提供了一种通用的、语言驱动的替代方案，同时保持了相对可行性保证。

## 🔬 方法详解

**问题定义**：论文旨在解决组合优化（CO）问题，例如旅行商问题、车辆路径问题等。现有方法通常需要人工设计特定领域的算法，或者依赖于中间步骤，如生成代码或调用外部求解器，这限制了其通用性和易用性。此外，这些方法往往需要大量的领域知识和手动调整。

**核心思路**：论文的核心思路是直接利用大型语言模型（LLM）学习从自然语言问题描述到解决方案的映射。通过将CO问题转化为语言理解和生成任务，避免了对特定领域算法的依赖，并提高了模型的通用性和可访问性。这种方法的核心在于如何引导LLM生成既可行又高质量的解决方案。

**技术框架**：整体框架包含两个主要阶段：监督微调（SFT）和可行性和最优性感知强化学习（FOARL）。在SFT阶段，使用领域特定求解器生成的数据对LLM进行微调，使其学习到解决方案的生成模式。在FOARL阶段，通过强化学习进一步优化LLM，使其能够生成满足约束条件且具有较高质量的解决方案。该框架直接将自然语言问题描述输入LLM，输出解决方案，无需中间步骤。

**关键创新**：最重要的技术创新点在于将LLM作为端到端的CO求解器，避免了对传统求解器或代码生成的依赖。此外，FOARL过程显式地考虑了可行性和最优性，通过设计特定的奖励函数，引导LLM生成高质量的解决方案。与现有方法相比，该方法更加通用、易用，并且能够处理多种不同的CO问题。

**关键设计**：SFT阶段使用领域特定求解器生成的数据进行微调，损失函数为交叉熵损失。FOARL阶段的关键在于奖励函数的设计，该奖励函数综合考虑了可行性和最优性，例如，对于违反约束的解决方案给予负奖励，对于高质量的解决方案给予正奖励。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在七个NP-hard CO问题上取得了显著的性能提升。通过调整一个70亿参数的LLM，实现了高可行率，并将平均最优性差距降低到1.03-8.20%，优于GPT-4o、DeepSeek-R1等通用LLM和领域特定的启发式方法。这表明该方法具有很强的竞争力和潜力。

## 🎯 应用场景

该研究成果可广泛应用于物流、供应链管理、生产调度、资源分配等领域。通过自然语言描述问题，即可利用LLM快速生成解决方案，降低了对专业算法工程师的依赖，提高了决策效率。未来，该方法有望扩展到更复杂的优化问题，并与其他AI技术相结合，实现更智能化的决策支持。

## 📄 摘要（原文）

> Combinatorial optimization (CO) problems, central to decision-making scenarios like logistics and manufacturing, are traditionally solved using problem-specific algorithms requiring significant domain expertise. While large language models (LLMs) have shown promise in automating CO problem solving, existing approaches rely on intermediate steps such as code generation or solver invocation, limiting their generality and accessibility. This paper introduces a novel framework that empowers LLMs to serve as end-to-end CO solvers by directly mapping natural language problem descriptions to solutions. We propose a two-stage training strategy: supervised fine-tuning (SFT) imparts LLMs with solution generation patterns from domain-specific solvers, while a feasibility-and-optimality-aware reinforcement learning (FOARL) process explicitly mitigates constraint violations and refines solution quality. Evaluation across seven NP-hard CO problems shows that our method achieves a high feasibility rate and reduces the average optimality gap to 1.03-8.20% by tuning a 7B-parameter LLM, surpassing both general-purpose LLMs (e.g., GPT-4o), reasoning models (e.g., DeepSeek-R1), and domain-specific heuristics. Our method establishes a unified language-based pipeline for CO without extensive code execution or manual architectural adjustments for different problems, offering a general and language-driven alternative to traditional solver design while maintaining relative feasibility guarantees.

