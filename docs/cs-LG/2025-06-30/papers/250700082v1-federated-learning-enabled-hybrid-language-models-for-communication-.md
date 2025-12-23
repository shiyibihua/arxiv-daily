---
layout: default
title: Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission
---

# Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00082" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00082v1</a>
  <a href="https://arxiv.org/pdf/2507.00082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00082v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00082v1', 'Federated Learning-Enabled Hybrid Language Models for Communication-Efficient Token Transmission')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Faranaksadat Solat, Joohyung Lee, Mohamed Seif, Dusit Niyato, H. Vincent Poor

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-30

**备注**: 17 pages, 16 figures, IEEE Internet of Things

---

## 💡 一句话要点

**提出FedHLM以解决边缘设备通信效率低的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合语言模型` `联邦学习` `不确定性感知` `边缘计算` `通信效率` `低延迟推理` `令牌传输` `智能助手`

## 📋 核心要点

1. 现有的混合语言模型在低置信度预测时频繁卸载到大型语言模型，导致通信开销显著，尤其在带宽受限的环境中。
2. 本文提出FedHLM框架，通过联邦学习优化令牌级不确定性阈值，减少不必要的LLM调用，从而提高通信效率。
3. 实验结果显示，FedHLM在大规模新闻分类任务中将LLM传输减少超过95%，且准确性损失极小，验证了其有效性。

## 📝 摘要（中文）

混合语言模型（HLMs）结合了小型语言模型（SLMs）在边缘设备上的低延迟效率与大型语言模型（LLMs）在集中式服务器上的高准确性。与传统的端到端LLM推理不同，HLMs仅在本地SLM预测不确定时调用LLM，从而减少延迟和通信。然而，模糊或低置信度的预测仍需频繁卸载到LLM，导致在带宽受限环境下的通信开销显著。为此，本文提出了FedHLM，一个集成不确定性感知推理与联邦学习（FL）的通信高效HLM框架。FedHLM的关键创新在于协作学习决定何时需要LLM协助的令牌级不确定性阈值。通过FL优化这些阈值，FedHLM在保护隐私的同时实现了分布式学习。此外，FedHLM利用基于嵌入的令牌表示进行点对点（P2P）解析，使客户端能够重用语义相似的同伴推断的令牌，而无需调用LLM。实验表明，FedHLM在大规模新闻分类任务中将LLM传输减少了95%以上，且准确性损失微乎其微，适合可扩展的高效边缘AI应用。

## 🔬 方法详解

**问题定义**：本文旨在解决混合语言模型在低置信度预测时频繁卸载到大型语言模型所带来的通信开销问题，尤其是在带宽受限的环境中。

**核心思路**：FedHLM框架通过联邦学习优化令牌级不确定性阈值，确保仅在必要时调用LLM，从而减少通信负担。

**技术框架**：FedHLM的整体架构包括不确定性感知推理模块、联邦学习模块和基于嵌入的令牌表示模块。通过这些模块的协同工作，FedHLM能够高效地管理LLM的调用。

**关键创新**：FedHLM的主要创新在于通过联邦学习动态优化不确定性阈值，而非使用静态或手动调节的阈值，这使得模型在不同环境下具有更好的适应性。

**关键设计**：在设计中，FedHLM采用了基于嵌入的令牌表示，以支持点对点解析，同时引入了层次模型聚合机制，确保边缘服务器通过客户端更新优化本地路由策略。

## 📊 实验亮点

实验结果表明，FedHLM在大规模新闻分类任务中将LLM的传输量减少了超过95%，同时保持了几乎无损的准确性。这一显著的性能提升展示了FedHLM在边缘AI应用中的有效性和实用性。

## 🎯 应用场景

FedHLM框架具有广泛的应用潜力，特别是在需要高效通信的边缘计算环境中，如智能手机、物联网设备和边缘服务器等。其高效的通信机制和低延迟特性使其适合于实时语言处理和智能助手等应用场景，未来可能推动边缘AI技术的进一步发展。

## 📄 摘要（原文）

> Hybrid Language Models (HLMs) combine the low-latency efficiency of Small Language Models (SLMs) on edge devices with the high accuracy of Large Language Models (LLMs) on centralized servers. Unlike traditional end-to-end LLM inference, HLMs reduce latency and communication by invoking LLMs only when local SLM predictions are uncertain, i.e., when token-level confidence is low or entropy is high. However, ambiguous or low-confidence predictions still require frequent offloading to the LLM, leading to significant communication overhead in bandwidth-constrained settings. To address this, we propose FedHLM, a communication-efficient HLM framework that integrates uncertainty-aware inference with Federated Learning (FL). FedHLM's key innovation lies in collaboratively learning token-level uncertainty thresholds that govern when LLM assistance is needed. Rather than using static or manually tuned thresholds, FedHLM employs FL to optimize these thresholds in a privacy-preserving, distributed manner. Additionally, it leverages embedding-based token representations for Peer-to-Peer (P2P) resolution, enabling clients to reuse tokens inferred by semantically similar peers without engaging the LLM. We further introduce hierarchical model aggregation: edge servers refine local routing policies through client updates, while cross-cluster coordination aligns global decision boundaries. This layered design captures recurring uncertainty patterns, reducing redundant LLM queries. Experiments on large-scale news classification tasks show that FedHLM reduces LLM transmissions by over 95 percent with negligible accuracy loss, making it well-suited for scalable and efficient edge-AI applications.

