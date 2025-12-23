---
layout: default
title: Mitigating Catastrophic Forgetting with Adaptive Transformer Block Expansion in Federated Fine-Tuning
---

# Mitigating Catastrophic Forgetting with Adaptive Transformer Block Expansion in Federated Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05977" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05977v1</a>
  <a href="https://arxiv.org/pdf/2506.05977.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05977v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05977v1', 'Mitigating Catastrophic Forgetting with Adaptive Transformer Block Expansion in Federated Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujia Huo, Jianchun Liu, Hongli Xu, Zhenguo Ma, Shilong Wang, Liusheng Huang

**分类**: cs.LG, cs.DC

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出FedBE以解决联邦微调中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `灾难性遗忘` `自适应变换器` `模型微调` `数据隐私` `异构环境` `深度学习`

## 📋 核心要点

1. 现有的联邦微调方法未能有效解决灾难性遗忘问题，尤其是在异构数据分布和设备能力差异的情况下。
2. 本文提出FedBE框架，通过自适应变换器块扩展机制和动态块分配策略，解决了联邦环境中的灾难性遗忘问题。
3. 实验结果显示，FedBE在微调后的准确率保持上比现有方法提高了12-74%，并且模型收敛速度加快了1.9-3.1倍。

## 📝 摘要（中文）

联邦微调（FedFT）大语言模型（LLMs）已成为适应分布式数据环境的有前景的解决方案，同时确保数据隐私。然而，现有的FedFT方法主要采用参数高效微调（PEFT）技术，未能有效应对灾难性遗忘这一关键挑战。为此，本文提出了FedBE框架，结合自适应变换器块扩展机制和动态可训练块分配策略，旨在更好地适应异构的联邦环境并提高模型的泛化能力。实验结果表明，FedBE在微调后相较于现有方法，准确率保持提升12-74%，模型收敛加速比为1.9-3.1倍，且未降低下游任务的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决联邦微调中的灾难性遗忘问题，现有方法在异构环境中无法有效应对数据分布和设备能力的差异，导致模型泛化能力下降。

**核心思路**：FedBE框架通过扩展可训练的变换器块，将新学习的任务特定知识与原有的预训练表示结构性分离，从而减少遗忘现象。

**技术框架**：FedBE的整体架构包括自适应变换器块扩展和动态块分配两个主要模块。自适应扩展模块负责根据客户端的数据分布和计算能力动态调整可训练块的数量和位置。

**关键创新**：FedBE的核心创新在于其自适应变换器块扩展机制和动态分配策略，这与传统的集中式微调方法有本质区别，后者无法应对联邦环境的异构性和隐私约束。

**关键设计**：在设计上，FedBE采用了动态分配策略，根据每个客户端的具体数据特征和计算能力，灵活分配可训练块，确保模型在不同设备上的高效训练。

## 📊 实验亮点

实验结果表明，FedBE在微调后相较于现有的联邦微调方法，准确率保持提升12-74%，并且模型收敛速度加快了1.9-3.1倍，显示出显著的性能优势。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和智能设备等需要保护数据隐私的分布式学习场景。FedBE能够在保证数据隐私的前提下，提高模型在异构环境中的适应性和泛化能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Federated fine-tuning (FedFT) of large language models (LLMs) has emerged as a promising solution for adapting models to distributed data environments while ensuring data privacy.
>   Existing FedFT methods predominantly utilize parameter-efficient fine-tuning (PEFT) techniques to reduce communication and computation overhead.
>   However, they often fail to adequately address the catastrophic forgetting, a critical challenge arising from continual adaptation in distributed environments. The traditional centralized fine-tuning methods, which are not designed for the heterogeneous and privacy-constrained nature of federated environments, struggle to mitigate this issue effectively. Moreover, the challenge is further exacerbated by significant variation in data distributions and device capabilities across clients, which leads to intensified forgetting and degraded model generalization. To tackle these issues, we propose FedBE, a novel FedFT framework that integrates an adaptive transformer block expansion mechanism with a dynamic trainable-block allocation strategy. Specifically, FedBE expands trainable blocks within the model architecture, structurally separating newly learned task-specific knowledge from the original pre-trained representations. Additionally, FedBE dynamically assigns these trainable blocks to clients based on their data distributions and computational capabilities. This enables the framework to better accommodate heterogeneous federated environments and enhances the generalization ability of the model.Extensive experiments show that compared with existing federated fine-tuning methods, FedBE achieves 12-74% higher accuracy retention on general tasks after fine-tuning and a model convergence acceleration ratio of 1.9-3.1x without degrading the accuracy of downstream tasks.

