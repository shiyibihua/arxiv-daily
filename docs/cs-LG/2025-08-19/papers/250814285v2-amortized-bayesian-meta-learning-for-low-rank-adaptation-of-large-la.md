---
layout: default
title: Amortized Bayesian Meta-Learning for Low-Rank Adaptation of Large Language Models
---

# Amortized Bayesian Meta-Learning for Low-Rank Adaptation of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14285" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14285v2</a>
  <a href="https://arxiv.org/pdf/2508.14285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14285v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14285v2', 'Amortized Bayesian Meta-Learning for Low-Rank Adaptation of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liyi Zhang, Jake Snell, Thomas L. Griffiths

**分类**: cs.LG, cs.AI, stat.ML

**发布日期**: 2025-08-19 (更新: 2025-12-09)

**备注**: 16 pages, 2 figures

---

## 💡 一句话要点

**提出ABMLL以解决大语言模型低秩适应的泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩适应` `贝叶斯元学习` `大语言模型` `泛化能力` `模型微调` `不确定性量化` `自然语言处理`

## 📋 核心要点

1. 现有方法在提高大语言模型的泛化能力时，往往需要大量内存和计算资源，限制了其应用。
2. 本文提出的ABMLL方法通过摊销贝叶斯元学习，优化了低秩适应过程，提升了计算效率。
3. 实验结果表明，ABMLL在CrossFit和Unified-QA数据集上表现优异，超越了现有技术，具有更好的准确性和校准能力。

## 📝 摘要（中文）

对大型语言模型（LLMs）进行低秩适应（LoRA）微调是一种有效的方式，可以将特定数据集的信息融入模型中。然而，微调后的LLM在未见数据集上的泛化能力常常不明确。现有方法通过优化上下文提示或使用元学习来提高泛化能力，但这些方法在内存和计算上成本高昂。为了解决这些挑战，本文提出了基于摊销贝叶斯元学习的LoRA方法（ABMLL），该方法在保持计算效率的同时，将摊销贝叶斯元学习的思想应用于LLMs。ABMLL在CrossFit和Unified-QA数据集上进行了测试，结果显示其在准确性和期望校准误差方面均优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在特定数据集微调后的泛化能力不足的问题。现有方法如优化上下文提示和元学习虽然有效，但在内存和计算上代价高昂。

**核心思路**：ABMLL通过摊销贝叶斯元学习的框架，适应于大型语言模型，保持计算效率的同时，提升模型的泛化能力。该方法重新定义了任务特定参数和全局参数的关系，并引入新的超参数来平衡重构精度与任务特定参数的保真度。

**技术框架**：ABMLL的整体架构包括任务特定参数和全局参数的重构过程，利用贝叶斯框架进行不确定性量化。该方法通过优化超参数来实现高效的微调。

**关键创新**：ABMLL的核心创新在于将摊销贝叶斯元学习方法成功应用于大型语言模型，显著提高了模型的泛化能力和不确定性量化能力，与传统方法相比，计算开销大幅降低。

**关键设计**：在ABMLL中，设计了新的超参数以平衡重构精度与任务特定参数的保真度，确保模型在微调过程中的稳定性和有效性。

## 📊 实验亮点

在CrossFit和Unified-QA数据集上的实验结果显示，ABMLL在准确性和期望校准误差方面均优于现有方法，具体提升幅度达到X%（具体数据未知），证明了其有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等。通过提高大型语言模型的泛化能力，ABMLL能够在多种任务中实现更好的性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Fine-tuning large language models (LLMs) with low-rank adaptation (LoRA) is a cost-effective way to incorporate information from a specific dataset. However, it is often unclear how well the fine-tuned LLM will generalize, i.e., how well it will perform on unseen datasets. Methods have been proposed to improve generalization by optimizing in-context prompts, or by using meta-learning to fine-tune LLMs. However, these methods are expensive in memory and computation, requiring either long-context prompts or saving copies of parameters and using second-order gradient updates. To address these challenges, we propose Amortized Bayesian Meta-Learning for LoRA (ABMLL). This method builds on amortized Bayesian meta-learning for smaller models, adapting this approach to LLMs while maintaining its computational efficiency. We reframe task-specific and global parameters in the context of LoRA and use a new hyperparameter to balance reconstruction accuracy and the fidelity of task-specific parameters to the global ones. ABMLL provides effective generalization and scales to large models such as LLAMA3-8B. Furthermore, as a result of using a Bayesian framework, ABMLL provides improved uncertainty quantification. We test ABMLL on CrossFit and Unified-QA datasets and find that it outperforms existing methods on these benchmarks in terms of both accuracy and expected calibration error.

