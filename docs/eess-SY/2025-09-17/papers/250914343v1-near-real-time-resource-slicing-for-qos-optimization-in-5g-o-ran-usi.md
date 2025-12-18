---
layout: default
title: Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN using Deep Reinforcement Learning
---

# Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN using Deep Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14343" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14343v1</a>
  <a href="https://arxiv.org/pdf/2509.14343.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14343v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14343v1', 'Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN using Deep Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peihao Yan, Jie Lu, Huacheng Zeng, Y. Thomas Hou

**分类**: eess.SY, cs.AI

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出xSlice，利用深度强化学习优化5G O-RAN中近实时资源切片，提升QoS。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `O-RAN` `资源切片` `深度强化学习` `图卷积网络` `QoS优化` `近实时控制` `无线资源管理`

## 📋 核心要点

1. 现有5G O-RAN资源分配方法难以适应无线信道、用户移动和流量波动的动态变化，导致QoS下降。
2. xSlice采用深度强化学习框架，结合Actor-Critic模型和图卷积网络，实现对MAC层资源的自适应调整。
3. 实验结果表明，xSlice在实际场景中能够显著降低性能遗憾，相比现有方法降低了67%。

## 📝 摘要（中文）

本文提出了一种名为xSlice的xApp，用于5G O-RAN的近实时（Near-RT）RAN智能控制器（RIC）。xSlice是一种在线学习算法，能够自适应地调整MAC层资源分配，以应对动态网络状态，包括时变的无线信道条件、用户移动性、流量波动以及用户需求的变化。为了应对这些网络动态，我们首先将服务质量（QoS）优化问题建模为一个遗憾最小化问题，通过加权吞吐量、延迟和可靠性来量化所有流量会话的QoS需求。然后，我们开发了一个深度强化学习（DRL）框架，该框架利用actor-critic模型来结合基于价值和基于策略的更新方法的优点。图卷积网络（GCN）被整合为DRL框架的一个组件，用于RAN数据的图嵌入，使xSlice能够处理动态数量的流量会话。我们在一个包含10部智能手机的O-RAN测试平台上实现了xSlice，并进行了广泛的实验，以评估其在实际场景中的性能。实验结果表明，与最先进的解决方案相比，xSlice可以将性能遗憾降低67%。源代码可在GitHub上找到。

## 🔬 方法详解

**问题定义**：论文旨在解决5G O-RAN中动态网络环境下，如何优化MAC层资源分配以满足不同流量会话的QoS需求，包括吞吐量、延迟和可靠性。现有方法难以有效应对无线信道条件、用户移动性、流量波动等带来的挑战，导致QoS性能下降。

**核心思路**：论文的核心思路是将QoS优化问题建模为遗憾最小化问题，并利用深度强化学习（DRL）方法在线学习最优的资源分配策略。通过actor-critic模型结合价值和策略迭代的优点，加速学习过程并提高策略的稳定性。同时，利用图卷积网络（GCN）处理动态变化的流量会话数量，实现对RAN数据的有效嵌入。

**技术框架**：xSlice的整体框架包含以下几个主要模块：首先，通过O-RAN的RIC收集RAN数据，包括信道状态信息、用户位置、流量需求等。然后，利用GCN对RAN数据进行图嵌入，提取特征。接着，actor网络根据嵌入的特征输出资源分配策略，critic网络评估该策略的价值。最后，利用DRL算法更新actor和critic网络的参数，不断优化资源分配策略。

**关键创新**：论文的关键创新在于将GCN与DRL相结合，用于解决O-RAN中动态资源分配问题。GCN能够有效处理动态变化的流量会话数量，提取RAN数据的拓扑信息，而DRL能够在线学习最优的资源分配策略，无需预先建模复杂的网络环境。这种结合使得xSlice能够自适应地应对各种网络动态，实现QoS优化。

**关键设计**：论文中，actor网络和critic网络均采用深度神经网络结构。GCN的输入是RAN数据的邻接矩阵和节点特征，输出是节点的嵌入向量。损失函数采用actor-critic算法中的策略梯度损失和价值函数损失。具体参数设置（如学习率、折扣因子等）在论文中有详细描述。状态空间包括信道质量指示（CQI）、用户速率需求等，动作空间为资源块（RB）分配比例。

## 📊 实验亮点

实验结果表明，xSlice在实际O-RAN测试平台上，与最先进的资源分配方案相比，能够将性能遗憾降低67%。该结果验证了xSlice在动态网络环境下，能够有效提升QoS性能，并自适应地应对各种网络变化。

## 🎯 应用场景

xSlice可应用于5G及未来无线通信系统的O-RAN架构中，实现智能化的资源管理和QoS保障。该研究成果有助于提升网络性能、改善用户体验，并为运营商提供更灵活、高效的网络运营手段。未来可扩展到其他无线接入技术和应用场景，例如工业物联网、车联网等。

## 📄 摘要（原文）

> Open-Radio Access Network (O-RAN) has become an important paradigm for 5G and beyond radio access networks. This paper presents an xApp called xSlice for the Near-Real-Time (Near-RT) RAN Intelligent Controller (RIC) of 5G O-RANs. xSlice is an online learning algorithm that adaptively adjusts MAC-layer resource allocation in response to dynamic network states, including time-varying wireless channel conditions, user mobility, traffic fluctuations, and changes in user demand. To address these network dynamics, we first formulate the Quality-of-Service (QoS) optimization problem as a regret minimization problem by quantifying the QoS demands of all traffic sessions through weighting their throughput, latency, and reliability. We then develop a deep reinforcement learning (DRL) framework that utilizes an actor-critic model to combine the advantages of both value-based and policy-based updating methods. A graph convolutional network (GCN) is incorporated as a component of the DRL framework for graph embedding of RAN data, enabling xSlice to handle a dynamic number of traffic sessions. We have implemented xSlice on an O-RAN testbed with 10 smartphones and conducted extensive experiments to evaluate its performance in realistic scenarios. Experimental results show that xSlice can reduce performance regret by 67% compared to the state-of-the-art solutions. Source code is available on GitHub [1].

