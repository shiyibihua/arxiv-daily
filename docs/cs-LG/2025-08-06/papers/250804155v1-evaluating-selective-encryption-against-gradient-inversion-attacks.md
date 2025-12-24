---
layout: default
title: Evaluating Selective Encryption Against Gradient Inversion Attacks
---

# Evaluating Selective Encryption Against Gradient Inversion Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04155" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04155v1</a>
  <a href="https://arxiv.org/pdf/2508.04155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04155v1', 'Evaluating Selective Encryption Against Gradient Inversion Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajun Gu, Yuhang Yao, Shuaiqi Wang, Carlee Joe-Wong

**分类**: cs.CR, cs.LG

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出选择性加密以应对梯度反演攻击问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `梯度反演攻击` `选择性加密` `隐私保护` `联邦学习` `模型架构` `攻击评估`

## 📋 核心要点

1. 梯度反演攻击对联邦学习等分布式训练框架的隐私构成威胁，现有加密方法计算开销高。
2. 提出选择性加密方法，仅对重要梯度数据进行加密，旨在降低计算负担并保持隐私保护。
3. 通过对不同模型架构和攻击类型的实验，发现梯度幅度是有效的保护指标，但没有单一策略适用于所有场景。

## 📝 摘要（中文）

梯度反演攻击对分布式训练框架（如联邦学习）构成了重大隐私威胁，使恶意方能够从客户端与聚合服务器之间的梯度通信中重建敏感的本地训练数据。尽管传统的基于加密的防御方法（如同态加密）在不损害模型效用的情况下提供了强大的隐私保障，但通常会带来高昂的计算开销。为此，选择性加密作为一种有前景的方法应运而生，仅对基于特定指标的重要性选择梯度数据进行加密。本文系统评估了不同重要性指标下的选择性加密方法对先进攻击的有效性，提出了一种基于距离的重要性分析框架，为选择关键梯度元素进行加密提供理论基础。实验结果表明，选择性加密在降低计算开销的同时，仍能保持对攻击的抵抗力。

## 🔬 方法详解

**问题定义**：本文解决梯度反演攻击对联邦学习隐私的威胁，现有方法如同态加密计算开销高，难以广泛应用。

**核心思路**：提出选择性加密方法，依据梯度数据的重要性选择性加密，旨在在降低计算负担的同时保持隐私保护。

**技术框架**：整体架构包括重要性分析、选择性加密和攻击评估三个主要模块。首先通过距离分析确定重要梯度元素，然后对这些元素进行加密，最后评估其对不同攻击的防护效果。

**关键创新**：提出基于距离的重要性分析框架，为选择性加密提供理论基础，识别出梯度幅度作为有效的保护指标，区别于传统的全量加密方法。

**关键设计**：在实验中使用了多种模型架构（如LeNet、CNN、BERT、GPT-2），并对不同攻击类型进行了评估，发现没有单一的选择性加密策略适用于所有场景，提供了针对不同需求的策略选择指南。

## 📊 实验亮点

实验结果表明，选择性加密方法在降低计算开销的同时，能够有效抵御优化基础的梯度反演攻击。具体而言，使用梯度幅度作为保护指标时，能够显著提升模型的隐私保护能力，且在不同模型架构下均表现出良好的适应性。

## 🎯 应用场景

该研究的潜在应用领域包括联邦学习、隐私保护计算和安全多方计算等。通过有效的选择性加密方法，可以在保证模型效用的同时，保护用户数据隐私，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Gradient inversion attacks pose significant privacy threats to distributed training frameworks such as federated learning, enabling malicious parties to reconstruct sensitive local training data from gradient communications between clients and an aggregation server during the aggregation process. While traditional encryption-based defenses, such as homomorphic encryption, offer strong privacy guarantees without compromising model utility, they often incur prohibitive computational overheads. To mitigate this, selective encryption has emerged as a promising approach, encrypting only a subset of gradient data based on the data's significance under a certain metric. However, there have been few systematic studies on how to specify this metric in practice. This paper systematically evaluates selective encryption methods with different significance metrics against state-of-the-art attacks. Our findings demonstrate the feasibility of selective encryption in reducing computational overhead while maintaining resilience against attacks. We propose a distance-based significance analysis framework that provides theoretical foundations for selecting critical gradient elements for encryption. Through extensive experiments on different model architectures (LeNet, CNN, BERT, GPT-2) and attack types, we identify gradient magnitude as a generally effective metric for protection against optimization-based gradient inversions. However, we also observe that no single selective encryption strategy is universally optimal across all attack scenarios, and we provide guidelines for choosing appropriate strategies for different model architectures and privacy requirements.

