---
layout: default
title: Privacy-Preserving Offloading for Large Language Models in 6G Vehicular Networks
---

# Privacy-Preserving Offloading for Large Language Models in 6G Vehicular Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05320" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05320v1</a>
  <a href="https://arxiv.org/pdf/2509.05320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05320v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05320v1', 'Privacy-Preserving Offloading for Large Language Models in 6G Vehicular Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ikhlasse Badidi, Nouhaila El Khiyaoui, Aya Riany, Badr Ben Elallid, Amine Abouaomar

**分类**: cs.CR, cs.LG

**发布日期**: 2025-08-30

**备注**: 7 pages, 6 figures, 1 algorithm, 5 equations

---

## 💡 一句话要点

**提出隐私保护的卸载框架以解决6G车联网中的数据安全问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `大型语言模型` `车联网` `联邦学习` `差分隐私` `智能交通` `边缘计算`

## 📋 核心要点

1. 现有方法在将大型语言模型计算卸载到边缘时，面临用户数据隐私泄露的重大风险。
2. 本文提出了一种结合联邦学习和差分隐私的混合方法，以保护用户数据并优化计算效率。
3. 实验结果显示，该框架在保持高准确率的同时，通信开销和计算效率均表现良好。

## 📝 摘要（中文）

大型语言模型（LLM）在6G车联网中的集成为智能交通系统带来了前所未有的进步。然而，将LLM计算从车辆卸载到边缘基础设施会带来显著的隐私风险，可能暴露敏感用户数据。本文提出了一种新颖的隐私保护卸载框架，结合了联邦学习（FL）和差分隐私（DP）技术，以保护用户数据并保持LLM性能。框架包括一个隐私感知的任务划分算法，优化了本地和边缘计算之间的权衡，同时考虑隐私约束和系统效率。实验结果表明，该方法在全球准确率上达到75%，与非隐私保护方法相比仅降低2-3%，同时保持DP保证，隐私预算为ε=0.8。该框架在每轮的通信开销约为2.1MB，计算占总处理时间的90%以上，验证了其在资源受限的车载环境中的效率。

## 🔬 方法详解

**问题定义**：本文旨在解决在6G车联网中将大型语言模型计算卸载到边缘时，用户数据隐私泄露的问题。现有方法往往忽视了隐私保护，导致敏感数据暴露的风险增大。

**核心思路**：论文提出的核心思路是结合联邦学习和差分隐私技术，通过隐私感知的任务划分算法，优化本地与边缘计算之间的平衡，从而在保护隐私的同时保持模型性能。

**技术框架**：整体架构包括数据收集、任务划分、模型训练和结果聚合四个主要模块。首先，车辆收集数据并进行本地计算，然后通过隐私感知算法决定哪些任务卸载到边缘，最后通过安全通信协议传输模型更新和聚合结果。

**关键创新**：最重要的技术创新在于提出了一种新的任务划分算法，能够在隐私保护和系统效率之间实现最佳权衡。这一方法与传统的集中式计算方式有本质区别，能够有效降低隐私风险。

**关键设计**：在设计中，设置了隐私预算ε=0.8，确保差分隐私的保证。同时，框架的通信开销稳定在约2.1MB每轮，计算时间占总处理时间的90%以上，显示出在资源受限环境中的高效性。

## 📊 实验亮点

实验结果表明，提出的框架在全球准确率上达到75%，与非隐私保护方法相比仅降低2-3%。同时，保持了差分隐私的保证，隐私预算为ε=0.8，显示出良好的性能和效率。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶车辆和车联网服务等。通过保护用户隐私，该框架能够促进更广泛的LLM应用，提升用户信任度，并推动智能交通技术的进一步发展。未来，该技术可能在数据安全和隐私保护方面产生深远影响。

## 📄 摘要（原文）

> The integration of Large Language Models (LLMs) in 6G vehicular networks promises unprecedented advancements in intelligent transportation systems. However, offloading LLM computations from vehicles to edge infrastructure poses significant privacy risks, potentially exposing sensitive user data. This paper presents a novel privacy-preserving offloading framework for LLM-integrated vehicular networks. We introduce a hybrid approach combining federated learning (FL) and differential privacy (DP) techniques to protect user data while maintaining LLM performance. Our framework includes a privacy-aware task partitioning algorithm that optimizes the trade-off between local and edge computation, considering both privacy constraints and system efficiency. We also propose a secure communication protocol for transmitting model updates and aggregating results across the network. Experimental results demonstrate that our approach achieves 75\% global accuracy with only a 2-3\% reduction compared to non-privacy-preserving methods, while maintaining DP guarantees with an optimal privacy budget of $\varepsilon = 0.8$. The framework shows stable communication overhead of approximately 2.1MB per round with computation comprising over 90\% of total processing time, validating its efficiency for resource-constrained vehicular environments.

