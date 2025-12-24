---
layout: default
title: A Data-driven ML Approach for Maximizing Performance in LLM-Adapter Serving
---

# A Data-driven ML Approach for Maximizing Performance in LLM-Adapter Serving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08343" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08343v3</a>
  <a href="https://arxiv.org/pdf/2508.08343.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08343v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08343v3', 'A Data-driven ML Approach for Maximizing Performance in LLM-Adapter Serving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ferran Agullo, Joan Oliveras, Chen Wang, Alberto Gutierrez-Torre, Olivier Tardieu, Alaa Youssef, Jordi Torres, Josep Ll. Berral

**分类**: cs.PF, cs.AI, cs.CL

**发布日期**: 2025-08-11 (更新: 2025-11-19)

**备注**: Accepted in a computer science workshop

**🔗 代码/项目**: [GITHUB](https://github.com/FerranAgulloLopez/GPULLMAdapterOptimization)

---

## 💡 一句话要点

**提出数据驱动的机器学习方法以优化LLM适配器服务性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `适配器优化` `机器学习` `数字双胞胎` `GPU性能` `请求聚合`

## 📋 核心要点

1. 现有方法在服务多个LLM适配器时容易导致GPU内存超限，从而引发请求饥饿，影响系统性能。
2. 本研究提出了一种数据驱动的机器学习方法，通过可解释模型优化并发和并行适配器的配置，以提高GPU吞吐量。
3. 实验结果显示，数字双胞胎模型的吞吐量与真实结果的误差仅为5.1%，而机器学习方法的预测误差不超过7.2%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的快速普及，LLM适配器逐渐成为一种常见的轻量级模型专门化工具。在单个GPU上同时服务数百或数千个适配器可以实现请求聚合，提高吞吐量，但如果超出GPU内存限制，可能导致请求饥饿。为了解决这一问题，本研究专注于确定并发和并行适配器的联合配置，以最大化GPU吞吐量而不引发饥饿。我们提出了一种数据驱动的机器学习方法，利用可解释模型来解决这一缓存问题，并引入了首个能够重现LLM适配器服务系统的数字双胞胎，从而实现高效的训练数据生成。实验结果表明，数字双胞胎的吞吐量与真实结果的误差在5.1%以内，而机器学习方法在异构真实工作负载下预测的并发和并行适配器的最优数量误差最多为7.2%。

## 🔬 方法详解

**问题定义**：本论文旨在解决在单个GPU上同时服务多个LLM适配器时，由于内存限制导致的请求饥饿问题。现有方法在处理异构适配器和流量特性时，往往无法有效配置适配器，导致性能下降。

**核心思路**：论文提出了一种数据驱动的机器学习方法，利用可解释模型来优化适配器的并发和并行配置，从而最大化GPU的吞吐量，避免请求饥饿。通过引入数字双胞胎技术，能够高效生成训练数据，提升模型的准确性。

**技术框架**：整体架构包括数据收集、模型训练和性能评估三个主要模块。首先，通过数字双胞胎模拟LLM适配器服务系统，生成训练数据；然后，利用机器学习模型进行适配器配置的优化；最后，通过实验验证模型的预测性能。

**关键创新**：本研究的关键创新在于提出了数字双胞胎技术，能够准确重现LLM适配器服务系统，并结合可解释机器学习模型进行优化。这一方法在处理异构工作负载时表现出显著优势。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡吞吐量和请求饥饿的风险，同时对适配器的并发和并行数量进行了系统的参数调优，以确保模型的预测精度和实用性。

## 📊 实验亮点

实验结果表明，数字双胞胎模型的吞吐量与真实结果的误差仅为5.1%，而机器学习方法在异构真实工作负载下预测的并发和并行适配器的最优数量误差不超过7.2%。这些结果显示了该方法在实际应用中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括云计算服务、智能助手和自然语言处理等场景，能够有效提升大型语言模型在实际应用中的服务性能。通过优化适配器配置，可以在资源有限的情况下实现更高的吞吐量，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With the rapid adoption of Large Language Models (LLMs), LLM-adapters have become increasingly common, providing lightweight specialization of large-scale models. Serving hundreds or thousands of these adapters on a single GPU allows request aggregation, increasing throughput, but may also cause request starvation if GPU memory limits are exceeded. To address this issue, this study focuses on determining the joint configuration of concurrent and parallel adapters that maximizes GPU throughput without inducing starvation, given heterogeneous adapter and traffic properties. We propose a data-driven ML approach leveraging interpretable models to tackle this caching problem and introduce the first Digital Twin capable of reproducing an LLM-adapter serving system, enabling efficient training data generation. Experiments with the vLLM framework and LoRA adapters show that the Digital Twin reproduces throughput within 5.1% of real results, while the ML approach predicts optimal numbers of concurrent and parallel adapters with an error of at most 7.2% under heterogeneous, real-world workloads. The code is publicly available at https://github.com/FerranAgulloLopez/GPULLMAdapterOptimization.

