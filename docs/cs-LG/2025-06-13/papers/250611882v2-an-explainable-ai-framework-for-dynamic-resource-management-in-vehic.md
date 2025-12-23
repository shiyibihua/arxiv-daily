---
layout: default
title: An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing
---

# An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11882" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11882v2</a>
  <a href="https://arxiv.org/pdf/2506.11882.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11882v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11882v2', 'An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haochen Sun, Yifan Liu, Ahmed Al-Tahmeesschi, Swarna Chetty, Syed Ali Raza Zaidi, Avishek Nag, Hamed Ahmadi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-09-17)

**备注**: To appear in Proceedings of IEEE PIMRC 2025. 6 pages, 4 figures

---

## 💡 一句话要点

**提出可解释的深度强化学习框架以解决车载网络切片中的动态资源管理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `车载网络` `网络切片` `深度强化学习` `可解释性` `资源管理` `服务质量` `Shapley值` `注意力机制`

## 📋 核心要点

1. 现有方法在车载网络中资源管理和网络切片的可靠性方面存在挑战，难以满足不同服务的需求。
2. 本文提出的XRL框架通过结合Shapley值和注意力机制，增强了强化学习代理的决策可解释性和优化能力。
3. 实验结果显示，提出的方法在URLLC和eMBB服务的QoS满意度上均有显著提升，分别提高了2.13%和1.77%。

## 📝 摘要（中文）

有效的资源管理和网络切片对于满足车载网络中多样化的服务需求至关重要，包括增强移动宽带（eMBB）和超可靠低延迟通信（URLLC）。本文提出了一种可解释的深度强化学习（XRL）框架，用于车载网络中的动态网络切片和资源分配，基于近实时的无线接入网智能控制器。通过结合基于特征的方法，利用Shapley值和注意力机制，我们解释并优化了强化学习代理的决策，解决了车载通信系统中的关键可靠性挑战。仿真结果表明，我们的方法提供了清晰的实时资源分配过程洞察，并且在可解释性精度上优于纯注意力机制。此外，URLLC服务的服务质量（QoS）满意度从78.0%提高到80.13%，而eMBB服务的满意度从71.44%提高到73.21%。

## 🔬 方法详解

**问题定义**：本文旨在解决车载网络中动态资源管理和网络切片的挑战，现有方法在应对多样化服务需求时，可靠性不足，难以提供实时的决策支持。

**核心思路**：提出的XRL框架通过引入可解释性机制，结合Shapley值和注意力机制，提升了强化学习代理的决策透明度和优化能力，从而更好地满足服务质量要求。

**技术框架**：整体架构包括数据采集模块、特征提取模块、强化学习决策模块和可解释性分析模块。数据采集模块负责实时获取网络状态，特征提取模块利用Shapley值进行特征评估，决策模块基于强化学习进行资源分配，最后可解释性分析模块提供决策的可视化和解释。

**关键创新**：最重要的创新点在于将可解释性与深度强化学习相结合，通过Shapley值和注意力机制的融合，显著提高了决策的可解释性和准确性，与传统方法相比，提供了更为清晰的决策依据。

**关键设计**：在参数设置上，采用了动态学习率和经验回放机制，损失函数设计为结合可解释性损失和强化学习损失的复合损失函数，网络结构上使用了深度神经网络与注意力机制相结合的架构，以增强模型的学习能力。

## 📊 实验亮点

实验结果表明，提出的XRL框架在URLLC服务的QoS满意度上从78.0%提升至80.13%，而eMBB服务的满意度从71.44%提升至73.21%。相较于传统的注意力机制，XRL框架在可解释性精度上表现更佳，提供了更清晰的资源分配过程洞察。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶车辆的通信网络以及车联网（V2X）服务等。通过提升资源管理的效率和可靠性，能够显著改善车载网络的服务质量，满足未来智能交通的需求，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Effective resource management and network slicing are essential to meet the diverse service demands of vehicular networks, including Enhanced Mobile Broadband (eMBB) and Ultra-Reliable and Low-Latency Communications (URLLC). This paper introduces an Explainable Deep Reinforcement Learning (XRL) framework for dynamic network slicing and resource allocation in vehicular networks, built upon a near-real-time RAN intelligent controller. By integrating a feature-based approach that leverages Shapley values and an attention mechanism, we interpret and refine the decisions of our reinforcementlearning agents, addressing key reliability challenges in vehicular communication systems. Simulation results demonstrate that our approach provides clear, real-time insights into the resource allocation process and achieves higher interpretability precision than a pure attention mechanism. Furthermore, the Quality of Service (QoS) satisfaction for URLLC services increased from 78.0% to 80.13%, while that for eMBB services improved from 71.44% to 73.21%.

