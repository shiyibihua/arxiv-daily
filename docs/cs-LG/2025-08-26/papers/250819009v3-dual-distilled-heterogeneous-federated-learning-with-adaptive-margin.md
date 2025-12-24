---
layout: default
title: Dual-Distilled Heterogeneous Federated Learning with Adaptive Margins for Trainable Global Prototypes
---

# Dual-Distilled Heterogeneous Federated Learning with Adaptive Margins for Trainable Global Prototypes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19009" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19009v3</a>
  <a href="https://arxiv.org/pdf/2508.19009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19009v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19009v3', 'Dual-Distilled Heterogeneous Federated Learning with Adaptive Margins for Trainable Global Prototypes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fatema Siddika, Md Anwar Hossen, Wensheng Zhang, Anuj Sharma, Juan Pablo Muñoz, Ali Jannesari

**分类**: cs.LG, cs.DC

**发布日期**: 2025-08-26 (更新: 2025-12-19)

**备注**: 11 pages, 8 figures

---

## 💡 一句话要点

**提出双蒸馏异构联邦学习以解决原型边界收缩问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `异构联邦学习` `知识蒸馏` `原型聚合` `对比学习` `模型异构性` `非IID数据` `深度学习`

## 📋 核心要点

1. 现有的基于原型的HFL方法在聚合原型时使用标准加权平均，导致全局知识的收缩和模型性能下降。
2. 本文提出FedProtoKD框架，通过双知识蒸馏机制和自适应原型边界，解决了原型边界收缩的问题。
3. 实验结果表明，FedProtoKD在多种设置下平均提高了1.13%的测试准确率，最高可达34.13%，显著优于现有方法。

## 📝 摘要（中文）

异构联邦学习（HFL）因其处理客户端模型和数据异构性的能力而受到广泛关注。基于原型的HFL方法作为一种有前景的解决方案，旨在应对统计和模型异构性以及隐私挑战。然而，传统的加权平均聚合方法往往导致全局知识的亚优化，特别是在模型异构和非独立同分布（non-IID）数据分布的情况下。本文提出的FedProtoKD框架利用增强的双知识蒸馏机制，通过对客户端的logits和原型特征表示进行优化，解决了原型边界收缩问题。实验结果显示，FedProtoKD在多种设置下平均提高了1.13%的测试准确率，最高可达34.13%，显著超越现有的HFL方法。

## 🔬 方法详解

**问题定义**：本文解决的是在异构联邦学习中，传统加权平均聚合导致的原型边界收缩问题，这种收缩会影响模型在非独立同分布数据上的性能。

**核心思路**：提出的FedProtoKD框架通过双知识蒸馏机制，结合客户端的logits和原型特征表示，增强了系统性能，并引入自适应原型边界以解决边界收缩问题。

**技术框架**：该框架包括两个主要模块：1）客户端模块，负责生成原型和logits；2）服务器模块，利用对比学习方法训练可调的全局原型，并根据样本与类代表原型的接近度评估公共样本的重要性。

**关键创新**：最重要的创新在于引入了对比学习基础的可调服务器原型和类-wise自适应原型边界，显著改善了原型聚合的效果，克服了传统方法的局限性。

**关键设计**：在损失函数设计上，结合了知识蒸馏损失和对比学习损失，确保了原型的有效聚合和边界的适应性调整。网络结构上，采用了深度神经网络以提取更丰富的特征表示。

## 📊 实验亮点

FedProtoKD在多种实验设置下平均提高了1.13%的测试准确率，最高可达34.13%。与现有的最先进HFL方法相比，FedProtoKD在处理模型异构性和非IID数据分布时表现出显著的性能提升，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗数据分析、金融欺诈检测和智能交通系统等，尤其是在数据隐私和安全性要求较高的场景中。通过提升异构联邦学习的性能，FedProtoKD能够为多方协作提供更有效的解决方案，促进各行业的智能化发展。

## 📄 摘要（原文）

> Heterogeneous Federated Learning (HFL) has gained significant attention for its capacity to handle both model and data heterogeneity across clients. Prototype-based HFL methods emerge as a promising solution to address statistical and model heterogeneity as well as privacy challenges, paving the way for new advancements in HFL research. This method focuses on sharing class-representative prototypes among heterogeneous clients. However, aggregating these prototypes via standard weighted averaging often yields sub-optimal global knowledge. Specifically, the averaging approach induces a shrinking of the aggregated prototypes' decision margins, thereby degrading model performance in scenarios with model heterogeneity and non-IID data distributions. The propose FedProtoKD in a Heterogeneous Federated Learning setting, utilizing an enhanced dual-knowledge distillation mechanism to enhance system performance by leveraging clients' logits and prototype feature representations. The proposed framework aims to resolve the prototype margin-shrinking problem using a contrastive learning-based trainable server prototype by leveraging a class-wise adaptive prototype margin. Furthermore, the framework assess the importance of public samples using the closeness of the sample's prototype to its class representative prototypes, which enhances learning performance. FedProtoKD improved test accuracy by an average of 1.13% and up to 34.13% across various settings, significantly outperforming existing state-of-the-art HFL methods.

