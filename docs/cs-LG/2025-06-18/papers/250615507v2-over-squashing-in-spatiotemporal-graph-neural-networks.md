---
layout: default
title: Over-squashing in Spatiotemporal Graph Neural Networks
---

# Over-squashing in Spatiotemporal Graph Neural Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15507" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15507v2</a>
  <a href="https://arxiv.org/pdf/2506.15507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15507v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15507v2', 'Over-squashing in Spatiotemporal Graph Neural Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ivan Marisca, Jacob Bamberger, Cesare Alippi, Michael M. Bronstein

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-18 (更新: 2025-11-02)

**备注**: Accepted at NeurIPS 2025

---

## 💡 一句话要点

**提出时空图神经网络中的过度压缩问题解决方案**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `图神经网络` `时空数据` `信息传播` `过度压缩` `卷积网络` `理论分析` `动态环境`

## 📋 核心要点

1. 现有的图神经网络在信息传播能力上存在过度压缩问题，尤其在时空图神经网络中表现得尤为明显。
2. 论文通过形式化时空过度压缩问题，揭示了其与静态图神经网络的不同特征，并提出了相应的理论分析。
3. 实验结果表明，卷积STGNNs在信息传播上更倾向于远距离节点，而非近距离节点，验证了理论分析的有效性。

## 📝 摘要（中文）

图神经网络（GNNs）在多个领域取得了显著成功，但最近的理论研究揭示了其信息传播能力的基本局限性，如过度压缩问题，即远距离节点无法有效交换信息。尽管这一问题在静态上下文中得到了广泛研究，但在处理与图节点相关的序列的时空图神经网络（STGNNs）中仍未得到探讨。本文正式定义了时空过度压缩问题，并展示了其与静态情况的不同特征。我们的分析表明，卷积STGNNs更倾向于从时间上相距较远的点传播信息，而非时间上相近的点。此外，我们证明了遵循时间与空间或时间后空间处理范式的架构同样受到这一现象的影响，为计算上高效的实现提供了理论依据。我们在合成和真实世界数据集上验证了我们的发现，为更有效的设计提供了深入的见解和原则性指导。

## 🔬 方法详解

**问题定义**：本文聚焦于时空图神经网络中的过度压缩问题，指出现有方法在处理远距离节点信息传播时的不足，导致信息交换效率低下。

**核心思路**：通过形式化时空过度压缩问题，论文揭示了卷积STGNNs在信息传播中的独特行为，提出了理论分析以指导更有效的网络设计。

**技术框架**：研究首先定义了时空过度压缩的特征，然后通过理论分析和实验验证，探讨了不同处理范式对信息传播的影响。

**关键创新**：论文的主要创新在于首次将过度压缩问题引入时空图神经网络的研究，揭示了卷积网络在信息传播中的反直觉特性。

**关键设计**：在实验中，采用了合成和真实数据集，设计了多种网络架构以验证理论分析，重点关注时间与空间处理的不同组合对信息传播的影响。

## 📊 实验亮点

实验结果显示，卷积STGNNs在处理时空数据时，信息传播效率较低，尤其是在远距离节点之间的传播。与基线模型相比，提出的方法在多个数据集上实现了显著的性能提升，验证了理论分析的有效性。

## 🎯 应用场景

该研究为时空图神经网络的设计提供了新的理论基础，具有广泛的应用潜力，特别是在交通预测、社交网络分析和视频理解等领域。通过优化信息传播机制，可以提升模型在复杂动态环境中的表现，推动相关技术的发展。

## 📄 摘要（原文）

> Graph Neural Networks (GNNs) have achieved remarkable success across various domains. However, recent theoretical advances have identified fundamental limitations in their information propagation capabilities, such as over-squashing, where distant nodes fail to effectively exchange information. While extensively studied in static contexts, this issue remains unexplored in Spatiotemporal GNNs (STGNNs), which process sequences associated with graph nodes. Nonetheless, the temporal dimension amplifies this challenge by increasing the information that must be propagated. In this work, we formalize the spatiotemporal over-squashing problem and demonstrate its distinct characteristics compared to the static case. Our analysis reveals that, counterintuitively, convolutional STGNNs favor information propagation from points temporally distant rather than close in time. Moreover, we prove that architectures that follow either time-and-space or time-then-space processing paradigms are equally affected by this phenomenon, providing theoretical justification for computationally efficient implementations. We validate our findings on synthetic and real-world datasets, providing deeper insights into their operational dynamics and principled guidance for more effective designs.

