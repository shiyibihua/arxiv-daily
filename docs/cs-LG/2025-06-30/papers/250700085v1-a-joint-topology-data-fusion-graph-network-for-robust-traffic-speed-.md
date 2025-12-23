---
layout: default
title: A Joint Topology-Data Fusion Graph Network for Robust Traffic Speed Prediction with Data Anomalism
---

# A Joint Topology-Data Fusion Graph Network for Robust Traffic Speed Prediction with Data Anomalism

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00085" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00085v1</a>
  <a href="https://arxiv.org/pdf/2507.00085.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00085v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00085v1', 'A Joint Topology-Data Fusion Graph Network for Robust Traffic Speed Prediction with Data Anomalism')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiyuan Jiang, Dongyao Jia, Eng Gee Lim, Pengfei Fan, Yuli Zhang, Shangbo Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出GFEN以解决交通速度预测中的数据异常问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `交通速度预测` `图融合` `深度学习` `数据异常` `智能交通系统` `时空特征` `非平稳性` `鲁棒性`

## 📋 核心要点

1. 现有交通速度预测方法在处理复杂的交通动态和数据异常时表现不佳，难以有效整合空间和时间特征。
2. 本文提出的GFEN框架通过图融合技术提取和融合时空相关性，结合深度学习结构自适应处理历史数据异常。
3. 实验结果显示GFEN在预测准确性上提升约6.3%，收敛速度几乎是现有混合模型的两倍，验证了其优越性。

## 📝 摘要（中文）

准确的交通预测对智能交通系统（ITS）至关重要，但现有方法在处理交通动态的复杂性和非线性时面临挑战，难以有效整合空间和时间特征。此外，现有方法使用静态技术来处理非平稳和异常的历史数据，限制了适应性并削弱了数据平滑性。为此，本文提出了一种创新的图融合增强网络（GFEN），该框架通过可训练的方法精确提取和融合数据分布和网络拓扑中的空间和时间相关性，从而建模多尺度的时空特征。GFEN还结合了基于k阶差分的数学框架与基于注意力的深度学习结构，以自适应平滑历史观测并动态减轻数据异常和非平稳性。实验结果表明，GFEN在预测准确性上超越了最先进的方法约6.3%，并且收敛速度几乎是最近混合模型的两倍，确认了其优越性能和显著提升交通预测系统效率的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决交通速度预测中的数据异常和非平稳性问题。现有方法多采用静态技术，难以适应动态变化的交通环境，导致预测效果不佳。

**核心思路**：GFEN框架通过引入图融合技术，能够动态提取和融合空间与时间特征，适应交通数据的非平稳性和异常情况，从而提高预测的准确性和鲁棒性。

**技术框架**：GFEN的整体架构包括数据预处理模块、图融合模块和预测模块。数据预处理模块负责清洗和准备输入数据，图融合模块通过可训练的方式提取时空特征，预测模块则基于深度学习结构进行最终的速度预测。

**关键创新**：GFEN的主要创新在于其独特的时空图融合技术，能够同时考虑数据分布和网络拓扑的影响，这与传统方法的静态处理方式形成鲜明对比。

**关键设计**：GFEN采用了基于k阶差分的数学框架来处理历史数据，并结合注意力机制来动态调整模型的关注点，确保模型在面对数据异常时仍能保持良好的预测性能。损失函数设计上，考虑了预测误差的加权，以提高模型的鲁棒性。

## 📊 实验亮点

GFEN在实验中表现出色，预测准确性提升约6.3%，并且收敛速度几乎是现有混合模型的两倍。这些结果表明GFEN在处理交通速度预测中的数据异常和非平稳性方面具有显著优势，验证了其在智能交通系统中的应用潜力。

## 🎯 应用场景

GFEN框架在智能交通系统中具有广泛的应用潜力，能够有效提升交通速度预测的准确性和可靠性。这一研究成果不仅有助于优化交通管理和调度，还能为智能交通系统的决策支持提供更为精准的数据基础，推动智能城市的发展。未来，GFEN的技术可以扩展到其他领域，如物流管理和城市规划等，具有重要的实际价值和影响力。

## 📄 摘要（原文）

> Accurate traffic prediction is essential for Intelligent Transportation Systems (ITS), yet current methods struggle with the inherent complexity and non-linearity of traffic dynamics, making it difficult to integrate spatial and temporal characteristics. Furthermore, existing approaches use static techniques to address non-stationary and anomalous historical data, which limits adaptability and undermines data smoothing. To overcome these challenges, we propose the Graph Fusion Enhanced Network (GFEN), an innovative framework for network-level traffic speed prediction. GFEN introduces a novel topological spatiotemporal graph fusion technique that meticulously extracts and merges spatial and temporal correlations from both data distribution and network topology using trainable methods, enabling the modeling of multi-scale spatiotemporal features. Additionally, GFEN employs a hybrid methodology combining a k-th order difference-based mathematical framework with an attention-based deep learning structure to adaptively smooth historical observations and dynamically mitigate data anomalies and non-stationarity. Extensive experiments demonstrate that GFEN surpasses state-of-the-art methods by approximately 6.3% in prediction accuracy and exhibits convergence rates nearly twice as fast as recent hybrid models, confirming its superior performance and potential to significantly enhance traffic prediction system efficiency.

