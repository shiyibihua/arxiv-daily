---
layout: default
title: Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices
---

# Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19078" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19078v2</a>
  <a href="https://arxiv.org/pdf/2508.19078.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19078v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19078v2', 'Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fahao Chen, Jie Wan, Peng Li, Zhou Su, Dongxiao Yu

**分类**: cs.DC, cs.AI

**发布日期**: 2025-08-26 (更新: 2025-10-10)

**备注**: Accepted by EuroSys 2026

---

## 💡 一句话要点

**提出FLUX以解决资源受限设备上MoE模型的联邦微调问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `大规模语言模型` `Mixture-of-Experts` `模型微调` `资源优化` `动态分配` `量化分析`

## 📋 核心要点

1. 现有方法在联邦微调MoE模型时面临计算资源不足的问题，导致性能无法满足需求。
2. FLUX通过量化本地分析、适应性专家合并和动态角色分配等创新方法，优化了资源使用效率。
3. 实验结果显示，FLUX在多个基准数据集上显著提升了时间到达准确率，速度提升可达4.75倍。

## 📝 摘要（中文）

联邦微调基于Mixture-of-Experts (MoE)的大型语言模型（LLMs）面临巨大的计算需求和参与者的资源限制。现有方法通过模型量化、计算卸载或专家剪枝来填补这一空白，但由于不切实际的系统假设和对MoE特性缺乏考虑，无法达到预期性能。本文提出FLUX，一个旨在实现资源受限设备上MoE模型的联邦微调的系统，旨在最小化时间到达准确率。FLUX引入了三项关键创新：量化基础的本地分析、适应性层感知的专家合并和动态专家角色分配。大量实验表明，FLUX在时间到达准确率上显著优于现有方法，速度提升可达4.75倍。

## 🔬 方法详解

**问题定义**：本文旨在解决在资源受限设备上进行MoE模型的联邦微调时的计算需求过高和性能不足的问题。现有方法未能充分考虑MoE模型的特性，导致效果不佳。

**核心思路**：FLUX的核心思路是通过量化和动态调整专家角色来优化资源使用，同时保持模型的准确性。这样的设计旨在在有限的计算资源下实现高效的模型微调。

**技术框架**：FLUX的整体架构包括三个主要模块：量化基础的本地分析模块、适应性层感知的专家合并模块和动态专家角色分配模块。这些模块协同工作，以实现高效的联邦微调。

**关键创新**：FLUX的关键创新在于其量化本地分析和动态角色分配策略，这与传统方法的静态专家选择和简单量化方法有本质区别，能够更好地适应MoE模型的特性。

**关键设计**：在FLUX中，量化分析用于估计专家激活，减少计算开销；适应性专家合并通过分析层级特征来优化资源消耗；动态角色分配则采用探索-利用策略，以平衡调优和非调优专家的角色。具体的参数设置和损失函数设计在实验中经过调优，以确保最佳性能。

## 📊 实验亮点

实验结果表明，FLUX在LLaMA-MoE和DeepSeek-MoE模型上表现优异，相较于现有方法，时间到达准确率提升可达4.75倍，显著提高了联邦微调的效率和效果。

## 🎯 应用场景

FLUX的研究成果在多个领域具有广泛的应用潜力，尤其是在需要高效处理大规模语言模型的场景中，如智能助手、在线教育和个性化推荐系统等。通过在资源受限设备上实现高效的模型微调，FLUX能够推动这些应用的普及和发展，提升用户体验。

## 📄 摘要（原文）

> Federated fine-tuning of Mixture-of-Experts (MoE)-based large language models (LLMs) is challenging due to their massive computational requirements and the resource constraints of participants. Existing working attempts to fill this gap through model quantization, computation offloading, or expert pruning. However, they cannot achieve desired performance due to impractical system assumptions and a lack of consideration for MoE-specific characteristics. In this paper, we propose FLUX, a system designed to enable federated fine-tuning of MoE-based LLMs across participants with constrained computing resources (e.g., consumer-grade GPUs), aiming to minimize time-to-accuracy. FLUX introduces three key innovations: (1) quantization-based local profiling to estimate expert activation with minimal overhead, (2) adaptive layer-aware expert merging to reduce resource consumption while preserving accuracy, and (3) dynamic expert role assignment using an exploration-exploitation strategy to balance tuning and non-tuning experts. Extensive experiments on LLaMA-MoE and DeepSeek-MoE with multiple benchmark datasets demonstrate that FLUX significantly outperforms existing methods, achieving up to 4.75X speedup in time-to-accuracy.

